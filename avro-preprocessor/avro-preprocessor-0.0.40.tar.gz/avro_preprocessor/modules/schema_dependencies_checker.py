"""
A module to analyze schema dependencies in a path
"""

from collections import OrderedDict
from typing import Optional

import networkx as nx

from avro_preprocessor.avro_domain import Avro
from avro_preprocessor.preprocessor_module import PreprocessorModule
from avro_preprocessor.schemas_container import SchemasContainer

__author__ = "Nicola Bova"
__copyright__ = "Copyright 2018, Jaumo GmbH"
__email__ = "nicola.bova@jaumo.com"


class SchemaDependenciesChecker(PreprocessorModule):
    """
    Checks schema dependencies - exception thrown if it detects cycles.
    """
    def __init__(self, schemas: SchemasContainer):
        super().__init__(schemas)

        self.record_dependencies: OrderedDict = OrderedDict()
        self.record_dependencies_graph = nx.DiGraph()

        self.current_schema_fully_qualified_name: Optional[str] = None

    def process(self) -> None:
        """Process all schemas."""
        self.find_dependencies()

    def find_dependencies(self) -> None:
        """Detects all dependencies among schemas."""
        for _, schema in self.processed_schemas_iter():
            self.find_dependencies_in_schema(schema)

        dependencies = {record: nx.descendants(self.record_dependencies_graph, record)
                        for record in self.record_dependencies_graph}

        self.record_dependencies = \
            OrderedDict(sorted(dependencies.items(), key=lambda kv: len(kv[1])))

        if self.schemas.verbose:
            for record, dependencies in self.record_dependencies.items():
                print('# deps:', len(dependencies), record, dependencies)

        # let's assert there are no cycles
        try:
            nx.find_cycle(self.record_dependencies_graph)
            raise ValueError("The supplied list of schemas contains cyclic dependencies!")
        except nx.exception.NetworkXNoCycle:
            pass  # the is the expected outcome. No cycles should be found.

    def find_dependencies_in_schema(self, schema: OrderedDict) -> None:
        """
        Detects dependencies for a schema.
        :param schema: The schema
        """
        self.current_schema_fully_qualified_name = \
            '.'.join((schema[Avro.Namespace], schema.get(Avro.Name, schema.get(Avro.Protocol))))
        self.record_dependencies_graph.add_node(self.current_schema_fully_qualified_name)

        self.traverse_schema(schema, self.store_dependencies_of_field)

    def store_dependencies_of_field(self, field: OrderedDict) -> None:
        """
        Store dependencies of other records in a field in a private dict
        :param field: The input field
        """

        # subschemas (or rather avro types) can be referenced in Avro.Type or Avro.Items fields
        type_and_items = [field[t] for t in [Avro.Type, Avro.Items] if t in field]

        for sub_field in type_and_items:
            if isinstance(sub_field, str):
                if '.' in sub_field:
                    self.record_dependencies_graph.add_edge(
                        self.current_schema_fully_qualified_name, sub_field)
