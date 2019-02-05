use clinica;

delete from animal;
delete from especie;
delete from tipo_animal;

insert into tipo_animal (acronimo, nome) values ('cao', 'cachorro');
insert into tipo_animal (acronimo, nome) values ('gat', 'gato');

insert into especie (nome, descricao, tipo_animal_acronimo) values ('cachorro comum', 'um tipo de cachorro vira-latas', 'cao');
insert into especie (nome, descricao, tipo_animal_acronimo) values ('gato comum', 'um tipo de gato', 'gat');

insert into animal (especie_id, nome, nascimento)
select especie.id, 'toto', NOW() from especie
where especie.nome = 'cachorro comum';

insert into animal (especie_id, nome, nascimento)
select especie.id, 'bichano', NOW() from especie
where especie.nome = 'gato comum';

insert into animal (especie_id, nome, nascimento)
select especie.id, 'tom', NOW() from especie
where especie.nome = 'gato comum';

insert into animal (especie_id, nome, nascimento)
select especie.id, 'gatuno', NOW() from especie
where especie.nome = 'gato comum';
