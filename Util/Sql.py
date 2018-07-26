# encoding = utf-8

create_database = 'CREATE DATABASE IF NOT EXISTS davieyang DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
drop_table = 'DROP TABLE testdata;'
create_table = """
    CREATE TABLE testdata(
        ID int primary key not null auto_increment comment '主键',
        BOOKNAME varchar(40) unique not null comment '书名',
        AUTHOR varchar(30) not null comment '作者'
    )engine = innodb character set utf8 comment '测试数据表';
"""