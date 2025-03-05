import os
import shutil
source = os.getcwd()
source2 = os.path.basename(__file__)
finalsource = source + "/" + source2
print("eCrypt Installer 3.1")
print("© Majix Co.")
#open("temp.sh", 'x')
print("Preparing Installer")
print(source)
print("Getting needed files")
i = input("Hello!, Would you like to full package or just the minimal packages? (f/m): ")
if i == "f":
    try:
        os.mkdir("eCrypt-Installer")
        print("Okay will get full package")
        platformcheck = os.name
        if platformcheck == "posix":
            shutil.move(finalsource,"eCrypt-Installer")
            print("System Deteced as Posfix (Unix Based System)")
            os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/posfixinstall.sh -o posfixinstall.sh')
            os.system('chmod +x posfixinstall.sh')
            os.system('./posfixinstall.sh')
            exit()
        elif platformcheck == "nt":
            shutil.move(finalsource,"eCrypt-Installer")
            print("NT DETECTED")
            print("Windows support is still beta and may have some issues")
            print("Please report any on the issue page on github")
            os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/posfixinstall.bat -o posfixinstall.bat')
            os.system('posfixinstall.bat')
        else:
            print("This script is not compatible with your OS (yet)")
    except FileExistsError:
        print("Partial Install Detected")
        print("Removing old files please re-download this script")
        os.remove(__file__)
        os.rmdir("eCrypt-Installer")
        print("Cleaned up")
        exit()
elif i == "m":
    print("Whoops!, Minimal install is not currently supported please use full install")
    exit()                  


