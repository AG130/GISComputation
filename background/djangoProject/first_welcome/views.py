from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
from subprocess import *
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from .models import *
from django.contrib.auth.hashers import make_password

import json

# Create your views here.
# python manage.py runserver


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username):  # 用户名已存在
            error_message = "用户名已存在"
            return render(request, "register.html", {"error_message": error_message})
        elif password != password2:  # 两次密码不一致
            error_message = "两次密码不一致，请重新输入"
            return render(request, "register.html", {"error_message": error_message})
        else:  # 可以注册
            User.objects.create(username=username, password=make_password(password))  # 增
            request.session['username'] = username  # 添加session
            return render(request, "register.html", {"success": True})
    else:
        return render(request, "register.html")

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
    if request.method == "GET":
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

    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            print("login")
            return render(request, "welcome.html", {"username": request.POST.get("username")})
        else:
            return render(request, "index.html", {"error_message": "用户名或密码错误！"})
    else:
        return render(request, "index.html")


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
    backx=gis_table.objects.all()
    print(backx)
    backget=gis_table.objects.get(name="路人甲")
    print(backget)
    print(type(backget))
    print(backget.name)
    print(backget.sex)
    print(backget.locate_x)
    print(backget.locate_x_float)
    return render(request, "baidu_webGIS_try.html")

# @csrf_exempt
@require_GET
def explore_form_db(request):  #查
    explore_type=request.GET.get('type')
    explore_value=request.GET.get('value')
    # {'type':   ,'value':   }
    print(explore_type)
    print(explore_value)
    #判断查询类型
    if(explore_type=="id"):
        scences=gis_table.objects.filter(id=explore_value)
    elif(explore_type=="name"):
        scences=gis_table.objects.filter(name=explore_value)
    elif(explore_type=="sex"):
        scences=gis_table.objects.filter(sex=explore_value)
    elif(explore_type=="id_card"):
        scences=gis_table.objects.filter(id_card=explore_value)
    elif(explore_type=="checkdate"):
        scences=gis_table.objects.filter(checkdate=explore_value)
    elif(explore_type=="result"):
        scences=gis_table.objects.filter(result=explore_value)
    elif(explore_type=="resbonsibilityman"):
        scences=gis_table.objects.filter(responsibilityman=explore_value)
    elif(explore_type=="rect_explore"):
        # explore_value[0]为左上点
        # explore_value[0]为又下点
        scences=gis_table.objects.filter(locate_x_float__gt=explore_value[0][0],
                                         locate_x_float__lt=explore_value[1][0],
                                         locate_y_float__gt=explore_value[1][1],
                                         locate_y_float__lt=explore_value[0][1])

    dict ={"code":0,"msg":"","data":[]}
    count=scences.count()
    dict['count']=count

#   写入：
    for row in scences:
        row_dict={}
        row_dict['id']=row.id
        row_dict['name']=row.name
        row_dict['sex']=row.sex
        row_dict['id_card']=row.id_card
        row_dict['checkdata']=row.checkdate
        row_dict['result']=row.result
        row_dict['responsibilityman']=row.responsibilityman
        row_dict['lon']=row.locate_x_float
        row_dict['lat']=row.locate_y_float
        row_dict['phone']=row.phone
        row_dict['address']=row.address

        dict['data'].append(row_dict)


    print(dict)
    return JsonResponse(data={'result':dict})

@require_GET
def all_explore_form_db(request):  #查
    scences=gis_table.objects.all()
    dict ={"code":0,"msg":"","data":[]}
    count=scences.count()
    dict['count']=count

#   写入：
    for row in scences:
        row_dict={}
        row_dict['id']=row.id
        row_dict['name']=row.name
        row_dict['sex']=row.sex
        row_dict['id_card']=row.id_card
        row_dict['checkdata']=row.checkdate
        row_dict['result']=row.result
        row_dict['responsibilityman']=row.responsibilityman
        row_dict['lon']=row.locate_x_float
        row_dict['lat']=row.locate_y_float
        row_dict['phone']=row.phone
        row_dict['address']=row.address
        dict['data'].append(row_dict)



    print(dict)
    return JsonResponse(data={'result':dict})

