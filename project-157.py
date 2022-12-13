# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:24:48 2022

@author: User
"""

from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("Endless Pokemon card Game 2")
root.geometry("600x700")
root.configure(background="chocolate1")

but = ImageTk.PhotoImage(Image.open("button.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
ivyasaur=ImageTk.PhotoImage(Image.open("ivysaur.jpg"))



player1_label = Label(root,text="Player 1",bg="red",fg="white")
player1_label.place(relx=0.1,rely =0.3, anchor=CENTER)

player2_label = Label(root,text="Player 2",bg="red",fg="white")
player2_label.place(relx=0.9,rely =0.3, anchor=CENTER)

player1_score_label = Label(root, bg="royal blue", fg="white")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score_label = Label(root, bg="royal blue", fg="white")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

label_image = Label(root)
label_image.place(relx=0.5, rely=0.5)

pokemon_list = ["Charmander","Jigglypuff","Squirtle","Kadabra","Persion","Nidoking","Ivysaur"]
pokemon_hp = ["50","70","50","70","70","90","100"]

player1_score = 0

def player1() :
    global player1_score
    random_card = random.randint(1,7)
    random_pokemon= pokemon_list[random_card]
    label_image["image"] = random_card
    
    random_hp = pokemon_hp[random_no]
    player1_score = player1_score + random_hp
    player1_score_label["text"]= str(player1_score)
   
    
player2_score = 0

def player2() :
    global player2_score
    random_card2 = random.randint(1,7)
    random_pokemon2= pokemon_list[random_card]
    label_image["image"] = random_card2
    
    random_hp2 = pokemon_hp[random_no]
    player2_score = player2_score + random_hp2
    player2_score_label["text"]= str(player2_score)
   

    

player1_btn = Button(root, image = button, command=player1)
player1_btn.place(relx=0.1, rely=0.5, anchor=CENTER)

player2_btn = Button(root, image = button , command=player2)
player2_btn.place(relx=0.9, rely=0.5, anchor=CENTER)
root.mainloop()