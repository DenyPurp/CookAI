@echo off
chcp 65001 >nul
title Запуск CookAI

echo [1/3] Запуск базы данных (Ubuntu + Docker)...
start "CookAI - DB" powershell -NoExit -Command "wsl -d Ubuntu -e bash -c \"dockerd > /tmp/dockerd.log 2>&1 & cd '/mnt/w/4 kurs/Main_project' && docker-compose up -d && echo 'База данных запущена' && exec bash\""

timeout /t 4 /nobreak >nul

echo [2/3] Запуск бэкенда (Django)...
start "CookAI - Backend" cmd /k "cd /d W:\4 kurs\Main_project\backend && .\venv\Scripts\activate && python manage.py runserver"

timeout /t 2 /nobreak >nul

echo [3/3] Запуск фронтенда (React)...
start "CookAI - Frontend" cmd /k "cd /d W:\4 kurs\Main_project\frontend && npm run dev"

echo.
echo Все сервисы запущены!
pause