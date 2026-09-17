list_of_dic = []
log_level_dic = {}
log_list = []

def load_log(list_of_dic , log_list ):
    try:
        with open("app.log","r") as file:
            for line in file:
                log_list.append(line.strip())
    except FileNotFoundError:
        print("File not found !")
        return
    if log_list:
        for line in log_list:
            date,time,message = line.split(" ",2)
            list_of_dic.append({
                "Date" : date,
                "Time" : time,
                "Message" : message
            })

def log_level(log_level_dic , list_of_dic ):
    load_log(list_of_dic , log_list)
    for dic in list_of_dic:
        parts = dic["Message"].split(" ",1)
        log_type = parts[0]
        if log_type in log_level_dic.keys():
            log_level_dic[log_type] += 1
        else:
            log_level_dic[log_type] = 1

    print("=== OCCURANCES ===")
    for key,value in log_level_dic.items():
        print(f'{key} : {value}')


def display_errors(list_of_dic ):
    print("=== ERRORS ===")
    for dic in list_of_dic:
        parts = dic["Message"].split(" ",1)
        log_type = parts[0]
        if log_type == "ERROR":
            print(dic["Message"])

def common_level(list_of_dic , log_level_dic ):
    max_count = max(log_level_dic.values())
    if not log_level_dic:
        print("No logs available to count.")
        return
    print("Most common occurances !")
    for log_type,count in log_level_dic.items():
        if count == max_count:
            print(f'{log_type} : {count}')



def search_log(list_of_dic, log_list):
    to_search = input("Search Log : ").lower().strip()
    for line in log_list:
        parts = line.split(" ",2)
        message = parts[2]
        if to_search in message.lower().strip():
            print(message)


def log_summary(list_of_dic , log_level_dic  , log_list ):
    print(f' Total log entries : {len(log_list)}')
    for key,value in log_level_dic.items():
        print(f'{key} : {value}')
    common_level(list_of_dic , log_level_dic )


log_level(log_level_dic , list_of_dic )
display_errors(list_of_dic)
log_summary(list_of_dic , log_level_dic  , log_list)
search_log(list_of_dic, log_list)
