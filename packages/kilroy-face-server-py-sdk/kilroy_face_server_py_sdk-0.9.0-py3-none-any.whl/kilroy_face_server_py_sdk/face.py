from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, AsyncIterable, Dict, Generic, Optional, Tuple, TypeVar
from uuid import UUID

from kilroy_face_py_shared import Metadata
from kilroy_server_py_utils import Configurable, JSONSchema, classproperty

StateType = TypeVar("StateType")


class Face(Configurable[StateType], ABC, Generic[StateType]):
    # noinspection PyMethodParameters
    @classproperty
    @abstractmethod
    def metadata(cls) -> Metadata:
        pass

    # noinspection PyMethodParameters
    @classproperty
    @abstractmethod
    def post_schema(cls) -> JSONSchema:
        pass

    @abstractmethod
    async def post(
        self, content: Dict[str, Any]
    ) -> Tuple[UUID, Optional[str]]:
        pass

    @abstractmethod
    async def score(self, id: UUID) -> float:
        pass

    @abstractmethod
    def scrap(
        self,
        limit: Optional[int] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
    ) -> AsyncIterable[Tuple[UUID, Dict[str, Any], float]]:
        pass

    async def reset_self(self) -> None:
        await self.cleanup()
        await self.init()

    async def save_self(self, directory: Path) -> None:
        await self.save(directory)
