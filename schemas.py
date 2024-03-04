

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    description: str
    nickname: str


class STask(BaseModel):
    description: str
    nickname: str

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    id: int
