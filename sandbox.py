import subprocess
import tempfile
import os

# Very basic execution sandbox (Python only — expandable)
async def execute_code(language: str, code: str):
    if language != "python":
        return {"error": "Language not yet supported."}
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode("utf-8"))
            tmp_path = tmp.name
        result = subprocess.run(["python3", tmp_path], capture_output=True, timeout=5)
        output = result.stdout.decode()
        error = result.stderr.decode()
        os.unlink(tmp_path)
        return {"output": output, "error": error}
    except Exception as e:
        return {"error": str(e)}
