from datetime import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    description: str


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    id: int
