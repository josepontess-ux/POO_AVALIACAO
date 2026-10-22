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

 def classificar_pedido(self, subtotal):
   """
   Retorna a classificação do tipo do pedido
   """
   if subtotal <= 30:
            classificacao = "Pedido pequeno"
        elif subtotal <= 100:
            classificacao = "Pedido médio"
        else:
            classificacao = "Pedido grande"

        return classificacao

def exibir_resumo(self):
  """
  exebir o resumo do pedido, e o total
  """
  subtotal = calcular_subtotal(quantidade, preco_unitario)
  desconto = calcular_desconto(subtotal, cupom)
  total = subtotal - desconto
  classificação = classificar_pedido(subtotal)

print("===== RESUMO DO PEDIDO ======")
print(f"Cliente: {nome}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Subtotal: R$ {subtotal:.2}")
print(f"Desconto: R$ {desconto:.2}")
print(f"Total: R$ {total:.2}")
print(f"Classificação: {classificação}")

