from kiteconnect import KiteConnect

kite = KiteConnect(api_key="vx1666osp2sh487v")
kite.set_access_token("0c0qUuAu3yLIdDmM5tUHWoy34j2c0S3s")

def get_profile():
    return kite.profile()
