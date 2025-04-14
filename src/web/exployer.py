from fastapi import APIRouter 

router = APIRouter(prefix="/exployer")

@router.get("/") # root
def top():
    return "top exployer here3"

