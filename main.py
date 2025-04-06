# main.py

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from model_infer import generate_caption

class CaptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Captioning App")

        self.label = tk.Label(root, text="Upload an image to get caption", font=("Arial", 14))
        self.label.pack(pady=10)

        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.caption_text = tk.StringVar()
        self.caption_label = tk.Label(root, textvariable=self.caption_text, font=("Arial", 12), wraplength=500)
        self.caption_label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image, font=("Arial", 12))
        self.upload_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.display_image(file_path)
            caption = generate_caption(file_path)
            self.caption_text.set("Caption: " + caption)

    def display_image(self, path):
        img = Image.open(path)
        img = img.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        self.img_label.configure(image=photo)
        self.img_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionApp(root)
    root.mainloop()
