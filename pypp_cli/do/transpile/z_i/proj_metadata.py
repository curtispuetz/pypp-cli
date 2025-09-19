from pydantic import BaseModel


class ProjMetadata(BaseModel):
    namespace: str
