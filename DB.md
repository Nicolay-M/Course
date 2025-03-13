CREATE TABLE Clients (client_id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, email VARCHAR(100), phone VARCHAR(15)); CREATE TABLE Apartments (apartment_id SERIAL PRIMARY KEY, address VARCHAR(255) NOT NULL, number_of_rooms INT, area INT, price INT NOT NULL, available BOOLEAN DEFAULT TRUE); CREATE TABLE Employees (employee_id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), position VARCHAR(50)); CREATE TABLE Rentals (rental_id SERIAL PRIMARY KEY, client_id INT, apartment_id INT, employee_id INT, start_date DATE, end_date DATE, rental_price INT, FOREIGN KEY (client_id) REFERENCES Clients(client_id), FOREIGN KEY (apartment_id) REFERENCES Apartments(apartment_id), FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)); 



INSERT INTO Clients (first_name, last_name, email, phone) VALUES ('Иван', 'Иванов', 'ivan.ivanov@example.com', '1234567890'), ('Мария', 'Петрова', 'maria.petrova@example.com', '2345678901'), ('Алексей', 'Смирнов', 'alexey.smirnov@example.com', '3456789012'), ('Елена', 'Давыдова', 'elena.davydova@example.com', '4567890123'), ('Дмитрий', 'Михайлов', 'dmitry.mikhaylov@example.com', '5678901234'), ('Светлана', 'Бровина', 'svetlana.brovina@example.com', '6789012345'), ('Максим', 'Васильев', 'maxim.vasilyev@example.com', '7890123456'), ('Анна', 'Кузнецова', 'anna.kuznetsova@example.com', '8901234567'), ('Петр', 'Тимофеев', 'petr.timofeev@example.com', '9012345678'), ('Ольга', 'Смирнова', 'olga.smirnova@example.com', '0123456789'); INSERT INTO Apartments (address, number_of_rooms, area, price, available) VALUES ('Улица Ленина, 123', 2, 45, 50000, TRUE), ('Улица Пушкина, 456', 3, 60, 75000, TRUE), ('Проспект Мира, 789', 1, 30, 35000, TRUE), ('Улица Советская, 101', 4, 80, 120000, TRUE), ('Улица Дружбы, 202', 2, 50, 55000, FALSE), ('Площадь Победы, 303', 3, 70, 85000, TRUE), ('Улица Красная, 404', 2, 55, 65000, TRUE), ('Улица Роза, 505', 1, 35, 40000, TRUE), ('Улица Октябрьская, 606', 3, 75, 95000, FALSE), ('Улица Зелёная, 707', 4, 90, 130000, TRUE); INSERT INTO Employees (first_name, last_name, position) VALUES ('Алексей', 'Смирнов', 'Менеджер'), ('Борис', 'Кузнецов', 'Продавец'), ('Чарли', 'Попов', 'Техник'), ('Дебора', 'Морозова', 'Агент'), ('Эдуард', 'Петров', 'Администратор'), ('Франк', 'Сидоров', 'Координатор'), ('Грета', 'Фролова', 'Ассистент'), ('Генри', 'Романов', 'Директор'), ('Ирина', 'Лебедева', 'Секретарь'), ('Джек', 'Новиков', 'Консультант'); INSERT INTO Rentals (client_id, apartment_id, employee_id, start_date, end_date, rental_price) VALUES (1, 1, 1, '2024-01-01', '2024-12-31', 500), (2, 2, 2, '2024-02-01', '2024-08-31', 750), (3, 3, 3, '2024-03-01', '2024-09-30', 350), (4, 4, 4, '2024-04-01', '2024-10-31', 1200), (5, 5, 5, '2024-05-01', '2024-11-30', 550), (6, 6, 6, '2024-06-01', '2024-12-31', 850), (7, 7, 7, '2024-07-01', '2024-09-30', 650), (8, 8, 8, '2024-08-01', '2024-11-30', 400), (9, 9, 9, '2024-09-01', '2024-12-31', 950), (10, 10, 10, '2024-10-01', '2024-12-31', 1300);
 


















