import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

        try:
            import mysql.connector

            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", "3306")),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=os.getenv("DB_NAME", "object_detection")
            )
            self.cursor = self.connection.cursor()
            print("MySQL connected.")
        except Exception as e:
            print(f"MySQL connection unavailable: {e}")
            print("Detection will continue without database logging.")

    def log_detection(self, object_name, confidence):
        if not self.connection or not self.cursor:
            return

        query = """
        INSERT INTO detections (object_name, confidence, detected_at)
        VALUES (%s, %s, %s)
        """
        values = (object_name, confidence, datetime.now())

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"Database logging error: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
