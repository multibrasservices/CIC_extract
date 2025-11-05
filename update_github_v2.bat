@echo off
rem Script robuste pour automatiser les commandes git add, commit, et push

echo.
echo =================================================
echo    Assistant de Commit et Push pour GitHub
echo =================================================
echo.

rem Récupère le nom de la branche actuelle
for /f %%i in ('git branch --show-current') do set current_branch=%%i

rem Vérifie si nous sommes bien sur une branche
if not defined current_branch (
    echo.
    echo ERREUR : Impossible de déterminer la branche actuelle.
    echo Etes-vous dans un dépôt Git ? Avez-vous des commits ?
    echo Annulation de l'opération.
    goto end
)

echo --- Branche actuelle : %current_branch% ---
echo.

rem Ajoute tous les changements au staging
echo --- Ajout de tous les fichiers en cours... ---
git add .
echo.

rem Demande à l'utilisateur d'entrer un message de commit
set /p commit_message="Entrez le message de commit : "

rem Vérifie si le message est vide
if "%commit_message%"=="" (
    echo.
    echo ERREUR : Le message de commit ne peut pas être vide.
    echo Annulation de l'opération.
    goto end
)

rem Exécute le commit
echo.
echo --- Commit en cours... ---
git commit -m "%commit_message%"
echo.

rem Pousse les changements vers la branche actuelle sur le dépôt distant
echo --- Push vers origin %current_branch%... ---
git push origin %current_branch%
echo.

:end
echo =================================================
echo                 OPERATION TERMINEE
echo =================================================
echo.
pause