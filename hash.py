
import hashlib
import time
import sys

# Banner
def show_banner():
    print(r"""
  ____  _   _ _           _       _            _             
 / ___|| \ | (_)_ __   __| | ___ | | ___   ___| | _____ _ __ 
 \___ \|  \| | | '_ \ / _` |/ _ \| |/ _ \ / __| |/ / _ \ '__|
  ___) | |\  | | | | | (_| | (_) | | (_) | (__|   <  __/ |   
 |____/|_| \_|_|_| |_|\__,_|\___/|_|\___/ \___|_|\_\___|_|   

             🔓 SNHashCracker - Smart Hash Cracker
    """)

# Supported algorithms
supported_algos = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512
}

# AI-based smart variant generator
def ai_generate_variants(word):
    return list(set([
        word,
        word.capitalize(),
        word.upper(),
        word[::-1],
        word + "123",
        "123" + word,
        word + "@2024",
        word + "!",
        word + word,
        word.replace("a", "@").replace("s", "$"),
        word.capitalize() + "123",
        word.upper() + "@",
    ]))

def generate_variants(word, mode="smart"):
    if mode == "basic":
        return [word]
    elif mode == "smart":
        return [word, word.capitalize(), word.upper()]
    elif mode == "aggressive":
        return ai_generate_variants(word)
    else:
        return [word]

# Spinner animation
def spinner():
    while True:
        for cursor in '|/-\\':
            yield cursor

def crack_any_hash(target_hash, wordlist_path, mode="smart"):
    print(f"\n[*] Cracking hash: {target_hash} | Mode: {mode.upper()}")
    found = False
    spinner_gen = spinner()
    attempts = 0

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                for variant in generate_variants(word, mode):
                    if found:
                        break
                    # Show spinner every 5 attempts
                    if attempts % 5 == 0:
                        sys.stdout.write(f"\r[~] Cracking {next(spinner_gen)} Trying: {variant}   ")
                        sys.stdout.flush()
                    attempts += 1

                    for algo_name, algo_func in supported_algos.items():
                        hashed_variant = algo_func(variant.encode()).hexdigest()
                        if hashed_variant == target_hash.lower():
                            print("\n[+] Hash cracked! 🔓")
                            print(f"    Algorithm: {algo_name.upper()}")
                            print(f"    Password : {variant}")
                            found = True
                            break
                if found:
                    break
        if not found:
            print("\n[-] Sorry, no match found.")
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")

    print("\n[✔] Finished - Powered by SNHashCracker 🔓 (Smart Hash Cracker)")

# === Main Program ===
if __name__ == "__main__":
    show_banner()
    input_hash = input("Enter the hash to crack: ").strip()
    wordlist = input("Enter path to wordlist: ").strip()

    print("""
Choose cracking mode:
[1] Basic      → Example: password
[2] Smart      → Example: password, Password, PASSWORD
[3] Aggressive → Example: Password123, 123password, password@2024
     (Includes AI-based mutations like leetspeak, reversals, symbols)
""")

    mode_input = input("Select mode (1/2/3): ").strip()

    mode_map = {
        "1": "basic",
        "2": "smart",
        "3": "aggressive"
    }
    mode = mode_map.get(mode_input, "smart")

    crack_any_hash(input_hash, wordlist, mode)
