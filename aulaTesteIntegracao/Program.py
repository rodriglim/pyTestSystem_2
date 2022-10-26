from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.PedidoRepository import PedidoRepository
from Repositories.ProdutoRepository import ProdutoRepository

customer1 = Cliente(1, "Rodrigo")


customer_repository = ClienteRepository()
customer_repository.adicionar_cliente(customer1)

product1 = Produto(1, "Pão", 8.78, 2)
product2 = Produto(2, "Leite", 11.00, 11)


product_repository = ProdutoRepository()
product_repository.adicionar_produto(product1)
product_repository.adicionar_produto(product2)




pedido = Pedido(1, customer1, datetime.today)
order_product1 = PedidoProduto()
order_product2 = PedidoProduto()
print(order_product1.adicionar_produto(product2, 5))
print(order_product2.adicionar_produto(product1, 10))
pedido.adicionar_produto_pedido(order_product1)
pedido.adicionar_produto_pedido(order_product2)
pedido.atualizar_preco_total()

print("\n** Relatório de pedido **")
print(pedido)


print("\n** Relatório dos produtos **")
print(product_repository)
