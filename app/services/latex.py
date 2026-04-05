import os
import uuid
import subprocess
from app.models.schemas import CompileRequest
from app.utils.security import sanitize_latex
from app.core.config import settings

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(settings.TMP_DIR, exist_ok=True)


async def compile_latex_files(request: CompileRequest):
    outputs = []

    for file in request.files:
        job_id = str(uuid.uuid4())

        tex_path = os.path.join(settings.TMP_DIR, f"{job_id}.tex")
        pdf_tmp_path = os.path.join(settings.TMP_DIR, f"{job_id}.pdf")
        pdf_final_path = os.path.join(OUTPUT_DIR, f"{job_id}.pdf")

        content = sanitize_latex(file.content)

        with open(tex_path, "w") as f:
            f.write(content)

        process = subprocess.run(
            ["tectonic", tex_path, "--outdir", settings.TMP_DIR],
            capture_output=True,
            text=True,
            timeout=settings.TIMEOUT
        )

        if process.returncode != 0:
            raise Exception(f"LaTeX failed:\n{process.stderr}")

        if not os.path.exists(pdf_tmp_path):
            raise Exception("PDF not generated")

        # Move to public folder
        os.rename(pdf_tmp_path, pdf_final_path)

        outputs.append({
            "filename": file.filename.replace(".tex", ".pdf"),
            "url": f"http://localhost:8000/files/{job_id}.pdf"
        })

    return {"outputs": outputs}