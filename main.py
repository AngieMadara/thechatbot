from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_interaction_to_chat_log

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '8wLs1T3BlbkFJUJ5BxAcvjbvkjgffvrOjUcAMX7njo78'



@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    
    if "Main Menu" in incoming_msg or "menu" in incoming_msg or "main menu" in incoming_msg:
        answer = '''
            Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
            1: Learn 📚
            2: Ask a question 🙋🏻‍♀️
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)
    
    if "purpose" in incoming_msg.lower():
        answer = '''
            Our Purpose, Who are we = "Building a technology startup can be an exciting and rewarding journey. 
            As a woman looking to convert your business idea into a technology business, 
            it's essential to have a clear roadmap to guide you along the way. 
            Here's our guide to help you build a technology startup 🏗️💻🚀
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)
    
    if "go back home" in incoming_msg.lower():
        answer = '''
            Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
            1: Learn 📚
            2: Ask a question 🙋🏻‍♀️
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)
    
    if "go back home" == incoming_msg.lower():
        answer = '''
            Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
            1: Learn 📚
            2: Ask a question 🙋🏻‍♀️
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)
    
    if "topic sequence" == incoming_msg.lower() or "what is topic sequence" == incoming_msg.lower():
        answer = '''
            - Topic Name
            - Objectives
            - Content
            - Essential Essential Questions 
            - Identify a problem to solve
            - Resources 
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)

     if "1" == incoming_msg.lower() or "Option 1" in incoming_msg.lower():
        answer = '''
            - Topic Name
            - Objectives
            - Content
            - Essential Essential Questions 
            - Identify a problem to solve
            - Resources 
        '''
        msg = MessagingResponse()
        msg.message(answer)
        print(answer)
        print(msg)
    
        return str(msg)
    
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    # session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                        #  chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    print(answer)
    print(msg)
   
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
    