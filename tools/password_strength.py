import re
import string

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BBLACK  = "\033[90m"
MAGENTA = "\033[95m"

COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "welcome", "monkey", "dragon", "master",
    "shadow", "12345678", "abc123", "iloveyou", "sunshine",
    "princess", "football", "charlie", "donald", "superman",
    "batman", "trustno1", "hello", "welcome1", "passw0rd",
]

def score_password(pwd):
    score    = 0
    feedback = []
    checks   = {}

    checks['length_8']   = len(pwd) >= 8
    checks['length_12']  = len(pwd) >= 12
    checks['length_16']  = len(pwd) >= 16
    checks['uppercase']  = bool(re.search(r'[A-Z]', pwd))
    checks['lowercase']  = bool(re.search(r'[a-z]', pwd))
    checks['digits']     = bool(re.search(r'\d', pwd))
    checks['special']    = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd))
    checks['no_spaces']  = ' ' not in pwd
    checks['not_common'] = pwd.lower() not in COMMON_PASSWORDS
    checks['no_repeat']  = not bool(re.search(r'(.)\1{2,}', pwd))
    checks['no_seq']     = not any(
        seq in pwd.lower() for seq in ['123', 'abc', 'qwerty', 'pass', 'admin']
    )

    score_map = {
        'length_8':   10,
        'length_12':  15,
        'length_16':  20,
        'uppercase':  10,
        'lowercase':  10,
        'digits':     10,
        'special':    20,
        'no_spaces':   5,
        'not_common': 25,
        'no_repeat':  10,
        'no_seq':     10,
    }

    for check, val in checks.items():
        if val:
            score += score_map[check]

    score = min(score, 100)

    if not checks['length_8']:
        feedback.append(f"  {RED}✗{RESET} Too short — minimum 8 characters")
    elif not checks['length_12']:
        feedback.append(f"  {YELLOW}⚠{RESET} Consider using 12+ characters")
    elif not checks['length_16']:
        feedback.append(f"  {YELLOW}⚠{RESET} 16+ characters recommended")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Good length ({len(pwd)} chars)")

    if not checks['uppercase']:
        feedback.append(f"  {RED}✗{RESET} Add uppercase letters")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Has uppercase letters")

    if not checks['lowercase']:
        feedback.append(f"  {RED}✗{RESET} Add lowercase letters")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Has lowercase letters")

    if not checks['digits']:
        feedback.append(f"  {RED}✗{RESET} Add numbers")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Has numbers")

    if not checks['special']:
        feedback.append(f"  {RED}✗{RESET} Add special characters (!@#$...)")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Has special characters")

    if not checks['not_common']:
        feedback.append(f"  {RED}✗{RESET} This is a commonly used password!")
    else:
        feedback.append(f"  {GREEN}✓{RESET} Not a common password")

    if not checks['no_repeat']:
        feedback.append(f"  {YELLOW}⚠{RESET} Avoid repeated characters (aaa, 111)")
    else:
        feedback.append(f"  {GREEN}✓{RESET} No repeated character sequences")

    if not checks['no_seq']:
        feedback.append(f"  {YELLOW}⚠{RESET} Avoid sequences (123, abc, qwerty)")
    else:
        feedback.append(f"  {GREEN}✓{RESET} No common sequences")

    entropy = len(set(pwd)) * len(pwd)

    return score, feedback, checks, entropy

def get_strength_label(score):
    if score >= 90:
        return f"{GREEN}{BOLD}VERY STRONG{RESET}", GREEN
    elif score >= 70:
        return f"{GREEN}STRONG{RESET}", GREEN
    elif score >= 50:
        return f"{YELLOW}MODERATE{RESET}", YELLOW
    elif score >= 30:
        return f"{RED}WEAK{RESET}", RED
    else:
        return f"{RED}{BOLD}VERY WEAK{RESET}", RED

def draw_bar(score, color):
    filled = int(score / 5)
    empty  = 20 - filled
    return f"{color}{'█' * filled}{BBLACK}{'░' * empty}{RESET}"

def estimate_crack_time(score, pwd_len):
    if score >= 90:
        return "centuries"
    elif score >= 70:
        return "years to decades"
    elif score >= 50:
        return "months to years"
    elif score >= 30:
        return "hours to days"
    else:
        return "seconds to minutes"

def run():
    while True:
        print(f"\n{CYAN}{BOLD}  Password Strength Checker{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")
        print(f"  {YELLOW}[1]{RESET} {WHITE}Check a password{RESET}")
        print(f"  {YELLOW}[2]{RESET} {WHITE}Check passwords from file{RESET}")
        print(f"  {YELLOW}[3]{RESET} {WHITE}Compare multiple passwords{RESET}")
        print(f"  {YELLOW}[0]{RESET} {WHITE}Back{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")

        choice = input(f"\n  {CYAN}Select: {RESET}").strip()

        if choice == '1':
            import getpass
            pwd = getpass.getpass(f"\n  {YELLOW}Enter password (hidden): {RESET}")
            if not pwd:
                continue

            score, feedback, checks, entropy = score_password(pwd)
            label, color = get_strength_label(score)
            bar          = draw_bar(score, color)
            crack_time   = estimate_crack_time(score, len(pwd))

            print(f"\n  {BBLACK}{'─' * 50}{RESET}")
            print(f"  {WHITE}Strength  : {RESET}{label}")
            print(f"  {WHITE}Score     : {RESET}{color}{score}/100{RESET}")
            print(f"  {WHITE}Bar       : {RESET}{bar}")
            print(f"  {WHITE}Entropy   : {RESET}{entropy}")
            print(f"  {WHITE}Est. crack: {RESET}{crack_time}")
            print(f"\n  {CYAN}Analysis:{RESET}")
            for line in feedback:
                print(f"  {line}")
            print(f"  {BBLACK}{'─' * 50}{RESET}")

        elif choice == '2':
            path = input(f"\n  {YELLOW}File path: {RESET}").strip()
            try:
                with open(path) as f:
                    passwords = [l.strip() for l in f if l.strip()]
            except FileNotFoundError:
                print(f"  {RED}File not found.{RESET}")
                continue

            print(f"\n  {BBLACK}{'─' * 65}{RESET}")
            print(f"  {WHITE}{'Password':<30} {'Score':>5}  {'Strength'}{RESET}")
            print(f"  {BBLACK}{'─' * 65}{RESET}")

            for pwd in passwords:
                score, _, _, _ = score_password(pwd)
                label, color   = get_strength_label(score)
                display = pwd[:28] + '..' if len(pwd) > 28 else pwd
                print(f"  {WHITE}{display:<30}{RESET} {color}{score:>5}{RESET}  {label}")

            print(f"  {BBLACK}{'─' * 65}{RESET}")

        elif choice == '3':
            raw = input(f"\n  {YELLOW}Enter passwords (comma separated): {RESET}").strip()
            if not raw:
                continue

            passwords = [p.strip() for p in raw.split(',') if p.strip()]
            print(f"\n  {BBLACK}{'─' * 65}{RESET}")

            for pwd in passwords:
                score, _, _, _ = score_password(pwd)
                label, color   = get_strength_label(score)
                bar            = draw_bar(score, color)
                display        = pwd[:20] + '..' if len(pwd) > 20 else pwd
                print(f"  {WHITE}{display:<22}{RESET} {bar} {color}{score}{RESET}")

            print(f"  {BBLACK}{'─' * 65}{RESET}")

        elif choice == '0':
            break

        else:
            print(f"  {RED}Invalid.{RESET}")
