from fastapi import Header, HTTPException
from env import GetWinnerEnv

async def verifyApiKey(get_winner_key: str = Header(..., alias="get_winner_key")):
    if get_winner_key != GetWinnerEnv.KEY:
        raise HTTPException(status_code=403, detail="INVALID_API_KEY")