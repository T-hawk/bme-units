import re
from bme_units.number import *
import tkinter as tk

def convert(input_string, label_text):
    pattern = r"(\d+\.?\d*)\s*(\w+)\s*to\s*(\w+)"
    match = re.match(pattern, input_string)

    if match:
        number = float(match.group(1))
        from_unit = match.group(2)
        to_unit = match.group(3)

        orig_num = Number(number, from_unit)
        to_unit_num = Number(1, to_unit)
        new_num = orig_num.convert(to_unit_num)
        label_text.set(str(new_num.value) + " " + new_num.full_unit)

def key_pressed(event):
    if event.keysym == "Return":
        convert(input.get("1.0", tk.END).strip(), label_text)
        input.delete("1.0", tk.END)


def main():
    root = tk.Tk()

    root.geometry('350x120')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the window
    x = ((screen_width - root.winfo_width()) // 2) - root.winfo_width() // 2
    y = ((screen_height - root.winfo_height()) // 2) - root.winfo_height() // 2

    # Set window position
    root.geometry(f"+{x}+{y}")


    global input
    input = tk.Text(root,
                       height = 2,
                       width = 20)
    input.config(font=("Courier", 20))
    input.pack()

    global label_text
    label_text = tk.StringVar(value="")
    label = tk.Label(root, textvariable=label_text)
    label.config(font=("Courier", 20))
    label.pack()

    root.bind("<KeyRelease>", key_pressed)

    input.focus_set()

    root.mainloop()

if __name__ == "__main__":
    main()
