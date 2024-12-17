import os
import shutil
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Dossiers sur le bureau
DESKTOP_PATH = os.path.expanduser("~/Desktop")
WATCH_FOLDERS = {
    "pdf": os.path.join(DESKTOP_PATH, "PDF"),  # Dossier pour les fichiers .md à convertir en PDF
    "html": os.path.join(DESKTOP_PATH, "HTML"),  # Dossier pour les fichiers .md à convertir en HTML
    "docx": os.path.join(DESKTOP_PATH, "DOCX")  # Dossier pour les fichiers .md à convertir en DOCX
}

# Dossier "Fichiers convertis" et sous-dossiers
CONVERTED_FOLDER = os.path.join(DESKTOP_PATH, "Fichiers convertis")
PDF_FOLDER = os.path.join(CONVERTED_FOLDER, "PDF converti")
HTML_FOLDER = os.path.join(CONVERTED_FOLDER, "HTML converti")
DOCX_FOLDER = os.path.join(CONVERTED_FOLDER, "DOCX converti")

# Dossier pour déplacer les fichiers .md originaux après conversion
ORIGINAL_FOLDER = os.path.join(DESKTOP_PATH, "Fichier origine")

# Crée les dossiers si ils n'existent pas
os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(HTML_FOLDER, exist_ok=True)
os.makedirs(DOCX_FOLDER, exist_ok=True)
os.makedirs(ORIGINAL_FOLDER, exist_ok=True)

# Fonction pour convertir .md en PDF
def convert_md_to_pdf(md_file):
    try:
        filename = os.path.splitext(md_file)[0]
        command = ['pandoc', md_file, '--pdf-engine=lualatex', '-o', f'{filename}.pdf']
        subprocess.run(command, check=True)
        print(f"Conversion en PDF réussie : {md_file} -> {filename}.pdf")
        # Déplacer le fichier PDF dans le bon dossier
        shutil.move(f'{filename}.pdf', PDF_FOLDER)
    except Exception as e:
        print(f"Erreur lors de la conversion en PDF de {md_file}: {e}")

# Fonction pour convertir .md en HTML
def convert_md_to_html(md_file):
    try:
        filename = os.path.splitext(md_file)[0]
        command = ['pandoc', md_file, '-o', f'{filename}.html']
        subprocess.run(command, check=True)
        print(f"Conversion en HTML réussie : {md_file} -> {filename}.html")
        # Déplacer le fichier HTML dans le bon dossier
        shutil.move(f'{filename}.html', HTML_FOLDER)
    except Exception as e:
        print(f"Erreur lors de la conversion en HTML de {md_file}: {e}")

# Fonction pour convertir .md en DOCX
def convert_md_to_docx(md_file):
    try:
        filename = os.path.splitext(md_file)[0]
        command = ['pandoc', md_file, '-o', f'{filename}.docx']
        subprocess.run(command, check=True)
        print(f"Conversion en DOCX réussie : {md_file} -> {filename}.docx")
        # Déplacer le fichier DOCX dans le bon dossier
        shutil.move(f'{filename}.docx', DOCX_FOLDER)
    except Exception as e:
        print(f"Erreur lors de la conversion en DOCX de {md_file}: {e}")

# Classe pour gérer les événements du dossier
class MDFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        # Si un fichier .md est ajouté au dossier
        if event.src_path.endswith('.md'):
            print(f"Fichier détecté : {event.src_path}")
            
            # Détecte dans quel dossier le fichier a été ajouté et effectue la conversion correspondante
            if event.src_path.startswith(WATCH_FOLDERS["pdf"]):
                convert_md_to_pdf(event.src_path)
            elif event.src_path.startswith(WATCH_FOLDERS["html"]):
                convert_md_to_html(event.src_path)
            elif event.src_path.startswith(WATCH_FOLDERS["docx"]):
                convert_md_to_docx(event.src_path)
            
            # Déplacer le fichier .md original dans le dossier "Fichier origine"
            shutil.move(event.src_path, ORIGINAL_FOLDER)
            print(f"Fichier {event.src_path} déplacé vers le dossier 'Fichier origine'.")

# Fonction principale pour surveiller les dossiers
def monitor_folders():
    event_handler = MDFileHandler()
    observer = Observer()

    # Surveillance des trois dossiers
    for folder in WATCH_FOLDERS.values():
        observer.schedule(event_handler, folder, recursive=False)
    
    observer.start()
    print(f"Surveillance des dossiers {', '.join(WATCH_FOLDERS.values())} pour les fichiers .md...")
    
    try:
        while True:
            pass  # Le programme continue à surveiller les fichiers
    except KeyboardInterrupt:
        observer.stop()
        print("Arrêt de la surveillance.")
    
    observer.join()

# Démarrer la surveillance
if __name__ == "__main__":
    monitor_folders()
