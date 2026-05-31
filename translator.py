from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

translator = Translator()

# Create window
root = Tk()
root.title("AI Language Translator")
root.geometry("700x500")
root.config(bg="#f2f2f2")

# Function to translate text
def translate_text():
    try:
        source_lang = source_combo.get()
        target_lang = target_combo.get()
        text = input_text.get("1.0", END)

        if text.strip() == "":
            messagebox.showwarning("Warning", "Please enter text")
            return

        translated = translator.translate(text, src=source_lang, dest=target_lang)

        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Heading
heading = Label(root, text="AI Language Translation Tool", font=("Arial", 20, "bold"), bg="#f2f2f2")
heading.pack(pady=10)

# Input text
Label(root, text="Enter Text", font=("Arial", 12), bg="#f2f2f2").pack()
input_text = Text(root, height=8, width=70)
input_text.pack(pady=5)

# Language selection frame
frame = Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

languages = list(LANGUAGES.keys())

Label(frame, text="Source Language", bg="#f2f2f2").grid(row=0, column=0, padx=10)
source_combo = ttk.Combobox(frame, values=languages, width=20)
source_combo.set("en")
source_combo.grid(row=1, column=0)

Label(frame, text="Target Language", bg="#f2f2f2").grid(row=0, column=1, padx=10)
target_combo = ttk.Combobox(frame, values=languages, width=20)
target_combo.set("hi")
target_combo.grid(row=1, column=1)

# Translate button
translate_btn = Button(root, text="Translate", font=("Arial", 12, "bold"),
                       bg="#4CAF50", fg="white", command=translate_text)
translate_btn.pack(pady=10)

# Output text
Label(root, text="Translated Text", font=("Arial", 12), bg="#f2f2f2").pack()
output_text = Text(root, height=8, width=70)
output_text.pack(pady=5)

root.mainloop()
