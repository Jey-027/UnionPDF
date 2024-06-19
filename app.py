import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

def unir_pdfs():
    # Obtener la lista de archivos PDF
    archivos = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    
    if not archivos:
        return
    
    # Crear un objeto PdfMerger
    merger = PyPDF2.PdfMerger()
    
    for pdf in archivos:
        merger.append(pdf)
    
    # Guardar el archivo PDF unido
    archivo_guardado = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
    if archivo_guardado:
        with open(archivo_guardado, 'wb') as archivo_unido:
            merger.write(archivo_unido)
        messagebox.showinfo("Éxito", f"Archivos PDF unidos exitosamente en '{archivo_guardado}'")

# Crear la ventana principal
root = tk.Tk()
root.title("Unir PDFs")

# Crear el botón para unir PDFs
boton_unir = tk.Button(root, text="Unir PDFs", command=unir_pdfs)
boton_unir.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
