import tkinter as tk
def send_message():
    message = entry.get()
    if message:
        chat_display.config(state='normal')
        chat_display.insert(tk.END, "You: " + message + "\n")
        chat_display.config(state='disabled')
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Interface")

chat_display = tk.Text(root, state='disabled', height=15, width=40)
chat_display.pack(padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()