from json           import loads
from random         import choice
from utils.api      import Utils
from utils.sign     import sign
from utils.client   import get_client
from urllib.parse   import urlencode
from hashlib        import md5
from metasec_tt     import Signer


if __name__ == '__main__':
    devices = open('./data/devices.txt', 'r').read().splitlines()
    device  = loads(choice(devices))
    client  = get_client()
    phone   = '+XX XXXXXXXX'
    
    payload = urlencode({
        "check_register"    : 1,
        "auto_read"         : 1,
        "account_sdk_source": "app",
        "unbind_exist"      : 35,
        "mix_mode"          : 1,
        "mobile"            : Utils.encrypt(phone),
        "is6Digits"         : 1,
        "multi_login"       : 1,
        "type"              : 3731
    })
    
    params = Utils.get_params(device, '25.6.2')

    headers = {
        **Signer.sign(params, payload),
        "accept-encoding"           : "gzip",
        "sdk-version"               : "2",
        "passport-sdk-version"      : "19",
        "x-ss-req-ticket"           : "1675464756985",
        "x-tt-bypass-dp"            : "1",
        "x-vc-bdturing-sdk-version" : "2.2.1.i18n",
        "x-tt-dm-status"            : "login=0;ct=0;rt=7",
        "x-tt-store-region"         : "ie",
        "x-tt-store-region-src"     : "did",
        "x-tt-store-region-did"     : "ie",
        "x-tt-store-region-uid"     : "none",
        "content-type"              : "application/x-www-form-urlencoded; charset=UTF-8",
        "host"                      : "api16-normal-c-useast1a.tiktokv.com",
        "connection"                : "Keep-Alive",
    }

    req = client.post(f"https://api16-normal-c-useast1a.tiktokv.com/passport/mobile/send_code/v1/?{params}", 
        headers = headers, data = payload)
    
    print(req.json())
    
    {
        'data': {
            'mobile': '+XX****XXXX', 
            'mobile_ticket': 
            'mobile_ticket_XXXXXXXXXXXXXXXXXXXXXXX', 
            'retry_time': 60
        }, 
        'message': 'success'
    }
