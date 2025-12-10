import pyfiglet
import os
import sys

# تعريف الألوان باستخدام رموز ANSI
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
r = "\033[0m"  # reset color

while True:
    os.system('clear')
    logo = pyfiglet.figlet_format("W I F I",font="3-d")
    print(f"{blue}{logo}{r}")
    print(f"{cyan}+-===-+>BRUTE FORCE TO WIFI<+-===-+{r}")
    print(f"{cyan}+---------------------------------+{r}")
    print(f"{cyan}|{r}{yellow}         BRUTE FORCE TO WIFI     {cyan}|{r}")
    print(f"{cyan}+---------------------------------+{r}")
    print(f"{cyan}|{r}{green}(1) Brute Force{blue}      {r}            {cyan}|{r}")
    print(f"{cyan}|{r}{green}(2) Wait...{blue}       {r}               {cyan}|{r}")
    print(f"{cyan}|{r}{green}(3) Wait...{blue}         {r}             {cyan}|{r}")
    print(f"{cyan}|{r}{green}(4) Wait...{blue}  {r} {cyan}                   |{r}")
    print(f"{cyan}|{r}{red}(5) Quit ✗{r}                       {cyan}|{r}")
    print(f"{cyan}+---------------------------------+{r}")
    choice = int(input(f"{magenta}Enter chioce..:{r} "))
    wordlist = input(f"{blue}Enter wordlist path: {r}")
    handshake = input(f"{blue}Enter handshake file path (.cap / .hccapx):{r} ")

    if choice == 1:
        wordlist = input(f"{blue}Enter wordlist path: {r}")
        handshake = input(f"{blue}Enter handshake file path (.cap / .hccapx):{r} ")
    # أمر simulation آمن
        cmd = f"aircrack-ng -w {wordlist} {handshake}"
        os.system(cmd)
        sys.exit(0)
    
