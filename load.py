#サーバー監視ログファイル(txt形式)を読み込む関数を作成

def load_log(path):
    with open(path) as f:
        log_all = [s.strip() for s in f.readlines()]

    #エラー処理追加したい2021年2月11日
    num = []
    date = []
    network = []
    state = []
    count = 0
    for i in log_all:
        s = i.split(',')
        num.append(count)
        date.append(s[0])
        network.append(s[1])
        state.append(s[2])
        count+=1

    log_dict = {'num':num,'date':date,'network':network,'state':state}
    return log_dict