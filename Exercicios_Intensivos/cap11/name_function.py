def get_formatted_name(fisrt, last, midle=''):
    """ Gera um nome fomatado"""
    if midle:
        full_name =  f'{fisrt} {midle} {last}'
    else:
        full_name =  f'{fisrt} {last}'
    return full_name.title()