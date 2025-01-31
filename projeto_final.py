from PyQt5.QtWidgets import QApplication,  QWidget , QLabel , QLineEdit , QPushButton, QVBoxLayout , QMessageBox

import sys



class projeto(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(10,40,400,300)
                         
#  nome da barra
        self.setWindowTitle("Finalizar Vendas")

        # gerenciador de layout vertical
        self.projeto_final = QVBoxLayout()


  # labels para os dados do cliente
        self.label_vendas = QLabel("Finalizar Vendas")
        self.label_vendas.setStyleSheet("QLabel{font-size:15pt;color:red}")

        self.projeto_final.addWidget(self.label_vendas)
# ------------------------------------------------------
        self.label_total = QLabel("Total da venda:")
        self.label_total.setStyleSheet("QLbel{font-size:13pt;color:black}")

        self.projeto_final.addWidget(self.label_total)


        # Edit Caixinha na DIREITA ----------------------- lado DIREITO

      
# ------------------------------------------------------
        self.label_desconto = QLabel("Desconto:")
        self.label_desconto.setStyleSheet("Qlabel{font-size:13pt;color:black}")

        self.projeto_final.addWidget(self.label_desconto)

# ------------------------------------------------------

        self.label_acrescimo = QLabel("Acréscimo:")
        self.label_acrescimo.setStyleSheet("Qlabel{font-size:13pt;color:black}")

        self.projeto_final.addWidget(self.label_acrescimo)
# --------------------------------------------------------
        self.label_liquido = QLabel("Total Liquído:")
        self.label_liquido.setStyleSheet("Qlabel{font-size:13pt;color:black}")

        self.projeto_final.addWidget(self.label_liquido)
# -----------------------------------------------------
        self.label_troco = QLabel("Troco:")
        self.label_troco.setStyleSheet("Qlabel{font-size:13pt;color:black}")
        

        self.projeto_final.addWidget(self.label_troco)
# ---------------------------------------------------


# Edit Caixinha na esquerda

       
#---------------------------------------------------------
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{Font-size:12pt}")

        self.edit_patrimonio = QLineEdit()
        self.edit_patrimonio.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")
        

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

    #  adicionar o layout na tela
        self.setLayout(self.projeto_final)
       
app = QApplication(sys.argv)

# iniciar a janela
tela = projeto() 
# Exibir na tela durante a execução

tela.show()
# clicar e sair da tela e sair da memória
app.exec() 

























