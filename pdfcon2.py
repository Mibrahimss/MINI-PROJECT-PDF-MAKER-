import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image
from fpdf import FPDF
import os

class PDFMaker:
    def __init__(self, win):
        self.win = win
        self.win.title("PDF Maker - Text & Image to PDF")
        self.win.geometry("700x500")
        self.win.configure(bg="#1e1e1e")

        tk.Label(win, text="Text to PDF", font=("Arial", 14), bg="#1e1e1e", fg="white").pack(pady=10)
        self.text_area = scrolledtext.ScrolledText(win, width=70, height=10, font=("Arial", 12), bg="#2b2b2b", fg="white")
        self.text_area.pack(pady=10)

        tk.Button(win, text="Convert Text to PDF", command=self.text_to_pdf, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(win, text="Convert Image to PDF", command=self.image_to_pdf, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=10)

    def text_to_pdf(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Text area is empty.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filepath:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for line in text.split('\n'):
                pdf.multi_cell(0, 10, line)
            pdf.output(filepath)
            messagebox.showinfo("Success", f"PDF saved as:\n{filepath}")

    def image_to_pdf(self):
        files = filedialog.askopenfilenames(title="Select Image(s)", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not files:
            return
        
        images = []
        for file in files:
            img = Image.open(file).convert("RGB")
            images.append(img)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            if len(images) == 1:
                images[0].save(save_path)
            else:
                images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", f"Image(s) saved to PDF:\n{save_path}")

# Run the app
if __name__ == "__main__":
    win = tk.Tk()
    app = PDFMaker(win)
    win.mainloop()