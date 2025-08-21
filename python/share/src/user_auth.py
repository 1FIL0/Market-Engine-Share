from typing import Callable
import requests
import definitions
import keyring
from requests.exceptions import RequestException
import logger

# MIGHT BE CALLED FROM FLASK SERVER THREAD

class UserData:
    def __init__(self):
        self.email: str
        self.premiumHint: bool

g_keyringServiceName = "Market Engine"
g_keyringUsername = "Market Engine User"
g_user: UserData
g_userValidatedCallback = None

def tryAutologin() -> None:
    res = validateToken(getKeyringToken())
    if not res.status_code == 200: return
    constructUser(res)
    if g_userValidatedCallback:
        g_userValidatedCallback()

def processServerToken(token: str) -> None:
    res = validateToken(token)
    if not res.status_code == 200: return
    constructUser(res)
    saveKeyringToken(token)
    if g_userValidatedCallback:
        g_userValidatedCallback()

def validateToken(token: str) -> requests.Response:
    res: requests.Response = requests.Response()
    try:
        res = requests.post(definitions.URL_MARKET_ENGINE_VALIDATE_TOKEN, json={"token": token})
    except RequestException as e:
        logger.sendMessage(f"Token Validation failed: {e}")
        return res

    if res.status_code != 200:
        logger.sendMessage("Denied: " + str(res.status_code))
    return res

def constructUser(res: requests.Response) -> None:
    global g_user
    g_user = UserData()
    data = res.json()
    g_user.email = data["email"]
    g_user.premiumHint = data["premium"]

def getUser() -> UserData:
    return g_user

def getKeyringToken() -> str:
    token: str = str(keyring.get_password(g_keyringServiceName, g_keyringUsername))
    return token

def saveKeyringToken(token: str) -> None:
    keyring.set_password(g_keyringServiceName, g_keyringUsername, token)

def setUserValidatedCallback(callback: Callable[[], None]) -> None:
    global g_userValidatedCallback
    g_userValidatedCallback = callback

