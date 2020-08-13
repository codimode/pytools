from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    result = enviador.enviar(
        'renzo@python.pro.br',
        'luciano@pytho.pro.br',
        'Cursos Python Pro',
        'Primeira turma aberta'
    )
    assert 'renzo@python.pro.br' in result
