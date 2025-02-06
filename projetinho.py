from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox, QTextEdit
import sys 

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,30,600,800)

        # Texto para a barra de título
        self.setWindowTitle("Caixa")

        #Layout vertical da tela inteira
        self.layout_v_total = QVBoxLayout()

        #Label titulo
        self.label_titulo = QLabel("Finalizar Venda")
        self.label_titulo.setStyleSheet("QLabel{background-color:white}")
        # adicionar a label de titulo ao layout
        self.layout_v_total.addWidget(self.label_titulo)







        #Label dados
        self.label_dados = QLabel()

        # Criar e adicionar um layout horizontal para 
        # os dados da compra
        self.layout_h_dados = QHBoxLayout()

        #================================================================================
        # criar label da esquerda ######################################
        self.label_esquerda = QLabel()
        # Criar um layout vertical
        self.layout_v_esquerda = QVBoxLayout()
        # label para guardar o texto Total de venda
        # e a caixa total de venda, ou seja, irá
        # a guardar uma nova label e uma lineEdit
       
    #    ===================Total Venda==============================
       
        self.label_total_venda = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_venda = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_venda = QLabel("Total de Venda")
        # Criar a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_venda)

# ================== Fim do total venda ======================================


# =================== Inicio do Desconto ====================================

        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Desconto")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Desconto =========================================

# =================================== Acréscimo ===========================

        # Adicionar o layout vertical da esquerda
        # na coluna da esquerda
        self.label_esquerda.setLayout(self.layout_v_esquerda)

        self.label_esquerda.setStyleSheet("QLabel{background-color:gray}")
        # adicionar a label da esquerda no layout 
        # horizontal
        self.layout_h_dados.addWidget(self.label_esquerda)
        #=============================================================

 #    ===================Acréscimo==============================
       
        self.label_acrescimo = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_acrescimo = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_acre = QLabel("Total de Acréscimo")
        # Criar a LineEdit que recebe o total de venda
        self.edit_acre = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_acrescimo.addWidget(self.label_acre)
        self.layout_h_acrescimo.addWidget(self.edit_acre)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_acrescimo.setLayout(self.layout_h_acrescimo)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_acrescimo)

# ================== Fim do Acréscimo ======================================

 #    ===================Inicio Total Líquido==============================
       
        self.label_total_liquido = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_liquido = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_total_liqui = QLabel("Total de Líquido")
        # Criar a LineEdit que recebe o total de venda
        self.edit_total_liqui = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_liquido.addWidget(self.label_total_liqui)
        self.layout_h_total_liquido.addWidget(self.edit_total_liqui)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_liquido.setLayout(self.layout_h_total_liquido)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_liquido)

# ================== Fim do Total Líquido ======================================

 #    ===================Total de Troco==============================
       
        self.label_troco= QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_troco = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_troc= QLabel("Total do Troco")
        # Criar a LineEdit que recebe o total de venda
        self.edit_troc = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_troco.addWidget(self.label_troc)
        self.layout_h_troco.addWidget(self.edit_troc)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_troco.setLayout(self.layout_h_troco)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_troco)

# ================== Fim do Troco ======================================


         # criar label da direita
        #self.label_direita = QLabel()
        #self.label_direita.setStyleSheet("QLabel{background-color:yellow}")
        # adicionar a label da direita no layout 
        # horizontal
        #self.layout_h_dados.addWidget(self.label_direita)
#==============================================================================
        self.label_cliente = QLabel ()
        
        self.layout_cliente= QHBoxLayout()

        self.label_clie= QLabel("Cliente")
        
        self.edit_clie = QLineEdit("1-Consumidor final")

        self.label_vendedor = QLabel("Vendedor")
        self.edit_vendedor = QLineEdit("999-SYNDATA")


        self.layout_cliente.addWidget(self.label_clie)
        self.layout_cliente.addWidget(self.edit_clie)
        
        self.layout_cliente.addWidget(self.label_vendedor)
        self.layout_cliente.addWidget(self.edit_vendedor)

        self.label_cliente.setLayout(self.layout_cliente)
        

        self.layout_h_dados.addWidget(self.label_cliente)
#=======================================================================================
        #self.label_vendedo = QLabel()

        #self.layout_vendedor = QHBoxLayout()

        #self.label_vendedor = QLabel("Vendedor")
        #self.edit_vendedor = QLineEdit("999-SYNDATA")

        #self.layout_vendedor.addWidget(self.label_vendedor)
        #self.layout_vendedor.addWidget(self.edit_vendedor)

        #self.label_vendedo.setLayout(self.layout_vendedor)

        
        #self.layout_h_dados.addWidget(self.label_vendedo)
#=====================================================================================
        self.label_formas = QLabel()

        self.layout_formas = QHBoxLayout ()

        self.label_forma = QLabel ("Formas de pagamento")
        self.edit_forma = QLineEdit("1-dinheiro")
        self.edit_forma1 = QLineEdit("R$0,00")
        
        

        self.layout_formas.addWidget(self.label_forma)
        self.layout_formas.addWidget(self.edit_forma)
        self.layout_formas.addWidget(self.edit_forma1)
        

        self.label_formas.setLayout(self.layout_formas)

        self.layout_h_dados.addWidget(self.label_formas)
        #==============================================================================
        self.label_caixa = QLabel()

        self.layout_caixa = QVBoxLayout()

        self.caix = QLineEdit ()
        self.caix.setFixedSize(300,80)

        self.layout_caixa.addWidget(self.caix)

        self.label_caixa.setLayout(self.layout_caixa)

        self.layout_h_dados.addWidget(self.label_caixa)
        

#======================================================================================
        self.label_dados.setLayout(self.layout_h_dados)
        self.label_dados.setStyleSheet("QLabel{background-color:red}")
        self.layout_v_total.addWidget(self.label_dados)
        
        









        #Label rodape
        #self.label_rodape = QLabel()
        #self.label_rodape.setStyleSheet("QLabel{background-color:green}")
        #self.layout_v_total.addWidget(self.label_rodape)

#==============================================================================
        #self.label_selecao = QLabel()

        #self.layout_selecao = QVBoxLayout()
        
        #self.label_seleca = QLabel("Selecione o Documento para emissão")

        #self.layout_selecao.addWidget(self.label_seleca)

        #self.label_selecao.setLayout(self.layout_selecao)

       # self.layout_v_total.addWidget(self.label_selecao)
#==============================================================================
        #self.label_primeiro = QLabel()
        #self.layout_primeiro = QVBoxLayout()

        #self.button1 = QPushButton("(ESC) Sair")
        #self.layout_primeiro.addWidget(self.button1)

        #self.label_primeiro.setLayout(self.layout_primeiro)
        #self.layout_v_total.addWidget(self.label_primeiro)
#================================================================================
        self.label_butao = QLabel()

        self.layout_butao = QHBoxLayout()

        self.button2  = QPushButton("(F6) Cupom fiscal")
        self.button3 = QPushButton("(F8) NFC-Online")
        self.button1 = QPushButton("(ESC) Sair")
        self.button4 = QPushButton("(F9)NFC-Online")
        self.button5 = QPushButton("(F7) Pedido de venda")

        self.layout_butao.addWidget(self.button1)
        self.layout_butao.addWidget(self.button2)
        self.layout_butao.addWidget(self.button3)
        self.layout_butao.addWidget(self.button5)
        self.layout_butao.addWidget(self.button4)
        

        self.label_butao.setLayout(self.layout_butao)

        self.layout_v_total.addWidget(self.label_butao)


#===================================================================================
        # adicionar o layout vertical a tela
        self.setLayout(self.layout_v_total)


app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()