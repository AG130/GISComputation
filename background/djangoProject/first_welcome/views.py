from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
from subprocess import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from .models import *
from django.contrib.auth.hashers import make_password

import json


# Create your views here.
# python manage.py runserver


def register(request):
    if request.method == "GET":
        username = request.GET.get("username")
        useremail = request.GET.get("useremail")
        password = request.GET.get("password")
        # password2 = request.GET.get("password2")
        if User.objects.filter(username=username):  # 用户名已存在
            error_message = "用户名已存在"
            return JsonResponse(data={'result': '用户名已存在'})
        # elif password != password2:  # 两次密码不一致
        #     error_message = "两次密码不一致，请重新输入"
        #     return render(request, "register.html", {"error_message": error_message})
        else:  # 可以注册
            User.objects.create(username=username, password=make_password(password)
                                , useremail=useremail)  # 增
            request.session['username'] = username  # 添加session
            return JsonResponse(data={'result': '可以注册'})
    else:
        return JsonResponse(data={'result': 'else'})


def user_logout(request):
    logout(request)
    return render(request, "index.html")


def welcome(request):
    # os.system('notepad')
    if request.method == "GET":
        print('welcome')
        return render(request, "welcome.html")

    # if request.method == "POST":
    #     mypyenv = "D:\Pytorch_virtualenv\Scripts\python.exe"
    #     # "D:\Pytorch_virtualenv\Scripts\python.exe"
    #
    #     proc = Popen(mypyenv + ' -u D:\GIS\djangoProject/first_welcome/test_py/test_py_stay_points.py', shell=True,
    #                  stdout=PIPE)
    #     proc.wait()
    #     py_test_output=proc.stdout.read().decode().strip()
    #     print(py_test_output)
    #     return render(request, "welcome.html",
    #                   {"username":py_test_output})


def index(request):
    # 前端到后端传参
    if request.method == "POST":
        print("request.method == GET")
        return render(request, "index.html")

    # if request.method == "POST":
    #     print("request.method == POST")
    #
    #     print(request.POST.get("username"))
    #     print(request.POST.get("password"))
    #
    #     return render(request, "welcome.html",
    #       {"username":request.POST.get("username")})

    if request.method == "GET":
        user = authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
        if user is not None:
            return JsonResponse(data={'result': 'success'})
        else:
            return JsonResponse(data={'result': 'fail'})
    else:
        return JsonResponse(data={'result': 'else'})


# def index_pro(request):
#     if request.method == "POST":
#         user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
#         if user:
#             login(request, user)
#             return render(request, "welcome.html", {"username": request.POST.get("username")})
#         else:
#             return render(request, "index.html", {"error_message": "用户名或密码错误！"})
#     else:
#         return render(request, "index.html")
# python manage.py runserver

def baidu_webGIS_try(request):
    return render(request, "baidu_webGIS_try.html")


def webGIS_1(request):
    return render(request, "webGIS_1.html")


def db_to_web(request):
    backx = gis_table.objects.all()
    print(backx)
    backget = gis_table.objects.get(name="路人甲")
    print(backget)
    print(type(backget))
    print(backget.name)
    print(backget.sex)
    print(backget.locate_x)
    print(backget.locate_x_float)
    return render(request, "baidu_webGIS_try.html")


@require_GET
def all_explore_form_db(request):  # 查
    scences = gis_table.objects.all()
    dict = {"code": 0, "msg": "", "data": []}
    count = scences.count()
    dict['count'] = count

    #   写入：
    for row in scences:
        row_dict = {}
        row_dict['table_id'] = row.table_id
        row_dict['name'] = row.name
        row_dict['id_card'] = row.id_card
        row_dict['address'] = row.address
        row_dict['lat'] = row.lat
        row_dict['lon'] = row.lon
        row_dict['phone'] = row.phone
        row_dict['checkdate'] = row.checkdate
        row_dict['result'] = row.result
        dict['data'].append(row_dict)
    return JsonResponse(data={'result': dict})


@require_GET
def add_to_db(request):  # 增
    value = request.GET
    gis_table.objects.create(
        table_id=value.get('table_id'),
        name=value.get('name'),
        id_card=value.get('id_card'),
        address=value.get('address'),
        lat=value.get('lat'),
        lon=value.get('lon'),
        phone=value.get('phone'),
        checkdate=value.get('checkdate'),
        result=value.get('result')
    )
    return JsonResponse(data={'result': 'success'})


