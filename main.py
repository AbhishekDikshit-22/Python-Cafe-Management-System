from tkinter import *
import random
import time
from tkinter import filedialog,messagebox



#funtions



def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textReceipt.get(1.0 , END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information', 'Your bill is successfully saved')


def receipt():
    textReceipt.delete(1.0,END)
    x= random.randint(100 , 1000)
    Billnumber = 'BILL' + str(x)
    date = time.strftime('%d/%m/%Y')
    textReceipt.insert(END, 'Receipt Ref:\t\t'+ Billnumber+date+'\n')
    textReceipt.insert(END,'************************************************************\n')
    textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
    textReceipt.insert(END,'************************************************************\n')
    if e_roti.get()!= '0':
        textReceipt.insert(END, f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
        
    if e_rice.get()!= '0':
        textReceipt.insert(END, f'Rice\t\t\t{int(e_rice.get())*50}\n\n')
        
    if e_dal.get()!= '0':
        textReceipt.insert(END, f'Dal\t\t\t{int(e_dal.get())*60}\n\n')
    
    if e_paneer.get()!= '0':
        textReceipt.insert(END, f'Paneer\t\t\t{int(e_paneer.get())*120}\n\n')
        
    if e_mutton.get()!= '0':
        textReceipt.insert(END, f'Mutton\t\t\t{int(e_mutton.get())*180}\n\n')
        
    if e_chicken.get()!= '0':
        textReceipt.insert(END, f'Chicken\t\t\t{int(e_chicken.get())*160}\n\n')
        
    if e_mixveg.get()!= '0':
        textReceipt.insert(END, f'Mix-Veg\t\t\t{int(e_mixveg.get())*90}\n\n')
        
    if e_fish.get()!= '0':
        textReceipt.insert(END, f'Fish\t\t\t{int(e_fish.get())*100}\n\n')
        
    if e_rajma.get()!= '0':
        textReceipt.insert(END, f'Rajma\t\t\t{int(e_rajma.get())*85}\n\n')
        
     
    textReceipt.insert(END,'************************************************************\n')
    
    
    
    
        
    if e_lassi.get()!= '0':
        textReceipt.insert(END, f'Lassi\t\t\t{int(e_lassi.get())*60}\n\n')
        
    if e_coffee.get()!= '0':
        textReceipt.insert(END, f'Coffee\t\t\t{int(e_coffee.get())*80}\n\n')
        
    if e_faluda.get()!= '0':
        textReceipt.insert(END, f'Faluda\t\t\t{int(e_faluda.get())*120}\n\n')
        
    if e_shikanji.get()!= '0':
        textReceipt.insert(END, f'Shikanji\t\t\t{int(e_shikanji.get())*40}\n\n')
        
    if e_jaljeera.get()!= '0':
        textReceipt.insert(END, f'Jaljeera\t\t\t{int(e_jaljeera.get())*30}\n\n')
        
    if e_roohfza.get()!= '0':
        textReceipt.insert(END, f'Roohfza\t\t\t{int(e_roohfza.get())*50}\n\n')
        
    if e_masalatea.get()!= '0':
        textReceipt.insert(END, f'Masala-Tea\t\t\t{int(e_masalatea.get())*55}\n\n')
        
    if e_badammilk.get()!= '0':
        textReceipt.insert(END, f'Badam-milk\t\t\t{int(e_badammilk.get())*80}\n\n')
        
    if e_colddrinks.get()!= '0':
        textReceipt.insert(END, f'Cold-Drinks\t\t\t{int(e_colddrinks.get())*50}\n\n')


    
    
    
    textReceipt.insert(END,'************************************************************\n')

        
    if e_oreo.get()!= '0':
        textReceipt.insert(END, f'Oreo cake\t\t\t{int(e_oreo.get())*450}\n\n')
        
    if e_apple.get()!= '0':
        textReceipt.insert(END, f'Apple Cake\t\t\t{int(e_apple.get())*360}\n\n')
        
    if e_kitkat.get()!= '0':
        textReceipt.insert(END, f'Kitkat Cake\t\t\t{int(e_kitkat.get())*440}\n\n')
        
    if e_vanilla.get()!= '0':
        textReceipt.insert(END, f'Vanilla Cake\t\t\t{int(e_vanilla.get())*300}\n\n')
        
    if e_banana.get()!= '0':
        textReceipt.insert(END, f'Banana Cake\t\t\t{int(e_banana.get())*360}\n\n')
        
    if e_brownie.get()!= '0':
        textReceipt.insert(END, f'Brownie\t\t\t{int(e_brownie.get())*220}\n\n')
        
    if e_pineapple.get()!= '0':
        textReceipt.insert(END, f'Pineapple Cake\t\t\t{int(e_pineapple.get())*350}\n\n')
        
    if e_chocolate.get()!= '0':
        textReceipt.insert(END, f'Chocolate\t\t\t{int(e_chocolate.get())*420}\n\n')
        
    if e_blackforest.get()!= '0':
        textReceipt.insert(END, f'Black Forest\t\t\t{int(e_blackforest.get())*500}\n\n')
    

    textReceipt.insert(END,'************************************************************\n')
    textReceipt.insert(END,'************************************************************\n')
    if costoffoodvar.get()!= '0 Rs':
        textReceipt.insert(END, f'Cost of Food\t\t\t{priceofFood}Rs\n\n')
        
    if costofdrinksvar.get()!= '0 Rs':
        textReceipt.insert(END, f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n\n')
    
    if costofcakesvar.get()!= '0 Rs':
        textReceipt.insert(END, f'Cost of cakes\t\t\t{priceofCakes}Rs\n\n')
    textReceipt.insert(END,'************************************************************\n')
    
    
    textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
    textReceipt.insert(END, f'Sub Total\t\t\t{servicetax}Rs\n\n')
    textReceipt.insert(END, f'Sub Total\t\t\t{totalcostItems}Rs\n\n')


def totalcost():
    global priceofCakes , subtotalofItems, servicetax,totalcostItems
    global priceofFood
    global priceofDrinks
    
    item1=int(e_roti.get())
    item2=int(e_rice.get())
    item3=int(e_dal.get())
    item4=int(e_paneer.get())
    item5=int(e_mutton.get())
    item6=int(e_chicken.get())
    item7=int(e_mixveg.get())
    item8=int(e_fish.get())
    item9=int(e_rajma.get())
    
    item10=int(e_lassi.get())
    item11=int(e_coffee.get())
    item12=int(e_faluda.get())
    item13=int(e_shikanji.get())
    item14=int(e_jaljeera.get())
    item15=int(e_roohfza.get())
    item16=int(e_masalatea.get())
    item17=int(e_badammilk.get())
    item18=int(e_colddrinks.get())
    
    item19=int(e_oreo.get())
    item20=int(e_apple.get())
    item21=int(e_kitkat.get())
    item22=int(e_vanilla.get())
    item23=int(e_banana.get())
    item24=int(e_brownie.get())
    item25=int(e_pineapple.get())
    item26=int(e_chocolate.get())
    item27=int(e_blackforest.get())
    
    
    priceofFood = (item1*10) + (item2*50) + (item3*60) + (item4*120) + (item5*180) + (item6*160) \
        + (item7*90) + (item8*100) + (item9*85)
    
    priceofDrinks = (item10*60) + (item11*80) + (item12*120) + (item13*40) \
        + (item14 *30) + (item15*50) + (item16*55) + (item17*80) + (item18*50)
        
    priceofCakes = (item19*450) + (item20*360)  + (item21*440) + (item22*300) \
        + (item23*360) + (item24*220) + (item25*350) + (item26*420) + (item27*500)    
        
        
    costoffoodvar.set(str(priceofFood)+' Rs')
    costofdrinksvar.set(str(priceofDrinks)+' Rs')
    costofcakesvar.set(str(priceofCakes)+' Rs')
    
    subtotalofItems=priceofFood+priceofDrinks+priceofCakes
    subtotalvar.set(str(subtotalofItems)+' Rs')
    
    servicetax= 0.18 * subtotalofItems 
    servicetaxvar.set(str(servicetax)+' Rs')
    totalcostItems= subtotalofItems + servicetax
    totalcostvar.set(str(totalcostItems)+' Rs')



def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def rice():
    if var2.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')

def dal():
    if var3.get()==1:
        textdal.config(state=NORMAL)
        textdal.delete(0,END)
        textdal.focus()
    else:
        textdal.config(state=DISABLED)
        e_dal.set('0')

def paneer():
    if var4.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def mutton():
    if var5.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def chicken():
    if var6.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def mixveg():
    if var7.get()==1:
        textmixveg.config(state=NORMAL)
        textmixveg.delete(0,END)
        textmixveg.focus()
    else:
        textmixveg.config(state=DISABLED)
        e_mixveg.set('0')

def fish():
    if var8.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def rajma():
    if var9.get()==1:
        textrajma.config(state=NORMAL)
        textrajma.delete(0,END)
        textrajma.focus()
    else:
        textrajma.config(state=DISABLED)
        e_rajma.set('0')

def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def faluda():
    if var12.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def shikanji():
    if var13.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')
        
def jaljeera():
    if var14.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
        
def roohfza():
    if var15.get()==1:
        textroohfza.config(state=NORMAL)
        textroohfza.delete(0,END)
        textroohfza.focus()
    else:
        textroohfza.config(state=DISABLED)
        e_roohfza.set('0')



def masalatea():
    if var16.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')

def badammilk():
    if var17.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')

def colddrinks():
    if var18.get()==1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.delete(0,END)
        textcolddrinks.focus()
    else:
        textcolddrinks.config(state=DISABLED)
        e_colddrinks.set('0')

def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')

def kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def brownie():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')

def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def chocolate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def blackforest():
    if var27.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')





root = Tk()

root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title('Cafe Management System')
root.config(bg='firebrick4')

topFrame = Frame(root , bd =10, relief = RIDGE , bg='firebrick4')
topFrame.pack(side=TOP)
labelTitle = Label(topFrame, text = 'Cafe Management System', font=('sans-serif', 30,'bold'),
                   fg='yellow' , bg='red4' , bd =9 , width= 50)
labelTitle.grid(row=0, column=0)

#frames

menuFrame = Frame(root, bd =10, relief= RIDGE , bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame , bd= 4 ,  relief=RIDGE , bg='firebrick4')
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame , text='Food', font=('ariaL' , 19 ,'bold'), bd=10, relief=RIDGE ,fg='red4',bg='white')
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame , text='Drinks', font=('ariaL' , 19 ,'bold'), bd=10, relief=RIDGE, fg='red4', bg='white')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame , text='Cakes', font=('ariaL' , 19 ,'bold'), bd=10, relief=RIDGE,fg='red4',bg='white')
cakesFrame.pack(side=LEFT)