@require_GET
def add_to_db(request):  #增
    will_add_value_str=request.GET
    print('will_add_value_str:')
    print(will_add_value_str['value[0][name]'])
    # 'data': [{'id': 1, 'name': '路人甲', 'sex': '男',
    # 'id_card': '140098098', 'checkdata': '20191989',
    # 'result': '阳性', 'responsibilityman': '负责人1',
    # 'lon': 100.111, 'lat': 79.999}]
    # 增加类型

    # 需要添加address、phone
    example_dict={'name': '路人add_try', 'sex': '男',
     'id_card': '12398098', 'checkdata': '2012289',
      'result': '阳性', 'responsibilityman': '负责人cs',
      'lon': 100.111, 'lat': 79.999}
    value_dict=will_add_value_str
    gis_table.objects.create(name=value_dict['value[0][name]'],sex=value_dict['value[0][sex]'],
                             id_card=value_dict['value[0][id_card]'],checkdate=value_dict['value[0][checkdata]'],
                             result=value_dict['value[0][result]'],responsibilityman=value_dict['value[0][responsibilityman]'],
                             locate_x=str(value_dict['value[0][lon]']),locate_y=str(value_dict['value[0][lat]']),
                             locate_x_float=value_dict['value[0][lon]'],locate_y_float=value_dict['value[0][lat]'],
                             address=value_dict['value[0][address]'],phone=value_dict['value[0][phone]'])
    print(value_dict)
    return JsonResponse(data={'result':'success'})


def deleta_from_db(request):   #删
    will_delete_id=request.GET.get('value')

    t=gis_table.objects.get(id_card=will_delete_id)
    t.delete()
    return JsonResponse(data={'result':'success'})


def change_from_db(request):  #改
    change_id=request.GET.get('id')
    change_type=request.GET.get('type')
    change_value=request.GET.get('value')
    # {'type':   ,'value':   }
    #判断查询类型
    if(change_type=="name"):
        t=gis_table.objects.get(id=change_id)
        t.name=change_value
        t.save()

    elif(change_type=="sex"):
        t=gis_table.objects.get(id=change_id)
        t.sex=change_value
        t.save()

    elif(change_type=="id_card"):
        t=gis_table.objects.get(id=change_id)
        t.id_card=change_value
        t.save()

    elif(change_type=="checkdate"):
        t=gis_table.objects.get(id=change_id)
        t.checkdate=change_value
        t.save()

    elif(change_type=="result"):
        t=gis_table.objects.get(id=change_id)
        t.result=change_value
        t.save()

    elif(change_type=="resbonsibilityman"):
        t=gis_table.objects.get(id=change_id)
        t.resbonsibilityman=change_value
        t.save()

    elif(change_type=="rect_explore"):
        t=gis_table.objects.get(id=change_id)
        t.locate_x_float=change_value[0]
        t.locate_y_float=change_value[1]
        t.locate_x=str(change_value[0])
        t.locate_y=str(change_value[1])
        t.save()

    elif(change_type=="lon"):
        t=gis_table.objects.get(id=change_id)
        t.locate_x=change_value
        t.locate_x_float=float(change_value)
        t.save()

    elif(change_type=="lat"):
        t=gis_table.objects.get(id=change_id)
        t.locate_y=change_value
        t.locate_y_float=float(change_value)

        t.save()

    elif(change_type=="phone"):
        t=gis_table.objects.get(id=change_id)
        t.phone=change_value
        t.save()

    elif(change_type=="address"):
        t=gis_table.objects.get(id=change_id)
        t.address=change_value
        t.save()


    return JsonResponse(data={'result':'success'})



def cell_ajax_post(request):
    return render(request, "cell_ajax_post.html")

@require_GET
def all_area_form_db(request):  #查区域路径
    scences=positive_line_area.objects.all()
    dict ={"code":0,"msg":"","data":[]}
    count=scences.count()
    dict['count']=count

#   写入：
    for row in scences:
        row_dict={}
        row_dict['lng']=row.center_lng
        row_dict['lat']=row.center_lat
        row_dict['radius']=row.center_radius
        row_dict['line']=[]

        all_points_str=row.line_points.split('T')

        one_line_points={"points":[]}

        for i in range(len(all_points_str)):
            one_point_xy=all_points_str[i].split("E")
            one_xy={}
            one_xy['lng']=float(one_point_xy[0])
            one_xy['lat']=float(one_point_xy[1])

            one_line_points['points'].append(one_xy)
            row_dict['line'].append(one_line_points)

        dict['data'].append(row_dict)



    print(dict)
    return JsonResponse(data={'result':dict})

@require_GET
def api_stay_points_return(request):  #停驻点api
    stay_points_id=request.GET.get('id')
    dist_threh=request.GET.get('dist_th')
    time_threh=request.GET.get('time_th')
    command="python /Users/wsy/GIS/djangoProject/stay_points_explore/api_id_out_points.py "\
            +str(stay_points_id)+' '+str(dist_threh)+' '+str(time_threh)
    r=os.popen(command)
    info = r.readlines()  # 读取命令行的输出到一个list
    print(len(info))

    dict ={"code":0,"msg":"","data":[]}
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

    print(dict)


    return JsonResponse(data={'result':dict})


