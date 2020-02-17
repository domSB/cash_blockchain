import hashlib
import os
import argparse

def main():
    parser = argparse.ArgumentParser('Blockchain für die Kassendaten erstellen')
    parser.add_argument('path', type=str, help='relativer Pfad zum Ordner mit den Dateien angeben')

    args = parser.parse_args()

    print(os.listdir(args.path))
    datei_namen = os.listdir(args.path)
    for datei_name in datei_namen:
        with open(os.path.join(args.path, datei_name)) as file:
            inhalt = file.read().encode()
            file_hash = hashlib.sha256(inhalt).hexdigest()
            print(file_hash)

if __name__ == '__main__':
    main()