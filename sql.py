import pymysql as sql


def setdb():
    #db 연결
    db = sql.connect(
        user='nl',
        passwd='nowleague',
        host='138.2.121.169',
        db='NL',
        charset='utf8'
    )

    return db


def setcurser(db):
    cursor = db.cursor(sql.cursors.DictCursor)
    return cursor


def getselectquery(tablename, columns, condition):
    query = 'SELECT ' + columns + ' FROM NL.' + tablename + ' WHERE ' + condition
    return query
