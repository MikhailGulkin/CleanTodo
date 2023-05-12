from blacksheep.server.openapi.common import ContentInfo, EndpointDocs, ResponseInfo
from src.application.user.dto import User

user_create = EndpointDocs(
    responses={
        201: ResponseInfo(
            "User",
            content=[
                ContentInfo(
                    User,
                )
            ],
        ),
    }
)
