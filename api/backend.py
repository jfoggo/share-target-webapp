# required modules (see requirements.txt)
import os.path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# initializie fastapi application
app = FastAPI()

# serve static files (from 'www' directory)
app.mount(
    path="/",
    app=StaticFiles(
        directory=os.path.join(os.path.dirname(__file__), "../www/"),
        html=True
    ),
    name="Frontend"
)