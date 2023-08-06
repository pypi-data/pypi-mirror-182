from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal import utils


class ValorIcmsProprio():

    def __init__(self, base_calculo: Decimal, aliq_icms_proprio: Decimal):
        self.base_calculo = base_calculo
        self.aliq_icms_proprio = aliq_icms_proprio
    
    def calcular_valor_icms_proprio(self):
        return utils.round_abnt(
            (self.aliq_icms_proprio / 100 * self.base_calculo), 2)
