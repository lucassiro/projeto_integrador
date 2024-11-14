from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Create a SQLite database engine
user = "lucas"
password = "12345"
host = "localhost:5432"
database = "camara"

engine = create_engine(f"postgresql://{user}:{password}@{host}/{database}")


# Create a base class for our declarative class definitions
class Base(DeclarativeBase):
    pass


# Define a simple table model
class Deputados(Base):
    __tablename__ = "deputados"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    uf = Column(String)
    sigla_partido = Column(String)
    cod_legislatura = Column(Integer)


class Despesas(Base):
    __tablename__ = "despesas"
    id = Column(Integer, primary_key=True)
    id_deputado = Column(Integer)
    mes = Column(Integer)
    num_mes = Column(Integer)
    ano = Column(Integer)
    descricao = Column(String)
    descricao_especificacao = Column(String)
    num_sub_cota = Column(Integer)
    cnpj_cpf_fornecedor = Column(String)
    data_emissao = Column(String)
    valor_documento = Column(Float)
    valor_glosa = Column(Float)
    valor_liquido = Column(Float)
    txt_passageiro = Column(String)
    txt_trecho = Column(String)
    num_lote = Column(Integer)
    num_ressarcimento = Column(String)
    dat_pagamento_restituicao = Column(String)
    vlr_restituicao = Column(Float)
    nu_deputado_id = Column(Integer)
    ide_documento = Column(Integer)
    url_documento = Column(String)


class Fornecedores(Base):
    __tablename__ = "fornecedores"
    cnpj_cpf = Column(String, primary_key=True)
    nome = Column(String)
    numero = Column(String)


# Drop tables if they exist
Base.metadata.drop_all(engine)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
