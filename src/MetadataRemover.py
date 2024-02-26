import subprocess
import subprocess
import os
import shutil

def remove_metadata_and_move(file_path, destination_folder):
    try:
        subprocess.run(['exiftool', '-all=', '-overwrite_original', file_path], check=True, stdout=subprocess.PIPE)
        
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(destination_folder, file_name)
        
        shutil.move(file_path, new_file_path)
        print(f"Archivo movido a {new_file_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al eliminar metadatos: {e}")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

# Corrección: Uso de rutas como cadenas raw para evitar problemas con las secuencias de escape
source_folder = r'../Metadata_Remover/ToRemove'
destination_folder = r'../Metadata_Remover/Removed'

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)
    remove_metadata_and_move(file_path, destination_folder)
