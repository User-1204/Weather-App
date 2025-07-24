import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# Create gradient background
def create_gradient(w, h, c1, c2):
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    for y in range(h):
        ImageDraw.Draw(mask).line([(0, y), (w, y)], fill=int(255 * y / h))
    return ImageTk.PhotoImage(Image.composite(top, base, mask))

# Build GUI and return widgets
def build_gui(callbacks):
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("420x700")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=420, height=700)
    canvas.pack(fill="both", expand=True)
    bg = create_gradient(420, 700, "#7F2929", "#7F2929")
    canvas.create_image(0, 0, anchor="nw", image=bg)

    container = tk.Frame(canvas, bg="#7F2929")
    canvas.create_window((0, 0), window=container, anchor="nw", width=420, height=700)

    tk.Label(container, text="Weather App", font=("Helvetica", 20, "bold"), bg="#7F2929", fg="#E06363").pack(pady=(20,10))

    city_entry = tk.Entry(container, font=("Helvetica", 13), justify="center", width=30, bd=2, relief="groove")
    city_entry.pack(pady=10)
    city_entry.bind("<Return>", lambda e: callbacks['get_weather']())  # pressing Enter shows weather

    btn_style = dict(font=("Helvetica", 11), bg="#D96459", fg="white", activebackground="#b9584b", relief="flat", width=20)
    tk.Button(container, text="Get Weather", command=callbacks['get_weather'], **btn_style).pack(pady=5)
    tk.Button(container, text="Toggle °C/°F", command=callbacks['toggle_unit'], **btn_style).pack(pady=5)
    tk.Button(container, text="Detect Location", command=callbacks['detect_location'], **btn_style).pack(pady=5)

    icon_label = tk.Label(container, bg="#7F2929")
    icon_label.pack(pady=10)

    result_label = tk.Label(container, text="", font=("Helvetica", 12), bg="#7F2929", justify="center")
    result_label.pack(pady=5)

    hourly_label = tk.Label(container, text="", font=("Helvetica", 11), bg="#7F2929", justify="left", fg="#FFFFFF")
    hourly_label.pack(pady=(10, 5))

    daily_label = tk.Label(container, text="", font=("Helvetica", 11), bg="#7F2929", justify="left", fg="#FFFFFF")
    daily_label.pack(pady=5)

    tk.Frame(container, height=2, bd=1, relief="sunken", bg="#7F2929").pack(fill="x", padx=20, pady=15)
    tk.Label(container, text="Made by Sakshi | 2025", font=("Helvetica", 9, "italic"), bg="#7F2929", fg="#D7CBCB").pack(side="bottom", pady=10)

    root.bg = bg
    return city_entry, result_label, icon_label, hourly_label, daily_label, root
