import uuid,json,time

from fastapi import HTTPException,Cookie

from config import TOKEN

Token_Expired_Time=24*60*60

#用于个人网站，以及为了方便之后的账号、Token管理，我选择直接将user、token表直接存储在本地文件上
#可根据你自己的需求来选择，是否连接数据库存储user、token
async def create_token(username:str,password:str,user_list:dict):
    if username not in user_list:
        raise HTTPException(status_code=401,detail="用户不存在")
    if user_list[username]==password:
        token=str(uuid.uuid4()) 
        with open(TOKEN,"r",encoding="utf-8") as f:
            try:
                valid_token_list=json.load(f)
            except json.JSONDecodeError:
                valid_token_list={}
        current_time=time.time()
        Expired_Time=current_time+Token_Expired_Time
        valid_token_list[token]=Expired_Time
        with open(TOKEN,"w",encoding="utf-8") as f:
            json.dump(valid_token_list,f,indent=4)
    else:
        raise HTTPException(status_code=401,detail="密码错误")
    return token

async def verify_token(token:str=Cookie(None)):
    if not token:
        raise HTTPException(status_code=401,detail="个人网站，非本网站指定用户禁止入内")
    with open(TOKEN,"r",encoding="utf-8") as f:
        valid_token_list=json.load(f)
    if token not in valid_token_list:
        raise HTTPException(status_code=401,detail="登录状态已过期")
    current_time=time.time()
    if current_time>valid_token_list[token]:
        del valid_token_list[token]
        with open(TOKEN,"w",encoding="utf-8") as f:
            json.dump(valid_token_list,f,indent=4)
        raise HTTPException(status_code=401,detail="登录状态已过期")

    return token