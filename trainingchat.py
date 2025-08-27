import json
import difflib
import time
import os
from colorama import init, Fore, Style

if os.name == "nt":
   os.system("cls")
else:
   os.system("clear")

os.system("python3 feed_bot.py")


init()

def find_closest_match(user_input, questions, cutoff=0.8):
    matches = difflib.get_close_matches(user_input.lower(), questions, n=1, cutoff=cutoff)
    return matches[0] if matches else None


def printdy(text, colorama1=Fore.WHITE):
  for i in text:
    if i.isdigit():
      print(colorama1 + Style.BRIGHT + i + Style.RESET_ALL, end='', flush=True)
    else:
      print(colorama1 + i + Style.RESET_ALL, end='', flush=True)
    time.sleep(0.034)
  time.sleep(1)
  print("")
  return None

f = open("training.json", 'r')
re = f.read()
values = json.loads(re)

questions = values["questions"]
answers = values["answers"]

f.close()

print(Fore.WHITE + """
╔═══╦╗
║╔═╗║║
║║─║║║╔══╦═╦═╗╔══╗
║╚═╝║║║║═╣╔╣╔╗╣╔╗║
║╔═╗║╚╣║═╣║║║║║╔╗║
╚╝─╚╩═╩══╩╝╚╝╚╩╝╚╝
""")

print(Fore.GREEN + "Learn,", Fore.CYAN + "Remeber,", Fore.LIGHTRED_EX + "Improve,", Fore.WHITE +  "Redo." + Fore.RESET + "\n")

while True:
    ask = input(Fore.WHITE + "Alerna $> ")
    match = find_closest_match(ask, questions)
    if "quit" in ask.lower():
        break

    if "refresh_screen" in ask.lower():
        if os.name == "nt":
            os.system("cls")
            print(Fore.WHITE + """
╔═══╦╗
║╔═╗║║
║║─║║║╔══╦═╦═╗╔══╗
║╚═╝║║║║═╣╔╣╔╗╣╔╗║
║╔═╗║╚╣║═╣║║║║║╔╗║
╚╝─╚╩═╩══╩╝╚╝╚╩╝╚╝
""")

            print(Fore.GREEN + "Learn,", Fore.CYAN + "Remeber,", Fore.LIGHTRED_EX + "Improve,", Fore.WHITE +  "Redo." + Fore.RESET + "\n")
        else:
            os.system("clear")
            print(Fore.WHITE + """
╔═══╦╗
║╔═╗║║
║║─║║║╔══╦═╦═╗╔══╗
║╚═╝║║║║═╣╔╣╔╗╣╔╗║
║╔═╗║╚╣║═╣║║║║║╔╗║
╚╝─╚╩═╩══╩╝╚╝╚╩╝╚╝
""")

            print(Fore.GREEN + "Learn,", Fore.CYAN + "Remeber,", Fore.LIGHTRED_EX + "Improve,", Fore.WHITE +  "Redo." + Fore.RESET + "\n")




    elif not match:
        questions.append(ask.lower())
        answ1 = input(Fore.GREEN + "im sorry i do not know that statement, whats the answer to that, or how to respond to it? >> ")
        answers.append(answ1.lower())
        printdy(f"Got it, now on ill answer {ask} with {answ1}", Fore.CYAN)
    else:
        try:
            printdy(answers[questions.index(match)], Fore.RED)
            questions.append(match)
            answers.append(answers[questions.index(match)])
        except:
            printdy("A random error has occured during proccessing.", Fore.YELLOW)
    f = open("training.json", 'w')
    f.write(json.dumps(values, indent=2))
    f.close()
    


    