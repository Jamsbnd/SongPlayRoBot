import os
API_ID = int(os.getenv("11574784"))
API_HASH = os.getenv("f3a679a6171fb564f6d8b8ba8bf777de")
BOT_TOKEN = os.getenv("5164991910:AAHDQaMG-gfKool8_WTi-oVEh4lvX8Mx_ZA")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
