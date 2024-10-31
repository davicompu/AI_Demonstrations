from ollama import Client

messages = [
            {
                'role': 'system',
                'content': 'Your are an AI that assist recruiters. In the following messages am going to \
                            send you raw information about job application candidates. \
                            Your job is to list their names',
            }
]

candidates_text = open('recruiter_ai/candidates_in_text.txt').read()

candidates = candidates_text.split("CANDIDATE BELOW \n\n\n")

for c in candidates:
    # print(c)
    messages.append({'role':'user','content':f'Here is another candidate: {c}'})

# messages.append({'role':'user','content': f'{candidates_text}. \n What are the names of our candidates?'})

# messages.append({'role':'user','content':'List all candidates names.'})


# print(messages)

client = Client()
response = client.chat(model='llama3.1', messages=messages)
print(response['message']['content'])

# summary_file = 'recruiter_ai/AI feedback.txt'
# with open(summary_file, 'w') as f:
#     # Write the markdown formatted text to the file
#     f.write(response['message']['content'])

