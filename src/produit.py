from src.database import getConnection

class Produit:
    def __init__(self, nom, prix, quantite):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    
    def save(self):
        connexion = getConnection()
        cursor = connexion.cursor()
        
        if self.id is None:
            cursor.execute("""
            INSERT INTO produit (nom, prix, quantite) VALUES (%s, %s, %s)
            """, (self.nom, self.prix, self.quantite))
            self.id = cursor.lastrowid
        
        else:
            cursor.execute(
            "UPDATE produit SET nom=%s, prix=%s, quantite=%s WHERE id=%s", 
            (self.nom, self.prix, self.quantite, self.id)
            )
            connexion.commit()
            cursor.close()
            connexion.close()
    @staticmethod    
    def find():
        
        connexion=getConnection()
        cursor=connexion.cursor(dictionary=True)
        
        cuursor.execute("SELECT * FROM produit WHERE id=%s", (id,))
        
        row = cursor.fetchone()
        cursor.close()
        connexion.close()
        
        return Produit(row['nom'], row['prix'], row['quantite']) if row else None
    
    @staticmethod
    
    def all():
        
        conn=getConnection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produit")
        rows=cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return [Produit(row['nom'], row['prix'], row['quantite']) for row in rows]