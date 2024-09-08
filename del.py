import os

def remove_ds_store(directory):
    """
    지정된 디렉터리 및 하위 폴더에서 .DS_Store 파일을 삭제합니다.
    """
    for root, dirs, files in os.walk(directory):  # 모든 하위 폴더를 탐색
        for file in files:
            if file == '.DS_Store':
                file_path = os.path.join(root, file)
                os.remove(file_path)  # .DS_Store 파일 삭제
                print(f'Removed: {file_path}')

# 디렉토리 경로를 지정
directory_path = '/home/elicer/jyj/원천데이터/2실외중소형주차장_축소'
remove_ds_store(directory_path)