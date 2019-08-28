import pyautogui as pg
#import request
#import json

pg.press("shift")
pg.press("f1")
#pg.typewrite("Hello pyautogui!")

pg.alert(text='test', title='test')
pg.confirm(text='test' , title='test', buttons=['ok', 'cancel'])
pg.prompt(text='test', title='test', default='test')

pg.screenshot('test.png')

seat_btn = pg.locateOnScreen('seaticon.png')
center_seat_btn = pg.center(seat_btn)
pg.click(center_seat_btn)