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
    sigla_partido = Column(String)
    email = Column(String)


class Despesas(Base):
    __tablename__ = "despesas"
    id = Column(Integer, primary_key=True)
    id_deputado = Column(Integer)
    ano = Column(Integer)
    cnpj_cpf_fornecedor = Column(String)
    cod_documento = Column(String)
    cod_lote = Column(String)
    cod_tipo_documento = Column(String)
    data_documento = Column(String)
    mes = Column(Integer)
    num_documento = Column(String)
    num_ressarcimento = Column(String)
    parcela = Column(String)
    tipo_despesa = Column(String)
    tipo_documento = Column(String)
    url_documento = Column(String)
    valor_documento = Column(Float)
    valor_glosa = Column(Float)
    valor_liquido = Column(Float)


class Fornecedores(Base):
    __tablename__ = "fornecedores"
    cnpj_cpf = Column(String, primary_key=True)
    nome = Column(String)


# Drop tables if they exist
# Base.metadata.drop_all(engine)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
