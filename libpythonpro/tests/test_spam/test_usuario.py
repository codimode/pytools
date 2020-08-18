from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Pedro Campos', email='pcampos@qwer.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Pedro', email='pcampos@qwer.com.br'), Usuario(nome='Paulo', email='pcampos@qwer.com.br')]
    for u in usuarios:
        sessao.salvar(u)
    assert usuarios == sessao.listar()
