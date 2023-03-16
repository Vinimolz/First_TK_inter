from tkinter import *

def convert_milage():
    new_label = float(my_entry.get()) * 1.609
    converted_value.config(text=new_label)


def add(*args):
    result = 0
    for n in args:
        result = result + n 
    
    print(result)
    return result

window = Tk()
window.title("First TKinter window")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

my_entry = Entry()
my_entry.grid(column=1, row=0)

miles_label = Label(text="mile(s)")
miles_label.grid(column=2, row=0)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

equals_label = Label(text="is equals to")
equals_label.grid(column=0, row=1)

converter_button = Button(text="Convert", command=convert_milage)
converter_button.grid(column=1, row=2)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

#This must be the last line of code
window.mainloop()