def deleta_from_db(request):  # 删
    will_delete_id = request.GET.get('value')
    t = gis_table.objects.get(table_id=will_delete_id)
    t.delete()
    return JsonResponse(data={'result': 'success'})


def change_from_db(request):  # 改
    change_id = request.GET.get('id')
    change_type = request.GET.get('type')
    change_value = request.GET.get('value')
    # {'type':   ,'value':   }
    # 判断查询类型
    if change_type == "name":
        t = gis_table.objects.get(table_id=change_id)
        t.name = change_value
        t.save()

    elif change_type == "id_card":
        t = gis_table.objects.get(table_id=change_id)
        t.id_card = change_value
        t.save()

    elif change_type == "address":
        t = gis_table.objects.get(table_id=change_id)
        t.address = change_value
        t.save()

    elif change_type == "lat":
        t = gis_table.objects.get(table_id=change_id)
        t.lat = float(change_value)
        t.save()

    elif change_type == "lon":
        t = gis_table.objects.get(table_id=change_id)
        t.lon = float(change_value)
        t.save()

    elif change_type == "checkdate":
        t = gis_table.objects.get(table_id=change_id)
        t.checkdate = change_value
        t.save()

    elif change_type == "result":
        t = gis_table.objects.get(table_id=change_id)
        t.result = change_value
        t.save()

    # elif (change_type == "rect_explore"):
    #     t = gis_table.objects.get(id=change_id)
    #     t.locate_x_float = change_value[0]
    #     t.locate_y_float = change_value[1]
    #     t.locate_x = str(change_value[0])
    #     t.locate_y = str(change_value[1])
    #     t.save()

    elif change_type == "phone":
        t = gis_table.objects.get(table_id=change_id)
        t.phone = change_value
        t.save()

    return JsonResponse(data={'result': 'success'})


def cell_ajax_post(request):
    return render(request, "cell_ajax_post.html")


@require_GET
def all_area_form_db(request):  # 查区域路径
    scences = positive_line_area.objects.all()
    dict = {"code": 0, "msg": "", "data": []}
    count = scences.count()
    dict['count'] = count
    #   写入：
    for row in scences:
        row_dict = {}
        row_dict['lng'] = row.center_lng
        row_dict['lat'] = row.center_lat
        row_dict['radius'] = row.center_radius
        row_dict['line'] = []

        all_points_str = row.line_points.split('T')

        one_line_points = {"points": []}

        for i in range(len(all_points_str)):
            one_point_xy = all_points_str[i].split("E")
            one_xy = {}
            one_xy['lng'] = float(one_point_xy[0])
            one_xy['lat'] = float(one_point_xy[1])

            one_line_points['points'].append(one_xy)
            row_dict['line'].append(one_line_points)

        dict['data'].append(row_dict)

    # print(dict)
    return JsonResponse(data={'result': dict})


@require_GET
def api_stay_points_return(request):  # 停驻点api
    stay_points_id = request.GET.get('id')
    dist_threh = request.GET.get('dist_th')
    time_threh = request.GET.get('time_th')
    print(stay_points_id, dist_threh, time_threh)
    command = "python /Users/wsy/GIS/djangoProject/stay_points_explore/api_id_out_points.py " \
              + str(stay_points_id) + ' ' + str(dist_threh) + ' ' + str(time_threh)
    r = os.popen(command)
    info = r.readlines()  # 读取命令行的输出到一个list
    print(len(info))

    dict = {"code": 200, "msg": "", "data": []}
    count = len(info)
    dict['count'] = count

    #   写入：
    for line in info:
        row_dict = {}
        row_dict['points'] = []

        one_xy = {}
        one_xy['lng'] = float(line.split(' ')[0])
        one_xy['lat'] = float(line.split(' ')[1])

        row_dict['points'].append(one_xy)

        dict['data'].append(row_dict)

    # print(dict)

    return JsonResponse(data={'result': dict})


@require_GET
def api_add_line(request):
    # print(request.GET.get('line_id'))
    # print(request.GET.get('people_name'))
    # print(request.GET.get('people_id_card'))
    # print(request.GET.get('time'))
    # print(request.GET.get('line_info'))
    loc_x_y_list = request.GET.getlist('loc_x_y')

    positive_info.objects.create(line_id=request.GET.get('line_id'),
                                 people_name=request.GET.get('people_name'),
                                 people_id_card=request.GET.get('people_id_card'),
                                 time=request.GET.get('time'),
                                 line_info=request.GET.get('line_info'))

    for i in range(len(request.GET.getlist('loc_x_y'))):
        positive_line.objects.create(line_id=request.GET.get('line_id'),
                                     people_name=request.GET.get('people_name'),
                                     people_id_card=request.GET.get('people_id_card'),
                                     time=request.GET.get('time'),
                                     line_info=request.GET.get('line_info'),
                                     locate_x_float=loc_x_y_list[i].split(',')[0],
                                     locate_y_float=loc_x_y_list[i].split(',')[1], )

    return JsonResponse(data={'result': 'success'})


