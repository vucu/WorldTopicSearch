import tkinter as tk
import persistence.settings as settings

def run():
    window = tk.Tk()
    window.title("World Topic Search")

    label = tk.Label(window, text="Topic:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Search", command=__search)
    button.pack()

    window.bind("<Destroy>", __on_destroy)
    window.mainloop()

def __search():
    x = 2

def __on_destroy(event):
    settings.save()