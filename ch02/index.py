from flask import Flask, render_template, request
import pymysql   # 빠져 있어서 추가했어요!

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["Post"])
def save_db():
    data = request.get_json()
    print(data.get("count"))
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='Study')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO numcount(num) VALUES({data.get('count')})")
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/send", methods=["POST"])
def send_data():   # 함수 이름 send → send_data 로 변경
    data = request.json
    print(data["count"])
    return {"message": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
