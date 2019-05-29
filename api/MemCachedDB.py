import memcache
class MemcachedDB():

    def __init__(self, hostname="127.0.0.1", port="11211"):
        self.hostname = "%s:%s" % (hostname, port)
        self.server = memcache.Client([self.hostname])

    def set(self, key, value, expiry=3600):
        self.server.set(key, value, expiry)

    def get(self, key):
        return self.server.get(key)

    def delete(self, key):
        self.server.delete(key)

    def gets(self,key):
        return self.server.gets(key)

    def cas(self,key,value,cas):
        return self.server.cas(key,value,noreply=cas)

    def decr(self,key):
        return self.server.decr(key)