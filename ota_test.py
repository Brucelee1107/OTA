import zipfile
import hashlib

# Define update content
update_version = "3.0"
update_files = ["/usr/lib/firmware/tlg2300_firmware.bin", "/home/dinesh/.local/lib/python3.11/site-packages/zmq/utils/config.json"]

# Create a zip archive for the update package
with zipfile.ZipFile("ota_update.zip", "a") as zipfile:
    for file in update_files:
        zipfile.write(file)

# Calculate checksum of the update package
checksum = hashlib.sha256()
with open("ota_update.zip", "rb") as update_file:
    while chunk := update_file.read(8192):
        checksum.update(chunk)
update_checksum = checksum.hexdigest()

# Create metadata file
metadata = f"""\
Version: {update_version}
Checksum: {update_checksum}
"""

with open("ota_metadata.txt", "w") as metadata_file:
    metadata_file.write(metadata)

print("OTA package created successfully.")

