create table if not exists customers (
	customer_id uuid primary key,
	cpf varchar(14) unique,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(80),
    phone varchar(20)
);

create table if not exists products (
	product_id uuid primary key,
	name varchar(30) not null,
    description varchar(150) not null,
    category varchar(30) not null,
    price decimal(7,2) not null,
    image_url varchar(150)
);

create table if not exists orders (
	order_id uuid primary key,
	customer_id uuid not null,
    creation_date timestamp default now(),
    order_total decimal(7,2)
);

create table if not exists order_items (
	order_id uuid not null,
	product_id not null,
	product_quantity integer not null
);