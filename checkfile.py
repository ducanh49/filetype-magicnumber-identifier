import sys
import binascii
import os

#databaze MN
MAGIC_NUMBERS = {
    "FFD8FFE0": "jpeg",
    "FFD8FFE1": "jpeg",
    "89504E47": "png",
    "47494638": "gif",
    "25504446": "pdf",
    "504B0304": "zip",  
    "4D5A9000": "exe", 
}

def get_magic_number(path, length=4):
    #vrati prvnich N bajtu (4)
    with open(path, "rb") as f:
        data = f.read(length)
    return binascii.hexlify(data).upper().decode()

def guess_filetype(hex_magic):
    #Zjisti filetype podle magic number - pokud MN neni v db vrati "unknown"
    for magic, filetype in MAGIC_NUMBERS.items():
        if hex_magic.startswith(magic):
            return filetype
    return "unknown"

def main():
    if len(sys.argv) < 2:
        print("Pouziti: python filecheck.py soubor.jpg")
        return

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Soubor neexistuje!")
        return

    # magic number
    hex_magic = get_magic_number(file_path, 4)
    detected_type = guess_filetype(hex_magic)

    # pripona
    extension = os.path.splitext(file_path)[1].replace(".", "").lower()

    print(f"\nSoubor: {file_path}")
    print(f"Magic number: {hex_magic}")
    print(f"Zjisteny typ: {detected_type}")
    print(f"Pripona: {extension}")

    # kontrola shody
    if detected_type == "unknown":
        print("\nPOZOR! Soubor ma neznamy magic number! Podezrele.")
    elif detected_type != extension:
        print("\nPOZOR! Pripona neodpovida typu souboru!")
        print(">>muze se jednat o prejmenovany malware")
    else:
        print("\nTyp souboru odpovida pripone - Pravdepodobne OK")

if __name__ == "__main__":
    main()
