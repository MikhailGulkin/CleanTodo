from src.domain.user.events import UserCreated
from src.infrastructure.event_bus import events as integration_events


def convert_user_created_to_integration(event: UserCreated) -> integration_events.UserCreated:
    return integration_events.UserCreated(
        user_id=event.id,
        username=event.username,
        email=event.email,
        password=event.password,
    )
