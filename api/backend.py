import os.path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/share-target")
def share_target(request: Request):
    return request.query_params._dict

app.mount(
    path="/",
    app=StaticFiles(
        directory=os.path.join(os.path.dirname(__file__), "../www/"),
        html=True
    ),
    name="Frontend"
)