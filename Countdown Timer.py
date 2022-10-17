import tkinter as tk
from tkinter import *
import time
import winsound
class gui():
    def __init__(self):
        self.box= tk.Tk()
        self.box.geometry('360x400')
        self.box.title('Countdown Timer')
        self.box.configure(bg = 'brown')
        self.hr = StringVar()
        self.minute = StringVar()
        self.seconds = StringVar()
        self.hr.set('00')
        self.minute.set('00')
        self.seconds.set('00')
        hours = tk.Entry( self.box, font = ('bold',25) , text = self.hr , bg = 'lightgreen')
        mins = tk.Entry( self.box, font  = ('bold',25) , text = self.minute , bg = 'lightgreen')
        secs = tk.Entry( self.box, font  = ('bold',25) , text = self.seconds , bg = 'lightgreen')
        hours.place(x=50,y=20,width = 50,height=70)
        mins.place(x=150,y=20,width = 50,height=70)
        secs.place(x=250,y=20,width = 50,height=70)
        self.h = StringVar()
        self.m = StringVar()
        self.s = StringVar()
        self.h.set('00')
        self.m.set('00')
        self.s.set('00')
        self.hour_display = Label(self.box,textvariable = self.h)
        self.min_display = Label(self.box , textvariable = self.m)
        self.secs_display = Label(self.box , textvariable = self.s)
        self.hour_display.place(x = 50 , y = 300 , height = 70 , width = 50)
        self.min_display.place(x = 150 , y = 300 , height = 70 , width = 50)
        self.secs_display.place(x = 250 , y = 300 , height = 70 , width = 50)
        self.hour_display.config(font = ('bold',18) , bg = 'lightgreen')
        self.min_display.config(font = ('bold',18) , bg = 'lightgreen')
        self.secs_display.config(font = ('bold',18) , bg = 'lightgreen')
        self.hour_label_1 = Label(self.box , text = "H")
        self.min_label_1 = Label(self.box , text = "M")
        self.sec_label_1 = Label(self.box , text = "S")
        self.hour_label_2 = Label(self.box , text = "H")
        self.min_label_2 = Label(self.box , text = "M")
        self.sec_label_2 = Label(self.box , text = "S")
        self.hour_label_1.place(x = 30 , y = 300 , height = 10 , width = 10)
        self.hour_label_1.config(bg = 'brown')
        self.min_label_1.place(x = 130 , y = 300 , height = 10 , width = 10)
        self.min_label_1.config(bg = 'brown')
        self.sec_label_1.place(x = 230 , y = 300 , height = 10 , width = 10)
        self.sec_label_1.config(bg = 'brown')
        self.hour_label_2.place(x = 30 , y = 20 , height = 10 , width = 10)
        self.hour_label_2.config(bg = 'brown')
        self.min_label_2.place(x = 130 , y = 20 , height = 10 , width = 10)
        self.min_label_2.config(bg = 'brown')
        self.sec_label_2.place(x = 230 , y = 20 , height = 10 , width = 10)
        self.sec_label_2.config(bg = 'brown')
        self.countdown_title = Label(self.box , text = 'COUNTDOWN TIMER')
        self.countdown_title.place(x = 90 , y = 230 , height = 50 , width = 180)
        self.countdown_title.config(bg = 'brown' , font = ("bold" , 13))
        self.input_label1 = Label(self.box , text = "IN")
        self.input_label1.place(x = 10 , y = 40 , height = 20 , width = 20)
        self.input_label1.config(bg = 'brown' , font = ('italic' , 14))
        self.input_label1 = Label(self.box , text = "OUT")
        self.input_label1.place(x = 8 , y = 320 , height = 20 , width = 40)
        self.input_label1.config(bg = 'brown' , font = ('italic' , 14))
        self.timer_on = False
        self.timer_pause_count = 0
        self.stop_var = 0
        self.reset_var = 0
        self.flag = 0

        def start():
            self.flag = 0
            self.reset_var = 0
            self.timer_pause_count = 0
            self.timer_on = True
            self.stop_var = 0
            self.h.set(hours.get())
            self.m.set(mins.get())
            self.s.set(secs.get())
            iterations = 0
            iterations = int(hours.get())*3600+int(mins.get())*60+int(secs.get())
            while iterations > -1 and self.timer_pause_count == 0 and self.flag == 0:
                if iterations <= 0:
                    self.flag = 1
                    winsound.PlaySound('SystemHand',1)
                    self.s.set('00')
                    self.m.set('00')
                    self.h.set('00')
                    break
                Min , Sec = (iterations//60 , iterations % 60)
                Hours = 0
                if Min > 60:
                    Hours , Min = (Min // 60 , Min %60)
                if self.timer_on == True and self.stop_var == 0 and self.reset_var == 0 and self.flag == 0:
                    self.s.set(Sec)
                    self.m.set(Min)
                    self.h.set(Hours)

                    self.box.update()
                    time.sleep(1)

                    iterations -= 1
                self.box.update()
                
        def Pause():
            self.timer_on = False
            self.pause = True
            self.timer_pause_count = 1
            iterations = 0
            iterations = int(self.h.get())*3600+int(self.m.get())*60+int(self.s.get())
            while iterations > -1:
                if self.stop_var == 1 or self.reset_var == 1 or self.flag == 1:   
                    break
                if self.pause == False:
                    break
                if iterations <= 0:
                    winsound.PlaySound('SystemHand',1)
                    self.s.set('00')
                    self.m.set('00')
                    self.h.set('00')
                    break
                Min , Sec = (iterations//60 , iterations % 60)
                Hours = 0
                if Min > 60:
                    Hours , Min = (Min // 60 , Min %60)

                if self.stop_var == 1:
                    break

                self.s.set(Sec)
                self.m.set(Min)
                self.h.set(Hours)

                self.box.update()
                
        def resume():
            self.reset_var = 0
            self.timer_on = True
            self.pause = False
            iterations = 0
            iterations = int(self.h.get())*3600+int(self.m.get())*60+int(self.s.get())
            while iterations > -1:
                if self.stop_var == 1 or self.flag == 1:
                    break
                if iterations <= 0:
                    winsound.PlaySound('SystemHand',1)
                    self.s.set('00')
                    self.m.set('00')
                    self.h.set('00')
                    break
                Min , Sec = (iterations//60 , iterations % 60)
                Hours = 0
                if Min > 60:
                    Hours , Min = (Min // 60 , Min %60)
                if self.timer_on == True and self.stop_var == 0 and self.reset_var == 0:  
                    self.s.set(Sec)
                    self.m.set(Min)
                    self.h.set(Hours)
                    self.box.update()
                    time.sleep(1)
                    iterations -= 1
                self.box.update()

        def stop():
            self.stop_var = 1
            if self.timer_on == True or self.stop_var == 1:  
                self.timer_on = False
                self.stop_var = 1
                iterations = 0
                self.timer_pause_count = 1
                self.stop_var = 1
                winsound.PlaySound('SystemExclamation',1)
                self.s.set('00')
                self.m.set('00')
                self.h.set('00')
                self.hr.set('00')
                self.minute.set('00')
                self.seconds.set('00')
                iterations = -1
            
        self.resetbtn = tk.Button(self.box , text = 'RESET' , bg = 'green' , command = self.reset)
        self.resetbtn.place(x=20 , y = 110 ,width = 90 , height = 50)
        self.stopbtn = tk.Button(self.box , text = 'STOP' , bg = 'red' , command = stop)
        self.stopbtn.place(x = 250 , y = 110 , width = 90 , height = 50)
        self.pausebtn = tk.Button(self.box , text = 'PAUSE' , bg = 'yellow' , command = Pause)
        self.pausebtn.place(x = 20 , y = 180 , width = 90 , height = 50)
        self.startbtn = tk.Button(self.box , text = 'START' , bg = 'skyblue' , command = start)
        self.startbtn.place(x=250 , y = 180 , width = 90 , height = 50)
        self.resumebtn = tk.Button(self.box , text = 'RESUME' , bg = 'darkgreen' , command = resume)
        self.resumebtn.place(x = 135 , y = 145 , width = 90 , height = 50)
        self.box.mainloop()
        
    def reset(self):
        self.reset_var = 1
        iterations = 0
        if self.reset_var == 1:
            winsound.PlaySound('SystemHand',1)
            self.hr.set('00')
            self.minute.set('00')
            self.seconds.set('00')
            self.h.set('00')
            self.m.set('00')
            self.s.set('00')

if __name__ == '__main__':
    box = gui()

