import random, string, requests, subprocess, os, sys

def obfuscate(url, times=100):
    return url.split(chr(47))[0]+chr(47)*2+"".join([("".join([(random.choice([chr(i) for i in range(97, 123)]+[(chr(i)) for i in range(48, 58)])) for i in range(times)])+"."+"".join([(random.choice([chr(i) for i in range(97, 123)]+[chr(i) for i in range(48, 58)]+['.com', 'discord', 'bit.ly', 'api', 'webhook', 'download', '.exe', 'telegram', 'org'])) for i in range(times)])+"@") for i in range(3)])+url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1)+chr(35)+"".join([(random.choice([chr(i) for i in range(33, 127)]+[url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1).split('/')[0]]*5+["discord.com/api/webhooks/"+"".join([random.choice(string.digits) for i in range(18)])+"/"+"".join([random.choice(string.ascii_letters) for i in range(68)])for i in range(15)])) for i in range(times)])
    
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')
    
def credit():
    print('\x1b[31;1mh\x1b[32;1mt\x1b[33;1mt\x1b[34;1mp\x1b[35;1ms\x1b[36;1m:\x1b[32;1m/\x1b[33;1m/\x1b[34;1mg\x1b[35;1mi\x1b[36;1mt\x1b[32;1mh\x1b[33;1mu\x1b[34;1mb\x1b[35;1m.\x1b[36;1mc\x1b[32;1mo\x1b[33;1mm\x1b[34;1m/\x1b[35;1mB\x1b[36;1ml\x1b[32;1ma\x1b[33;1mn\x1b[34;1mk\x1b[35;1m-\x1b[36;1mc\x1b[32;1m/\x1b[33;1mB\x1b[34;1ml\x1b[35;1ma\x1b[36;1mn\x1b[32;1mk\x1b[33;1m-\x1b[34;1mU\x1b[35;1mR\x1b[36;1mL\x1b[32;1m-\x1b[33;1mO\x1b[34;1mb\x1b[35;1mf\x1b[36;1mu\x1b[32;1ms\x1b[33;1mc\x1b[34;1ma\x1b[35;1mt\x1b[36;1mo\x1b[32;1mr\x1b[33;1m/\x1b[0m\n\n')

def main():
    clear()
    os.system('title Blank URL Obfuscator' if os.name == 'nt' else '')
    credit()

    if len(sys.argv) != 2:
        print('\u001b[31;1mUsage: python script.py <URL>\u001b[0m')
        return

    URL = sys.argv[1]
    try:
        r = requests.get(URL)
    except Exception:
        print('\u001b[31;1mUnable to reach URL!\u001b[0m\n')
        return

    clear()
    credit()
    print('\u001b[33;1mProcessing...\u001b[0m')
    output_file = f'Obfuscated URL.txt'
    while os.path.exists(output_file):
        overwrite = input(f'\u001b[31;1mA file named "{output_file}" already exists. Do you want to overwrite it? (Y/N): \u001b[0m').lower()
        if overwrite == 'y':
            break
        elif overwrite == 'n':
            new_file_name = input('\u001b[33;1mPlease enter a different name for the output file: \u001b[0m')
            if not new_file_name.endswith('.txt'):
                new_file_name += '.txt'
            output_file = new_file_name
        else:
            print('\u001b[31;1mInvalid input. Please enter Y or N.\u001b[0m')

    with open(output_file, 'w') as file:
        file.write(obfuscate(URL))

    clear()
    credit()
    print(f'\u001b[32;1m\aSaved URL in "\u001b[34;1m{os.path.join(os.path.dirname(__file__), output_file)}\u001b[32;1m"!\u001b[0m\n')

    if os.name == 'nt':
        subprocess.run(['notepad.exe', output_file], check=True)
    else:
        subprocess.run(['xdg-open', output_file], check=True)

    input("\u001b[37;1m(Press enter to exit)\u001b[0m")

if __name__ == "__main__":
    main()
