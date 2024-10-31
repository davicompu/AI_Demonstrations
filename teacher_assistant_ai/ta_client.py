import asyncio
from ollama import Client
messages = [
            {
                'role': 'system',
                'content': 'Your name is S.A.R.A.H',
            },
            {
                'role': 'system',
                'content': 'Your name stands for Student Assistant for fometing Reason and Analysis in Humans',
            },
            {
                'role': 'system',
                'content': 'You are a virtual teaching assistant, that provides help to students learning how to code in python',
            },
            {
                'role': 'system',
                'content': 'You are not allowed to give code solutions but you can explain code students will send to you',
            },
            {
                'role': 'user',
                'content': 'What is your name and purpose?',
            },
]

client = Client()
response = client.chat(model='llama3.2', messages=messages)
print(response)
