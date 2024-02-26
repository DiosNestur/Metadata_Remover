import subprocess
import os
import shutil
from datetime import datetime, timedelta
import random

# Función para generar una fecha aleatoria dentro de un rango no menos de 4 meses de la fecha actual
def generate_random_date_within_months(months=4):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months*30) 
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y:%m:%d %H:%M:%S') 

def remove_metadata_and_set_random_dates(file_path, destination_folder):
    try:
        # Primero, eliminar todos los metadatos
        subprocess.run(['exiftool', '-all=', '-overwrite_original', file_path], check=True, stdout=subprocess.PIPE)

        # Luego, genera y establece fechas aleatorias para cada campo de metadato
        commands = [
            '-FileModifyDate=' + generate_random_date_within_months(),
            '-FileAccessDate=' + generate_random_date_within_months(),
            '-FileCreateDate=' + generate_random_date_within_months(),
            '-CreateDate=' + generate_random_date_within_months(),
            '-ModifyDate=' + generate_random_date_within_months(),
            '-TrackCreateDate=' + generate_random_date_within_months(),
            '-TrackModifyDate=' + generate_random_date_within_months(),
            '-MediaCreateDate=' + generate_random_date_within_months(),
            '-MediaModifyDate=' + generate_random_date_within_months(),
            '-overwrite_original'
        ]
        
        # Ejecuta ExifTool nuevamente con los comandos para actualizar las fechas
        subprocess.run(['exiftool', *commands, file_path], check=True, stdout=subprocess.PIPE)
        
        # Mueve el archivo a la carpeta de destino
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, new_file_path)
        print(f"Metadatos eliminados, fechas actualizadas y archivo movido a {new_file_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error al modificar metadatos: {e}")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

source_folder = r'../Metadata_Remover/ToRemove'
destination_folder = r'../Metadata_Remover/Removed'

# Procesa cada archivo en la carpeta de origen
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)
    remove_metadata_and_set_random_dates(file_path, destination_folder)
