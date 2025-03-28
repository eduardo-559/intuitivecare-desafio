from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # Permite acesso do frontend

conn = psycopg2.connect(
    dbname="ans",
    user="desafio",
    password="desafio123",
    host="localhost",
    port="5432"
)

@app.route('/api/top-operadoras')
def top_operadoras():
    cur = conn.cursor()
    cur.execute("""
        SELECT reg_ans,
               SUM(CAST(REPLACE(vl_saldo_final, ',', '.') AS NUMERIC)) AS total_saldo
        FROM demonstrativos
        GROUP BY reg_ans
        ORDER BY total_saldo DESC
        LIMIT 10;
    """)
    rows = cur.fetchall()
    cur.close()
    return jsonify([
        {'reg_ans': row[0], 'total_saldo': float(row[1])}
        for row in rows
    ])

if __name__ == '__main__':
    app.run(debug=True)
