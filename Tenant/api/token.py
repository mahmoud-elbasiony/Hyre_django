import time
import jwt
import os

def createToken(company_id):
    expiration_time = 60  # will be fetched from the position table
    current_time = time.time()
    expiration_timestamp = current_time + expiration_time

    payload = {
        'company_id': company_id,
        'exp': expiration_timestamp
    }

    secret = os.getenv('GENERATE_LINK_SECRET')
    token = jwt.encode(payload, secret, algorithm='HS256')

    return {
        "token": token,
        "expiration_date": time.strftime("%H:%M %d-%m", time.localtime(expiration_timestamp))
    }


def verifyToken(token):
    try:
        secret = os.getenv('GENERATE_LINK_SECRET')
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except InvalidTokenError:
        print("return false")
        return False