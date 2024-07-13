# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28002029")

API_HASH = os.environ.get("API_HASH", "8580ae9cf42255112cf4a302673b2f8f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7476808785:AAGyq9FJYWzXjM9DYiBVhknj1xFcpqy4FOs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "SR_MOVI") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://fedom33658:wieOPXioVtlb32P3@sagar.bxdcweo.mongodb.net/?retryWrites=true&w=majority&appName=Sagar")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1340901101').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
