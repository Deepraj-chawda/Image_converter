import tkinter as tk
from PIL import Image, ImageTk


'''
Guys the code below is working well but it is not Object Oriented, and 
Buttons also do not contain commands.


But The layout is good, we just need it to be object oriented and have 
some style too.
'''

# Creating Master
root = tk.Tk()

# Defining size for the window
size = (1250, 515) # do not change this values as they are static
root.geometry(f'{size[0]}x{size[1]}')


# some constant static variables
top_labels_height = 25     # Top Label Height
button_height = 5          # button height
image_frames_height = 400  # image frame height

# setting an example file (.anyImage file)
file_path = "test_images//car.jpg"


top_labels = tk.LabelFrame(root, width = size[0],
 height = top_labels_height).grid(row = 0, column = 0, columnspan = 2)

tk.Label(top_labels, text = "Original Image").grid(row = 0, column = 0)
tk.Label(top_labels, text = "Puzzled Image").grid(row = 0, column = 1)



image_frames = [
		tk.LabelFrame(root, width = size[0]//2,
		 height = image_frames_height).grid(row = 1, column = 0),
		tk.LabelFrame(root, width = size[0]//2,
		 height = image_frames_height).grid(row = 1, column = 1),
	]



images = [
		tk.Label(image_frames[0],),
		tk.Label(image_frames[1],),
	]

# Please do correct ----------------------------------------------------
# def load_image(path):
# 	global images
# 	img = ImageTk.PhotoImage(Image.open(path).resize((size[0]//2,
 # image_frames_height), Image.ANTIALIAS))
# 	images[0].config(image = img)


# def generate_image(path):
# 	global images
# 	img = ImageTk.PhotoImage(Image.open(path).resize((size[0]//2,
 # image_frames_height), Image.ANTIALIAS))
# 	images[1].config(image = img)
# -------------------------------------------------------------------------------------------------------

# Loading Image
img = ImageTk.PhotoImage(Image.open(file_path).resize((size[0]//2,
 image_frames_height), Image.ANTIALIAS))

tk.Button(root, text = "Load Image", width = 88,
 height = button_height).grid(row = 2, column = 0),
tk.Button(root, text = "Generate Image", width = 88,
 height = button_height).grid(row = 2, column = 1)

images[0].grid(row = 1, column = 0)
images[1].grid(row = 1, column = 1)

images[0].config(image = img)
images[1].config(image = img)

root.mainloop()

# I tried It with OOP but there is some issue ----------------------------
# class App(tk.Tk):
# 	def __init__(self, *, title = "Puzzle Generator", size = (850, 450)):
# 		super().__init__()
# 		self.title(title)
# 		self.size = size
# 		self.geometry(f'{self.size[0]}x{self.size[1]}')
		
# 	def set_widgets(self):
# 		top_labels = tk.LabelFrame(self, width = self.size[0], height = 25).grid(row = 0, column = 0, columnspan = 2)
# 		tk.Label(top_labels, text = "Original Image").grid(row = 0, column = 0)
# 		tk.Label(top_labels, text = "Puzzled Image").grid(row = 0, column = 1)

# 		image_frames = [
# 			tk.LabelFrame(self, width = self.size[0]//2, height = 400).grid(row = 1, column = 0),
# 			tk.LabelFrame(self, width = self.size[0]//2, height = 400).grid(row = 1, column = 1),
# 		]

# 		file_path = "E://Desktop Files//Car.jpg"
# 		img = Image.open(file_path).resize((self.size[0]//2, 400), Image.ANTIALIAS)
# 		img = ImageTk.PhotoImage(img)


# 		self.images = [
# 			tk.Label(image_frames[0], image = img),
# 			tk.Label(image_frames[1], image = img),
# 		]

# 		tk.Button(self, text = "Load Image").grid(row = 2, column = 0),
# 		tk.Button(self, text = "Generate Image").grid(row = 2, column = 1)
		
# 		self.images[0].grid(row = 1, column = 0)
# 		self.images[1].grid(row = 1, column = 1)


# app = App()
# app.set_widgets()
# app.mainloop()

# -------------------------------------------------------------------------