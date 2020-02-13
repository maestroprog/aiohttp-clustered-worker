from aiohttp.web import Application, Request, Response, get


async def handler(request: Request) -> Response:
    return Response(body="Hello, world!")


def main(*args):
    app = Application()
    app.add_routes([get('/', handler)])

    return app
