from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/share-target")
def share_target(request: Request):
    return request.query_params._dict