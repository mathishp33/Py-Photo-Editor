import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageDraw



class Paint():
    def __init__(self):
        self.shape = 'rectangle'
        self.tool = 'pencil'
        self.color = 'black'
        self.size = 1
        self.image = Image.new('RGBA', (1600, 900),(255, 255, 240))
        self.draw = ImageDraw.Draw(self.image)
        self.pos1 = (0, 0)
        self.pos2 = (0, 0)
        self.release = True

    def switch_pencil(self): self.tool = 'pencil'
    def switch_rect(self): self.tool = 'rect'
    def switch_circle(self): self.tool = 'circle'
    
    def red(self): self.color = 'red'
    def green(self): self.color = 'green'
    def yellow(self): self.color = 'yellow'
    def orange(self): self.color = 'orange'
    def white(self): self.color = 'white'
    def black(self): self.color = 'black'
    def blue(self): self.color = 'blue'
    def purple(self): self.color = 'purple'

    def select_size(self):
        self.size = self.selected_size.get()
        self.new_root.destroy()

    def size_(self):
        self.selected_size = tk.IntVar()
        self.new_root = tk.Tk()
        self.new_root.geometry('300x300+700+400')
        self.size_slider = tk.Scale(self.new_root, orient='horizontal', variable=self.selected_size, from_=1, to=100, resolution=1, length=200)
        self.submit_size = tk.Button(self.new_root, text='Submit Width', command=self.select_size)
        self.size_slider.grid()
        self.submit_size.grid()
        
    def open_file(self):
        self.file = askopenfile()#on ouvre une fenetre permettant de charger l'image
        self.file = self.file.name#on récupère le PATH 

    def save_file(self):
        self.file = asksaveasfile()
        self.file = self.file.name
        self.extension = [self.file[-i] if not self.file[-i] == '.' else '' for i in range (1, 4, 1)]
        self.extension.reverse()
        self.extension = ''.join(self.extension)
        self.image.save(self.file, self.extension)
        print('saved image at', self.file, ' , ', self.extension)
    
    def mouse_click(self, mouse):
        self.lastx, self.lasty = mouse.x, mouse.y
        if self.pos1 == (0, 0) and self.release:
            self.pos1 = (mouse.x, mouse.y)
        else:
            self.pos2 = (mouse.x, mouse.y)
        self.release = False
    
    def mouse_moving(self, mouse):
        if self.tool == 'pencil': 
            self.draw.line(xy=(self.lastx, self.lasty, mouse.x, mouse.y), fill=self.color, width=self.size)
            self.canvas.create_line(self.lastx, self.lasty, mouse.x, mouse.y, fill=self.color, width=self.size)
        self.mouse_click(mouse)
    
    def release_(self, mouse):
        self.release = True
        if self.tool == 'rect':
            if not self.pos1 == (0, 0):
                self.draw.rectangle([self.pos1, self.pos2], fill=self.color if self.fill.get() else 'white', outline='black', width=self.size)
                self.canvas.create_rectangle(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1], fill=self.color if self.fill.get() else '')
                self.pos1 = self.pos2 = (0, 0)
        if self.tool == 'circle':
            if not self.pos1 == (0, 0):
                self.draw.ellipse(xy=(self.pos1, self.pos2), fill=self.color if self.fill.get() else 'white', outline='black', width=self.size)
                self.canvas.create_oval(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1], fill=self.color if self.fill.get() else '')
                self.pos1 = self.pos2 = (0, 0)
    
    def __run__(self):
        self.root = tk.Tk()
        self.root.geometry('1600x900')
        self.root.title('Py-Paint')
        
        self.fill = tk.IntVar()

        self.header = tk.Menu(self.root)
        self.root.config(menu=self.header)
        self.canvas = tk.Canvas(self.root, width=1600, height=900, background='ivory')
        self.canvas.pack()

        self.file_menu = tk.Menu(self.header, tearoff=0)
        self.tools_menu = tk.Menu(self.header, tearoff=0)
        self.color_menu = tk.Menu(self.header, tearoff=0)
        self.size_menu = tk.Menu(self.header, tearoff=0)

        self.header.add_cascade(label='File', menu=self.file_menu)
        self.header.add_cascade(label='Tools', menu=self.tools_menu)
        self.header.add_cascade(label='Color', menu=self.color_menu)
        self.header.add_cascade(label='Size', menu=self.size_menu)

        self.file_menu.add_cascade(label='Open', command=self.open_file)#on ajoute le boutton Open au menu file
        self.file_menu.add_cascade(label='Save', command=self.save_file)#on ajoute le boutton Save
        self.file_menu.add_separator()#on ajoute un séparateur
        self.file_menu.add_cascade(label='Exit', command=self.root.quit)#on ajoute le boutton Exit

        self.tools_menu.add_cascade(label='Pencil', command=self.switch_pencil)
        self.tools_menu.add_cascade(label='Rectangle', command=self.switch_rect)
        self.tools_menu.add_cascade(label='Circle', command=self.switch_circle)

        self.color_changer = tk.Menu(self.color_menu, tearoff=0)
        self.color_menu.add_checkbutton(label='Fill shapes', variable=self.fill)
        self.color_menu.add_cascade(label='Change Color', menu=self.color_changer)
        self.color_changer.add_cascade(label='Red', command=self.red)
        self.color_changer.add_cascade(label='Green', command=self.green)
        self.color_changer.add_cascade(label='Yellow', command=self.yellow)
        self.color_changer.add_cascade(label='Orange', command=self.orange)
        self.color_changer.add_cascade(label='White', command=self.white)
        self.color_changer.add_cascade(label='Black', command=self.black)
        self.color_changer.add_cascade(label='Blue', command=self.blue)
        self.color_changer.add_cascade(label='Purple', command=self.purple)


        self.size_menu.add_cascade(label='Change Width', command=self.size_)

        self.root.bind('<ButtonRelease-1>', self.release_)
        self.root.bind('<Button-1>', self.mouse_click)
        self.root.bind("<B1-Motion>", self.mouse_moving)
        self.root.mainloop()

if __name__ == '__main__':
    main = Paint()
    main.__run__()
