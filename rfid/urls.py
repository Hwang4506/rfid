from django.urls import path

from . import views

app_name = 'rfid'

urlpatterns = [
    path('mw/', views.index, name='index'),
    path('pl/', views.proline, name='proline'),
    path('fpw/', views.fpware, name='fpware'),
    path('rest/', views.material_list),
    path('rest2/', views.production_list),
    path('rest3/', views.finished_list),
    path('rule/', views.rule),
    path('visual/', views.visual),
    path('direction/', views.direction, name='dir'),
    path('rest4/', views.direction_list),
    path('main/', views.main, name='main'),
    path('rule1/', views.rule1, name='rule1'),
    path('rule2/', views.rule2, name='rule2'),
    path('rule3/', views.rule3, name='rule3'),
    path('rule4/', views.rule4, name='rule4'),
    path('pl/<int:production_id>/', views.edit_pl, name='pl_edit'),
    path('pl/<int:production_id>/modify/', views.pl_modify, name='pl_mdf'),
    path('pl/<int:production_id>/delete/', views.pl_delete, name='pl_del'),
    path('mw/<int:material_id>/', views.edit_mt, name='mt_edit'),
    path('mw/<int:material_id>/modify/', views.mt_modify, name='mt_mdf'),
    path('mw/<int:material_id>/delete/', views.mt_delete, name='mt_del'),
    path('fpw/<int:finished_id>/', views.edit_fp, name='fp_edit'),
    path('fpw/<int:finished_id>/modify/', views.fp_modify, name='fp_mdf'),
    path('fpw/<int:finished_id>/delete/', views.fp_delete, name='fp_del'),
    path('dir/<int:direction_id>/', views.edit_dir, name='dir_edit'),
    path('dir/<int:direction_id>/modify/', views.dir_modify, name='dir_mdf'),
    path('dir/<int:direction_id>/delete/', views.dir_delete, name='dir_del'),
]