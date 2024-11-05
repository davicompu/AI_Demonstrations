import streamlit as st
import requests

# Streamlit app
def main():
  st.title("Talk to OLLAMA Agent")

  # Input field for user message
  user_input = st.text_input("Type your message here:")

  if st.button("Send"):
      if user_input:
          # Call the OLLAMA API
          response = call_ollama_api(user_input)
          if response:
              st.write("**Agent:**", response)
          else:
              st.write("**Error:** Could not get a response from the agent.")
      else:
          st.write("Please enter a message.")

def call_ollama_api(message):
    # data = response.json()
    return {'reply':'response'}
#   api_url = "https://api.ollama.com/agent"  # Replace with your actual API endpoint
#   api_key = "YOUR_API_KEY"  # Replace with your actual API key

#   headers = {
#       "Content-Type": "application/json",
#       "Authorization": f"Bearer {api_key}"
#   }

#   payload = {
#       "message": message
#   }

#   try:
#       response = requests.post(api_url, headers=headers, json=payload)
#       response.raise_for_status()  # Raise an error for bad responses
#       data = response.json()
#       return data.get("reply", "No reply field in response.")
#   except requests.exceptions.RequestException as e:
#       st.error(f"Request failed: {e}")
#       return None

if __name__ == "__main__":
  main()