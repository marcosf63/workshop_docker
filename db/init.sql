create database ditec;
\c ditec
create table equipe (
  id serial not null,
  nome varchar(50) not null
);

insert into equipe (nome) values ('sacti');
insert into equipe (nome) values ('sages');
insert into equipe (nome) values ('sainf');

