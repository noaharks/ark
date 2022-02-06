#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/28/10:37
# @Author  : Mr.wen
# @File    : NoahServer.py
# @Software: VScode


import socket
import re
import threading
import os
import sys
import requests
import time
import logging
import json
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.log

from tornado.escape import json_encode

'''forum = open('F:\my_code\web\noah\templates\forum.html',mode = 'r')
forumCode = forum.read()
forum.close()
print(forumCode)'''
    
trueIp = socket.gethostbyname(socket.gethostname())
print('the ip is ',trueIp)
# 定义一个默认值为80，类型为整型
tornado.options.define('port', default=80, type=int)


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('forum.html', **{'word': ''})
        word = self.get_argument('word')
        print('a man send',word)
        
        
        
def main():
    
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/',Index)],
    template_path=os.path.join(os.path.dirname(__file__),'templates'))
    temPath=os.path.join(os.path.dirname(__file__),'templates')
    print(temPath)
    httpserver = tornado.httpserver.HTTPServer(app)
    print(tornado.options.options.port) 
    httpserver.bind(80)#tornado.options.options.port)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    print(filename)
    return [filename,tornado.options.options.port]

    
    
if __name__ == '__main__':
    mainret = main()
    print(mainret)

