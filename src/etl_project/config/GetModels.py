from config.models.VwEstacao import VwEstacao
from config.models.Intervalos import Intervalos
from config.models.MovPeriodo import MovPeriodo
from config.models.TipoDiaBilh import BilhTipoDia
from config.models.AcompanhamentoPCD import AcompanhamentoPCD
from config.sql.views.intervalos import INTERVALOS_VIEW
from config.sql.views.passag_per_tipo_dia import PASSAG_PER_TIPO_DIA
from config.sql.views.acompanhamento_pcd import ACOMPANHAMENTO_PCD
from config.sql.views.pcd_hora_linha import PCD_HORA_LINHA
from config.sql.views.bilh_tipo_dia import BILH_TIPO_DIA

class GetModels():
    @staticmethod
    def get_model_by_path(path):
        model_path = {
            "dmo_anl_vw_estacao": [VwEstacao,[]],
            
            "dmo_anl_vw_tot_mov_periodo": [MovPeriodo, [PASSAG_PER_TIPO_DIA]],
            "acompanhamento_pcd": [AcompanhamentoPCD, [ACOMPANHAMENTO_PCD, PCD_HORA_LINHA]],
            "intervalos": [Intervalos, [INTERVALOS_VIEW]],
            "bilh_tipo_dia": [BilhTipoDia, [BILH_TIPO_DIA]]
        }

        return model_path.get(path)