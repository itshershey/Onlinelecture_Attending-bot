import smtplib  # for email  # pip install secure-smtplib
import sys
from tkinter.filedialog import *
import tkinter as tk  # pip install tkinter
import PyPDF2
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # pip install DateTime
import os  # pip install os-win
import cv2  # pip install opencv-python
from requests import get  # pip install requests
import wikipedia  # pip install wikipedia
import webbrowser  # pip install pycopy-webbrowser
import pywhatkit as kit  # pip install pywhatkit
import pytz  # python time zone # pip install pytz
import pyautogui  # for screenshot and for controlling system volume
import psutil  # pip install psutil
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import pywikihow  # for how to do mode  # pip install pywikihow
import winsound  # For Alarm
import pyjokes  # For telling jokes  # pip install pyjokes
import winshell
# import ecapture as ec
from datetime import date
import datetime
import pyautogui
from selenium import webdriver
import time
import keyboard
from tkinter import *
import os
import random

from selenium.webdriver.common import by
from tabulate import tabulate


# For joing lectures according to timetable
def google_meet():
    # class timetable in Dict forat

    MAR = MAR_LAB = "https://meet.google.com/ysa-bjtd-tzm"
    EM = "https://meet.google.com/woj-mqpr-mjg"  # test
    SE = SE_LAB = "https://meet.google.com/xez-iwnr-ojp"
    CWP = CWP_LAB = CP = "https://meet.google.com/zpn-vmgd-vkm"
    MAR_TUT = "https://meet.google.com/xow-pdxg-jvy"
    CWP_TUT = "https://meet.google.com/vdh-xdff-uwp"

    timetable = {"Monday": {"8:00": SE_LAB, "10:00": MAR, "12:00": EM, "13:00": SE},
                 "Tuesday": {"8:00": MAR_LAB, "11:00": SE, "12:00": EM, "13:00": MAR},
                 "Wednesday": {"00:11": CWP_LAB, "10:00": MAR, "12:00": CWP, "13:08": SE},
                 "Thursday": {"8:00": CP, "10:00": MAR, "12:00": CWP, "13:00": SE},
                 "Friday": {"10:00": EM, "11:00": CWP},
                 "Saturday": {"8:00": CWP_TUT, "10:00": EM, "11:00": CWP, "13:00": MAR_TUT}

                 }

    def join_lect(link):
        file = open("Details.txt", 'r')
        details = file.read().split("\n")
        email = details[0]
        password = details[1]

        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
        driver.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ');
        email_in = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        email_in.send_keys(email)
        nxt = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        nxt.click()
        time.sleep(2)
        password_in = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password_in.send_keys(password)
        signup = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        signup.click()
        time.sleep(3)
        driver.get(link)
        time.sleep(6)

        dismiss = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
        dismiss.click()
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(1)

        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(1)
        join = driver.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
        join.click()
        print("Successfully Joined ")
        time.sleep(3600)  # keep link joined for about 1 hr
        main()

    def find_lect(day, current_time):
        if (day not in timetable):
            print("You have a holiday today.")

        else:
            todays_lects = timetable[day]  # this dict will have all lect links of the particular day
            print("You have these lectures today ,Be ready!")
            for i in todays_lects:
                print(i, todays_lects[i])
            # checking for this time if there is any lect
            if (current_time in todays_lects):
                get_link = todays_lects[current_time]
                print("Joining Lecture ... " + get_link)
                # function for joining google meet
                join_lect(get_link)

            else:
                print("You do not have any lecture at this time")
                time.sleep(60)  # wait for 1 min
                main()

    def main():

        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        today = date.today()
        y = int(today.strftime("%Y"))
        m = int(today.strftime("%m"))
        d = int(today.strftime("%d"))
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        week_num = datetime.date(y, m, d).weekday()
        day = week_days[week_num]
        print(day)
        print(current_time)
        # sending todays day and time to
        find_lect(day, current_time)

    main()


