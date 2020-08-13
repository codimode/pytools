import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['renzo@python.pro.br', 'foo@bar.pro.br'])
def test_remetente(remetente):
    enviador = Enviador()
    result = enviador.enviar(
        remetente,
        'luciano@pytho.pro.br',
        'Cursos Python Pro',
        'Primeira turma aberta'
    )
    assert remetente in result


@pytest.mark.parametrize('remetente', ['renzo', ''])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        result = enviador.enviar(
            remetente,
            'luciano@pytho.pro.br',
            'Cursos Python Pro',
            'Primeira turma aberta'
        )
