import os
import shutil
mainvar = open('tempfile.txt', 'r')
tempvar = mainvar.read().strip()
mainvar.close()
shutil.move(tempvar + '/' + 'posfixinstall.py', tempvar + '/' + "eCrypt-Installer")
os.remove('tempfile.txt')
print("eCrypt Self Extracting Script")
print("1/5 | Downloading needed files")
print("\nWindows Version")
print("Preparing for deployment")
print("//////////////////////Preparing Self Extracting Script////////////////////////////////")
print("Getting needed files")
print("Getting files")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCrypt4.1.py')
shutil.move(tempvar + '/' + "eCrypt4.1.py", tempvar + '/' + "eCrypt-Installer")
print("Detected as encrypted")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgen3.py')
shutil.move(tempvar + '/' + "passwordgen3.py", tempvar + '/' + "eCrypt-Installer")
print("Downloading all other files requried")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCryptcm.py')
shutil.move(tempvar + '/' + "eCryptcm.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgencm.py')
shutil.move(tempvar + '/' + "passwordgencm.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/posfixinstall2nt.py -o posfixinstall2.py')
shutil.move(tempvar + '/' + "posfixinstall2.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/postfixinstall3.py -o postfixinstall3.py')
shutil.move(tempvar + '/' + "postfixinstall3.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/decryptnt.py -o decrypt.py')
shutil.move(tempvar + '/' + "decrypt.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanupnt.py -o cleanup.py')
shutil.move(tempvar + '/' + "cleanup.py", tempvar + '/' + "eCrypt-Installer")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanup.bat -o cleanup.bat')
shutil.move(tempvar + '/' + "cleanup.bat", tempvar + '/' + "eCrypt-Installer")
print("Returning to Python Codebase")
run = "python3" + " " + tempvar + "\\" + "eCrypt-Installer" + "\\" + "posfixinstall2.py"
os.system(run)
exit
