"""
Replacement for vcpb/config/__init__.py
"""
import ast
from os import environ
from pyrogram import filters

API_ID = "1566635"
API_HASH = "407389a923d7a47a31b0deaeb22d24ae"
TOKEN = "1416304053:AAFkAx7Fr4A0V3ZkySAbzGPEwkh5Hj-WMgc"
SUDO_USERS = "695291232"
GROUP = "-1001440655092"
MONGO_DB_URI = ""
USERS_MUST_JOIN = "true"
LANG = "en"
DUR_LIMIT = "10"

API_ID = int(API_ID)
SUDO_USERS = list(map(int, SUDO_USERS.split()))

if type(GROUP) == str:
    GROUP = int(GROUP)

DUR_LIMIT = int(DUR_LIMIT)
USERS_MUST_JOIN = ast.literal_eval(USERS_MUST_JOIN)
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)


async def custom_filter(_, __, ___):
    return bool(LOG_GROUP)

LOG_GROUP_FILTER = filters.create(custom_filter)
