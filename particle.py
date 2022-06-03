import sqlite3


class particle :
    def __init__(self) -> None:
        pass
    def connectDb():
        try :
          db =sqlite3.connect('app.db')
          cr = db.cursor()
          cr.execute('select * from users')
          cr.execute(
              "update users set name = 'abdelrhman abdullah noureldin elmahdy' where name = 'abdelrhman'")

        #   cr.execute("delete from users where id = 1")
          db.commit()
          print(cr.fetchall())
          print('connected success')
        except:
            print('error')


classMethod = particle.connectDb()

