# encoding = utf-8
import redis


class ConnectRedis(object):
    def __init__(self, host, port):
        self.conn = redis.ConnectionPool(
            host=host,
            port=port
        )
        r = redis.Redis(connection_pool=self.conn)
        pipe = r.pipeline(transaction=True)
        r.set('zcx', '5555')
        r.set('zcx', '6666')
        pipe.execute()
        print(r.mget('zcx'))


if __name__ == "__main__":
    ConnectRedis(host='210.13.50.105', port='31859')
