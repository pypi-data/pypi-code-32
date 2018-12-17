import os


from flask import Flask, send_file
from werkzeug.serving import run_simple

from ..core.helpers import console
from ..applib.app import findApp, findAppConfig
from ..applib.helpers import getLocalDir, configure
from ..server.kernel import makeTfConnection
from .command import (
    argCheck,
    argDebug,
    argDocker,
    argLocalClones,
    argModules,
    argParam,
)
from .serve import (
    TIMEOUT,
    serveTable,
    serveQuery,
    servePassage,
    serveExport,
    serveDownload,
    serveAll,
)


myDir = os.path.dirname(os.path.abspath(__file__))


class Setup(object):
  def __init__(self, dataSource, lgc, check):
    self.dataSource = dataSource

    (commit, appDir) = findApp(dataSource, lgc, check)
    self.appDir = appDir

    config = findAppConfig(dataSource, appDir)
    self.config = config

    if config is None:
      return

    self.TF = makeTfConnection(config.HOST, config.PORT['kernel'], TIMEOUT)
    self.wildQueries = set()

    cfg = configure(config, lgc, None)
    version = cfg['version']
    cfg['localDir'] = getLocalDir(cfg, lgc, version)
    self.localDir = cfg['localDir']


def factory(setup):
  app = Flask(__name__)

  @app.route('/server/static/<path:filepath>')
  def serveStatic(filepath):
    return send_file(f'{myDir}/static/{filepath}')

  @app.route('/data/static/<path:filepath>')
  def serveData(filepath):
    return send_file(f'{setup.appDir}/static/{filepath}')

  @app.route('/local/<path:filepath>')
  def serveLocal(filepath):
    return send_file(f'{setup.localDir}/{filepath}')

  @app.route('/sections', methods=['GET', 'POST'])
  def serveSectionsBare():
    return serveTable(setup, 'sections', None)

  @app.route('/sections/<int:getx>', methods=['GET', 'POST'])
  def serveSections(getx):
    return serveTable(setup, 'sections', getx)

  @app.route('/tuples', methods=['GET', 'POST'])
  def serveTuplesBare():
    return serveTable(setup, 'tuples', None)

  @app.route('/tuples/<int:getx>', methods=['GET', 'POST'])
  def serveTuples(getx):
    return serveTable(setup, 'tuples', getx)

  @app.route('/query', methods=['GET', 'POST'])
  def serveQueryBare():
    return serveQuery(setup, None)

  @app.route('/query/<int:getx>', methods=['GET', 'POST'])
  def serveQueryX(getx):
    return serveQuery(setup, getx)

  @app.route('/passage', methods=['GET', 'POST'])
  def servePassageBare():
    return servePassage(setup, None)

  @app.route('/passage/<getx>', methods=['GET', 'POST'])
  def servePassageX(getx):
    return servePassage(setup, getx)

  @app.route('/export', methods=['GET', 'POST'])
  def serveExportX():
    return serveExport(setup, )

  @app.route('/download', methods=['GET', 'POST'])
  def serveDownloadX():
    return serveDownload(setup, )

  @app.route('/', methods=['GET', 'POST'])
  @app.route('/<path:anything>', methods=['GET', 'POST'])
  def serveAllX(anything=None):
    return serveAll(setup, anything)

  return app


if __name__ == "__main__":
  dataSource = argParam(interactive=True)
  modules = argModules()

  if dataSource is not None:
    modules = tuple(modules[6:].split(',')) if modules else ()
    lgc = argLocalClones()
    check = argCheck()
    debug = argDebug()
    setup = Setup(dataSource, lgc, check)
    config = setup.config
    if config is not None:
      onDocker = argDocker()
      console(f'onDocker={onDocker}')
      webapp = factory(setup)
      run_simple(
          '0.0.0.0' if onDocker else config.HOST,
          config.PORT['web'],
          webapp,
          use_reloader=False,
          use_debugger=debug,
      )
