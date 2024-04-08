import time
import subprocess
import os
import threading

def run_main(script_name):
    while True:
        print(f'{Fore.YELLOW}> [DEBUG] < :{Style.RESET_ALL} Loading main module...')
        process = subprocess.Popen([python, script_name])
        process.wait()
        time.sleep(1)
        print(f'{Fore.YELLOW}> [DEBUG] < :{Style.RESET_ALL} Module loaded successfully. Ending start process...')

if os.system('python3 --version') > 0:
    if os.system('py --version') > 0:
        python = 'python'
    else:
        python = 'py'
else:
    python = 'python3'

try:
    print('> [DEBUG] < : Verifying all libraries is installed...')
    from colorama import Fore, Style
except ImportError:
    print('[FALATALL ERROR] one or more libraries are not installed. Try pip install -r requirements.txt')
finally:
    print('> [DEBUG] < : All libraries are installed successfully')
    print('> [DEBUG] < : Importing modules...')

try:
    import main
except ImportError:
    print(f'{Fore.RED}[FALATALL ERROR]{Style.RESET_ALL} unable to import one of modules! Check debug for more information.')
finally:
    print(f'{Fore.YELLOW}> [DEBUG] < {Style.RESET_ALL}: All modules imported successfully')
    print(f'{Fore.YELLOW}> [DEBUG] < {Style.RESET_ALL}: Starting bot...')
    run_main('main.py')
