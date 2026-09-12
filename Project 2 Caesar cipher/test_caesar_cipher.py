import unittest
from caesar_cipher import encrypt, decrypt, vigenere_encrypt, vigenere_decrypt


class TestCaesarCipher(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(encrypt("ABC", 3), "DEF")
        self.assertEqual(decrypt("DEF", 3), "ABC")

    def test_wraparound(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")
        self.assertEqual(decrypt("ABC", 3), "XYZ")

    def test_case_preserved(self):
        self.assertEqual(encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_non_alpha_untouched(self):
        text = "Room 101, Floor 2!"
        cipher = encrypt(text, 4)
        original_non_alpha = [c for c in text if not c.isalpha()]
        cipher_non_alpha = [c for c in cipher if not c.isalpha()]
        self.assertEqual(original_non_alpha, cipher_non_alpha)

    def test_round_trip(self):
        text = "The quick brown fox jumps over the lazy dog."
        for key in range(0, 26):
            self.assertEqual(decrypt(encrypt(text, key), key), text)

    def test_negative_and_large_keys(self):
        self.assertEqual(encrypt("abc", -1), encrypt("abc", 25))
        self.assertEqual(encrypt("abc", 29), encrypt("abc", 3))


class TestVigenereCipher(unittest.TestCase):
    def test_round_trip(self):
        text = "Meet me at midnight!"
        key = "shield"
        cipher = vigenere_encrypt(text, key)
        self.assertEqual(vigenere_decrypt(cipher, key), text)

    def test_non_alpha_untouched(self):
        cipher = vigenere_encrypt("A, B!", "key")
        self.assertIn(",", cipher)
        self.assertIn("!", cipher)


if __name__ == "__main__":
    unittest.main()
