from datetime import datetime
from contextlib import ExitStack

class ConnectionManager:
    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"[{datetime.now()}] Connexion à {self.service_name} établie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[{datetime.now()}] Déconnexion de {self.service_name}.")
        if exc_type:
            print(f"Erreur détectée : {exc_type.__name__} — {exc_value}")
                  
with ExitStack() as stack:
    log = stack.enter_context(open("log.txt", "a"))
    conn = stack.enter_context(ConnectionManager("Serveur X"))
    log.write(f"[{datetime.now()}] Tâche effectuée sur {conn.service_name}")
with ExitStack() as stack:
    log = stack.enter_context(open("log.txt", "a"))
    conn = stack.enter_context(ConnectionManager("Base Y"))
    raise RuntimeError("Erreur de traitement")