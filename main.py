from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from mainUI import Ui_MainWindow
from atendenteUI import Ui_Form_Atendente
from pedidosUI import Ui_Form_Pedidos
from vendasUI import Ui_Form
from cardapioUI import Ui_Form_Cardapio
from pedidoSelecUI import Ui_Form_PedidoSelec
from logica import Item, Pedido, Sistema

dicPreco ={
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

class AtendenteWindow(QtWidgets.QWidget, Ui_Form_Atendente): #pronto
    def __init__(self, sistema):
        super().__init__()
        self.setupUi(self)
        self.checkoutButton.clicked.connect(self.cart)
        self.pagoButton.clicked.connect(self.pago) #n direciona pro cart, faz um outro
        self.sistema = sistema
        self.pedido = Pedido()
        self.total = 0.0


    
    def cart(self, checked):
        item = Item()
        first_page = self.tabWidget.widget(0)
        toolbox = first_page.findChild(QtWidgets.QToolBox)
        for index in range(toolbox.count()): #parte pra pegar os nomes e quantidades dos itens do menu
            widget = toolbox.widget(index)
            form_layouts = widget.findChildren(QtWidgets.QFormLayout)
            for form_layout in form_layouts:
                for i in range(form_layout.rowCount()):
                    label_item = form_layout.itemAt(i, QtWidgets.QFormLayout.LabelRole)
                    spinbox_item = form_layout.itemAt(i, QtWidgets.QFormLayout.FieldRole)
                    if label_item is not None:
                        label = label_item.widget()
                        if isinstance(label, QtWidgets.QLabel):
                            item._nome = label.text()
                            item._preco = dicPreco[label.text()]
                    if spinbox_item is not None:
                        spinbox = spinbox_item.widget()
                        if isinstance(spinbox, QtWidgets.QSpinBox):
                            item._quant = spinbox.value()
                    if item._quant > 0:
                        self.pedido.adiciona_itens(item._nome, item._preco, item._quant)
        self.tabWidget.setCurrentIndex(1)
        self.checkout()

    def checkout(self):
        second_page = self.tabWidget.widget(1)
        vbox = second_page.findChild(QtWidgets.QVBoxLayout)
        for index in range(len(self.pedido._lista_itens)):
            hbox = QtWidgets.QHBoxLayout()
            hbox.addWidget(QtWidgets.QLabel(self.pedido._lista_itens[index][0]))
            hbox.addWidget(QtWidgets.QLabel(str(self.pedido._lista_itens[index][2])))
            vbox.addLayout(hbox)
            self.total += self.pedido._lista_itens[index][1]
        self.labelPrecoTotal.setText(str(self.total))
    
    def pago(self):
        self.pedido.id = self.spinMesa.value()
        self.sistema.adiciona_pedido(self.pedido)
        self.sistema.faturaTotal = self.total
        for index in range(len(self.pedido._lista_itens)):
            self.sistema.adiciona_item_vendido(self.pedido._lista_itens[index][0], self.pedido._lista_itens[index][2])
        self.close()

class PedidosWindow(QtWidgets.QWidget, Ui_Form_Pedidos):
    def __init__(self, sistema):
        super().__init__()
        self.setupUi(self)
        self.sistema = sistema
        self.sistema.cria_lista_status()
        self.listaID = []
        self.listaButton = []
        for index in range(len(self.sistema._listaStatus)):#ajeita o listaStatus e eras, ai tem que botar pushButtons dependendo do status e fazer uma tela que mostra os itens, além de um checkbox pra cada etapa do preparo que muda o status do pedido
           for x in range(len(self.sistema._listaStatus[index])):
                button = QtWidgets.QPushButton()
                button.setText("Pedido " + str(sistema._listaStatus[index][x]))
                self.listaID.append(sistema._listaStatus[index][x])
                if index == 0:
                    self.layoutAguardo.addWidget(button)
                elif index == 1:
                    self.layoutPreparo.addWidget(button)
                else:
                    self.layoutFinalizado.addWidget(button)
                self.listaButton.append(button)
        for x in range(len(self.listaButton)):
            self.listaButton[x].clicked.connect(lambda checked, id=self.listaID[x]: self.show_pedido_window(self, id))
    
    def show_pedido_window(self, checked, identidade):
        self.close()
        self.w = PedidoSelecWindow(self.sistema, identidade)
        self.w.show()

                   
class PedidoSelecWindow(QtWidgets.QWidget, Ui_Form_PedidoSelec):
    def __init__(self, sistema, identidade):
        super().__init__()
        self.setupUi(self)
        self.identidade = identidade
        self.sistema = sistema
        if self.sistema._listaPedidos[self.identidade].status == "pedido":
            self.radioButton_3.setChecked(True)
        elif self.sistema._listaPedidos[self.identidade].status == "preparo":
            self.radioButton_2.setChecked(True)
        else:
            self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.finalizado)
        self.radioButton_2.toggled.connect(self.preparo)
        vbox = self.verticalLayout
        vbox.setAlignment(Qt.AlignTop)
        for x in range(len(self.sistema._listaPedidos)):
            if self.sistema._listaPedidos[x].id == self.identidade:
                for index in range(len(self.sistema._listaPedidos[x]._lista_itens)):
                    hbox = QtWidgets.QHBoxLayout()
                    hbox.addWidget(QtWidgets.QLabel(self.sistema.listaPedidos[x]._lista_itens[index][0]))
                    hbox.addWidget(QtWidgets.QLabel(str(self.sistema.listaPedidos[x]._lista_itens[index][2])))
                    vbox.addLayout(hbox)
    
    def finalizado(self, checked):
        for x in range(len(self.sistema._listaPedidos)):
            if self.sistema._listaPedidos[x].id == self.identidade:
                self.sistema._listaPedidos[x].status = "pronto"
                
    def preparo(self, checked):
        for x in range(len(self.sistema._listaPedidos)):
            if self.sistema._listaPedidos[x].id == self.identidade:
                self.sistema._listaPedidos[x].status = "preparo"


class VendasWindow(QtWidgets.QWidget, Ui_Form): #pronto
    def __init__(self, sistema):
        super().__init__()
        self.setupUi(self)
        self.sistema = sistema
        self.totalValor.setText(str(sistema.faturaTotal))
        vbox = self.verticalLayout
        for index in range(len(self.sistema._itensVendidos)):
            hbox = QtWidgets.QHBoxLayout()
            hbox.addWidget(QtWidgets.QLabel(self.sistema._itensVendidos[index][0]))
            hbox.addWidget(QtWidgets.QLabel(str(self.sistema._itensVendidos[index][1])))
            vbox.addLayout(hbox)

class CardapioWindow(QtWidgets.QWidget, Ui_Form_Cardapio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.atendenteButton.clicked.connect(self.show_atendente_window)
        self.pedidosButton.clicked.connect(self.show_pedidos_window)
        self.vendasButton.clicked.connect(self.show_vendas_window)
        self.cardapioButton.clicked.connect(self.show_cardapio_window)
        self.sistema = Sistema()
        
    
    def show_atendente_window(self, checked):
        self.w = AtendenteWindow(self.sistema)
        self.w.show()
    
    def show_pedidos_window(self, checked):
        self.w = PedidosWindow(self.sistema)
        self.w.show()
    
    def show_vendas_window(self, checked):
        self.w = VendasWindow(self.sistema)
        self.w.show()
    
    def show_cardapio_window(self, checked):
        self.w = CardapioWindow()
        self.w.show()

app = QtWidgets.QApplication([])
w = MainWindow()
w.show()
app.exec()
