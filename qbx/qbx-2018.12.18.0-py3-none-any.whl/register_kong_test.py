from .register_kong import register_kong


def test_reg():
    register_kong(['--name', 'pytest', '--ip', '1.2.3.4', '--hosts', 'pytest.qbtrade.org', '--port', '8080',
                   '--upstream-suffix', '/hello'])

    register_kong(['--name', 'pytest2', '--ip', '1.2.3.4', '--hosts', 'pytest.qbtrade.org', '--port', '8080',
                   ])
