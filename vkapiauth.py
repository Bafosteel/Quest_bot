import vk_api
import random
from settings import token

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def send_msg(user_id, token, message, attachment = ""):
    vk.messages.send(
        message=message,
        random_id=random.getrandbits(64),
        peer_id=str(user_id))
