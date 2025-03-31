top.geometry(800x330+30+30)

Label = Label(top, text = "Enetr total amount", bg= 'light grey')
entry = Entry(top)
lbl = Label(top, text = "Here are the number of notes for each denoination", bg = 'light grey')

l1  Label(top, text = "2000", bg= 'light grey')
l2= Label(top, text= "500", bg = 'light grey')
l3 = Label(top, text= "100", bg= 'light grey')

t1 = Entry(top)
t2 = Entry(top)
t3 = Entry(top)


def calculator():
    try:
        global amount
        amount = int(entry.get)