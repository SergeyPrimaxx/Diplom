import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = 'vk1.a.VxsERUUBgY139G6pR-fYxAuRZdhA9vQCy89ZbAlNtO3vP-GMF7-5xUYSTrkmpdYL9g9ftzcDCXe1hoxVJSuC4q3tTq9IdJFJ5_Q5hu8hAAIaqc0w-QVAH-ABIdRBLfnwRxKZ3150cyaHfyeiCEMReaVwOpOHjWUucoJes82U-nTA20MH1lo5Eh7jp4cwV5NeCAW8Pvla1z-d5x6kr-bgEQ'
user_id = '762618932'
vk = VK(access_token, user_id)
print(vk.users_info())