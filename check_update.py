import os
import requests

def download_file(url, save_path):
    get_update_file = requests.get(url)
    if get_update_file.status_code == 200:
        content = get_update_file.text
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File downloaded and saved to '{save_path}'.")
    else:
        print("File not found.")

def checking_func():
    file_url = 'https://github.com/Brucelee1107/OTA/blob/eb4e303d013019e78c43c6c0d0e61222ff775a52/update.yaml' 
    save_path = '/home/dinesh/target/dev/usb/update.yaml'
    
    check_update_file = requests.head(file_url)

    if check_update_file.status_code == 200:
        print("Update found")
        download = str(input('Do you want to download the update yes ''y'' or no ''n'' : '))
        if download == 'y':
            if os.path.exists(save_path):
                print("File already exists.")
            else:
                download_file(file_url, save_path)
        elif download == 'n':
            print('Update found, Download not started')
    else:
        return 'No update found'
def package_install():
    

checking_func()

