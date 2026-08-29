import random
import itertools

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BBLACK  = "\033[90m"

ADJECTIVES = [
    "dark", "silent", "ghost", "shadow", "cyber", "red", "black",
    "cold", "iron", "storm", "void", "lost", "dead", "zero", "wild",
    "fatal", "toxic", "elite", "rogue", "alpha", "omega", "ultra",
]

NOUNS = [
    "wolf", "hawk", "viper", "blade", "fox", "rat", "snake", "bear",
    "hunter", "hacker", "coder", "ninja", "ghost", "agent", "storm",
    "byte", "root", "shell", "core", "node", "link", "proxy",
]

def name_to_usernames(first, last, birth_year=""):
    combos = set()
    f  = first.lower()
    l  = last.lower()
    fi = f[0] if f else ''
    li = l[0] if l else ''
    yr = str(birth_year) if birth_year else ''

    patterns = [
        f"{f}{l}", f"{l}{f}", f"{f}.{l}", f"{f}_{l}",
        f"{fi}{l}", f"{f}{li}", f"{f}{li}{yr}", f"{fi}{l}{yr}",
        f"{f}{yr}", f"{l}{yr}", f"{f}{l}{yr}", f"{l}{f}{yr}",
        f"{f}.{l}{yr}", f"{f}_{l}{yr}", f"_{f}{l}_",
        f"{f[0:3]}{l[0:3]}", f"{l[0:3]}{f[0:3]}",
        f"the{f}{l}", f"real{f}{l}", f"im{f}{l}",
        f"{f}{l}x", f"x{f}{l}", f"{f}xx{l}",
    ]

    for p in patterns:
        if len(p) >= 3:
            combos.add(p)
            combos.add(p + str(random.randint(1, 999)))

    return sorted(combos)

def random_usernames(count=20):
    results = set()
    styles  = ['adj_noun', 'noun_num', 'adj_num', 'adj_noun_num', 'noun_noun']

    while len(results) < count:
        style = random.choice(styles)

        if style == 'adj_noun':
            results.add(random.choice(ADJECTIVES) + random.choice(NOUNS))
        elif style == 'noun_num':
            results.add(random.choice(NOUNS) + str(random.randint(10, 9999)))
        elif style == 'adj_num':
            results.add(random.choice(ADJECTIVES) + str(random.randint(10, 9999)))
        elif style == 'adj_noun_num':
            results.add(random.choice(ADJECTIVES) + random.choice(NOUNS) + str(random.randint(1, 99)))
        elif style == 'noun_noun':
            results.add(random.choice(NOUNS) + random.choice(NOUNS))

    return sorted(results)

def run():
    while True:
        print(f"\n{CYAN}{BOLD}  Username Generator{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")
        print(f"  {YELLOW}[1]{RESET} {WHITE}Generate from real name{RESET}")
        print(f"  {YELLOW}[2]{RESET} {WHITE}Generate random usernames{RESET}")
        print(f"  {YELLOW}[3]{RESET} {WHITE}Generate from keywords{RESET}")
        print(f"  {YELLOW}[0]{RESET} {WHITE}Back{RESET}")
        print(f"  {BBLACK}{'─' * 40}{RESET}")

        choice = input(f"\n  {CYAN}Select: {RESET}").strip()

        if choice == '1':
            first = input(f"\n  {YELLOW}First name: {RESET}").strip()
            last  = input(f"  {YELLOW}Last name: {RESET}").strip()
            year  = input(f"  {YELLOW}Birth year (optional): {RESET}").strip()
            out   = input(f"  {YELLOW}Output file (optional): {RESET}").strip()

            if not first and not last:
                print(f"  {RED}Enter at least one name.{RESET}")
                continue

            usernames = name_to_usernames(first, last, year)

            print(f"\n  {BBLACK}{'─' * 40}{RESET}")
            for i, u in enumerate(usernames, 1):
                print(f"  {BBLACK}{i:>3}.{RESET} {WHITE}{u}{RESET}")
            print(f"  {BBLACK}{'─' * 40}{RESET}")
            print(f"  {GREEN}Total: {len(usernames)} usernames{RESET}")

            if out:
                with open(out, 'w') as f:
                    for u in usernames:
                        f.write(u + '\n')
                print(f"  {GREEN}✓ Saved to {out}{RESET}")

        elif choice == '2':
            try:
                count = int(input(f"\n  {YELLOW}How many usernames: {RESET}").strip())
            except ValueError:
                count = 20

            out  = input(f"  {YELLOW}Output file (optional): {RESET}").strip()
            names = random_usernames(count)

            print(f"\n  {BBLACK}{'─' * 40}{RESET}")
            for i, u in enumerate(names, 1):
                print(f"  {BBLACK}{i:>3}.{RESET} {WHITE}{u}{RESET}")
            print(f"  {BBLACK}{'─' * 40}{RESET}")

            if out:
                with open(out, 'w') as f:
                    for u in names:
                        f.write(u + '\n')
                print(f"  {GREEN}✓ Saved to {out}{RESET}")

        elif choice == '3':
            raw  = input(f"\n  {YELLOW}Enter keywords (comma separated): {RESET}").strip()
            out  = input(f"  {YELLOW}Output file (optional): {RESET}").strip()

            keywords = [k.strip().lower() for k in raw.split(',') if k.strip()]
            if not keywords:
                print(f"  {RED}No keywords entered.{RESET}")
                continue

            results = set()
            for kw in keywords:
                results.add(kw)
                results.add(kw + str(random.randint(1, 999)))
                results.add(kw + '_' + random.choice(NOUNS))
                results.add(random.choice(ADJECTIVES) + '_' + kw)
                results.add(kw + random.choice(NOUNS))
                for kw2 in keywords:
                    if kw != kw2:
                        results.add(kw + kw2)
                        results.add(kw + '_' + kw2)

            results = sorted(results)

            print(f"\n  {BBLACK}{'─' * 40}{RESET}")
            for i, u in enumerate(results, 1):
                print(f"  {BBLACK}{i:>3}.{RESET} {WHITE}{u}{RESET}")
            print(f"  {BBLACK}{'─' * 40}{RESET}")
            print(f"  {GREEN}Total: {len(results)} usernames{RESET}")

            if out:
                with open(out, 'w') as f:
                    for u in results:
                        f.write(u + '\n')
                print(f"  {GREEN}✓ Saved to {out}{RESET}")

        elif choice == '0':
            break

        else:
            print(f"  {RED}Invalid.{RESET}")
