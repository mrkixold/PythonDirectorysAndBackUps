import directory

print("")
print("")
source_path = input("Introduce la ruta de la carpeta a copiar: ")
destination_path = input("Introduce la unidad de destino: ")
print("")
print("")

folder = directory.Directory(source_path)

print("")
print("")
print("Creating a zip from the file...")

folder.GenerateZipFile(destination_path)