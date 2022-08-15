from neo4j import GraphDatabase

class NeoInterface:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_test(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._random_call)
            print(greeting)

    @staticmethod
    def _random_call(tx):
        result = tx.run("""
            MATCH (r:Recipe)-[:CONTAINS_INGREDIENT]-(i:Ingredient)
            WHERE i.name = 'chocolate'
            RETURN r
            LIMIT 10
        """)
        return result.single()[0]


if __name__ == "__main__":
    driver = NeoInterface("bolt://localhost:7687", "neo4j", "your_password")
    driver.print_test()
    driver.close()
