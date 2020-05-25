from ac05_filme import Filme, Banco

# Objeto da classe Banco
banco = Banco()

# Cria a tabela Filme
banco.criar_tabela()

# Criar um objeto e incluir no banco de dados
filme1 = Filme("Parasite", "Bong Joon Ho", 2019, 132, 40273, 8.6, 'Comedy, Drama, Thriller')
banco.incluir(filme1)

# Verifica se o objeto foi armazenados no banco. O ID será atribuído automaticamente aos objetos
print('ID do filme:', filme1.id)       # 1 (será 1 apenas na primeira inserção, depois o id vai aumentando conforme a inserção dos dados)
print('Nome do filme:', filme1.nome)   # Parasite

# Incluir lista de objetos no banco de dados
filme2 = Filme("Joker", "Todd Phillips", 2019, 122, 78481, 8.5, 'Crime, Drama, Thriller')
filme3 = Filme("Avengers: Endgame", "Anthony Russo, Joe Russo", 2019, 181, 715250, 8.4, 'Crime, Drama, Thriller')
filme4 = Filme("Get Smart", "Peter Segal, John Hockridge, Susan Bierbaum", 2008, 110, 1784, 6.1, "Action, Comedy, Thriller")
filme5 = Filme("Thick as Thieves", "Mimi Leder, Sandy Schklair", 2009, 104, 371, 5.9, "Action, Thriller, Crime")
filme6 = Filme("Dredd", "Pete Travis, Vinca Cox, Julia Chiavetta", 2012, 95, 2731, 6.7, "Action, Science Fiction")
filme7 = Filme("The Hunger Games", "Gary Ross, Dawn Gilliam", 2012, 142, 14241, 7.1, "Science Fiction, Adventure, Fantasy")
filme8 = Filme("The Last of the Mohicans", "Michael Mann", 1992, 112, 1336, 7.3, "Action, Adventure, Drama, History, Romance, War")
filme9 = Filme("Ninja", "Isaac Florentine", 2009, 83, 125, 5.6, "Action, Crime, Drama, Thriller")
filme10 = Filme("Oblivion", "Joseph Kosinski, Rebecca Boyle, Trisha Burton", 2013, 124, 6691, 6.5, "Action, Science Fiction, Adventure, Mystery")

lista_filmes = [filme2, filme3, filme4, filme5, filme6, filme7, filme8, filme9, filme10]
banco.incluir_lista(lista_filmes)

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de todos os filmes cadastrados no banco
    print(f.id, f.nome, f.diretor, f.ano, f.duracao, f.votos, f.avaliacao, f.genero)

print()
print('Quantidade de Filmes cadastrados:', len(lista))      # 10 (este é o valor na primeira execução, nas demais esse valor vai aumentar, conforme os dados inseridos na tabela)
print('Nome do primeiro filme:', lista[0].nome)             # Avengers: Endgame (valor na primeira execução)
print('Nome do último filme:', lista[-1].nome)              # Thick as Thieves (valor na primeira execução)

# Busca todos os filmes do gênero Crime, ordenados pelo nome
lista = banco.buscar_por_genero("Crime")
print('-'*60)
for f in lista:
    print(f.id, f.nome, f.diretor, f.ano, f.duracao, f.votos, f.avaliacao, f.genero)

# Busca todos os filmes de 2019, ordenados pelo id
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:
    print(f.id, f.nome, f.diretor, f.ano, f.duracao, f.votos, f.avaliacao, f.genero)

# Busca filmes de 2019 com avaliação igual ou superior a 8.5, ordenados pela avaliação (da maior para a menor)
lista = banco.buscar_melhores_do_ano(2019)
print('-'*60)
for f in lista:     # exibe a lista dos filmes
    print(f.id, f.nome, f.diretor, f.ano, f.duracao, f.votos, f.avaliacao, f.genero)

# Busca o filme de id 7
filme = banco.buscar_por_id(7)

# altera a avalação do filme de id 7 para 8.7
if filme is not None:
    banco.alterar_avaliacao(filme, 8.7)

# Exclui o filme de id 6
banco.excluir(6)

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de todos os filmes cadastrados no banco
    print(f.id, f.nome, f.diretor, f.ano, f.duracao, f.votos, f.avaliacao, f.genero)
