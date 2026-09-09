import mysql.connector
import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="blood_db"
        )
        print("Connection Successfully")

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""
                insert into donor(name,blood_group,phone,city,last_donation)
                values(%s,%s,%s,%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor added Successfully...")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="Select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record==None:
                print("Donor not found!")
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id = %s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record==None:
                print("Donor not found")
            else:
                query = "delete from donor where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor deleted Successfully...!")
                print("Donor not found")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="Select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record != None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update donor set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor details update successfully")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)


donor_instance=BloodDonorManager()
# donor_instance.post(name="Anu",blood_group="AB-",phone="987555550",city="Alappuzha",last_donation=datetime.datetime.today())
#donor_instance.get()
#donor_instance.retrieve()
donor_instance.delete(id=5)
# donor_instance.get()
# donor_instance.put(id=4,name="Ansiya",blood_group="A+",phone="927555550",city="Kunnathery",last_donation=datetime.datetime.today())
# donor_instance.put(id=5,name="Anu",blood_group="A-",phone="5486548794",city="Calicut",last_donation=datetime.datetime.today())