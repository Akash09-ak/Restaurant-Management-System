from tkinter import *               # importing all classes from tkinter package
import random                       # usimg random package
import time                         # using time package
import string                       # importing string package for using stirng functions without warning error
  
#----------------------------------------------- creating  new window-----------------------------------
window=Tk()

#----------------------------------------------- creating geometry of window----------------------------
window.geometry("1600x800+0+0")
window.minsize(1200,600)            # giving window a minimum size

#-------------------------------------------------- naming the window or giving it a title-----------------
window.title("Ichiraku Ramen Management System")


#------------------------------------- taking input for claculator display------------------
myinput=StringVar()
op=""

#----------------------------------------------- creating frames---------------------------------------------
top=Frame(window,width=1600,bg= "black", relief=SUNKEN)
top.pack(side="top")                                          # here we can either write side=TOP  or side="top" both are right but non else
f1=Frame(window,width=800,height= 700, relief=SUNKEN)
f1.pack(side=LEFT)                                              # or f1.pack(side="left")
f2=Frame(window,width=300,height= 700,bg= "cyan", relief=SUNKEN)
f2.pack(side="right")

#--------------------------------------------------- getting current time--------------------------------------
currenttime=time.asctime(time.localtime(time.time()))


#-------------------------------------------- creating labels for my window(info about our sytem)---------------------
mylabel=Label(top,font=("arial",50,"bold","underline"),fg="red",bg="black",text="Welcome to Ichiraku Ramen ",bd=10,anchor='w')
mylabel.grid(row=0,column=0)
mytime=Label(top,font=("arial",20,"bold"),fg="red",bg="black",text=currenttime,bd=10,anchor='w')          # here border=10 and this functionshowing current date n time
mytime.grid(row=1,column=0)


#-------------------------- ------------------- creating calculator----------------------------------------

    
def btnClick(num):                                      # it will take values
    global op                                        # defining global string variable    , putting it empty above
    op=op+str(num)                                  # adding input to op by concatination
    myinput.set(op)                                # giving myinput value

# function to clear calculator display
def Clearscreen():                  
    op=""
    myinput.set(op)

# function to get calculation for = button
def Equals():
    global op
# using try except bloack for invalid expresions
    try:
        calculate=str(eval(op))                                  # eval function gets the result of expression
    except:
        calculate=""
    myinput.set(calculate)
    op=""

# function to get total and  Random reference
def Ref():
    x=random.randint(12999,50898)   # creating random no.
    randomRef=str(x)

    myref.set(randomRef)
    try:
        pricenoodles=float(Noodles.get())
    except:
        pricenoodles = 0.0
    try:
        pricespringroll = float(SpringRoll.get())
    except:
        pricespringroll = 0.0
    try:
        priceburger = float(Burger.get())
    except:
        priceburger = 0.0
    try:
        pricekabab = float(Kabab.get())
    except:
        pricekabab = 0.0
    try:
        pricemomos = float(Momos.get())
    except:
        pricemomos = 0.0
    try:
        pricemasalakabab=float(MasalaKabab.get())
    except:
        pricemasalakabab=0.0
    try:
        pricevegmanchurian = float(VegManchurian.get())
    except:
        pricevegmanchurian=0.0
    try:
        priceredpasta= float(RedPasta.get())
    except:
        priceredpasta=0.0
    try:
        pricewhitepasta = float(WhitePasta.get())
    except:
        pricewhitepasta=0.0
    try:
        pricenchillipotato = float(ChilliPotato.get())
    except:
        pricenchillipotato=0.0
    try:
        pricencolddrink = float(ColdDrink.get())
    except:
        pricencolddrink=0.0


    totalpricenoodles = pricenoodles* 50
    totalpricespringroll = pricespringroll*60
    totalpriceburger = priceburger*50
    totalpricekabab = pricekabab*60
    totalpricemomos = pricemomos*60
    totalpricemasalakabab = pricemasalakabab*80
    totalpricevegmanchurian = pricevegmanchurian*70
    totalpriceredpasta =priceredpasta*80
    totalpricewhitepasta = pricewhitepasta*80
    totalpricenchillipotato = pricenchillipotato*100
    totalpricencolddrink = pricencolddrink*30

    Totalcost="₹",str( totalpricenoodles + totalpricespringroll + totalpriceburger + totalpricekabab + totalpricemomos + totalpricemasalakabab + totalpricevegmanchurian + totalpriceredpasta + totalpricewhitepasta + totalpricenchillipotato + totalpricencolddrink)

    Total.set(Totalcost)


