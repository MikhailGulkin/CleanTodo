from blacksheep.server.controllers import APIController


class BaseAPIController(APIController):
    @classmethod
    def version(cls) -> str:
        return "v1"
