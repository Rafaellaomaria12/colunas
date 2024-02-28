import sys
 
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem,QLabel,QLineEdit, QVBoxLayout, QPushButton
 
from pymongo import MongoClient
 
cliente = MongoClient("mongodb://root:senac123@127.0.0.1:37452")
 
db = cliente.Loja_db
 
class exibirUsuarios(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.setGeometry(30,400,600,300)
        self.setWindowTitle("cadastro de usuarios")
 
        labelNome = QLabel("Nome do usuario: ")
        self.editNome = QLineEdit()
 
        labelsenha = QLabel("Senha: ")
        self.editsenha = QLineEdit()
 
        labelnivel = QLabel("nivel: ")
        self.editnivel = QLineEdit()
 
        psbCadastro = QPushButton("Cadastrar")
        self.labelMsg =QLabel("|")
 
        layout = QVBoxLayout()
        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)
       
        layout.addWidget(labelsenha)
        layout.addWidget(self.editsenha)
 
        layout.addWidget(labelnivel)
        layout.addWidget(self.editnivel)
 
        layout.addWidget(psbCadastro)
 
        layout.addWidget(self.labelMsg)
 
        psbCadastro.clicked.connect(self.cadCurs)
 
        self.setLayout(layout)
 
    def cadCurs(self):
       usuario_id = db["usuario"].insert_one({"nomeusuario":self.editNome.text(),"senha":self.editsenha.text(),"nivel":self.editnivel.text()}).inserted_id
       self.labelMsg.setText("Cliente cadastrado")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = exibirUsuarios()
    tela.show()
    sys.exit(app.exec_())