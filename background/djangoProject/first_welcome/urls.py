from django.urls import path
from . import views

urlpatterns = [
    path('welcome.html/', views.welcome, name='welcome'),
    path('index.html/', views.index, name='index'),
    # path('subprocess_output.html/', views.subprocess_output, name='subprocess_output'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register.html/', views.register, name='register'),

    path('baidu_webGIS_try.html/', views.baidu_webGIS_try, name='baidumap1'),
    path('webGIS_1.html/', views.webGIS_1, name='webGIS_1'),

    path('show',views.db_to_web,name='db_to_web'),

    path('post_type_value/',views.explore_form_db,name='post_type_value'),  #查

    path('all_post_type_value/', views.all_explore_form_db, name='all_post_type_value'),  # 查

    path('cell_ajax_post.html/',views.cell_ajax_post,name='cell_ajax_post'),

    path('add_to_db/',views.add_to_db,name='add_to_db'),
    path('change_from_db/',views.change_from_db,name='change_from_db'),
    path('delete_from_db/',views.deleta_from_db,name='delete_from_db'),

    path('all_area_form_db/',views.all_area_form_db,name="all_area_form_db"),

    path('api_stay_points_return/',views.api_stay_points_return,name="api_stay_points_return"),
]

# python manage.py runserver