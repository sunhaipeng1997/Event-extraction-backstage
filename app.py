import requests, json

from flask import Flask, jsonify, abort, request
from learn_sql import app, db, Article

PREFIX = "/api"
@app.route(PREFIX+'/articles', methods=['GET'])
def get_articles():
    # articles = Article.query.all()
    page = request.args.get('page', 1)
    title = request.args.get("content")
    if title == None:
        articles = Article.query.paginate(page=int(page), per_page=10)
    else:
        articles = Article.query.filter(Article.content.contains(title)).paginate(page=int(page), per_page=10)

    result = []
    data = {}
    pageData = {
        'total': articles.total,
        'page': articles.page,
    }
    for article in articles.items:
        result.append(article.to_json())
    data['articles'] = result
    data['pageData'] = pageData
    return jsonify(data), 200


@app.route(PREFIX+'/addArticle', methods=['POST'])
def add_article():
    content = request.get_json()['data']['content']
    ## 把数据字典转化为json字符串储存
    result = json.dumps(request.get_json()['data']['result'], ensure_ascii=False)
    article = Article(content=content, result=result)
    db.session.add(article)
    db.session.commit()
    msg = "添加成功"
    return jsonify(msg), 200


@app.route(PREFIX+'/handleArticle', methods=['POST'])
def handle_article():
    content = request.get_json()['data']['content']
    data = {
        'text': content}
    url = 'http://127.0.0.1:5003/mas/rest/fire/v1'
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data, ensure_ascii=False)
    ## post的时候，将data字典形式的参数用json包转换成json格式。
    response = requests.post(url=url, headers=headers, data=data.encode("UTF-8"))
    print(response)
    ## 把json字符串转化为数据字典
    data = json.loads(response.text)
    return jsonify(data), 200


@app.route(PREFIX+'/deleteArticle', methods=['POST'])
def delete_article():
    id = request.get_json()['data']['id']
    articles = Article.query.all()
    for article in articles:
        if article.id == id:
            db.session.delete(article)
            db.session.commit()
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(port=7777)
