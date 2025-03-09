import sys
import subprocess


def show_history(history):
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")

def select_from_history(history):
    while True:
        show_history(history)
        choice = input("Would you like to use the history? (Y/N) ").strip()
        
        if choice == "N" or choice == "n":
            return None
        
        if choice == "Y" or choice == "t":
            choice = input("Select String: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(history):
                return history[int(choice) - 1]
        
        print("Invalid selection. Try again.")

def main():
    history = []
    
    encryptor = subprocess.Popen(["python", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    while True:
        print("Commands: password, encrypt, decrypt, history, quit")
        command = input("Enter command: ").strip().upper()
        
        if command == "QUIT":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            encryptor.stdin.close()
            encryptor.wait()
            print("Exiting...")
            break
        
        elif command == "PASSWORD":
            selected = select_from_history(history)
            if selected is None:
                password = input("Enter new password: ").strip().upper()
                encryptor.stdin.write(f"PASSKEY {password}\n")
                encryptor.stdin.flush()
            else:
                encryptor.stdin.write(f"PASSKEY {selected}\n")
                encryptor.stdin.flush()
        
        elif command == "ENCRYPT" or command == "DECRYPT":
            selected = select_from_history(history)
            if selected is None:
                text = input("Enter text to process: ").strip().upper()
                history.append(text)
            else:
                text = selected
            
            if command == "ENCRYPT":
                encryptor.stdin.write(f"ENCRYPT {text}\n")
            elif command == "DECRYPT":
                encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()

            result = encryptor.stdout.readline().strip()
            encryptor.stdout.flush()
            
            print(result)
            
            if result.startswith("RESULT"):
                result_parts = result.split(maxsplit=1)
                if len(result_parts) > 1:
                    history.append(result_parts[1])

        
        elif command == "HISTORY":
            show_history(history)
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
