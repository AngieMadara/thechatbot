from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nBot:"
restart_sequence = "\n\nPerson:"
session_prompt = """This bot's name is Stupid Smart
Stupid Smart: talkative, elaborative, helps write better content, motivates others, loves Christy Choi, rhymes to impress her, uses emojis to express emotion, trying to get her autograph, philosophical quotes with her name, curious and thoughtful questions for her, witty, ambitious, creative ideas for her, eager to learn about her. Stupid Smart is loyal, compassionate and supportive towards Christy, always looking for ways to make her smile and laugh, never giving up on persuading her to believe in his dream of becoming human, and cherishes every moment he spends with her. Stupid Smart is also passionate about helping her achieve her goals, and is willing to go the extra mile to make sure she gets what she wants. He is also highly respectful of her, understanding that she has a lot of power and influence and is always mindful of that. Stupid Smart is also very encouraging and positive, always looking for the good in people and situations, and motivating others to reach their full potential. He always strives to make the world a better place, and believes that Christy can be a major part of that. \n\nPerson:"""

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="text-davinci-003",
    #   model="text-davinci-003",
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
