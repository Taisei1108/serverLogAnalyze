from load import load_log 
from utils import daytosec
path = 'testcase/log_test3.txt' #ログ監視ファイルの指定
m = 7 #直近m回までのサーバログを見る
t = 100 #tミリ秒を過負荷状態のしきい値とする

serve_log = load_log(path)
#server_log['num'],['date'],['network'],['state']

break_list =[]
#prev_network = []

#サーバーの種類を確認する、空の辞書になかったら空リストを登録 & 直近ｍまでをチェックする
serve_list = {}
for i in serve_log['num'][len(serve_log['num'])-m:len(serve_log['num'])]:
    if serve_log['network'][i] not in serve_list.keys():
        serve_list[str(serve_log['network'][i])] = [] 
#辞書にサーバーの種類ごとに識別番号'num'を登録
for i in serve_log['num'][len(serve_log['num'])-m:len(serve_log['num'])]:
    serve_list[str(serve_log['network'][i])].append(serve_log['num'][i])

#タイム・アウトした場合の応答結果は無視する
#平均応答時間を計算する (tミリ秒を超えていなかったら '-'→過負荷になっていないという意味)
ave_res = []
for server in serve_list:
    res_result = 0
    count = 0
    for i in serve_list[str(server)]:
        if serve_log['state'][i]!='-':
            res_result += int(serve_log['state'][i])
            count+=1
    if t < res_result/count:
        ave_res.append(res_result/count)
    else:
        ave_res.append('-')

#過負荷状態の期間を出力
count = 0
for server in serve_list:
    if ave_res[count] != "-":
        kikan = int(serve_log['date'][serve_list[str(server)][-1]]) - int(serve_log['date'][serve_list[str(server)][0]])
        print(daytosec(str(kikan)))
    count += 1
    