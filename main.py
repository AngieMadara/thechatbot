from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = 'nd23hc823hdcdcdcbhjgug7g8g89bkh70923h3j2nc0393d2d23'

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    from testingpromax import chatbotHandler
    answer = chatbotHandler(incoming_msg)
    msg = MessagingResponse()
    msg.message(answer)
   
    return str(msg)

@app.route('/test', methods=['POST'])
def test():
    incoming_msg = request.values['Body']
    return incoming_msg

if __name__ == '__main__':
    app.run(debug=True)
    
