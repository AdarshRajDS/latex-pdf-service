from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router



app = FastAPI(
    title="LaTeX PDF Compiler API",
    version="2.0.0"
)

# Serve generated PDFs
app.mount("/files", StaticFiles(directory="outputs"), name="files")

app.include_router(router)