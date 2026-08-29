import re
import hashlib

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BBLACK  = "\033[90m"

HASH_SIGNATURES = [
    {
        "name": "MD5",
        "length": 32,
        "regex": r'^[a-f0-9]{32}$',
        "description": "Message Digest 5 — very common, fast to crack",
        "example": "5f4dcc3b5aa765d61d8327deb882cf99"
    },
    {
        "name": "SHA-1",
        "length": 40,
        "regex": r'^[a-f0-9]{40}$',
        "description": "Secure Hash Algorithm 1 — deprecated",
        "example": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
    },
    {
        "name": "SHA-224",
        "length": 56,
        "regex": r'^[a-f0-9]{56}$',
        "description": "SHA-2 family, 224-bit variant",
        "example": ""
    },
    {
        "name": "SHA-256",
        "length": 64,
        "regex": r'^[a-f0-9]{64}$',
        "description": "SHA-2 family, 256-bit — widely used",
        "example": "5e884898da28047151d0e56f8dc629277"
    },
    {
        "name": "SHA-384",
        "length": 96,
        "regex": r'^[a-f0-9]{96}$',
        "description": "SHA-2 family, 384-bit variant",
        "example": ""
    },
    {
        "name": "SHA-512",
        "length": 128,
        "regex": r'^[a-f0-9]{128}$',
        "description": "SHA-2 family, 512-bit — very strong",
        "example": ""
    },
    {
        "name": "bcrypt",
        "length": 60,
        "regex": r'^\$2[ayb]\$.{56}$',
        "description": "Adaptive hash — slow by design, hard to crack",
        "example": "$2y$10$abcdefghijklmnopqrstuuABCDEFGHIJKLMNOPQRSTUVWXYZ01234"
    },
    {
        "name": "MD5 (Unix/salted)",
        "length": 22,
        "regex": r'^\$1\$.+\$.+$',
        "description": "Unix MD5 crypt format",
        "example": "$1$salt$hash"
    },
    {
        "name": "SHA-512 (Unix)",
        "length": 98,
        "regex": r'^\$6\$.+\$.+$',
        "description": "Unix SHA-512 crypt format",
        "example": "$6$salt$hash"
    },
    {
        "name": "NTLM",
        "length": 32,
        "regex": r'^[A-F0-9]{32}$',
        "description": "Windows NTLM hash — uppercase hex",
        "example": "8846F7EAEE8FB117AD06BDD830B7586C"
    },
    {
        "name": "MySQL4/5",
        "length": 41,
        "regex": r'^\*[A-F0-9]{40}$',
        "description": "MySQL password hash",
        "example": "*FE8009E3707D48C1B20D88ED528FE5E7D7699B26"
    },
    {
        "name": "SHA-3 (256)",
        "length": 64,
        "regex": r'^[a-f0-9]{64}$',
        "description": "SHA-3 family, same length as SHA-256",
        "example": ""
    },
    {
        "name": "Whirlpool",
        "length": 128,
        "regex": r'^[a-f0-9]{128}$',
        "description": "Whirlpool hash — same length as SHA-512",
        "example": ""
    },
    {
        "name": "RIPEMD-160",
        "length": 40,
        "regex": r'^[a-f0-9]{40}$',
        "description": "RACE Integrity Primitives Evaluation",
        "example": ""
    },
    {
        "name": "CRC32",
        "length": 8,
        "regex": r'^[a-f0-9]{8}$',
        "description": "Cyclic Redundancy Check — not a secure hash",
        "example": ""
    },
    {
        "name": "Argon2",
        "length": None,
        "regex": r'^\$argon2.+\$.+',
        "description": "Memory-hard hash — very resistant to cracking",
        "example": "$argon2id$v=19$m=65536..."
    },
    {
        "name": "scrypt",
        "length": None,
        "regex": r'^\$s0\$.+',
        "description": "Memory and CPU hard hash",
        "example": "$s0$..."
    },
]

