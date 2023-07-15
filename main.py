from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_interaction_to_chat_log
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '8wLs1T3BlbkFJUJ5BxAcvjbvkjgffvrOjUcAMsdcevevwdsvdX7njo7vjvhj8nmb'

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    from testingpromax import chatbotHandler
    answer = chatbotHandler(incoming_msg)
    msg = MessagingResponse()
    msg.message(answer)
   
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
    
