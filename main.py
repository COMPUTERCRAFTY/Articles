from flask import Flask,jsonify,request
import csv
all_articles=[]
with open("articles.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
liked_articles=[]
not_liked_articles=[]
app=Flask(__name__)
@app.route('/get-article')
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route('/liked-articles',methods=["POST"])
def liked_articles():
    article=all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201
@app.route('/not-liked-articles',methods=["POST"])
def not_liked_articles():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201
if __name__=="__main__":
    app.run()