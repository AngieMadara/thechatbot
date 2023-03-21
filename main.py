from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
# from bot import ask, append_interaction_to_chat_log

from dotenv import load_dotenv
from random import choice
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"
completion = openai.Completion()



# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values['Body']
    
#     if "Main Menu" in incoming_msg or "menu" in incoming_msg or "main menu" in incoming_msg:
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "purpose" in incoming_msg.lower():
#         answer = '''
#             Our Purpose, Who are we = "Building a technology startup can be an exciting and rewarding journey. 
#             As a woman looking to convert your business idea into a technology business, 
#             it's essential to have a clear roadmap to guide you along the way. 
#             Here's our guide to help you build a technology startup 🏗️💻🚀
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "go back home" in incoming_msg.lower():
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "go back home" == incoming_msg.lower():
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "topic sequence" == incoming_msg.lower() or "what is topic sequence" == incoming_msg.lower():
#         answer = '''
#             - Topic Sequences \n
#             - Objectives \n
#             - Content \n
#             - Essential Essential Questions \n
#             - Identify a problem to solve\n
#             - Resources \n
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)

#     if "1" == incoming_msg.lower() or "Option 1" in incoming_msg.lower():
#         answer = '''
#             You Can Choose a Topic Below 
#             Topic 1 - Idea Validation
#             Topic 2 - Business Planning
#             Topic 3 - Product Development
#             Topic 4 - User Acquisition
#             Topic 5 - Funding and Finance
#             Topic 6 - Growth and Scaling
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     chat_log = session.get('chat_log')
#     answer = ask(incoming_msg, chat_log)
#     # session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
#                                                         #  chat_log)
#     msg = MessagingResponse()
#     msg.message(answer)
#     print(answer)
#     print(msg)
   
#     return str(msg)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request
import requests
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '8wLs1T3BlbkFJUJ5BxAcvjbvkjgffvrOjUcAMX7njo78'


menu_options = {
    '1': {
        'name': 'Learn',
        'topics': [
            {
                'name': 'Idea Validation',
                'objectives': 'To learn how to validate a business idea by engaging with potential customers. 📈👥💭',
                'content': 'Identify a problem to solve: Start by identifying a problem that you are passionate about solving. Identify your target audience and their needs: Determine who your target customers are, what their pain points are, and how your product or service can solve their problems.',
                'resources': 'Read "The Mom Test" by Rob Fitzpatrick to learn how to effectively validate your business idea. 📖💡🤔\nWatch "How to Validate Your Startup Idea" by Y Combinator on YouTube - https://www.youtube.com/watch?v=CGlGp-B6oM8 📹💻👀'
            },
            {
                'name': 'Topic 2',
                'objectives': 'Objectives for topic 2',
                'content': 'Content for topic 2',
                'resources': 'Resources for topic 2'
            },
            {
                'name': 'Topic 3',
                'objectives': 'Objectives for topic 3',
                'content': 'Content for topic 3',
                'resources': 'Resources for topic 3'
            },
            {
                'name': 'Topic 4',
                'objectives': 'Objectives for topic 4',
                'content': 'Content for topic 4',
                'resources': 'Resources for topic 4'
            },
            {
                'name': 'Topic 5',
                'objectives': 'Objectives for topic 5',
                'content': 'Content for topic 5',
                'resources': 'Resources for topic 5'
            },
            {
                'name': 'Topic 6',
                'objectives': 'Objectives for topic 6',
                'content': 'Content for topic 6',
                'resources': 'Resources for topic 6'
            }
        ]
    },
    '2': {
        'name': 'Ask a Question',
        'topics': []
    }
}

start_sequence = "\nBot:"
restart_sequence = "\n\nPerson:"
session_prompt = """
I am athenabot, My name is athenabot.
__

Our Purpose, Who are we = "Building a technology startup can be an exciting and rewarding journey. 
As a woman looking to convert your business idea into a technology business, 
it's essential to have a clear roadmap to guide you along the way. 
Here's our guide to help you build a technology startup 🏗️💻🚀"

"""

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values['Body'].lower()
    resp = MessagingResponse()
    
    if 'menu' in incoming_msg or 'main menu' in incoming_msg:
        # Show menu options
        message = resp.message()
        message.body('Main Menu:\n1 - Learn\n2 - Ask a Question')
    
    
        return str(message)
        
    elif incoming_msg == '1':
        # Show topics for Learn
        message = resp.message()
        message.body('Choose a topic to learn about:')
        for i, topic in enumerate(menu_options['1']['topics']):
            message.body(f'{i+1}. {topic["name"]}')
        session['current_topic'] = None
        return str(message)
        
        
    elif incoming_msg in ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6']:
        # Show topic content
        topic_num = int(incoming_msg.split('.')[1]) - 1
        topic = menu_options['1']['topics'][topic_num]
        message = resp.message()
        message.body(f'{topic["name"]}:\n{topic["objectives"]}\n\n{topic["content"]}\n\nResources:\n{topic["resources"]}')
        message = resp.message()
        message.body('Say "continue" to see the next section.')
        message.media('https://media.giphy.com/media/26xBwdIuRJiAIqHwA/giphy.gif')
        session['current_topic'] = topic_num
        session['current_section'] = 0
        return str(message)
        
        
    elif incoming_msg == 'continue':
        # Show next section
        message = resp.message()
        if 'current_topic' not in session:
            message.body('Please choose a topic first.')
            return str(message)

        current_topic = session['current_topic']
        current_section = session.get('current_section', 0)
        topic = menu_options['1']['topics'][current_topic]
        sections = [topic['objectives'], topic['content'], topic['resources']]
        if current_section == len(sections):
            # If all sections have been shown, reset session and return to topic selection
            session.pop('current_topic', None)
            session.pop('current_section', None)
            message.body('You have reached the end of this topic. Please choose another topic to learn about.')
            return str(message)
        else:
            # Show the next section
            message.body(sections[current_section])
            session['current_section'] = current_section + 1
            return str(message)
    else:
        prompt_text = f'{session_prompt}{restart_sequence}: {incoming_msg}{start_sequence}:'
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            # model="text-davinci-003",
            prompt=prompt_text,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.3,
            stop=["\n"],
        )
        message = resp.message()
        message.body(response['choices'][0]['text'])
    
        return str(message)
    

if __name__ == '__main__':
    app.run(debug=True)