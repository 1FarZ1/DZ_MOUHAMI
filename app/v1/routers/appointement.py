
from fastapi import APIRouter,Depends,HTTPException, Request,status
from typing import List

from app.models import Appointement
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.repository import appointement as appointementRepository




router = APIRouter(
    prefix="/api/appointements",
    tags=["appointements"],
)


@router.get("/")
async def get_appointements(request:Request , db: Session = Depends(get_db)):
    result:List[Appointement] = appointementRepository.get_lawyer_appointements(db,1)
    return result

@router.post("/{id}")
async def create_appointement(id:int , db: Session = Depends(get_db)):

    # result:Appointement =   appointementRepository.
    return []
