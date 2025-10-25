import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("dark")   # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Main window
app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("320x480")

# Entry display
entry = ctk.CTkEntry(app, width=280, height=60, font=("Arial", 24), justify="right")
entry.place(x=20, y=30)

# Function to handle button clicks
def button_click(value):
    if value == "C":
        entry.delete(0, "end")
    elif value == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    else:
        entry.insert("end", value)

# Button layout
buttons = [
    ("7", 20, 120), ("8", 100, 120), ("9", 180, 120), ("/", 260, 120),
    ("4", 20, 200), ("5", 100, 200), ("6", 180, 200), ("*", 260, 200),
    ("1", 20, 280), ("2", 100, 280), ("3", 180, 280), ("-", 260, 280),
    ("0", 20, 360), (".", 100, 360), ("=", 180, 360), ("+", 260, 360),
    ("C", 20, 440)
]

# Create buttons
for (text, x, y) in buttons:
    btn = ctk.CTkButton(
        app,
        text=text,
        width=60,
        height=60,
        corner_radius=20,
        font=("Arial", 20),
        command=lambda t=text: button_click(t)
    )
    btn.place(x=x, y=y)

app.mainloop()
