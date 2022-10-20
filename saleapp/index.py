from flask import render_template
from saleapp import app
import dao




@app.route("/")
def home():
    cates = dao.load_categories()
    return render_template('index.html', categories=cates)






if __name__ == '__main__':
    app.run(debug=True)
