"""
Project 2: Basic Encryption & Decryption
DecodeLabs Cyber Security Internship

Implements a Caesar cipher (mono-alphabetic shift cipher) using the
IPO model taught in the training deck:

    Encryption:  E(x) = (x - base + key) % 26 + base
    Decryption:  D(x) = (x - base - key) % 26 + base

Where 'x' is the ASCII code of a letter and 'base' is 65 ('A') for
uppercase letters or 97 ('a') for lowercase letters. Non-alphabetic
characters (spaces, digits, punctuation) are passed through unchanged
so the message structure stays readable.
"""

ALPHABET_SIZE = 26


def _shift_char(char: str, key: int, encrypt: bool = True) -> str:
    """Shift a single character by `key` positions, wrapping with modulo 26.

    Uppercase and lowercase letters are handled with their own base
    (65 for 'A', 97 for 'a') so case is preserved. Anything that is not
    a letter (spaces, punctuation, numbers) is returned unchanged.
    """
    if not char.isalpha():
        return char

    base = ord('A') if char.isupper() else ord('a')
    direction = key if encrypt else -key

    shifted = (ord(char) - base + direction) % ALPHABET_SIZE
    return chr(shifted + base)


def encrypt(plaintext: str, key: int) -> str:
    """Encrypt plaintext with a Caesar cipher shift of `key`."""
    key = key % ALPHABET_SIZE
    return ''.join(_shift_char(ch, key, encrypt=True) for ch in plaintext)


def decrypt(ciphertext: str, key: int) -> str:
    """Decrypt ciphertext that was encrypted with the same `key`."""
    key = key % ALPHABET_SIZE
    return ''.join(_shift_char(ch, key, encrypt=False) for ch in ciphertext)


# ---------------------------------------------------------------------------
# Bonus: Vigenère cipher (polyalphabetic) - mentioned in the deck as a
# stretch goal for a stronger, less pattern-preserving cipher than Caesar.
# ---------------------------------------------------------------------------

def _vigenere_shift(char: str, key_char: str, encrypt: bool = True) -> str:
    if not char.isalpha():
        return char

    base = ord('A') if char.isupper() else ord('a')
    key_shift = ord(key_char.lower()) - ord('a')
    direction = key_shift if encrypt else -key_shift

    shifted = (ord(char) - base + direction) % ALPHABET_SIZE
    return chr(shifted + base)


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Encrypt plaintext with a Vigenère cipher using a repeating text key."""
    if not key.isalpha():
        raise ValueError("Vigenère key must contain only letters.")

    result = []
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():
            key_char = key[key_index % len(key)]
            result.append(_vigenere_shift(ch, key_char, encrypt=True))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt ciphertext that was encrypted with the same Vigenère key."""
    if not key.isalpha():
        raise ValueError("Vigenère key must contain only letters.")

    result = []
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            key_char = key[key_index % len(key)]
            result.append(_vigenere_shift(ch, key_char, encrypt=False))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


# ---------------------------------------------------------------------------
# Demo / CLI
# ---------------------------------------------------------------------------

def _run_demo():
    print("=" * 50)
    print("  DecodeLabs - Project 2: Basic Encryption & Decryption")
    print("=" * 50)

    user_text = input("\nEnter text to encrypt: ") or "Attack at dawn!"
    while True:
        raw_key = input("Enter shift key (integer, e.g. 3): ") or "3"
        try:
            key = int(raw_key)
            break
        except ValueError:
            print("Please enter a whole number for the shift key.")

    cipher_text = encrypt(user_text, key)
    recovered_text = decrypt(cipher_text, key)

    print("\n--- Caesar Cipher ---")
    print(f"Plaintext:  {user_text}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {cipher_text}")
    print(f"Decrypted:  {recovered_text}")
    print(f"Match:      {user_text == recovered_text}")

    print("\n--- Bonus: Vigenère Cipher (multi-letter key) ---")
    v_key = "shield"
    v_cipher = vigenere_encrypt(user_text, v_key)
    v_plain = vigenere_decrypt(v_cipher, v_key)
    print(f"Key:        {v_key}")
    print(f"Encrypted:  {v_cipher}")
    print(f"Decrypted:  {v_plain}")


if __name__ == "__main__":
    _run_demo()
