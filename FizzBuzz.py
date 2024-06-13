import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('FizzBuzz')

# store grade
email = tk.StringVar()


def login_clicked():
    global grade_answer, int_answer
    grade_answer = email.get()
    int_answer = int(grade_answer)
    try:
     num = int(grade_answer)
    except ValueError:
     msg = ('Make sure you are inserting a number')
    else:
         for num in range(1, num+1):
             if num % 3 == 0 and num % 5 ==0:
                 msg = ("fizz buzz")
             elif num % 3 == 0:
                 msg = ("fizz")
             elif num % 5 == 0:
                 msg = ("buzz")
             else:
                 msg = (num)

    showinfo(
        title='Response',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# enters grade box
email_label = ttk.Label(signin, text="Insert A Number: ")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)

email_entry.pack(fill='x', expand=True)
email_entry.focus()

# confirm button
confirm_button = ttk.Button(signin, text="Confirm", command=login_clicked)
confirm_button.pack(fill='x', expand=True, pady=10)

root.mainloop()