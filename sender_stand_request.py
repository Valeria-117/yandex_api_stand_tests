import configuration
import requests
import data
def post_products_kits(ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=ids)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки




def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


