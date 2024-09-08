import os

def count_files_in_directory(directory_path):
    file_count = 0
    # 디렉토리 내의 모든 파일을 재귀적으로 탐색합니다.
    for root, dirs, files in os.walk(directory_path):
        file_count += len(files)
    return file_count

if __name__ == "__main__":
    directory_path = '/home/elicer/new_val/label_seg_merged'
    
    total_file_count = count_files_in_directory(directory_path)
    print(f"Total number of files in '{directory_path}': {total_file_count}")
