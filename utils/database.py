# backend\app\utils\database.py
import psycopg2
from psycopg2.extras import RealDictCursor

connection_info = {
    "host": "localhost",
    "port": "2222",
    "database": "my-imbiss",
    "user": "postgres",
    "password": "0808"
}

def get_db_connection ():
    try:
        conn = psycopg2.connect(**connection_info, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"Fehler beim Verbinden zur Datenbank: {e}")
        return None

def test_connection():
    try:
        conn = get_db_connection ()
        if conn:
            print("Verbindung zur Datenbank erfolgreich hergestellt.")
            conn.close()
    except Exception as e:
        print(f"Fehler beim Verbinden zur Datenbank: {e}")

# Teste die Verbindung beim Laden dieser Datei
test_connection()
