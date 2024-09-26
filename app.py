# FastAPI api app for processing images
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

    
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    nombre = "Hacking"
    apellido = "Tecnologias del futuro"
    comando = "Integración continua y hacking"
    data = {"nombre":nombre, "apellido": "apellido":apellido, "comando":comando}
    return {"message": data}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/openapi.json")
async def get_openapi():
    return JSONResponse(get_openapi(title="FastAPI", version=1, routes=app.routes))


