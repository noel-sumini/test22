from fastapi import APIRouter

router = APIRouter(prefix="/common")

@router.get("/ping", status_code=200)
def health_cheak():
    return {"msg": "pong"}