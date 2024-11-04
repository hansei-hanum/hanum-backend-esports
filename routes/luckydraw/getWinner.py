from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from database.core import AsyncSessionLocal
from database import Luckydraws, DrawField
from sqlalchemy import select, func
from env import GetWinnerEnv
from depends import verifyApiKey

router = APIRouter(prefix="/luckydraw")

@router.get("/getWinner")
async def getWinner(api_key: str = Depends(verifyApiKey)):
    async with AsyncSessionLocal() as session:
        
        result = await session.execute(
            select(DrawField)
            .where(DrawField.isActive == True)
        )
        activeDrawField = result.scalar_one_or_none()
        
        if not activeDrawField: 
            raise HTTPException(status_code=404, detail="ACTIVE_DRAW_FIELD_NOT_FOUNDED")
        
        result = await session.execute(
                select(Luckydraws)
                .where(Luckydraws.drawFieldId == activeDrawField.id)
                .order_by(func.random())
                .limit(2)  
            )
        winners = result.scalars().all()
        
        if not winners:
            raise HTTPException(status_code=404, detail="WINNER_NOT_FOUNDED")
        
        return {
            "message":"SUCCESS",
            "data": [
                {
                    "userSchool": winner.userSchool,
                    "userStudentNumber": winner.userStudentNumber,
                    "userName": winner.userName,
                    "drawFieldId": winner.drawFieldId,
                }
                for winner in winners
            ]
        }