# For game
def startgame():
    def game(name):
        list_of_words = ["night","python","database","file","location","meet","word","slicing","character"]
        word = random.choice(list_of_words)
        l = len(word)
        turns = 10
        points = 0
        guessmade = ''  # user wil make this guess
        valid_entry = set('abcdefghijklmnopqrstuvwxyz')  # Only these characters must be entered by the user.
        while l > 0:
            main_word = ""  # Word which user is creating OR word which we want to show the user

            # Checking whether the guess is correct or not
            for letter in word:
                if letter in guessmade:
                    main_word = main_word + letter
                else:
                    main_word = main_word + "- "

            if main_word == word:
                c = 0
                print(main_word)
                print("Congrats, YOU WON!!!!")
                print("Your Score:", turns, "/10")
                f = open("score.txt", 'w')
                f = open("score.txt", 'a')
                f.write("\n")
                f.write(name)
                f.write("=")
                f.write(str(turns))
                f = open("score.txt", 'r')
                content = f.read().split('\n')
                for words in content:
                    c = c + 1
                if (c >= 5):
                    os.remove("score.txt")

                break

            print("Guess the Words ", main_word)  # Here the main_word will show the dashes
            guess = input()

            if guess in valid_entry:
                guessmade = guessmade + guess
            else:
                print("Enter Valid Alphabet !!!!")
                guess = input()

            if guess not in word:
                turns = turns - 1

                if turns == 9:
                    print("9 turns left!!!")
                    print("^------------------^")
                if turns == 8:
                    print("8 turns left!!!")
                    print("^------------------^")
                    print("         O          ")
                if turns == 7:
                    print("7 turns left!!!")
                    print("^------------------^")
                    print("         O          ")
                    print("         |          ")
                if turns == 6:
                    print("6 turns left!!!")
                    print("^------------------^")
                    print("         O          ")
                    print("         |          ")
                    print("        /          ")
                if turns == 5:
                    print("5 turns left!!!")
                    print("^------------------^")
                    print("         O          ")
                    print("         |          ")
                    print("        / \         ")
                if turns == 4:
                    print("4 turns left!!!")
                    print("^------------------^")
                    print("         O/          ")
                    print("         |         ")
                    print("        / \         ")
                if turns == 3:
                    print("3 turns left!!!")
                    print("^------------------^")
                    print("        \O/          ")
                    print("         |         ")
                    print("        / \         ")
                if turns == 2:
                    print("2 turns left!!!")
                    print("^------------------^")
                    print("        \O/ |        ")
                    print("         |         ")
                    print("        / \         ")
                if turns == 1:
                    print("1 turn left!!! Hangman On His Last Breath ")
                    print("^------------------^")
                    print("        \O/_|        ")
                    print("         |         ")
                    print("        / \         ")
                if turns == 0:
                    print("YOU LOSE")
                    print("you left a good man die")
                    print("^------------------^")
                    print("         O_|        ")
                    print("        /|\         ")
                    print("        / \         ")
                    print("Your Score: 0/10")
                    break

    def main_1():
        name = input("ENTER YOUR NAME:")
        print(f"   Welcome {name} !")
        print("* Score Board *")
        f = open("score.txt", 'r')
        content = f.read()
        print(content)
        print("<--------^--^-------->")
        print("          \U0001F600")
        print("Try to guess the Word in less than 10 attempts")
        game(name)

    main_1()


