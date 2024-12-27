import pytest
from config.models.VwEstacao import VwEstacao
from config.models.Intervalos import Intervalos
from config.models.MovPeriodo import MovPeriodo
from config.models.AcompanhamentoPCD import AcompanhamentoPCD
from config.sql.views.intervalos import INTERVALOS_VIEW
from config.sql.views.mov_periodo_view import MOV_PERIODO_COMMAND
from config.sql.views.acompanhamento_pcd import ACOMPANHAMENTO_PCD
from config.GetModels import GetModels

def test_get_model_by_path_valid_key():
    # Test for a valid key
    result = GetModels.get_model_by_path("dmo_anl_vw_estacao")
    assert result is not None
    assert result[0] == VwEstacao
    assert result[1] == ""

def test_get_model_by_path_another_valid_key():
    # Test for another valid key
    result = GetModels.get_model_by_path("intervalos")
    assert result is not None
    assert result[0] == Intervalos
    assert result[1] == INTERVALOS_VIEW

def test_get_model_by_path_invalid_key():
    # Test for an invalid key
    result = GetModels.get_model_by_path("invalid_key")
    assert result is None
