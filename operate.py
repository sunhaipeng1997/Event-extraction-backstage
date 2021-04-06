from learn_sql import db, Student,Article

# s = Student(name="张三",gender="男",phone="1234567")
# s2 = Student(name="张三1",gender="男",phone="12345678")
# s3 = Student(name="张三2",gender="男",phone="12345679")
# s4 = Student(name="张三3",gender="男",phone="12345670")
# s5 = Student(name="张三4",gender="男",phone="12345671")
# db.session.add(s2)
# db.session.add(s3)
# db.session.add(s4)
# db.session.add(s5)
# db.session.commit()

s1 = Article(title="张三1",content="content1",result="result1")
s2 = Article(title="张三2",content="content1",result="result1")
s3 = Article(title="张三3",content="content1",result="result1")
s4 = Article(title="张三4",content="content1",result="result1")
s5 = Article(title="张三5",content="content1",result="result1")
# db.session.add(s1)
# db.session.add(s2)
# db.session.add(s3)
# db.session.add(s4)
# db.session.add(s5)
# db.session.commit()
# stu = Student.query.get(1)
# stu = Student.query.all()
# stu = Student.query.filter(Student.id >= 2)
# stu = Student.query.filter_by(name="张三").all()
#
# stu = Student.query.get(2)
# stu.name = "list"
# db.session.add(stu)
# db.session.commit()
# print(stu)
# for i in stu:
#     print(i.name,i.id)

articles = Article.query.all()
print(articles)