# For taking various queries in jarvis
def jarvis():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 200)

    # text to speech
    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    # voice to text
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception as e:
            speak("Pardon Sir")
            return "none"
        return query

    # to wish
    def wish():
        hour = int(datetime.datetime.now().hour)

        if 0 <= hour <= 12:
            speak("Good Morning Sir")
        elif 12 < hour < 18:
            speak("Good Afternoon Sir")
        else:
            speak("Good Evening Sir")

    def cpu():
        cpu = str(psutil.cpu_percent())
        speak(f"You have used {cpu} of CPU.")
        battery = psutil.sensors_battery().percent
        speak(f"You have used {battery} of battery")

    def date():
        t_date = datetime.datetime.now(tz=pytz.timezone('Asia/kolkata'))
        speak("Today's date is.")
        speak(t_date.strftime("%d %B, of %Y"))

    def time():
        t_now = datetime.datetime.now().strftime('%H:%M:%S')
        speak("Sir the running time is")
        speak(t_now)

        speak("Please tell me how can I help you")

    root = tk.Tk()
    window = tk.Canvas(root, width=200, height=200)
    window.pack()

    def screenshot():
        img = pyautogui.screenshot()

        speak("From which name do you want to save file")
        file_path = asksaveasfilename()

        img.save(file_path + " _screenshot.png")

        window.create_window(100, 100)
        speak("I have taken the screenshot.")

    def sendEmail(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('gpratik246@gmail.com', 'ppg#7635')
        server.sendmail('gpratik246@gmail.com', to, content)
        server.close()

    def alarm(Timing):
        altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
        altime = altime[11:-3]
        print(altime)
        Hourreal = altime[:2]
        Hourreal = int(Hourreal)
        Minutereal = altime[3:5]
        Minutereal = int(Minutereal)
        speak(f"Done, the alarm is set for {Timing}")
        while True:
            if Hourreal == datetime.datetime.now().hour:
                if Minutereal == datetime.datetime.now().minute:
                    print("Alarm is running")
                    winsound.PlaySound('abcd', winsound.SND_LOOP)

                elif Minutereal < datetime.datetime.now().minute:
                    break

    def pdf():
        file = open("MAR Sensor Notes 1.1.pdf", "rb")
        reader = PyPDF2.PdfFileReader(file)  # pip install PyPDF2
        pages = reader.numPages  # for counting number of pages in pdf
        speak(f"Total number of pages in the pdf are {pages}")
        speak("Sir please enter the page number which you want to read")
        pg = int(input("Enter page number = "))
        page1 = reader.getPage(pg)
        pdfData = page1.extractText()
        speak(pdfData)

    if __name__ == '__main__':
        wish()
        time()
        while True:
            if 1:
                query = takecommand().lower()

                # logic building for tasks

                if "open notepad" in query:
                    npath = "C:\\Windows\\SysWOW64\\notepad.exe"
                    os.startfile(npath)

                elif "open command prompt" in query:
                    os.system("start cmd")

                elif "open camera" in query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "play music" in query:
                    music_dir = "C:\\Users\HP\\Downloads\\music1.mpeg"
                    os.startfile(music_dir)

                elif "date" in query:
                    date()

                elif "ip address" in query:
                    ip = get("https://api.ipify.org").text
                    speak(f"Your ip address is {ip}")

                elif "battery" in query:
                    cpu()

                elif "open learner website" in query:
                    webbrowser.open("https://learner.vierp.in/home")

                elif "join math lecture" in query:
                    webbrowser.open("https://meet.google.com/wxq-dyqc-pxs")

                elif "join mechanics lecture" in query:
                    webbrowser.open("http://meet.google.com/exh-ehok-prk")

                elif "join python lecture" in query:
                    webbrowser.open("https://meet.google.com/zpn-vmgd-vkm")

                elif "wikipedia" in query:
                    speak("searching wikipedia.....")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("according to wikipedia ")
                    speak(results)  # speak like " what is python" according to wikipedia
                    # print(results)

                elif "play gaana music" in query:
                    speak("Sir which music do you want to listen")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}https://gaana.com/")

                elif "open snakify" in query:
                    webbrowser.open("https://snakify.org/en/")

                elif "search youtube" in query:
                    speak("sir, what should i search on youtube")
                    cm = takecommand().lower()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")



                elif "open my instagram" in query:
                    webbrowser.open("www.instagram.com")

                elif "screenshot" in query:
                    screenshot()

                elif "open google" in query:
                    speak("sir, what should i search on google")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}")

                elif "open my whatsapp" in query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif "join the system engineering lecture" in query:
                    webbrowser.open("https://meet.google.com/xez-iwnr-ojp")

                elif "show my time table" in query:
                    webbrowser.open("file:///C:/Users/HP/Downloads/DiV%20E%20New%20Time%20Table.pdf")

                elif "hello" in query:
                    speak("Hello sir . How are you.")

                elif "how are you jarvis" in query:
                    speak("I'm fine sir. ")

                elif "send whatsapp message" in query:
                    speak("What message should i send sir")
                    cm = takecommand().lower()

                    kit.sendwhatmsg("+918308830669", f"{cm}", 23, 58)  # 24 hours time format


                elif "send email" in query:
                    try:
                        speak("What should i say?")
                        content = takecommand().lower()
                        to = "gpratik246@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent.")

                    except Exception as e:
                        print(e)
                        speak("sorry sir, I am not able to sent this email")

                elif "weather" in query:
                    speak("Which city temperature should I check weather ?")
                    cm = takecommand().lower()
                    search = "temperature in", {cm}
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current temperature in {cm} is {temp}")



                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)


                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis1.txt", "r")
                    print(file.read())
                    speak(file.read())

                elif "alarm" in query:
                    speak("Sir please tell me for which time do you want to set alarm?, for example, set alarm to 5:30 am")
                    t1 = takecommand()  # set alarm at 5:30
                    t1 = t1.replace("set alarm to ", "")  # 5:30 a.m.
                    t1 = t1.replace(".", "")  # 5:30 am
                    t1 = t1.upper()  # 5:30 AM
                    alarm(t1)
                elif "activate how to do mode" in query:
                    speak("How to do mode is activated. Please tell me what you want to know ?")
                    how = takecommand()
                    max_results = 1
                    how_to = pywikihow.search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)

                elif "volume up" in query:
                    pyautogui.press("volumeup")
                elif "volume down" in query:
                    pyautogui.press("volumedown")
                elif "volume mute" in query:
                    pyautogui.press("volumemute")

                elif "read pdf" in query:
                    pdf()

                elif "start google meet" in query:
                    google_meet()

                elif "start game" in query:
                    startgame()

                elif "exit" in query:
                    quit()