rightFrame = Frame(root , bd =15 , relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame , bd =1 , relief= RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame = Frame(rightFrame , bd= 4 ,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame = Frame(rightFrame , bd= 3 ,relief=RIDGE,bg='red4')
buttonFrame.pack()



#Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()


e_roti=StringVar()
e_rice=StringVar()
e_dal=StringVar()
e_paneer=StringVar()
e_mutton=StringVar()
e_chicken=StringVar()
e_mixveg=StringVar()
e_fish=StringVar()
e_rajma=StringVar()

e_roti.set('0')
e_rice.set('0')
e_dal.set('0')
e_paneer.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_mixveg.set('0')
e_fish.set('0')
e_rajma.set('0')


e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jaljeera=StringVar()
e_roohfza=StringVar()
e_masalatea=StringVar()
e_badammilk=StringVar()
e_colddrinks=StringVar()

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_masalatea.set('0')
e_jaljeera.set('0')
e_roohfza.set('0')
e_badammilk.set('0')
e_colddrinks.set('0')

e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()
e_blackforest=StringVar()

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')


costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()




#FOOD

roti= Checkbutton(foodFrame, text='Roti', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var1,
                  command=roti)
roti.grid(row=0 , column= 0 ,sticky=W)

rice= Checkbutton(foodFrame, text='Rice', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var2,
                  command=rice)
rice.grid(row=1 , column= 0,sticky=W)

dal= Checkbutton(foodFrame, text='Dal', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var3,
                 command=dal)
dal.grid(row=2 , column= 0,sticky=W)

paneer= Checkbutton(foodFrame, text='Paneer', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var4,
                    command=paneer)
paneer.grid(row=3 , column= 0,sticky=W)

mutton= Checkbutton(foodFrame, text='Mutton', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var5,
                    command=mutton)
mutton.grid(row=4 , column= 0,sticky=W)

chicken= Checkbutton(foodFrame, text='Chicken', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var6,
                     command=chicken)

chicken.grid(row=5 , column= 0,sticky=W)

mixveg= Checkbutton(foodFrame, text='Mix Veg', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var7,
                    command=mixveg)
mixveg.grid(row=6 , column= 0,sticky=W)

fish= Checkbutton(foodFrame, text='Fish', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var8,
                  command=fish)
fish.grid(row=7 , column= 0,sticky=W)

rajma= Checkbutton(foodFrame, text='Rajma', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var9,
                   command=rajma)
rajma.grid(row=8 , column= 0,sticky=W)


#Entry fields for Food items

textroti= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0 ,column=1)

textrice= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=1 ,column=1)

