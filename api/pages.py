#-*- coding: utf-8 -*-
import random

import datetime
from flask import request,session,render_template

from api.Extrasens import Extrasens
from api.MemCachedDB import MemcachedDB


def index(username):
    extrasense = Extrasens()
    expCredibility =  extrasense.getCredibilityAll()

    userHis = getUserHistory(username)

    return render_template('index.html',expCredibility = expCredibility,userHis = userHis)

def getExtrasenseAnswer(user=None):
    extrasense = Extrasens()
    count_ext  = random.randint(2,6) # количество экстрасеносв ответивших
    extData = []
    extID = []
    for i in xrange(count_ext):
        ext_id = extrasense.getRandomExtrasens()
        while (extID.count(ext_id) != 0):
            ext_id = extrasense.getRandomExtrasens()
        extID.append(ext_id)
        ext_id,answer = extrasense.getExtrasenseNumber(ext_id)
        extData.append({"name":ext_id.replace("extrasens_",u"Экстрасенс "),"id":ext_id,"answer":answer})

    memcash = MemcachedDB()
    memcash.set("answer_"+user,extData)
    return render_template("extrasense.html",extData=extData)

'''
   проверка введенного номера и обработка того что угадали экстрасенсы
'''
def setUserNumber(request,user):
    extrasense = Extrasens()
    memcash = MemcachedDB()
    answer = memcash.get("answer_"+user)
    dt = request.form
    num = int(dt['number'])
    print answer
    print num
    for l in answer:
        if l['answer'] == num:
            extrasense.incCredibility(l['id'])
        else :
            extrasense.decCredibility(l['id'])
    userHis = memcash.get("userHistory_"+user)
    if userHis is None :
        userHis = []

    now = datetime.datetime.now()
    userHis.append({"userValue":num,"createDate":now.strftime("%d-%m-%Y %H:%M")})
    res = memcash.set("userHistory_"+user,userHis)
    memcash.delete("answer_"+user)

    return render_template("start.html")

def getExtrasenseHistory():
    pass

def getUserHistory(user):
    memcash = MemcachedDB()
    res = memcash.get("userHistory_" + user)
    res.reverse()
    return res

def getExtrasenseRaiting():
    extrasense = Extrasens()
    expCredibility =  extrasense.getCredibilityAll()

    return render_template("table_extrasense_raiting.html",expCredibility = expCredibility)