#----------------------------------------#
#CLASSES
class User:
  def __init__(self, login, senha, nome, email, cpf):
    self.login = login
    self.senha = senha
    self.nome = nome
    self.email = email
    self.cpf = cpf
    self.saldo = 1000
    self.carrinho = []
class Produto:
  def __init__(self,iD, produto, preco):
    self.iD = iD
    self.produto = produto
    self.preco = preco
#----------------------------------------#

#VARIÁVEIS
#----------------------------------------#
#Utilize as credenciais abaixo para realizar login como Usuário Administrador do Sistema
admin = User("admin","admin","admin","admin@gmail.com","-") 
#cadu = User("cadu","cadu","cadu","cadu@gmail.com","11967944059")
adm = False #var adm serve para validação posterior das permissões do usuário
#----------------------------------------#

#ARRAYS
#----------------------------------------#
users_data = [admin] #Dados de TODOS os usuários do sistema
produtos = [
  Produto("0","Pasta de dente",4.99),
  Produto("1","Arroz 5Kg",18.99),
  Produto("2","Feijão 1Kg", 8.99),
  Produto("3","Açúcar 1Kg", 3.49),
  Produto("4","Sal de cozinha 1Kg", 1.49),
  Produto("5","Água Mineral 5L", 4.99),
  Produto("6","Refrigerante Coca-cola 2L", 8.49),
  Produto("7","Bolacha recheada", 1.99),
  Produto("8","Presunto", 4.75),
  Produto("9","Óleo de Soja 500ml", 3.49),
  Produto("10","Leite 1L", 4.99),
  Produto("11","Batata Monalisa 1Kg", 6.49),
  Produto("12","Erva Mate", 8.49),
  Produto("13","Detergente", 1.50),
  Produto("14","Sabão em pó", 12.99),
  Produto("15","Barra de Chocolate", 3.99),
  Produto("16","Banana caturra 1Kg", 3.49),
  Produto("17","Picanha Bovina 1Kg", 37.99),
  Produto("18","Maçã Fuji 1Kg", 7.49),
  Produto("19","Papel Higiênico 12 Rolos", 18.99)
  ] #todos os produtos cadastrados
invalid_cpf = [
  "11111111111",
  "22222222222",
  "33333333333",
  "44444444444",
  "55555555555",
  "66666666666",
  "77777777777",
  "88888888888",
  "99999999999",
  "01234567890"
] #todos os cpfs inválidos por padrão
#----------------------------------------#

#FUNÇÕES DE VALIDAÇÃO
#----------------------------------------#
def check_user(usuario): #Checa se o usuário existe no sistema
  global contador #Define como global a variável contador
  contador = 0 #Serve para definir a posição do usuário em users_data
  for i in users_data:
    if i.login == usuario:
      for j in range(1,4): #Define 3 tentativas para acertar a senha
        pwd = input("Senha: ")
        if pwd != i.senha:
          print(f"\033[1;31m Senha incorreta! {3-j} tentativa(s) restante(s).\033[0m")
          if (3-j) == 0:
            clear_t()
            return False
        else:
          global user #define a variável como global para parâmetro de usuário no código
          user = users_data[contador]
          return True    
    contador += 1 #Adiciona sempre que o usuário não for encontrado em users_data
  if contador == len(users_data): #Se o contador tiver o mesmo tamanho que a users_data, não foi encontrado o usuário
    print("\033[1;31m Usuário não encontrado! \033[0m")
def check_admin(user): #Checa se o login foi feito com uma conta de administrador
  if user == admin.login:
    clear_t()
    print("\n\033[1;32m Entrou como Administrador \033[0m")
    global adm #Define as mudanças em adm como globais
    adm = True #Define que a sessão atual é de administrador
    return True
  else:
    clear_t()
    print(f"\n\033[1;32m Bem vindo/a {user.upper()} \033[0m")
    return False #Retorna falso se a sessão atual não for de adminstrador
