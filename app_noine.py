from noine import nine

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def input():
    return render_template("input.html")

@app.route("/result", methods=['POST','GET'])
def ninenineahbikinbingungninamafungsi():
    data_input = (request.form)
    integer=data_input.get('int')

    list_int=list(map(int,integer.split()))
    what_nine_lst=nine(list_int)
    what_nine_str=", ".join(map(str,what_nine_lst))
    return render_template("result.html",result=what_nine_str)

if __name__ == "__main__":
    app.run()