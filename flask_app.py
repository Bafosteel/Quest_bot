
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,request, json
from settings import confirmation_token, token
import vk_api
import messageHandler

app = Flask(__name__)
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'this is not vk data'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        print(data['object']['user_id'])
        print(data)
        user_id = data['object']['user_id']
        # отправляем сообщение
        messageHandler.create_answer(data['object'], token)
        return 'ok'