textdal= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_dal)
textdal.grid(row=2 ,column=1)

textpaneer= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=3 ,column=1)

textmutton= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=4 ,column=1)

textchicken= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=5 ,column=1)

textmixveg= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_mixveg)
textmixveg.grid(row=6 ,column=1)

textfish= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=7 ,column=1)

textrajma= Entry(foodFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_rajma)
textrajma.grid(row=8 ,column=1)


#Drinks

lassi= Checkbutton(drinksFrame, text='Lassi', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var10,
                   command=lassi)
lassi.grid(row=0 , column= 0,sticky=W)

coffee= Checkbutton(drinksFrame, text='Coffee', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var11,
                    command=coffee)
coffee.grid(row=1 , column= 0,sticky=W)

faluda= Checkbutton(drinksFrame, text='Faluda', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var12,
                    command=faluda)
faluda.grid(row=2 , column= 0,sticky=W)

shikanji= Checkbutton(drinksFrame, text='Shikanji', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var13,
                      command=shikanji)
shikanji.grid(row=3 , column= 0,sticky=W)

jaljeera= Checkbutton(drinksFrame, text='JalJeera', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var14,
                      command=jaljeera)
jaljeera.grid(row=4 , column= 0,sticky=W)

roohfza= Checkbutton(drinksFrame, text='Roohfza', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var15,
                     command=roohfza)
