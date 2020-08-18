from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Pedro', email='pedro@qwer.com.br'),
            Usuario(nome='Paulo', email='paulo@qwer.com.br')
        ],
        [
            Usuario(nome='Pedro', email='pedro@qwer.com.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for u in usuarios:
        sessao.salvar(u)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'asdf@qwer.com.br',
        'titulo',
        'conteudo')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    u = Usuario(nome='pcampos', email='pcampos@qwer.com.br')
    sessao.salvar(u)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'asdf@qwer.com.br',
        'titulo',
        'conteudo')
    enviador.enviar.assert_called_once_with(
        'asdf@qwer.com.br',
        'pcampos@qwer.com.br',
        'titulo',
        'conteudo')
