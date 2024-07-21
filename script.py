import csv
from datetime import datetime

# Dizionario per normalizzare i nomi degli store
store_alias = {
    "despar": ["supermercato despar", "despar"],
    "coop": ["supermercato coop", "coop"],
    # Aggiungi altri store e varianti qui
}

# Funzione per normalizzare il nome dello store
def normalizza_store(store):
    store = store.lower()
    for chiave, alias in store_alias.items():
        if store in alias:
            return chiave
    return store

# Funzione per aggiungere una transazione (entrata o uscita)
def aggiungi_transazione(data, tipo, descrizione, importo, store):
    store_normalizzato = normalizza_store(store)
    with open('finanze.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, tipo, descrizione, importo, store_normalizzato])

# Funzione per visualizzare il bilancio attuale
def visualizza_bilancio():
    bilancio = 0
    with open('finanze.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta la riga di intestazione
        for row in reader:
            tipo, importo = row[1], float(row[3])
            if tipo == 'entrata':
                bilancio += importo
            elif tipo == 'uscita':
                bilancio -= importo
    return bilancio

# Funzione per caricare i dati dal file CSV
def carica_dati():
    try:
        with open('finanze.csv', mode='r') as file:
            reader = csv.reader(file)
            if not list(reader):  # Se il file è vuoto, scrive l'intestazione
                with open('finanze.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['data', 'tipo', 'descrizione', 'importo', 'store'])
    except FileNotFoundError:
        with open('finanze.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['data', 'tipo', 'descrizione', 'importo', 'store'])

# Funzione principale per il sistema di gestione
def gestione_finanze():
    print("Sistema di gestione delle finanze")
    while True:
        print("\n1. Aggiungi entrata")
        print("2. Aggiungi uscita")
        print("3. Visualizza bilancio")
        print("4. Esci")
        scelta = input("Seleziona un'opzione: ")

        if scelta == '1':
            data = input("Data dell'entrata (YYYY-MM-DD): ")
            descrizione = input("Descrizione dell'entrata: ")
            importo = float(input("Importo dell'entrata: "))
            store = input("Luogo di entrata: ")
            aggiungi_transazione(data, 'entrata', descrizione, importo, store)
        elif scelta == '2':
            data = input("Data dell'uscita (YYYY-MM-DD): ")
            descrizione = input("Descrizione dell'uscita: ")
            importo = float(input("Importo dell'uscita: "))
            store = input("Luogo di uscita: ")
            aggiungi_transazione(data, 'uscita', descrizione, importo, store)
        elif scelta == '3':
            bilancio = visualizza_bilancio()
            print(f"Bilancio attuale: {bilancio} €")
        elif scelta == '4':
            print("Uscita dal sistema.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Caricare i dati al primo avvio del programma
carica_dati()

# Avviare il sistema di gestione
gestione_finanze()
