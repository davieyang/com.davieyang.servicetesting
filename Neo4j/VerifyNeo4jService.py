'''
@Time    : 2018/10/24 10:14
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyNeo4jService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
from neo4j import GraphDatabase

class VerifyNeo4j:
    """
       Handler of graph database Neo4j reading and writing.
       """

    def __init__(self, driver):
        """
        Get Neo4j server driver.
        :param driver: driver object
            A driver object holds the detail of a Neo4j database including server URIs, credentials and other configuration, see
            " http://neo4j.com/docs/api/python-driver/current/driver.html ".
        """
        self.driver = driver

    def __repr__(self):
        printer = 'o(>﹏<)o ......Neo4j old driver "{0}" carry me fly...... o(^o^)o'.format(self.driver)
        return printer

    def listreader(self, cypher, keys):
        """
        Read data from Neo4j in specified cypher.
        Read and parse data straightly from cypher field result.
        :param cypher: string
            Valid query cypher statement.
        :param keys: list
            Cypher query columns to return.
        :return: list
            Each returned record constructs a list and stored in a big list, [[...], [...], ...].
        """
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                data = []
                result = tx.run(cypher)
                for record in result:
                    rows = []
                    for key in keys:
                        rows.append(record[key])
                    data.append(rows)
                return data

    def dictreader(self, cypher):
        """
        Read data from Neo4j in specified cypher.
        The function depends on constructing dict method of dict(key = value) and any error may occur if the "key" is invalid to Python.
        you can choose function dictreaderopted() below to read data by hand(via the args "keys").
        :param cypher: string
            Valid query cypher statement.
        :return: list
            Each returned record constructs a dict in "key : value" pairs and stored in a big list, [{...}, {...}, ...].
        """
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                data = []
                for record in tx.run(cypher).records():
                    item = {}
                    for args in str(record).split('>')[0].split()[1:]:
                        exec
                        "item.update(dict({0}))".format(args)
                    data.append(item)
                return data

    def dictreaderopted(self, cypher, keys=None):
        """
        Optimized function of dictreader().
        Read and parse data straightly from cypher field result.
        :param cypher: string
            Valid query cypher statement.
        :param keys: list, default : none(call dictreader())
            Cypher query columns to return.
        :return: list.
            Each returned record constructs an dict in "key : value" pairs and stored in a list, [{...}, {...}, ...].
        """
        if not keys:
            return self.dictreader(cypher)
        else:
            with self.driver.session() as session:
                with session.begin_transaction() as tx:
                    data = []
                    result = tx.run(cypher)
                    for record in result:
                        item = {}
                        for key in keys:
                            item.update({key: record[key]})
                        data.append(item)
                    return data

    def cypherexecuter(self, cypher):
        """
        Execute manipulation into Neo4j in specified cypher.
        :param cypher: string
            Valid handle cypher statement.
        :return: none.
        """
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                tx.run(cypher)
        session.close()
if __name__ == '__main__':
    uri = "bolt://210.13.50.105:32225"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "111111"))
    MyNH = VerifyNeo4j(driver)
    print(MyNH)
    cypher_exec = """
        CREATE (Neo:Crew {name:'Neo'}),
        (Morpheus:Crew {name: 'Morpheus'}),
        (Trinity:Crew {name: 'Trinity'}),
        (Cypher:Crew:Matrix {name: 'Cypher'}),
        (Smith:Matrix {name: 'Agent Smith'}),
        (Architect:Matrix {name:'The Architect'}),
        (Neo)-[:KNOWS]->(Morpheus),
        (Neo)-[:LOVES]->(Trinity),
        (Morpheus)-[:KNOWS]->(Trinity),
        (Morpheus)-[:KNOWS]->(Cypher),
        (Cypher)-[:KNOWS]->(Smith),
        (Smith)-[:CODED_BY]->(Architect)
    """
    cypher_read = """
                        MATCH (a) -[:KNOWS|LOVES]-> (b:Crew {name: 'Trinity'})
                        RETURN a.name AS l, b.name AS r
                      """
    MyNH.cypherexecuter(cypher_exec)
    print(MyNH.listreader(cypher_read, ['l', 'r']))
    print(MyNH.dictreader(cypher_read))
    print(MyNH.dictreaderopted(cypher_read, ['l']))
