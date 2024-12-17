# 🚀 **Auto Convert Pandoc**

## 📝 **Description du projet**

**Auto Convert Pandoc** est un outil d'automatisation pour convertir des fichiers **Markdown (.md)** en **PDF**, **HTML** et **DOCX** à l'aide de **Pandoc** et **Python**.  
L'utilisateur dépose un fichier `.md` dans un dossier spécifique (PDF, HTML ou DOCX), et le script s'occupe de :

1. **Convertir automatiquement** le fichier dans le format souhaité.
2. **Organiser les fichiers** :
   - Les fichiers convertis sont déplacés dans des sous-dossiers appropriés (`PDF converti`, `HTML converti`, `DOCX converti`).
   - Les fichiers `.md` d'origine sont archivés dans un dossier `Fichier d'origine`.

---

## 📂 **Structure du projet**

Voici la structure complète des dossiers et fichiers :

```plaintext
/Desktop
    /auto_convert_pandoc           <-- Dossier principal du projet
        /PDF                       <-- Déposer les fichiers .md à convertir en PDF
        /HTML                      <-- Déposer les fichiers .md à convertir en HTML
        /DOCX                      <-- Déposer les fichiers .md à convertir en DOCX
        /Fichier d'origine         <-- Fichiers .md d'origine après conversion
        /Fichier converti          <-- Dossier des fichiers convertis
            /PDF converti          <-- Fichiers PDF convertis
            /HTML converti         <-- Fichiers HTML convertis
            /DOCX converti         <-- Fichiers DOCX convertis
        convert_md.py              <-- Script Python principal pour la conversion
        requirements.txt           <-- Liste des dépendances Python
        README.md                  <-- Documentation du projet
```
⚙️ Prérequis
Outils nécessaires

  Pandoc :
    Installez Pandoc pour permettre la conversion des fichiers Markdown.
    👉 Télécharger Pandoc

 Python 3 :
    Assurez-vous d'avoir Python 3 installé.
    👉 Télécharger Python

  MikTeX ou TeX Live :
    Nécessaire pour générer des fichiers PDF.
    👉 Installer MiKTeX

🔧 Installation
1. Cloner le projet

Clonez le projet sur votre machine :

git clone https://github.com/votre-utilisateur/auto_convert_pandoc.git
cd auto_convert_pandoc

2. Installer les dépendances

Installez les dépendances Python requises :

pip install -r requirements.txt

🚀 Utilisation
1. Lancer le script

Depuis le dossier principal auto_convert_pandoc, exécutez le script :

python convert_md.py

2. Déposer un fichier Markdown

Placez un fichier .md dans l'un des dossiers suivants selon le format souhaité :

   PDF : pour convertir en PDF.
    HTML : pour convertir en HTML.
    DOCX : pour convertir en DOCX.

🔄 Processus de conversion

 Conversion automatique :
    Le script détecte le fichier .md ajouté dans un dossier et le convertit dans le format correspondant.

   Organisation des fichiers :
        Le fichier converti est déplacé dans le sous-dossier correspondant dans Fichier converti :
            PDF converti
            HTML converti
            DOCX converti
        Le fichier .md d'origine est déplacé dans le dossier Fichier d'origine.

📊 Exemple d'utilisation
Étape 1 : Ajouter un fichier

Déposez un fichier exemple.md dans le dossier PDF.
Étape 2 : Résultat

   Le fichier exemple.pdf sera généré dans Fichier converti/PDF converti.
    Le fichier exemple.md sera déplacé dans Fichier d'origine.

💡 Commandes Pandoc utiles

Si vous souhaitez tester manuellement les conversions avec Pandoc :

    Convertir en PDF :

pandoc exemple.md -o exemple.pdf

Convertir en HTML :

pandoc exemple.md -o exemple.html

Convertir en DOCX :

 pandoc exemple.md -o exemple.docx

🛠️ Personnalisation

Vous pouvez personnaliser le script convert_md.py pour :

  Ajouter des options Pandoc spécifiques (exemple : templates personnalisés).
    Gérer d'autres formats comme EPUB ou LaTeX.

📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.
📧 Contact

Pour toute question ou suggestion, contactez-moi via GitHub.
🚀 Bonnes conversions avec Auto Convert Pandoc ! 🚀


---

### 📌 **Instructions pour l'ajouter sur GitHub** :

1. **Créez le fichier `README.md`** dans votre dossier `auto_convert_pandoc` sur votre bureau.
2. Copiez-collez le contenu ci-dessus dans le fichier `README.md`.
3. **Ajoutez et poussez le fichier sur GitHub** :

```bash
git add README.md
git commit -m "Ajout du fichier README avec description du projet"
git push origin main
```

Votre fichier README.md apparaîtra directement sur votre page GitHub pour que les utilisateurs puissent comprendre et utiliser votre projet facilement. 🚀

