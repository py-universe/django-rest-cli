from typing import Optional, List
import asyncio


class AddCrud:
    @staticmethod
    async def __add(app_name: str, directory: Optional[str] = None) -> None:
        pass

    @classmethod
    async def addcrud_for_multiple_apps(cls, apps: List) -> None:
        funcs = []
        for app in apps:
            funcs.append(asyncio.ensure_future(cls.__add(app)))
        await asyncio.gather(*funcs)
