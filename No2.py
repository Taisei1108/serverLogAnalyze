from load import load_log 
from utils import daytosec
path = 'testcase/log_test3.txt' #ログ監視ファイルの指定
N = 1 #N回連続タイムアウトで故障認定

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
    break_count = 0
    for i in serve_list[str(server)]:
        if serve_log['state'][i]=='-':
            if break_count==0:
                break_i = i
                break_count+=1
            else:
                break_count+=1
            if break_count>=N:
                break_flag=1
        elif serve_log['state'][i]!='-' and break_flag ==1:
            date = int(serve_log['date'][i])-int(serve_log['date'][break_i])
            print(server,':',daytosec(str(date)))
            break_flag = 0 
            break_count = 0
        else:
            break_count=0
