from blacksheep.server.controllers import APIController


class BaseController(APIController):

    @classmethod
    def version(cls) -> str:
        return 'v1'
