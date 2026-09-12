# Project 2: Basic Encryption & Decryption

Caesar cipher implementation built for the **DecodeLabs Cyber Security Internship** — Batch 2026, Project 2 (Industrial Training Kit).

## Overview

This project implements a classic **Caesar cipher** — a mono-alphabetic substitution cipher that shifts each letter by a fixed number of positions in the alphabet. It follows the Input → Process → Output (IPO) model:

```
Plaintext  --[ Algorithm + Key ]-->  Ciphertext
```

Encryption and decryption use the same symmetric key (the shift value):

```
E(x) = (x - base + key) % 26 + base    # encrypt
D(x) = (x - base - key) % 26 + base    # decrypt
```

where `x` is a letter's ASCII code and `base` is `65` ('A') or `97` ('a'), so letter case is always preserved.

## Features

- **Encrypt** any text using a configurable integer shift key
- **Decrypt** ciphertext back to the original plaintext
- **Case preserved** — uppercase and lowercase are shifted independently
- **Edge cases handled** — spaces, digits, and punctuation pass through unchanged
- **Any key works** — negative keys and keys larger than 26 are normalized with modulo arithmetic
- **Bonus:** a **Vigenère cipher** (polyalphabetic, multi-letter key) is included as a stronger alternative, as suggested in the training deck

## Why Caesar Alone Isn't Enough

The Caesar cipher is a good teaching tool for the mechanics of encryption, but it's cryptographically weak:

- **Tiny key space** — only 25 possible shifts, so it can be brute-forced instantly
- **Pattern preservation** — the shifted ciphertext keeps the same letter-frequency distribution as the original language, making it vulnerable to frequency analysis

This is why real-world systems use modern algorithms like **AES-256**, which add confusion and diffusion through much larger keys and XOR-based transformations. The Vigenère cipher included here is a step in that direction — a different shift per character, driven by a repeating keyword — but it's still not production-grade encryption.

## Files

| File | Purpose |
|---|---|
| `caesar_cipher.py` | Core encrypt/decrypt logic, plus the Vigenère bonus and a CLI demo |
| `test_caesar_cipher.py` | Unit tests covering basic shifts, wraparound, case handling, non-alpha characters, and round-trips |

## Usage

### Run the interactive demo

```bash
python3 caesar_cipher.py
```

You'll be prompted for text and a shift key, then shown the encrypted and decrypted output side by side.

### Use as a module

```python
from caesar_cipher import encrypt, decrypt

cipher_text = encrypt("Attack at dawn!", 3)
print(cipher_text)          # Dwwdfn dw gdzq!

plain_text = decrypt(cipher_text, 3)
print(plain_text)           # Attack at dawn!
```

### Bonus: Vigenère cipher

```python
from caesar_cipher import vigenere_encrypt, vigenere_decrypt

cipher_text = vigenere_encrypt("Attack at dawn!", "shield")
plain_text = vigenere_decrypt(cipher_text, "shield")
```

### Run tests

```bash
python3 -m unittest test_caesar_cipher.py -v
```

## Example

```
Plaintext:  Attack at dawn!
Key:        3
Encrypted:  Dwwdfn dw gdzq!
Decrypted:  Attack at dawn!
Match:      True
```

## Requirements

- Python 3.7+ (no external dependencies)

## Author

Ahmad — Freelance WordPress/WooCommerce developer, aspiring cybersecurity analyst.

## License

For educational use as part of the DecodeLabs internship program.
