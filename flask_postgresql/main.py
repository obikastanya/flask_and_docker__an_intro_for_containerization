from flask import Flask
import os
from psycopg2 import connect

app=Flask(__name__)


class Connection:
    def __new__(cls) -> object:

        return connect(
            database=os.getenv("DB"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT")
        )

@app.get("/product")
def get_product():
    conn=Connection()
    cursor=conn.cursor()

    query="""
        select * from product
    """
    cursor.execute(query)

    result=cursor.fetchall()

    response_data=[]

    for item in result:
      response_data.append(
        {
          "id": item[0],
          "title": item[1],
          "description": item[2],
          "price": item[3],
          "discountPercentage": item[4],
          "rating": item[5],
          "stock": item[6],
          "brand": item[7],
          "category": item[8],
          "thumbnail": item[9],
          "images": item[10]
        }
      )
    conn.close()

    return {"result":response_data} 

if __name__=="__main__":
  app.run(debug=True, port=5000, host="0.0.0.0")