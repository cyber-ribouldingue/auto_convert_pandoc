# Auto Convert Pandoc

## Description

Ce projet permet d'automatiser la conversion de fichiers `.md` (Markdown) en différents formats tels que PDF, HTML et DOCX à l'aide de **Pandoc** et **Python**. Les fichiers `.md` sont déposés dans des dossiers spécifiques (PDF, HTML, DOCX) sur le bureau, et une fois déposés, le script Python les convertit automatiquement dans le format choisi.

## Fonctionnalités

- Conversion automatique des fichiers `.md` en PDF, HTML, et DOCX.
- Les fichiers convertis sont déplacés dans des sous-dossiers appropriés (`PDF converti`, `HTML converti`, `DOCX converti`).
- Le fichier `.md` d'origine est déplacé dans un dossier `Fichier d'origine`.

## Installation

### Prérequis

1. **Installer Pandoc** : [Installation de Pandoc](https://pandoc.org/installing.html)
2. **Installer Python** : [Télécharger Python](https://www.python.org/downloads/)
3. **Installer les dépendances Python** :

   Si vous avez un fichier `requirements.txt` dans le projet, installez les dépendances avec :

   ```bash
   pip install -r requirements.txt
