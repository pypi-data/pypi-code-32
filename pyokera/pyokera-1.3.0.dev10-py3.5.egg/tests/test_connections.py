# Copyright 2017 Okera Inc. All Rights Reserved.
#
# Tests that verify connection issues with specific server auth settings.

# pylint: disable=broad-except
# pylint: disable=bad-continuation
# pylint: disable=bad-indentation
import os
import unittest
from okera import context

SERVER_AUTH = 'NOSASL'
if 'PYCEREBRO_TEST_AUTH_MECH' in os.environ:
    SERVER_AUTH = os.environ['PYCEREBRO_TEST_AUTH_MECH']

ROOT_TOKEN = os.environ['OKERA_HOME'] + '/integration/tokens/cerebro.token'

class ConnectionErrorsTest(unittest.TestCase):

    @unittest.skipIf(SERVER_AUTH != 'NOSASL', "Test requires server to have no auth.")
    def test_unauthenticated_server_planner(self):
        ctx = context()
        ctx.enable_token_auth('bad.token')
        thrown = False
        try:
            ctx.connect()
        except Exception as e:
            msg = str(e)
            self.assertTrue("Ensure server has authentication enabled" in msg, msg=e)
            thrown = True
        self.assertTrue(thrown)

    @unittest.skipIf(SERVER_AUTH != 'NOSASL', "Test requires server to have no auth.")
    def test_unauthenticated_server_worker(self):
        ctx = context()
        ctx.enable_token_auth('bad.token')
        thrown = False
        try:
            ctx.connect_worker()
        except Exception as e:
            msg = str(e)
            self.assertTrue("Ensure server has authentication enabled" in msg, msg=e)
            thrown = True
        self.assertTrue(thrown)

    @unittest.skipIf(SERVER_AUTH != 'TOKEN', "Test requires server to have token auth.")
    def test_token_server_wrong_token(self):
        ctx = context()

        # Wrong token
        thrown = False
        try:
            ctx.enable_token_auth(token_str='bad.token')
            ctx.connect()
        except Exception as e:
            msg = str(e)
            thrown = True
            self.assertTrue("Could not verify token" in msg, msg=e)
        self.assertTrue(thrown)

    @unittest.skipIf(SERVER_AUTH != 'TOKEN', "Test requires server to have token auth.")
    def test_token_server_no_token(self):
        thrown = False
        ctx = context()
        try:
            ctx.disable_auth()
            ctx.connect()
        except Exception as e:
            msg = str(e)
            thrown = True
            self.assertTrue("Client does not have authentication enabled" in msg, msg=e)
        self.assertTrue(thrown)

    @unittest.skipIf(SERVER_AUTH != 'TOKEN', "Test requires server to have kerberos.")
    def test_token_server_valid_token(self):
        ctx = context()
        ctx.enable_token_auth(token_file=ROOT_TOKEN)
        with ctx.connect() as p:
            self.assertTrue(p.get_protocol_version() is not None)

    @unittest.skipIf(SERVER_AUTH != 'KERBEROS', "Test requires server to have kerberos.")
    def test_kerberos_server_no_override(self):
        ctx = context()
        # This assumes the server principal is cerebro/localhost, which is wrong
        ctx.enable_kerberos('cerebro')
        thrown = False
        try:
            ctx.connect()
        except Exception as e:
            msg = str(e)
            thrown = True
            self.assertTrue("cerebro/localhost@CEREBRO.TEST" in msg, msg=e)
        self.assertTrue(thrown)

    @unittest.skipIf(SERVER_AUTH != 'KERBEROS', "Test requires server to have kerberos.")
    def test_kerberos_server_valid_client(self):
        ctx = context()
        ctx.enable_kerberos('cerebro', host_override='service')
        with ctx.connect() as p:
            self.assertTrue(p.get_protocol_version() is not None)
            p.close()

if __name__ == "__main__":
    unittest.main()
