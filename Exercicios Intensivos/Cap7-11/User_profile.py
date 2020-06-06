def build_profile(First, Last, **User_info):
    Profile = {}
    Profile['First_Name'] = First
    Profile['Last_Name'] = Last
    for Key , value in User_info.items():
        Profile[Key] =  value
    return Profile

User_Profile = build_profile('Albert', 'Einstein', Location = 'Princeton', Field = 'Physics' )

print(User_Profile)