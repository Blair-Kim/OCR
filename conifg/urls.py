"""conifg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from . import views
import board.views

app_name = 'board'
urlpatterns = [
    #이메일 보내기 페이지에서 이메일 보냈을 때
    path('send_email/', board.views.send_email, name='send_email'),
    #이메일 보내기 페이지
    path('email/<int:pk>', board.views.send_email, name='board_email'),
    #보낸 메일함 페이지
    path('mail_log/', board.views.log_mail, name='board_mail_log'),
    #관리자페이지 연결
    path('admin/', admin.site.urls),
    # 메인페이지 연결(로그인 페이지)
    path('', board.views.main, name='main'),
    # 게시판으로 연결
    path('board/', board.views.index, name='board_main'),
    # 사용자 추가 페이지로 연결
    path('write/', board.views.write, name='board_write'),
    # 사용자 추가 페이지에서 저장 눌렀을 때,
    path('write/save', board.views.write_board, name='write_board'),
    # 사용자 수정 페이지로 연결
    path('edit/<int:pk>', board.views.edit, name='board_edit'),
    # 사용자 수정 페이지에서 수정 눌렀을 때,
    path('edit/save/<int:pk>', board.views.edit, name='board_edit_save'),
    # 사용자 삭제
    path('delete/<int:pk>', board.views.delete, name='board_delete')

    # path('<int:board_id>/', board.views.detail, name='detail'),

    # path('write/', board.views.write, name='write'),

    

    # path('<int:board_id>/create_reply', board.views.create_reply, name='create_reply'),

]
