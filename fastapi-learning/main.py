from fastapi import FastAPI

app = FastAPI()

# TODO 1: Register GET /health.
# Return {"status": "ok"}.
@app.get("/health")
async def health():
    return {"status": "ok"}


# TODO 2: Register GET /projects/{project_id}.
# project_id should be int.
# verbose should be bool, default False.
# Return both values in a dictionary.

@app.get("/projects/{projectId}")
async def getProject(projectId: int, verbose: bool = False):
    return {"project_id": projectId, "verbose": verbose}
