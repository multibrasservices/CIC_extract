# Extracteur de Relevés Bancaires CIC

Cette application Streamlit permet d'extraire les transactions de relevés bancaires PDF de la banque CIC et de les exporter dans un fichier Excel propre et formaté.

## Fonctionnalités

- **Téléversement multiple** : Chargez un ou plusieurs fichiers PDF de relevés bancaires.
- **Extraction de données** : Analyse les tables dans les PDF pour extraire la date, le libellé, et les montants des transactions.
- **Traitement des données** : Convertit les débits en nombres négatifs et les crédits en nombres positifs.
- **Visualisation** : Affiche les données extraites dans un tableau clair et trié par date.
- **Export Excel** : Téléchargez toutes les transactions consolidées dans un unique fichier `.xlsx`.
- **Mise en forme Excel** : Le fichier exporté a des largeurs de colonnes auto-ajustées et un format monétaire pour les débits/crédits.

## Installation et Lancement

1.  **Clonez le projet ou téléchargez les fichiers.**

2.  **Installez les dépendances** :
    Assurez-vous d'avoir Python 3.8+ installé. Ouvrez un terminal dans le dossier du projet et exécutez :
    ```bash
    pip install -r requirements.txt
    ```

3.  **Lancez l'application** :
    Toujours dans le même dossier, exécutez :
    ```bash
    streamlit run app.py
    ```

L'application devrait s'ouvrir dans votre navigateur web.

## Fichiers du projet

- `app.py`: Le code source principal de l'application Streamlit.
- `requirements.txt`: La liste des dépendances Python.
- `README.md`: Ce fichier.
- `assets/mon_logo.png`: Le logo de l'application.
