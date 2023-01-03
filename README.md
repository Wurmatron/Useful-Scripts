# Useful-Scripts

A collection of scripts that i have needed for various projects / server upkeep or automation.

# Scripts / Usage

- <a href="#RimWorld OpenWorld Server Mod Strip">RimWorld OpenWorld Mod Strip</a>
- <a href="#MkDocs Auto-Updater">MkDocs Auto-Updater</a>

### RimWorld OpenWorld Server Mod Strip
Script: `cleannup_mods_rimworld-openworld.py`

A script to strip <a href="">rimworld</a> mods for use with a <a href="https://steamcommunity.com/workshop/filedetails/?id=2768146099">OpenWorld</a> server. It removes all the unneeded parts of the mods to compress the folder down. Generally saves around 90% of disk space.

Usage: Place script into the folder with the mods and run. `python cleannup_mods_rimworld-openworld.py`

Requires: `Python3`,
   
   
### MkDocs Auto-Updater
Script: `mkdocs_autoupdate.py`

A script to automatically pull a git repo and build its <a href="https://www.mkdocs.org/">mkdocs</a> and place the build into a specific folder. IE A web directory.

Usage: Run this script, when needed or via <a href="https://crontab-generator.org/">crontab</a> perodically. `mkdocs_autoupdate.py`
  - Change the `REPO` to the link to the git repo
  - Change the `FOLDER` to the name of the project
  - Change the `DOCS_FOLDER` to the folder that contains the <a href="https://www.mkdocs.org/">mkdocs</a> within your repo
  - Change the `WEB_ROOT` to the folder which you want the built docs to be placed into, when the script is run.
    
Requires: `Python3`, `mkdocs`, Any <a href="https://www.mkdocs.org/dev-guide/plugins/">mkdocs plugins</a> the repo uses
