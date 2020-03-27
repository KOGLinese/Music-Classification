import pymysql
import pandas as pd
from sqlalchemy import create_engine
class SQL():
    def __init__(self):
        # 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
        self.address = "localhost"
        self.user = "root"
        self.password = "lsj123"
        self.db_name = "graduation"

    def insert_song(self, values):
        db = pymysql.connect(self.address, self.user, self.password, self.db_name,charset='utf8')
        # 插入一条记录
        ss = "("
        for i in range(0,5):
            ss=ss + "\'"+str(values[i])+"\'"
            if i == 4:
                ss=ss+")"
            else:
                ss=ss+","
        sql = "insert ignore into songs(song_id,song_name,song_author,song_lrc,song_url)" \
              " values "+ss

        # 接着我们获取 cursor 来操作我们的 pytest 这个数据库
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print("成功插入数据")
        db.close()

    def insert_recoder(self, values):
        db = pymysql.connect(self.address, self.user, self.password, self.db_name,charset='utf8')
        # 插入一条记录
        ss = "("
        for i in range(0,7):
            ss=ss + "\'"+str(values[i])+"\'"
            if i == 6:
                ss=ss+")"
            else:
                ss=ss+","
        sql = "insert ignore into recoder(user_id,song_id,tag,start_time,end_time,times,message) " \
              " values "+ss

        # 接着我们获取 cursor 来操作我们的 pytest 这个数据库
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print("成功插入数据")
        db.close()

    def get_recoder_byUid(self,uid):
        """
        返回uid用户的recoder数据
        :param uid:
        :return:
        """
        engine =pymysql.connect(self.address, self.user, self.password, self.db_name,charset='utf8')
        sql = "select * from recoder where user_id="+"\'"+str(uid)+"\'"
        result = pd.read_sql_query(sql,con=engine)
        # print(result)
        return result


if __name__ == '__main__':
    sql = SQL()
    sql.get_recoder_byUid(393361316)
