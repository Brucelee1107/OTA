import subprocess
import yaml
import requests

def install_packages_from_remote_yaml(yaml_url):
    try:
        # Fetch the YAML content
        response = requests.get(yaml_url)
        response.raise_for_status()
        yaml_content = response.text

        # Parse the YAML data
        data = yaml.safe_load(yaml_content)

        # Get the list of packages to update
        packages_to_update = data['packages']['ready_to_update']

        if not packages_to_update:
            print("No packages to update.")
            return

        num_packages = len(packages_to_update)
        print(f"There are {num_packages} packages ready to update.")

        # Ask for user confirmation before installation
        user_input = input("Do you want to install the packages? (y/n): ").lower()

        if user_input == 'y':
            # Install each package using apt
            for package in packages_to_update:
                command = ['sudo', 'apt', 'install', package, '-y']
                subprocess.run(command, check=True)

            print("Packages successfully installed.")
        else:
            print("Package installation aborted.")

    except requests.exceptions.RequestException as req_err:
        print("Request error:", req_err)
    except yaml.YAMLError as yaml_err:
        print("YAML error:", yaml_err)
    except subprocess.CalledProcessError as cmd_err:
        print("Command error:", cmd_err)
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
remote_yaml_url = 'https://raw.githubusercontent.com/Brucelee1107/OTA/main/update.yaml'
install_packages_from_remote_yaml(remote_yaml_url)

