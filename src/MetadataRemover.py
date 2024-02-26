import datetime
import random
import subprocess
import os
import shutil

def generate_random_datetime_within_months(months=4, start_hour=9, end_hour=21):
    end_date = datetime.datetime.now()  # Corregido aquí
    start_date = end_date - datetime.timedelta(days=months*30)
    random_days = random.randrange((end_date - start_date).days)
    random_date = start_date + datetime.timedelta(days=random_days)
    
    random_hour = random.randint(start_hour, end_hour - 1)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    # Combinar fecha aleatoria con hora aleatoria
    return datetime.datetime.combine(random_date.date(), datetime.time(random_hour, random_minute, random_second))  # Corregido aquí

def remove_all_metadata_and_set_random_dates(file_path, destination_folder):
    # Genera una fecha y hora aleatoria para aplicar a todos los metadatos de fecha/hora
    random_datetime = generate_random_datetime_within_months()
    formatted_datetime = random_datetime.strftime('%Y:%m:%d %H:%M:%S')
    
    try:
        commands = [
            '-all=',  # Borra todos los metadatos
            '-FileModifyDate=' + formatted_datetime,
            '-FileAccessDate=' + formatted_datetime,
            '-FileCreateDate=' + formatted_datetime,
            '-CreateDate=' + formatted_datetime,
            '-ModifyDate=' + formatted_datetime,
            '-TrackCreateDate=' + formatted_datetime,
            '-TrackModifyDate=' + formatted_datetime,
            '-MediaCreateDate=' + formatted_datetime,
            '-MediaModifyDate=' + formatted_datetime,
            '-overwrite_original'
        ]
        
        subprocess.run(['exiftool', *commands, file_path], check=True, stdout=subprocess.PIPE)
        
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, new_file_path)
        print(f"Metadatos borrados y actualizados, archivo movido a {new_file_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error al modificar metadatos: {e}")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

source_folder = r'../Metadata_Remover/ToRemove'
destination_folder = r'../Metadata_Remover/Removed'

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)
    remove_all_metadata_and_set_random_dates(file_path, destination_folder)
