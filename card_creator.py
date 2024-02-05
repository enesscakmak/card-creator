import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageFont
import random


def generate_card():
    # Get values from entries
    str_value = strEntry.get()
    dex_value = dexEntry.get()
    con_value = conEntry.get()
    int_value = intEntry.get()
    wis_value = wisEntry.get()
    cha_value = chaEntry.get()
    hp_value = hpEntry.get()
    armor_value = armorEntry.get()

    # Create a new image
    card_image = Image.new("RGB", (325, 650), "#e0516e")
    draw = ImageDraw.Draw(card_image)

    # Set font and size
    font = ImageFont.truetype("arial.ttf", 20)

    # Draw text on the image
    draw.text((10, 10), nameEntry.get().upper(), font=ImageFont.truetype("arial.ttf", 25), fill="black")
    draw.text((255, 50), f"Tier: {tierEntry.get()}", font=font, fill="black")
    draw.text((40, 500), f"STR: {str_value}", font=font, fill="black")
    draw.text((40, 540), f"DEX: {dex_value}", font=font, fill="black")
    draw.text((40, 580), f"CON: {con_value}", font=font, fill="black")
    draw.text((200, 500), f"INT: {int_value}", font=font, fill="black")
    draw.text((200, 540), f"WIS: {wis_value}", font=font, fill="black")
    draw.text((200, 580), f"CHA: {cha_value}", font=font, fill="black")
    draw.text((40, 620), f"Health: {hp_value}", font=font, fill="black")
    draw.text((200, 620), f"Armor: {armor_value}", font=font, fill="black")

    # Draw the uploaded image with specified size and position
    if uploaded_image_path:
        uploaded_image = Image.open(uploaded_image_path)
        uploaded_image = uploaded_image.resize((300, 400))  # Set the size
        card_image.paste(uploaded_image, (13, 90))  # Set the position

    # Save the image
    card_image.save(f"generated_card{random.randint(0,10000000)}.png")


def upload_image():
    global uploaded_image_path
    uploaded_image_path = filedialog.askopenfilename()
    # You can add code to display or process the uploaded image if needed


root = tk.Tk()
root.title("Card Creator")
root.geometry("485x300")

# Widget style
style = ttk.Style()
style.configure("TLabel", font="helvetica 11", padding=5)
style.configure("TButton", font="helvetica 11", padding=5, width=20)
style.configure("TEntry", font="helvetica 11", padding=5, width=20)

# Labels
ttk.Label(text="Name").grid(row=0, column=0)
ttk.Label(text="Tier").grid(row=0, column=2, pady=20)
ttk.Label(text="STR").grid(row=1, column=0)
ttk.Label(text="DEX").grid(row=2, column=0)
ttk.Label(text="CON").grid(row=3, column=0)
ttk.Label(text="INT").grid(row=1, column=2)
ttk.Label(text="WIS").grid(row=2, column=2)
ttk.Label(text="CHA").grid(row=3, column=2)
ttk.Label(text="HP").grid(row=6, column=0)
ttk.Label(text="Armor").grid(row=6, column=2)

# Entries
nameEntry = ttk.Entry()
nameEntry.grid(row=0, column=1)
tierEntry = ttk.Entry()
tierEntry.grid(row=0, column=3)
strEntry = ttk.Entry()
strEntry.grid(row=1, column=1)
dexEntry = ttk.Entry()
dexEntry.grid(row=2, column=1)
conEntry = ttk.Entry()
conEntry.grid(row=3, column=1)
intEntry = ttk.Entry()
intEntry.grid(row=1, column=3)
wisEntry = ttk.Entry()
wisEntry.grid(row=2, column=3)
chaEntry = ttk.Entry()
chaEntry.grid(row=3, column=3)
hpEntry = ttk.Entry()
hpEntry.grid(row=6, column=1)
armorEntry = ttk.Entry()
armorEntry.grid(row=6, column=3)

# Buttons
ttk.Button(text="Upload Image", command=upload_image).grid(row=8, column=1, columnspan=1, pady=10)
ttk.Button(text="Generate", command=generate_card).grid(row=8, column=3, columnspan=1)

uploaded_image_path = None

root.mainloop()
