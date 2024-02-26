# Metadata_Remover
Nuevo proyecto esta vez usamos exiftool para borrar metadatos de archivos e intentar sobreescribir informacion para evitar ciberataques

IMPORTANTE: Esta version solo sirve para editar archivos de video.

# Pasos para el funcionamiento del codigo

Descarga ExifTool:

Ve al sitio web oficial de ExifTool (https://exiftool.org/) y descarga la versión de Windows. Usualmente se descarga como un archivo ZIP.
Extrae el Archivo:

Extrae el contenido del archivo ZIP. Obtendrás un archivo .exe llamado exiftool(-k).exe.
Renombra ExifTool (Opcional):

Para facilitar su uso desde la línea de comandos, puedes renombrar el archivo exiftool(-k).exe a exiftool.exe

Mueve el archivo exiftool.exe a una ubicación permanente en tu sistema, como por ejemplo C:\ExifTool. Si no existe la carpeta créala.
Añade la Carpeta al PATH:

Ahora, debes añadir la carpeta donde colocaste exiftool.exe al PATH del sistema. Sigue estos pasos:
Presiona la tecla Windows y busca "Editar las variables de entorno del sistema".
En la ventana de Propiedades del Sistema, haz clic en el botón "Variables de Entorno...".
En la sección "Variables del sistema", busca y selecciona la variable Path, luego haz clic en "Editar...".
En la ventana de edición, haz clic en "Nuevo" y pega la ruta de la carpeta donde guardaste exiftool.exe (por ejemplo, C:\ExifTool).
Haz clic en "Aceptar" para cerrar la ventana de edición, luego nuevamente en "Aceptar" para cerrar las Variables de Entorno, y una vez más en "Aceptar" para cerrar las Propiedades del Sistema.

Para verificar que ExifTool ha sido correctamente añadido al PATH, abre una nueva ventana de la línea de comandos (cmd) o PowerShell y escribe exiftool. Si has seguido los pasos, deberías ver la versión de ExifTool aparecer en la consola.