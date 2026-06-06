from tkinter import *

root = Tk()
root.title("Calculatrice simple")
root.geometry("580x620+130+260")
root.resizable(False, False)
root.configure(bg="#17171b")

equation = ""

def show(value):
    global equation
    equation += str(value)
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text="")

def calculate():
    global equation

    try:
        result = str(eval(equation))
        label_result.config(text=result)
        equation = result
    except:
        label_result.config(text="Erreur")
        equation = ""

label_result = Label(
    root,
    width=25,
    height=2,
    text="",
    font=("Arial", 30),
    bg="#17171b",
    fg="white"
)
label_result.pack()

# Ligne 1
Button(root, text="C", width=5, height=1, font=("Arial",30,"bold"),
       bg="#3697f5", fg="white", command=clear).place(x=10, y=100)

Button(root, text="/", width=5, height=1, font=("Arial",30,"bold"),
       bg="#2a2d36", fg="white", command=lambda: show("/")).place(x=150, y=100)

Button(root, text="%", width=5, height=1, font=("Arial",30,"bold"),
 bg="#2a2d36", fg="white", command=lambda: show("%")).place(x=290, y=100)

Button(root, text="*", width=5, height=1, font=("Arial",30,"bold"),
bg="#2a2d36", fg="white", command=lambda: show("*")).place(x=430, y=100)

# Ligne 2
Button(root, text="7", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("7")).place(x=10, y=200)

Button(root, text="8", width=5, height=1, font=("Arial",30,"bold"),
          command=lambda: show("8")).place(x=150, y=200)

Button(root, text="9", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("9")).place(x=290, y=200)

Button(root, text="-", width=5, height=1, font=("Arial",30,"bold"),
       bg="#2a2d36", fg="white", command=lambda: show("-")).place(x=430, y=200)

# Ligne 3
Button(root, text="4", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("4")).place(x=10, y=300)

Button(root, text="5", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("5")).place(x=150, y=300)

Button(root, text="6", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("6")).place(x=290, y=300)

Button(root, text="+", width=5, height=1, font=("Arial",30,"bold"),
       bg="#2a2d36", fg="white", command=lambda: show("+")).place(x=430, y=300)

# Ligne 4
Button(root, text="1", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("1")).place(x=10, y=400)

Button(root, text="2", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("2")).place(x=150, y=400)

Button(root, text="3", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show("3")).place(x=290, y=400)

# Ligne 5
Button(root, text="0", width=11, height=1, font=("Arial",30,"bold"),
       command=lambda: show("0")).place(x=10, y=500)

Button(root, text=".", width=5, height=1, font=("Arial",30,"bold"),
       command=lambda: show(".")).place(x=290, y=500)

Button(root, text="=", width=5, height=3, font=("Arial",30,"bold"),
       bg="#fe9037", fg="white", command=calculate).place(x=430, y=400)

root.mainloop()