list_of_dic = []
log_level_dic = {
    "ERROR" : 0,
    "INFO" : 0,
    "WARNING" : 0
}
log_list = []

def load_log(list_of_dic = list_of_dic, log_list = log_list):
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

def log_level(log_level_dic = log_level_dic, list_of_dic = list_of_dic):
    load_log()
    for dic in list_of_dic:
        message = dic["Message"]
        parts = message.split(" ",1)
        log_type = parts[0]
        if log_type in log_level_dic:
            log_level_dic[log_type] += 1

    print(f'ERROR : {log_level_dic["ERROR"]}')
    print(f'INFO : {log_level_dic["INFO"]}')
    print(f'WARNING : {log_level_dic["WARNING"]}')

def display_errors(list_of_dic = list_of_dic):
    print("=== ERRORS ===")
    for dic in list_of_dic:
        parts = dic["Message"].split(" ",1)
        log_type = parts[0]
        if log_type == "ERROR":
            print(dic["Message"])


def common_level(list_of_dic = list_of_dic , log_level_dic = log_level_dic):
    max_count = max(log_level_dic.values())
    if max_count == 0:
        print("No logs in file.")
        return
    max_logs = []
    for log_type,count in log_level_dic.items():
        if count == max_count:
            max_logs.append(log_type)
    print(f'OCCURRANCES : {max_count}')
    for log in max_logs:
        print(f'Most common log : {log}')


def search_log(list_of_dic = list_of_dic, log_list = log_list):
    to_search = input("Search Log : ").lower().strip()
    for line in log_list:
        if to_search in line.lower().strip():
            print(line)

def log_summary(list_of_dic = list_of_dic , log_level_dic = log_level_dic , log_list = log_list):
    print(f' Total log entries : {len(log_list)}')
    for key,value in log_level_dic.items():
        print(f'{key} : {value}')
        common_level()


log_level()
display_errors()
search_log()
log_summary()
