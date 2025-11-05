# Extracteur de Relevés Bancaires CIC

Cette application Streamlit permet d'extraire les transactions de relevés bancaires PDF de la banque CIC et de les exporter dans un fichier Excel propre et formaté.

## 🚀 Fonctionnalités

### Extraction et Traitement
- **Téléversement multiple** : Chargez un ou plusieurs fichiers PDF de relevés bancaires en une seule fois.
- **Barre de progression** : Suivez l'avancement du traitement de vos fichiers en temps réel.
- **Extraction de données** : Analyse automatique des tables dans les PDF pour extraire la date, le libellé, et les montants des transactions.
- **Traitement des données** : Convertit automatiquement les débits en nombres négatifs et les crédits en nombres positifs.
- **Validation des fichiers** : Vérification automatique que les fichiers sont bien des PDF valides.

### Statistiques et Analyse
- **Tableau de bord statistique** : Affiche en temps réel :
  - 💳 Solde total des transactions
  - 📉 Total des débits
  - 📈 Total des crédits
  - 🔢 Nombre de transactions
  - 📅 Période couverte (date min/max)

### Filtres et Recherche
- **Recherche par libellé** : Recherchez rapidement dans les libellés des transactions (insensible à la casse).
- **Filtre par date** : Sélectionnez une plage de dates pour afficher uniquement les transactions souhaitées.
- **Filtre par montant** : Utilisez un slider pour filtrer les transactions par montant (min/max).
- **Filtre par type** : Affichez uniquement les débits, les crédits, ou toutes les transactions.
- **Compteur dynamique** : Affiche le nombre de transactions filtrées par rapport au total.

### Visualisation
- **Tableau interactif** : Affichage des données extraites dans un tableau clair et trié par date.
- **Alternance de couleurs** : Lignes alternées pour une meilleure lisibilité.
- **Hauteur optimisée** : Tableau avec défilement intégré pour gérer de grandes quantités de données.

### Export Excel
- **Export intelligent** : Téléchargez toutes les transactions consolidées dans un unique fichier `.xlsx`.
- **Nom de fichier avec date** : Les fichiers exportés incluent automatiquement la date d'export (format : `transactions_cic_YYYY-MM-DD.xlsx`).
- **Mise en forme professionnelle** : 
  - Largeurs de colonnes auto-ajustées
  - Format monétaire pour les débits/crédits
  - Format de date DD/MM/YYYY
  - Styles appliqués automatiquement

### Expérience Utilisateur
- **Persistance des données** : Les données extraites restent en mémoire après traitement (session state).
- **Bouton Effacer** : Réinitialisez facilement pour traiter de nouveaux fichiers sans recharger la page.
- **Animation de succès** : Célébration visuelle après extraction réussie.
- **Interface responsive** : Design adaptatif pour tous les écrans.

## 📦 Installation et Lancement

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Clonez le projet** :
   ```bash
   git clone https://github.com/multibrasservices/CIC_extract.git
   cd CIC_extract
   ```

2. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Lancement

**Option 1 : Via le script batch (Windows)**
- Double-cliquez sur `lanceur_streamlit_app.bat`

**Option 2 : Via la ligne de commande**
```bash
streamlit run app.py
```

L'application devrait s'ouvrir automatiquement dans votre navigateur web à l'adresse `http://localhost:8501`.

## 📁 Structure du projet

```
CIC_extract/
├── app.py                 # Code source principal de l'application Streamlit
├── requirements.txt        # Liste des dépendances Python
├── README.md              # Ce fichier
├── .gitignore             # Fichiers à ignorer par Git
├── lanceur_streamlit_app.bat  # Script de lancement Windows
├── assets/
│   └── mon_logo.png       # Logo de l'application
├── data/                  # Dossier pour les fichiers Excel (ignoré par Git)
└── pdf/                   # Dossier pour les fichiers PDF d'exemple (optionnel)
```

## 🔧 Dépendances

Les dépendances principales sont :
- `streamlit` : Framework web pour l'interface utilisateur
- `pandas` : Manipulation et analyse de données
- `pdfplumber` : Extraction de données depuis les PDF
- `openpyxl` : Génération et formatage des fichiers Excel

Voir `requirements.txt` pour la liste complète.

## 📝 Utilisation

1. **Chargez vos fichiers PDF** : Sélectionnez un ou plusieurs fichiers PDF de relevés bancaires CIC.
2. **Cliquez sur "Extraire et Traiter les Données"** : L'application extrait automatiquement toutes les transactions.
3. **Consultez les statistiques** : Visualisez un résumé de vos transactions.
4. **Filtrez si nécessaire** : Utilisez les filtres pour affiner votre recherche.
5. **Exportez vers Excel** : Téléchargez le fichier Excel formaté avec toutes vos transactions.

## 🎨 Améliorations récentes

- ✨ Ajout de statistiques détaillées
- ✨ Barre de progression pour le traitement de fichiers multiples
- ✨ Système de filtres avancé (recherche, date, montant, type)
- ✨ Persistance des données avec session state
- ✨ Bouton de réinitialisation
- ✨ Nom de fichier Excel avec date d'export
- ✨ Validation des fichiers PDF
- ✨ Améliorations visuelles (alternance de couleurs, design moderne)
- ✨ Footer fixe optimisé

## 📄 Licence

© 2025 - Tous droits réservés

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
