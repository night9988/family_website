import os,json

from fastapi import FastAPI,Depends,Response,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles

from auth.auth import create_token,verify_token
from schemas.user import SignInRequest

app=FastAPI()
@app.exception_handler(HTTPException)
async def unauthorized_redirect(request:Response,exc:HTTPException):
    if exc.status_code==401:
        return RedirectResponse(url="/",status_code=302)
    return JSONResponse(status_code=exc.status_code,content={"detail":exc.detail})
app.mount("/static",StaticFiles(directory="static"),name="static")

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
STATIC_DIR=os.path.join(BASE_DIR,"static")
USER_DIR=os.path.join(BASE_DIR,r"data\user")

USER_PATH=os.path.join(USER_DIR,"user.json")
HTML_HOME=os.path.join(STATIC_DIR,"home.html")
SIGN_IN=os.path.join(STATIC_DIR,"sign_in.html")

with open(USER_PATH,"r",encoding="utf-8") as f:
    user_list=json.load(f)

@app.get("/",response_class=HTMLResponse)
async def sign_in():
    with open(SIGN_IN,"r",encoding="utf-8") as f:
        html=f.read()
    return html

@app.post("/sign",response_class=JSONResponse)
async def get_token(user:SignInRequest,response:Response):
    username=user.username
    password=user.password
    token=await create_token(username,password,user_list)
    response.set_cookie(
        key="family_token",
        value=token,
        httponly=True,
        path="/",
        max_age=86400*7
    )
    return {"message":"登录成功"}

@app.get("/root",response_class=HTMLResponse)
async def welcome(token:str=Depends(verify_token)):
    with open(HTML_HOME,"r",encoding="utf-8") as f:
        html=f.read()
    return html

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="::",port=8000,reload=True)