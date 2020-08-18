from tkinter import *

root = Tk()

frame_search = LabelFrame(root, text="Search for customer here:", padx=5, pady=5)
frame_search.pack()
e = Entry(frame_search, width=35, borderwidth=5)
e.pack()


def button_click():
    return


button_search = Button(frame_search, text="Search", padx=0, pady=0, command=lambda: button_click())
button_search.pack()

frame_new_customer = LabelFrame(root, padx=5, pady=5)
frame_new_customer.pack(padx=10, pady=10)
button_new = Button(frame_new_customer, text="New Customer")
button_new.pack()

root.mainloop()
