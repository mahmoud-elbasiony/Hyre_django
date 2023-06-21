import time
import jwt
import os

def createToken(company_id, expiration_date):
    expiration_timestamp = expiration_date.timestamp()

    payload = {
        'company_id': company_id,
        'exp': expiration_timestamp
    }

    secret = os.getenv('GENERATE_LINK_SECRET')
    token = jwt.encode(payload, secret, algorithm='HS256')

    return {
        "token": token,
        "expiration_date": expiration_date.strftime("%H:%M %d-%m")
    }


def verifyToken(token):
    try:
        secret = os.getenv('GENERATE_LINK_SECRET')
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.InvalidTokenError:
        print("return false")
        return False