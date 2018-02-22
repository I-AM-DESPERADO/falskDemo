 # ！/usr/bin/python
from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from . import news
from .. import db
from flask import jsonify,request
import time,datetime
#from . import mysqlDB
#import mysqlDB.mysqlOperate #也可以这么写 导入某个包

__author__ = 'AidChow'


@news.route('/list/<page>', methods=['GET'])
def news_list(page):
    page = int(page)
    if page == 0:
        page = 1
    with db.connect().cursor() as cur:
        # sql = 'SELECT * from news_list limit %s,%s'
        sql = 'SELECT * from news_list order by  news_push_time DESC'
        cur.execute(sql)
        result = cur.fetchall()
        l = []
        if result is ():
            return jsonify({'code': 200, 'msg': 'load complete', 'content': None})
        for i in result:
            data = {'original_url': i[1], 'content_id': i[2],
                    'news_title': i[3], 'news_push_time': i[4],
                    'news_preview': i[5]}
            l.append(data)
    return jsonify({'code': 200, 'msg': 'request success', 'content': l})


@news.route('/content/<news_id>', methods=['GET'])
def news_content(news_id):
    with db.connect().cursor() as cur:
        sql = 'SELECT * from news_content WHERE news_p_id =%s'
        cur.execute(sql, news_id)
        result = cur.fetchone()
        if result is None:
            return jsonify({'code': 404, 'msg': 'page not found', 'content': None}), 404
        else:
            return jsonify({'code': 200, 'msg': 'request success', 'content': result[2]})


@news.route('/addFeedBack',methods=['POST'])
def addFeedback():
    # with db.connect().cursor() as cursor:
    # conn=pymysql.connect(host='59.68.29.90',user='root',passwd='dangxuan601',db='dangxuanDB',port=3306,charset='utf8')
    conn=db.connect()
    cursor=conn.cursor()#获取一个游标
    data=request.get_json()
    title=data["title"]
    print(title)
    nickname=data["nikename"]
    print(nickname)
    content=data["content"]
    res=(nickname,title,content)
    print(content)
    sql = "insert into feedbackinfo(username,feedbacktitle,feedbackcontent,feedback_timestamp)values(%s,%s,%s,unix_timestamp(now()))"
    try:
        result=cursor.execute(sql,res)
    except Exception as e:
        conn.rollback() #事务回滚
        print (e)
    conn.commit()
    cursor.close()
    conn.close()
    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': "true"})
    else:
        return jsonify({'code': "E01", 'message': '调用失败'})


@news.route("/carousel", methods=['POST'])
def carousel():
    with db.connect().cursor() as cursor:
        sql = "select picture_url from t_radio_carousel  order by picture_id  DESC limit 5  "
        cursor.execute("use dangxuanDB")
        cursor.execute(sql)
        result = cursor.fetchall()
    # cursor.execute("set names utf8")

    arr=[]
    j = 0
    for i in result:
        data = result[j]
        j=j+1
        arr.extend(data)
    if result:
        return jsonify({'code': 200, 'msg': 'request success', 'content': arr})
    else:
        return jsonify({'code': 404, 'msg': 'request failure', 'content': None})


@news.route('/getMagazineImage', methods=['POST'])
def getMagazineImage():
    with db.connect().cursor() as cursor:
        sql = "select first_logo_url,second_logo_url from t_magazine_logo where logo_flag in (select logo_flag from t_magazine_logo where logo_flag in (select logo_flag from t_magazine_logo group by logo_flag) order by logo_flag) limit 1"
        cursor.execute("use dangxuanDB")
        cursor.execute(sql)
        result = cursor.fetchall()

    arr = []
    j = 0
    for i in result:
        data = result[j]
        j = j+1
        arr.extend(data)
    if result:
        return jsonify({'code': 200, 'message': '获取成功', 'content': arr})
    else:
        return jsonify({'code': 404, 'message': '调用失败','content': None})


