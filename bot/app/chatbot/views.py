import os
from flask import request, abort, url_for
from . import chatbot_bp as chatbot
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

LINE_MESSAGE_API_ACCESS_TOKEN = os.environ.get('LINE_MESSAGE_API_ACCESS_TOKEN')
LINE_MESSAGE_API_CLIENT_SECRET = os.environ.get('LINE_MESSAGE_API_CLIENT_SECRET')

# LINE_CLIENT_ID = os.environ.get('LINE_CLIENT_ID')
# LINE_CLIENT_SECRET = os.environ.get('LINE_CLIENT_SECRET')

line_bot_api = LineBotApi(LINE_MESSAGE_API_ACCESS_TOKEN)
handler = WebhookHandler(LINE_MESSAGE_API_CLIENT_SECRET)


@chatbot.route('/message/callback', methods=['POST'])
def line_message_callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text.lower() == 'hello':
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text='world!'))
