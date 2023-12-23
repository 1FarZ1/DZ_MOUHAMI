from fastapi import APIRouter
from app.models.user import User
from app.config.database import db

router = APIRouter(
    prefix="/api/users",
)


# get All Users
@router.get("/")
async def get_users():
    result:List[User] = db.query(User).all() 
    return result

@router.get("/users/{id}")
async def get_user(id: int):
    result:User = db.query(User).filter(User.id == id).first()
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result



