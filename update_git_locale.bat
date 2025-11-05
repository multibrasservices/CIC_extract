@echo off
set /p message="Entrez le message de commit : "
git add .
git commit -m "%message%"
pause