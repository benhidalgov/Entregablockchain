import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY_FILE = "key.bin"
KEY_SIZE = 32  # 256 bits para máxima seguridad

def generate_key():
    key = get_random_bytes(KEY_SIZE)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print(f"[+] Llave generada y guardada en {KEY_FILE}")

def load_key():
 
    if not os.path.exists(KEY_FILE):
        print("[-] Error: No se encontró el archivo de llave (key.bin).")
        sys.exit(1)
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(file_path):
    key = load_key()
    cipher = AES.new(key, AES.MODE_EAX)
    
    with open(file_path, "rb") as f:
        data = f.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    with open("cifrado.bin", "wb") as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
    print("[+] Archivo cifrado con éxito. Resultado en 'cifrado.bin'.")

def decrypt_file(encrypted_file):
    key = load_key()
    
    with open(encrypted_file, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
        
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        print("[+] Descifrado exitoso. Contenido original:")
        print("-" * 20)
        print(data.decode('utf-8'))
        print("-" * 20)
    except ValueError:
        print("[-] Error: La llave es incorrecta o el archivo ha sido manipulado.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python crypto_tool.py [genkey | encrypt <file> | decrypt <file>]")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "genkey":
        generate_key()
    elif command == "encrypt" and len(sys.argv) == 3:
        encrypt_file(sys.argv[2])
    elif command == "decrypt" and len(sys.argv) == 3:
        decrypt_file(sys.argv[2])
    else:
        print("Comando no reconocido o faltan argumentos.")