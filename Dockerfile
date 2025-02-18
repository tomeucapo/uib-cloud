# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Descarga el proyecto desde GitHub
RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/tomeucapo/.git . \
    && apt-get remove -y git \
    && apt-get autoremove -y
  
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "temp_mean.py"]