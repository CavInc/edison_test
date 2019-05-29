#-*- coding: utf-8 -*-
import sqlite3

class WorkDB:
  conn = None
  #:memory:
  def __init__(self,base):
    self.conn = sqlite3.connect(base)

  def query(self,sql):
    cur = self.conn.cursor()
    cur.execute(sql)
    self.lid = cur.lastrowid
    pass

  def queryResult(self,sql):
    cur = self.conn.cursor()
    cur.execute(sql)
    return cur.fetchall()
    pass

  def commit(self):
    self.conn.commit()

  def getlastid(self):
    return self.lid