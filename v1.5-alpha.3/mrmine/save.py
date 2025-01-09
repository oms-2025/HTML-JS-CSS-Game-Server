#!/usr/bin/env python3
log_loc= '/workspaces/coolmathgames/v1.5-alpha.3/mrmine/log.txt'
import json
import string
import time
from typing import Dict, Any, Union
from pathlib import Path
def write_log(message):
	with open(log_loc, "a") as log_file:
		message1=('Timestamp '+ str(time.time())+': '+ str(message) + "\n")
		log_file.write(message1)
class DictionaryEncryption:
    def __init__(self, caesar_shift: int = 3, vigenere_key: str = "SECRETKEY"):
        """
        Initialize encryption system with custom or default keys.
        
        Args:
            caesar_shift (int): Shift value for Caesar cipher (default: 3)
            vigenere_key (str): Key for Vigenère cipher (default: "SECRETKEY")
        """
        # Validate and set initial keys
        self.set_caesar_shift(caesar_shift)
        self.set_vigenere_key(vigenere_key)
        
        # Setup character sets
        self.alphabet = string.ascii_letters + string.digits + string.punctuation
        self.rev_alphabet = self.alphabet[::-1]
        self.char_map = str.maketrans(self.alphabet, self.rev_alphabet)

    def set_caesar_shift(self, shift: int) -> None:
        """
        Set a new Caesar cipher shift value.
        
        Args:
            shift (int): New shift value (must be a positive integer)
        
        Raises:
            ValueError: If shift is not a positive integer
        """
        if not isinstance(shift, int) or shift < 0:
            write_log("From class \'DictionaryEncryption\': Caesar shift must be a positive integer")
        self.caesar_shift = shift

    def set_vigenere_key(self, key: str) -> None:
        """
        Set a new Vigenère cipher key.
        
        Args:
            key (str): New key (must contain only letters)
        
        Raises:
            ValueError: If key is empty or contains non-letter characters
        """
        if not key or not all(c.isalpha() for c in key):
            write_log("From class \'DictionaryEncryption\': Vigenère key must be a non-empty string containing only letters")
        self.vigenere_key = key.upper()

    def get_encryption_config(self) -> Dict[str, Any]:
        """
        Get current encryption configuration.
        
        Returns:
            Dict containing current encryption settings
        """
        return {
            "caesar_shift": self.caesar_shift,
            "vigenere_key": self.vigenere_key
        }

    def caesar_encrypt(self, text: str) -> str:
        """
        Applies Caesar cipher encryption with current shift.
        """
        result = ""
        for char in text:
            if char in self.alphabet:
                idx = (self.alphabet.index(char) + self.caesar_shift) % len(self.alphabet)
                result += self.alphabet[idx]
            else:
                result += char
        return result

    def caesar_decrypt(self, text: str) -> str:
        """
        Applies Caesar cipher decryption with current shift.
        """
        result = ""
        for char in text:
            if char in self.alphabet:
                idx = (self.alphabet.index(char) - self.caesar_shift) % len(self.alphabet)
                result += self.alphabet[idx]
            else:
                result += char
        return result

    def vigenere_encrypt(self, text: str) -> str:
        """
        Applies Vigenère cipher encryption with current key.
        """
        result = ""
        key_idx = 0
        for char in text:
            if char in self.alphabet:
                key_char = self.vigenere_key[key_idx % len(self.vigenere_key)]
                shift = self.alphabet.index(key_char)
                idx = (self.alphabet.index(char) + shift) % len(self.alphabet)
                result += self.alphabet[idx]
                key_idx += 1
            else:
                result += char
        return result

    def vigenere_decrypt(self, text: str) -> str:
        """
        Applies Vigenère cipher decryption with current key.
        """
        result = ""
        key_idx = 0
        for char in text:
            if char in self.alphabet:
                key_char = self.vigenere_key[key_idx % len(self.vigenere_key)]
                shift = self.alphabet.index(key_char)
                idx = (self.alphabet.index(char) - shift) % len(self.alphabet)
                result += self.alphabet[idx]
                key_idx += 1
            else:
                result += char
        return result

    def atbash_cipher(self, text: str) -> str:
        """
        Applies Atbash cipher (reversible).
        """
        return text.translate(self.char_map)

    def encrypt_string(self, text: str) -> str:
        """
        Encrypts a string using all three ciphers in sequence.
        """
        text = self.caesar_encrypt(text)
        text = self.vigenere_encrypt(text)
        text = self.atbash_cipher(text)
        return text

    def decrypt_string(self, text: str) -> str:
        """
        Decrypts a string using all three ciphers in reverse sequence.
        """
        text = self.atbash_cipher(text)
        text = self.vigenere_decrypt(text)
        text = self.caesar_decrypt(text)
        return text

    def encrypt_dict(self, data: Dict[str, Any]) -> str:
        """
        Encrypts an entire dictionary by converting it to a string and applying encryption.
        """
        if not isinstance(data, dict):
            write_log("From class \'DictionaryEncryption\': Input must be a dictionary")
        
        # Convert dictionary to JSON string
        json_str = json.dumps(data)
        
        # Encrypt the entire string
        return self.encrypt_string(json_str)

    def decrypt_dict(self, encrypted_str: str) -> Dict[str, Any]:
        """
        Decrypts an encrypted string back into a dictionary.
        """
        try:
            # Decrypt the string
            json_str = self.decrypt_string(encrypted_str)
            
            # Parse JSON string back to dictionary
            return json.loads(json_str)
        except json.JSONDecodeError:
            write_log("From class \'DictionaryEncryption\': Failed to decode decrypted data")

def write_save(self, data: Dict[str, Any], filename: str) -> None:
    """
    Encrypts dictionary and saves it as a single encrypted string.
    """
    try:
        # Validate input
        if not isinstance(data, dict):
            write_log("From function \'write_save\': Input must be a dictionary")
        if not filename:
            write_log("From function \'write_save\': Filename cannot be empty")

        # Create directory if it doesn't exist
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        # Encrypt the entire dictionary as a single string
        encrypted_str = self.encrypt_dict(data)

        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(encrypted_str)

    except Exception as e:
        write_log(f"From function \'write_save\': Failed to write save file: {str(e)}")

def read_save(self, filename: str) -> Dict[str, Any]:
    """
    Reads and decrypts dictionary from a file containing a single encrypted string.
    """
    try:
        # Validate input
        if not filename:
            write_log("From function \'read_save\': Filename cannot be empty")

        # Check if file exists
        if not Path(filename).is_file():
            write_log(f"From function \'read_save\': Save file not found: {filename}")

        # Read encrypted string from file
        with open(filename, 'r', encoding='utf-8') as f:
            encrypted_str = f.read()

        # Decrypt the string back to dictionary
        return self.decrypt_dict(encrypted_str)

    except Exception as e:
        write_log(f"From function \'read_save\': Failed to read save file: {str(e)}")