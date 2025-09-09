@echo off

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
