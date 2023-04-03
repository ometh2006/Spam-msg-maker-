import tkinter as tk
from tkinter import Text, ttk
import webbrowser

root = tk.Tk()
root.title('Spam massage maker')
root.iconbitmap('./assets/spam_maker.ico')
root.geometry('600x400')
main_msg=tk.Label(text="This software made only for educational purpose!!!")
main_msg.pack()

spamdetails=ttk.Frame(root)
spamdetails.pack()

msg=tk.StringVar()
ammount=tk.IntVar()

text_box = Text(
    root,
    height=12,
    width=40
    )
text_box.pack(expand=True)
def create_clicked():



    
    

    for i in range(ammount.get()):
            text_box.insert('end',msg.get())
            
           



msg_lable=ttk.Label(spamdetails,text='TEXT')
msg_lable.pack(fill='x', expand=True)

msg_entry = ttk.Entry(spamdetails, textvariable=msg)
msg_entry.pack(fill='x', expand=True)
msg_entry.focus()

ammount_lable=ttk.Label(spamdetails,text='Ammount')
ammount_lable.pack(fill='x',expand=True)

ammount_entry=ttk.Entry(spamdetails,textvariable=ammount)
ammount_entry.pack(fill='x',expand=True)
ammount_entry.focus()

login_button = ttk.Button(spamdetails, text="Genarate", command=create_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()

