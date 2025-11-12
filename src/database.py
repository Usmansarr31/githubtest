import mysql.connector

def getConnection():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="stock_db")
    
def init_db():
    
    connexion=getConnection()
    cursor=connexion.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produit(
        
        id INT PRIMARY KEY AUTO_INCREMENT,
        nom VARCHAR(255) NOT NULL,
        prix FLOAT NOT NULL,
        quantite INT NOT NULL
    )""")
    
    connexion.commit()
    cursor.close()
    connexion.close()