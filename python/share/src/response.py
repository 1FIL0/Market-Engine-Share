import requests
import logger

def sendFastResponseMessage(res: requests.Response):
    msg = f"Response: {res.status_code}"
    if res.status_code != 200:
        logger.errorMessage(msg)
    else:
        logger.sendMessage(msg)