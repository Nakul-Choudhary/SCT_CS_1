import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def on_encrypt():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        encrypted_text = encrypt(text, shift)
        result_var.set(encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def on_decrypt():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        decrypted_text = decrypt(text, shift)
        result_var.set(decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def on_clear():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result_var.set("")

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Result copied to clipboard.")

def create_gradient(canvas, width, height, color1, color2):
    """Create a vertical gradient from color1 to color2 on the given canvas."""
    limit = height
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)

    r_ratio = float(r2-r1) / limit
    g_ratio = float(g2-g1) / limit
    b_ratio = float(b2-b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)


root = tk.Tk()
root.title("Caesar Cipher")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


gradient_canvas = tk.Canvas(root, width=screen_width, height=screen_height)
gradient_canvas.pack(fill="both", expand=True)

create_gradient(gradient_canvas, screen_width, screen_height, "#003366", "#66ccff")


frame = tk.Frame(gradient_canvas, padx=20, pady=20, bg="#b3e0ff")  
frame.place(relx=0.5, rely=0.5, anchor="center")

message_label = tk.Label(frame, text="Enter your message:", bg="#99ccff", fg="#000000", font=("Arial", 14, "bold"))
message_label.grid(row=0, column=0, sticky="e")
message_entry = tk.Entry(frame, width=60, font=("Arial", 14))
message_entry.grid(row=0, column=1, pady=10)

shift_label = tk.Label(frame, text="Enter shift value:", bg="#99ccff", fg="#000000", font=("Arial", 14, "bold"))
shift_label.grid(row=1, column=0, sticky="e")
shift_entry = tk.Entry(frame, width=10, font=("Arial", 14))
shift_entry.grid(row=1, column=1, pady=10, sticky="w")


button_frame = tk.Frame(frame, bg="#b3e0ff")  
button_frame.grid(row=2, columnspan=2, pady=20)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=on_encrypt, bg="#80b3ff", fg="#000000", font=("Arial", 14, "bold"), padx=10, pady=5)
encrypt_button.pack(side=tk.LEFT, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=on_decrypt, bg="#80b3ff", fg="#000000", font=("Arial", 14, "bold"), padx=10, pady=5)
decrypt_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=on_clear, bg="#ffcc99", fg="#000000", font=("Arial", 14, "bold"), padx=10, pady=5)
clear_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copy", command=on_copy, bg="#ffcc99", fg="#000000", font=("Arial", 14, "bold"), padx=10, pady=5)
copy_button.pack(side=tk.LEFT, padx=10)


result_label = tk.Label(frame, text="Result:", bg="#99ccff", fg="#000000", font=("Arial", 14, "bold"))
result_label.grid(row=3, column=0, sticky="e")
result_var = tk.StringVar()
result_display = tk.Entry(frame, textvariable=result_var, relief="sunken", width=60, font=("Arial", 14), state='readonly')
result_display.grid(row=3, column=1, pady=10)


root.mainloop()

