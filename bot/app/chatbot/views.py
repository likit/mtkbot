from . import chatbot_bp as chatbot


@chatbot.route('/message')
def message_handler(message):
    return 'What?'