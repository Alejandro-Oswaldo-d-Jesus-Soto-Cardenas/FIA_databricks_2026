volume_path = "/Volumes/fia_databricks/datos/fia_volume/datos_prueba.txt"

print("Ruta del archivo:")
print(volume_path)

print("\nContenido del archivo:")
print(dbutils.fs.head(volume_path))