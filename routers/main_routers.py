from fastapi import APIRouter
from routers.common_routers import router as common_router
from routers.board_routers import router as board_router

api_router = APIRouter(prefix = "/v1")
api_router.include_router(common_router)
api_router.include_router(board_router)