@require_GET
def api_get_positive_info(request):
    scences = positive_info.objects.all()
    dict = {"code": 0, "msg": "", "data": []}
    count = scences.count()
    dict['count'] = count

    #   写入：
    for row in scences:
        row_dict = {}
        row_dict['line_id'] = row.line_id
        row_dict['people_name'] = row.people_name
        row_dict['people_id_card'] = row.people_id_card
        row_dict['time'] = row.time
        row_dict['line_info'] = row.line_info
        dict['data'].append(row_dict)

    # print(dict)
    return JsonResponse(data={'result': dict})


def del_people_info(request):
    will_delete_id = request.GET.get('line_id')

    t = positive_info.objects.get(line_id=will_delete_id)
    t.delete()

    tt = positive_line.objects.get(line_id=will_delete_id)
    tt.delete()

    return JsonResponse(data={'result': 'success'})


def from_positive_line_get_line(request):
    line_id_list = request.GET.getlist('index_list')
    count = len(line_id_list)

    all_dict = {"all_data": [], 'count': count}

    for lind_id in line_id_list:
        scences = positive_line.objects.filter(line_id=lind_id)
        count = scences.count()
        dict = {"line_id": lind_id, "msg": "", "data": []}

        #   写入：
        for row in scences:
            row_dict = {}
            row_dict['locate_x_float'] = row.locate_x_float
            row_dict['locate_y_float'] = row.locate_y_float

            dict['data'].append(row_dict)

        # print(dict)
        all_dict['all_data'].append(dict)

    return JsonResponse(data={'result': all_dict})


def add_check_point(request):
    check_point.objects.create(point_id=request.GET.get('point_id'),
                               point_name=request.GET.get('point_name'),
                               poind_address=request.GET.get('poind_address'),
                               locate_x_float=request.GET.get('locate_x_float'),
                               locate_y_float=request.GET.get('locate_y_float'))

    return JsonResponse(data={'result': 'success'})


def del_check_point(request):
    will_delete_id = request.GET.get('point_id')

    t = check_point.objects.get(point_id=will_delete_id)
    t.delete()

    return JsonResponse(data={'result': 'success'})


def explore_all_check_point(request):
    scences = check_point.objects.all()
    dict = {"code": 0, "msg": "", "data": []}
    count = scences.count()
    dict['count'] = count

    #   写入：
    for row in scences:
        row_dict = {}
        row_dict['point_id'] = row.point_id
        row_dict['point_name'] = row.point_name
        row_dict['poind_address'] = row.poind_address
        row_dict['locate_x_float'] = row.locate_x_float
        row_dict['locate_y_float'] = row.locate_y_float
        dict['data'].append(row_dict)

    # print(dict)
    return JsonResponse(data={'result': dict})


def sevelal_day_without_check(request):
    day = request.GET.get('day')
    scences = gis_table.objects.filter(checkdate__lt=day)
    dict = {"code": 0, "msg": "", "data": []}
    count = scences.count()
    dict['count'] = count

    #   写入：
    for row in scences:
        row_dict = {}
        row_dict['locate_x_float'] = row.lat
        row_dict['locate_y_float'] = row.lon
        dict['data'].append(row_dict)

    # print(dict)
    return JsonResponse(data={'result': dict})


def edit_test_place(request):
    change_id = request.GET.get('id')
    change_type = request.GET.get('type')
    change_value = request.GET.get('value')
    if change_type == "t_name":
        t = check_point.objects.get(point_id=change_id)
        t.point_name = change_value
        t.save()

    elif change_type == "t_address":
        t = check_point.objects.get(point_id=change_id)
        t.point_address = change_value
        t.save()

    elif change_type == "x":
        t = check_point.objects.get(point_id=change_id)
        t.locate_x_float = change_value
        t.save()

    elif change_type == "y":
        t = check_point.objects.get(point_id=change_id)
        t.locate_y_float = change_value
        t.save()

    return JsonResponse(data={'result': 'success'})
