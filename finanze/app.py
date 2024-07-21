from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)

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

# Funzione per leggere tutte le transazioni dal file CSV
def leggi_transazioni():
    transazioni = []
    with open('finanze.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta la riga di intestazione
        for row in reader:
            if len(row) == 6:  # Assicurarsi che la riga abbia 6 colonne
                transazioni.append({
                    'data': row[0],
                    'tipo': row[1],
                    'descrizione': row[2],
                    'importo': float(row[3]),
                    'store': row[4],
                    'quantità': int(row[5]) if row[5] else 1  # Default quantità to 1 if missing
                })
    return transazioni

# Funzione per filtrare transazioni per data
def filtra_transazioni_per_data(transazioni, start_date, end_date):
    transazioni_filtrate = []
    for t in transazioni:
        data_transazione = datetime.strptime(t['data'], '%Y-%m-%d')
        if start_date <= data_transazione <= end_date:
            transazioni_filtrate.append(t)
    return transazioni_filtrate

# Funzione per calcolare il saldo attuale
def calcola_saldo(transazioni):
    saldo = 0
    for transazione in transazioni:
        if transazione['tipo'] == 'entrata':
            saldo += transazione['importo']
        elif transazione['tipo'] == 'uscita':
            saldo -= transazione['importo']
    return saldo

# Funzione per preparare i dati per i grafici
def prepara_dati_grafici(transazioni):
    entrate = sum(t['importo'] for t in transazioni if t['tipo'] == 'entrata')
    uscite = sum(t['importo'] for t in transazioni if t['tipo'] == 'uscita')

    pezzi_per_store = defaultdict(int)
    for t in transazioni:
        if t['tipo'] == 'uscita':
            pezzi_per_store[t['store']] += t['quantità']

    return {
        'entrate': entrate,
        'uscite': uscite,
        'pezzi_per_store': dict(pezzi_per_store)
    }

# Funzione per calcolare pezzi acquistati per mese
def calcola_pezzi_per_mese(transazioni):
    pezzi_per_mese = defaultdict(lambda: defaultdict(int))
    for t in transazioni:
        if t['tipo'] == 'uscita':
            mese = datetime.strptime(t['data'], '%Y-%m-%d').strftime('%Y-%m')
            pezzi_per_mese[t['descrizione']][mese] += t['quantità']
    return pezzi_per_mese

# Funzione per calcolare il negozio con il prezzo minore
def calcola_negozio_prezzo_minore(transazioni):
    prezzo_minore = defaultdict(lambda: {'store': '', 'prezzo': float('inf')})
    for t in transazioni:
        if t['tipo'] == 'uscita':
            if t['importo'] < prezzo_minore[t['descrizione']]['prezzo']:
                prezzo_minore[t['descrizione']]['prezzo'] = t['importo']
                prezzo_minore[t['descrizione']]['store'] = t['store']
    return prezzo_minore

# Funzione per calcolare la variazione percentuale
def calcola_variazione_percentuale(transazioni_correnti, transazioni_precedenti):
    spese_correnti = sum(t['importo'] for t in transazioni_correnti if t['tipo'] == 'uscita')
    spese_precedenti = sum(t['importo'] for t in transazioni_precedenti if t['tipo'] == 'uscita')
    if spese_precedenti == 0:
        return 0
    variazione = ((spese_correnti - spese_precedenti) / spese_precedenti) * 100
    return variazione

@app.route('/', methods=['GET', 'POST'])
def index():
    transazioni = leggi_transazioni()
    oggi = datetime.today()
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not start_date or not end_date:
        # Default: ultimo mese
        start_date = (oggi - timedelta(days=30)).strftime('%Y-%m-%d')
        end_date = oggi.strftime('%Y-%m-%d')

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    transazioni_filtrate = filtra_transazioni_per_data(transazioni, start_date, end_date)

    # Per la variazione percentuale rispetto al periodo corrispondente
    if (end_date - start_date).days > 30:
        start_date_precedente = start_date - timedelta(days=365)
        end_date_precedente = end_date - timedelta(days=365)
    else:
        start_date_precedente = start_date - timedelta(days=30)
        end_date_precedente = end_date - timedelta(days=30)

    transazioni_precedenti = filtra_transazioni_per_data(transazioni, start_date_precedente, end_date_precedente)

    saldo = calcola_saldo(transazioni_filtrate)
    dati_grafici = prepara_dati_grafici(transazioni_filtrate)
    pezzi_per_mese = calcola_pezzi_per_mese(transazioni_filtrate)
    prezzo_minore = calcola_negozio_prezzo_minore(transazioni_filtrate)
    variazione_percentuale = calcola_variazione_percentuale(transazioni_filtrate, transazioni_precedenti)

    return render_template(
        'index.html',
        transazioni=transazioni_filtrate,
        saldo=saldo,
        dati_grafici=dati_grafici,
        pezzi_per_mese=pezzi_per_mese,
        prezzo_minore=prezzo_minore,
        variazione_percentuale=variazione_percentuale,
        start_date=start_date.strftime('%Y-%m-%d'),
        end_date=end_date.strftime('%Y-%m-%d')
    )

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    data = request.form['data']
    tipo = request.form['tipo']
    descrizione = request.form['descrizione']
    importo = float(request.form['importo'])
    store = normalizza_store(request.form['store'])
    quantità = int(request.form['quantità']) if request.form['quantità'] else 1
    
    with open('finanze.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, tipo, descrizione, importo, store, quantità])
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