def login(): #Pede o usuário e chama as validações de permissão
  while True:
    user = input("Usuário: ")
    if check_user(user) == True: #Chama a validação check_user
      if check_admin(user) == True:#Chama a validação check_admin
        return True
      else:
        return False
def check_permission(x): #Checa o parâmetro passado para definir qual o menu que será mostrado
  if x == True: #Se o usuário for admin, será executado o menu_admin
    menu_admin()
  else: #Se não, será executado o menu_cliente
    menu_client()
def check_cpf(cpf): #Checa se o CPF é válido ou não
  while True:
    list_cpf = []
    if len(str(cpf)) != 11 or str(cpf) in invalid_cpf: #checa se o CPF tem o número de digitos corretos ou é um valor inválido..
      print("\033[1;31m CPF inválido \033[0m")
      return False
    else: #faz a validação com os digitos de parâmetro.
      stringcpf = str(cpf)    
      for i in stringcpf:
        list_cpf.append(int(i))
      mult = mult_cpf(list_cpf,9,10) #Linha 406
      newvalor = mult % 11
      if newvalor > 1:
        digito_um = 11 - newvalor
      else:
        digito_um = 0
      mult2 = mult_cpf(list_cpf,10,11) #Linha 406
      newvalor2 = mult2 % 11
      if newvalor2 > 1:
        digito_dois = 11 - newvalor2
      else:
        digito_dois = 0
      if digito_um == list_cpf[-2] and digito_dois == list_cpf[-1]:#faz a comparação com os digitos verificadores
        print("\033[1;32m Seu CPF é válido! \033[0m")
        return True
      else:
        print("\033[1;31m Seu CPF é inválido! \033[0m")
        return False
#----------------------------------------#

#FUNÇÕES DE AÇÃO
#----------------------------------------#
def update_usr():#função parâmetro para editar usuários e checar as informações atuais de usuários
  global logins #lista global para logins
  global emails #lista global para emails
  global cpfs #lista global para cpfs
  logins = []
  emails =[]
  cpfs = []
  for j in users_data:#loop for para adição de atualizações nas informações de users_data
    logins.append(j.login)
    emails.append(j.email)
    cpfs.append(j.cpf)
