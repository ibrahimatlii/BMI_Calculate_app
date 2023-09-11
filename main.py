from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI calculator")
window.config(padx=20, pady=20)
window.minsize(300, 200)
window.iconbitmap("calculator.ico")


def calculate():
    if entry_weight.get() != "" and entry_height.get() != "":
        if entry_weight.get().isdigit() and entry_height.get().isdigit():
            result = int(entry_weight.get()) / (float(entry_height.get()) * float(entry_height.get()) / 10000)
            # print(result)
            # messagebox.showinfo("title", result)

            if result < 18.5:
                result_label.config(text="Your BMI is %.2f" % result + "  you are underweight range")
            elif 18.5 < result < 24.9:
                result_label.config(text="Your BMI is %.2f" % result + "  you are  Healthy Weight range")
            elif 25.0 < result < 29.9:
                result_label.config(text="Your BMI is %.2f" % result + "  you are  overweight range")
            else:
                result_label.config(text="Your BMI is %.2f" % result + "  you are   obese range")
            # result_label.config(text=result)
        else:
            messagebox.showerror("error", "please Enter valid a number ! ")
    else:
        messagebox.showerror("error", "please fill blank areas")


label1 = Label(text="Enter your Weight (kg)")
entry_weight = Entry(width=15)

label2 = Label(text="Enter your Height (cm)")
entry_height = Entry(width=15)

label1.pack()
entry_weight.pack(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=calculate)

result_label = Label(text="0")

label2.pack()
entry_height.pack()
calculate_button.pack()
result_label.pack()
window.mainloop()
