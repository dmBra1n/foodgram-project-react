import csv

from django.core.management import BaseCommand
from recipes.models import Ingredient

ENCODING = 'utf-8'


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Ingredient.objects.exists():
            self.stdout.write('Данные уже были загружены')
            return
        path_csv = 'data/ingredients.csv'
        self.load_ingredients(path_csv)
        self.stdout.write('Данные успешно загружены')

    def load_ingredients(self, path_csv):
        with open(path_csv, encoding=ENCODING) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                Ingredient.objects.create(
                    name=row[0],
                    measurement_unit=row[1]
                )
