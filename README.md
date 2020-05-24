## Flask: IVAO WebEye Friend Status
This project generates a website that displays the online/offline status of all the friends in an IVAO WebEye Account.

### Requirements

Project **only** runs on a Windows with Chrome v81 installed due to the ChromeDriver binary!
This issue will be addressed eventually!

The following files must be provided in the project's root directory:

#### config.ini
```ini
[ACCOUNT]
# Example config file
# Specify IVAO WebEye login credentials here
user: admin
password: admin
```

#### friends.csv
A list of people you want to track, with their:
- IVAO ID
- name
- notes (this fills the third row of the table)
```csv
ivao_id,name,notes
123,John Doe,Martin Marietta
999,Perry Example,PanAm
```
Eventually this file will be deprecated and data will be gathered from IVAO WebEye.



#### To Do:
Fix a bug: friends with special characters in their name are not displayed with special characters as expected
