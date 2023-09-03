create database Oficina;
use Oficina;

create table clientes ( 
id int primary key unique not null auto_increment,
nome varchar(45) not null,
endereco varchar(50) not null,
telefone varchar(11)
);

create table veiculos(
id_veiculo int not null primary key unique auto_increment,
placa char(7),
modelo varchar(15),
ano varchar(4)
);

create table servicos (
id_servico int primary key not null unique auto_increment,
descricao varchar(20),
valor decimal(10,2)
);

create table OS(
id_os int primary key unique auto_increment,
id_cliente_fk int,
id_veiculo_fk int,
id_servicos_fk int,
foreign key (id_cliente_fk) references clientes(id),
foreign key (id_servicos_fk) references servicos(id_servico),
foreign key (id_veiculo_fk) references veiculos(id_veiculo)
);
