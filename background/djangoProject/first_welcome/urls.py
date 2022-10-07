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

    path('show', views.db_to_web, name='db_to_web'),

    path('all_post_type_value/', views.all_explore_form_db, name='all_post_type_value'),  # 查

    path('cell_ajax_post.html/', views.cell_ajax_post, name='cell_ajax_post'),

    path('add_to_db/', views.add_to_db, name='add_to_db'),
    path('change_from_db/', views.change_from_db, name='change_from_db'),
    path('delete_from_db/', views.deleta_from_db, name='delete_from_db'),

    path('all_area_form_db/', views.all_area_form_db, name="all_area_form_db"),

    path('api_stay_points_return/', views.api_stay_points_return, name="api_stay_points_return"),
    path('api_add_line/', views.api_add_line, name="api_add_line"),
    path('api_get_positive_info/', views.api_get_positive_info, name="api_get_positive_info"),
    path('del_people_info/', views.del_people_info, name="del_people_info"),
    path('from_positive_line_get_line/', views.from_positive_line_get_line, name="from_positive_line_get_line"),

    path('add_check_point/', views.add_check_point, name="add_check_point"),
    path('del_check_point/', views.del_check_point, name="del_check_point"),
    path('explore_all_check_point/', views.explore_all_check_point, name="explore_all_check_point"),

    path('sevelal_day_without_check/', views.sevelal_day_without_check, name="sevelal_day_without_check"),
    path('edit_test_place/', views.edit_test_place, name="edit_test_place")

]

# python manage.py runserver