roohfza.grid(row=5 , column= 0,sticky=W)

masalatea= Checkbutton(drinksFrame, text='Masala-Tea', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var16,
                       command=masalatea)
masalatea.grid(row=6 , column= 0,sticky=W)

badammilk= Checkbutton(drinksFrame, text='Badam-Milk', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var17,
                       command=badammilk)
badammilk.grid(row=7 , column= 0,sticky=W)

colddrinks= Checkbutton(drinksFrame, text='Cold- Drinks', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var18,
                        command=colddrinks)
colddrinks.grid(row=8 , column= 0,sticky=W)

#Entry Fields in Drinks

textlassi= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0 ,column=1)


textcoffee= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1 ,column=1)

textfaluda= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2 ,column=1)

textshikanji= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3 ,column=1)

textjaljeera= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=4 ,column=1)

textroohfza= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_roohfza)
textroohfza.grid(row=5 ,column=1)

textmasalatea= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6 ,column=1)

textbadammilk= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=7 ,column=1)

textcolddrinks= Entry(drinksFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_colddrinks)
textcolddrinks.grid(row=8 ,column=1)


#cakes

oreo= Checkbutton(cakesFrame, text='Oreo Cake', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var19,
                  command=oreo)
oreo.grid(row=0 , column= 0,sticky=W)

apple= Checkbutton(cakesFrame, text='Apple', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var20,
                   command=apple)
apple.grid(row=1 , column= 0,sticky=W)

kitkat= Checkbutton(cakesFrame, text='Kitkat', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var21,
                    command=kitkat)
kitkat.grid(row=2 , column= 0,sticky=W)

vanilla= Checkbutton(cakesFrame, text='Vanilla', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var22,
                     command=vanilla)
vanilla.grid(row=3 , column= 0,sticky=W)

