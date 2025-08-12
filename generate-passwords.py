#!/usr/bin/env python3
"""
generate_passwords.py
Simple local script to generate sample passwords and estimate rough entropy.
For educational use only.
"""

import secrets
import string
import math

def estimate_entropy(password):
    """
    Estimate bits of entropy by approximating charset size.
    This is a rough estimator (educational) and does not replace formal entropy analysis.
    """
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    if charset == 0:
        return 0.0
    return len(password) * math.log2(charset)

def make_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def make_passphrase(word_list, words=4, separator='-'):
    """
    Build a passphrase by choosing random words from a list.
    Provide your own wordlist file or small sample.
    """
    return separator.join(secrets.choice(word_list) for _ in range(words))

if __name__ == '__main__':
    # Example usage:
    samples = {
        'weak_example': 'password123',
        'moderate_example': 'BlueHouse2024',
        'random_12': make_random_password(12),
        'random_20': make_random_password(20),
    }

    print("Sample passwords and estimated entropy (bits):\n")
    for name, pwd in samples.items():
        print(f"{name}: {pwd}  |  length: {len(pwd)}  |  entropy: {estimate_entropy(pwd):.1f} bits")
