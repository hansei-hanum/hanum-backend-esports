from fastapi import FastAPI 
from .luckydraw.getDraw import router as getDrawRouter
from .luckydraw.getWinner import router as getWinnerRouter

def include_router(app: FastAPI):
    app.include_router(getDrawRouter)
    app.include_router(getWinnerRouter)