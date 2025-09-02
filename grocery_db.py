import sqlite3

class GMS:
    def __init__(self,db):
        self.con  = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS data(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         Product_name TEXT NOT NULL,
                         Price INTEGER NOT NULL,
                         Quantity INTEGER NOT NULL
                         )
                    """)
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM data")
        return self.cur.fetchall()
    
    def add(self, product_name, price, qty):
        add = "INSERT INTO data (Product_name, Price, Quantity) VALUES (?,?,?)"
        self.cur.execute(add,(product_name, price, qty))
        self.con.commit()

    
    def update(self,id_val,product_name,price,qty):
        update = "UPDATE data SET Product_name=?, Price=?, Quantity=? WHERE id=?"
        self.cur.execute(update, (product_name, price, qty, id_val))
        self.con.commit()
    
    def delete(self,id_val):
        self.cur.execute("DELETE FROM data WHERE id=?",(id_val,))
        self.con.commit()
