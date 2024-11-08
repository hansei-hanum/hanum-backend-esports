from fastapi import Header, HTTPException
from env import GetWinnerEnv

async def verifyApiKey(secret: str = Header(...)):
    if secret != GetWinnerEnv.KEY:
        raise HTTPException(status_code=403, detail="INVALID_API_KEY")