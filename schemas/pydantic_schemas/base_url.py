from pydantic import BaseModel, AnyUrl


class BaseUrlSchema(BaseModel):
    characters: AnyUrl
    locations: AnyUrl
    episodes: AnyUrl
