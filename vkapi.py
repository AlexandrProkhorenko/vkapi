import requests,pprint,json,yadisk,os,random
from random import randint



def request_vk_id():
    vk_token = 'Веди сюда свой токен доступа VK api'
    users_id = input('Введите ID старницы')
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id':  users_id,
        'album_id': 'profile',
        'photo_sizes': '1',
        'access_token': vk_token,
        'no_service_albums':'1',
        'extended':'1',
        'v': '5.131'

    }
    res = requests.get(url,params=params)
    # pprint.pprint(res.json())
    image = []

    for elem in res.json()['response']['items']:  #Отсеял максимальные значения к фото
        photo_name = randint(1, 10000)
        pics = elem['sizes'][-1]['url']
        print(pics)
        # name_of_pic = input('Введите название фотографии\n')
        url = pics
        img = requests.get(url)
        img_option = open(str(photo_name) +'.png', 'wb') # загрузка файлов
        img_option.write((img.content))
        img_option.close()
    choice = input('Требуется загзуить на яндекс диск? Y/N \n')
    if choice == 'Y':
        yandex_disk()
    elif choice == 'N':
        print('Загрузка фото закончена')
        start()


def yandex_disk():
    y = yadisk.YaDisk(token = 'AQAAAAA-k-wJAAd7SFBnEvWl3kxNjve_S5x7h-M')
    for photos in os.listdir():
        photo_name = randint(1, 1000)
        y.upload(photos,photo_name)
    print('Загрузка фото Хуесоса звершенна')


def start():
    yes = input('Начать работу?\n')
    if yes == 'Y':
        request_vk_id()
    elif yes == 'N':
        print('Работа программы завершенна\n')
        return 'stop'


start()
















    # for save in pics[1]:
    #     pass



#
# request_vk_id()


# 5921118
# 7988249







