sudo apt install docker.io docker-compose
-----------
SELECT 
    Despesas.id AS id_despesa,
    Despesas.id_deputado AS id_deputado_despesa,
    Despesas.ano,
    Despesas.cnpj_cpf_fornecedor AS cnpj_cpf_despesa,
    Despesas.cod_documento,
    Despesas.cod_lote,
    Despesas.cod_tipo_documento,
    Despesas.data_documento,
    Despesas.mes,
    Despesas.num_documento,
    Despesas.num_ressarcimento,
    Despesas.parcela,
    Despesas.tipo_despesa,
    Despesas.tipo_documento,
    Despesas.url_documento,
    Despesas.valor_documento,
    Despesas.valor_glosa,
    Despesas.valor_liquido,
    Deputados.id AS id_deputado_principal, 
    Deputados.nome AS nome_deputado,
    Fornecedores.cnpj_cpf AS cnpj_cpf_fornecedor,
    Fornecedores.nome AS nome_fornecedor
FROM 
    Despesas
JOIN 
    Deputados ON Despesas.id_deputado = Deputados.id
JOIN 
    Fornecedores ON Despesas.cnpj_cpf_fornecedor = Fornecedores.cnpj_cpf

---
SELECT 
    despesas.id AS id_despesa,
    despesas.id_deputado AS id_deputado_despesa,
    despesas.ano,
    despesas.cnpj_cpf_fornecedor AS cnpj_cpf_despesa,
    despesas.ide_documento,
    despesas.num_lote,
    despesas.num_sub_cota,
    despesas.data_emissao,
    despesas.mes,
    despesas.num_mes,
    despesas.num_ressarcimento,
    despesas.descricao,
    despesas.descricao_especificacao,
    despesas.url_documento,
    despesas.valor_documento,
    despesas.valor_glosa,
    despesas.valor_liquido,
    deputados.id AS id_deputado_principal, 
    deputados.nome AS nome_deputado,
    deputados.uf,
    deputados.sigla_partido,
    deputados.cod_legislatura,
    fornecedores.cnpj_cpf AS cnpj_cpf_fornecedor,
    fornecedores.nome AS nome_fornecedor
FROM 
    despesas
JOIN 
    deputados ON despesas.id_deputado = deputados.id
JOIN 
    fornecedores ON despesas.cnpj_cpf_fornecedor = fornecedores.cnpj_cpf;

