import json

with open('configuration.json', 'r') as f:
    curr_settings: dict = json.load(f)

user = input('Enter your username, if you set any, during MySQL installation(press Enter without writing anything, if you hadn\'t set anything): ') or 'root'
passwd = input('Enter the password you had set during MySQL installation: ')

curr_settings['user'] = user
curr_settings['passwd'] = passwd

with open('configuration.json', 'w') as f:
    json.dump(curr_settings, f, indent=4)
