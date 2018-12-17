# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""The details of the configuration options for OAI-PMH server."""

import pkg_resources

OAISERVER_PAGE_SIZE = 10
"""Define maximum length of list responses.

Request with verbs ``ListRecords``, ``ListIdentifiers``, and ``ListSets``
are affected by this option.
"""

OAISERVER_RECORD_INDEX = 'records'
"""Specify an Elastic index with records that should be exposed via OAI-PMH."""

# The version of the OAI-PMH supported by the repository.
OAISERVER_PROTOCOL_VERSION = '2.0'

OAISERVER_ADMIN_EMAILS = [
    'info@inveniosoftware.org',
]
"""The e-mail addresses of administrators of the repository.

It **must** include one or more instances.
"""

# TODO Add support for compressions.
OAISERVER_COMPRESSIONS = [
    'identity',
]

OAISERVER_GRANULARITY = 'YYYY-MM-DDThh:mm:ssZ'
"""The finest harvesting granularity supported by the repository.

The legitimate values are ``YYYY-MM-DD`` and ``YYYY-MM-DDThh:mm:ssZ``
with meanings as defined in ISO8601.
"""

OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME = 1 * 60
"""The expiration time of a resumption token in seconds.

**Default: 60 seconds = 1 minute**.

.. note::

    Setting longer expiration time may have a negative impact on your
    Elasticsearch cluster as it might need to keep open cursors.

    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html
"""

OAISERVER_METADATA_FORMATS = {
    'oai_dc': {
        'serializer': (
            'invenio_oaiserver.utils:dumps_etree', {
                'xslt_filename': pkg_resources.resource_filename(
                    'invenio_oaiserver', 'static/xsl/MARC21slim2OAIDC.xsl'
                ),
            }
        ),
        'schema': 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
        'namespace': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    },
    'marc21': {
        'serializer': (
            'invenio_oaiserver.utils:dumps_etree', {
                'prefix': 'marc',
            }
        ),
        'schema': 'http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd',
        'namespace': 'http://www.loc.gov/MARC21/slim',
    }
}
"""Define the metadata formats available from a repository.

Every key represents a ``metadataPrefix`` and its value has a following
structure.

* ``schema`` - the location of an XML Schema describing the format;
* ``namespace`` - the namespace of serialized document;
* ``serializer`` - the importable string or tuple with the importable string
  and keyword arguments.

.. note::

    If you are migrating an instance running older versions of Invenio<=2.1,
    you might want to copy settings from ``'marc21'`` key to ``'marcxml'``
    in order to ensure compatibility for all your OAI-PMH clients.

"""

OAISERVER_REGISTER_RECORD_SIGNALS = True
"""Catch record/set insert/update/delete signals and update the `_oai`
field."""

OAISERVER_REGISTER_SET_SIGNALS = True
"""Catch set insert/update/delete signals and update the `_oai` record
field."""

OAISERVER_QUERY_PARSER = 'elasticsearch_dsl:Q'
"""Define query parser for OIASet definition."""

OAISERVER_CACHE_KEY = 'DynamicOAISets::'
"""Key prefix added before all keys in cache server."""

OAISERVER_CELERY_TASK_CHUNK_SIZE = 100
"""Specify the maximum number of records each task will update."""

OAISERVER_CONTROL_NUMBER_FETCHER = 'recid'
"""PIDStore fetcher for the OAI ID control number."""

OAISERVER_DESCRIPTIONS = []
"""Specify the optional description containers that can be used to express
properties of the repository that are not covered by the standard response
to the Identify verb.
For further information see:
http://www.openarchives.org/OAI/2.0/guidelines.htm

The `eprints`, `oai_identifier` and `friends` description can be added using
the helper functions in utils.py as follows:

.. code-block:: python

    from invenio_oaiserver.utils import eprints_description
    from invenio_oaiserver.utils import friends_description
    from invenio_oaiserver.utils import oai_identifier_description

    OAISERVER_DESCRIPTIONS = [
        eprints_description(metadataPolicy, dataPolicy,
                            submissionPolicy, content),
        oai_identifier_description(scheme, repositoryIdentifier,
                                   delimiter, sampleIdentifier),
        friends_description(baseUrls)
    ]

The parameters of each description element are strings if their type is unique
or dictionaries, with the type being the key, if it can differ.
E.g. the dataPolicy of the eprints element can consist of a
text and or URL so it will have the form:

.. code-block:: python

    metadataPolicy = {'text': 'Metadata can be used by commercial'
                      'and non-commercial service providers',
                      'URL': 'http://arXiv.org/arXiv_metadata_use.htm'}

Whereas for the scheme of the oai_identifier it will just be:

.. code-block:: python

    scheme = 'oai'

If the parameter can take an arbitrary amount of elements it can be a list:

.. code-block:: python

    baseUrls = [http://oai.east.org/foo/,
                http://oai.hq.org/bar/,
                http://oai.south.org/repo.cgi]

"""

OAISERVER_XSL_URL = None
"""Specify the url (relative or absolute) to the XML Stylesheet file to
transform XML OAI 2.0 responses into XHTML.

The url can be a relative path to a local static file:

.. code-block:: python

    OAISERVER_XSL_URL = '/static/xsl/oai2.xsl'

or an absolute url to a remote file (be aware of CORS restrictions):

.. code-block:: python

    OAISERVER_XSL_URL = 'https//www.otherdomain.org/oai2.xsl'

You can obtain an already defined XSL Stylesheet for OAIS 2.0 on `EPrints
repository
<https://raw.githubusercontent.com/eprints/eprints/3.3/lib/static/oai2.xsl>`_
(GPLv3 licensed).
"""
