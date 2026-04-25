from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = pymysql.connect(
            host='appdb.crs4qkg0w1yz.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='11sayu23',
            database='aapdb'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return "Backend Connected to DB: " + str(data)

    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
