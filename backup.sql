--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: apartments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apartments (
    apartment_id integer NOT NULL,
    address character varying(255) NOT NULL,
    number_of_rooms integer,
    area integer,
    price integer NOT NULL,
    available boolean DEFAULT true
);


ALTER TABLE public.apartments OWNER TO postgres;

--
-- Name: apartments_apartment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apartments_apartment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.apartments_apartment_id_seq OWNER TO postgres;

--
-- Name: apartments_apartment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apartments_apartment_id_seq OWNED BY public.apartments.apartment_id;


--
-- Name: clients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clients (
    client_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(100),
    phone character varying(15)
);


ALTER TABLE public.clients OWNER TO postgres;

--
-- Name: clients_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clients_client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clients_client_id_seq OWNER TO postgres;

--
-- Name: clients_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clients_client_id_seq OWNED BY public.clients.client_id;


--
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    "position" character varying(50)
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- Name: employees_employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.employees_employee_id_seq OWNER TO postgres;

--
-- Name: employees_employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;


--
-- Name: rentals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rentals (
    rental_id integer NOT NULL,
    client_id integer,
    apartment_id integer,
    employee_id integer,
    start_date date,
    end_date date,
    rental_price integer
);


ALTER TABLE public.rentals OWNER TO postgres;

--
-- Name: rentals_rental_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rentals_rental_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rentals_rental_id_seq OWNER TO postgres;

--
-- Name: rentals_rental_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rentals_rental_id_seq OWNED BY public.rentals.rental_id;


--
-- Name: apartments apartment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apartments ALTER COLUMN apartment_id SET DEFAULT nextval('public.apartments_apartment_id_seq'::regclass);


--
-- Name: clients client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients ALTER COLUMN client_id SET DEFAULT nextval('public.clients_client_id_seq'::regclass);


--
-- Name: employees employee_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);


--
-- Name: rentals rental_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rentals ALTER COLUMN rental_id SET DEFAULT nextval('public.rentals_rental_id_seq'::regclass);


--
-- Data for Name: apartments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.apartments (apartment_id, address, number_of_rooms, area, price, available) FROM stdin;
1	Улица Ленина, 123	2	45	50000	t
2	Улица Пушкина, 456	3	60	75000	t
3	Проспект Мира, 789	1	30	35000	t
4	Улица Советская, 101	4	80	120000	t
5	Улица Дружбы, 202	2	50	55000	f
6	Площадь Победы, 303	3	70	85000	t
7	Улица Красная, 404	2	55	65000	t
8	Улица Роза, 505	1	35	40000	t
9	Улица Октябрьская, 606	3	75	95000	f
10	Улица Зелёная, 707	4	90	130000	t
11	Сыктывкар, д.3	5	90	5000	t
\.


--
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clients (client_id, first_name, last_name, email, phone) FROM stdin;
1	Иван	Иванов	ivan.ivanov@example.com	1234567890
2	Мария	Петрова	maria.petrova@example.com	2345678901
3	Алексей	Смирнов	alexey.smirnov@example.com	3456789012
4	Елена	Давыдова	elena.davydova@example.com	4567890123
5	Дмитрий	Михайлов	dmitry.mikhaylov@example.com	5678901234
6	Светлана	Бровина	svetlana.brovina@example.com	6789012345
7	Максим	Васильев	maxim.vasilyev@example.com	7890123456
8	Анна	Кузнецова	anna.kuznetsova@example.com	8901234567
9	Петр	Тимофеев	petr.timofeev@example.com	9012345678
10	Ольга	Смирнова	olga.smirnova@example.com	0123456789
11	Иван	Иванов	ivan@mail.ru	894589435
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employees (employee_id, first_name, last_name, "position") FROM stdin;
1	Алексей	Смирнов	Менеджер
2	Борис	Кузнецов	Продавец
3	Чарли	Попов	Техник
4	Дебора	Морозова	Агент
5	Эдуард	Петров	Администратор
6	Франк	Сидоров	Координатор
7	Грета	Фролова	Ассистент
8	Генри	Романов	Директор
9	Ирина	Лебедева	Секретарь
10	Джек	Новиков	Консультант
11	Иван	Иванов	Менеджер
\.


--
-- Data for Name: rentals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rentals (rental_id, client_id, apartment_id, employee_id, start_date, end_date, rental_price) FROM stdin;
1	1	1	1	2024-01-01	2024-12-31	500
2	2	2	2	2024-02-01	2024-08-31	750
3	3	3	3	2024-03-01	2024-09-30	350
4	4	4	4	2024-04-01	2024-10-31	1200
5	5	5	5	2024-05-01	2024-11-30	550
6	6	6	6	2024-06-01	2024-12-31	850
7	7	7	7	2024-07-01	2024-09-30	650
8	8	8	8	2024-08-01	2024-11-30	400
9	9	9	9	2024-09-01	2024-12-31	950
10	10	10	10	2024-10-01	2024-12-31	1300
11	4	6	8	2024-10-10	2024-12-10	1000
\.


--
-- Name: apartments_apartment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apartments_apartment_id_seq', 11, true);


--
-- Name: clients_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clients_client_id_seq', 11, true);


--
-- Name: employees_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employees_employee_id_seq', 11, true);


--
-- Name: rentals_rental_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rentals_rental_id_seq', 11, true);


--
-- Name: apartments apartments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apartments
    ADD CONSTRAINT apartments_pkey PRIMARY KEY (apartment_id);


--
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (client_id);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);


--
-- Name: rentals rentals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rentals
    ADD CONSTRAINT rentals_pkey PRIMARY KEY (rental_id);


--
-- Name: rentals rentals_apartment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rentals
    ADD CONSTRAINT rentals_apartment_id_fkey FOREIGN KEY (apartment_id) REFERENCES public.apartments(apartment_id);


--
-- Name: rentals rentals_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rentals
    ADD CONSTRAINT rentals_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.clients(client_id);


--
-- Name: rentals rentals_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rentals
    ADD CONSTRAINT rentals_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(employee_id);


--
-- PostgreSQL database dump complete
--

