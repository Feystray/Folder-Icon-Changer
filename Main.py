from pathlib import Path
import subprocess
import sys

FilesList = []
for root, dir, files in Path(".").walk():
    for Filename in files:
        FilePath = Path(f"{root}\\{Filename}")
        if FilePath.suffix == ".ico" or FilePath.suffix == ".exe":
            FilesList.append(FilePath)
for i in range(0, len(FilesList)):
    print(f"{i + 1}-> {FilesList[i]}")
Filetobechoosen = input("Enter the number of the File of which icon should be (d to delete): ")

OpenpedPath = Path("desktop.ini")
if Filetobechoosen != "":
    if Filetobechoosen == "d":
        pa = Path("desktop.ini")
        try:
            subprocess.run(["cmd","/c","del", "/a", "desktop.ini"])
            subprocess.run(["taskkill", "/im", "explorer.exe", "/f"])
            subprocess.run(["cmd", "/c", "explorer", Path(".").absolute()])
            subprocess.run(["cmd", "/c", "start", "explorer"])
            sys.exit()
        except:
            sys.exit()
    if int(Filetobechoosen) - 1 > len(FilesList):
        raise FileNotFoundError
    if not Path("desktop.ini").exists():
        FileContent = f'''[.ShellClassInfo]
        IconResource={FilesList[int(Filetobechoosen) - 1].absolute()},0
        [Viewstate]
        Mode=
        Vid=
        FolderType=Generic'''
        OpenpedPath.write_text(FileContent)
        subprocess.run(["attrib", "+h", "+s", "-a", "./desktop.ini"])
        subprocess.run(["attrib", "+r", "."])
        subprocess.run(["taskkill", "/im", "explorer.exe", "/f"])
        subprocess.run(["cmd", "/c", "explorer", Path(".").absolute()])
        subprocess.run(["cmd", "/c", "start", "explorer"])
        subprocess.run(["cmd", "/c", "del", "Folder_icon.exe"])
    if Path("desktop.ini").exists():
        subprocess.run(["cmd", "/c", "del", "/a", "desktop.ini"])
        FileContent = f'''[.ShellClassInfo]
                IconResource={FilesList[int(Filetobechoosen) - 1].absolute()},0
                [Viewstate]
                Mode=
                Vid=
                FolderType=Generic'''
        OpenpedPath.write_text(FileContent)
        subprocess.run(["attrib", "+h", "+s", "-a", "./desktop.ini"])
        subprocess.run(["attrib", "+r", "."])
        subprocess.run(["taskkill", "/im", "explorer.exe", "/f"])
        subprocess.run(["cmd", "/c", "explorer", Path(".").absolute()])
        subprocess.run(["cmd", "/c", "start", "explorer"])
        subprocess.run(["cmd", "/c", "del", "Folder_icon.exe"])

