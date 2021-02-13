import sys
import pyautogui 
import itertools
from threading import Timer 
wh = pyautogui.size()
wh
pyautogui.position()
pyautogui.moveTo(42, 643, duration=0.25)
pyautogui.click()
pyautogui.click()
pyautogui.sleep(5)
pyautogui.hotkey('m','c','b') #input whatever username 
pyautogui.moveTo(947, 552, duration=0.25)
pyautogui.click()
pyautogui.hotkey('f','a','n','t','a','s','y','x','y','z','2','3','!') #input whatever password 
pyautogui.click()
pyautogui.click(882,616)
pyautogui.sleep(6)
pyautogui.click(495,334)
pyautogui.click(856,209)
pyautogui.sleep(2.5)
class automation:
      def auto(self):
            pyautogui.hotkey('a')
            pyautogui.click(614,398)
            pyautogui.click()
            pyautogui.click(980,541)
            pyautogui.hotkey('1') #Insert reorder point number
            pyautogui.click(992,710)
            pyautogui.hotkey('2') #Insert reorder amount
            pyautogui.click(1381,761)
execute = automation()
execute.auto()
pyautogui.click(495,334)
pyautogui.click(856,209)
def repeat(auto, times=None):
    if times is None:
        while True: 
            yield object
    else:
        for i in range(10):
            yield object 
























""" def repeat(auto, times=None):
    if times is None: 
        while True:
            yield auto
    else:
        for i in range(10): 
            yield auto """


"""
      def repetition(self)
repetition = itertools.repeat(execute, 10)

# next(islice(iter(auto,object())), 10, 10), None)
# execute.repeat_fun(10, auto) """



""" loopIterator = iter([])
while True:
    try: 
        if loopIterator < 10:
            loopIterator += 1 
        else:
            break """

""" class loopthrough(automation):
    def __init__(self, count):
        self._index = -1 
        self._count = 10

    def __iter__(self):
        return self
    
    def __next__(self):
        self._index = += 1
        if self._index = self._count:
            self._index = -1
            raise StopIteration
        else: 
            break """



