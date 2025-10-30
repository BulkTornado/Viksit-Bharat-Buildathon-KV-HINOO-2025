import json

with open('proj_settings.json', 'r') as f:
    curr_settings: dict = json.load(f)

passwd = input('Enter the password you had set during MySQL installation: ')

curr_settings['passwd'] = passwd

with open('proj_settings.json', 'w') as f:
    json.dump(curr_settings, f, indent=4)
