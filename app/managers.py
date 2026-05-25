import sqlite3

from app.models import Actor



class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self._connection = sqlite3.connect(self.db_name)
        self.cursor = self._connection.cursor()
        self.cursor.execute(f'CREATE TABLE {self.table_name} '
                            f'( id INTEGER PRIMARY KEY, '
                            f'first_name TEXT NOT NULL, '
                            f'second_name TEXT NOT NULL, ) ')

    def create(self,first_name: str, last_name: str):
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f'INSERT INTO {self.table_name} '
                             f'(first_name, last_name) VALUES (?, ?)',
                             (first_name, last_name)
                             )
        self._connection.commit()


    def all(self):
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f'SELECT * FROM {self.table_name}')
        return actor_cursor.fetchall()

    def update(self,first_name: str, last_name: str):
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f'UPDATE {self.table_name} '
                             f'SET first_mane = (?), last_name = (?)',
                             (first_name, last_name))
        self._connection.commit()

    def delete(self,first_name: str, last_name: str):
        actor_cursor = self._connection.cursor()
        actor_cursor.execute(f'DELETE FROM {self.table_name} '
                             f'WHERE first_mane = (?) AND last_name = (?)',
                             (first_name, last_name))
        self._connection.commit()

# mngr = ActorManager('app/actor.db', 'actor.sqlite3')
# mngr.create('first_name', 'last_name')
# print(mngr.all())
