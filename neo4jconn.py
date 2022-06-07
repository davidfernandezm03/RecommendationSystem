from neo4j import GraphDatabase

class Neo4jConnection:

    def __init__(self, uri, user, password, db):
        self.db = db
        self.connectivity = None
        self.driver = None
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            self.driver.verify_connectivity()
            self.connectivity = True
        except Exception as e:
            print("Cannot establish a connection to the database")
            print(e)

    def close(self):
        if self.driver:
            self.driver.close()

    def verify_connectivity(self):
        self.connectivity = None
        if self.driver:
            try:
                self.driver.verify_connectivity()
                self.connectivity = True
            except Exception as e:
                print("Failed to connect")
                print(e)

    def run_query(self, query, parameters=None):
        response = []
        if self.connectivity:
            try:
                with self.driver.session(database=self.db) as session:
                    response = list(session.run(query, parameters))
            except Exception as e:
                print("Query failed")
                print(e)
        return response