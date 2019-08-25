from sqlalchemy.orm import sessionmaker

from Classes import Usuario, Permissao, PermissaoUsuario, engine

DBSession = sessionmaker(bind=engine)


def inserir_usuario(matricula, nome, email, login, senha):
    usuario = Usuario(matricula=matricula, nome=nome, email=email, login=login, senha=senha)
    session = DBSession()
    session.add(usuario)
    session.commit()
    session.close()


def inserir_permissao(id, descricao):
    permissao = Permissao(id=id, descricao=descricao)
    session = DBSession()
    session.add(permissao)
    session.commit()
    session.close()


def inserir_permissao_usuario(matricula, permissao):
    permissao_usuario = PermissaoUsuario(matricula=matricula, permissao=permissao)
    session = DBSession()
    session.add(permissao_usuario)
    session.commit()
    session.close()


def listar_usuarios():
    session = DBSession()
    usuarios = session.query(Usuario).all()
    session.close()
    return usuarios


def listar_permissoes():
    session = DBSession()
    permissoes = session.query(Permissao).all()
    session.close()
    return permissoes


def listar_permissoes_usuarios():
    session = DBSession()
    permissoes = session.query(PermissaoUsuario).all()
    session.close()
    return permissoes


if __name__ == '__main__':
    inserir_usuario(1616415, 'Pedro Becker', 'phgbecker@gmail.com', 'phgbecker', '*7&%656q12')
    inserir_permissao(1, 'DONO')
    inserir_permissao_usuario(1616415, 1)

    for usuario in listar_usuarios():
        print('Matrícula = {} - Nome = {} - Email = {} - Login = {} - Senha = {}'.format(
            usuario.matricula,
            usuario.nome,
            usuario.email,
            usuario.login,
            usuario.senha
        ))

    for permissao in listar_permissoes():
        print('ID = {} - Descrição  = {}'.format(
            permissao.id,
            permissao.descricao,
        ))

    for permissoes_usuarios in listar_permissoes_usuarios():
        print('Matricula = {} - Permissão = {}'.format(
            permissoes_usuarios.matricula,
            permissoes_usuarios.permissao)
        )
