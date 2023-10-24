from elasticsearch import Elasticsearch


class MyEs:

    def __init__(self, conf):

        host = conf.get("host")
        port = conf.get("port")
        username = conf.get("username", "test")
        password = conf.get("password", "test")
        self.es = Elasticsearch([{"host": host, "port": port}], http_auth=(username, password))

    def search(self, index, body):
        """
        搜索
        :param index:
        :param body:
        :return:
        """
        res = self.es.search(index=index, body=body)["hits"]["hits"]
        arr = []
        if res:
            for item in res:
                arr.append(item["_source"])
        return arr

    def delete_index(self, index):
        """
        删除索引
        :param index:
        :return:
        """
        self.es.indices.delete(index)

