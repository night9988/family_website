import uuid,os

from fastapi import HTTPException,Cookie

valid_token_list=[]

async def create_token(username:str,password:str,user_list:dict):
    if username not in user_list:
        raise HTTPException(status_code=401,detail="用户不存在")
    if user_list[username]==password:
        
        token=str(uuid.uuid4())
        valid_token_list.append(token)
    else:
        raise HTTPException(status_code=401,detail="密码错误")
    return token

async def verify_token(token:str=Cookie(None)):
    if not token:
        raise HTTPException(status_code=401,detail="个人网站，非本网站指定用户禁止入内")

    if token not in valid_token_list:
        raise HTTPException(status_code=401,detail="登录状态已过期")

    return token