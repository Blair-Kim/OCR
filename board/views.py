from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import user_master
from .models import email_setting

# Create your views here.

def main(request) :
        return render(request, "login_main.html")
        
def index(request):
    user_list = user_master.objects.all().order_by('id_seq') # 모든 데이터 조회, 내림차순(-표시) 조회
    context = {'사용자목록':user_list,'title':'사용자 목록'}
    return render(request, 'index.html', context)

def write(request):
    context = {'title':'사용자 추가'}
    return render(request, 'write.html', context)

def write_board(request):
    b = user_master(user_id=request.POST['user_id'], user_pw=request.POST['user_pw'], user_name=request.POST['user_name'], user_email=request.POST['user_email'])
    b.save()
    return HttpResponseRedirect(reverse('board_main'))

def delete(request):
     

# def detail(request, board_id):
#     board = user_master.objects.get(id=board_id)
#     return render(request, 'board/detail.html', {'board': board})

# def create_reply(request, board_id):
#     b = user_master.objects.get(id = board_id)
#     b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
#     return HttpResponseRedirect(reverse('board:detail', args=(board_id,)))   



# def boardmain(request) :
#         return render(request,"index.html")
        
# def detail(request) :
#         if request.method =='GET':
#                 postForm = postForm()
#                 context = {'postForm' : postForm}
#                 return render(request, 'board/create.html')
#         if request.method =='POST':
                
#                 return redirect(request, '/admin/')
        
# def write(request) :
#         if request.method =='GET':
#                 postForm = postForm()
#                 context = {'postForm' : postForm}
#                 return render(request, 'board/create.html')
#         if request.method =='POST':
                
#                 return redirect(request, '/admin/')
                
