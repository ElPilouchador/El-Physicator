import os
import tkinter as Tk
from PIL import Image, ImageTk, ImageDraw
from math import *

#-fonctions-#
def fonction(event):
    global angle
    angle=entree1.get()
    entree1.delete(0,Tk.END)
    try:
        angle==int(recup)
        erreur = False
    except:
        Tk.messagebox.showerror("Erreur","Entrez un angle compris entre 0 et 90.")
        erreur = True
    if not erreur:
        if angle>=90 or angle<=0:
            Tk.messagebox.showerror("Erreur","Entrez un angle compris entre 0 et 90.")
    return()
#fct menu environnement
def fond():
    rep=os.getcwd
    fic=""
    root=Tk.Tk()
    root.withdraw()
    fichier=Tk.filedialog.askopenfilename(title="Ouvrir un fichier image", initialdir=rep,initialfile=fic,filetypes=[("Fichiers Image","*.jpeg;*.gif;*.jpg;*.png")])
    root.destroy()
    img=Image.open(fichier)
    w=img.size[0]
    h=img.size[1]
    root.destroy()
    can1.image=fichier
    can1.update()
    return()
def pente():
    texte1=Tk.label(fen1, text="Entrez un angle comprit entre 0 et 90:")
    entree1=Tk.Entry(fen1)
    #ligne
    x1,y1=w,h
    x2,y2=0,tan(angle)*w
    ligne=can1.create_line(x1,y1,x2,y2,width=2,fill="red",capstyle="round")
    return()
def G():
	global x1,y1,vx1,vy1,r1,w,h,gravite
    y1=y1-gravite
    can1.coords(balleVerte,x1-r1,y1-r1,x1+r1,y1+r1)

      
	return()
  
def createBalle():
  	can1.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,width=1,fill='black')
  	return()
def frottement():
	return()
def bougerballe():
    global x1,y1,vx1,vy1,r1,w,h
    #collisions bords
  	if x1+y1>=w:
        vx1=-10
    elif x1-r1<=0:
        vx1=10
    elif y1+r1>=h:
        vy1=-10
    elif y1-r1<=0:
        vy1=10
    #faire avancer balle
  	color= pixPil[x,y]
    if color==(255,0,0):
        collision()
    else :
		x1,y1=x1+vx1,y1+vy1
    
    can1.coords(balleVerte,x1-r1,y1-r1,x1+r1,y1+r1)
    G()  
    fen1.after(17,bougerVerte)
    return()
def collision() :
    #collision pente
	global x1, y1, Y, X, vx1, vy1, r1
    coulPix=[]
    for alpha in range(0, 360):
    	X=r1*(sin(alpha))+x1
    	Y=r1*(cos(alpha))+y1
		couleur=image.getpixel((X, Y))
        if couleur == "red":
    		x1 = (sin(angle)*vx1)+x1
    		y1 = (cos(angle)*vy1)+y1
    		can1.coords(balleVerte,x1-r1,y1-r1,x1+r1,y1+r1)
            return()
        else :
           continu
    return()
#-prog principal-
fen1=Tk.Tk()
fen1.title("El physicator")
x1=int(w)/2
y1=int(h)/2
r1=15
vx1,vy1=10,10
w=1000
h=1000

can1 = Tk.Canvas(fen1, width = w, height = h)
can1.pack()

menubar=Tk.Menu(fen1)
#menu environnement
menuEvrt=Tk.Menu(menubar,tearoff=0)
menuEvrt.add_command(label="Ajouter un fond", command=fond)
menuEvrt.add_command(label="Ajouter pente", command=pente)
menubar.add_cascade(label="Environnement", menu=menuEvrt)
#menu paramètres physiques
menuPhysique=Tk.Menu(menubar,tearoff=0)
menuPhysique.add-command(label="Gravité", command=G)
menubar.add_cascade(label="Paramètres physiques", menu=menuPhysique)
#menu matière
menuObjet=Tk.Menu(menubar,tearoff=0)
menuObjet.add_command(label="Matériaux", command=frottement)
menu.add_separator()
menuAjout=Tk.Menu(menuObjet, tearoff=0)
menuAjout.add-command(label="Balle", command=creatBalle)
menuObjet.add_cascade(label="Ajouter", menu=menuAjout)
menubar.add_cascade(label="Objet", menu=menuObjet)

fen1.config(menu=menubar)
fen1.mainloop()

#faire en fonction de la couleurs pixels en verifiant la couleur des pixels autour de la balle (avec le rayon de la balle) OKaaaa 
# /!\ PLUS : mettre hitbox !
#faire une fonction pour la vitesse, a chaque colision elle descent, on doit donc créer un boucle for pour determiner quand la boule doit arreter de monter et ensuite actioner la fonction G