banana= Checkbutton(cakesFrame, text='Banana', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var23,
                    command=banana)
banana.grid(row=4 , column= 0,sticky=W)

brownie= Checkbutton(cakesFrame, text='Brownie', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var24,
                     command=brownie)
brownie.grid(row=5 , column= 0,sticky=W)

pineapple= Checkbutton(cakesFrame, text='Pineapple', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var25,
                       command=pineapple)
pineapple.grid(row=6 , column= 0,sticky=W)

chocolate= Checkbutton(cakesFrame, text='Chocolate', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var26,
                       command=chocolate)
chocolate.grid(row=7 , column= 0,sticky=W)

blackforest= Checkbutton(cakesFrame, text='Black Forest', font=('arial', 18 ,'bold'), onvalue= 1, offvalue=0 , variable=var27,
                         command=blackforest)
blackforest.grid(row=8 , column= 0,sticky=W)

#Entry fields in cakes

textoreo= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0 ,column=1)

textapple= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1 ,column=1)

textkitkat= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2 ,column=1)

textvanilla= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3 ,column=1)

textbanana= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4 ,column=1)

textbrownie= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5 ,column=1)

textpineapple= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6 ,column=1)

textchocolate= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7 ,column=1)

textblackforest= Entry(cakesFrame, font=('arial',18,'bold'),bd =7, width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8 ,column=1)


#costlabels and entry fields

labelCostofFood=Label(costFrame,text='Cost of Food', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=40)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=40)

labelCostofCakes=Label(costFrame,text='Cost of Cakes', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=40)


labelSubTotal=Label(costFrame,text='Sub Total', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=40)

labelServiceTax=Label(costFrame,text='Service Tax', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=40)

labelTotalCost=Label(costFrame,text='Total Cost', font=('arial',16,'bold'), bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=15,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=40)


#Buttons


buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,
                     command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,
                  command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3)
buttonReset.grid(row=0,column=4)

#textarea

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=40,height=15)
textReceipt.grid(row=0,column=0)


#calculator

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)
    
def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''
    


calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,font=('arial',15,'bold'),text='7',width=7,fg='yellow',bg='firebrick4',bd=5,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,font=('arial',15,'bold'),text='8',width=7,fg='yellow',bg='firebrick4',bd=5,
               command=lambda: buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,font=('arial',15,'bold'),text='9',width=7,fg='yellow',bg='firebrick4',bd=5,
               command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,font=('arial',15,'bold'),text='+',width=7,fg='yellow',bg='firebrick4',bd=5,
                  command=lambda: buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,font=('arial',15,'bold'),text='4',width=7,fg='yellow',bg='firebrick4',bd=3,
               command=lambda: buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,font=('arial',15,'bold'),text='5',width=7,fg='red4',bg='white',bd=3,
               command=lambda: buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,font=('arial',15,'bold'),text='6',width=7,fg='red4',bg='white',bd=3,
               command=lambda: buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,font=('arial',15,'bold'),text='-',width=7,fg='yellow',bg='firebrick4',bd=3,
                   command=lambda: buttonClick('-'))
buttonMinus.grid(row=2,column=3)


button1=Button(calculatorFrame,font=('arial',15,'bold'),text='1',width=7,fg='yellow',bg='firebrick4',bd=3,
               command=lambda: buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,font=('arial',15,'bold'),text='2',width=7,fg='red4',bg='white',bd=3,
               command=lambda: buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,font=('arial',15,'bold'),text='3',width=7,fg='red4',bg='white',bd=3,
               command=lambda: buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,font=('arial',15,'bold'),text='*',width=7,fg='yellow',bg='firebrick4',bd=3,
                  command=lambda: buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,font=('arial',15,'bold'),text='Ans',width=7,fg='yellow',bg='firebrick4',bd=3,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,font=('arial',15,'bold'),text='Clear',width=7,fg='yellow',bg='firebrick4',bd=3,
                   command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,font=('arial',15,'bold'),text='0',width=7,fg='yellow',bg='firebrick4',bd=3,
               command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,font=('arial',15,'bold'),text='/',width=7,fg='yellow',bg='firebrick4',bd=3,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()
