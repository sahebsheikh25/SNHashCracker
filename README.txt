SNHashCracker - Smart Hash Cracker
----------------------------------

SNHashCracker is a Python-based terminal tool designed for ethical hackers and cybersecurity students to crack password hashes using smart dictionary-based attacks and AI-inspired mutations.

FEATURES:
- Supports popular hash types: MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- Cracking Modes:
  1. Basic      → Example: password
  2. Smart      → Example: password, Password, PASSWORD
  3. Aggressive → Example: Password123, 123password, password@2024, P@ssword, etc.
- Uses AI-style password mutation logic (leetspeak, suffixes, case combos)
- Spinner animation during cracking
- Highlights cracked hash and password
- Clean banner and terminal output
- Lightweight, portable, and offline

USAGE:
1. Run with Python 3:
   python3 main.py

2. Provide the following:
   - Target hash
   - Path to wordlist file (e.g., wordlist.txt)
   - Cracking mode (1, 2, or 3)

EXAMPLE:
Enter the hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Enter path to wordlist: wordlist.txt
Select mode (1/2/3): 3

RESULT:
[+] Hash cracked! 🔓
    Algorithm: MD5
    Password : password

NOTES:
- Ensure Python 3 is installed (`python3 --version`)
- Use custom or built-in wordlists (like Kali's rockyou.txt)
- Aggressive mode uses smart mutations: reverse, suffixes, leetspeak

📥 SNHashCracker – GitHub Download & Usage Manual

🔗 Step 1: Visit the Repository
   https://github.com/isaheb360/SNHashCracker

📦 Step 2: Download the Project
Option A: As ZIP
   - Click the green “Code” button
   - Select "Download ZIP"
   - Extract the ZIP file

Option B: Via Git
   git clone https://github.com/isaheb360/SNHashCracker.git
