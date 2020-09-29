# V0.00:

# get pdf
# Get date
# Get the day's lessons link and time
# Get time
# Get the next lesson
# When the time is right, enter in the link, deactivate the camera and enter the lesson.

# Resuming: Get date, get PDF, get time, browse the web

import PyPDF2
import datetime
import selenium
from time import sleep

links = {
    "ronaldo": "",
    "leandro": "",
    "tiago": "",
    "bruno": "https://meet.google.com/bqm-gfef-xud?authuser=0",
    "gabriel": "",
    "davi": "",
    "otavio": "",
    "débora": "",
    "henrique": "",
    "rodolfo": "",
    "homero": ""
}

order = [
    ['ronaldo', 'olivia', 'bruno', 'henrique', 'bruno', 'debora'],
    ['otávio', 'débora', 'henrique', 'ronaldo', 'homero', 'rodolfo'],
    ['ronaldo', 'davi', 'davi', 'leandro', 'tiago', 'ronaldo'],
    ['olívia', 'olívia', 'gabriel', 'gabriel', 'bruno', 'leandro'],
    ['otávio', 'otávio', 'leandro', 'rodolfo', 'gabriel', 'davi']
]

times = [["07", "10"], ["8", "00"], ["9", "10"], ["10", "00"], ["11", "10"], ["12", "00"]]

def getDate():
    time = str(datetime.datetime.now().time()).split(":")
    hr = time[0]
    min = time[1]
    day = datetime.datetime.now().weekday()
    return day, hr, min


class lesson:
    def __init__(self, p1):
        self.lsn = p1
        # setup selenium
        print("Setting up selenium...")

    def join(self):
        # browse to the lesson link > deactivate camera > join
        print("entrando na aula...")
        print(links[self.lsn])

    def quit(self):
        # click in the "quit" button or change the location
        print("Saindo da aula...")


if __name__ == '__main__':
    day, hr, min = getDate()
    print(f"Dia: {day}, {hr}hrs, {min}min")
    todayOrder = order[day]
    for str in todayOrder:
        ls = lesson(str)
        ls.join()
        sleep(2)
        ls.quit()