@news.route("/getMagazineList", methods=['POST'])
def getMagazineList():
    with db.connect().cursor() as cursor:
        sql = "select magazine_journal_no,magazine_journal_title,magazine_journal_picture_url,magazine_program_id from t_magazine_program order by magazine_program_id"
        cursor.execute("use dangxuanDB")
        cursor.execute(sql)
        result = cursor.fetchall()

    arr=[]
    j = 0
    for i in result:
        data = result[j]
        j=j+1
        arr.extend(data)
    if result:
        return jsonify({'code': 200, 'msg': '获取成功', 'content': arr})
    else:
        return jsonify({'code': 404, 'msg': '调用失败','content': None})


@news.route('/getMagazineContent',methods=['POST'])
def getMagazineContent():
    with db.connect().cursor() as cur:
         data=request.get_json()
         print(request.get_json())
         title_id = data["title_id"]
         print(title_id)
         cur.execute("select list_content from t_magazine_list where list_title =%s" ,title_id)
         result = cur.fetchall()
         arr = []
         j = 0
         for i in result:
             data ={"list_content":i[0]}
             j = j + 1
             arr.append(data)
    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': arr})
    else:
        return jsonify({'code': "E01", 'message': '调用失败','content': None})


@news.route('/getMagazineSearch',methods=['POST'])
def getMagazineSearch():
    with db.connect().cursor() as cur:
         data=request.get_json()
         key = data["inputKeywords"]
         print(key)
         keywords="%"+key+"%"
         content=(keywords,keywords)
         cur.execute("select list_title from t_magazine_list where list_title like %s or list_content like %s",content)
         result = cur.fetchall()
         arr = []
         j = 0
         for i in result:
             data = {"list_title":i[0]}
             j = j + 1
             arr.append(data)
         print(arr)
    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': arr})
    else:
        return jsonify({'code': "E01", 'message': '调用失败','content': None})


@news.route("/getRadioList", methods=['POST'])
def getRadioList():
    # conn = pymysql.connect(host="59.68.29.90", user="root", passwd="dangxuan601", charset='utf8mb4',
    #                        cursorclass=pymysql.cursors.DictCursor)
    # cursor = conn.cursor()
    with db.connect().cursor() as cursor:
        cursor.execute("use dangxuanDB")
        arr2 = []
        sql = "select distinct(program_date) from t_radio_program  order by program_id desc limit 5"
        cursor.execute(sql)
        rows=[]
        # old_rows = cursor.fetchall()
        # m=0
        # for i in old_rows:
        #     data={
        #         "program_date":i[0]
        #     }
        #     m=m+1
        #     rows.append(data)
        try:
            week=datetime.date.today().weekday()
            if week==0:
                rows=['周一','周五','周四','周三','周二']
            elif week==1:
                rows=['周二','周一','周五','周四','周三']
            elif week==2:
                rows=['周三','周二','周一','周五','周四']
            elif week==3:
                rows=['周四','周三','周二','周一','周五']
            elif week==4:
                rows=['周五','周四','周三','周二','周一']
            elif week==5:
                rows=['周五','周四','周三','周二','周一']
            elif week==6:
                rows=['周五','周四','周三','周二','周一']
        except:
            week==0
        for row in rows:
            # row1 = row['program_date']
            cursor.execute(
                "select program_name,program_picture_url ,program_id  from t_radio_program where program_date =%s order by program_id desc limit 3 ",
                row)
            j = 0
            res=[]
            old_res = cursor.fetchall()
            for r in old_res:
                mydata={
                    "programid": r[2],
                    "program_name": r[0],
                    "program_picture_url": r[1]
                }
                res.append(mydata)
            dict1 = {
                'weektime': row,
                'list': res
            }
            arr2.append(dict1)
        if rows:
            return jsonify({'code': 200, 'msg': 'request success', 'content': arr2})
        else:
            return jsonify({'code': 404, 'msg': 'request failure', 'content': None})


