from datetime import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    description: str | None

    model_config = ConfigDict(from_attributes=True)


class STask(STaskAdd):
    id: int




class STaskId(BaseModel):
    id: int
