from django.utils import timezone
# 장고 html 관련 프레임워크
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# 장고 메시지 프레임워크
from django.contrib import messages

# 장고 models 
from .models import user_master
from .models import email_setting
from .models import email_log

#이메일 보내기
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# # ------------------------------------send email 전체 설정------------------------------------
# 모르겠네 슈발...........
# from board.models import user_master

# # user_activate가 1인 데이터만 가져오기
# # 현재 임의로 관리자 계정의 active_users를 1로 설정한 상태
# active_users = user_master.objects.filter(user_activate='1')

# # 이메일 백엔드 설정
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587

# # 이메일 호스트 설정 (로그인한 유저 정보를 바탕으로 이메일 주소 설정)
# if active_users.exists():
#     first_user = active_users.first()
#     EMAIL_HOST = 'smtp.naver.com'  # 사용자의 이메일 호스트로 설정 (예: smtp.example.com)
#     EMAIL_HOST_USER = first_user.user_email
#     EMAIL_HOST_PASSWORD = first_user.user_pw  # 사용자의 이메일 비밀번호로 설정
#     print('good')
# else:
#     # user_activate가 1인 사용자가 없을 경우 기본 호스트 정보 설정
#     EMAIL_HOST = 'smtp.naver.com'
#     EMAIL_HOST_USER = 'bfalcom@naver.com'
#     EMAIL_HOST_PASSWORD = 'kj477552!'

# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# # ------------------------------------send email 전체 설정------------------------------------

#이메일 보내는 함수
def send_email(request):
    #현재는 context 쓸모 없음. 하지만 나중엔 context 에 보내는 유저의 정보를 띄울 예정
    context = {'title':'send_email'}


    if request.method == 'POST':
        subject = request.POST['subject']	# 제목
        to = [request.POST['to']]			# 수신할 이메일 주소
        from_email = "bfalcom@naver.com"	# 발신할 이메일 주소
        body = request.POST['body']	        # 본문 내용
        bcc_str = request.POST['cc']        # 참조를 콤마로 구분한 문자열

        # 콤마로 나눈 문자열을 리스트로 변환 - 장고에서 사용하는 EmailMessage 클래스의 bcc 리턴 값은 무조건 배열 또는 튜플 형태여야 한다고 함...(오류메세지)
        bcc = [email.strip() for email in bcc_str.split(',')]
        
        # E-mail 전송
        EmailMessage(subject=subject, body=body, to=to, from_email=from_email, bcc=bcc).send()
        # 로그 남기기
        log = email_log(mail_title = subject, mail_to = to, mail_from = from_email, mail_body = body, mail_bcc = bcc)
        log.save()
        return HttpResponseRedirect(reverse('board_main'))
        
    else :
        return render(request, "send_email.html")
    
#보낸 메일함
def log_mail(request):
    mail_list = email_log.objects.all().order_by('mail_datetime') # 모든 메일 로그 조회
    context = {'보낸메일':mail_list,'title':'보낸 메일함'}
    return render(request, 'mail_log.html', context)

# 로그인 메인
def main(request) :
        return render(request, "login_main.html")

#게시판 메인(유저정보)
def index(request):
    user_list = user_master.objects.all().order_by('id_seq') # 모든 데이터 조회, 내림차순(-표시) 조회
    context = {'사용자목록':user_list,'title':'사용자목록'}

    return render(request, 'index.html', context)

#사용자 추가 페이지 
def write(request):
    context = {'title':'회원 가입'}
    return render(request, 'write.html', context)

#사용자 추가 함수
def write_board(request):
    b = user_master(user_id=request.POST['user_id'], user_pw=request.POST['user_pw'], user_name=request.POST['user_name'], user_email=request.POST['user_email'])
    b.save()
    return HttpResponseRedirect(reverse('board_main'))

def edit(request,pk):
    b = user_master.objects.get(id_seq=pk)
    if request.method == "POST":
        b.user_id = request.POST['user_id']
        b.user_pw = request.POST['user_pw']
        b.user_name = request.POST['user_name']
        b.user_email = request.POST['user_email']

        b.save()

        return HttpResponseRedirect(reverse('board_main'))

    else:
        context = {'user_info':b, 'title':'사용자수정'}
        return render(request, 'edit.html', context)
    
#사용자 삭제 함수
def delete(request, pk):
    b = user_master.objects.get(id_seq=pk)
    b.delete()
    return HttpResponseRedirect(reverse('board_main'))

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
                