@news.route('/getRadioSearch',methods=['POST'])
def getRadioSearch():
        with db.connect().cursor() as cur:
            data = request.get_json()
            key = data["inputKeywords"]
            keywords = "%" + key + "%"
            content = (keywords, keywords)
            cur.execute(
                "select DISTINCT program_name,t_radio_program.program_picture_url,t_radio_program.program_id from t_radio_program,t_radio_content where t_radio_content.program_id=t_radio_content.program_id  and (program_name like %s or t_radio_content.program_introduction like %s)",
                content)

            old_result = cur.fetchall()
            result=[]
            for r in old_result:
                mydata={
                    "program_id": r[2],
                    "program_name": r[0],
                    "program_picture_url": r[1]
                }
                result.append(mydata)
            j = 0
            data = {"data": result

                    }
        if result:
            return jsonify({'code': "N01", 'message': '调用成功', 'content': data})
        else:
            return jsonify({'code': "E01", 'message': '调用失败', 'content': None})

@news.route('/getWeiboContent',methods=['POST'])
def getWeiboContent():
    with db.connect().cursor() as cur:
        cur.execute("select * from t_weibo order by record_sid DESC")
        old_result = cur.fetchall()
        result=[]
        for res in old_result:
            data={
                "cite": res[3],
                "img": res[4],
                "msg_from": res[2],
                "others_repost_num": res[7],
                "others_talk_num": res[8],
                "others_time": res[5],
                "post_time": res[6],
                "record_sid": res[0],
                "self_repost_num": res[9],
                "self_talk_num": res[10],
                "text_content":res[1]
            }
            result.append(data)

    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': result})
    else:
        return jsonify({'code': "E01", 'message': '调用失败', 'content': None})

@news.route('/getMagazineListByPeriod',methods=['POST'])
def getMagazineListByPeriod():
    with db.connect().cursor() as cur:
         data=request.get_json()
         #print(request.get_json())
         title_id = data["title_id"]
         print(title_id)
         # sql = "select list_content from t_magazine_list where magazine_list_id ='%s' ,title_id"
         cur.execute("select list_title from t_magazine_list where magazine_program_id ='%s'order by insert_time desc" ,title_id)
         # cur.execute(sql)
         result = cur.fetchall()
         arr = []
         j = 0
         for i in result:
             data = result[j]
             j = j + 1
             arr.append(data)
    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': arr})
    else:
        return jsonify({'code': "E01", 'message': '调用失败','content': None})

@news.route('/getMagazineContentByPeriod',methods=['POST'])
def getMagazineContentByPeriod():
    with db.connect().cursor() as cur:
         data=request.get_json()
         title_id = data["title_id"]
         print(title_id)
         cur.execute("select list_content from t_magazine_list where magazine_program_id ='%s'order by insert_time desc" ,title_id)
         result = cur.fetchall()
         arr = []
         j = 0
         for i in result:
             data = { "list_content":i[0]}
             j = j + 1
             arr.append(data)
    if result:
        return jsonify({'code': "N01", 'message': '调用成功', 'content': arr})
    else:
        return jsonify({'code': "E01", 'message': '调用失败','content': None})

@news.route('/getTelevisionTitle',methods=['POST'])
def getTelevisionTitle():
    with db.connect().cursor() as cur:
        cur.execute("select television_title from t_television_program")
        old_result = cur.fetchall()
        result=[]
        for res in old_result:
            data={"television_title": res[0]}
            result.append(data)
        tv_list = {
        'tv_list':result
         }
        if result:
            return jsonify({'code': "N01", 'message': '调用成功', 'content': tv_list})
        else:
            return jsonify({'code': "E01", 'message': '调用失败', 'content': None})


