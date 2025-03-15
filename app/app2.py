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

class ViewTablesApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Просмотр всех таблиц")
        self.set_border_width(10)
        self.set_default_size(800, 500)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        self.table_combo = Gtk.ComboBoxText()
        self.table_combo.append_text("Clients")
        self.table_combo.append_text("Apartments")
        self.table_combo.append_text("Employees")
        self.table_combo.append_text("Rentals")
        self.table_combo.set_active(0)
        vbox.pack_start(self.table_combo, False, False, 0)
        
        self.view_button = Gtk.Button(label="Показать")
        self.view_button.connect("clicked", self.show_table_data)
        vbox.pack_start(self.view_button, False, False, 0)
        
        self.result_view = Gtk.TextView()
        self.result_view.set_editable(False)
        self.result_buffer = self.result_view.get_buffer()
        
        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        scroll.add(self.result_view)
        vbox.pack_start(scroll, True, True, 0)
    
    def show_table_data(self, widget):
        table_name = self.table_combo.get_active_text()
        query = f"SELECT * FROM {table_name}"
        
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            
            result_text = " | ".join(columns) + "\n" + "-" * 80 + "\n"
            result_text += "\n".join([" | ".join(map(str, row)) for row in rows]) if rows else "Нет данных"
            
            self.result_buffer.set_text(result_text)
            
            cur.close()
            conn.close()
        except Exception as e:
            self.result_buffer.set_text(f"Ошибка: {e}")

if __name__ == "__main__":
    app = ViewTablesApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

