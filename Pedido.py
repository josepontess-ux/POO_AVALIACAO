class pedido:
  def __init__(self, nome, produto, quantidade, preco_unitario, cupom):
    self.nome = nome
    self.produto = produto
    self.quantidade = quantidade
    self.preco_unitario = preco_unitario
    self.cupom = cupom.lower()

def calcular_subtotal(self):
    """
    Retorna o Subtotal numérico.
    """
    subtotal = quantidade*preco_unitario
    return subtotal

def calcular_desconto(self, subtotal, cupom):
  """
  Retorna o valor do desconto
  """
        if cupom == "sim":
            desconto = subtotal * 0.10
        else:
            desconto = 0

        return desconto

