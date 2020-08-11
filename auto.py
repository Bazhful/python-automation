import argparse
import subprocess 
import getpass
import webbrowser
import os
import re
username = getpass.getuser()
vscode = {
    'wsl': "/mnt/c/Users/%s/AppData/Local/Programs/Microsoft VS Code/Code.exe" % (username),
    'windows': 'C:\\Users\\%s\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe' % (username) 
}
xampp = {
    'wsl': r'/mnt/c/xampp/xampp-control.exe',
    'windows': 'C:\\xampp\\xampp-control.exe'
}
folderDrop = {
   "wsl": "/mnt/c/Users/%s/Dropbox" % (username) ,
   "windows": 'C:\\Users\\%s\\Dropbox' % (username)
}
def main():
    parser = argparse.ArgumentParser(description='Type what type of programming language you are going to code in!')
    parser.add_argument('--language', "-l", metavar="", required=True, help='What programming language you are going to use. Example --> auto.py -L php')
    parser.add_argument('--system', '-s', metavar="", required=True, help='What system are u using. Example --> WSL, Linux, Windows.')
    args = parser.parse_args()

    if args.system == "wsl":
        systype = "wsl"
    elif args.system == "windows":
        systype = "windows"
    else:
        systype = "windows"

    if args.language == "php":
        subprocess.Popen(vscode[systype])
        subprocess.Popen(xampp[systype])
        webbrowser.open('https://www.php.net/docs.php')
        os.startfile(folderDrop[systype])
        
        print(username)

    else:
        print("It didnt work")

if __name__ == "__main__":
    main()


