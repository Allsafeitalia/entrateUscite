# Importiamo i moduli necessari
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

# Configurazione del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConsulenzaInformatica:
    def __init__(self, project_name):
        self.project_name = project_name
        logger.info(f"Inizializzazione del progetto: {self.project_name}")

    def load_data(self, file_path):
        """Carica i dati da un file CSV."""
        try:
            data = pd.read_csv(file_path)
            logger.info(f"Dati caricati con successo da {file_path}")
            return data
        except Exception as e:
            logger.error(f"Errore nel caricamento dei dati: {e}")
            raise

    def analyze_data(self, data):
        """Esegue un'analisi di base sui dati."""
        try:
            summary = data.describe()
            logger.info("Analisi dei dati completata.")
            return summary
        except Exception as e:
            logger.error(f"Errore nell'analisi dei dati: {e}")
            raise

    def generate_report(self, analysis):
        """Genera un report basato sull'analisi dei dati."""
        try:
            report = analysis.to_string()
            report_file = f"{self.project_name}_report.txt"
            with open(report_file, 'w') as f:
                f.write(report)
            logger.info(f"Report generato con successo: {report_file}")
        except Exception as e:
            logger.error(f"Errore nella generazione del report: {e}")
            raise

    def visualize_data(self, data, columns):
        """Crea visualizzazioni per le colonne specificate dei dati."""
        try:
            for column in columns:
                plt.figure()
                data[column].hist()
                plt.title(f'Istogramma di {column}')
                plt.xlabel(column)
                plt.ylabel('Frequenza')
                image_path = f"{self.project_name}_{column}_histogram.png"
                plt.savefig(image_path)
                logger.info(f"Istogramma per {column} salvato con successo.")
        except Exception as e:
            logger.error(f"Errore nella visualizzazione dei dati: {e}")
            raise

    def generate_html_report(self, analysis, columns):
        """Genera un report HTML che include l'analisi dei dati e le visualizzazioni."""
        try:
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Report di Consulenza Informatica</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1, h2 {{ color: #2c3e50; }}
                    img {{ max-width: 600px; height: auto; }}
                </style>
            </head>
            <body>
                <h1>Report del Progetto: {self.project_name}</h1>
                <h2>Analisi dei Dati</h2>
                <pre>{analysis.to_string()}</pre>
                <h2>Visualizzazioni</h2>
            """

            for column in columns:
                image_path = f"{self.project_name}_{column}_histogram.png"
                if os.path.exists(image_path):
                    html_content += f'<h3>Istogramma di {column}</h3><img src="{image_path}" alt="Istogramma di {column}"><br>'

            html_content += """
            </body>
            </html>
            """

            html_file = f"{self.project_name}_report.html"
            with open(html_file, 'w') as f:
                f.write(html_content)
            logger.info(f"Report HTML generato con successo: {html_file}")
        except Exception as e:
            logger.error(f"Errore nella generazione del report HTML: {e}")
            raise

# Esempio di utilizzo del modulo
if __name__ == "__main__":
    consulenza = ConsulenzaInformatica("Progetto_Consulenza")
    
    # Caricamento dei dati
    data = consulenza.load_data("//Users/giuseppe.mastronardi/Desktop/entrateUscite/dati.csv")  # Sostituisci con il percorso reale
    
    # Analisi dei dati
    analysis = consulenza.analyze_data(data)
    print(analysis)
    
    # Generazione del report
    consulenza.generate_report(analysis)
    
    # Visualizzazione dei dati
    consulenza.visualize_data(data, ['colonna1', 'colonna2'])  # Sostituire con le colonne reali
    
    # Generazione del report HTML
    consulenza.generate_html_report(analysis, ['colonna1', 'colonna2'])  # Sostituire con le colonne reali
