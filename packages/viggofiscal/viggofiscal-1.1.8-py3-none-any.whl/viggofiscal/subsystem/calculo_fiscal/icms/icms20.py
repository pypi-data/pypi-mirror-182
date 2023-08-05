from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.icms.base_reduzida_icms_proprio \
    import BaseReduzidaIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.icms.icms00 \
    import Icms00
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt

class Icms20():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_ipi: Decimal, valor_desconto: Decimal,
                 aliquota_icms_proprio: Decimal, percentual_reducao: Decimal):
        self.valor_produto = valor_produto
        self.valor_frete = valor_frete
        self.valor_seguro = valor_seguro
        self.despesas_acessorias = despesas_acessorias
        self.valor_ipi = valor_ipi
        self.valor_desconto = valor_desconto
        self.aliquota_icms_proprio = aliquota_icms_proprio
        self.percentual_reducao = percentual_reducao
        self.base_reduzida_icms = BaseReduzidaIcmsProprio(
            valor_produto, valor_frete, valor_seguro, despesas_acessorias,
            valor_desconto, percentual_reducao, valor_ipi)
    
    def base_reduzida_icms_proprio(self):
        return self.base_reduzida_icms.calcular_base_reduzida_icms_proprio()
    
    def valor_icms_proprio(self) -> Decimal:
        base_reduzida_icms = self.base_reduzida_icms_proprio()
        valor_icms = base_reduzida_icms * (self.aliquota_icms_proprio / 100)
        return round_abnt(valor_icms, 2)

    def valor_icms_desonerado(self) -> Decimal:
        icms00 = Icms00(
            self.valor_frete, self.valor_seguro, self.despesas_acessorias,
            self.valor_ipi, self.valor_desconto, self.aliquota_icms_proprio)
        valor_icms_normal = icms00.valor_icms_proprio()
        valor_icms_desonerado = valor_icms_normal - self.valor_icms_proprio()
        return round_abnt(valor_icms_desonerado, 2)