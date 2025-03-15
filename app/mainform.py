import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from app import DatabaseApp
from app1 import ReportsApp
from app2 import ViewTablesApp



class LoginWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Авторизация")
        self.set_border_width(10)
        self.set_default_size(300, 200)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        self.label = Gtk.Label(label="Введите имя пользователя и пароль")
        vbox.pack_start(self.label, False, False, 0)
        
        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Имя пользователя")
        vbox.pack_start(self.username_entry, False, False, 0)
        
        self.password_entry = Gtk.Entry()
        self.password_entry.set_placeholder_text("Пароль")
        self.password_entry.set_visibility(False)
        vbox.pack_start(self.password_entry, False, False, 0)
        
        self.login_button = Gtk.Button(label="Войти")
        self.login_button.connect("clicked", self.on_login)
        vbox.pack_start(self.login_button, False, False, 0)
        
        self.client_button = Gtk.Button(label="Я клиент")
        self.client_button.connect("clicked", self.login_as_client)
        vbox.pack_start(self.client_button, False, False, 0)
    
    def on_login(self, widget):
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()
        
        if username == "postgres" and password == "22081921":
            self.hide()
            main_app = MainApp()
            main_app.connect("destroy", Gtk.main_quit)
            main_app.show_all()
        else:
            self.label.set_text("Неверные учетные данные")
    
    def login_as_client(self, widget):
        self.hide()
        app = ReportsApp()
        app.connect("destroy", Gtk.main_quit)
        app.show_all()

class MainApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Главное меню")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        btn_data_entry = Gtk.Button(label="Ввод данных")
        btn_data_entry.connect("clicked", self.open_data_entry)
        vbox.pack_start(btn_data_entry, False, False, 0)
        
        btn_reports = Gtk.Button(label="Отчёты")
        btn_reports.connect("clicked", self.open_reports)
        vbox.pack_start(btn_reports, False, False, 0)
        
        btn_table_view = Gtk.Button(label="Просмотр таблиц")
        btn_table_view.connect("clicked", self.open_table_view)
        vbox.pack_start(btn_table_view, False, False, 0)
    
    def open_data_entry(self, widget):
        app = DatabaseApp()
        app.show_all()
    
    def open_reports(self, widget):
        app = ReportsApp()
        app.show_all()
    
    def open_table_view(self, widget):
        app = ViewTablesApp()
        app.show_all()

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.connect("destroy", Gtk.main_quit)
    login_window.show_all()
    Gtk.main()

