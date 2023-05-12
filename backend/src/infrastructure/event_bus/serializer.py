from typing import Any
from uuid import UUID

import aio_pika


def additionally_serialize(obj: Any) -> Any:
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, aio_pika.Message):
        return obj.info()
    raise TypeError(f"TypeError: Type is not JSON serializable: {type(obj)}")
