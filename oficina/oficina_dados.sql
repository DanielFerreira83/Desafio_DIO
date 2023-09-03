insert into clientes (nome, endereco, telefone) values('Daniel Ferreira','Rua 85','999998888')
,('Arthur Ferreira','Rua 22','999996666')
,('José Ferreira','Rua 12','999994444')
,('fabio Ferreira','Rua 44','999997777')
,('Lucas Ferreira','Rua 96','999992222');

insert into veiculos (placa, modelo, ano) values('abc1234','Argo','2020')
,('acb9685','Onix','2019')
,('Jab5c12','Onix','2017')
,('acb2563','Gol','2010')
,('abc1199','Uno','2010');

insert into servicos (descricao, valor) values('revisao',300.00)
,('troca de oleo',80.00)
,('pintura',650.00);

insert into OS (id_cliente_fk, id_veiculo_fk, id_servicos_fk) values(2, 1, 2)
,(1, 1, 2)
,(1,2,2)
,(3,2,1),
(2,1,1)
,(2,4,1)
,(3,5,2);



