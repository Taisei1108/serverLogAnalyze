#サーバー監視ログファイル(txt形式)を読み込む関数を作成

def load_log(path):
    with open(path) as f:
        log_all = [s.strip() for s in f.readlines()]
        print(type(f))

    #エラー処理追加したい2021年2月11日
    date = []
    network = []
    state = []
    for i in log_all:
        s = i.split(',')
        date.append(s[0])
        network.append(s[1])
        state.append(s[2])

    log_dict = {'date':date,'network':network,'state':state}
    return log_dict