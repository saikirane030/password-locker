import sys
import pyperclip

PASSWORDS = {
    'email': 'hittu@abc',
    'blog': 'neha@123',
    'luggage': 'Sonia_45'
}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for '{account}' copied to clipboard.")
else:
    print(f"There is no account named '{account}'.")