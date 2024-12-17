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
