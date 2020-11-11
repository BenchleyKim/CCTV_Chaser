import json
import os.path

def visual():
    case = input("Enter text :")
    check_input = input_check(case)
    if check_input == -1:
       return 0
    
    path = 'c:/Users/Lee Myeongwon/Desktop/python_workplace/'+case+'.json'
    f = open(path,'r')
    json_str = f.read()
    output = json.loads(json_str)
    result_ID = []

    for item in output:
        result_ID.append(item["ID"])
    else:
        print(result_ID)
        return result_ID

def input_check(input):
    path = 'c:/Users/Lee Myeongwon/Desktop/python_workplace/'+input+'.json'
    if os.path.exists(path):
        print('파일이 존재함')
        return input
    else:
        print('파일명이 잘못되었습니다')
        return -1

visual()