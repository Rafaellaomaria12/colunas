from pymongo import MongoClient
 
cliente = MongoClient("mongodb://root:senac123@127.0.0.1:37452")
 
db = cliente.Loja_db
 
 
# selecionando o banco de dados loja_db
 
# Estamos obtendo os dados que estão cadastrado na tabela(coleção) usuario,
# usamos db [""].find().
# O comando find localiza os dados e retorna com todos eles para a variável us.
# Depois fizemos a leitura de todas linha com o for e exibimos na tela.
 
 
for us in db["usuario"].find():
    print(us)
 
# usuario_id = db["usuario"].insert_one({"nomeusuario":"jose","senha":"123","nivel":"usuario"}).inserted_id
# print(usuario_id)
 
#abaixo a consulta realiza o cadastro de um de um novo usuario e
#retorna o id do usuario cadastrado
 
 
 
#localizar apenas um usuario no banco de dados
# rs = db["usuario"].find_one({"nivel":"usuario"})
# print(rs)
 
 
# Localizar todos os dados do nível de acesso usuario
#for rs in db["usuario"].find({"nivel":"usuario"}):
#    print(rs)