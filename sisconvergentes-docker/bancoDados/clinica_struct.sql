create database if not exists clinica CHARACTER SET utf8 COLLATE utf8_bin;

use clinica;

drop table if exists animal ;
drop table if exists especie ;
drop table if exists tipo_animal ;


create table animal
  (
    id             bigint auto_increment not null ,
    nome           varchar (50) not null ,
    nascimento     date ,
    especie_id bigint not null ,
    constraint animal_pk primary key (id)
  ) ;

create table tipo_animal
  (
    acronimo  char (3) not null ,
    nome      varchar (100) not null ,
    descricao varchar (255),
    constraint tipo_animal_pk primary key (acronimo)
  ) ;

  create table especie
  (
    id                   bigint auto_increment not null ,
    nome                 varchar (50) not null ,
    descricao            varchar (100) ,
    tipo_animal_acronimo char (3) not null,
    constraint especie_pk primary key (id)
  ) ;


alter table tipo_animal add constraint tipo_animal_un unique ( nome ) ;

alter table especie add constraint especie_nome unique ( nome ) ;

alter table animal add constraint animal_especie_fk foreign key ( especie_id ) references especie ( id ) ;

alter table especie add constraint especie_tipo_animal_fk foreign key ( tipo_animal_acronimo ) references tipo_animal ( acronimo ) ;