def register(): #Função para cadastros de clientes - EXCLUSIVO ADMINISTRADOR
  print("\nINÍCIO DO CADASTRO\n")
  while True:
    qntd_users = input("Quantos usuários deseja cadastrar?\n")
    confirm = input(f"Tem certeza que deseja criar {qntd_users} novos usuários?\033[0m (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
    if confirm == "s":
      break
  try: #Testa se é possível transformar o input qntd_users em inteiro
    qntd_users = int(qntd_users)
  except:
    print("\033[1;31mValor não reconhecido!\033[0m")
  else:
    for i in range(qntd_users):
      update_usr() #Atualiza as listas de todos os Logins, Emails e CPFs cadastrados no sistema
      while True: 
        login = input("\nLogin: ")
        if login in logins:
          print("\033[1;31mIndisponível! Por favor, insira outro.\033[0m")
        else:
          senha = input("Senha: ")
          nome = input("Nome: ")
          while True:
            email = input("E-mail: ")
            if email in emails:
              print("\033[1;31mIndisponível! Por favor, insira outro.\033[0m")
            else:
              while True:
                cpf = input("CPF: ")
                if check_cpf(cpf) == True:
                  if cpf in cpfs:
                    print("\033[1;31mIndisponível!\033[0m")
                  else:
                    name = User(login, senha, nome, email, cpf) #Cria o usuário
                    users_data.append(name) #Adiciona o usuário na lista de usuário
                    print("\033[1;32m Usuário cadastrado com sucesso! \033[0m")
                    break
                  break
              break
          break
def shop(): #Realiza a adição de itens no carrinho de compras
  shelf() #Mostra a prateleira
  print("\033[1;33m 20 \033[0m. \tSair")
  while True:
    pid = input("\nQual o número do produto você deseja adicionar ao carrinho?\n\nCaso queira voltar ao menu, basta digitar o número correspondente.\n")
    try: #Testa se é possível transformar o PID em inteiro
      pid = int(pid)
    except: #Se não der, retorna que o valor é inválido
      print("\033[1;31mValor não reconhecido!\033[0m")
    else:
      if int(pid) == 20: #Opção SAIR
        clear_t()
        break
      elif pid > 20 or pid < 0:
        print("\033[1;31mValor não reconhecido!\033[0m")
      else:
        qnt = int(input("Qual a quantidade deste produto que você deseja comprar?\n"))
        prod =  produtos[int(pid)] #Relaciona o produto da lista em uma variável
        carrinho = user.carrinho #Pega o carrinho do usuário logado
        valor = round(prod.preco * qnt,2) #Arredonda o valor para 2
        carrinho.append([prod.iD,prod.produto,qnt,valor]) #Adiciona os produtos no carrinho
        while True:
          continuebuy = input("\033[1;47;30mDeseja continuar comprando?\033[0m (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
          if continuebuy == "n":
            clear_t()
            return True
          elif continuebuy == "s":
            break
          else:
            print("\033[1;31mValor não reconhecido.\033[0m")
def clear_t(): #Limpa o console após chamada a função
  import os # Função importada da Biblioteca OS.
  os.system('clear')# Roda automáticamente o clear no terminal
def product_remove():#Remove produtos do carrinho
  cart() # Chama função carrinho
  if valorFinal == 0: #Checa se carrinho está vazio
    print("\033[1;31mSEU CARRINHO ESTÁ VAZIO!\033[0m")
  else:
    removeprod = int(input("Qual o ID do produto você deseja remover? (-1 para sair)\n"))
    if removeprod >= -1: #Se o valor inputado for diferente de um ele irá remover, caso contrário o programa irá voltar ao menu printando produto não encontrado
      carrinho.pop(removeprod)# Remove o item específico da lista
      print("\033[1;32m Produto removido com sucesso!\033[0m")
    else:
      print("\033[1;31mProduto não encontrado\033[0m")
def client_remove(): # Remove o cliente, função exclusiva do administrador
  print("\033[1;41;37mRemover Cliente\033[0m\n")
  userCPF = input("Insira o CPF do(a) cliente (sem formatação):\n")
  cont = 0 # Contador para validar as informações do usuário
  checker = False# Setado como falso como padrão para cargo de comparações
  for i in users_data:
    if userCPF == i.cpf: #Checa se o usuário existe
      print(f"""
        Login: {i.login}
        Nome: {i.nome}
        e-mail: {i.email}
        CPF: {i.cpf}
        Saldo: \033[1;32mR$R${round(float(i.saldo),2)}\033[0m
        Carrinho: {i.carrinho}
        """)
      if userCPF == admin.cpf: #Checa se o usuário não é admin, pois o admin não deve ser removido
        print("\033[1;31mNão é possível remover o Administrador!\033[0m")
        checker = True
      else:
        cont += 1
        while True: #loop para confirmação de remoção
          askremove = input("Deseja remover este cilente? (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
          if askremove == "n":
            return True
          elif askremove == "s": #verficador final para remoção tomando como base contador
            users_data.pop(cont)
            print("\033[1;32mCliente removido com sucesso!\033[0m")
            return True
          else:
            print("\033[1;31mValor não reconhecido.\033[0m")
  if checker == False:  
    print("\033[1;31m Cliente não existe!\033[0m")
def client_edit(): #Realiza a edição de um cliente já cadastrado
  print("\033[1;46;37mEditar Cliente\033[0m\n")
  userCPF = input("Insira o CPF do(a) cliente (sem formatação):\n")
  checker = False #verifica se o cliente existe nos cadastros (True = sim, False = não)
  update_usr() #Atualiza as listas de todos os Logins, Emails e CPFs cadastradps no sistema
  for i in users_data: #Verifica todos os usuários cadastrados
    if userCPF == i.cpf: #Verifica se o CPF inserido é igual ao CPF do cadastro e printa os dados atuais do cliente
      print(f"""
        1. Login: {i.login}
        2. Senha: {i.senha}
        3. Nome: {i.nome}
        4. e-mail: {i.email}
        5. CPF: {i.cpf}
        6. Saldo: \033[1;32mR${round(float(i.saldo),2)}\033[0m
        7. Carrinho: {i.carrinho}
        """)
      #Abaixo, variáveis utilizadas para editar TEMPORARIAMENTE os dados, afim de não modificar AINDA os originais
      newLogin = i.login
      newSenha = i.senha
      newNome = i.nome
      newEmail = i.email
      newCPF = i.cpf
      newSaldo = i.saldo
      if userCPF == admin.cpf: #Verifica se o cpf inserido é igual ao do ADM. Não é possível alterar os dados do ADM pelo sistema, apenas no código
        print("\033[1;31mNão é possível editar o Administrador!\033[0m")
        return True
      else:
        checker = True #Define que o cliente existe
        while True:
          edit = input("Qual item deseja editar?\n")
          if edit == '1':
            while True:
              newLogin = input("Novo login:\n")
              if newLogin in logins:
                print("\033[1;31mIndisponível! Por favor, insira outro.\033[0m")
              else:
                break
          elif edit == '2':
            newSenha = input("Nova senha:\n")
          elif edit == '3':
            newNome = input("Novo nome:\n")
          elif edit == '4':
            while True:
              newEmail = input("Novo e-mail:\n")
              if newEmail in emails:
                print("\033[1;31mIndisponível! Por favor, insira outro.\033[0m")
              else:
                break
          elif edit == '5':
            while True:
              newCPF = input("Novo CPF:\n")
              if newCPF in cpfs:
                print("\033[1;31mIndisponível! Por favor, insira outro.\033[0m")
              else:
                if check_cpf(newCPF) == True: #Verifica se o CPF é válido
                  break
          elif edit == '6':
            newSaldo = input("Novo saldo:\n")
          elif edit == '7':
            print("Para editar o carrinho, faça login com a conta do usuário e remova os itens do carrinho através do menu!")
          else:
            print("\033[1;31m Valor inválido! \033[0m")
          editMore = input("Deseja continuar editando? (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
          if editMore == 'n':
            clear_t()
            break 
      #Printa os novos valores, MAS AINDA NÃO MUDA.
      print(f"""
        1. Login: {newLogin}
        2. Senha: {newSenha}
        3. Nome: {newNome}
        4. e-mail: {newEmail}
        5. CPF: {newCPF}
        6. Saldo: \033[1;32mR${float(newSaldo)}\033[0m
        7. Carrinho: {i.carrinho}
        """)
      while True:     
        askedit = input("Deseja confirmar as mudanças? (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
        if askedit == "n":
          return True
        elif askedit == "s": #SE CONFIRMADO, MUDA DEFINITIVAMENTE AS INFORMAÇÕES DO USUÁRIO
          i.login = newLogin 
          i.senha = newSenha
          i.nome = newNome
          i.email = newEmail
          i.cpf = newCPF
          i.saldo = newSaldo 
          print("\033[1;32mCliente editado com sucesso!\033[0m\n")
          return True
        else:
          print("\033[1;31mValor não reconhecido.\033[0m")
  if checker == False: #Se após todo o código o checker não virar True, retorna que o cliente não existe.
    print("\033[1;31m Cliente não existe!\033[0m")
def pay(): #Realiza o pagamento dos itens do carrinho
  cart()
  if valorFinal == 0: #Verifica se a variável global Valor Final, possui algum valor. Se não tiver, não há itens no carrinho.
    print("\033[1;31mSEU CARRINHO ESTÁ VAZIO!\033[0m")
  else:
    while True: 
      paycart = input("Deseja efetuar o pagamento? (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
      if paycart == "s":
        money = float(user.saldo) - valorFinal #Verifica o resultado da subtração entre o saldo do cliente e o valor total
        if money >= 0: #Se o cliente possui saldo suficiente:
          carrinho.clear() #Apaga todos os itens do carrinho
          user.saldo = money # Define o novo saldo como o valor verificado anteriormente
          print("\033[1;32m \nPAGAMENTO EFETUADO COM SUCESSO!\033[0m\n")
          break
        else: #Se o valor total ultrapassar o saldo do cliente, o pagamento não é efetuado e mantém-se os itens no carrinho
          print("\033[1;31mVOCÊ NÃO POSSUI SALDO SUFICIENTE!\033[0m")
          break
      elif paycart == "n": #Se o cliente não desejar pagar, o pagamento não é efetuado e mantém-se os itens no carrinho
        print("\033[1;31mPAGAMENTO NÃO FOI EFETUADO!\033[0m")
        break
      else: #Se o usuário inserir um valor diferente dos solicitados, a função reinicia.
        print("\033[1;31mValor não reconhecido!\033[0m")
def mult_cpf(lista, n_range, contn): #Realiza a multiplicação e soma do cálculo da validação do CPF
  soma = 0
  for j in range(n_range): #Para cada numero, multiplica-o pelo contn e adiciona o produto em soma.
    soma += lista[j] * contn
    contn -= 1 #Subtrai 1 do contn para seguir com a fórmula
  return soma #Retorna o valor da soma das multiplicações
#----------------------------------------#

#FUNÇÕES DE CONSULTA
#----------------------------------------#
def menu_admin(): #Mostra o menu de administrador
  while True: #loop para mostrar o menu após a realização de alguma ação
    print("------------------------------------------------------")
    print("""\n\033[47;1;30m Menu de Administrador:\033[0m\n
    1 - Cadastro de Cliente
    2 - Remover Cliente
    3 - Editar cliente
    4 - Consultar cliente
    5 - Meus Dados
    6 - Mostrar produtos
    7 - Comprar
    8 - Mostrar carrinho
    9 - Remover produto do carrinho
    10 - Pagar conta
    0 - Sair
    """)
    print("------------------------------------------------------")
    asw = input("\n\033[40;1;37mDigite o número da opção que você deseja fazer:\033[0m\n")#abaixo disso começa uma lista de verificações chamando as funções condizentes para realização das mesmas
    if asw == '1':
      clear_t()
      register()
    elif asw == '2':
      clear_t()
      client_remove()
    elif asw == '3':
      clear_t()
      client_edit()
    elif asw == '4':
      clear_t()
      client_consult()
    elif asw == '5':
      clear_t()
      self_data()
    elif asw == '6':
      clear_t()
      shelf()
    elif asw == '7':
      clear_t()
      shop()
    elif asw == '8':
      clear_t()
      cart()
    elif asw == '9':
      clear_t()
      product_remove()
    elif asw == '10':
      clear_t()
      pay()
    elif asw == '0':  
      print("SAIR")
      break
    else:
      print("\033[1;31m VALOR NÃO ENCONTRADO \033[0m")
def menu_client(): #Mostra o menu de cliente
  while True: #loop para mostrar o menu do cliente após a realização de alguma ação
    print("------------------------------------------------------")
    print("""\n\033[47;1;30m Menu de Cliente: \033[0m\n
    1 - Meus dados
    2 - Mostrar produtos
    3 - Comprar
    4 - Mostrar carrinho
    5 - Remover produto do carrinho
    6 - Pagar conta
    0 - Sair
    """)
    print("------------------------------------------------------")
    asw = input("\n\033[40;1;37m Digite o número da opção que você deseja fazer: \033[0m\n")#abaixo disso começa uma lista de verificações chamando as funções condizentes para realização das mesmas
    if asw == '1':
      clear_t()
      self_data()
    elif asw == '2':
      clear_t()
      shelf()
    elif asw == '3':
      clear_t()
      shop()
    elif asw == '4':
      clear_t()
      cart()
    elif asw == '5':
      clear_t()
      product_remove()
    elif asw == '6':
      clear_t()
      pay()
    elif asw == '0':
      print("SAIR")
      break
    else:
      print("\033[1;31m VALOR NÃO ENCONTRADO \033[0m")
def shelf(): #Mostra a prateleira de produtos
  print("")
  print("------------------------------------------------------")
  for i in produtos:
    print(f"\033[1;33m {i.iD} \033[0m. {i.produto} - \033[1;32m R${i.preco} \033[0m")
  print("------------------------------------------------------")
def cart(): #Mostra o carrinho de comprar do cliente que está logado no momento
  print("------------------------------------------------------")
  print(f"\t \033[47;1;30m CARRINHO DE  {user.nome.upper()} \033[0m")
  print("_______________________________________________")
  global carrinho  #As variáveis globais são utilizadas em outras partes do código
  global valorFinal
  carrinho = user.carrinho #Define carrinho como o carrinho do usuário
  valorFinal = 0
  pos = 0 #Posição do produto dentro do carrinho, começando em 0 até infinito
  for i in carrinho:
    print(f"""
      ID: \033[1;33m{pos}\033[0m\tProduto: \033[1;36m{i[1]}\033[0m\t Quantidade: \033[1;36m{i[2]}\033[0m\t Valor: \033[1;32mR${i[3]}\033[0m
    """) #Printa as informações de cada produto que foi comprado
    valorFinal += i[3] #Adiciona o valor de todos os produtos em uma variável
    pos += 1 #Muda a posição para definir o ID em cada item
  print("_______________________________________________")
  print(f"\nVALOR TOTAL:\t \033[1;32mR${round(valorFinal,2)}\033[0m") #Printa o valor total do carrinho
  print("------------------------------------------------------\n\n")
def client_consult(): #Consulta clientes no sistema
  while True:
    print("Consultar Cliente")
    print("------------------------------------------------------")
    validador = False #Verifica se o cliente existe
    clienteCPF = input("Insira o CPF do(a) cliente (sem formatação):\n")
    for i in users_data:
      if clienteCPF == i.cpf:
        print(f"""
        Login: {i.login}\t 
        Senha: {i.senha}\t 
        Nome: {i.nome}\t 
        e-mail: {i.email}\t 
        CPF: {i.cpf}
        Saldo: \033[1;32mR${round(float(i.saldo),2)}\033[0m
        Carrinho: {i.carrinho}
        """)
        validador = True
    if validador == False: #Se não existir, retorna que não foi encontrado
      print("\n\033[1;31mUsuário não encontrado!\033[0m\n")
    while True:
      continuebuy = input("Deseja continuar consultando? (\033[1;32ms\033[0m/\033[1;31mn\033[0m)\n")
      if continuebuy == "n":
        clear_t()
        return True
      elif continuebuy == "s":
        break
      else:
        print("\033[1;31mValor não reconhecido.\033[0m")
def self_data(): #Verificar os dados do usário logado
  print("------------------------------------------------------")
  print(f"\033[47;1;30m Dados de {user.nome.upper()}\033[0m")
  print("------------------------------------------------------")
  print(f"""
      Login: {user.login}\t 
      Senha: {user.senha}\t 
      Nome: {user.nome}\t 
      e-mail: {user.email}\t 
      CPF: {user.cpf}\t
      Saldo: \033[1;32mR${round(float(user.saldo),2)}\033[0m\t
      Carrinho: {user.carrinho}\t
      """)
#----------------------------------------#

#Corpo do Código
#----------------------------------------#
while True:
  check_permission(login())
  clear_t()