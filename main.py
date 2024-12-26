import os
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/sozluk.html')

@app.route("/sozluk")
def sozluk():
    dictionary = {"10": "tadic", "17": "irfan can", "9": "dzeko","24":"otarwolde","7":"ferdi","5":"ismail yüksek"}
    return render_template("sozluk.html", data=dictionary)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()