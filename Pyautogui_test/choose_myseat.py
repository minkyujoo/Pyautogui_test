import pyautogui as pg
import time
import schedule
import datetime

def choose_myseat():
    pg.keyDown("win")
    pg.press('r')
    pg.keyUp("win")
    pg.typewrite('http://hisk.skcc.com')
    pg.press('enter')

    pg.PAUSE = 10
    pg.click(x=1068,y=725)
    pg.PAUSE = 10

    pg.press('f11')
    pg.PAUSE = 10
    #pg.press('tab')
    #pg.press('tab')
    #pg.typewrite('http://')
    #time.sleep(5)

    t=['월', '화', '수', '목', '금', '토', '일'] #0,1,2,3,4,5,6
    date = t[datetime.date.today().weekday()]

    pg.click(x=650,y=50)
    pg.PAUSE =10
    #예약가능요일: 월57,화51,수57,목57,금51
    if (date =='월' or date=='수' or date=='목'):
        pg.click(x=576,y=645)
    elif (date=='화' or date=='금'):
        pg.click(x=620,y=645)

schedule.every().day.at("00:01").do(choose_myseat)

while True:
    schedule.run_pending()
    time.sleep(5)


