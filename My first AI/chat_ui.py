import tkinter as tk
from ai_core import chat

AI_NAME = "小智一号"

root = tk.Tk()
root.title("小智一号 🤖")
root.geometry("500x600")
root.configure(bg="#f5f5f5")


canvas = tk.Canvas(root, bg="#f5f5f5")
frame = tk.Frame(canvas, bg="#f5f5f5")
scrollbar = tk.Scrollbar(root, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.create_window((0,0), window=frame, anchor="nw")

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)


def add_message(text, is_user):

    bubble_frame = tk.Frame(frame, bg="#f5f5f5")

    if is_user:
        msg = tk.Label(
            bubble_frame,
            text=text,
            bg="#9fe8a6",
            fg="black",
            wraplength=300,
            padx=10,
            pady=5,
            justify="left"
        )
        msg.pack(anchor="e", padx=10, pady=5)
    else:
        msg = tk.Label(
            bubble_frame,
            text=text,
            bg="#ffffff",
            fg="black",
            wraplength=300,
            padx=10,
            pady=5,
            justify="left"
        )
        msg.pack(anchor="w", padx=10, pady=5)

    bubble_frame.pack(fill="both")

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)


def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    add_message(user_text, True)
    entry.delete(0, tk.END)

    reply = chat(user_text)
    add_message(reply, False)


entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind("<Return>", lambda event: send_message())


btn = tk.Button(root, text="发送", command=send_message)
btn.pack(pady=5)

root.mainloop()