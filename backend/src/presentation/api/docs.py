from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

docs = OpenAPIHandler(info=Info(title="Todo API", version="0.0.1"))

docs.include = lambda path, _: path.startswith("/api/")
