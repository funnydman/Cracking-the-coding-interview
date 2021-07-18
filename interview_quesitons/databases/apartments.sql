create table buildings (
    id serial primary key,
    name varchar(100),
    address varchar(500)
);

create table apartments (
    id serial primary key ,
    address varchar(500),
    building_id int references buildings
);


create table tenants (
    id serial primary key ,
    name varchar(100),
    address varchar(500)
);



create  table tenant_apartments (
    tenant_id int references tenants,
    apartment_id int references apartments
);
