from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal import utils


class BaseIcmsProprio():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_desconto: Decimal, valor_ipi: Decimal=Decimal('0.0')):
        self.valor_produto = valor_produto
        self.valor_frete = valor_frete
        self.valor_seguro = valor_seguro
        self.despesas_acessorias = despesas_acessorias
        self.valor_desconto = valor_desconto
        self.valor_ipi = valor_ipi
    
    def calcular_base_icms_proprio(self) -> Decimal:
        base_icms_proprio = (
            self.valor_produto + self.valor_frete + self.valor_seguro +
            self.despesas_acessorias + self.valor_ipi - self.valor_desconto)
        return utils.round_abnt(base_icms_proprio, 2)
