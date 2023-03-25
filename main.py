# import os
# if __name__== '__main__':
#     print("Wlcome to robo speker!")
#     x= input("Enter your word do you want speak: ")
#     comman= f"say {x}"
#     os.system(comman)
import pyttsx3

if __name__== '__main__':
    print("Welcome to AI speaker! Created by Sayed Al Mamoon!")
    while True:
        x = input("Enter the word you want to speak: ")
        if x == "q":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
