import PyPDF2

#Lista de los archivos pdf
pdfs = ['pdf_1.pdf', 'pdf_2.pdf']

# Crear un objeto Pdflinemerger
merger = PyPDF2.PdfMerger()

# Agregar cada archivo 
for pdf in pdfs:
    merger.append(pdf)

# Escribir el archivo pdf unido a uno nuevo pdf
with open('archivo_unido.pdf', 'wb') as archivo_unido:
    merger.write(archivo_unido)

print("Archivos PDF unidos exitosamente en 'archivo_unido.pdf'")

