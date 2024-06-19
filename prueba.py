import PyPDF2

opcion = 0
lista = []

print("**** Bienvenido al programa UNIONPDF ODT ***** \nseleccione una de las siguientes opciones:")
print('---------------------------------------------')
opcion = int(input("1. Agregar un archivo PDF \n2. Salir \n\n"))
while opcion == 1:
    print('---------------------------------------------')
    name_pdf = input("Ingrese el nombre del pdf con su extencion \n ejemplo(documento.pdf): \n\n")
    lista.append(name_pdf)
    print('---------------------------------------------')
    opcion = int(input("\n1. Agregar otro archivo PDF \n2. Generar archivo PDF \n\n"))
    print('---------------------------------------------')

merger = PyPDF2.PdfMerger()

for pdf in lista:
    merger.append(pdf)


name = input("\nIngrese el nombre del nuevo documento con su extencion.pdf: \n\n ")


with open(name, 'wb') as archivo_unido:
    merger.write(archivo_unido)

print('---------------------------------------------')    
print(f"Archivos PDF unidos exitosamente, su nuevo archivo es: {name}")
print('---------------------------------------------')
