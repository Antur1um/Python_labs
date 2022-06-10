from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
import requests

WK = 'https://rusmeteo.net/weather/kemerovo/'
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%53A1584716087546&source=hp&ei' \
             '=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq' \
             '=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294' \
             '...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4 '
EURO_RUB = 'https://www.google.com/search?q=евро+к+рублю&sxsrf=ALiCzsZfpTDUjvoPF2rtg4CfBh6o8vkAyQ%3A1651997130857&ei' \
           '=ynl3YtqCNIX6rgS_8rSYDw&oq=доллар+к+рублю&gs_lcp' \
           '=Cgdnd3Mtd2l6EAEYATIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIKCAAQRxCwAxDJAzIHCAAQRxCwAzIHCAAQsAMQQ0oECEEYAEoECEYYAFAAWABgtiBoAnABeACAAQCIAQCSAQCYAQDIAQrAAQE&sclient=gws-wiz '
JPY_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%BE%D0%B9+%D0%B9%D0%B5%D0%BD%D1%8B&sxsrf=ALiCzsbYW35KcA561_elk5MedqiBGx9xbQ%3A1654783523626&ei=I_6hYoLqJY36rgTBuLqIBA&oq=%D0%9A%D1%83%D1%80%D1%81+%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%BE%D0%B9&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMggIABCABBCxAzIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxDqAhAnOg0ILhDHARDRAxDqAhAnOhYIABDqAhC0AhCKAxC3AxDUAxDlAhgBOg0ILhCPARDqAhC0AhgCOg0IABCPARDqAhC0AhgCOgQIIxAnOgsIABCABBCxAxCDAToHCAAQsQMQQzoECAAQQzoFCC4QgARKBAhBGABKBAhGGAFQAFiRNmC_RmgCcAF4AIAB1AGIAakMkgEFNC45LjGYAQCgAQGwARTAAQHaAQYIARABGAHaAQYIAhABGAo&sclient=gws-wiz-serp'
Decks = 'https://mtgdecks.net/'
Explorer = 'https://mtgdecks.net/Explorer'
Standard = 'https://mtgdecks.net/Standard'
Pioneer = 'https://mtgdecks.net/Pioneer'
Pauper = 'https://mtgdecks.net/Pauper'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

