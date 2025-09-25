import json
tarefas = []

# CARREGAR TAREFAS DO ARQUIVO
def carregar():
	global tarefas
	try:
		with open("tarefas.json", "r") as f:
			tarefas = json.load(f)
	except FileNotFoundError:
		tarefas = []
	except json.JSONDecodeError:
		print('Arquivo corrompido ou vazia, inicie uma nova lista.')
		tarefas = []
	
# SALVAR TAREFAS NO ARQUIVO
def salvar():
	with open("tarefas.json", "w") as f:
		json.dump(tarefas, f, indent=4)

# REORGANIZAR IDS
def reorganizar():
	for a,tarefa in enumerate(tarefas, start=1):
		tarefa["id"] = a
	salvar()
	
# ENTRADA ERRADA
def erro():
		print('Erro, tente novamente!')
		
# DADOS DAS TAREFAS
def dados(b, mostrar_id = False):
	if mostrar_id:
		print(f'{b["id"]}. {b["nome"]}  ->  Status: {b["status"]}')
	else:
		print(f'> {b["nome"]}  ->  Status: {b["status"]}')
		
# MENU DE TAREFAS
def menu_tarefas():
	print("""
MENU

1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefas como concluido
4. Remover tarefas
5. Remover todas tarefas
6. Lista de concluidas
7. Lista de pendentes
8. Sair
""")

# ADICIONAR TAREFAS
def add_tarefa():
	nome = input('Digite nova tarefa: ').strip().upper()
	if not nome:
		print('Tarefa vazia, tente novamente!')
		return 
	tarefa = {'id': None,
	"nome": nome,
	'status': 'Pendente'}
	tarefas.append(tarefa)
	reorganizar()
	print(f'A tarefa: {tarefa["nome"]} foi adicionada com sucesso!')

# LISTA DE TAREFAS
def lista(mostrar_ids = False):
	if not tarefas:
		print('Não há nenhuma tarefa.')
	elif mostrar_ids:
		for a in tarefas:
			dados(a, mostrar_ids)
	else:
		for a in tarefas:
			dados(a)
			
# TAREFAS CONCLUIDAS
def tarefas_concluidas():
	lista(mostrar_ids = True)
	entrada = input('Digite o numero da tarefa: ').strip()
	if not entrada.isdigit():
		erro()
		return 
	id_tarefas = int(entrada)
	for a in tarefas:
		if  a["id"] == id_tarefas:
			a["status"] = "Concluido"
			print('Alteracao feita com sucesso.')
			salvar()
			break
	else:
		print('Id não encontrado.')

# APAGAR TAREFAS 
def apagar_tarefas():
	lista(mostrar_ids = True)
	entrada = input('Digite o numero da tarefa, se for mais de uma opção, sepera os numeros com virgula.').strip()
	if not entrada.replace(","," ").replace(" ", "").isdigit():
		erro()
		return 
		
	ids = [int(x) for x in entrada.split(",") if x.strip().isdigit()]
	
	removido = 0
	for id_tarefas in ids:
		for a in tarefas:
			if a["id"] == id_tarefas:
				tarefas.remove(a)
				removido +=1
				break
	if removido:
		reorganizar()
		print(f'{removido} removido(s) com sucesso!')
	else:
		print('id não encontrada!')
		
# APAGAR TUDO
def apagar_tudo():
	escolha = input('Confirmaçao para apagar todas as tarefas. Digite "sim" para confirmar.').lower().strip()
	if escolha == "sim":
		tarefas.clear()
		salvar()
		print('Tarefas removidas com sucesso.')
		
# LISTAR TAREFAS CONCLUIDAS
def lista_concluida():
	encontrar = [b for b in tarefas if b["status"] == "Concluido"]
	if not encontrar:
		print('Não há tarefa concluida.')
	else:
		for b in encontrar:
			dados(b)
			
# LISTAR TAREFAS PENDENTES
def lista_pendente():
	encontrar = [b for b in tarefas if b["status"] != "Concluido"]
	if not encontrar:
		print('Não há tarefa pendente.')
	else: 
		for b in encontrar:
			dados(b)
	
# MENU FUNCIONAL
if __name__ == "__main__":
	carregar()
	input('Seja bem vindo! Aperte enter para começar')
	while True:
	        menu_tarefas()
	        opcao = input("Escolha: ").strip()

	        if opcao == "1":
	           add_tarefa()
	        elif opcao == "2":
	           lista()
	        elif opcao == "3":
	          tarefas_concluidas()
	        elif opcao == "4":
	          apagar_tarefas()
	        elif opcao == "5":
	        	apagar_tudo()
	        elif opcao == "6":
	        	lista_concluida()
	        elif opcao == "7":
	        	lista_pendente()
	        elif opcao == "8":
	            print("Saindo do programa...")
	            break
	        else:
	            print("Opção invalida.")
