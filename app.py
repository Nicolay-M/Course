import gi
import psycopg2

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

DB_PARAMS = {
    "dbname": "agency",
    "user": "postgres",
    "password": "22081921",
    "host": "localhost",
    "port": "5432",
}

class DatabaseApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Управление базой данных")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        self.table_combo = Gtk.ComboBoxText()
        self.table_combo.append_text("Clients")
        self.table_combo.append_text("Apartments")
        self.table_combo.append_text("Employees")
        self.table_combo.append_text("Rentals")
        self.table_combo.set_active(0)
        vbox.pack_start(self.table_combo, False, False, 0)
        
        self.entry_grid = Gtk.Grid()
        vbox.pack_start(self.entry_grid, True, True, 0)
        
        self.submit_button = Gtk.Button(label="Добавить запись")
        self.submit_button.connect("clicked", self.on_submit)
        vbox.pack_start(self.submit_button, False, False, 0)
        
        self.table_combo.connect("changed", self.on_table_changed)
        self.on_table_changed()
    
    def on_table_changed(self, widget=None):
        for child in self.entry_grid.get_children():
            self.entry_grid.remove(child)
        
        table = self.table_combo.get_active_text()
        columns = self.get_columns(table)
        self.entries = {}
        
        for i, column in enumerate(columns):
            label = Gtk.Label(label=column)
            if column in ["client_id", "apartment_id", "employee_id"] and table == "Rentals":
                combo = Gtk.ComboBoxText()
                self.populate_combo(combo, column)
                self.entries[column] = combo
                self.entry_grid.attach(label, 0, i, 1, 1)
                self.entry_grid.attach(combo, 1, i, 1, 1)
            else:
                entry = Gtk.Entry()
                self.entries[column] = entry
                self.entry_grid.attach(label, 0, i, 1, 1)
                self.entry_grid.attach(entry, 1, i, 1, 1)
        
        self.show_all()
    
    def get_columns(self, table):
        column_map = {
            "Clients": ["first_name", "last_name", "email", "phone"],
            "Apartments": ["address", "number_of_rooms", "area", "price", "available"],
            "Employees": ["first_name", "last_name", "position"],
            "Rentals": ["client_id", "apartment_id", "employee_id", "start_date", "end_date", "rental_price"],
        }
        return column_map.get(table, [])
    
    def populate_combo(self, combo, column):
        table_map = {
            "client_id": "Clients",
            "apartment_id": "Apartments",
            "employee_id": "Employees",
        }
        table = table_map[column]
        id_column = column  # client_id, apartment_id, employee_id
        name_column = "first_name" if table != "Apartments" else "address"
        
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute(f"SELECT {id_column}, {name_column} FROM {table}")
            rows = cur.fetchall()
            for row in rows:
                combo.append_text(f"{row[0]} - {row[1]}")
            cur.close()
            conn.close()
        except Exception as e:
            print("Ошибка при получении данных:", e)
    
    def on_submit(self, widget):
        table = self.table_combo.get_active_text()
        columns = self.get_columns(table)
        values = []
        
        for col in columns:
            if isinstance(self.entries[col], Gtk.ComboBoxText):
                selected = self.entries[col].get_active_text()
                values.append(selected.split(" - ")[0] if selected else None)
            else:
                values.append(self.entries[col].get_text())
        
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute(query, values)
            conn.commit()
            cur.close()
            conn.close()
            print("Запись добавлена!")
        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    app = DatabaseApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

