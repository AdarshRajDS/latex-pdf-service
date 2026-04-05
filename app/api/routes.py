from fastapi import APIRouter, HTTPException
from app.models.schemas import CompileRequest, CompileResponse
from app.services.latex import compile_latex_files

router = APIRouter()

@router.post("/compile", response_model=CompileResponse)
async def compile_endpoint(request: CompileRequest):
    try:
        return await compile_latex_files(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
