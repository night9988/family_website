import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

STATIC_DIR=os.path.join(BASE_DIR,"static")
USER_DIR=os.path.join(BASE_DIR,r"data\user")


USER_PATH=os.path.join(USER_DIR,"user.json")
HTML_HOME=os.path.join(STATIC_DIR,"home.html")
SIGN_IN=os.path.join(STATIC_DIR,"sign_in.html")
TOKEN=os.path.join(USER_DIR,"token.json")

