from flask import Flask, render_template
from database import get_db, create_tables

app = Flask(__name__)

create_tables()


@app.route("/")
def home():
    conn = get_db()

    products = conn.execute("""
        SELECT *
        FROM products
        ORDER BY product_name
    """).fetchall()

    conn.close()

    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)