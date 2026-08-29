import hashlib
import time
from pathlib import Path

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BBLACK  = "\033[90m"

ALGOS = {
    '1': ('MD5',    hashlib.md5),
    '2': ('SHA-1',  hashlib.sha1),
    '3': ('SHA-256',hashlib.sha256),
    '4': ('SHA-512',hashlib.sha512),
    '5': ('SHA-384',hashlib.sha384),
}

def crack_single(target_hash, algo_name, algo_func, wordlist_path):
    target_hash = target_hash.strip().lower()
    found       = None
    tried       = 0
    start       = time.time()

    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            words = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print(f"  {RED}Wordlist not found: {wordlist_path}{RESET}")
        return

    total = len(words)
    print(f"\n  {CYAN}Cracking with {algo_name}...{RESET}")
    print(f"  {BBLACK}Wordlist: {wordlist_path} ({total} words){RESET}\n")

    for word in words:
        tried += 1
        attempt = algo_func(word.encode()).hexdigest()

        if tried % 500 == 0 or tried == total:
            pct = (tried / total) * 100
            bar = '█' * int(pct / 5) + '░' * (20 - int(pct / 5))
            print(f"\r  [{bar}] {tried}/{total} ({pct:.0f}%)", end='', flush=True)

        if attempt == target_hash:
            found = word
            break

    elapsed = round(time.time() - start, 2)
    print()
    print(f"  {BBLACK}{'─' * 50}{RESET}")
    print(f"  {WHITE}Hash    : {RESET}{target_hash}")
    print(f"  {WHITE}Algo    : {RESET}{algo_name}")
    print(f"  {WHITE}Tried   : {RESET}{tried} words in {elapsed}s")

    if found:
        print(f"  {GREEN}CRACKED : {RESET}{BOLD}{found}{RESET}")
    else:
        print(f"  {RED}NOT FOUND in wordlist.{RESET}")
    print(f"  {BBLACK}{'─' * 50}{RESET}")

def crack_file(hash_file, algo_name, algo_func, wordlist_path):
    try:
        with open(hash_file) as f:
            hashes = [l.strip().lower() for l in f if l.strip()]
    except FileNotFoundError:
        print(f"  {RED}Hash file not found.{RESET}")
        return

    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            words = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print(f"  {RED}Wordlist not found.{RESET}")
        return

    print(f"\n  {CYAN}Cracking {len(hashes)} hashes with {algo_name}...{RESET}\n")

    results = {}
    start   = time.time()

    for word in words:
        if len(results) == len(hashes):
            break
        attempt = algo_func(word.encode()).hexdigest()
        for h in hashes:
            if h not in results and attempt == h:
                results[h] = word

    elapsed = round(time.time() - start, 2)

    print(f"  {BBLACK}{'─' * 60}{RESET}")
    cracked = 0
    for h in hashes:
        if h in results:
            cracked += 1
            print(f"  {GREEN}✓{RESET} {h[:40]} → {BOLD}{results[h]}{RESET}")
        else:
            print(f"  {RED}✗{RESET} {h[:40]} → {BBLACK}Not found{RESET}")

    print(f"  {BBLACK}{'─' * 60}{RESET}")
    print(f"  {GREEN}Cracked: {cracked}/{len(hashes)}{RESET}  {BBLACK}Time: {elapsed}s{RESET}")

def run():
    while True:
        print(f"\n{CYAN}{BOLD}  Hash Cracker{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")
        print(f"  {YELLOW}[1]{RESET} {WHITE}Crack a single hash{RESET}")
        print(f"  {YELLOW}[2]{RESET} {WHITE}Crack hashes from file{RESET}")
        print(f"  {YELLOW}[0]{RESET} {WHITE}Back{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")

        choice = input(f"\n  {CYAN}Select: {RESET}").strip()

        if choice in ('1', '2'):
            print(f"\n  {CYAN}Algorithm:{RESET}")
            for k, (name, _) in ALGOS.items():
                print(f"  {YELLOW}[{k}]{RESET} {name}")

            algo_choice = input(f"\n  {CYAN}Select: {RESET}").strip()
            if algo_choice not in ALGOS:
                print(f"  {RED}Invalid.{RESET}")
                continue

            algo_name, algo_func = ALGOS[algo_choice]
            wordlist = input(f"  {YELLOW}Wordlist path (default: wordlists/common.txt): {RESET}").strip()
            if not wordlist:
                wordlist = "wordlists/common.txt"

            if choice == '1':
                h = input(f"  {YELLOW}Enter hash to crack: {RESET}").strip()
                if h:
                    crack_single(h, algo_name, algo_func, wordlist)

            elif choice == '2':
                path = input(f"  {YELLOW}Hash file path: {RESET}").strip()
                if path:
                    crack_file(path, algo_name, algo_func, wordlist)

        elif choice == '0':
            break

        else:
            print(f"  {RED}Invalid.{RESET}")
