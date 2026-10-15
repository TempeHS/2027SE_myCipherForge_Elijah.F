"""Test Phase 3 (password-dependent variable shift).

Run from the project root with:  python tests/test_phase3.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase3_encrypt, phase3_decrypt

# --- Test 1: Correct password round-trips ---
key = {"password": "DRAGON"}
message = "Hello World!"
print(f"Original: {message}")

encrypted = phase3_encrypt(message, key)
print(f"Encrypted: {encrypted}")

decrypted = phase3_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
print(f"Match: {decrypted == message}")

# --- Test 2: WRONG password produces garbage ---
print("\n--- Wrong password test ---")
key_dragon = {"password": "BIGMAN"}
encrypted = phase3_encrypt("The one secret", key_dragon)

key_unicorn = {"password": "HONK"}
wrong_decrypt = phase3_decrypt(encrypted, key_unicorn)

print(f"Encrypted with BIGMAN:    {encrypted}")
print(f"Decrypted with HONK:   {wrong_decrypt}")
print("Wrong password = garbage!")

# --- Test 3: Different passwords give different ciphertexts ---
print("\n--- Same message, different passwords ---")
for pw in ("cat", "CAT", "DOG", "password123"):
    enc = phase3_encrypt("Same message", {"password": pw})
    print(f"Password '{pw}': {enc}")
