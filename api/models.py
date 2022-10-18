from pydantic import BaseModel


class ImageData(BaseModel):
    percent: str
    fragments: int
    normals: int
    text: str
