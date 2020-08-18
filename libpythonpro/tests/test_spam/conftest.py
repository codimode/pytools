import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # setup
    con = Conexao()
    yield con
    # Tear down
    con.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
