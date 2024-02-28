import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
 
class GuiDuasColunas(QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.total = 0.0
        self.linha = 0

        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa da Padaria")
       
 
        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()
        layoutHor = QHBoxLayout()
 
        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#a1887f;}")
        labelColEsq.setFixedWidth(800)
 
        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#bcaaa4}")
        labelColEsq.setFixedWidth(800)
       
        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("Logo_padaria.png"))
        labelLogo.setScaledContents(True)
       
        labelCodigo = QLabel("Código do Produto: ")
        labelCodigo.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
        labelNomeProduto = QLabel("Nome do Produto: ")
        labelNomeProduto.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
        labelDesProduto = QLabel("Descrição do Produto: ")
        labelDesProduto.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.DesProdutoEdit = QLineEdit()
        self.DesProdutoEdit.setFixedHeight(100)
        self.DesProdutoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
       
        labelQtdProduto = QLabel("Quantidade do Produto: ")
        labelQtdProduto.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.qtdProdutoEdit = QLineEdit()
        self.qtdProdutoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
        labelpcProduto = QLabel("Preço do Produto: ")
        labelpcProduto.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.pcProdutoEdit = QLineEdit()
        self.pcProdutoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
        labelSubTotalProduto = QLabel("Total do Produto: ")
        labelSubTotalProduto.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.SubTotalProdutoEdit = QLineEdit("Tecle F3 para calcular o subtotal")
        # Desabilitar a caixa do subtotal
        self.SubTotalProdutoEdit.setEnabled(False)
        self.SubTotalProdutoEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
       
        layoutVerEs.addWidget(labelLogo)
        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)
       
        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)
       
        layoutVerEs.addWidget(labelDesProduto)
        layoutVerEs.addWidget(self.DesProdutoEdit)
       
        layoutVerEs.addWidget(labelQtdProduto)
        layoutVerEs.addWidget(self.qtdProdutoEdit)
       
        layoutVerEs.addWidget(labelpcProduto)
        layoutVerEs.addWidget(self.pcProdutoEdit)
       
        layoutVerEs.addWidget(labelSubTotalProduto)
        layoutVerEs.addWidget(self.SubTotalProdutoEdit)
       
        labelColEsq.setLayout(layoutVerEs)
       
        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)
       
        # Criando o cabecalho para a tabela resumo
        titulos = ["Código", "Nome Produto","Quantidade", "Preço Unitário", "Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)
       
        labelTotalPagar = QLabel("Total a Pagar ")
        labelTotalPagar.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.TotalPagarEdit = QLineEdit("0,00")
        self.TotalPagarEdit.setEnabled(False)
        self.TotalPagarEdit.setStyleSheet("QLineEdit{padding:10px; font-size:15pt; width:400}")
       
       
        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(self.TotalPagarEdit)
       
        labelColDir.setLayout(layoutVerDi)
       
 
        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)
 
        self.setLayout(layoutHor)

        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        
        if(e.key() == Qt.Key_F2):
            print('Você teclou f2')
            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.DesProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.qtdProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.pcProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.SubTotalProdutoEdit.text())))
            self.linha+=1
            

            self.total+=float(self.SubTotalProdutoEdit.text())
            self.TotalPagarEdit.setText(str(self.total))


            # Limpar os LineEdit
            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.DesProdutoEdit.setText("")
            self.qtdProdutoEdit.setText("")
            self.pcProdutoEdit.setText("")
            self.SubTotalProdutoEdit.setText("Tecle F3 para calcular o subtotal")       
        elif(e.key() == Qt.Key_F3):
            qtd = self.qtdProdutoEdit.text()
            prc = self.pcProdutoEdit.text()
            res = float(qtd) * float(prc)
            self.SubTotalProdutoEdit.setText(str(res))






app = QApplication(sys.argv)
janela = GuiDuasColunas()
janela.show()
app.exec_()