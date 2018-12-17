# (c) 2017, XYSec Labs

from collections import namedtuple


def mapper_json_api(model: type, resource: dict) -> object:
    """
    Returns an obj of type `model` from dictified JSON `resource` for JSON APIs
    """
    attr = dict()
    for field in model._fields:
        if field == 'id':
            attr[field] = resource['data']['id']
        else:
            attr[field] = resource['data']['attributes'][
                field.replace('_', '-')]
    return model(**attr)


def mapper_drf_api(model: type, resource: dict) -> object:
    """
    Returns an obj of type `model` from dictified JSON `resource` for DRF APIs
    """
    accepted_params = {k: resource[k] for k in model._fields}
    return model(**accepted_params)


User = namedtuple(
    'User',
    ['id', 'email', 'first_name', 'lang', 'last_name', 'username']
)

Organization = namedtuple(
    'Organization',
    ['id', 'name']
)

Project = namedtuple(
    'Project',
    ['id', 'created_on', 'file_count', 'package_name', 'platform',
     'updated_on']
)

File = namedtuple(
    'File',
    ['id', 'name', 'version', 'version_code', 'static_scan_progress']
)

Analysis = namedtuple(
    'Analysis',
    ['id', 'risk', 'status', 'cvss_base', 'cvss_vector', 'cvss_version',
     'cvss_metrics_humanized', 'findings', 'updated_on', 'vulnerability_id',
     'owasp']
)

Vulnerability = namedtuple(
    'Vulnerability',
    ['name', 'description', 'intro', 'related_to',
     'business_implication', 'compliant', 'non_compliant', 'types']
)

OWASP = namedtuple(
    'OWASP',
    ['code', 'title', 'description', 'year']
)

PersonalToken = namedtuple(
    'AccessToken',
    ['name', 'key']
)
