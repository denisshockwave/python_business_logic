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

                print "denis"
        else:
            print "CUrsor is none"
            
    def check_exist_state(self,query,event_code):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(event_code,))
                self.cursor.fetchall()
                rowCount=self.cursor.rowcount
                return rowCount
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
    def get_with_phone(self,query,phone_no):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(phone_no,))
                self.cursor.fetchall()
                rowCount=self.cursor.rowcount
                return rowCount
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
    def check_user_booked(self,query,phone_no,event_code):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(phone_no,event_code))
                self.cursor.fetchall()
                return self.cursor.rowcount
            
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
                    
    def check_ticket_availability(self,query,event_code):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(event_code,))
                
                for row in self.cursor:
                    return row[0]
                
                
            
    
            
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
    def insert_db(self,query,var1,var2,var3):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                data=(var1,var2,var3)
                self.cursor.execute(query,data)
                self.connection.commit()
                print "success" #add log info success
    
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
     
    def create_random(self):

        first = random.randint(1,9)
        first = str(first)
        n = 5

        nrs = [str(random.randrange(10)) for i in range(n-1)]
        for i in range(len(nrs))    :
            first += str(nrs[i])
    
        return str(first)
     
    def store_user(self,query,name,phone_no):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
               self.cursor.execute(query,(name,phone_no))
               self.connection.commit()
       
    
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
        
    
    def two_var(self,query,first,sec):
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
        
    def get_ticket_code(self,query,first,sec):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
               self.cursor.execute(query,(first,sec))
               for row in self.cursor:
                    return row[0]
     
    
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
        
        
    def get_code(self,query,phone):
        if(self.connection==None):
            print "No connection"
            return
        self.cursor=self.connection.cursor()
        if(self.cursor!=None):
            try:
                self.cursor.execute(query,(phone,))
                if(self.cursor.rowcount !=None):
                    for row in self.cursor:
                        return row[0]
                else:
                    return None
            
            except mysql.connector.Error as err:

                print err
        else:
            print "CUrsor is none"
            
            
    def one_var(self,query,value):
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
                
            
            
            
            
    def one_var_update(self,query,value):
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
            
