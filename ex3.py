import csv
from datetime import datetime

class BatchProcessor:
    def __init__(self, csv_path, log_path="journal.log"):
        self.csv_path = csv_path
        self.log_path = log_path
        self.csv_file = None
        self.log_file = None

    def __enter__(self):
        try:
            self.csv_file = open(self.csv_path, "r", newline="", encoding="utf-8")
        except Exception as e:
            raise IOError(f"Erreur d'ouverture CSV : {e}")

        try:
            self.log_file = open(self.log_path, "a", encoding="utf-8")
        except Exception as e:
            if self.csv_file:
                self.csv_file.close()
            raise IOError(f"Erreur d'ouverture journal : {e}")

        self.log("=== Début du batch ===")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.log(f"ERREUR détectée : {exc}")

        self.log("=== Fin du batch ===")

        if self.csv_file:
            self.csv_file.close()
        if self.log_file:
            self.log_file.close()

        return False

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(f"[{timestamp}] {message}\n")

    def process(self):
        reader = csv.reader(self.csv_file)
        for line in reader:
            if not line:
                continue
            operation = line[0]
            self.log(f"Traitement de : {operation}")
            print("Operation:", operation)
with BatchProcessor("operations.csv") as bp:
    bp.process()
