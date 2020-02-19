from aiohttp.web import Request, Response, get
from aiohttp_clustered.app import ClusteredApplication


class MyApp(ClusteredApplication):
    value = 0

    def initialize(self):
        super().initialize()
        import random
        self.value = random.randint(1, 100)

    def val(self):
        return self.value


def main(*args):
    app = MyApp()

    async def handler(request: Request) -> Response:
        app.value += 1
        return Response(body=f"Hello, world! {app.value}")

    app.add_routes([get('/', handler)])

    return app
