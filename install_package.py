import yaml
import subprocess
import requests


def install_package_from_server(yaml_file_path):
    try:
        get_file = requests.get(yaml_file_path)
        get_file.raise_for_status()
        yaml_content = get_file.text

        values = yaml.safe_load(yaml_content)

        package_to_update = values['packages']['ready_to_update']

        if not package_to_update:
            print('update not found')
        else: 
            num_packages = len(package_to_update)
            print(f'There are {num_packages} updates found')

            for index, package in enumerate(package_to_update, start=1):
                print(f'{index}. {package}')

            user_input = input("Do you want to install the packages? (y/n): ").lower()
            if user_input == 'y':
                for package in package_to_update:
                    command = ['sudo','apt','install',package]
                    subprocess.run(command, check=True)
                print('Successfully installed')
            elif user_input == 'n':
                print('update cancelled')
        
    except Exception as e:
        print(f'Error as : {e}')

yaml_file_path = 'https://raw.githubusercontent.com/Brucelee1107/OTA/main/update.yaml'

install_package_from_server(yaml_file_path)

