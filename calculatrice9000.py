from tkinter import*

class calculette():
    
    def __init__(entrer):
        entrer.num1=0
        entrer.num2=0
        entrer.result=0
        entrer.entry=StringVar()
        entrer.text=""
        entrer.oper=""
        entrer.entry.set("")

    def init(entrer):
        entrer.num1 = 0
        entrer.num2 = 0
        entrer.result = 0
        entrer.text = ""
        entrer.oper = ""
        
    def affichage(entrer):
        entrer.entry.set(entrer.text)
        
    def operateur(entrer):
        try :
            if "+" in entrer.text:
                entrer.addition()
            elif "-" in entrer.text:
                entrer.soustraction()
            elif "/" in entrer.text:
                entrer.division()
            elif "x" in entrer.text:
                entrer.multiplication()
        except:
            entrer.entry.set("Erreur")
            entrer.init()
            
    def addition(entrer):
        nb = entrer.text.split("+")
        entrer.num1 = float(nb[0])
        entrer.num2 = float(nb[1])
        entrer.result = entrer.num1 + entrer.num2
        entrer.entry.set(str(entrer.result))
        entrer.init()
        
    def soustraction(entrer):
        nb = entrer.text.split("-")
        entrer.num1 = float(nb[0])
        entrer.num2 = float(nb[1])
        entrer.result = entrer.num1 - entrer.num2
        entrer.entry.set(str(entrer.result))
        entrer.init()
        
    def multiplication(entrer):
        nb = entrer.text.split("x")
        entrer.num1 = float(nb[0])
        entrer.num2 = float(nb[1])
        entrer.result = entrer.num1 * entrer.num2
        entrer.entry.set(str(entrer.result))
        entrer.init()
        
    def division(entrer):    
        nb = entrer.text.split("/")
        entrer.num1 = float(nb[0])
        entrer.num2 = float(nb[1])
        entrer.result = entrer.num1 / entrer.num2
        entrer.entry.set(str(entrer.result))
        entrer.init()
        
    def afficher_nombre(entrer):
        entrer.set(entrer.text)

def bouton_1():
    calculatrice.text+="1"
    calculatrice.entry.set(calculatrice.text)
def bouton_2():
    calculatrice.text+="2"
    calculatrice.entry.set(calculatrice.text)
def bouton_3():
    calculatrice.text+="3"
    calculatrice.entry.set(calculatrice.text)
def bouton_4():
    calculatrice.text+="4"
    calculatrice.entry.set(calculatrice.text)
def bouton_5():
    calculatrice.text+="5"
    calculatrice.entry.set(calculatrice.text)
def bouton_6():
    calculatrice.text+="6"
    calculatrice.entry.set(calculatrice.text)
def bouton_7():
    calculatrice.text+="7"
    calculatrice.entry.set(calculatrice.text)
def bouton_8():
    calculatrice.text+="8"
    calculatrice.entry.set(calculatrice.text)
def bouton_9():
    calculatrice.text+="9"
    calculatrice.entry.set(calculatrice.text)
def bouton_0():
    calculatrice.text+="0"
    calculatrice.entry.set(calculatrice.text)
def bouton_effacer():
    calculatrice.entry.set("")
    calculatrice.init
def bouton_division():
    calculatrice.text+="/"
    calculatrice.entry.set(calculatrice.text)        
def bouton_operateur():
    calculatrice.operateur()
def bouton_multiplication():
    calculatrice.text+="x"
    calculatrice.entry.set(calculatrice.text)   
def bouton_additon():
    calculatrice.text+="+"
    calculatrice.entry.set(calculatrice.text)              
def bouton_soustraction():
    calculatrice.text+="-"
    calculatrice.entry.set(calculatrice.text) 
def bouton_point():
    calculatrice.text+="."
    calculatrice.entry.set(calculatrice.text) 
fen = Tk()
fen.title("Calculatrice9000")
calculatrice=calculette()
fen['bg']='gray'

ecran = Entry(fen, font = (20),bg='white' , textvariable = calculatrice.entry, bd=6)
ecran.grid(columnspan = 6, padx=20, pady=10)


boutton_7 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '7', command =bouton_7)
boutton_7.grid(row = 1, column = 0)

boutton_8 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '8', command =bouton_8) 
boutton_8.grid(row = 1, column = 1)

boutton_9 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '9', command =bouton_9)
boutton_9.grid(row = 1, column = 2)

boutton_additon = Button(fen, padx = 16,pady = 16, bd = 8, fg = 'black', font = (20), text = '+', command = bouton_additon) 
boutton_additon.grid(row = 1, column = 3)

boutton_4 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '4', command = bouton_4) 
boutton_4.grid(row = 2, column = 0)

boutton_5 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '5', command = bouton_5)
boutton_5.grid(row = 2, column = 1)

boutton_6 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '6', command = bouton_6) 
boutton_6.grid(row = 2, column = 2)

boutton_soustraction = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '-', command = bouton_soustraction)
boutton_soustraction.grid(row = 2, column = 3)

boutton_1 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '1',  command = bouton_1)
boutton_1.grid(row = 3, column = 0)

boutton_2 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '2',  command = bouton_2)
boutton_2.grid(row = 3, column = 1)

boutton_3 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '3', command = bouton_3)
boutton_3.grid(row = 3, column = 2)

boutton_multiplication = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '*', command = bouton_multiplication)
boutton_multiplication.grid(row = 3, column = 3)

boutton_0 = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '0', command = bouton_0)
boutton_0.grid(row = 4, column = 0)

boutton_effacer = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = 'C', command = bouton_effacer)
boutton_effacer.grid(row = 4, column = 1)

boutton_point = Button(fen, padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '.', command = bouton_point)
boutton_point.grid(row = 4, column = 2)

boutton_egal = Button(fen, padx =100, pady = 10, bd = 8, fg = 'black', font = (20), text = '=', command = bouton_operateur)
boutton_egal.grid(columnspan = 6, padx=20, pady=10)

boutton_division = Button(fen,padx = 16, pady = 16, bd = 8, fg = 'black', font = (20), text = '/', command = bouton_division)
boutton_division.grid(row = 4, column = 3)

fen.mainloop()