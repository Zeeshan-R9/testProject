
from Pexels import Client
from pprint import pprint 
client = Client(token="oAaoTX5Bnfsb58jacFxWsReS4v7luZiJYYLMlR5Gj3W6jqFWaoD3pCiC")

#search photos
photos = client.search_photos(query="Dog", page=1, per_page=80)


#you can access return data like
pprint(len(photos.photos))