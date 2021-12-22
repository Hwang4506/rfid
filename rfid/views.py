from .models import Material_Warehouse, Production_Line, Finished_Product_Warehouse, Direction, \
    Material_Warehouse_out, Production_Line_out, Finished_Product_Warehouse_out
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
import pusher
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rfid.serializers import MaterialSerializer, ProductionSerializer, FinishedSerializer, \
    DirectionSerializer, MaterialoutSerializer, ProductionoutSerializer, FinishedoutSerializer
from django.contrib import messages
from .forms import ProductionForm, MaterialForm, FinishedForm, DirectionForm, MaterialoutForm, \
    ProductionoutForm, FinishedoutoutForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

def index(request):
    """
    Material_Warehouse 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'rcrecent')  # 정렬기준
    page2 = request.GET.get('page2', '1')  # 페이지
    kw2 = request.GET.get('kw2', '')  # 검색어
    so2 = request.GET.get('so2', 'rlrecent')  # 정렬기준
    # 정렬
    if so == 'many':
        material_list = Material_Warehouse.objects.order_by('-Quantity_mw', '-Receiving_Date_mw')
    elif so == 'loc1':
        material_list = Material_Warehouse.objects.order_by('-Location_mw1', '-Receiving_Date_mw')
    else:  # rcrecent
        material_list = Material_Warehouse.objects.order_by('-Receiving_Date_mw')
    if so2 == 'many2':
        material_list2 = Material_Warehouse_out.objects.order_by('-Quantity_mwout', '-Release_Date_mw')
    elif so2 == 'loc':
        material_list2 = Material_Warehouse_out.objects.order_by('-Location_mw', '-Release_Date_mw')
    else:  # rlrecent
        material_list2 = Material_Warehouse_out.objects.order_by('-Release_Date_mw')
    # 검색
    if kw:
        material_list = material_list.filter(
            Q(Receiving_Date_mw__icontains=kw) |  # 입고날짜 검색
            Q(RFID_Number_mw__icontains=kw) |  # RFID넘버 검색
            Q(Quantity_mw__icontains=kw) |  # 수량 검색
            Q(Location_mw1__icontains=kw)  # 방향 검색
        ).distinct()

    if kw2:
        material_list2 = material_list2.filter(
            Q(Release_Date_mw__icontains=kw2) |  # 출고날짜 검색
            Q(RFID_Number_mwout__icontains=kw2) |  # RFID넘버 검색
            Q(Quantity_mwout__icontains=kw2)  |  # 수량 검색
            Q(Location_mw__icontains=kw2)  # 방향 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(material_list, 10)
    paginator2 = Paginator(material_list2, 10)# 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    page_obj2 = paginator2.get_page(page2)
    context = {'material_list': page_obj, 'page': page, 'kw': kw, 'so': so,
               'material_list2': page_obj2, 'page2': page2, 'kw2': kw2, 'so2': so2}
    return render(request, 'rfid/material_list.html', context)

def proline(request):
    """
        Production_Line 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    page2 = request.GET.get('page2', '1')  # 페이지
    kw2 = request.GET.get('kw2', '')  # 검색어
    so2 = request.GET.get('so2', 'rlrecent')  # 정렬기준
    # 정렬
    if so == 'many':
        production_list = Production_Line.objects.order_by('-Quantity_pl', '-Inline_Date')
    elif so == 'loc1':
        production_list = Production_Line.objects.order_by('-Location_pl1', '-Inline_Date')
    else:  # inrecent
        production_list = Production_Line.objects.order_by('-Inline_Date')
    if so2 == 'many2':
        production_list2 = Production_Line_out.objects.order_by('-Quantity_plout', '-Outline_Date')
    elif so2 == 'loc':
        production_list2 = Production_Line_out.objects.order_by('-Location_pl', '-Outline_Date')
    else:  # olrecent
        production_list2 = Production_Line_out.objects.order_by('-Outline_Date')
    # 검색
    if kw:
        production_list = production_list.filter(
            Q(Inline_Date__icontains=kw) |  # 인라인날짜 검색
            Q(RFID_Number_pl__icontains=kw) |  # RFID넘버 검색
            Q(Quantity_pl__icontains=kw) |  # 수량 검색
            Q(Location_pl1__icontains=kw)  # 방향 검색
        ).distinct()

    if kw2:
        production_list2 = production_list2.filter(
            Q(Outline_Date__icontains=kw2) |  # 출고날짜 검색
            Q(RFID_Number_plout__icontains=kw2) |  # RFID넘버 검색
            Q(Quantity_plout__icontains=kw2)  |  # 수량 검색
            Q(Location_pl__icontains=kw2)  # 방향 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(production_list, 10)  # 페이지당 10개씩 보여주기
    paginator2 = Paginator(production_list2, 10)# 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    page_obj2 = paginator2.get_page(page2)
    context = {'production_list': page_obj, 'page': page, 'kw': kw, 'so': so,
               'production_list2': page_obj2, 'page2': page2, 'kw2': kw2, 'so2': so2}
    return render(request, 'rfid/pl_list.html', context)

def fpware(request):
    """
    Finished_Product_Warehouse 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    page2 = request.GET.get('page2', '1')  # 페이지
    kw2 = request.GET.get('kw2', '')  # 검색어
    so2 = request.GET.get('so2', 'rlrecent')  # 정렬기준
    # 정렬
    if so == 'fmany':
        finished_list = Finished_Product_Warehouse.objects.order_by('-Quantity_fw', '-Receiving_Date_fw')
    elif so == 'floc1':
        finished_list = Finished_Product_Warehouse.objects.order_by('-Location_fw1', '-Receiving_Date_fw')
    else:  # frcrecent
        finished_list = Finished_Product_Warehouse.objects.order_by('-Receiving_Date_fw')
    if so2 == 'fmany2':
        finished_list2 = Finished_Product_Warehouse_out.objects.order_by('-Quantity_fwout', '-Release_Date_fw')
    elif so2 == 'floc':
        finished_list2 = Finished_Product_Warehouse_out.objects.order_by('-Location_fw', '-Release_Date_fw')
    else:  # frlrecent
        finished_list2 = Finished_Product_Warehouse_out.objects.order_by('-Release_Date_fw')
    # 검색
    if kw:
        finished_list = finished_list.filter(
            Q(Receiving_Date_fw__icontains=kw) |  # 입고날짜 검색
            Q(RFID_Number_fw__icontains=kw) |  # RFID넘버 검색
            Q(Quantity_fw__icontains=kw) |  # 수량 검색
            Q(Location_fw1__icontains=kw)  # 방향 검색
        ).distinct()

    if kw2:
        finished_list2 = finished_list2.filter(
            Q(Release_Date_fw__icontains=kw2) |  # 출고날짜 검색
            Q(RFID_Number_fwout__icontains=kw2) |  # RFID넘버 검색
            Q(Quantity_fwout__icontains=kw2) |  # 수량 검색
            Q(Location_fw__icontains=kw2)  # 방향 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(finished_list, 10)  # 페이지당 10개씩 보여주기
    paginator2 = Paginator(finished_list2, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    page_obj2 = paginator2.get_page(page2)
    context = {'finished_list': page_obj, 'page': page, 'kw': kw, 'so': so,
               'finished_list2': page_obj2, 'page2': page2, 'kw2': kw2, 'so2': so2}
    return render(request, 'rfid/finished_list.html', context)

def direction(request):
    """
        Direction 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    # 정렬
    if so == 'dir':
        direction_list = Direction.objects.order_by('-Direction')
    else:  # date
        direction_list = Direction.objects.order_by('-Work_Date')
    # 검색
    if kw:
        direction_list = direction_list.filter(
            Q(Work_Date__icontains=kw) |  # 작업날짜 검색
            Q(RFID_Number_dr__icontains=kw) |  # RFID넘버 검색
            Q(Gate_ID__icontains=kw) |  # 게이트ID 검색
            Q(Direction__icontains=kw)  # 방향성 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(direction_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'direction_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'rfid/direction.html', context)

@csrf_exempt
def test(request):
    if request.method == 'GET':
        text = "OK"
        return JsonResponse(text, safe=False)

@csrf_exempt
def material_list(request):
    if request.method == 'GET':
        query_set = Material_Warehouse.objects.all()
        serializer = MaterialSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPush(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def production_list(request):
    if request.method == 'GET':
        query_set = Production_Line.objects.all()
        serializer = ProductionSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushp(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class production_listcl(generics.ListCreateAPIView):
    queryset = Production_Line.objects.all()
    serializer_class = ProductionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'RFID_Number_pl', 'Quantity_pl', 'Location_pl1')

# class production_listcl(APIView):
#     def get(self, request, format=None):
#         queryset = Production_Line.objects.all()
#         serializer = ProductionSerializer(queryset, many=True)
#
#         return Response(serializer.data)
    # def post(self, request, format=None):
    #     serializer = ProductionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def finished_list(request):
    if request.method == 'GET':
        query_set = Finished_Product_Warehouse.objects.all()
        serializer = FinishedSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FinishedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushf(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def direction_list(request):
    if request.method == 'GET':
        query_set = Direction.objects.all()
        serializer = DirectionSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DirectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushd(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def sendPush(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event', data)

def sendPushp(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event2', data)

def sendPushf(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event3', data)

def sendPushd(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event4', data)

def rule(request):
    """
        룰 기반의 스마트 팩토리 상황정보 표현
    """
    return render(request, 'rfid/rule.html')

def visual(request):
    """
        스마트 팩토리 정보 시각화
    """
    return render(request, 'rfid/visual.html')

def main(request):
    return render(request, 'rfid/main.html')

def rule1(request):
    return render(request, 'rfid/rule1.html')

def rule2(request):
    return render(request, 'rfid/rule2.html')

def rule3(request):
    return render(request, 'rfid/rule3.html')

def rule4(request):
    return render(request, 'rfid/rule4.html')

def edit_pl(request, production_id):
    """
       production line 편집 화면 출력
       """
    production = Production_Line.objects.get(id=production_id)
    context = {'production': production}
    return render(request, 'rfid/pl_edit.html', context)

def pl_modify(request, production_id):
    """
        production line 내용수정
        """
    production = get_object_or_404(Production_Line, pk=production_id)

    if request.method == "POST":
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            production = form.save(commit=False)
            production.save()
            return redirect('rfid:pl_edit', production_id=production.id)
    else:
        form = ProductionForm(instance=production)
    context = {'form': form}
    return render(request, 'rfid/production_form.html', context)

def pl_delete(request, production_id):
    """
       production line 내용삭제
       """
    production = get_object_or_404(Production_Line, pk=production_id)
    production.delete()
    return redirect('rfid:proline')

def edit_mt(request, material_id):
    """
       material warehouse 편집 화면 출력
       """
    material = Material_Warehouse.objects.get(id=material_id)
    context = {'material': material}
    return render(request, 'rfid/mt_edit.html', context)

def mt_modify(request, material_id):
    """
        material warehouse 내용수정
        """
    material = get_object_or_404(Material_Warehouse, pk=material_id)

    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.save()
            return redirect('rfid:mt_edit', material_id=material.id)
    else:
        form = MaterialForm(instance=material)
    context = {'form': form}
    return render(request, 'rfid/material_form.html', context)

def mt_delete(request, material_id):
    """
       material warehouse 내용삭제
       """
    material = get_object_or_404(Material_Warehouse, pk=material_id)
    material.delete()
    return redirect('rfid:index')

def edit_fp(request, finished_id):
    """
       Finished_Product_Warehouse 편집 화면 출력
       """
    finished = Finished_Product_Warehouse.objects.get(id=finished_id)
    context = {'finished': finished}
    return render(request, 'rfid/fp_edit.html', context)

def fp_modify(request, finished_id):
    """
        Finished_Product_Warehouse 내용수정
        """
    finished = get_object_or_404(Finished_Product_Warehouse, pk=finished_id)

    if request.method == "POST":
        form = FinishedForm(request.POST, instance=finished)
        if form.is_valid():
            finished = form.save(commit=False)
            finished.save()
            return redirect('rfid:fp_edit', finished_id=finished.id)
    else:
        form = FinishedForm(instance=finished)
    context = {'form': form}
    return render(request, 'rfid/finished_form.html', context)

def fp_delete(request, finished_id):
    """
       Finished_Product_Warehouse 내용삭제
       """
    finished = get_object_or_404(Finished_Product_Warehouse, pk=finished_id)
    finished.delete()
    return redirect('rfid:fpware')

def edit_dir(request, direction_id):
    """
       Direction 편집 화면 출력
       """
    direction = Direction.objects.get(id=direction_id)
    context = {'direction': direction}
    return render(request, 'rfid/dir_edit.html', context)

def dir_modify(request, direction_id):
    """
        Direction 내용수정
        """
    direction = get_object_or_404(Direction, pk=direction_id)

    if request.method == "POST":
        form = DirectionForm(request.POST, instance=direction)
        if form.is_valid():
            direction = form.save(commit=False)
            direction.save()
            return redirect('rfid:dir_edit', direction_id=direction.id)
    else:
        form = DirectionForm(instance=direction)
    context = {'form': form}
    return render(request, 'rfid/direction_form.html', context)

def dir_delete(request, direction_id):
    """
       Direction 내용삭제
       """
    direction = get_object_or_404(Direction, pk=direction_id)
    direction.delete()
    return redirect('rfid:dir')

def edit_mtout(request, material2_id):
    """
       material warehouse out 편집 화면 출력
       """
    material2 = Material_Warehouse_out.objects.get(id=material2_id)
    context = {'material2': material2}
    return render(request, 'rfid/mtout_edit.html', context)

def mtout_modify(request, material2_id):
    """
        material warehouse out 내용수정
        """
    material2 = get_object_or_404(Material_Warehouse_out, pk=material2_id)

    if request.method == "POST":
        form = MaterialoutForm(request.POST, instance=material2)
        if form.is_valid():
            material2 = form.save(commit=False)
            material2.save()
            return redirect('rfid:mt_edit2', material2_id=material2.id)
    else:
        form = MaterialoutForm(instance=material2)
    context = {'form': form}
    return render(request, 'rfid/materialout_form.html', context)

def mtout_delete(request, material2_id):
    """
       material warehouse 내용삭제
       """
    material2 = get_object_or_404(Material_Warehouse_out, pk=material2_id)
    material2.delete()
    return redirect('rfid:index')

@csrf_exempt
def materialout_list(request):
    if request.method == 'GET':
        query_set = Material_Warehouse_out.objects.all()
        serializer = MaterialoutSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushout(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def sendPushout(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event5', data)

def edit_plout(request, production2_id):
    """
       production warehouse out 편집 화면 출력
       """
    production2 = Production_Line_out.objects.get(id=production2_id)
    context = {'production2': production2}
    return render(request, 'rfid/plout_edit.html', context)

def plout_modify(request, production2_id):
    """
        production warehouse out 내용수정
        """
    production2 = get_object_or_404(Production_Line_out, pk=production2_id)

    if request.method == "POST":
        form = ProductionoutForm(request.POST, instance=production2)
        if form.is_valid():
            production2 = form.save(commit=False)
            production2.save()
            return redirect('rfid:pl_edit2', production2_id=production2.id)
    else:
        form = ProductionoutForm(instance=production2)
    context = {'form': form}
    return render(request, 'rfid/productionout_form.html', context)

def plout_delete(request, production2_id):
    """
       Production Line 내용삭제
       """
    production2 = get_object_or_404(Production_Line_out, pk=production2_id)
    production2.delete()
    return redirect('rfid:proline')

@csrf_exempt
def productionout_list(request):
    if request.method == 'GET':
        query_set = Production_Line_out.objects.all()
        serializer = ProductionoutSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductionoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushout2(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def sendPushout2(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event6', data)

def edit_fwout(request, finished2_id):
    """
       finished warehouse out 편집 화면 출력
       """
    finished2 = Finished_Product_Warehouse_out.objects.get(id=finished2_id)
    context = {'finished2': finished2}
    return render(request, 'rfid/fwout_edit.html', context)

def fwout_modify(request, finished2_id):
    """
        finished warehouse out 내용수정
        """
    finished2 = get_object_or_404(Finished_Product_Warehouse_out, pk=finished2_id)

    if request.method == "POST":
        form = FinishedoutoutForm(request.POST, instance=finished2)
        if form.is_valid():
            finished2 = form.save(commit=False)
            finished2.save()
            return redirect('rfid:fw_edit2', finished2_id=finished2.id)
    else:
        form = FinishedoutoutForm(instance=finished2)
    context = {'form': form}
    return render(request, 'rfid/finishedout_form.html', context)

def fwout_delete(request, finished2_id):
    """
       Production Line 내용삭제
       """
    finished2 = get_object_or_404(Finished_Product_Warehouse_out, pk=finished2_id)
    finished2.delete()
    return redirect('rfid:fpware')

@csrf_exempt
def finishedout_list(request):
    if request.method == 'GET':
        query_set = Finished_Product_Warehouse_out.objects.all()
        serializer = FinishedoutSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FinishedoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()       # DB저장
            sendPushout3(serializer.data)
            # print("비데이터의 형식 : ", type(serializer.data))
            # print("비데이터 : ", serializer.data)
            # print("아이디 : ", serializer.data["id"])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def sendPushout3(data):
    pusher_client = pusher.Pusher(
        app_id='1187992',
        key='af1394a6d38f4e31ac54',
        secret='92529e0c8378dd72a42f',
        cluster='ap3',
        ssl=True
        )
    pusher_client.trigger('my-channel', 'my-event7', data)