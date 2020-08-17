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
    ses = conexao.gerar_sessao()
    yield ses
    ses.roll_back()
    ses.fechar()
