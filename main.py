import tkinter
from tkinter import *

#main
root = Tk()
#window size
root.geometry("800x800")
#window background
root.config(bg="skyblue")
# name of application
root.title("Temperature Converter")

#variables
cel = StringVar()
fahren = StringVar()
result = StringVar()

#defining functions
#celcius function
def convert_c():
    cel = int(celcius.get())
    fahren = (cel*9/5)+32
    return result.set(fahren)

#fahrenheit function
def convert_f():
    fahren = int(fahrenheit.get())
    cel = (fahren-32)*5/9
    return result.set(cel)

#clear function
def clear_inputs():
    celcius.delete(0, END)
    fahrenheit.delete(0, END)
    answer.config(state="normal")
    answer.delete(0, END)
    answer.config(state="readonly")

#exit function
def exit_program():
    return root.destroy()


# placing labels
label_celcius_to_fahrenheit = Label(root, text="Celcius To Fahrenheit")
label_fahrenheit_to_celcius = Label(root, text="Fahrenheit To Celcius")

# Entry text
celcius = Entry(root, textvariable=cel)
fahrenheit = Entry(root, textvariable=fahren)
answer = Entry(root, textvariable=result, bg="yellow")

# Adding buttons
activate_celcius = tkinter.Button(root, text="Celcius to Fahrenheit", command=convert_c)
activate_fahrenheit = tkinter.Button(root, text="Fahrenheit to Celcius", command=convert_f)
clear = tkinter.Button(root, text="Clear", command=clear_inputs)
exit = tkinter.Button(root, text="Exit Program", command=exit_program)

# labels position
label_celcius_to_fahrenheit.place(x=130, y=80)
label_fahrenheit_to_celcius.place(x=480, y=80)

# entry position
celcius.place(x=130, y=170)
fahrenheit.place(x=480, y=170)
answer.place(x=310, y=335, width=220, height=48)

# buttons position
activate_celcius.place(x=130, y=250)
activate_fahrenheit.place(x=480, y=250)
clear.place(x=580, y=335)
exit.place(x=130, y=335)


# function to run the program
root.mainloop()

