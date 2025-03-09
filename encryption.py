import sys

def vigenere_encrypt(text, key):
    encrypted_text = []
    key_length = len(key)
    
    for i, char in enumerate(text):
        shift = ord(key[i % key_length]) - ord('A')
        encrypted_text.append(chr(((ord(char) - ord('A') + shift) % 26) + ord('A')))
    
    return "".join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key_length = len(key)
    
    for i, char in enumerate(text):
        shift = ord(key[i % key_length]) - ord('A')
        decrypted_text.append(chr(((ord(char) - ord('A') - shift) % 26) + ord('A')))
    
    return "".join(decrypted_text)

def main():
    passkey = None
    
    while True:
        try:
            command_line = input().strip()
            if not command_line:
                continue
            
            parts = command_line.split(maxsplit=1)
            command = parts[0]
            argument = parts[1] if len(parts) > 1 else None
            
            if command == "QUIT":
                break
            
            elif command == "PASSKEY":
                if argument is None:
                    print("ERROR No passkey provided")
                else:
                    passkey = argument
            
            elif command == "ENCRYPT":
                if passkey is None:
                    print("ERROR Password not set")
                elif argument is None:
                    print("ERROR No text to encrypt")
                else:
                    print("RESULT", vigenere_encrypt(argument, passkey))
            
            elif command == "DECRYPT":
                if passkey is None:
                    print("ERROR Password not set")
                elif argument is None:
                    print("ERROR No text to decrypt")
                else:
                    print("RESULT", vigenere_decrypt(argument, passkey))
            
            else:
                print("ERROR Unknown command")

                
        except EOFError:
            break

if __name__ == "__main__":
    main()