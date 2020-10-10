from tkinter import *

root = Tk()
root.title('My GUI')
root.geometry("500x500")

# Search for customers
frame_search = LabelFrame(root, text="Search for customer here", padx=15, pady=15)
frame_search.pack()
e = Entry(frame_search, width=35, borderwidth=5)
e.pack()


def button_search_click(query):
    results = query
    label_results = Label(frame_results, text=f'{results}')
    label_results.pack()


button_search = Button(frame_search, text="Search", padx=0, pady=0, command=lambda: button_search_click(e.get()))
button_search.pack()
frame_results = LabelFrame(root, text='Results:', padx=15, pady=15)
frame_results.pack()
label_results_empty = Label(frame_results)
label_results_empty.pack()


# New customer
def button_newcustomer_click():
    newWindow = Toplevel(root)
    newWindow.title('New Customer')
    newWindow.geometry('200x200')
    Label(newWindow, text='New Customers').pack()


frame_new_customer = LabelFrame(root, padx=15, pady=15)
frame_new_customer.pack(padx=10, pady=10)
button_new = Button(frame_new_customer, text="New Customer", command=lambda: button_newcustomer_click())
button_new.pack()

root.mainloop()