def identify_hash(h):
    h = h.strip()
    matches = []

    for sig in HASH_SIGNATURES:
        try:
            if re.match(sig["regex"], h, re.IGNORECASE):
                matches.append(sig)
        except re.error:
            continue

    return matches

def hash_string(text):
    print(f"\n  {CYAN}Hash a String{RESET}\n")
    algos = {
        '1': ('MD5',    hashlib.md5),
        '2': ('SHA-1',  hashlib.sha1),
        '3': ('SHA-256',hashlib.sha256),
        '4': ('SHA-512',hashlib.sha512),
        '5': ('SHA-384',hashlib.sha384),
    }
    for k, (name, _) in algos.items():
        print(f"  {YELLOW}[{k}]{RESET} {WHITE}{name}{RESET}")

    choice = input(f"\n  {CYAN}Select algorithm: {RESET}").strip()
    if choice not in algos:
        print(f"  {RED}Invalid.{RESET}")
        return

    text_input = input(f"  {YELLOW}Enter text to hash: {RESET}").strip()
    if not text_input:
        print(f"  {RED}Nothing entered.{RESET}")
        return

    name, func = algos[choice]
    result = func(text_input.encode()).hexdigest()

    print(f"\n  {BBLACK}{'─' * 50}{RESET}")
    print(f"  {WHITE}Input   : {RESET}{text_input}")
    print(f"  {WHITE}Algo    : {RESET}{name}")
    print(f"  {GREEN}Hash    : {RESET}{result}")
    print(f"  {WHITE}Length  : {RESET}{len(result)} chars")
    print(f"  {BBLACK}{'─' * 50}{RESET}")

def run():
    while True:
        print(f"\n{CYAN}{BOLD}  Hash Identifier{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")
        print(f"  {YELLOW}[1]{RESET} {WHITE}Identify a hash{RESET}")
        print(f"  {YELLOW}[2]{RESET} {WHITE}Identify multiple hashes from file{RESET}")
        print(f"  {YELLOW}[3]{RESET} {WHITE}Hash a string{RESET}")
        print(f"  {YELLOW}[0]{RESET} {WHITE}Back{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")

        choice = input(f"\n  {CYAN}Select: {RESET}").strip()

        if choice == '1':
            h = input(f"\n  {YELLOW}Enter hash: {RESET}").strip()
            if not h:
                continue

            matches = identify_hash(h)
            print(f"\n  {BBLACK}{'─' * 60}{RESET}")
            print(f"  {WHITE}Hash   : {RESET}{h[:60]}{'...' if len(h)>60 else ''}")
            print(f"  {WHITE}Length : {RESET}{len(h)} chars\n")

            if matches:
                print(f"  {GREEN}Possible types:{RESET}")
                for m in matches:
                    print(f"\n  {CYAN}  ► {m['name']}{RESET}")
                    print(f"     {BBLACK}{m['description']}{RESET}")
            else:
                print(f"  {RED}Could not identify hash type.{RESET}")
            print(f"  {BBLACK}{'─' * 60}{RESET}")

        elif choice == '2':
            path = input(f"\n  {YELLOW}Enter file path: {RESET}").strip()
            try:
                with open(path) as f:
                    hashes = [l.strip() for l in f if l.strip()]
            except FileNotFoundError:
                print(f"  {RED}File not found.{RESET}")
                continue

            print(f"\n  {BBLACK}{'─' * 60}{RESET}")
            for h in hashes:
                matches = identify_hash(h)
                types   = ', '.join(m['name'] for m in matches) if matches else 'Unknown'
                color   = GREEN if matches else RED
                print(f"  {color}{h[:40]:<42}{RESET} → {WHITE}{types}{RESET}")
            print(f"  {BBLACK}{'─' * 60}{RESET}")

        elif choice == '3':
            hash_string('')

        elif choice == '0':
            break

        else:
            print(f"  {RED}Invalid.{RESET}")