# function to exit from code
def Quit():
    window.destroy()

# function to reset value
def Reset():
    myref.set("")
    Noodles.set("")
    SpringRoll.set("")
    Burger.set("")
    Kabab.set("")
    Momos.set("")
    VegManchurian.set("")
    MasalaKabab.set("")
    ChilliPotato.set("")
    RedPasta.set("")
    WhitePasta.set("")
    ColdDrink.set("")
    Total.set("")


textdisplay=Entry(f2,font=("arial",20,"bold"),textvariable=myinput,bd=30,bg="cyan",justify="right")       # here justify="right is used to take input from right to left
textdisplay.grid(columnspan=4)                     # giving 4 column space

# first row of claculator
btn7= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="7",bg="cyan",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="8",bg="cyan",command=lambda: btnClick(8)).grid(row=2,column=1)

btn8= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="9",bg="cyan",command=lambda: btnClick(9)).grid(row=2,column=2)

Addbutton= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="+",bg="cyan",command=lambda: btnClick('+')).grid(row=2,column=3)


# second row of calculator
btn4= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="4",bg="cyan",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="5",bg="cyan",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="6",bg="cyan",command=lambda: btnClick(6)).grid(row=3,column=2)

Subbutton= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="-",bg="cyan",command=lambda: btnClick('-')).grid(row=3,column=3)


# third row of calculator
btn1= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="1",bg="cyan",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="2",bg="cyan",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="3",bg="cyan",command=lambda: btnClick(3)).grid(row=4,column=2)

Mulbutton= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="*",bg="cyan",command=lambda: btnClick('*')).grid(row=4,column=3)


# forth row of calculator
btn0= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="0",bg="cyan",command=lambda: btnClick(0)).grid(row=5,column=0)

Clearbtn= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="C",bg="cyan",command=Clearscreen).grid(row=5,column=1)   # here we can use it without lambda if we use lambda we have to use paranthesis after Clearscreen function

Equalbtn= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="=",bg="cyan",command=Equals).grid(row=5,column=2)

Divbutton= Button(f2,padx=16,pady=16,bd=9,fg="black",font=("arial",20,"bold"),text="/",bg="cyan",command=lambda: btnClick('/')).grid(row=5,column=3)


#---------------------------------------------------------------- Restro. Info --------------------------
myref=StringVar()
Noodles=StringVar()
SpringRoll=StringVar()
Burger=StringVar()
Kabab=StringVar()
Momos=StringVar()
VegManchurian=StringVar()
MasalaKabab=StringVar()
ChilliPotato=StringVar()
Macroni=StringVar()
RedPasta=StringVar()
WhitePasta=StringVar()
ColdDrink=StringVar()
Total=StringVar()


labelref=Label(f1,font=("arial",16,"bold"),text="Refrence",bd=16,anchor='w')
labelref.grid(row=0,column=0)
textref=Entry(f1,font=("arial",16,"bold"),textvariable=myref,bd=16,bg="blue",justify="right")
textref.grid(row=0,column=1)


labelnoodles=Label(f1,font=("arial",16,"bold"),text="Noodles/Ramen",bd=16,anchor='w')
labelnoodles.grid(row=1,column=0)
textnoodles=Entry(f1,font=("arial",16,"bold"),textvariable=Noodles,bd=16,bg="blue",justify="right")
textnoodles.grid(row=1,column=1)


labelroll=Label(f1,font=("arial",16,"bold"),text="Spring Roll",bd=16,anchor='w')
labelroll.grid(row=2,column=0)
textroll=Entry(f1,font=("arial",16,"bold"),textvariable=SpringRoll,bd=16,bg="blue",justify="right")
textroll.grid(row=2,column=1)


