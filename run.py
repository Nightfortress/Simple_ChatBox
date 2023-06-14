

import openai
print('ss')
print('dd')
openai.api_key = "put your API key here"

def textResponse(messages):
    
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    response = completion.choices[0].message
    print("ChatBot: ", response['content'])
    messages.append({"role":"assistant", "content":response['content']})

    return messages

def imageResponse(message):
    response = openai.Image.create(
        prompt = f"{message}",
        n=2,
        size= "512x512"
    )
    print("your image can be found under this link!", str(response['data'][0]['url']))
    

def main():
    
    messages = []
    while True:

        choice = input("type chat or image or exit ")
        
        if choice == 'chat':
            message = input(" type your message ")
            messages.append({"role":"user", "content":f"{message}"})
            messages = textResponse(messages)
            
        elif choice == 'image':
            message = input("what image do you want me to generate ")
            imageResponse(message)
            
        
        elif choice =='exit':
          break

        else:
            print("Wrong command.. try again!")
            choice = input("type chat or image or exit ")

main()