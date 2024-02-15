from pydantic import BaseModel, AnyUrl
from datetime import datetime
from typing import List


class LocationSchema(BaseModel):
    id: int
    name: str
    type: str
    dimension: str
    residents: List[str]
    url: AnyUrl
    created: datetime