labelburger=Label(f1,font=("arial",16,"bold"),text="Burger",bd=16,anchor='w')
labelburger.grid(row=3,column=0)
textburger=Entry(f1,font=("arial",16,"bold"),textvariable=Burger,bd=16,bg="blue",justify="right")
textburger.grid(row=3,column=1)


labelkabab=Label(f1,font=("arial",16,"bold"),text="Kabab",bd=16,anchor='w')
labelkabab.grid(row=4,column=0)
textkabab=Entry(f1,font=("arial",16,"bold"),textvariable=Kabab,bd=16,bg="blue",justify="right")
textkabab.grid(row=4,column=1)



labelmomos=Label(f1,font=("arial",16,"bold"),text="Momos",bd=16,anchor='w')
labelmomos.grid(row=5,column=0)
textmomos=Entry(f1,font=("arial",16,"bold"),textvariable=Momos,bd=16,bg="blue",justify="right")
textmomos.grid(row=5,column=1)


labelvegmanchurian=Label(f1,font=("arial",16,"bold"),text="Veg. Manchurian",bd=16,anchor='w')
labelvegmanchurian.grid(row=6,column=0)
textvegmanchurian=Entry(f1,font=("arial",16,"bold"),textvariable=VegManchurian,bd=16,bg="blue",justify="right")
textvegmanchurian.grid(row=6,column=1)




#---------------------------------------------- Restro. Info 2--------------------------------------------------------

labelmasalakabab=Label(f1,font=("arial",16,"bold"),text="Masala Kabab",bd=16,anchor='w')
labelmasalakabab.grid(row=0,column=2)
textmasalakabab=Entry(f1,font=("arial",16,"bold"),textvariable=MasalaKabab,bd=16,bg="blue",justify="right")
textmasalakabab.grid(row=0,column=3)


labelredpasta=Label(f1,font=("arial",16,"bold"),text="Red Pasta",bd=16,anchor='w')
labelredpasta.grid(row=1,column=2)
textredpasta=Entry(f1,font=("arial",16,"bold"),textvariable=RedPasta,bd=16,bg="blue",justify="right")
textredpasta.grid(row=1,column=3)


labelwhitepasta=Label(f1,font=("arial",16,"bold"),text="White Pasta",bd=16,anchor='w')
labelwhitepasta.grid(row=2,column=2)
textwhitepasta=Entry(f1,font=("arial",16,"bold"),textvariable=WhitePasta,bd=16,bg="blue",justify="right")
textwhitepasta.grid(row=2,column=3)


labelchillipotato = Label(f1, font=("arial", 16, "bold"), text="Chilli Potato", bd=16, anchor='w')
labelchillipotato.grid(row=3, column=2)
textchillipotato = Entry(f1, font=("arial", 16, "bold"), textvariable=ChilliPotato, bd=16, bg="blue", justify="right")
textchillipotato.grid(row=3, column=3)


labelcolddrink = Label(f1, font=("arial", 16, "bold"), text="Cold Drink", bd=16, anchor='w')
labelcolddrink.grid(row=4, column=2)
textcolddrink = Entry(f1, font=("arial", 16, "bold"), textvariable=ColdDrink, bd=16, bg="blue", justify="right")
textcolddrink.grid(row=4, column=3)


labeltotal = Label(f1, font=("arial", 16, "bold"), text="Total", bd=16, anchor='w')
labeltotal.grid(row=5, column=2)
texttotal= Entry(f1, font=("arial", 16, "bold"), textvariable=Total, bd=16, bg="blue", justify="right")
texttotal.grid(row=5, column=3)

#--------------------------------------------------Buttons-----------------------------------------
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("Arial",16,"bold"),text="Total", bg="powder blue", command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("Arial",16,"bold"),text="Reset", bg="powder blue", command=Reset).grid(row=7,column=1)

btnQuit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("Arial",16,"bold"),text="Quit", bg="powder blue", command=Quit).grid(row=7,column=2)


window.mainloop()
