#-*- coding: utf-8 -*-
import random

from api.MemCachedDB import MemcachedDB


class Extrasens:
    max_extrasens = 20 # количество экстрасенов
    extrasens = []

    def __init__(self):
        if len(self.extrasens) == 0 :
            i = 0
            while (i<= self.max_extrasens):
                self.extrasens.append('extrasens_'+str(i))
                i +=1
        pass

    def getRandomExtrasens(self):
        id = random.randint(0,self.max_extrasens)
        return self.extrasens[id]

    def getAllExtrasensHistory(self):
        pass

    def getExtrasenseNumber(self,exrasense):
        return exrasense,random.randint(0,99)

    def getCredibility(self,extrasens):
        memcash = MemcachedDB()
        val = memcash.get('credibility_'+extrasens)
        if val == None:
            return 0
        return val

    def setCredibility(self,extrasens,value):
        memcash = MemcachedDB()
        res  = memcash.set('credibility_'+extrasens,value)
        return res

    def incCredibility(self,extrasens):
        memcash = MemcachedDB()
        res = memcash.get('credibility_'+extrasens)
        if res == None:
            res = 1
        else :
            res += 1
        return memcash.set('credibility_' + extrasens,res)

        '''
        while True:
            res,cas = memcash.gets('credibility_'+extrasens)
            print res,cas
            if res in None:
                res = 0
            else :
                res += 1
            if memcash.cas('credibility_'+extrasens,res,cas):
                break
        '''
        pass

    def decCredibility(self,extrasens):
        memcash = MemcachedDB()
        res = memcash.get('credibility_'+extrasens)
        if res == None:
            res = 0
        else:
            memcash.decr('credibility_'+extrasens)
        pass

    def getCredibilityAll(self):
        memcash = MemcachedDB()
        res = []
        for ext in self.extrasens:
            val = memcash.get('credibility_'+ext)
            if val == None:
                val = 0
            res.append({"name":ext,"val":val})
            pass
        return res