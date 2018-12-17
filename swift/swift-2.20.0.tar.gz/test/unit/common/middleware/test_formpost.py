# Copyright (c) 2011 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hmac
import unittest
from hashlib import sha1
from time import time

import six
from six import BytesIO

from swift.common.swob import Request, Response
from swift.common.middleware import tempauth, formpost
from swift.common.utils import split_path
from swift.proxy.controllers.base import get_cache_key


class FakeApp(object):

    def __init__(self, status_headers_body_iter=None,
                 check_no_query_string=True):
        self.status_headers_body_iter = status_headers_body_iter
        if not self.status_headers_body_iter:
            self.status_headers_body_iter = iter([('404 Not Found', {
                'x-test-header-one-a': 'value1',
                'x-test-header-two-a': 'value2',
                'x-test-header-two-b': 'value3'}, '')])
        self.requests = []
        self.check_no_query_string = check_no_query_string

    def __call__(self, env, start_response):
        try:
            if self.check_no_query_string and env.get('QUERY_STRING'):
                raise Exception('Query string %s should have been discarded!' %
                                env['QUERY_STRING'])
            body = b''
            while True:
                chunk = env['wsgi.input'].read()
                if not chunk:
                    break
                body += chunk
            env['wsgi.input'] = BytesIO(body)
            self.requests.append(Request.blank('', environ=env))
            if env.get('swift.authorize_override') and \
                    env.get('REMOTE_USER') != '.wsgi.pre_authed':
                raise Exception(
                    'Invalid REMOTE_USER %r with swift.authorize_override' % (
                        env.get('REMOTE_USER'),))
            if 'swift.authorize' in env:
                resp = env['swift.authorize'](self.requests[-1])
                if resp:
                    return resp(env, start_response)
            status, headers, body = next(self.status_headers_body_iter)
            return Response(status=status, headers=headers,
                            body=body)(env, start_response)
        except EOFError:
            start_response('499 Client Disconnect',
                           [('Content-Type', 'text/plain')])
            return ['Client Disconnect\n']


class TestCappedFileLikeObject(unittest.TestCase):

    def test_whole(self):
        self.assertEqual(
            formpost._CappedFileLikeObject(BytesIO(b'abc'), 10).read(),
            b'abc')

    def test_exceeded(self):
        exc = None
        try:
            formpost._CappedFileLikeObject(BytesIO(b'abc'), 2).read()
        except EOFError as err:
            exc = err
        self.assertEqual(str(exc), 'max_file_size exceeded')

    def test_whole_readline(self):
        fp = formpost._CappedFileLikeObject(BytesIO(b'abc\ndef'), 10)
        self.assertEqual(fp.readline(), b'abc\n')
        self.assertEqual(fp.readline(), b'def')
        self.assertEqual(fp.readline(), b'')

    def test_exceeded_readline(self):
        fp = formpost._CappedFileLikeObject(BytesIO(b'abc\ndef'), 5)
        self.assertEqual(fp.readline(), b'abc\n')
        exc = None
        try:
            self.assertEqual(fp.readline(), b'def')
        except EOFError as err:
            exc = err
        self.assertEqual(str(exc), 'max_file_size exceeded')

    def test_read_sized(self):
        fp = formpost._CappedFileLikeObject(BytesIO(b'abcdefg'), 10)
        self.assertEqual(fp.read(2), b'ab')
        self.assertEqual(fp.read(2), b'cd')
        self.assertEqual(fp.read(2), b'ef')
        self.assertEqual(fp.read(2), b'g')
        self.assertEqual(fp.read(2), b'')


