from database import Database
from family_database import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.212.11.72:7687", "neo4j", "defense-divider-aviation")
db.drop_all()

# Criando uma instância da classe FamilyDatabase para interagir com o banco de dados
match_db = FamilyDatabase(db)

# Criando pessoas
match_db.create_pessoa("Estudante", "Gabriel", 19, "Masculino")
match_db.create_pessoa("Veterinário", "Gustavo", 29, "Masculino")
match_db.create_pessoa("Administrador", "Karol", 29, "Feminino")
match_db.create_pessoa("RH", "Wanderley", 52, "Masculino")
match_db.create_pessoa("Enfermeira", "Nany", 50, "Feminino")
match_db.create_pessoa("Vendedora", "Wanessa", 29, "Feminino")
match_db.create_pessoa("Administrador", "Daniel", 32, "Masculino")


# Criando Dogs
match_db.create_dog("Mel", 2, "Feminino")
match_db.create_dog("Duda", 3, "Feminino")
match_db.create_dog("Meg", 9, "Feminino")

# Criando relacionamentos
match_db.pai_de("Wanderley", "Gabriel")
match_db.pai_de("Wanderley", "Karol")
match_db.pai_de("Nany", "Gabriel")
match_db.pai_de("Nany", "Gustavo")
match_db.dono_de("Nany", "Mel", 1)
match_db.dono_de("Nany", "Meg", 9)
match_db.dono_de("Nany", "Duda", 3)
match_db.esposo_de("Wanderley", "Nany")
match_db.esposo_de("Daniel", "Karol")
match_db.esposo_de("Gustavo", "Wanessa")
match_db.cunhado_de("Wanessa", "Gabriel")
match_db.cunhado_de("Daniel", "Gabriel")


# quem é pai de quem
print("Pais:")
print(match_db.get_pais())

# quantos anos que é dono do pet
print("Dono e tempo:")
print(match_db.get_donos_tempo())

# Quem tem a idade menor que 20 anos
print("Nome:")
print(match_db.get_idade())

# Fechando a conexão com o banco de dados
db.close()