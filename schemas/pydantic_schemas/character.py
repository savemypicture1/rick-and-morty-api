from pydantic import BaseModel, AnyUrl
from datetime import datetime
from typing import List


class OriginSchema(BaseModel):
    name: str
    url: AnyUrl


class LocationSchema(BaseModel):
    name: str
    url: AnyUrl


class CharacterSchema(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: OriginSchema
    location: LocationSchema
    image: str
    episode: List[AnyUrl]
    url: AnyUrl
    created: datetime
