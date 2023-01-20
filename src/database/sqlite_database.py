from typing import Optional
import sqlite3

from src.database.database import Database
from src.database.tables import Person
from src.utils import get_project_root


def convert_row_to_person(row):
    return Person(row[0], row[1])


class SQLiteDatabase(Database):
    conn = sqlite3.connect(str(get_project_root()) + "/FaceBase.db")

    def get_person(self, id) -> Optional[Person]:
        query = "SELECT * FROM People WHERE id = ?"
        cursor = self.conn.execute(query, (id,))
        person = None
        for row in cursor:
            person = convert_row_to_person(row)
        cursor.close()

        return person

    def get_id_by_name(self, name):
        query = f"SELECT * FROM People WHERE name = ?"
        cursor = self.conn.execute(query, (name,))

        for row in cursor:
            return row[0]

        return None

    def insert_or_update(self, person_name):
        query = f"SELECT * FROM People WHERE name = ?"

        cursor = self.conn.execute(query, (person_name,))
        is_record = False
        for row in cursor:
            is_record = True
            id = row[0]

        if is_record:
            cmd = f"""
                    UPDATE People
                    SET name = '{person_name}'
                    WHERE id = '{id}';
                    """
            self.conn.execute(cmd)
        else:
            params = (person_name, person_age)
            cmd = """
                    INSERT INTO People(name) 
                    Values(?);
                    """
            self.conn.execute(cmd, params)

        self.conn.commit()

