# -*- coding: utf-8 -*-

from datetime import datetime
import time
import psycopg2

x = 10

while True:
    time.sleep(2)
    now = datetime.now()
    if x == now.hour:
        print "executa"
        con = psycopg2.connect(host='localhost', database='produto', user='dougras', password='senha')
        if con:
            print "Conectou"
            cur = con.cursor()
            # sql = "create table cidade (id serial primary key, nome varchar(100), uf varchar(2));"
            # cur.execute(sql)
            # sql = "insert into cidade (nome, uf) values ('São Paulo','SP');"
            # cur.execute(sql)
            # sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
            # cur.execute(sql)
            # con.commit()
            cur.execute('select * from cidade')
            recset = cur.fetchall()
            for rec in recset:
                print rec
            con.close()
        else:
            print "Deu ruim"

        time.sleep(86400) # um dia tem 86400 segundos
        print "Saiu"
