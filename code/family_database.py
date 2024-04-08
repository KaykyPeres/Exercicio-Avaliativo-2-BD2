class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    # Criação de nós
    def create_pessoa(self, profissao, name, idade, sexo):
        query = f"CREATE (:Pessoa:{profissao} {{name: $name, idade: $idade, sexo: $sexo}})"
        parameters = {"name": name, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)

    def create_dog(self, name, idade, sexo):
        query = "CREATE (:Pet:Cachorro {name: $name, idade: $idade, sexo: $sexo})"
        parameters = {"name": name, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)
        
    # Criação dos relacionamentos
    def pai_de(self, namePai, nameFilho):
        query = "MATCH (p1:Pessoa {name: $namePai}) MATCH (p2:Pessoa {name: $nameFilho}) CREATE (p1)-[:PAI_DE]->(p2)"
        parameters = {"namePai": namePai, "nameFilho": nameFilho}
        self.db.execute_query(query, parameters)
        
    def cunhado_de(self, name1, name2):
        query = "MATCH (p1:Pessoa {name: $name1}) MATCH (p2:Pessoa {name: $name2}) CREATE (p1)-[:CUNHADO_DE]->(p2)"
        parameters = {"name1": name1, "name2": name2}
        self.db.execute_query(query, parameters)
        
    def esposo_de(self, name1, name2):
        query = "MATCH (p1:Pessoa {name: $name1}) MATCH (p2:Pessoa {name: $name2}) CREATE (p1)-[:ESPOSO_DE]->(p2)"
        parameters = {"name1": name1, "name2": name2}
        self.db.execute_query(query, parameters)
        
    def dono_de(self, name1, name2, anos):
        query = "MATCH (p1:Pessoa {name: $name1}) MATCH (p2:Pet {name: $name2}) CREATE (p1)-[:DONO_DE {anos: $anos}]->(p2)"
        parameters = {"name1": name1, "name2": name2, "anos": anos}
        self.db.execute_query(query, parameters)
        
        
    # Consultas
    # Quem é pai de quem
    def get_pais(self):
        query = "MATCH (p1:Pessoa)-[:PAI_DE]->(p2:Pessoa) RETURN p1.name AS name_pai, p2.name AS name_filho"
        results = self.db.execute_query(query)
        return [(result["name_pai"], result["name_filho"]) for result in results]
    
    # Faz quantos anos que é dono de um pet
    def get_donos_tempo(self):
        query = "MATCH (p:Pessoa)-[d:DONO_DE]->(:Pet) RETURN p.name AS nome_dono, d.anos AS dono_ha_anos"
        results = self.db.execute_query(query)
        return [(result["nome_dono"], result["dono_ha_anos"]) for result in results]
    
    # Quem tem a idade menor que 20 anos
    def get_idade(self):
        query = "MATCH (p:Pessoa) WHERE p.idade < 20 RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]