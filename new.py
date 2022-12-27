#import requests

#def get_info(gets):
#    url = f'https://rickandmortyapi.com/api/{gets}'
#    response = requests.get(url)
#    data = response.json()
#    return data

#def get_location(gets):
#    get_id=get_info(f'character/{gets}')
#    for i in get_id.keys():
#        if i=='location':
#            name_location=get_id['location']['name']
#            url_location=get_id['location']['url']
#            id_url=url_location.split('/')[-1]    
#            location=get_info(f'location/{id_url}')
#            name_dimension=location['dimension']
#            type_location=location['type']
#            information_location=f"""
#            Название локаций: {name_location}
#            Тип локаций:{type_location}
#            Измерение локаций:{name_location}
#            """


#def get_character_info(gets):
    #if gets <= 826:
      #  character = get_info(f'character/{gets}')
      #  edit_sylka = character['location']['url']
     #   if edit_sylka is not None:
#            id_locations = edit_sylka.split('/')[-1]
#            location = get_info(f'location/{id_locations}')
#            information = f"""
#            Идентификатор персонажа: {character['id']}
#            Имя персонажа: {character['name']}
#            Пол персонажа: {character['gender']}
#            Жизненное положение: {character['status']}
#            Какой расе относится: {character['species']}
#            Личность: {character['type']}

#            Измерения: {location['dimension']}
#            Дата создание: {character['created']}
#            """
    #        return information
   #     elif edit_sylka is None:
#            information = f"""
#            Идентификатор персонажа: {character['id']}
#            Имя персонажа: {character['name']}
#            Пол персонажа: {character['gender']}
#            Жизненное положение: {character['status']}
#            Какой расе относится: {character['species']}
#            Личность: {character['type']}

 #           Измерения: Unknown
 #           Дата создание: {character['created']}
 #           """
  #          return information
 #       return 'Не правильный id персонажа'
#print(get_character_info(361))


import requests

def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json()
    return data

def get_episode(gets):
    get_id_episodes = get_info(f'character/{gets}')
    for i in get_id_episodes['episode']:
        response = requests.get(i)
        episode = response.json()
        information_episode = f'''
    Эпизод где участвует персонаж 
        Название эпизода: {episode['name']}
        Дата релиза: {episode['air_date']}
        Эпизод: {episode['episode']}
        Дата создания: {episode['created']}
        '''
        return information_episode

def get_location(gets):
    get_id = get_info(f'character/{gets}')
    for i in get_id.keys():
        if i == 'location':
            name_location = get_id['location']['name']
            url_location = get_id['location']['url']
            if url_location not in '':
                id_url = url_location.split('/')[-1]
                location = get_info(f'location/{id_url}')
                name_dimension = location['dimension']
                type_location = location['type']
                information_location = f'''
        Название локации: {name_location}
        Тип локации: {type_location}
        Измерение локации: {name_dimension}
        '''
                return information_location
            else:
                information_location = f"""
        Название локации: {name_location}
        Тип локации: Unknown
        Измерение локации: Unknown"""
                return information_location

def get_character_info(gets):
    if gets <= 826:
        character = get_info(f'character/{gets}')
        information = f"""
        Идентификатор персонажа: {character['id']}
        Имя персонажа: {character['name']}
        Пол персонажа: {character['gender']}
        Жизненное положение: {character['status']}
        Какой расе относится: {character['species']}
        Личность: {character['type']}
        Дата создания: {character['created']}
        Эпизоды где есть персонаж: {' ' .join(character['episode']) .center(10)}
        {get_location(gets)}
        """
        return information
    return 'Не правильный id персонажа'
character = int(input('Введите id персонажа: '))
print(get_character_info(character))
    