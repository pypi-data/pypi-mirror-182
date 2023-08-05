from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.icms.base_icms_proprio \
    import BaseIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.icms.valor_icms_proprio \
    import ValorIcmsProprio

class Icms00():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_ipi: Decimal, valor_desconto: Decimal,
                 aliquota_icms_proprio: Decimal):
        self.valor_produto = valor_produto
        self.valor_frete = valor_frete
        self.valor_seguro = valor_seguro
        self.despesas_acessorias = despesas_acessorias
        self.valor_ipi = valor_ipi
        self.valor_desconto = valor_desconto
        self.aliquota_icms_proprio = aliquota_icms_proprio
        self.base_icms = BaseIcmsProprio(
            valor_produto, valor_frete, valor_seguro, despesas_acessorias,
            valor_desconto, valor_ipi)
    
    def base_icms_proprio(self):
        return self.base_icms.calcular_base_icms_proprio()
    
    def valor_icms_proprio(self) -> Decimal:
        return ValorIcmsProprio(
            self.base_icms_proprio(), self.aliquota_icms_proprio).\
            calcular_valor_icms_proprio()
