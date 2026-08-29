# PasswordTools — Red Team Edition

```
██████╗  █████╗ ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██████╔╝███████║███████╗███████╗   ██║   ██║   ██║██║   ██║██║     ███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
██║     ██║  ██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
```

> A modular password tools suite built for red teamers, CTF players, and security researchers.

---

## Overview

PasswordTools is a Python-based command-line toolkit that covers five core areas of password security testing. Everything runs locally with no external APIs or internet required after installation.

---

## File Structure

```
PasswordTools/
├── main.py
├── tools/
│   ├── __init__.py
│   ├── wordlist_generator.py
│   ├── hash_identifier.py
│   ├── hash_cracker.py
│   ├── password_strength.py
│   └── username_generator.py
├── wordlists/
│   └── common.txt
└── requirements.txt
```

---

## Tools Included

### Wordlist Generator
Generate custom wordlists for password attacks.
- Keyword-based with leet speak, years, and special chars
- Random password generation with custom charset
- Combination generator using itertools
- Pattern-based generator using `?`, `#`, `@` tokens

### Hash Identifier
Identify unknown hashes by type.
- Supports MD5, SHA-1, SHA-256, SHA-512, bcrypt, NTLM, MySQL, Argon2, scrypt, and more
- Scan single hash or entire file
- Hash a string using multiple algorithms

### Hash Cracker
Dictionary-based hash cracking.
- Crack a single hash against a wordlist
- Crack multiple hashes from a file
- Supports MD5, SHA-1, SHA-256, SHA-512, SHA-384
- Live progress bar with speed tracking

### Password Strength Checker
Analyze password security in detail.
- Scores passwords out of 100
- Checks length, complexity, entropy, common patterns
- Detects common passwords, repeated chars, sequences
- Estimates crack time
- Batch check from file or compare multiple at once

### Username Generator
Generate username lists for OSINT and enumeration.
- Generate from real name with common patterns
- Random usernames using word combinations
- Keyword-based username generation
- Save output to file

---

## Requirements

- Python 3.8+
- colorama

---

## Installation

```bash
git clone https://github.com/CodeScripting/PasswordTools
cd PasswordTools
pip install -r requirements.txt
python3 main.py
```

### Termux

```bash
pkg install python git
git clone https://github.com/batplatbot/PasswordTools
cd PasswordTools
pip install -r requirements.txt
python3 main.py
```

---

## Usage

```bash
python3 main.py
```

Navigate the menu with number keys. All output files are saved to your current working directory unless a path is specified.

---

## Example Workflows

**Generate a wordlist from a name and crack a hash:**
```
[1] Wordlist Generator → keyword-based → enter: john,doe,1995
[3] Hash Cracker → paste hash → point to generated wordlist
```

**Identify and crack an unknown hash:**
```
[2] Hash Identifier → paste hash → identify type
[3] Hash Cracker → select matching algorithm → run against wordlist
```

**Audit a password list:**
```
[4] Password Strength → check from file → point to your list
```

---

## Legal

This tool is intended for authorized penetration testing, CTF competitions, security research, and educational use only. Do not use against systems or accounts you do not own or have explicit written permission to test.

---

## Author

**CodeScripting**
📧 foodpoop96@gmail.com

---

## License

MIT License — free for personal and educational use.
