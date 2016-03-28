#!/usr/bin/env python
import mysql.connector
from mysql.connector import errorcode
import random

class Validation:
  
    cursor=None
    connection=None
    
    def __init__(self):
    
        self.open()
            
    def open(self):
        try:
            self.connection=mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='test_arduino')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
        return self.connection
    
       ##  BEGIN close connection
    def close(self) :
        self.cursor.close()
        self.connection.close()
    ##  END close connection
    

    def execute_query(self,query):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query)
                rows=self.cursor.fetchall()
                return rows
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
     
    def create_random(self,begin,end):

        first = random.randint(begin,end)
        first = str(first)
        n = 5

        nrs = [str(random.randrange(10)) for i in range(n-1)]
        for i in range(len(nrs))    :
            first += str(nrs[i])
    
        return str(first)

        
    
    def three_var(self,query,first,sec):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
               self.cursor.execute(query,(first,sec))
               self.connection.commit()
               print "success" #add log info success
               return True;
    
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
        

        

            
    def two_var(self,query,value):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(value,))
                if(self.cursor.rowcount !=None):
                    for row in self.cursor:
                        return row[0]
                else:
                    return None
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
    def subtract_time(self,query):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query)
                if(self.cursor.rowcount !=None):
                    for row in self.cursor:
                        return row[0]
                else:
                    return None
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
                
            
            
            
            
    def two_var_update(self,query,value):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(value,))
                self.connection.commit()
                print "success" #add log info success
                return True;
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
