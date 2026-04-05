from pydantic import BaseModel
from typing import List

class FileInput(BaseModel):
    filename: str
    content: str

class CompileRequest(BaseModel):
    files: List[FileInput]

class FileOutput(BaseModel):
    filename: str
    url: str

class CompileResponse(BaseModel):
    outputs: List[FileOutput]