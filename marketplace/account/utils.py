import json
import os
import random
import requests
import string
from django.utils.text import slugify
from io import BytesIO

def send_otp(phone):
    if phone:
        
        key = random.randint(999, 9999)
        phone = str(phone)
        otp_key = str(key)

        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=b3628db0-ce73-11eb-8089-0200cd936042&to={phone}&from=HMESHF&templatename=SMSTemp&var1=USER&var2={otp_key}'
        result = requests.get(link, verify=False)

        return otp_key

import uuid
def generate_ref_code():
    code = str(uuid.uuid4()).replace('-','')[:12]
    return code



