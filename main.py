#!/usr/bin/env python3

import os
import sys

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
MAGENTA = "\033[95m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BBLACK  = "\033[90m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    clear()
    print(f"{RED}{BOLD}")
    print("  ██████╗  █████╗ ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗")
    print("  ██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝")
    print("  ██████╔╝███████║███████╗███████╗   ██║   ██║   ██║██║   ██║██║     ███████╗")
    print("  ██╔═══╝ ██╔══██║╚════██║╚════██║   ██║   ██║   ██║██║   ██║██║     ╚════██║")
    print("  ██║     ██║  ██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║")
    print(f"  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{RESET}")
    print(f"{MAGENTA}{BOLD}")
    print("  ╔══════════════════════════════════════════════════════════════╗")
    print(f"  ║  {"Password Tools Suite — Red Team Edition":^60}  ║")
    print(f"  ║  {"Wordlist  •  Hash ID  •  Cracker  •  Strength  •  Users":^60}  ║")
    print(f"  ║  {"Author: CodeScripting  |  foodpoop96@gmail.com":^60}  ║")
    print(f"  ╚══════════════════════════════════════════════════════════════╝{RESET}")
    print()

def print_menu():
    print(f"  {CYAN}{BOLD}MAIN MENU{RESET}")
    print(f"  {BBLACK}{'─' * 50}{RESET}")
    print(f"  {YELLOW}[1]{RESET}  {WHITE}Wordlist Generator{RESET}       {BBLACK}— build custom wordlists{RESET}")
    print(f"  {YELLOW}[2]{RESET}  {WHITE}Hash Identifier{RESET}          {BBLACK}— detect hash type{RESET}")
    print(f"  {YELLOW}[3]{RESET}  {WHITE}Hash Cracker{RESET}             {BBLACK}— dictionary attack{RESET}")
    print(f"  {YELLOW}[4]{RESET}  {WHITE}Password Strength{RESET}        {BBLACK}— analyze passwords{RESET}")
    print(f"  {YELLOW}[5]{RESET}  {WHITE}Username Generator{RESET}       {BBLACK}— generate usernames{RESET}")
    print(f"  {YELLOW}[0]{RESET}  {WHITE}Exit{RESET}")
    print(f"  {BBLACK}{'─' * 50}{RESET}")

def main():
    sys.path.insert(0, os.path.dirname(__file__))

    from tools import (
        wordlist_generator,
        hash_identifier,
        hash_cracker,
        password_strength,
        username_generator,
    )

    while True:
        print_banner()
        print_menu()

        choice = input(f"\n  {CYAN}Select: {RESET}").strip()

        if   choice == '1': wordlist_generator.run()
        elif choice == '2': hash_identifier.run()
        elif choice == '3': hash_cracker.run()
        elif choice == '4': password_strength.run()
        elif choice == '5': username_generator.run()
        elif choice == '0':
            print(f"\n  {GREEN}Goodbye.\n{RESET}")
            sys.exit(0)
        else:
            print(f"\n  {RED}Invalid choice.{RESET}")

if __name__ == "__main__":
    main()
