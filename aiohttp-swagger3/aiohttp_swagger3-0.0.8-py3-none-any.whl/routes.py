from aiohttp import web

_SWAGGER_INDEX_HTML = "SWAGGER_INDEX_HTML"
_SWAGGER_SPECIFICATION = "SWAGGER_SPECIFICATION"


async def _swagger_home(request):
    return web.Response(text=request.app[_SWAGGER_INDEX_HTML], content_type="text/html")


async def _swagger_spec(request):
    return web.json_response(request.app[_SWAGGER_SPECIFICATION])


async def _redirect(request: web.Request):
    return web.HTTPMovedPermanently(f'{request.path}/')
