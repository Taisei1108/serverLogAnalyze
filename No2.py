import sys
from load import load_log 
path = 'testcase/log_test3.txt'


serve_log = load_log(path)
#server_log['num'],['date'],['network'],['state']

break_list =[]
#prev_network = []

#サーバーの種類を確認する、空の辞書になかったら空リストを登録
serve_list = {}
for i in serve_log['num']:
    if serve_log['network'][i] not in serve_list.keys():
        serve_list[str(serve_log['network'][i])] = [] 
#辞書にサーバーの種類ごとに識別番号'num'を登録
for i in serve_log['num']:
    serve_list[str(serve_log['network'][i])].append(serve_log['num'][i])

#故障を検出する
for server in serve_list:
    break_flag = 0
    for i in serve_list[str(server)]:
        if serve_log['state'][i]=='-' and break_flag ==0:
            break_flag = 1
            break_i = i
        elif serve_log['state'][i]!='-' and break_flag ==1:
            #故障時間を秒に治す関数作る
            print(server,':',int(serve_log['date'][i])-int(serve_log['date'][break_i]))
            break_flag = 0 
