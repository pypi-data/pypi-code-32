from enum import Enum
import requests
from furl import furl
import json
import re

from django.conf import settings


import logging
logger = logging.getLogger(__name__)


class PPM:
    """
    This class serves mostly to track the PPM project properties across
    studies and consolidate functionality common amongst all services.
    """

    @staticmethod
    def fhir_url():
        if hasattr(settings, 'FHIR_URL'):
            return settings.FHIR_URL

        raise ValueError('FHIR_URL not defined in settings')

    @staticmethod
    def is_tester(email):
        '''
        Checks test user email patterns and returns True if a user's email
        matches.
        :param email: The user's email address
        :return: bool
        '''
        if hasattr(settings, 'TEST_EMAIL_PATTERNS'):
            testers = settings.TEST_EMAIL_PATTERNS.split(',')
        else:
            testers = ['(b32147|bryan.n.larson)\+[a-zA-Z0-9_.+-]*@gmail.com',
                       'b32147@gmail.com',
                       'bryan.n.larson@gmail.com',
                       'bryan_larson@hms.harvard.edu']

        # Iterate through all patterns
        for pattern in testers:
            if re.match(pattern, email):
                return True

        return False

    class Project(Enum):
        NEER = 'neer'
        ASD = 'autism'

    # Set the appropriate participant statuses
    class Enrollment(Enum):
        Registered = 'registered'
        Consented = 'consented'
        Proposed = 'proposed'
        Accepted = 'accepted'
        Pending = 'pending'
        Ineligible = 'ineligible'

        ENROLLMENTS = (
            (Registered, 'Registered'),
            (Consented, 'Consented'),
            (Proposed, 'Proposed'),
            (Accepted, 'Accepted'),
            (Ineligible, 'Ineligible'),
        )

    class Questionnaire(Enum):
        ASDGuardianConsentQuestionnaire = 'ppm-asd-consent-guardian-quiz'
        ASDIndividualConsentQuestionnaire = 'ppm-asd-consent-individual-quiz'
        NEERQuestionnaire = 'ppm-neer-registration-questionnaire'
        ASDQuestionnaire = 'ppm-asd-questionnaire'

        @staticmethod
        def questionnaire_for_project(project):
            if project == PPM.Project.ASD:
                return PPM.Questionnaire.ASDQuestionnaire

            elif project == PPM.Project.NEER:
                return PPM.Questionnaire.NEERQuestionnaire

        @staticmethod
        def questionnaire_for_consent(composition):
            if composition.get('type', '').lower() == 'guardian':
                return PPM.Questionnaire.ASDGuardianConsentQuestionnaire

            else:
                return PPM.Questionnaire.ASDIndividualConsentQuestionnaire

    class Provider(Enum):
        Fitbit = 'fitbit'
        Twitter = 'twitter'
        Facebook = 'facebook'
        Gencove = 'gencove'
        uBiome = 'ubiome'

    class Service(object):

        # Subclasses set this to direct requests
        service = None

        # Set some JWT properties
        _jwt_cookie_name = 'DBMI_JWT'
        _jwt_authorization_prefix = 'JWT'

        @classmethod
        def _build_url(cls, path):

            # Build the url.
            url = furl(cls.service_url())

            # Clear segments and paths
            url.path.segments.extend(path.split('/'))

            # Filter empty segments (double slashes in path)
            segments = [segment for index, segment in enumerate(url.path.segments)
                        if segment != '' or index == len(url.path.segments) - 1]

            # Log the filter
            if len(segments) < len(url.path.segments):
                logger.debug('Path filtered: /{} -> /{}'.format('/'.join(url.path.segments), '/'.join(segments)))

            # Set it
            url.path.segments = segments

            return url.url

        @classmethod
        def service_url(cls):

            # Check variations of names
            names = ['###_URL', 'DBMI_###_URL', '###_API_URL', '###_BASE_URL']
            for name in names:
                if hasattr(settings, name.replace('###', cls.service.upper())):
                    service_url = getattr(settings, name.replace('###', cls.service.upper()))

                    # We want only the domain and no paths, as those should be specified in the calls
                    # so strip any included paths and queries and return
                    url = furl(service_url)
                    url.path.segments.clear()
                    url.query.params.clear()

                    return url.url

            raise ValueError('Service URL not defined in settings'.format(cls.service.upper()))

        @classmethod
        def headers(cls, request):
            return {"Authorization": 'JWT {}'.format(request.COOKIES.get("DBMI_JWT", None)),
                    'Content-Type': 'application/json'}

        @classmethod
        def get_jwt(cls, request):

            # Get the JWT token depending on request type
            if hasattr(request, 'COOKIES') and request.COOKIES.get(cls._jwt_cookie_name):
                return request.COOKIES.get(cls._jwt_cookie_name)

            # Check if JWT in HTTP Authorization header
            elif hasattr(request, 'META') and request.META.get('HTTP_AUTHORIZATION') \
                    and cls._jwt_authorization_prefix in request.META.get('HTTP_AUTHORIZATION'):

                # Remove prefix and return the token
                return request.META.get('HTTP_AUTHORIZATION') \
                    .replace('{} '.format(cls._jwt_authorization_prefix), '')

            return None

        @classmethod
        def head(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.head(
                    cls._build_url(path),
                    headers=cls.headers(request),
                    params=data
                )

                # Check response type
                if raw:
                    return response
                else:
                    return response.json()

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'data': data, 'path': path,
                })

            return None

        @classmethod
        def get(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.get(
                    cls._build_url(path),
                    headers=cls.headers(request),
                    params=data
                )

                # Check response type
                if raw:
                    return response
                else:
                    return response.json()

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'data': data, 'path': path,
                })

            return None

        @classmethod
        def post(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.post(
                    cls._build_url(path),
                    headers=cls.headers(request),
                    data=json.dumps(data)
                )

                # Check response type
                if raw:
                    return response
                else:
                    return response.json()

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'data': data, 'path': path,
                })

            return None

        @classmethod
        def put(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.put(
                    cls._build_url(path),
                    headers=cls.headers(request),
                    data=json.dumps(data)
                )

                # Check response type
                if raw:
                    return response
                else:
                    return response.json()

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'data': data, 'path': path,
                })

            return None

        @classmethod
        def patch(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.patch(cls._build_url(path),
                                          headers=cls.headers(request),
                                          data=json.dumps(data))

                # Check response type
                if raw:
                    return response
                else:
                    return response.ok

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'data': data, 'path': path,
                })

            return False

        @classmethod
        def delete(cls, request, path, data=None, raw=False):
            logger.debug('Path: {}'.format(path))

            # Check for params
            if not data:
                data = {}

            try:
                # Prepare the request.
                response = requests.delete(cls._build_url(path),
                                           headers=cls.headers(request),
                                           data=json.dumps(data))

                # Check response type
                if raw:
                    return response
                else:
                    return response.ok

            except Exception as e:
                logger.exception('{} error: {}'.format(cls.service, e), exc_info=True, extra={
                    'path': path,
                })

            return False
