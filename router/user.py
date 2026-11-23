import json

from fastapi import APIRouter,Response,Depends
from fastapi.responses import HTMLResponse,JSONResponse

from config import USER_PATH,HTML_HOME,SIGN_IN
from schemas.user import SignInRequest
from auth.auth import create_token,verify_token
router=APIRouter()

@router.get("/",response_class=HTMLResponse)
async def sign_in():
    with open(SIGN_IN,"r",encoding="utf-8") as f:
        html=f.read()
    return html

@router.post("/sign",response_class=JSONResponse)
async def get_token(user:SignInRequest,response:Response):
    username=user.username
    password=user.password
    with open(USER_PATH,"r",encoding="utf-8") as f:
        user_list=json.load(f)
    token=await create_token(username,password,user_list)
    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        path="/",
        max_age=86400*7
    )

@router.get("/root",response_class=HTMLResponse)
async def welcome(token:str=Depends(verify_token)):
    with open(HTML_HOME,"r",encoding="utf-8") as f:
        html=f.read()
    return html