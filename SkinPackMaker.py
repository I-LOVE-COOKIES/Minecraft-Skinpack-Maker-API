import shutil
import os
import datetime
import sys
import uuid
#---------------
Name = input("Short Minecraft Skin Pack Name (1 word)---->  ")
Long_Name = (""" 
you can use colors here §0 §1 §2 §3 §4 §5 §6 §7 §8 §9 §a §b
Example: §0HELLO §aGuys == Hello is Black and guys green

Enter your Full Skin Pack Name
""")
Long_Name = input("-->>  ")
UUID = str(uuid.uuid4())
UUID1 = str(uuid.uuid4())
print("Random UUID: %s"%(UUID))
Version = input("enter your Version (Example: 0,0,1) or skip --->  ")
SkinText ="""
Enter your Full skinname §2Hero §44 §aLive
when you Done enter 0 
or 
when you Done enter quit
"""
path= f"{os.getcwd()}/SKINPACKS/{Name}"
path2=f"{os.getcwd()}/SKINPACKS/"
path3 =f"{os.getcwd()}/SKINPACKS"
path = path.replace('\\', '/')
Finalpath= f"{os.getcwd()}/Packs"
Finalpath = Finalpath.replace('\\', '/')

print(Long_Name)
try:
    os.rmdir(path3)
except:
    pass
#-----------------------------------------------------------
try:
    os.mkdir(f"{os.getcwd()}/Packs")
    os.mkdir(f"{os.getcwd()}/SKINPACKS")
    os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}")
    os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}/texts")
except:
    pass

try:
    os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}")
except:
    pass

def LOGFile(event,path):
    log_file_path = path
    event = str(event)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(log_file_path):
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{timestamp}: {event}\n")
    else:
        with open(log_file_path, "w") as log_file:
            log_file.write(f"{timestamp}: {event}\n")
#------------------------------------------------------------

def Manifest_Creator(Name,uuid,version,Path):
    try:

        os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}")
        os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}/texts")
    except:
        pass
    Path = Path + "/manifest.json"
    Manifest = """
    {
        "format_version": 1,
        "header": {
            "name": "%s",
            "uuid": "%s",
            "version": [%s]
        },
        "modules": [
            {
                "type": "skin_pack",
                "uuid": "%s",
                "version": [%s]
            }
        ]
    }
    """ % (Name, uuid, version, UUID1, version)

    with open(Path, "w") as file:
        file.write(Manifest)
#------------------------------------------------------------
def zip_folder(folder_path, target_path, filename):
    zip_path = os.path.join(target_path, filename)
    ZIPED=shutil.make_archive(zip_path, 'zip', folder_path)
    end = Finalpath + "/%s"%(Name) +".mcpack"
    print("end== ",end,"  ","Zipped= ",ZIPED )
    os.rename(ZIPED, end)

# ------------------------------------------------------------

def skinLine(filepath,new,end,shortProjectName,longProjectName,skinname,skinFile):
    try:
        os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}/texts")
    except:
        pass
    filepath = filepath + "/skins.json"
    if new == True:
        txt = """{
      "geometry": "skinpacks/skins.json",
      "skins": [
     {"""
        with open(filepath, 'a') as file:
            file.write(txt + '\n')
        txt = """
            "localization_name": "%s",
            "geometry": "geometry.humanoid.customSlim",
            "texture": "%s",
            "type": "free"
        }""" % (skinname, skinFile)
        with open(filepath, 'a') as file:
            file.write(txt + '\n')

    if end == True:
        txt = """
        ],
        "serialize_name": "%s",
        "localization_name": "%s"
        }
        """%(shortProjectName, longProjectName)
        with open(filepath, 'a') as file:
            file.write(txt + '\n')

    if end != True and new != True:

      txt= """,{
        "localization_name": "%s",
        "geometry": "geometry.humanoid.customSlim",
        "texture": "%s",
        "type": "free"
    }"""%(skinname, skinFile)
      with open(filepath, 'a') as file:
          file.write(txt + '\n')


# ------------------------------------------------------------
def enUS(path,shortPackname,skinNameNormal,skinNameColor,longPackname,new):
    path = path + "/texts/en_US.lang"
    if new == True:
        txt = 'skinpack.%s=%s' % (shortPackname, longPackname)
        with open(path, 'a') as datei:
            datei.write(txt + '\n')
    txt = 'skin.%s.%s=%s' % (shortPackname, skinNameNormal, skinNameColor)
    with open(path, 'a') as datei:
        datei.write(txt + '\n')
#-------------------------------------------------------------
def CopyFile(dest,SRC):
    dest = dest + "/"
    try:
        shutil.copy2(SRC, dest)
    except:
        print("Error by Copy the File")
#  ------------------------------------------------------------
def NEWSKIN(New):
    print(SkinText)
    FullNAME = input("--->  ")
    if FullNAME == "0" or FullNAME == "quit":
        skinLine(path,False,True,Name,Long_Name,"f","f")
        zip_folder(path2, Finalpath, Name)
        input("Enter to QUIT")
        quit()
    ShortName =input("Enter A short Name for the skin (1word) -->  ")
    PNG =input("Drag n Drop your Skinfile --->>  ")
    PNG = PNG.replace('\\', '/')
    PNG = PNG.replace('"', '')
    CopyFile(path,PNG)
    o = os.path.basename(PNG)
    p = path + "/" + o
    try:
        os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}")
        os.mkdir(f"{os.getcwd()}/SKINPACKS/{Name}/texts")
    except:
        pass
    new = path +"/"+  ShortName + ".png"
    print(new,"NEW")
    os.rename(p, new)
    if New == True:
        Manifest_Creator(Name,UUID,Version,path)
    skinLine(path, New, False, Name, Long_Name, ShortName, ShortName +".png")
    enUS(path, Name, ShortName, FullNAME, Long_Name, New)
    NEWSKIN(False)
if Version == "" or Version == " ":
    Version = "0,0,1"
NEWSKIN(True)
