import os
import pandas as pd

def get_from_path(path:str):
    '''주소 참조 후 파일 불러오기
    공통 부분 함수화
    '''
    relative_path = path
    
    try:
        data = pd.read_csv(relative_path)
    except:
        absolute_path = os.path.abspath(relative_path)
        data = pd.read_csv(absolute_path)
        
    return data

def student_id_loader(self):
    '''데이터파일 불러와서 학번 리스트 반환
    '''
    relative_path = './data/si_checker.csv'

    student_id_data = get_from_path(relative_path)

    student_id_list = []

    for data in student_id_data.values:
        for i in data:
            student_id_list.append(f'{i}')
            
    print("[init data loader] ", len(student_id_list), "student_id_list load complete")
    
    return {'student_id_list' : student_id_list}

def locker_reserve_loader(self):
    '''사물함 예약 정보 불러와서 콘텍스트 리스트 반환
    '''
    
    relative_path = './data/locker_reserve_info.csv'
    
    locker_data = get_from_path(relative_path)
    
    locker_data_list = []
    
    for data in locker_data.values:
        print("data", data)
        for i in data:
            print(i, type(i))
        print()
        
