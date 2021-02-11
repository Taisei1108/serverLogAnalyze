
def daytosec(date):
    sec = 0
    bairitsu_list = [1,10,60,600,3600,36000,86400,864000]
    for i in range(len(date)):
        sec += bairitsu_list[i]*int(date[-(i+1)])
    return sec