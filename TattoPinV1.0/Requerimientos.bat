@echo off
:: Habilitar colores
color 0A

:: Configuración inicial
echo.
echo ################################################################################
echo       CONFIGURANDO EL ENTORNO PARA DJANGO
echo ################################################################################
echo.

:: Verifica si Python está instalado
echo =========================================
echo          VERIFICANDO PYTHON 
echo --..,_                       _,.--.
echo       `'.'.                .'`__ o  `;__.   
echo          '.'.            .'.'`  '---'`  `
echo            '.`'--....--'`.'
echo              `'--....--'`
echo =========================================
echo.
winget install python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado. Por favor, instálalo antes de continuar.
    pause
    exit /b
)

color 0B
:: Actualizar pip
echo.
echo ================================================================================
echo        ACTUALIZANDO PIP
echo ================================================================================
echo.
python -m pip install --upgrade pip

:: Instalar dependencias
echo.
echo ================================================================================
echo    INSTALANDO/ACTUALIZANDO DEPENDENCIAS
echo ================================================================================
echo.
pip install django
pip install pillow
pip install djangorestframework
pip install django-crispy-forms
pip install crispy

:: Migraciones de la base de datos
echo.
echo ========================================
echo       REALIZANDO MIGRACIONES
echo ========================================
echo.
python manage.py makemigrations
python manage.py migrate

:: Crear un superusuario
echo.
echo ========================================
echo         CREAR SUPERUSUARIO
echo ========================================
echo.
set /p create_superuser="¿Quieres crear un superusuario? (s/n): "
if /i "%create_superuser%"=="s" (
    python manage.py createsuperuser
)


:: Iniciar el servidor
echo.
echo ========================================
echo         INICIANDO EL SERVIDOR
echo ========================================
echo.
start http://127.0.0.1:8000
python manage.py runserver


:: Pausar para mantener la consola abierta
echo.
echo ========================================
echo           FINALIZADO
echo ========================================
pause
