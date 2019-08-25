from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'

    matricula = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    login = Column(String)
    senha = Column(String)


class Permissao(Base):
    __tablename__ = 'permissao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)


class PermissaoUsuario(Base):
    __tablename__ = 'permissao_usuario'

    matricula = Column(Integer, ForeignKey('usuario.matricula'), primary_key=True)
    permissao = Column(Integer, ForeignKey('permissao.id'), primary_key=True)


engine = create_engine('sqlite:///sistema.db', echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