@news.route('/getTelevisionContentByTitle',methods=['POST'])
def getTelevisionContentByTitle():
    data = request.get_json()
    title_name = data["title_name"]
    print(title_name)
    with db.connect().cursor() as cur:
        cur.execute("select * from t_television_program_content where television_program_id=(select television_program_id from t_television_program where television_title=%s)",title_name)
        old_result = cur.fetchall()
        result=[]
        for res in  old_result:
            data={
                "note": res[6],
                "television_program_content_id": res[0],
                "television_program_id": res[1],
                "thumbnails_url": res[2],
                "video_introduction": res[4],
                "video_timestamp": res[5],
                "video_url": res[3]
            }
            result.append(data)

        if result:
            return jsonify({'code': "N01", 'message': '调用成功', 'content': result})
        else:
            return jsonify({'code': "E01", 'message': '调用失败', 'content': None})

@news.route('/getTelevisionSearch',methods=['POST'])
def getTelevisionSearch():
        with db.connect().cursor() as cur:
            data = request.get_json()
            key = data["inputKeywords"]
            keywords = "%" + key + "%"
            content = (keywords, keywords)
            cur.execute("select DISTINCT  * from t_television_program_content where video_introduction like %s",keywords)
            old_result = cur.fetchall()
            result=[]
            for res in old_result:
                data = {
                    "note": res[6],
                    "television_program_content_id": res[0],
                    "television_program_id": res[1],
                    "thumbnails_url": res[2],
                    "video_introduction": res[4],
                    "video_timestamp": res[5],
                    "video_url": res[3]
                }
                result.append(data)

            if result:
                return jsonify({'code': "N01", 'message': '调用成功', 'content': result})
            else:
                return jsonify({'code': "E01", 'message': '无数查询数据', 'content': None})
@news.route('/getHistoryRecord',methods=['POST'])
def getHistoryRecord():
    data = request.get_json()
    res=[]
    program_id = data["program_id"]
    # program_date=data['program_date']
    # keywords=(program_name,program_date)
    with db.connect().cursor() as cur:
        cur.execute('select program_date,program_name from t_radio_program where program_id=%s',program_id )
        old_result = cur.fetchall()
        program_date=old_result[0][0]
        program_name=old_result[0][1]
        keywords=(program_name,program_date)
        cur.execute('select program_id from t_radio_program where  program_name=%s and program_date=%s order by program_id desc limit 1,10',keywords)
        program_ids=cur.fetchall()
        for program_id in program_ids:
            cur.execute('select program_content_id, program_audio_url,program_audio_duration,program_name,t_radio_content.program_picture_url from t_radio_content, t_radio_program where t_radio_content.program_id= t_radio_program.program_id and t_radio_content.program_id=%s',program_id)
            contents=cur.fetchall()
            # print(contents)
            for content in contents:
                data={
                "program_content_id":content[0],
                "program_audio_url":content[1],
                "program_audio_duration":content[2],
                "program_name":content[3],
                "program_picture_url":content[4]
                }
                res.append(data)
    # print(res)
        if res:
            return jsonify({'code': "N01", 'message': '调用成功', 'content': res})
        else:
            return jsonify({'code': "E01", 'message': '无数查询数据', 'content': None})
@news.route("/getRadioContent", methods=['POST'])
def getRadioContent():
    with db.connect().cursor() as cur:
        data = request.get_json()
        program_id=data['program_id']
        cur.execute("select program_picture_url,program_audio_url,program_introduction ,program_audio_anchor,program_audio_category ,program_audio_duration from t_radio_content where program_id=%s",program_id)
        results = cur.fetchall()
        if results:
            res={"program_picture_url":results[0][0],
            "program_audio_url":results[0][1],
            "program_introduction":results[0][2],
            "program_audio_anchor":results[0][3],
            "program_audio_category":results[0][4],
            "program_audio_duration":results[0][5]
            }
            return jsonify({'code': 200, 'msg': 'request success', 'content': res})
        else:
            return jsonify({'code': 404, 'msg': 'request failure', 'content': None})
