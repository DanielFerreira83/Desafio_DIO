-- Recuperações simples com SELECT Statement
SELECT * FROM clientes;
SELECT * FROM veiculos;
SELECT * FROM servicos;
SELECT * FROM OS;

-- Filtros com WHERE Statement
SELECT * FROM clientes WHERE nome = 'José Ferreira';
SELECT * FROM veiculos WHERE modelo = 'Onix';
SELECT * FROM servicos WHERE valor > 200.00;

-- Crie expressões para gerar atributos derivados
SELECT nome, CONCAT(endereco, ', ', telefone) AS endereco_completo FROM clientes;

-- Defina ordenações dos dados com ORDER BY
SELECT * FROM clientes ORDER BY nome;
SELECT * FROM veiculos ORDER BY ano DESC;
SELECT * FROM servicos ORDER BY valor;

-- Condições de filtros aos grupos – HAVING Statement
SELECT id_cliente_fk, COUNT(*) AS quantidade_servicos FROM OS GROUP BY id_cliente_fk HAVING COUNT(*) > 1;

-- Crie junções entre tabelas para fornecer uma perspectiva mais complexa dos dados
SELECT c.nome, v.modelo, s.descricao, s.valor 
FROM OS o 
JOIN clientes c 
ON o.id_cliente_fk = c.id 
JOIN veiculos v 
ON o.id_veiculo_fk = v.id_veiculo 
JOIN servicos s 
ON o.id_servicos_fk = s.id_servico;
