#!/usr/bin/env python3
log_loc= '/workspaces/coolmathgames/v1.5-alpha.3/mrmine/log.txt'
#!/usr/bin/env python3
#!/usr/bin/env python3

import json
import string
from typing import Dict, Any, Union, List, Tuple
from pathlib import Path

# Module-level variables (previously class attributes)
caesar_shift: int = 3
vigenere_key: str = "SECRETKEY"
alphabet: str = string.ascii_letters + string.digits + string.punctuation
rev_alphabet: str = alphabet[::-1]
char_map: str = str.maketrans(alphabet, rev_alphabet)

def set_caesar_shift(shift: int) -> None:
    """
    Set a new Caesar cipher shift value.
    
    Args:
        shift (int): New shift value (must be a positive integer)
    
    Raises:
        ValueError: If shift is not a positive integer
    """
    global caesar_shift
    if not isinstance(shift, int) or shift < 0:
        raise ValueError("Caesar shift must be a positive integer")
    caesar_shift = shift

def set_vigenere_key(key: str) -> None:
    """
    Set a new Vigenère cipher key.
    
    Args:
        key (str): New key (must contain only letters)
    
    Raises:
        ValueError: If key is empty or contains non-letter characters
    """
    global vigenere_key
    if not key or not all(c.isalpha() for c in key):
        raise ValueError("Vigenère key must be a non-empty string containing only letters")
    vigenere_key = key.upper()

def get_encryption_config() -> Dict[str, Any]:
    """
    Get current encryption configuration.
    
    Returns:
        Dict containing current encryption settings
    """
    return {
        "caesar_shift": caesar_shift,
        "vigenere_key": vigenere_key
    }

def caesar_encrypt(text: str) -> str:
    """
    Applies Caesar cipher encryption with current shift.
    """
    result = ""
    for char in text:
        if char in alphabet:
            idx = (alphabet.index(char) + caesar_shift) % len(alphabet)
            result += alphabet[idx]
        else:
            result += char
    return result

def caesar_decrypt(text: str) -> str:
    """
    Applies Caesar cipher decryption with current shift.
    """
    result = ""
    for char in text:
        if char in alphabet:
            idx = (alphabet.index(char) - caesar_shift) % len(alphabet)
            result += alphabet[idx]
        else:
            result += char
    return result

def vigenere_encrypt(text: str) -> str:
    """
    Applies Vigenère cipher encryption with current key.
    """
    result = ""
    key_idx = 0
    for char in text:
        if char in alphabet:
            key_char = vigenere_key[key_idx % len(vigenere_key)]
            shift = alphabet.index(key_char)
            idx = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[idx]
            key_idx += 1
        else:
            result += char
    return result

def vigenere_decrypt(text: str) -> str:
    """
    Applies Vigenère cipher decryption with current key.
    """
    result = ""
    key_idx = 0
    for char in text:
        if char in alphabet:
            key_char = vigenere_key[key_idx % len(vigenere_key)]
            shift = alphabet.index(key_char)
            idx = (alphabet.index(char) - shift) % len(alphabet)
            result += alphabet[idx]
            key_idx += 1
        else:
            result += char
    return result

def atbash_cipher(text: str) -> str:
    """
    Applies Atbash cipher (reversible).
    """
    return text.translate(char_map)

def encrypt_string(text: str) -> str:
    """
    Encrypts a string using all three ciphers in sequence.
    """
    text = caesar_encrypt(text)
    text = vigenere_encrypt(text)
    text = atbash_cipher(text)
    return text

def decrypt_string(text: str) -> str:
    """
    Decrypts a string using all three ciphers in reverse sequence.
    """
    text = atbash_cipher(text)
    text = vigenere_decrypt(text)
    text = caesar_decrypt(text)
    return text

def _convert_tuples_to_lists(data: Any) -> Any:
    """
    Recursively converts tuples to lists in nested structures.
    """
    if isinstance(data, dict):
        return {k: _convert_tuples_to_lists(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple)):
        return [_convert_tuples_to_lists(item) for item in data]
    return data

def encrypt_dict(data: Dict[str, Any]) -> str:
    """
    Encrypts an entire dictionary by converting it to a string and applying encryption.
    
    Args:
        data (Dict[str, Any]): Dictionary to encrypt
        
    Returns:
        str: Encrypted string
        
    Raises:
        ValueError: If input is not a dictionary
        TypeError: If dictionary contains non-serializable content
    """
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    try:
        # Convert tuples to lists for JSON serialization
        processed_data = _convert_tuples_to_lists(data)
        # Convert dictionary to JSON string
        json_str = json.dumps(processed_data)
        # Encrypt the entire string
        return encrypt_string(json_str)
    except TypeError as e:
        raise ValueError(f"Failed to serialize dictionary to JSON: {str(e)}")

def decrypt_dict(encrypted_str: str) -> Dict[str, Any]:
    """
    Decrypts an encrypted string back into a dictionary.
    
    Args:
        encrypted_str (str): Encrypted string to decrypt
        
    Returns:
        Dict[str, Any]: Decrypted dictionary
        
    Raises:
        ValueError: If decryption or JSON parsing fails
    """
    try:
        # Decrypt the string
        json_str = decrypt_string(encrypted_str)
        
        # Parse JSON string back to dictionary
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse decrypted data as JSON: {str(e)}")
    except Exception as e:
        raise ValueError(f"Failed to decrypt data: {str(e)}")

def write_save(data: Dict[str, Any], filename: str) -> None:
    """
    Encrypts dictionary and saves it as a single encrypted string.
    
    Args:
        data (Dict[str, Any]): Dictionary to encrypt and save
        filename (str): Path to save file
        
    Raises:
        ValueError: If input validation fails
        IOError: If file operations fail
    """
    try:
        # Validate input
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary")
        if not filename:
            raise ValueError("Filename cannot be empty")

        # Create directory if it doesn't exist
        save_path = Path(filename)
        save_path.parent.mkdir(parents=True, exist_ok=True)

        # Encrypt the entire dictionary as a single string
        encrypted_str = encrypt_dict(data)

        # Save to file
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(encrypted_str)

    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")
    except IOError as e:
        raise IOError(f"Failed to write save file '{filename}': {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while saving file: {str(e)}")

def read_save(filename: str) -> Dict[str, Any]:
    """
    Reads and decrypts dictionary from a file containing a single encrypted string.
    
    Args:
        filename (str): Path to encrypted save file
        
    Returns:
        Dict[str, Any]: Decrypted dictionary
        
    Raises:
        FileNotFoundError: If save file doesn't exist
        IOError: If file operations fail
        ValueError: If decryption or parsing fails
    """
    try:
        # Validate input
        if not filename:
            raise ValueError("Filename cannot be empty")

        # Check if file exists
        save_path = Path(filename)
        if not save_path.is_file():
            raise FileNotFoundError(f"Save file not found: {filename}")

        # Read encrypted string from file
        with open(save_path, 'r', encoding='utf-8') as f:
            encrypted_str = f.read().strip()

        if not encrypted_str:
            raise ValueError("Save file is empty")

        # Decrypt the string back to dictionary
        return decrypt_dict(encrypted_str)

    except FileNotFoundError:
        raise FileNotFoundError(f"Save file '{filename}' does not exist")
    except IOError as e:
        raise IOError(f"Failed to read save file '{filename}': {str(e)}")
    except ValueError as e:
        raise ValueError(f"Failed to decrypt save file: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading save file: {str(e)}")