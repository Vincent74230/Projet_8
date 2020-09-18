from . models import Products


class Fetch:
    def fetch_products_in_db(user_question):
        query = Products.objects.filter(iexact__name=user_question)
        return query[0].barcode
