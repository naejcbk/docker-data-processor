# Base slim con versión fija
FROM python:3.12.7-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar e instalar dependencias antes del código (aprovecha caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crear usuario sin privilegios y carpetas de trabajo
RUN useradd --create-home --shell /bin/bash appuser && \
    mkdir -p /app/data /app/output && \
    chown -R appuser:appuser /app

# Copiar el código fuente
COPY --chown=appuser:appuser src/ ./src/

# Ejecutar como usuario sin privilegios
USER appuser

# CMD en forma exec
CMD ["python", "src/process_data.py"]