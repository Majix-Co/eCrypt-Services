import filecmp
import time
import os
print("\nMajix Installer")
print("\n2/5 | Comparing files to web versions\n")
time.sleep(2)
dir = os.getcwd()
dirtest = "eCrypt-Installer"
source3 = dir.strip() + "/" + "license.txt"
license = open(source3, 'r')
print("Please ready the license below\n")
i = input("\nDo you agree to the license? (yes/no[default])")
print(license.read())
license.close()
os.remove(source3)
if dir in dirtest:
    if i == "yes":
        source = dir + "/" + "eCryptcm.py"
        scheck1 = dir + "/" + "eCrypt4.4.py"
        print("Checking values")
        filecheck = filecmp.cmp(source,scheck1)
        if filecheck == True:
            print("\nOkay File looks okay")
            source = dir + "/" + "passwordgencm.py"
            scheck1 = dir + "/" + "passwordgen3.py"
            filecheck2 = filecmp.cmp(source,scheck1)
            if filecheck2 == True:
                print("All checks Passed!")
                print("Preparing next check")
                os.system('chmod +x postfixinstall3.sh')
                os.system('./postfixinstall3.sh')
                exit()
            elif filecheck2 == False:
                print("Looks like the file is not right")
                exit()
        elif filecheck == False:
        print("File may have been tampered with they do not match killing script")
        exit()
    else:
        print("Whoops!, This program can not install if the license was not agreeded to")
        print("Please rerun the install script")
        deldir = "rm -rf " + dir
        os.system(deldir)
        exit()
else:
    print('Whoops!, A critical error was detected kill script to save system')
    print('What happened? You are running this NOT in the install directory')
    print("Doing this can delete dierectory's you do not want to be deleted")
    print('Delete this and ONLY use install.py DO NOT attempt to run any manualey')
    os.remove(__file__)
    exit('System Failsafe')
