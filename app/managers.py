import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.table_name = "actors"
        self._connection = sqlite3.connect("cinema.db3")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> list:
        cinema_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name from {self.table_name}"
        )
        return [Actor(*row) for row in cinema_cursor]

    def update(self, row_id: int, new_first: str, new_last: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name=? "
            "WHERE id = ?",
            (new_first, new_last, row_id),
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE from {self.table_name} " "WHERE id = ?", (id_to_delete,)
        )
