from rest_framework import serializers
from .models import Book
from datetime import datetime
import json

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# today = datetime.date()

# #SERIALIZATION
# book1 = Book("kelvin's Journey", "Sibuta", today)

# #Before serialization, you need to create a python dictionary
# book_dict = {
#     "title": book1.title,
#     "author": book1.author,
#     "date": book1.published_date
# }

# #convert the dictionary to json file

# book_json = json.dump(book_dict)

# #DE-SERIALIZATION
# # 1. convert json back to python
# book1_dict = json.load(book_dict)

# #convert the dictionary to a python object

# book1 = Book(author = book1_dict.get("author"), title = book1_dict.get("title"), date = book1_dict.get("published_date"))