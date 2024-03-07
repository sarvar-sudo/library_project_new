from .models import Book
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle','author','image',
        'content','isbn','price')
    
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author',None)
        
        # kiritiladigan qiymat harflardan iboratmi yo'qmi tekshirib olish 
        if not title.isalpha():
            raise ValidationError(
                {
                "status": False,
                "message": "Kitobni sahifasi harflardan tashkil topgan bo'lishi kerak !"
                }
            )
    
        # check author va title from database existence 
        if Book.objects.filter(author=author, title=title).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

    def validate_price(self, price):
        if price>0 and price<99999999999999:
            raise ValueError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )
        

class CashSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=255)
    output = serializers.CharField(max_length=255)
        