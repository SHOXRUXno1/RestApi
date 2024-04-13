from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        price = data.get('price', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi satr bo'lishi kerak"

                }
            )

        if title == author:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Muallif va kitob sarlavhasi bir xil bo'lishi mumkin emas!"
                }
            )

        if price.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narx satr bo'lishi mumkin emas!"
                }
            )

        if author.is_digit():
            raise ValidationError(
                {
                    'status': False,
                    "message": "Muallif son bo'lishi mumkin emas!"
                }
            )

        return data
