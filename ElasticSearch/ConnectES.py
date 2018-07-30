# encoding = utf-8
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class ElasticObj:
    def __init__(self, index_name='paas', index_type='paasweb', ip="210.13.50.105:32264"):
        self.index_name = index_name
        self.index_type = index_type
        # 无用户名密码状态
        self.es = Elasticsearch([ip])

    def Index_Data(self):
        list = [
            {"date": "2018-07-24",
             "source": "SpaceManagement",
             "link": "http://paasweb.tpaas.youedata.com/#/front/spaceManage/main",
             "keyword": "空间管理",
             "title": "创建空间"
             },
            {"date": "2018-07-24",
             "source": "数据库管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/databaseServicePage/main",
             "keyword": "四类数据库管理",
             "title": "创建数据库服务"
             },
            {"date": "2018-08-24",
             "source": "应用管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/image/imageList",
             "keyword": "镜像仓库",
             "title": "创建镜像"
             },
            {"date": "2018-08-24",
             "source": "应用管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/AppLocation/AppLocation",
             "keyword": "应用仓库",
             "title": "创建应用"
             }
        ]
        for item in list:
            res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item)
            print(res['created'])

    def bulk_Index_Data(self):
        list = [
            {"date": "2018-07-24",
             "source": "SpaceManagement",
             "link": "http://paasweb.tpaas.youedata.com/#/front/spaceManage/main",
             "keyword": "空间管理",
             "title": "创建空间"
             },
            {"date": "2018-07-24",
             "source": "数据库管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/databaseServicePage/main",
             "keyword": "四类数据库管理",
             "title": "创建数据库服务"
             },
            {"date": "2018-08-24",
             "source": "应用管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/image/imageList",
             "keyword": "镜像仓库",
             "title": "创建镜像"
             },
            {"date": "2018-08-24",
             "source": "应用管理",
             "link": "http://paasweb.tpaas.youedata.com/#/front/AppLocation/AppLocation",
             "keyword": "应用仓库",
             "title": "创建应用"
             }
        ]
        ACTIONS = []
        i = 1
        for line in list:
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_id": i, #_id 也可以默认生成，不赋值
                "_source": {
                    "date": line['date'],
                    "source": line['source'],
                    "link": line['link'],
                    "keyword": line['keyword'],
                    "title": line['title']}
            }
            i += 1
            ACTIONS.append(action)
            # 批量处理
        success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    def Delete_Index_Data(self,id):
        '''
        删除索引中的一条
        :param id:
        :return:
        '''
        res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
        print(res)

    def Get_Data_By_Body(self):
        for i in range(1,10000):
            # doc = {'query': {'match_all': {}}}
            doc = {
                "query": {
                    "match": {
                        "keyword": "镜像仓库"
                    }
                }
            }
            _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)

            for hit in _searched['hits']['hits']:
                # print hit['_source']
                print(hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'], \
                hit['_source']['title'])


if __name__ == '__main__':
    obj =ElasticObj("paas", "paasweb", ip="210.13.50.105:31532")
    # obj.Index_Data()
    obj.Get_Data_By_Body()

