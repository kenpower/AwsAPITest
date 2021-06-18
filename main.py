import pymysql
import secrets

host = 'database-1.c7ebogjv7tmg.eu-west-1.rds.amazonaws.com'
user = 'admin'
database = 'test_db'
password = secrets.password

create_user_table =("CREATE TABLE `users` ("
                    "`id` int(11) NOT NULL AUTO_INCREMENT, "
                    "`email` varchar(255) COLLATE utf8_bin NOT NULL, "
                    "`password` varchar(255) COLLATE utf8_bin NOT NULL, "
                    "PRIMARY KEY (`id`)"

                    ") AUTO_INCREMENT=1 ;")


def create_table(cur):
    cur.execute(create_user_table)
    message = cur.fetchall()
    print(message)


def create_db():
    pre_db_connection = pymysql.connect(
        user=user,
        password=password,
        host=host)
    with pre_db_connection.cursor() as cur:
        cur.execute("CREATE DATABASE test_db;")
        res = cur.fetchall()
        print("Create ", res)
        cur.execute("SHOW DATABASES")
        dbs = cur.fetchall()
        print("Databases: {} ", dbs)


def add_user(cur, email, password):
    insert_sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cur.execute(insert_sql, (email, password))
    connection.commit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create_db()

    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        database=database)
    with connection.cursor() as cursor:
        #create_table(cursor)
        add_user(cursor, 'user@test.com', '1234')
        sql = "SELECT `id`, `email`, `password` FROM `users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
