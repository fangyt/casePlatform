from flask import Flask,render_template,request,redirect,url_for
from datetime import timedelta

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route('/home/',methods=["GET","POST"])
def home():
    print(request.form)
    return render_template('html/home.html')

@app.route('/login',methods=["GET","POST"])
def login():

    if request.method == 'POST':

        email = request.form['inputEmail']
        pwd = request.form['inputPassword']

        if email == 'fangyt0810@163.com' and pwd == '123456':

            return  redirect(url_for('home'))

    return render_template('html/index.html')


@app.route('/object',methods=["GET","POST"])
def objectCase():

    return render_template('html/objectCase.html')

if __name__ == '__main__':
    app.run(debug=True)
