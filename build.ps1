# .\venv\Scripts\Activate.ps1 
# pip install --upgrade pip
# pip install -r requirements.txt
# rm -rf public
# reflex init
# reflex export --frontend-only
# Expand-Archive -Path frontend.zip -DestinationPath public
# rm -f frontend.zip
# deactivate

# Actualizar dependencias
python -m pip install --upgrade pip
pip install -r requirements.txt

# Limpiar carpeta pública
if (Test-Path public) { Remove-Item -Recurse -Force public }

# Exportar Reflex
reflex init
reflex export --frontend-only

# Extraer y limpiar
if (Test-Path frontend.zip) {
    Expand-Archive -Path frontend.zip -DestinationPath public
    Remove-Item -Force frontend.zip
}