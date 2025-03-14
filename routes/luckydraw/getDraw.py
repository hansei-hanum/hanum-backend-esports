from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.core import AsyncSessionLocal
from database import Luckydraws, DrawField
from sqlalchemy import select

router = APIRouter(prefix="/luckydraw")

class luckydrawRequest(BaseModel): 
    school : str 
    studentNumber : str 
    name : str 

@router.post("/getDraw")
async def getDraw(data: luckydrawRequest):
    
    if data.school not in ['HANSEI', 'SEMYEONG']:
        raise HTTPException(status_code=400, detail="WRONG_SCHOOL_NAME")
    
    async with AsyncSessionLocal() as session: 
        
        result = await session.execute(
            select(DrawField)
            .where(DrawField.isActive == True)
        )
        activeDrawField = result.scalar_one_or_none()
        
        if not activeDrawField:
            raise HTTPException(status_code=400, detail="NOT_ACTIVE_YET")
        
        if len(data.name) > 10 or len(data.studentNumber) > 10:
            raise HTTPException(status_code=400, detail="DATA_IS_TOO_LONG")
        
        result = await session.execute(
            select(Luckydraws)
            .where(
                (Luckydraws.userStudentNumber == data.studentNumber) &
                (Luckydraws.drawFieldId == activeDrawField.id)
            )
        ) 
        existingUser = result.scalar_one_or_none()
        
        if existingUser:
            raise HTTPException(status_code=400, detail="ALREADY_DRAWED")
        
        dbValue = Luckydraws(
            userSchool = data.school,
            userStudentNumber = data.studentNumber,
            userName = data.name,
            drawFieldId = activeDrawField.id,
            isWinner = False
        )
        session.add(dbValue)
        await session.commit()
        
        return {
            "message":"SUCCESS",
            "data" : {
                "userSchool" : data.school,
                "userStudentNumber" : data.studentNumber,
                "userName" : data.name
            }
        }
        