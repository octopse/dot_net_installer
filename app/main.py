import os
import subprocess
from time import sleep as _sl

DISM_FILE = os.path.expandvars("%SystemRoot%\\System32\\dism.exe")
PART1 = " /online /enable-feature /featurename:NetFX3 /source:"
PART2 = " /LimitAccess"

def file_exist():
    msg1 = "Enter the letter corresponding to the disk: "
    msg2 = "Please verify the letter and enter it again: "
    retry = 1
    while True:
        if retry == 1 :
            disk_letter = input(msg1).upper()
            retry+=1
        else:
            disk_letter = input(msg2).upper()

        verify = os.path.exists(f'{disk_letter}:\\sources\\sxs')
        if verify:
            break
        else:
            continue
    return f'{disk_letter}:{os.sep*2}sources{os.sep*2}sxs'

def message(msg):
    length = len(msg)+1
    print()
    print("="*(length))
    print(msg)
    print("="*(length))

def error_manager(error):
    if error.returncode == 740:
        os.system("cls")
        message(' You have to launch this program with administrator privileges')
        print("\nClosing in 10seconds...")
        _sl(10)
    else:
        print(error.stdout.decode())
def main():
    try:
        while True:
            path = file_exist()
            if path:
                #os.system('cls')
                message(' Installing .NET Framework 3.5 ...')
                try:

                    install = subprocess.run(f'{DISM_FILE} {PART1}"{path}"{PART2}',
                                         check=True, shell=True)
                except subprocess.CalledProcessError as err:
                    error_manager(err)
                    break
                if install:
                    message(' .NET Framework 3.5 is now installed and activated.')
                    if install.stdout:
                        print(install.stdout.decode())
                    break
                else:
                    print('Error\n\tAn error during installation')
            else:
                print("An Error. Please retry")
    except KeyboardInterrupt:
        print()
        message(' Program interrupted. Ctrl + C pressed!')



if __name__ == '__main__':
    main()
