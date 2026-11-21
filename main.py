import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
STATIC_DIR=os.path.join(BASE_DIR,"static")

HTML_HOME=os.path.join(STATIC_DIR,"home.html")

@app.get("/",response_class=HTMLResponse)
async def get_html():
    with open(HTML_HOME,"r",encoding="utf-8") as f:
        html=f.read()
    return html



if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="::",port=8000,reload=True)