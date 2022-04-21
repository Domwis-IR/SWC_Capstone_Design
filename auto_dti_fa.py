import os
import subprocess
import time


def main():
    ##################################
    # Parser for export // 이 부분만 입력하시고 실행시키시면 됩니다.
    BASEPATH = "C:/"
    studio_path = "C:/Users/RyuJihae/Desktop/dsi_studio_win"
    mri_path = os.path.join(BASEPATH, "Users/RyuJihae/Desktop/dsi_studio_win/HCP_YA1065_FIB_2mm")
    export_type = "dti_fa"
    ###################################

    file_list = os.listdir(mri_path)
    file_list.sort()
    print("The number of MRI is", len(file_list))
    print("ExportType:", export_type)
    os.chdir(mri_path)

    for file_name in file_list:
        chdir = os.popen(f"cd {mri_path}")
        print(f"------ Export {file_name} ------")
        stream = os.popen(f"start {studio_path}/dsi_studio.exe --action=exp --source={file_name} --export={export_type}")
        time.sleep(5)
    
if __name__=="__main__":
    main()
