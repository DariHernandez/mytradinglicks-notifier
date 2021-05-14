import requests

def telegram_bot_sendtext(bot_message, chat_ids):
    """
    Use bot for send enssage to specific chat
    """

    # Updates: https://api.telegram.org/bot1853683882:AAH_4aToI5HY8DNwC4M0nCQmyuTnKmKjoLc/getUpdates
    responses = []

    for chat_id in chat_ids:
        bot_token = '1853683882:AAH_4aToI5HY8DNwC4M0nCQmyuTnKmKjoLc'
        bot_chatID = chat_id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        responses.append(requests.get(send_text))
    
    return responses
