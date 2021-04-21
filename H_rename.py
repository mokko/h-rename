from pathlib import Path
import argparse
import re
import shutil

"""
Rename files so that certain single underlines become double underlines

I_MV_0801  (Folder) 
    Default (Folder)
        I_MV_0801__0000.jpg (File)
        I_MV_0801__0001.jpg (File)
    Download (Folder)
        I_MV_0801.pdf (File)
    Presentation (Folder)
        I_MV_0801__0000.tif (File)
    checksum (File MD5)
    I_MV_0801 (File METS/MODS) 


Andere mögliche Dateinamen
    Adr_(EJ)_1_0025
    EJ_44_0121
    HK_AmArch_38_0019

"""

if __name__ == "__main__":
    #let's simply act on the current directory
    parser = argparse.ArgumentParser(
    description="rename for Hendryk"
)
    parser.add_argument("-d", "--debug", action='store_true', help="Dont rename anything, just say what would be done")
    args = parser.parse_args()
    
    files = {p.resolve() for p in Path(".").glob("**/*") if p.suffix.lower() in [".jpg", ".tif"]}
    for file in files:
        parent = file.parent
        stem = file.stem
        suffix = file.suffix
        new_stem = re.sub("[\w\d]_(\d+)$", r"__\1", stem)
        new_file = parent.joinpath(new_stem+suffix)
        if (args.debug):
            print(f"{file}\n -> {new_file}")
        else:
            shutil.move(file, new_file)

