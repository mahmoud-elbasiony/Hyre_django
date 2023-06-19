import os
import jwt
import time
from jwt.exceptions import InvalidTokenError

def createToken(company_id):
    expiration_time = 60 # will be fetched from the position table
    payload = {
        'company_id': company_id,
        'exp':  time.time() + expiration_time
    }
    secret = os.getenv('GENERATE_LINK_SECRET')
    token = jwt.encode(payload, secret, algorithm='HS256')  # 1 hour expiration
    return token

def verifyToken(token):
    try:
        secret = os.getenv('GENERATE_LINK_SECRET')
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except InvalidTokenError:
        print("return false")
        return False