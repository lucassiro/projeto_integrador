from rich.console import Console
from rich.progress import track
from rich.table import Table

from api import CamaraAPI
from db import Deputados, Despesas, Fornecedores, Session

console = Console()
api = CamaraAPI()
deputados = api.get_deputados()


def main() -> None:
    with Session() as session:
        console.print("Inserindo registros no banco de dados...")

        # Deputados
        for deputado in track(deputados["dados"], description=""):
            deputado_obj = Deputados(
                id=deputado["id"],
                nome=deputado["nome"],
                sigla_partido=deputado["siglaPartido"],
                email=deputado["email"],
            )
            existing_deputado = session.query(Deputados).filter_by(id=deputado_obj.id).first()
            if not existing_deputado:
                session.add(deputado_obj)

            # Despesas
            despesas = api.get_despesas(id=deputado["id"], year=2022)
            for despesa in despesas["dados"]:
                despesa_obj = Despesas(
                    id_deputado=deputado_obj.id,
                    ano=despesa["ano"],
                    cnpj_cpf_fornecedor=despesa["cnpjCpfFornecedor"],
                    cod_documento=despesa["codDocumento"],
                    cod_lote=despesa["codLote"],
                    cod_tipo_documento=despesa["codTipoDocumento"],
                    data_documento=despesa["dataDocumento"],
                    mes=despesa["mes"],
                    num_documento=despesa["numDocumento"],
                    num_ressarcimento=despesa["numRessarcimento"],
                    parcela=despesa["parcela"],
                    tipo_despesa=despesa["tipoDespesa"],
                    tipo_documento=despesa["tipoDocumento"],
                    url_documento=despesa["urlDocumento"],
                    valor_documento=despesa["valorDocumento"],
                    valor_glosa=despesa["valorGlosa"],
                    valor_liquido=despesa["valorLiquido"],
                )
                session.add(despesa_obj)

                # Fornecedores
                fornecedor_obj = Fornecedores(
                    cnpj_cpf=despesa["cnpjCpfFornecedor"],
                    nome=despesa["nomeFornecedor"],
                )
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
