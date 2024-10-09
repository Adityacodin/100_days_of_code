from tkinter import *

TO_KM = 1.609

def convert_to_km():
    miles = int(miles_entry.get())
    km = miles*TO_KM
    km_output.config(text = str(km))


window = Tk()
window.title('Miles to Km Converter')
window.config(padx = 20,pady = 20)
Font = ('Arial',10,'bold')
msg_label = Label(text = 'is equal to ',font = Font)
msg_label.grid(row = 1,column=0)
miles_entry = Entry(width=10)
miles_entry.grid(row = 0,column = 1)
miles_label = Label(text = 'Miles', font = Font)
miles_label.grid(row = 0,column =2)
km_output = Label(text ='',font = Font)
km_output.grid(row = 1,column = 1)
km_label = Label(text = 'Kilometers', font = Font)
km_label.grid(row = 1,column = 2)
calculate_btn = Button(text = 'Calculate',font = Font,command=convert_to_km)
calculate_btn.grid(row = 2,column = 1)


window.mainloop()