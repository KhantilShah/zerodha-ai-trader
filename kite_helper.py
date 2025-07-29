

# Commented out actual Kite API logic for now
# from kiteconnect import KiteConnect

# kite = KiteConnect(api_key="vx1666osp2sh487v")
# kite.set_access_token("0c0qUuAu3yLIdDmM5tUHWoy34j2c0S3s")
# kite_helper.py

import os
from kiteconnect import KiteConnect

API_KEY = os.getenv("vx1666osp2sh487v")
API_SECRET = os.getenv("x9x011cansvfqcbefot005xf858ogwop")
kite = KiteConnect(api_key=API_KEY)

def generate_login_url():
    return kite.login_url()

def generate_session(request_token: str):
    data = kite.generate_session(request_token, API_SECRET)
    kite.set_access_token(data["access_token"])
    return data

def get_profile():
    return kite.profile()

