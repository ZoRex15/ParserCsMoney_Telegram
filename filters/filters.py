from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):

    def __init__(self, admin_id: int) -> None:
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> Any:
        return int(message.from_user.id) == int(self.admin_id)