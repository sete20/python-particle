import sqlite3

db = sqlite3.connect('app.db')
# , FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
db.execute(
    'CREATE TABLE if not exists skills(id INTEGER  PRIMARY KEY,name TEXT, progress integer, user_id integer,created_at DATETIME DEFAULT CURRENT_TIMESTAMP)',
    
    )
db.execute(
    'CREATE TABLE if not exists users (id INTEGER  PRIMARY KEY,name TEXT, email Email ,password text, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
cr = db.cursor()
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into users(name,email,password) values('abdelrhman','abdelrhman.abdullah.10@gmail.com ','123')")
cr.execute("insert into skills(name,progress,user_id) values('abdelrhman',50,1)")
db.commit()
cr.execute('select * from skills')
print(cr.fetchone())
db.close()
