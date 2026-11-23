from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles

from router import user

app=FastAPI()

@app.exception_handler(HTTPException)
async def unauthorized_redirect(request:Request,exc:HTTPException):
    if request.url.path=="/sign":
        return JSONResponse(status_code=exc.status_code,content={"detail":exc.detail})
    if exc.status_code==401:
        return RedirectResponse(url="/",status_code=302)
    return JSONResponse(status_code=exc.status_code,content={"detail":exc.detail})

app.mount("/static",StaticFiles(directory="static"),name="static")

app.include_router(user.router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)