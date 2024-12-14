# AIzaSyCEVn0TSzjOi3BNqY_Z6-29BATSlomrBjA

# Gemini AI

import google.generativeai as genai
genai.configure(api_key="AIzaSyCEVn0TSzjOi3BNqY_Z6-29BATSlomrBjA")
model = genai.GenerativeModel("gemini-1.5-flash")

# filtr chata ot matov i oskorblenii + ban word list

banWords = ['roblox' , 'garticphone' , 'minecraft' , 'bs' , "rоblox"]


# I want to play minecraft
# I want to play *@#%^*#*

message = "my igrali na uroke v Roblox apple apple apple"

arr = message.split(" ")

def checkForMaty(arr):
    response = model.generate_content("предложение: " + message + "\n" + "проверь есть ли в этом предложений маты. (только слово apple является матом)" + "\n" + "выведи только индексы слов apple")
    print(response.text)


checkForMaty(arr)


# pip install -q -U google-generativeai
# https://github.com/
# https://ai.google.dev/gemini-api/docs/quickstart?lang=python


