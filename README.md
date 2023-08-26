# ChatGpt-API

# Configuration
1.Create account on OpenAI's ChatGPT

2.Save your email and password

# Authentication methods: (Choose one)
- Email/Password
```python
{
  "email": "email",
  "password": "your password"
}
```

- Access token
https://chat.openai.com/api/auth/session
```python
{
  "access_token": "<access_token>"
}

```

# Usage
Basic example (streamed):
```python
from revChatGPT.V1 import Chatbot
chatbot = Chatbot(config={
  "access_token": "<your access_token>"
})
print("Chatbot: ")
prev_text = ""
for data in chatbot.ask(
    "Hello world",
):
    message = data["message"][len(prev_text) :]
    print(message, end="", flush=True)
    prev_text = data["message"]
print()
```

Basic example (single result):
```python
from revChatGPT.V1 import Chatbot
chatbot = Chatbot(config={
  "access_token": "<your access_token>"
})
prompt = "how many beaches does portugal have?"
response = ""
for data in chatbot.ask(
  prompt
):
    response = data["message"]
print(response)
```
