import os
import shutil

# Configuration
REPO = "https://github.com/Wurmcraft/WurmTweaks2.git"
FOLDER = "WurmTweaks2"
DOCS_FOLDER = "Docs"
WEB_ROOT = "Docs-WebRoot"


def run_command(cmd):
    os.system(cmd)


def download_repo():
    if os.path.exists(os.path.dirname(__file__) + "/" + FOLDER):
        os.chdir(os.path.dirname(__file__) + "/" + FOLDER)
        run_command("git pull")
    else:
        print("Repo Folder does not exists, Downloading")
        run_command('git clone ' + REPO)


def build_docs():
    os.chdir(os.path.dirname(__file__) + "/" + FOLDER + "/" + DOCS_FOLDER)
    run_command("mkdocs build")


def move_docs_to_web_dir():
    src = os.path.dirname(__file__) + "/" + FOLDER + "/" + DOCS_FOLDER
    target = os.path.dirname(__file__) + "/" + FOLDER + "/" + WEB_ROOT
    file_names = os.listdir(src)
    for file_name in file_names:
        shutil.copy(os.path.join(src, file_name), target)


download_repo()
build_docs()
move_docs_to_web_dir()
