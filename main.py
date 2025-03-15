from fastapi import FastAPI
from routers.main_routers import api_router


app = FastAPI(
    title="sk_networks",
    version="0.0.1"
)

app.include_router(api_router)