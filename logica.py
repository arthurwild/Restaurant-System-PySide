class Item:
    def __init__(self):
        self._nome = ""
        self._quant = 0
        self._preco = 0.0
        self._diciPreco ={
            "Fetuccine Alfredo" : 20.00,
            "Spaghetti Carbonara" : 25.00,
            "Gnocci al Pesto" : 30.00,
            "Mac 'n Cheese Kids" : 15.00,
            "Fusli Bolonhesa" : 20.00,
            "Refrigerante" : 5.00,
            "Suco Natural" : 6.00,
            "Água" : 3.00,
            "Salada Caprese" : 15.00,
            "Polenta Brustolada" : 10.00,
            "Sopa de Capeletti" : 18.00,
            "Petit Gateau" : 15.00,
            "Sorvete" : 10.00
        }
    
    @property
    def nome(self):
        return self._nome
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, nome):
        self._preco = self._dicPreco[nome]
    @property
    def quant(self):
        return self._quant
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @quant.setter
    def quant(self, quant):
        self._quant = quant

class Pedido:
    def __init__(self):
        self._lista_itens = []
        self._status= "pedido"
        self._id = 0
    @property
    def listaItens(self):
        return self._lista_itens
    @property
    def status(self):
        return self._status
    @property
    def id(self):
        return self._id
    @status.setter
    def status(self, novoStatus):
        self._status = novoStatus
    def adiciona_itens(self, nome, preco, quant):
        lista = [nome, preco, quant]
        self._lista_itens.append(lista)
    @id.setter
    def id(self, val):
        self._id = val

class Sistema:
    def __init__(self):
        self._faturaTotal = 0.0
        self._itensVendidos = [] #primeiro slot para o nome dos itens, segundo para quant
        self._listaPedidos = [] #slot para os itens nos pedidos
        self._listaId = []
        self._listaStatus = [[],[],[]] #primeiro slot para itens pedidos, segundo para preparo, terceiro para prontos
    
    @property
    def listaStatus(self):
        return self._listaStatus
    def cria_lista_status(self):
        self._listaStatus = [[],[],[]] #reseta a lista de status pra n repetir as que ja tavam
        for x in range(len(self._listaPedidos)):
            if self._listaPedidos[x].status == "pedido":
                self._listaStatus[0].append(self._listaPedidos[x].id)
            elif self._listaPedidos[x].status == "preparo":
                self._listaStatus[1].append(self._listaPedidos[x].id)
            else:
                self._listaStatus[2].append(self._listaPedidos[x].id)
    @property
    def faturaTotal(self):
        return self._faturaTotal
    @property
    def listaPedidos(self):
        return self._listaPedidos
    @property
    def itensVendidos(self):
        return self._itensVendidos
    @faturaTotal.setter
    def faturaTotal(self, val):
        self._faturaTotal += val

    def adiciona_pedido(self, pedido:Pedido):
        self._listaPedidos.append(pedido)

    def adiciona_item_vendido(self, nome, quant):
        lista =[nome, quant]
        self._itensVendidos.append(lista)
    
    
