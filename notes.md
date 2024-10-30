sudo apt install docker.io docker-compose


SELECT 
    Despesas.id_deputado AS id_deputado_despesa,
    Deputados.id AS id_deputado_principal, 
    Despesas.*, 
    Deputados.nome AS nome_deputado
FROM 
    Despesas
JOIN 
    Deputados ON Despesas.id_deputado = Deputados.id