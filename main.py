import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
green_dot = 'C:/Users/ASUS/Desktop/BOT/green dot.png'
smiley_paper_clip = 'C:/Users/ASUS/Desktop/BOT/smiley paper clip.png'
position1 = pt.locateOnScreen(smiley_paper_clip, confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y

    position = pt.locateOnScreen(smiley_paper_clip, confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 70, y - 50, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(10, 10)
    pt.leftClick()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)
    return whatsapp_message


# get_message()


def post_response(message):
    global x, y

    position = pt.locateOnScreen(smiley_paper_clip, confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=0.5)
    pt.click()
    pt.typewrite(message, interval=0.05)
    pt.typewrite("\n", interval=0.1)


# post_response(get_message())

def process_response(message):
    welcome = ["oye", "hi", "hello", "hii", "hiii", "sunn", "helloo", "helLoooo", "helo", "sunno", "listen bot",
               "yo bot", "botty", "yo"]
    tareef = ["nice", "amazing", "amazing work", "awesome", "cool", "very cool", "awesome work", "cool"]
    if "haha" in str(message).lower():  # laugh
        list1 = ['hahahahaha', 'XD', 'LOL']
        return str(random.choice(list1))
    elif "bye" in str(message).lower():  # byeeeeee
        list1 = ["Goodbye", "TaTa", "see ya again", "byeeee"]
        return str(random.choices(list1)[0])
    elif "nic" in str(message).lower():  # Tareef
        list1 = ["I am glad you think, I work correctly", "Thanks for the feedback"]
        return str(random.choices(list1)[0])
    elif "goo" in str(message).lower():  # tareef
        list1 = ["I am glad you think, I work correctly", "Thanks for the feedback"]
        return str(random.choices(list1)[0])
    elif "coo" in str(message).lower():  # cool
        return "very cool"
    elif "no" in str(message).lower():  # NO
        list1 = ["I am observing denial",
                 "quite understandable"]
        return str(random.choice(list1))
    elif "hehe" in str(message).lower():  # laugh
        list1 = ['hahahahaha', 'XD', 'LOL']
        return str(random.choice(list1))
    elif str(message).lower() in tareef:  # tareef
        list1 = [":)", ":))", ":)))", "UwU", "Thank you, Thank you"]
        return str(random.choices(list1)[0])
    elif "when" in str(message).lower():
        list1 = ["He will be bck in no time", "really really soon", "at max 8 hours, because he might be sleeping"]
        return str(random.choice(list1))
    elif "where is" in str(message).lower():  # where
        list1 = ["at home or maybe at college", "maybe at home or maybe at college, call him for more information"]
        return str(random.choice(list1))
    elif "joke" in str(message).lower():  # joke
        list1 = ["I once tried ordering a lighter on amazon, all I got was matches",
                 "How did a bot pay for his burgers?? - with cache, obviously"]
        return str(random.choice(list1))
    elif str(message).lower() in welcome:  # welcome
        list1 = ["Hi, while you were looking for Vasu, you have accidentally run into a bot, I can help you with a few "
                 "questions, as where he might be, and when will he be back I can tell a few jokes or facts too. ",
                 "hello there, I am a bot, I deal with things when he is doing other things,"
                 "I can guide you with where he is and what he might be doing, I can also tell"
                 " some facts and jokes. ",
                 "hellooo, it seems like you have a bot in your contact list, I can help you with a few"
                 " questions, as where he is"]
        return str(random.choice(list1))
    elif "who" in str(message).lower():  # answer for knock knock
        return "a bot"
    elif "fact" in str(message).lower():  # fact
        list1 = ["cold air is heavier than hot air",
                 "Crocodiles and Aligators are different breeds, but only differ in teeth arrangement",
                 "Light travelled 151.39 million kms to reach Earth"]
        return str(random.choice(list1))
    elif "doing" in str(message).lower():  # what
        list1 = ["Most probably sleeping", "well he made you a test subject by testing me on you",
                 "testing his bot", "he is sleeping"]
        return str(random.choices(list1)[0])
    elif "yeah" in str(message).lower():  # yeah
        return "yeahhhhhh"
    elif "congrat" in str(message).lower():  # congratss
        return "thank you very much!"
    elif "you do" in str(message).lower():  # what all bot can do
        return "I can, crack jokes, tell facts, tell where is Vasu, what is he doing, When will he be back"
    elif "thank" in str(message).lower():  # thanks
        list1 = ["glad i could help", "my pleaure", ":)"]
        return str(random.choice(list1))
    else:  # else
        list1 = ["it seems like you asked something I am not programmed to answer, try being grammatically correct or "
                 "ask something else, I can only say what I am programmed say",
                 "whooops I couldn't understand that, try something else or look for typos. "]

        return str(random.choice(list1))


# processed_message = process_response(get_message())
# post_response(processed_message)

def check_for_new_messages():
    while True:
        try:
            position = pt.locateOnScreen(green_dot, confidence=0.95)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(0.5)
                processed_message = process_response(get_message())
                print("response -", processed_message)
                post_response(processed_message)
                # pt.moveTo(703, 942)
        except Exception:
            print("No new other users with new messages located")

        # # if pt.pixelMatchesColor(703, 942, (38, 45, 49), tolerance=5):
        #     print("is grey")
        #     processed_message = process_response(get_message())
        #     post_response(processed_message)
        else:
            print("No new messages yet...")
        pt.moveTo(300, 942)
        pt.click()
        sleep(5)


check_for_new_messages()
