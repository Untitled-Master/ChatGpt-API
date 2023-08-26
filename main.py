from revChatGPT.V1 import Chatbot
chatbot = Chatbot(config={
  "access_token": "your_access_token"
})
prompt = "who are you?"
response = ""
for data in chatbot.ask(
  prompt
):
    response = data["message"]
print(response)
