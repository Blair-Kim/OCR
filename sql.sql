show databases;
DROP database blog;

CREATE DATABASE django_pj default CHARACTER SET UTF8;
-- django_pj 데이터베이스 사용하기
use django_pj;
show tables;

CREATE TABLE user_master
(
     id_seq INT AUTO_INCREMENT,
     user_id VARCHAR(32) NOT NULL,
     user_pw varchar(32) NOT NULL,
     user_name VARCHAR(12) DEFAULT '이름을 설정하세요.',
     user_email VARCHAR(30) default 'E-mail을 설정하세요',
     PRIMARY KEY(id_seq)
)ENGINE=INNODB;

-- drop table user_master;
DESCRIBE user_master;
DESCRIBE board_post;

CREATE TABLE email_setting
(
	 mail_seq INT AUTO_INCREMENT,
     mail_sender_host VARCHAR(30) NOT NULL,
     smtp_port VARCHAR(12) NOT NULL,
     sender_user VARCHAR(24) NOT NULL,
     sender_password VARCHAR(30) NOT NULL,
     PRIMARY KEY (mail_seq)-- ,
-- 	 FOREIGN KEY (`sender_user`, `sender_password`) REFERENCES user_master (`user_name`, `user_pw`)
)ENGINE=INNODB;

insert into board_user_master(user_id,user_pw,user_name,user_email) values('admin',1234,'관리자','bfalcom@naver.com');

select * from board_user_master;

