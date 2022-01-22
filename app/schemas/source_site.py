from pydantic import BaseModel


class SourceSite(BaseModel):
    url : str