class TestFormPost(unittest.TestCase):

    def setUp(self):
        self.app = FakeApp()
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)

    def _make_request(self, path, tempurl_keys=(), **kwargs):
        req = Request.blank(path, **kwargs)

        # Fake out the caching layer so that get_account_info() finds its
        # data. Include something that isn't tempurl keys to prove we skip it.
        meta = {'user-job-title': 'Personal Trainer',
                'user-real-name': 'Jim Shortz'}
        for idx, key in enumerate(tempurl_keys):
            meta_name = 'temp-url-key' + (("-%d" % (idx + 1) if idx else ""))
            if key:
                meta[meta_name] = key

        _junk, account, _junk, _junk = split_path(path, 2, 4)
        req.environ.setdefault('swift.infocache', {})
        req.environ['swift.infocache'][get_cache_key(account)] = \
            self._fake_cache_env(account, tempurl_keys)
        return req

    def _fake_cache_env(self, account, tempurl_keys=()):
        # Fake out the caching layer so that get_account_info() finds its
        # data. Include something that isn't tempurl keys to prove we skip it.
        meta = {'user-job-title': 'Personal Trainer',
                'user-real-name': 'Jim Shortz'}
        for idx, key in enumerate(tempurl_keys):
            meta_name = 'temp-url-key' + ("-%d" % (idx + 1) if idx else "")
            if key:
                meta[meta_name] = key

        return {'status': 204,
                'container_count': '0',
                'total_object_count': '0',
                'bytes': '0',
                'meta': meta}

    def _make_sig_env_body(self, path, redirect, max_file_size, max_file_count,
                           expires, key, user_agent=True):
        sig = hmac.new(
            key,
            '%s\n%s\n%s\n%s\n%s' % (
                path, redirect, max_file_size, max_file_count, expires),
            sha1).hexdigest()
        body = [
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file1"; '
            'filename="testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file2"; '
            'filename="testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR--',
            '',
        ]
        if six.PY3:
            body = [line.encode('utf-8') for line in body]
        wsgi_errors = six.StringIO()
        env = {
            'CONTENT_TYPE': 'multipart/form-data; '
            'boundary=----WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
            'HTTP_ACCEPT_LANGUAGE': 'en-us',
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,*/*;q=0.8',
            'HTTP_CONNECTION': 'keep-alive',
            'HTTP_HOST': 'ubuntu:8080',
            'HTTP_ORIGIN': 'file://',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
            '10_7_2) AppleWebKit/534.52.7 (KHTML, like Gecko) '
            'Version/5.1.2 Safari/534.52.7',
            'PATH_INFO': path,
            'REMOTE_ADDR': '172.16.83.1',
            'REQUEST_METHOD': 'POST',
            'SCRIPT_NAME': '',
            'SERVER_NAME': '172.16.83.128',
            'SERVER_PORT': '8080',
            'SERVER_PROTOCOL': 'HTTP/1.0',
            'swift.infocache': {},
            'wsgi.errors': wsgi_errors,
            'wsgi.multiprocess': False,
            'wsgi.multithread': True,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
        }
        if user_agent is False:
            del env['HTTP_USER_AGENT']

        return sig, env, body

    def test_passthrough(self):
        for method in ('HEAD', 'GET', 'PUT', 'POST', 'DELETE'):
            resp = self._make_request(
                '/v1/a/c/o',
                environ={'REQUEST_METHOD': method}).get_response(self.formpost)
            self.assertEqual(resp.status_int, 401)
            self.assertNotIn('FormPost', resp.body)

    def test_auth_scheme(self):
        # FormPost rejects
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() - 10), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        authenticate_v = None
        for h, v in headers:
            if h.lower() == 'www-authenticate':
                authenticate_v = v
        self.assertTrue('FormPost: Form Expired' in body)
        self.assertEqual('Swift realm="unknown"', authenticate_v)

    def test_safari(self):
        key = 'abc'
        path = '/v1/AUTH_test/container'
        redirect = 'http://brim.net'
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig = hmac.new(
            key,
            '%s\n%s\n%s\n%s\n%s' % (
                path, redirect, max_file_size, max_file_count, expires),
            sha1).hexdigest()
        wsgi_input = '\r\n'.join([
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file1"; '
            'filename="testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file2"; '
            'filename="testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR--',
            '',
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        wsgi_input = BytesIO(wsgi_input)
        wsgi_errors = six.StringIO()
        env = {
            'CONTENT_TYPE': 'multipart/form-data; '
            'boundary=----WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
            'HTTP_ACCEPT_LANGUAGE': 'en-us',
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,*/*;q=0.8',
            'HTTP_CONNECTION': 'keep-alive',
            'HTTP_HOST': 'ubuntu:8080',
            'HTTP_ORIGIN': 'file://',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
            '10_7_2) AppleWebKit/534.52.7 (KHTML, like Gecko) '
            'Version/5.1.2 Safari/534.52.7',
            'PATH_INFO': path,
            'REMOTE_ADDR': '172.16.83.1',
            'REQUEST_METHOD': 'POST',
            'SCRIPT_NAME': '',
            'SERVER_NAME': '172.16.83.128',
            'SERVER_PORT': '8080',
            'SERVER_PROTOCOL': 'HTTP/1.0',
            'swift.infocache': {
                get_cache_key('AUTH_test'): self._fake_cache_env(
                    'AUTH_test', [key]),
                get_cache_key('AUTH_test', 'container'): {
                    'meta': {}}},
            'wsgi.errors': wsgi_errors,
            'wsgi.input': wsgi_input,
            'wsgi.multiprocess': False,
            'wsgi.multithread': True,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
        }
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://brim.net?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue('http://brim.net?status=201&message=' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_firefox(self):
        key = 'abc'
        path = '/v1/AUTH_test/container'
        redirect = 'http://brim.net'
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig = hmac.new(
            key,
            '%s\n%s\n%s\n%s\n%s' % (
                path, redirect, max_file_size, max_file_count, expires),
            sha1).hexdigest()
        wsgi_input = '\r\n'.join([
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="file1"; '
            'filename="testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="file2"; '
            'filename="testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '-----------------------------168072824752491622650073',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '-----------------------------168072824752491622650073--',
            ''
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        wsgi_input = BytesIO(wsgi_input)
        wsgi_errors = six.StringIO()
        env = {
            'CONTENT_TYPE': 'multipart/form-data; '
            'boundary=---------------------------168072824752491622650073',
            'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
            'HTTP_ACCEPT_LANGUAGE': 'en-us,en;q=0.5',
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,*/*;q=0.8',
            'HTTP_CONNECTION': 'keep-alive',
            'HTTP_HOST': 'ubuntu:8080',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; '
            'rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'PATH_INFO': '/v1/AUTH_test/container',
            'REMOTE_ADDR': '172.16.83.1',
            'REQUEST_METHOD': 'POST',
            'SCRIPT_NAME': '',
            'SERVER_NAME': '172.16.83.128',
            'SERVER_PORT': '8080',
            'SERVER_PROTOCOL': 'HTTP/1.0',
            'swift.infocache': {
                get_cache_key('AUTH_test'): self._fake_cache_env(
                    'AUTH_test', [key]),
                get_cache_key('AUTH_test', 'container'): {
                    'meta': {}}},
            'wsgi.errors': wsgi_errors,
            'wsgi.input': wsgi_input,
            'wsgi.multiprocess': False,
            'wsgi.multithread': True,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
        }
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://brim.net?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue('http://brim.net?status=201&message=' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_chrome(self):
        key = 'abc'
        path = '/v1/AUTH_test/container'
        redirect = 'http://brim.net'
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig = hmac.new(
            key,
            '%s\n%s\n%s\n%s\n%s' % (
                path, redirect, max_file_size, max_file_count, expires),
            sha1).hexdigest()
        wsgi_input = '\r\n'.join([
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="file1"; '
            'filename="testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="file2"; '
            'filename="testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '------WebKitFormBoundaryq3CFxUjfsDMu8XsA--',
            ''
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        wsgi_input = BytesIO(wsgi_input)
        wsgi_errors = six.StringIO()
        env = {
            'CONTENT_TYPE': 'multipart/form-data; '
            'boundary=----WebKitFormBoundaryq3CFxUjfsDMu8XsA',
            'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
            'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',
            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,*/*;q=0.8',
            'HTTP_CACHE_CONTROL': 'max-age=0',
            'HTTP_CONNECTION': 'keep-alive',
            'HTTP_HOST': 'ubuntu:8080',
            'HTTP_ORIGIN': 'null',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
            '10_7_2) AppleWebKit/535.7 (KHTML, like Gecko) '
            'Chrome/16.0.912.63 Safari/535.7',
            'PATH_INFO': '/v1/AUTH_test/container',
            'REMOTE_ADDR': '172.16.83.1',
            'REQUEST_METHOD': 'POST',
            'SCRIPT_NAME': '',
            'SERVER_NAME': '172.16.83.128',
            'SERVER_PORT': '8080',
            'SERVER_PROTOCOL': 'HTTP/1.0',
            'swift.infocache': {
                get_cache_key('AUTH_test'): self._fake_cache_env(
                    'AUTH_test', [key]),
                get_cache_key('AUTH_test', 'container'): {
                    'meta': {}}},
            'wsgi.errors': wsgi_errors,
            'wsgi.input': wsgi_input,
            'wsgi.multiprocess': False,
            'wsgi.multithread': True,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
        }
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://brim.net?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue('http://brim.net?status=201&message=' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_explorer(self):
        key = 'abc'
        path = '/v1/AUTH_test/container'
        redirect = 'http://brim.net'
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig = hmac.new(
            key,
            '%s\n%s\n%s\n%s\n%s' % (
                path, redirect, max_file_size, max_file_count, expires),
            sha1).hexdigest()
        wsgi_input = '\r\n'.join([
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="file1"; '
            'filename="C:\\testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="file2"; '
            'filename="C:\\testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '-----------------------------7db20d93017c',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '-----------------------------7db20d93017c--',
            ''
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        wsgi_input = BytesIO(wsgi_input)
        wsgi_errors = six.StringIO()
        env = {
            'CONTENT_TYPE': 'multipart/form-data; '
            'boundary=---------------------------7db20d93017c',
            'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
            'HTTP_ACCEPT_LANGUAGE': 'en-US',
            'HTTP_ACCEPT': 'text/html, application/xhtml+xml, */*',
            'HTTP_CACHE_CONTROL': 'no-cache',
            'HTTP_CONNECTION': 'Keep-Alive',
            'HTTP_HOST': '172.16.83.128:8080',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT '
            '6.1; WOW64; Trident/5.0)',
            'PATH_INFO': '/v1/AUTH_test/container',
            'REMOTE_ADDR': '172.16.83.129',
            'REQUEST_METHOD': 'POST',
            'SCRIPT_NAME': '',
            'SERVER_NAME': '172.16.83.128',
            'SERVER_PORT': '8080',
            'SERVER_PROTOCOL': 'HTTP/1.0',
            'swift.infocache': {
                get_cache_key('AUTH_test'): self._fake_cache_env(
                    'AUTH_test', [key]),
                get_cache_key('AUTH_test', 'container'): {
                    'meta': {}}},
            'wsgi.errors': wsgi_errors,
            'wsgi.input': wsgi_input,
            'wsgi.multiprocess': False,
            'wsgi.multithread': True,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
        }
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://brim.net?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue('http://brim.net?status=201&message=' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_messed_up_start(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://brim.net', 5, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'XX' + b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)

        def log_assert_int_status(env, response_status_int):
            self.assertTrue(isinstance(response_status_int, int))

        self.formpost._log_request = log_assert_int_status
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: invalid starting boundary' in body)
        self.assertEqual(len(self.app.requests), 0)

    def test_max_file_size_exceeded(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://brim.net', 5, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: max_file_size exceeded' in body)
        self.assertEqual(len(self.app.requests), 0)

    def test_max_file_count_exceeded(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://brim.net', 1024, 1,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(
            location,
            'http://brim.net?status=400&message=max%20file%20count%20exceeded')
        self.assertIsNone(exc_info)
        self.assertTrue(
            'http://brim.net?status=400&message=max%20file%20count%20exceeded'
            in body)
        self.assertEqual(len(self.app.requests), 1)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')

    def test_subrequest_does_not_pass_query(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['QUERY_STRING'] = 'this=should&not=get&passed'
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(
            iter([('201 Created', {}, ''),
                  ('201 Created', {}, '')]),
            check_no_query_string=True)
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        # Make sure we 201 Created, which means we made the final subrequest
        # (and FakeApp verifies that no QUERY_STRING got passed).
        self.assertEqual(status, '201 Created')
        self.assertIsNone(exc_info)
        self.assertTrue('201 Created' in body)
        self.assertEqual(len(self.app.requests), 2)

    def test_subrequest_fails(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://brim.net', 1024, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('404 Not Found', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://brim.net?status=404&message=')
        self.assertIsNone(exc_info)
        self.assertTrue('http://brim.net?status=404&message=' in body)
        self.assertEqual(len(self.app.requests), 1)

    def test_truncated_attr_value(self):
        key = 'abc'
        redirect = 'a' * formpost.MAX_VALUE_LENGTH
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', redirect, max_file_size, max_file_count,
            expires, key)
        # Tack on an extra char to redirect, but shouldn't matter since it
        # should get truncated off on read.
        redirect += 'b'
        wsgi_input = '\r\n'.join([
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file1"; '
            'filename="testfile1.txt"',
            'Content-Type: text/plain',
            '',
            'Test File\nOne\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file2"; '
            'filename="testfile2.txt"',
            'Content-Type: text/plain',
            '',
            'Test\nFile\nTwo\n',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="file3"; filename=""',
            'Content-Type: application/octet-stream',
            '',
            '',
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR--',
            '',
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(
            location,
            ('a' * formpost.MAX_VALUE_LENGTH) + '?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue(
            ('a' * formpost.MAX_VALUE_LENGTH) + '?status=201&message=' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_no_file_to_process(self):
        key = 'abc'
        redirect = 'http://brim.net'
        max_file_size = 1024
        max_file_count = 10
        expires = int(time() + 86400)
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', redirect, max_file_size, max_file_count,
            expires, key)
        wsgi_input = '\r\n'.join([
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="redirect"',
            '',
            redirect,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_size"',
            '',
            str(max_file_size),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="max_file_count"',
            '',
            str(max_file_count),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="expires"',
            '',
            str(expires),
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="signature"',
            '',
            sig,
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR--',
            '',
        ])
        if six.PY3:
            wsgi_input = wsgi_input.encode('utf-8')
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(
            location,
            'http://brim.net?status=400&message=no%20files%20to%20process')
        self.assertIsNone(exc_info)
        self.assertTrue(
            'http://brim.net?status=400&message=no%20files%20to%20process'
            in body)
        self.assertEqual(len(self.app.requests), 0)

    def test_formpost_without_useragent(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://redirect', 1024, 10,
            int(time() + 86400), key, user_agent=False)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)

        def start_response(s, h, e=None):
            pass
        body = ''.join(self.formpost(env, start_response))
        self.assertTrue('User-Agent' in self.app.requests[0].headers)
        self.assertEqual(self.app.requests[0].headers['User-Agent'],
                         'FormPost')

    def test_formpost_with_origin(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://redirect', 1024, 10,
            int(time() + 86400), key, user_agent=False)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        env['HTTP_ORIGIN'] = 'http://localhost:5000'
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created',
                                  {'Access-Control-Allow-Origin':
                                   'http://localhost:5000'}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)

        headers = {}

        def start_response(s, h, e=None):
            for k, v in h:
                headers[k] = v
            pass

        body = ''.join(self.formpost(env, start_response))
        self.assertEqual(headers['Access-Control-Allow-Origin'],
                         'http://localhost:5000')

    def test_formpost_with_multiple_keys(self):
        key = 'ernie'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://redirect', 1024, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        # Stick it in X-Account-Meta-Temp-URL-Key-2 and make sure we get it
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)

        status = [None]
        headers = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
        body = ''.join(self.formpost(env, start_response))
        self.assertEqual('303 See Other', status[0])
        self.assertEqual(
            'http://redirect?status=201&message=',
            dict(headers[0]).get('Location'))

    def test_formpost_with_multiple_container_keys(self):
        first_key = 'ernie'
        second_key = 'bert'
        keys = [first_key, second_key]

        meta = {}
        for idx, key in enumerate(keys):
            meta_name = 'temp-url-key' + ("-%d" % (idx + 1) if idx else "")
            if key:
                meta[meta_name] = key

        for key in keys:
            sig, env, body = self._make_sig_env_body(
                '/v1/AUTH_test/container', 'http://redirect', 1024, 10,
                int(time() + 86400), key)
            env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
            env['swift.infocache'][get_cache_key('AUTH_test')] = (
                self._fake_cache_env('AUTH_test'))
            # Stick it in X-Container-Meta-Temp-URL-Key-2 and ensure we get it
            env['swift.infocache'][get_cache_key(
                'AUTH_test', 'container')] = {'meta': meta}
            self.app = FakeApp(iter([('201 Created', {}, ''),
                                     ('201 Created', {}, '')]))
            self.auth = tempauth.filter_factory({})(self.app)
            self.formpost = formpost.filter_factory({})(self.auth)

            status = [None]
            headers = [None]

            def start_response(s, h, e=None):
                status[0] = s
                headers[0] = h
            body = ''.join(self.formpost(env, start_response))
            self.assertEqual('303 See Other', status[0])
            self.assertEqual(
                'http://redirect?status=201&message=',
                dict(headers[0]).get('Location'))

    def test_redirect(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://redirect', 1024, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location, 'http://redirect?status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue(location in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_redirect_with_query(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', 'http://redirect?one=two', 1024, 10,
            int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '303 See Other')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertEqual(location,
                         'http://redirect?one=two&status=201&message=')
        self.assertIsNone(exc_info)
        self.assertTrue(location in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_no_redirect(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '201 Created')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('201 Created' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertEqual(self.app.requests[0].body, 'Test File\nOne\n')
        self.assertEqual(self.app.requests[1].body, 'Test\nFile\nTwo\n')

    def test_no_redirect_expired(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() - 10), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Form Expired' in body)

    def test_no_redirect_invalid_sig(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        # Change key to invalidate sig
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key + ' is bogus now']))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_no_redirect_with_error(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'XX' + b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: invalid starting boundary' in body)

    def test_no_v1(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v2/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_empty_v1(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '//AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_empty_account(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1//container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_wrong_account(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_tst/container', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([
            ('200 Ok', {'x-account-meta-temp-url-key': 'def'}, ''),
            ('201 Created', {}, ''),
            ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_no_container(self):
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test', '', 1024, 10, int(time() + 86400), key)
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '401 Unauthorized')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: Invalid Signature' in body)

    def test_completely_non_int_expires(self):
        key = 'abc'
        expires = int(time() + 86400)
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, expires, key)
        for i, v in enumerate(body):
            if v == str(expires):
                body[i] = 'badvalue'
                break
        env['wsgi.input'] = BytesIO(b'\r\n'.join(body))
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        location = None
        for h, v in headers:
            if h.lower() == 'location':
                location = v
        self.assertIsNone(location)
        self.assertIsNone(exc_info)
        self.assertTrue('FormPost: expired not an integer' in body)

    def test_x_delete_at(self):
        delete_at = int(time() + 100)
        x_delete_body_part = [
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="x_delete_at"',
            '',
            str(delete_at),
        ]
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        wsgi_input = b'\r\n'.join(x_delete_body_part + body)
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '201 Created')
        self.assertTrue('201 Created' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertTrue("X-Delete-At" in self.app.requests[0].headers)
        self.assertTrue("X-Delete-At" in self.app.requests[1].headers)
        self.assertEqual(delete_at,
                         self.app.requests[0].headers["X-Delete-At"])
        self.assertEqual(delete_at,
                         self.app.requests[1].headers["X-Delete-At"])

    def test_x_delete_at_not_int(self):
        delete_at = "2014-07-16"
        x_delete_body_part = [
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="x_delete_at"',
            '',
            str(delete_at),
        ]
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        wsgi_input = b'\r\n'.join(x_delete_body_part + body)
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        self.assertTrue('FormPost: x_delete_at not an integer' in body)

    def test_x_delete_after(self):
        delete_after = 100
        x_delete_body_part = [
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="x_delete_after"',
            '',
            str(delete_after),
        ]
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        wsgi_input = b'\r\n'.join(x_delete_body_part + body)
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        env['swift.infocache'][get_cache_key(
            'AUTH_test', 'container')] = {'meta': {}}
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '201 Created')
        self.assertTrue('201 Created' in body)
        self.assertEqual(len(self.app.requests), 2)
        self.assertTrue("X-Delete-After" in self.app.requests[0].headers)
        self.assertTrue("X-Delete-After" in self.app.requests[1].headers)
        self.assertEqual(delete_after,
                         self.app.requests[0].headers["X-Delete-After"])
        self.assertEqual(delete_after,
                         self.app.requests[1].headers["X-Delete-After"])

    def test_x_delete_after_not_int(self):
        delete_after = "2 days"
        x_delete_body_part = [
            '------WebKitFormBoundaryNcxTqxSlX7t4TDkR',
            'Content-Disposition: form-data; name="x_delete_after"',
            '',
            str(delete_after),
        ]
        key = 'abc'
        sig, env, body = self._make_sig_env_body(
            '/v1/AUTH_test/container', '', 1024, 10, int(time() + 86400), key)
        wsgi_input = b'\r\n'.join(x_delete_body_part + body)
        env['wsgi.input'] = BytesIO(wsgi_input)
        env['swift.infocache'][get_cache_key('AUTH_test')] = (
            self._fake_cache_env('AUTH_test', [key]))
        self.app = FakeApp(iter([('201 Created', {}, ''),
                                 ('201 Created', {}, '')]))
        self.auth = tempauth.filter_factory({})(self.app)
        self.formpost = formpost.filter_factory({})(self.auth)
        status = [None]
        headers = [None]
        exc_info = [None]

        def start_response(s, h, e=None):
            status[0] = s
            headers[0] = h
            exc_info[0] = e

        body = ''.join(self.formpost(env, start_response))
        status = status[0]
        headers = headers[0]
        exc_info = exc_info[0]
        self.assertEqual(status, '400 Bad Request')
        self.assertTrue('FormPost: x_delete_after not an integer' in body)


if __name__ == '__main__':
    unittest.main()
