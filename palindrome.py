#Ra7oox
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("palindrome check")
root.geometry("400x400")
label=Label(root,text="give a word")
label.place(x=150,y=50)
input=Entry(root)
input.place(x=120,y=80)
def palindrome():
    if(input.get()==input.get()[::-1]):
        messagebox.showinfo("yes","it's palindrome")
    else:
        messagebox.showerror("not","is not a palindrome")
        






button=Button(root,text="check",command=palindrome,bg="green",border=0)
button.place(x=160,y=120)
root.mainloop()