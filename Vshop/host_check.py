from tkinter import *
from threading import Timer

def repeater(interval, function):
    Timer(interval, repeater, [interval, function]).start()
    function()

def click_ref():
   host_file = open('c:/windows/system32/drivers/etc/hosts','r')
   len_host = len(host_file.readlines())
   host_file.seek(0, 0)
   for i in range(0, len_host):
      s = host_file.readline()
      if '#' not in s:
         win_title = s
   window.title(win_title)   
   host_file.close()   

window = Tk()
window.attributes("-topmost",True)
window.attributes('-toolwindow', True)
window.geometry('210x0')

repeater(5, click_ref)

window.mainloop()