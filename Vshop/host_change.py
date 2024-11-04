from tkinter import *
from tkinter import ttk

def click_ref():
   host_file = open('c:/windows/system32/drivers/etc/hosts','r')
   active_host=[]
   len_host = int(len(host_file.readlines()))
   host_file.seek(0,0)
   for i in range(0,len_host):
      s = host_file.readline()
      if '#' not in s:
         active_host.append(s)
   newti=str(active_host[0])
   window.title(newti)   
   #lbl.configure(text=active_host[0])
   host_file.close()  

window = Tk()
window.geometry("200x32")
window.title("Active host")
window.attributes("-topmost",True)
#window.overrideredirect(1)
#window.resizable(0,0)
window.attributes('-toolwindow', True)

def write_callback(var, index, mode):
    print(f"The variable {var} has been written to in mode:", mode)

hosts =('192.168.202.82 gate.synerget.ru', '192.168.202.30 gate.synerget.ru', '192.168.202.238 gate.synerget.ru', '192.168.202.10 gate.synerget.ru')

var = StringVar()
combobox = ttk.Combobox(window, textvariable = var)
combobox['values'] = hosts
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 5, pady=5)

var.trace('w', write_callback)




 




#lbl = Label(window, text='none')
#lbl.grid(column=0, row=0)



window.mainloop()