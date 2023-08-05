from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt


class BaseReduzidaIcmsProprio():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_desconto: Decimal, percentual_reducao: Decimal,
                 valor_ipi: Decimal=Decimal('0.0')):
        self.valor_produto = valor_produto 
        self.valor_frete = valor_frete
        self.valor_seguro = valor_seguro
        self.despesas_acessorias = despesas_acessorias
        self.valor_desconto = valor_desconto
        self.percentual_reducao = percentual_reducao
        self.valor_ipi = valor_ipi
    
    def calcular_base_reduzida_icms_proprio(self) -> Decimal:
        base_icms = (
            self.valor_produto + self.valor_frete + self.valor_seguro +
            self.despesas_acessorias - self.valor_desconto)
        base_reduzida_icms_proprio = (
            base_icms - (base_icms * (self.percentual_reducao / 100)) +
            self.valor_ipi)
        return round_abnt(base_reduzida_icms_proprio, 2)
