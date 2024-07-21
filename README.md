# Gestione Entrate e Uscite

Questo progetto è un sistema di gestione delle entrate e delle uscite scritto in Python con Flask. Permette di tracciare le entrate e le uscite finanziarie, visualizzare grafici e statistiche, e gestire i dati in modo interattivo tramite una dashboard.

## Caratteristiche

- Aggiunta di transazioni di entrata e uscita con descrizione, importo, store e quantità.
- Visualizzazione delle transazioni in una tabella con colorazione per entrate (verde) e uscite (rosso).
- Grafico delle entrate e delle uscite.
- Grafico dei pezzi per store.
- Calcolo della variazione percentuale delle spese rispetto al periodo precedente.
- Filtro delle transazioni per intervallo di date.
- Utilizzo di un file CSV per salvare le transazioni.

## Requisiti

- Python 3.x
- Flask

## Installazione

Segui questi passaggi per installare e configurare il progetto:

1. **Clona il repository:**

   ```
   git clone https://github.com/Allsafeitalia/entrateUscite.git
   ```
   ```
   cd entrateUscite
   ```

   
3. **Crea un ambiente virtuale:**
```
python3 -m venv venv
```

**Attiva l'ambiente virtuale:**

**Su macOS e Linux:**

```
source venv/bin/activate
```
**Su Windows:**
```
.\venv\Scripts\activate
```
## Installa le dipendenze:
```
pip install -r requirements.txt
```
**Utilizzo**
**Esegui l'applicazione Flask:**
```
python app.py
```
**Apri un browser web e vai all'indirizzo:**

```
http://127.0.0.1:5000/
```

# Interagisci con la dashboard:

**Aggiungi Transazione:**<br/>
Compila il form per aggiungere una nuova transazione. <br/>
Inserisci la data, il tipo (entrata o uscita), la descrizione, l'importo, lo store e la quantità. <br/>
Clicca su "Aggiungi" per salvare la transazione.<br/>
**Filtra per Data:** <br/> 
Utilizza il form in alto per selezionare l'intervallo di date da analizzare. <br/>
Clicca su "Filtra" per visualizzare le transazioni nell'intervallo selezionato.<br/>
**Visualizza Grafici:** <br/>
Osserva i grafici per confrontare le entrate e le uscite e i pezzi per store.<br/>
**Variazione Percentuale:**<br/>
La dashboard mostra la variazione percentuale delle spese rispetto al periodo precedente.

# File Importanti
`app.py`: Script principale che esegue l'applicazione Flask. <br/>
`finanze.csv`: File CSV utilizzato per salvare le transazioni.<br/>
`templates/index.html`: Template HTML per la dashboard.<br/>
`requirements.txt`: Elenco delle dipendenze del progetto.<br/>
`.gitignore`: File per ignorare i file e le directory non necessari nel repository.<br/>

# Contributori
Progetto realizzato da [Giuseppe Mastronardi](https://giuseppemastronardi.dev).

# Licenza
Questo progetto è concesso in licenza sotto i termini della licenza MIT. Vedi il file LICENSE per i dettagli.
