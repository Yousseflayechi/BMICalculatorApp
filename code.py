from tkinter import *
class App :
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI")
        self.label = Label(font=('bold',15),fg='blue',text="Your weight in kg")
        self.label.pack()
        self.entry = Entry(font=('bold',15),fg='black')
        self.entry.pack()
        self.label2 = Label(font=('bold', 15), fg='blue', text="Your height in m ")
        self.label2.pack()
        self.entry2 = Entry(font=('bold', 15), fg='black')
        self.entry2.pack()
        self.b = Button(font=('bold',10),fg='blue',text="Calaculate your BMi",command=self.calculate_Bmi)
        self.b.pack()
        self.text = Text(font=('bold', 8), fg='blue',)
        self.text.pack()
        self.root.mainloop()

    def calculate_Bmi(self):
        w = int(self.entry.get())
        h = float(self.entry2.get())

        Bmi = w / (h ** 2)
        if Bmi <=18.5  :
            self.text.delete("1.0", END)
            self.text.insert("1.0", f' Your BMI : {Bmi:.4f} and you are underweight')
        elif 18.5<=Bmi<=24.9 :
            self.text.delete("1.0", END)
            self.text.insert("1.0", f' Your BMI : {Bmi:.4f} and you are Normal')
        elif  25 <=Bmi<= 39.9:
            self.text.delete("1.0", END)
            self.text.insert("1.0", f' Your BMI : {Bmi:.4f} and you are Overweight')
        else:
            self.text.delete("1.0", END)
            self.text.insert("1.0", f' Your BMI : {Bmi:.4f} and you are obese')


if __name__== "__main__" :
    app = App()



