import gi
import psycopg2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("GTK3Agg")
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


DB_PARAMS = {
    "dbname": "agency",
    "user": "postgres",
    "password": "22081921",
    "host": "localhost",
    "port": "5432",
}

class ReportsApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Отчёты")
        self.set_border_width(10)
        self.set_default_size(600, 400)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        self.report_combo = Gtk.ComboBoxText()
        self.report_combo.append_text("Доступные квартиры")
        self.report_combo.append_text("Статистика за год")
        self.report_combo.append_text("Поиск по клиенту")
        self.report_combo.append_text("Поиск по адресу")
        self.report_combo.set_active(0)
        vbox.pack_start(self.report_combo, False, False, 0)
        
        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("Введите данные для поиска")
        vbox.pack_start(self.search_entry, False, False, 0)
        
        self.search_button = Gtk.Button(label="Выполнить")
        self.search_button.connect("clicked", self.run_report)
        vbox.pack_start(self.search_button, False, False, 0)
        
        self.result_view = Gtk.TextView()
        self.result_view.set_editable(False)
        self.result_buffer = self.result_view.get_buffer()
        
        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        scroll.add(self.result_view)
        vbox.pack_start(scroll, True, True, 0)
    
    def run_report(self, widget):
        report_type = self.report_combo.get_active_text()
        search_text = self.search_entry.get_text()
        
        query = ""
        if report_type == "Доступные квартиры":
            query = "SELECT * FROM Apartments WHERE available = TRUE"
        elif report_type == "Статистика за год":
            self.show_yearly_statistics()
            return
        elif report_type == "Поиск по клиенту" and search_text:
            query = f"""
                SELECT Apartments.* FROM Rentals
                JOIN Apartments ON Rentals.apartment_id = Apartments.apartment_id
                WHERE Rentals.client_id IN (
                    SELECT client_id FROM Clients 
                    WHERE first_name ILIKE '%{search_text}%' 
                    OR last_name ILIKE '%{search_text}%')
            """
        elif report_type == "Поиск по адресу" and search_text:
            query = f"""
                SELECT Clients.* FROM Rentals
                JOIN Apartments ON Rentals.apartment_id = Apartments.apartment_id
                JOIN Clients ON Rentals.client_id = Clients.client_id
                WHERE Apartments.address ILIKE '%{search_text}%'
            """
        
        if query:
            self.execute_query(query)
    
    def execute_query(self, query):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            
            result_text = "\n".join([str(row) for row in rows]) if rows else "Нет данных"
            self.result_buffer.set_text(result_text)
            
            cur.close()
            conn.close()
        except Exception as e:
            self.result_buffer.set_text(f"Ошибка: {e}")
    
    def show_yearly_statistics(self):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute("""
                SELECT EXTRACT(MONTH FROM start_date) AS rental_month, COUNT(*)
                FROM Rentals
                WHERE start_date >= date_trunc('year', CURRENT_DATE)
                GROUP BY rental_month
                ORDER BY rental_month
            """)
            data = cur.fetchall()
            cur.close()
            conn.close()
            
            if not data:
                self.result_buffer.set_text("Нет данных за текущий год")
                return
            
            months = [int(row[0]) for row in data]
            counts = [row[1] for row in data]
            
            full_months = list(range(1, 13))
            full_counts = [counts[months.index(m)] if m in months else 0 for m in full_months]
            
            plt.figure(figsize=(8, 4))
            plt.plot(full_months, full_counts, marker='o', linestyle='-', color='blue')
            plt.xlabel('Месяц')
            plt.ylabel('Количество аренд')
            plt.title('Статистика аренд за год')
            plt.xticks(full_months, ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"])
            plt.grid()
            plt.show()
        except Exception as e:
            self.result_buffer.set_text(f"Ошибка: {e}")

if __name__ == "__main__":
    app = ReportsApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

