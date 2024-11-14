import pandas as pd
from rich.console import Console
from rich.progress import track
from rich.table import Table
from rich.traceback import install

from db import Deputados, Despesas, Fornecedores, Session

install(show_locals=True)


def main() -> None:
    console = Console()

    df = pd.read_csv("src/data/Ano-2022.csv", sep=";")
    for column in df.columns:
        if df[column].dtype == "int64" or df[column].dtype == "float64":
            df[column] = df[column].fillna(0)
        elif df[column].dtype == "object":
            df[column] = df[column].fillna("")

    with Session() as session:
        console.print("Inserindo registros no banco de dados...")
        for row in track(df.itertuples(), total=len(df)):
            # Deputados
            deputado_obj = Deputados(
                id=row.ideCadastro,
                nome=row.txNomeParlamentar,
                cpf=row.cpf,
                uf=row.sgUF,
                sigla_partido=row.sgPartido,
                cod_legislatura=row.codLegislatura,
            )
            existing_deputado = session.query(Deputados).filter_by(id=deputado_obj.id).first()
            if not existing_deputado:
                session.add(deputado_obj)

            # Despesas
            despesa_obj = Despesas(
                id_deputado=row.ideCadastro,
                mes=row.numMes,
                num_mes=row.numMes,
                ano=row.numAno,
                descricao=row.txtDescricao,
                descricao_especificacao=row.txtDescricaoEspecificacao,
                num_sub_cota=row.numSubCota,
                cnpj_cpf_fornecedor=row.txtCNPJCPF,
                data_emissao=row.datEmissao,
                valor_documento=row.vlrDocumento,
                valor_glosa=row.vlrGlosa,
                valor_liquido=row.vlrLiquido,
                txt_passageiro=row.txtPassageiro,
                txt_trecho=row.txtTrecho,
                num_lote=row.numLote,
                num_ressarcimento=row.numRessarcimento,
                dat_pagamento_restituicao=row.datPagamentoRestituicao,
                vlr_restituicao=row.vlrRestituicao,
                nu_deputado_id=row.nuDeputadoId,
                ide_documento=row.ideDocumento,
                url_documento=row.urlDocumento,
            )
            session.add(despesa_obj)

            # Fornecedores
            fornecedor_obj = Fornecedores(cnpj_cpf=row.txtCNPJCPF, nome=row.txtFornecedor, numero=row.txtNumero)
            existing_fornecedor = session.query(Fornecedores).filter_by(cnpj_cpf=fornecedor_obj.cnpj_cpf).first()
            if not existing_fornecedor:
                session.add(fornecedor_obj)

        session.commit()

    # Count records
    with Session() as session:
        deputados_count = session.query(Deputados).count()
        despesas_count = session.query(Despesas).count()
        fornecedores_count = session.query(Fornecedores).count()

    table = Table(title="Quantidade de registros")

    table.add_column("Tabela", style="bold")
    table.add_column("Quantidade", style="bold")

    table.add_row("Deputados", str(deputados_count))
    table.add_row("Despesas", str(despesas_count))
    table.add_row("Fornecedores", str(fornecedores_count))

    console.print("\n")
    console.print(table)


if __name__ == "__main__":
    main()
