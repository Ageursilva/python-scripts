def build_profile(First, Last, **User_info):
    Profile = {}
    Profile['First_Name'] = First
    Profile['Last_Name'] = Last
    for Key , value in User_info.items():
        Profile[Key] =  value
    return Profile

User_Profile = build_profile('Ageu', 'Silva', Location = 'Arujá', Field = 'Science Computer',
                                                        Football_Team = 'São Paulo', Favorite_Food = "Feijoada"  )

print(User_Profile)