def delete2():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("400x250")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", height='2', width="15").pack()
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
    jarvis()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("500x350")
    Label(screen4, text="Password or Email Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("500x350")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def des2():
    screen2.destroy()
    screen1.destroy()


def success():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Successfully Register")
    screen2.geometry("500x350")
    Label(screen2, text="Registration Successful", fg="green", font=("calibri", 11)).pack()
    Label(screen1, text="").pack()
    Button(screen2, text="ok", bg="lightgreen", height="2", width="20", command=des2).pack()


def register_user():
    print("working")

    email_info = email.get()
    password_info = password.get()

    file = open("Details.txt", "w")
    file.write(email_info + "\n")
    file.write(password_info)
    file.close()

    email_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11), command=success()).pack()


def login_verify():
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    f = open("Details.txt", "r")
    verify = (f.readlines())
    if (verify != ""):
        if email1 and password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register Here")
    screen1.geometry("500x350")

    global email
    global password
    global email_entry
    global password_entry
    email = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Email * ").pack()

    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", bg="lightgreen", height="2", width="20", command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x350")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_entry1
    global password_entry1

    Label(screen2, text="Email * ").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", bg="aqua", height="2", width="20", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x450")
    screen.title("Python Project")
    Label(text="Welcome\n\nUser", bg="skyblue", width="300", height="5", font=("TimesNewRoman", 23)).pack()
    Label(text="").pack()
    Button(text="Login", bg="skyblue", height="3", width="50", command=login).pack()
    Label(text="").pack()
    Button(text="Register", bg="skyblue", height="3", width="50", command=register).pack()

    screen.mainloop()


main_screen()
