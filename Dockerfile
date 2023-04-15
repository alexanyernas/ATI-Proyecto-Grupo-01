# Usar la imagen oficial de Python
FROM python:3.9

# Definir el directorio de trabajo
WORKDIR /myWorkDir

# Copiar los archivos de la aplicación
COPY requirements.txt .
COPY /src /myWorkDir/src

# Instalar las dependencias
RUN pip install -r requirements.txt

# Ejecutar la aplicación
CMD ["python", "/myWorkDir/src/app.py"]