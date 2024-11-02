#on importe les bibliothèques
import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk, ImageFilter
import random
import threading


class Application():
    def __init__(self):#fonction appelée à la création de la classe
        self.image = Image.new('RGB', (500, 500), (255, 0, 0)) #on initialize la variable image pour éviter une erreur si la fonction l.89 n'arrive pas a charger une image
    def show_img(self):#fonction pour afficher l'image conenue dans la variable self.image
        self.photo = ImageTk.PhotoImage(self.image)#on convertit le type d'image pour l'afficher
        self.image_label.config(image=self.photo)#on l'affiche dans un label tkinter

    #les lignes 17 à 23 et le script paint.py ne sont pas à prendre en compte
    def paint(self):#fonction pour ouvrir le créateur d'image
        from paint import Paint#on importe le script paint
        self.paint_appli = Paint()#on attribue l'appli
        self.paint_appli.__run__()#on démarre l'appli
    
    def rotate2(self):#fonction effectuant la rotation de l'image
        self.angle = int(self.angle.get())#on récupère la variable en int
        self.image = self.image.rotate(self.angle)#ion effectue une rotation de self.angle degrés
        self.show_img()#on affiche l'image
        self.rotate_button.destroy()#on supprime le boutton tkinter
        self.rotate_scale.destroy()#on supprime le scale tkinter
    
    def rotate(self):#fonction pour choisir l'angle choisit pour tourner l'image
        self.angle = tk.IntVar(value=0)#on initialise l'angle à 0
        self.rotate_scale = tk.Scale(self.root, orient='horizontal', variable=self.angle, from_=-180, to=180, resolution=1, length=200)#on définit un scale tkinter pour choisir l'angle
        self.rotate_button = tk.Button(self.root, text='Rotate', command=self.rotate2)#on définit un boutton tkinter pour valider l'angle voulu
        self.rotate_scale.grid()#on affiche le scale tkinter
        self.rotate_button.grid()#on affiche le boutton tkinter
    
    def flip_0(self):#fonction appelé pour retourner horizontalement l'image
        self.new_image = Image.new(self.image.mode, self.image.size)#image temporaire pour retourner l'image
        for i in range(self.image.width):#boucle pour chaque pixel en longueur
            for j in range(self.image.height):#boucle pour chaque pixel en hauteur
                self.new_image.putpixel((i, j), self.image.getpixel((self.image.width-i-1, j)))#on inverse les pixels horizontalement
        self.image = self.new_image#on finalise en mettant la variable image à la nouvelle image retournée
        self.show_img()#on affiche l'image
    
    def flip_1(self):#fonction appelé pour retourner verticalement l'image
        self.new_image = Image.new(self.image.mode, self.image.size)#image temporaire pour retourner l'image
        for i in range(self.image.width):#boucle pour chaque pixel en longueur
            for j in range(self.image.height):#boucle pour chaque pixel en hauteur
                self.new_image.putpixel((i, j), self.image.getpixel((i, self.image.height-j-1)))#on inverse les pixels verticalement
        self.image = self.new_image#on finalise en mettant la variable image à la nouvelle image retournée
        self.show_img()#on affiche l'image
    
    def change_sat2(self):#fonction pour changer la transparence d'une image
        self.sat = abs(int(self.sat.get())-255)#on récupère la variable modifiée dans la fonction l.36
        self.image.putalpha(self.sat)#on change la transparence de l'image
        self.show_img()#on affiche l'image
        self.sat_button.destroy()#on supprime le boutton tkinter
        self.sat_scale.destroy()#on supprime le slider tkinter
    
    def change_sat(self):#fonction pour choisir la nouvelle transparence d'une image
        self.image = self.image.convert('RGBA')#on convertit l'image en RGBA pour éviter les erreurs si l'image est en RGB par exemple
        self.sat = tk.IntVar()#on définit la variable contenant la valaur de la nouvelle transparence
        self.sat_scale = tk.Scale(self.root, orient='horizontal', variable=self.sat, from_=0, to=255, resolution=1, length=200)#on définit un scale tkinter pour choisir la transparence facilement
        self.sat_button = tk.Button(self.root, text='Change Saturation', command=self.change_sat2)#on définit le boutton tkinter pour vailder
        self.sat_scale.grid()#on affiche le scale tkinter
        self.sat_button.grid()#on affiche le boutton tkinter
    
    def convert_rgb(self):#fonction pour convertir l'image en format RGB
        self.image = self.image.convert('RGB')# on convertit en RGB
        self.show_img()#on affiche l'image
    
    def convert_rgba(self):#fonction pour convertir l'image en format RGBA
        self.image = self.image.convert('RGBA')# on convertit en RGBA
        self.show_img()#on affiche l'image
    
    def convert_gray(self):#fonction pour convertir l'image en format gris
        self.image = self.image.convert('L')#on converit en nuances de gris
        self.show_img()#on affiche l'image
    
    def blur(self):#fonction pour flouter l'image
        self.image = self.image.filter(ImageFilter.BLUR)#on applique un filtre pour flouter l'image
        self.show_img()#on affiche l'image
    
    def resize2(self):#fonction pour redimensionner l'image
        self.resize_val = int(self.resize_val.get())#on récupère le coeff qui va multiplier la resolution
        self.image = self.image.resize((self.image.width*self.resize_val, self.image.height*self.resize_val))#on multiplie la résolution par le coeff
        self.show_img()#on affiche l'image
        self.resize_scale.destroy()#on supprime le scale tkinter 
        self.resize_submit.destroy()#on supprime le boutton tkinter
    
    def resize(self):#fonction pour choisir le coeff de redimensionnement de l'image
        self.resize_val = tk.DoubleVar()#on définit le coeff qui va modifier la taille de l'image
        self.resize_scale = tk.Scale(self.root, orient='horizontal', variable=self.resize_val, from_=1, to=5, resolution=1, length=200)#on définit un scale tkinter pour choisir le coeff
        self.resize_scale.grid(padx=0, pady=0)#on affiche le scale
        self.resize_submit = tk.Button(self.root, text='Resize', command=self.resize2)##on définit le bouttonpour valider
        self.resize_submit.grid()#on affiche le boutton tkinter
    
    def change_res2(self):#fonction pour redimensionner l'image
        self.res_val = int(self.res_val[0].get()), int(self.res_val[1].get())#on récupère les nouvelles valeurs des dimensions de l'image
        self.image = self.image.resize((self.res_val[0], self.res_val[1]))#on redimensionne l'image
        self.show_img()#on affiche l'image
        self.width_scale.destroy()#on supprime le scale
        self.height_scale.destroy()#on supprime le scale
        self.res_button.destroy()#on supprime le scale
        
    def change_res(self):#fonction pour obtenir les nouvelles dimensions
        self.res_val = [tk.IntVar(value=self.image.width), tk.IntVar(value=self.image.height)]#on définit les nouvelles dimensions 
        self.width_scale = tk.Scale(self.root, orient='horizontal', variable=self.res_val[0], from_=1, to=self.image.width*2, length=500 )#on définit le scale pour choisir la largeur de l'image
        self.height_scale = tk.Scale(self.root, orient='horizontal', variable=self.res_val[1], from_=1, to=self.image.width*2, length=500 )#on définit le scale pour choisir la hauteur de l'image
        self.res_button = tk.Button(self.root, text='Change Resolution', command=self.change_res2)#on définit un boutton pour valider les valeurs
        self.width_scale.grid()#on affiche le scale largeur
        self.height_scale.grid()#on affiche le scale hauteur
        self.res_button.grid()#on affiche le boutton pour valider
        
    def save_file(self):#fonction pour sauvegarder l'image sur l'ordinateur
        self.file = asksaveasfile()#on ouvre une fenetre permettant de sauvegarder l'image en format désiré
        self.file = self.file.name#on récupère le PATH
        self.image.save(self.file)#on sauvegarde l'image
        
    def open_file(self):#fonction pour charger l'image depuis l'ordinateur
        self.file = askopenfile()#on ouvre une fenetre permettant de charger l'image
        self.file = self.file.name#on récupère le PATH 
        self.image = Image.open(self.file)#on charge l'image
        self.show_img()#on l'affiche
    
    def andy_thread1(self):#fonction pour créer une image à la façon Andy Wahrol
        new_image = Image.new('RGB', (self.copy_img.width, self.copy_img.height), (0, 0, 0))#on crée une image de taille 3 fois plus petite pour optimiser
        filter = [[random.randint(0, 255) for j in range(3)] for i in range(3)]#on choisit 3 couleurs aléatoire à modifier
        for i in range(self.copy_img.width):#pour chaque pixel en longueur
            for j in range(self.copy_img.height):#pour chaque pixel en hauteur
                R, G, B = self.copy_img.getpixel((i, j))#on récupère les couleurs du pixel voulu
                gris = (R+G+B)//3#on calcule le niveau de gris
                if gris<81:#si le gris est plus petit que 81
                    color = filter[0]#on prend la 1ere couleur
                elif gris<161:#si le gris est plus petit que 161
                    color = filter[1]#on prend la 2eme couleur
                else:#sinon
                    color = filter[2]#on prend la 3eme couleur
                new_image.putpixel((i, j), (tuple(color)))#on met le pixel contenant la couleur modifiée
        self.new_images.append(new_image)#on ajoute cette image modifiée à la liste des 9 images modifiées
    
    def andy_thread2(self):#fonction pour créer une image à la façon Andy Wahrol
        new_image = Image.new('RGB', (self.copy_img.width, self.copy_img.height), (0, 0, 0))#on crée une image de taille 3 fois plus petite pour optimiser
        filter = [random.randint(-255, 255) for i in range(3)]#on choisit pour chqaque composante de la couleur aléatoire à modifier
        for i in range(self.copy_img.width):#pour chaque pixel en longueur
            for j in range(self.copy_img.height):#pour chaque pixel en hauteur
                R, G, B= self.copy_img.getpixel((i, j))#on récupère les couleurs du pixel voulu
                gray = (R+G+B)//3 #on calcule le gris pour avoir un meilleur teint
                color = [gray, gray, gray]#on créer la liste color contenant les couleurs pour mettre le pixel avec le taux de gris voulu
                for l in range(3): #pour chaque l pour R, G et B
                    color[l] = color[l]+filter[l]#on ajoute la couleur de la composante aléatoire
                    if color[l]>255: #si la couleur dépasse 255
                        color[l] = 255+(255-color[l])#on la réduit pour ne pas avoir d'erreurs
                    elif color[l]<0:#si la couleur est inférieure à 0
                        color[l] = -color[l]#on inverse la composante pour avoir une valeur positive

                new_image.putpixel((i, j), (tuple(color)))#on met le pixel contenant la couleur modifiée
        self.new_images.append(new_image)#on ajoute cette image modifiée à la liste des 9 images modifiées
    
    def andy_it1(self):#fonction pour organiser les images façcon Andy Wahrol pour les images sans beacoup de contraste
        self.image = self.image.convert('RGB')#on convertit l'image en RGBA pour éviter les erreurs de formats
        self.new_images = []#création de la liste des images modifiées
        self.threads = []#liste contenant les threads
        self.copy_img = self.image.resize((self.image.width//3, self.image.height//3))#on définit une image modèle pour savoir les dimensions
        for k in range(9):#boucle for pour obtenir 9 images modifiées
            self.threads.append(threading.Thread(target=self.andy_thread1, name=k))#on lance un thread pour lancer les fonctions parrallèlement (ça ira plus vite)
            self.threads[k].start()#on démarre le thread
        for k in self.threads:#pour chaque thread
            k.join()#on attend que chaque thread soit fini
        self.big_img = Image.new('RGB', (self.copy_img.width *3, self.copy_img.height*3), (0, 0, 0))#on définit une image contenants les 9 images modifiées
        k = 0#on initialise une variable indiquant l'index dans la liste
        for i in range(0, self.image.width-self.copy_img.width+1, self.copy_img.width):#on fait une boucle de 3 positions x pour paste l'image
            for j in range(0, self.image.height-self.copy_img.height+1, self.copy_img.height):#on fait une boucle de 3 positions y pour paste l'image
                Image.Image.paste(self.big_img, self.new_images[k], (i, j))#on colle chaque petite image à sa position i et j
                k+=1#on incrémente l'index pour avoir le prochain élément dans la liste
        self.image = self.big_img#on définit l'image principale comme l'image finie
        self.show_img()#on affiche

    def andy_it2(self):#fonction pour organiser les images façcon Andy Wahrol pour les images avec du contraste
        self.image = self.image.convert('RGB')#on convertit l'image en RGBA pour éviter les erreurs de formats
        self.new_images = []#création de la liste des images modifiées
        self.threads = []#liste contenant les threads
        self.copy_img = self.image.resize((self.image.width//3, self.image.height//3))#on définit une image modèle pour savoir les dimensions
        for k in range(9):#boucle for pour obtenir 9 images modifiées
            self.threads.append(threading.Thread(target=self.andy_thread2, name=k))#on lance un thread pour lancer les fonctions parrallèlement (ça ira plus vite)
            self.threads[k].start()#on démarre le thread
        for k in self.threads:#pour chaque thread
            k.join()#on attend que chaque thread soit fini
        self.big_img = Image.new('RGB', (self.copy_img.width *3, self.copy_img.height*3), (0, 0, 0))#on définit une image contenants les 9 images modifiées
        k = 0#on initialise une variable indiquant l'index dans la liste
        for i in range(0, self.image.width-self.copy_img.width+1, self.copy_img.width):#on fait une boucle de 3 positions x pour paste l'image
            for j in range(0, self.image.height-self.copy_img.height+1, self.copy_img.height):#on fait une boucle de 3 positions y pour paste l'image
                Image.Image.paste(self.big_img, self.new_images[k], (i, j))#on colle chaque petite images à sa position i et j
                k+=1#on incrémente l'index pour avoir le prochain élément dans la liste
        self.image = self.big_img#on définit l'image principale comme l'image finie
        self.show_img()#on affiche
    
    def __run__(self):#fonction quand on veut éxecuter l'application
        self.root = tk.Tk()#création de la fenêtre
        self.root.geometry('1600x900')#on définit les dimensions de la fenêtre
        self.root.title('Py-Photo-Modifier')#on nomme la fenêtre

        self.header = tk.Menu(self.root)#on définit un bandeau contenant les menus
        self.root.config(menu=self.header)#on l'ajoute en haut

        self.file_menu = tk.Menu(self.header, tearoff=0)#on ajoute un menu tkinter
        self.edit_menu = tk.Menu(self.header, tearoff=0)#on ajoute un menu tkinter
        self.filter_menu = tk.Menu(self.header, tearoff=0)#on ajoute un menu tkinter
        self.convert_menu = tk.Menu(self.header, tearoff=0)#on ajoute un menu tkinter

        self.header.add_cascade(label='File', menu=self.file_menu)#on ajoute un menu File
        self.header.add_cascade(label='Edit', menu=self.edit_menu)#on ajoute un menu Edit
        self.header.add_cascade(label='Filter', menu=self.filter_menu)#on ajoute un menu Filter
        self.header.add_cascade(label='Convert', menu=self.convert_menu)#on ajoute un menu Convert

        self.file_menu.add_cascade(label='Open', command=self.open_file)#on ajoute le boutton Open au menu file
        self.file_menu.add_cascade(label='Save', command=self.save_file)#on ajoute le boutton Save
        self.file_menu.add_cascade(label='Paint', command=self.paint)#on ajoute le boutton Save
        self.file_menu.add_separator()#on ajoute un séparateur
        self.file_menu.add_cascade(label='Exit', command=self.root.quit)#on ajoute le boutton Exit

        self.edit_menu.add_cascade(label='Resize Image', command=self.resize)#on ajoute le boutton Resize image au menu Edit
        self.edit_menu.add_cascade(label='Change Resolution', command=self.change_res)#on ajoute le boutton Change Resolution
        self.edit_menu.add_separator()
        self.edit_menu.add_cascade(label='Flip Horizontaly', command=self.flip_0)#on ajoute le boutton Flip Ho...
        self.edit_menu.add_cascade(label='Flip Verticaly', command=self.flip_1)#on ajoute le boutton Flip Ver...
        self.edit_menu.add_cascade(label='Rotate', command=self.rotate)#on ajoute le boutton rotate

        self.filter_menu.add_cascade(label='Blur Function', command=self.blur) #on ajoute le boutton Blur Fonction au menu filter
        self.andy_menu = tk.Menu(self.filter_menu, tearoff=0)#on créer un menu pour choisir entre les deux fonctions andy wahrol 
        self.filter_menu.add_cascade(label='Andy Wahrol Functions', menu=self.andy_menu)#on affiche le menu
        self.andy_menu.add_cascade(label='Add Method Function', command=self.andy_it2) #on ajoute le boutton Andy Warhol pour la méthode add
        self.andy_menu.add_cascade(label='3 Division Method Function', command=self.andy_it1) #on ajoute le boutton Andy Warhol pour la méthode replace
        self.filter_menu.add_cascade(label='Change Saturation', command=self.change_sat) #on ajoute le boutton Change Saturation

        self.convert_menu.add_cascade(label='Convert to RGBA', command=self.convert_rgba)#on fait la meme chose pour le menu convert
        self.convert_menu.add_cascade(label='Convert to RGB', command=self.convert_rgb)
        self.convert_menu.add_cascade(label='Convert to Gray', command=self.convert_gray)

        self.image_label = tk.Label(self.root)#on définit un label qui contiendra plus tard une image
        self.image_label.grid()#on affiche le label

        
        self.root.mainloop()#cela répète les instructions dans __run__(self)



if __name__ == '__main__':#on regarde si le script n'est pas importé
    main = Application()#on définit main comme l'Apllication
    main.__run__()#on lance l'application
    
