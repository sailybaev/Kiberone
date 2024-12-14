import random
import json

#read
with open('books.json' , 'r') as knigi:
    books = json.load(knigi)

# cate -> books -> bookinfo

#print(books['categories'][0]['name'])
def randomBook() :
    a = random.choice(books['categories'])
    book = (a['name'], random.choice(a['books'])['title'])
    return book

def listCategory():
    for x in books['categories']:
        print(x['name'] , end=", ")

def byCategory(cat):
    for x in books['categories']:
        if x['name'] == cat:
            for i in x['books']:
                print(str(i['id']) +', '+ i['title'] + ', ' + i['author'] + ', ' + str(i['year']))

print(byCategory("Fiction"))




