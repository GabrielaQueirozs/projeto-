

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QSpacerItem, QSizePolicy
)
import sys

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar a geometria da tela (posição X e Y, largura e altura)
        self.setGeometry(300, 20, 600, 150)  
        self.setWindowTitle("Caixa")

        # Layout principal vertical
        self.layout_v_total = QVBoxLayout()

        # titulo "cabeçalho"
        self.label_titulo = QLabel("Finalizar Venda                     Gabis´s")
        self.label_titulo.setStyleSheet("QLabel{background-color:pink; font-size: 17px; font-weight: italic; padding: 5px;}")
        self.label_titulo.setFixedHeight(50)  
        self.layout_v_total.addWidget(self.label_titulo)
        

        # dados
        self.layout_h_dados = QHBoxLayout()

        # coluna esquerda
        self.layout_v_esquerda = QVBoxLayout()

        # total venda primeira caixa
        self.layout_h_total_venda = QHBoxLayout()
        self.label_venda = QLabel("Total de Venda")

        self.label_venda.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_venda = QLineEdit("R$ 0,00")
        self.edit_venda.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)
        self.layout_v_esquerda.addLayout(self.layout_h_total_venda)

        # desconto 
        self.layout_h_desconto = QHBoxLayout()
        self.label_desc = QLabel("Desconto:")
        self.label_desc.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_desc = QLineEdit("R$ 0,00")
        self.edit_desc.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)
        self.layout_v_esquerda.addLayout(self.layout_h_desconto)


        # acrescimo
        self.layout_h_acrecimo = QHBoxLayout()
        self.label_acre = QLabel("Acréscimo:")
        self.label_acre.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_acre = QLineEdit("R$ 0,00")
        self.edit_acre.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_acrecimo.addWidget(self.label_acre)
        self.layout_h_acrecimo.addWidget(self.edit_acre)
        self.layout_v_esquerda.addLayout(self.layout_h_acrecimo)



        # total liquido
        self.layout_h_total_liquido = QHBoxLayout()
        self.label_liquido = QLabel("Total Líquido:")
        self.label_liquido.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_liquido = QLineEdit("R$ 0,00")
        self.edit_liquido.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_total_liquido.addWidget(self.label_liquido)
        self.layout_h_total_liquido.addWidget(self.edit_liquido)
        self.layout_v_esquerda.addLayout(self.layout_h_total_liquido)






        # troco
        self.layout_h_total_troco = QHBoxLayout()
        self.label_troco = QLabel(" Troco:")
        self.label_troco.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_troco = QLineEdit("R$ 0,00")
        self.edit_troco.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_total_troco.addWidget(self.label_troco)
        self.layout_h_total_troco.addWidget(self.edit_troco)
        self.layout_v_esquerda.addLayout(self.layout_h_total_troco)

        self.layout_h_dados.addLayout(self.layout_v_esquerda)

        # coluna direita 
        self.layout_v_direita = QVBoxLayout()

        # cliente
        self.layout_h_cliente = QHBoxLayout()
        self.label_cliente = QLabel("Cliente:")
        self.label_cliente.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_cliente = QLineEdit(" ")
        self.edit_cliente.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_cliente.addWidget(self.label_cliente)
        self.layout_h_cliente.addWidget(self.edit_cliente)
        self.layout_v_direita.addLayout(self.layout_h_cliente)

        # vendedor
        self.layout_h_vendedor = QHBoxLayout()
        self.label_vendedor = QLabel("Vendedor:")
        self.label_vendedor.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_vendedor = QLineEdit(" ")
        self.edit_vendedor.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_vendedor.addWidget(self.label_vendedor)
        self.layout_h_vendedor.addWidget(self.edit_vendedor)
        self.layout_v_direita.addLayout(self.layout_h_vendedor)

        # pagamento
        self.layout_h_pagamento = QHBoxLayout()
        self.label_pagamento = QLabel("Forma de Pagamento:")
        self.label_pagamento.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.combo_pagamento = QComboBox()
        self.combo_pagamento.addItems(["DINHEIRO", "CARTÃO", "PIX", "BOLETO"])


        self.label_valor = QLabel("Valor:")
        self.label_valor.setStyleSheet("QLabel{background-color:pink; font-size: 10px; font-weight: roman; padding: 5px;}")
        self.edit_valor = QLineEdit("R$ 0,00")
        self.edit_valor.setStyleSheet("QLineEdit{background-color:#f4e1e7;}")

        self.layout_h_pagamento.addWidget(self.label_pagamento)
        self.layout_h_pagamento.addWidget(self.combo_pagamento)
        self.layout_h_pagamento.addWidget(self.label_valor)
        self.layout_h_pagamento.addWidget(self.edit_valor)

        self.layout_v_direita.addLayout(self.layout_h_pagamento)

        # Caixa de texto
        self.label_obs = QLabel("")
        self.text_obs = QTextEdit()
        self.text_obs.setFixedHeight(60)  
        self.layout_v_direita.addWidget(self.label_obs)
        self.layout_v_direita.addWidget(self.text_obs)

        self.layout_h_dados.addLayout(self.layout_v_direita)
        self.layout_v_total.addLayout(self.layout_h_dados)

     # rodapé  
        self.layout_h_botoes = QHBoxLayout()

        self.btn_cupom = QPushButton("Cupom Fiscal")

        self.btn_pedido = QPushButton("Pedido de Venda")
        self.btn_nfc_online = QPushButton("NFC-e OnLine")
        self.btn_nfc_offline = QPushButton("NFC-e OffLine")
        self.btn_sair = QPushButton("Sair")

        self.layout_h_botoes.addWidget(self.btn_cupom)
        self.layout_h_botoes.addWidget(self.btn_pedido)
        self.layout_h_botoes.addWidget(self.btn_nfc_online)
        self.layout_h_botoes.addWidget(self.btn_nfc_offline)
        self.layout_h_botoes.addWidget(self.btn_sair)

        self.layout_v_total.addLayout(self.layout_h_botoes)
# fim do rodapé
        # Definir o layout principal
        self.setLayout(self.layout_v_total)

app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()