#!/usr/bin/env python3
"""
Script transforming Extended Avro (.exavsc) to regular Avro (.avsc) schema files.
Extends Avro schema definition with 'nullable_optional' keyword.
"""
from collections import OrderedDict
from typing import List, Optional

from avro_preprocessor.avro_paths import AvroPaths
from avro_preprocessor.colored_json import ColoredJson
from avro_preprocessor.modules.avro_sorter import AvroSorter, AvroOrderChecker
from avro_preprocessor.modules.documentation_checker import DocumentationChecker
from avro_preprocessor.modules.documentation_list_condenser import DocumentationCondenser
from avro_preprocessor.modules.java_classes_creator import JavaClassesCreator
from avro_preprocessor.modules.keys_generator import KeysGenerator
from avro_preprocessor.modules.metadata_adder import MetadataAdder
from avro_preprocessor.modules.names_checker import NamesChecker
from avro_preprocessor.modules.namespace_checker import NamespaceChecker
from avro_preprocessor.modules.nullable_optional_expander import NullableOptionalExpander
from avro_preprocessor.modules.references_expander import ReferencesExpander
from avro_preprocessor.modules.schema_dependencies_checker import SchemaDependenciesChecker
from avro_preprocessor.modules.schema_mapping_generator import SchemaMappingGenerator
from avro_preprocessor.modules.schema_registrar import SchemaRegistrar
from avro_preprocessor.modules.schema_registry_checker import SchemaRegistryChecker
from avro_preprocessor.preprocessor_module import PreprocessorModule
from avro_preprocessor.schemas_container import SchemasContainer

__author__ = "Nicola Bova"
__copyright__ = "Copyright 2018, Jaumo GmbH"
__email__ = "nicola.bova@jaumo.com"


class AvroPreprocessor:
    """
    Avro extender main class.
    """

    #: When adding a module, add it here to make it available
    preprocessing_modules = [
        DocumentationCondenser,
        NamespaceChecker,
        DocumentationChecker,
        NamesChecker,
        AvroOrderChecker,
        MetadataAdder,
        SchemaDependenciesChecker,
        NullableOptionalExpander,
        ReferencesExpander,
        AvroSorter,
        KeysGenerator,
        SchemaMappingGenerator,
        JavaClassesCreator,
        SchemaRegistryChecker,
        SchemaRegistrar
    ]

    #: OrderedDict of module_name -> module_class
    available_preprocessing_modules = OrderedDict((
        (m.__name__, m) for m in preprocessing_modules
    ))

    def __init__(self,
                 paths: AvroPaths,
                 verbose: bool = True,
                 json_indent: int = 4,
                 schema_registry_url: str = 'http://localhost:8081') -> None:
        """
        Initialization function.

        :param paths: The paths of the input and output directories
        :param verbose: Verbose flag
        :param json_indent: How much to indent JSON strings
        :param schema_registry_url: The URL of the Confluent Schema Registry
        """
        self.paths = paths
        ColoredJson.json_indent = json_indent
        SchemaRegistrar.schema_registry_url = schema_registry_url

        self.schemas: SchemasContainer = SchemasContainer(self.paths, verbose)

    def process(self, requested_modules: Optional[List[str]] = None) -> None:
        """
        Process all the schemas using the modules pipeline.
        Standard schemas are saved in .avsc
        (or whatever set by the output_schema_file_extension parameter)
        files in the output path.

        :param requested_modules: The modules to activate, all available ones if set to None
        """

        self.schemas.read_schemas()

        for module in self.get_requested_modules(requested_modules):
            # self.schemas.print_schemas('json')
            try:
                module.process()
            except Exception as exc:
                print('\n', "*" * 100, "\nException while processing schema:",
                      module.current_schema_name, '\n', "*" * 100)
                raise exc

        self.schemas.write_schemas()

    def get_requested_modules(self, requested_modules_names: Optional[List[str]])\
            -> List[PreprocessorModule]:
        """
        Process the requested modules creating an instance of each of them.

        :param requested_modules_names: The names of the requested modules
        :return: List of modules
        """

        if requested_modules_names:
            for module in requested_modules_names:
                if module not in self.available_preprocessing_modules:
                    raise ValueError("No such module {}".format(module))
            requested_modules_names_checked = requested_modules_names
        else:
            requested_modules_names_checked = list(self.available_preprocessing_modules)

        return [
            self.available_preprocessing_modules[module](self.schemas)  # type: ignore
            for module in self.available_preprocessing_modules
            if module in requested_modules_names_checked
        ]
