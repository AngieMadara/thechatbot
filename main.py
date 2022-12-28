from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_interaction_to_chat_log
# import sqlite3

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '8wLs1T3BlbkFJUJ5BxArOjUcAMX7njo78'


# def get_memory(conversation_id):
#   connection = sqlite3.connect("memory.db")
#   cursor = connection.cursor()
#   cursor.execute(f"SELECT * FROM conversations WHERE conversation_id='{conversation_id}'")
#   result = cursor.fetchone()
#   connection.close()
#   if result:
#     return result[1]
#   else:
#     return ""

# def add_to_memory(conversation_id, message):
#   connection = sqlite3.connect("memory.db")
#   cursor = connection.cursor()
#   cursor.execute(f"INSERT INTO conversations VALUES ('{conversation_id}', '{message}')")
#   connection.commit()
#   connection.close()


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    # conversation_id = request.values["From"]
    print(incoming_msg)

    chat_log = session.get('chat_log')
    # answer = ask(incoming_msg, chat_log)
    
    # memory = get_memory(conversation_id)
    # add_to_memory(conversation_id, incoming_msg)
    prompt = f"{memory}\n{incoming_msg}"
    response = ask(prompt, chat_log)
    add_to_memory(conversation_id, response)

    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    msg = MessagingResponse(response)
    msg.message(response)
    print(response)
    print(msg)
   
    return str(msg)



if __name__ == '__main__':
    app.run(debug=True)