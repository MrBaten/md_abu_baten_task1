import json
from django.core.management.base import BaseCommand
from myapp.models import TradeData
from datetime import datetime

class Command(BaseCommand):
    help = 'Load JSON data into the Trade model'

    def handle(self, *args, **kwargs):
        with open('jsondata/stock_market_data.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                item['date'] = datetime.strptime(item['date'], '%Y-%m-%d').date()
                item['volume'] = int(item['volume'].replace(',', ''))
                item['high'] = float(item['high'].replace(',',''))
                item['low'] = float(item['low'].replace(',',''))
                item['open'] = float(item['open'].replace(',', ''))
                item['close'] = float(item['close'].replace(',', ''))
                TradeData.objects.create(**item)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))