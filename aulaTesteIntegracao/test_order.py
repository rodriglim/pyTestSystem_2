from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository


def test_new_order_with_product_total_price():
    # Arrange
    cliente = Cliente(1, "Rodrigo")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Leite", 50, 10)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    order_product1 = PedidoProduto()
    order_product1.adicionar_produto(product1, 5)
    pedido.adicionar_produto_pedido(order_product1)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 250


def test_new_order_without_product():
    # Arrange
    cliente = Cliente(1, "Rodrigo")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Acucar", 50, 10)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()
    pedido_produto.adicionar_produto(product1, 15)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 0



def test_new_processar_pedido():
    cliente = Cliente(1, "Rodrigo")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 100)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()
    pedido_produto.adicionar_produto(product1, 15)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Act
    pedido_produto.processar_pedido(product1, 30)

    # Assert
    assert product1.estoque==55

def test_new_baixar_estoque():
    cliente = Cliente(1, "Rodrigo")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 100)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()
    pedido_produto.adicionar_produto(product1, 15)
    pedido.adicionar_produto_pedido(pedido_produto)

    product1.baixar_estoque(30)

    # Assert
    assert product1.estoque == 55

def test_se_baixar_estoque_retorna_o_estoque_correto():
    product1 = Produto(1,"acucar", 40,80)
    product1.baixar_estoque(30)

    # Assert
    assert product1.estoque == 50
