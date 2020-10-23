"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World1!'}
    return jsonify(json_data)
    from bs4 import BeautifulSoup  # для парсинга старниц
    from requests import get  # для запросов к сайту, получения содержимого веб-страницы

    url = 'http://www.azair.com/azfin.php?tp=0&searchtype=flexi&srcAirport=Tenerife+North+%5BTFN%5D+%28%2BTFS%29&srcTypedText=tene&srcFreeTypedText=&srcMC=&srcap0=TFS&srcFreeAirport=&dstAirport=London+%5BLGW%5D+%28%2BLHR%2CSEN%2CLTN%2CSTN%29&dstTypedText=london&dstFreeTypedText=&dstMC=LON_ALL&adults=1&children=0&infants=0&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&dstap0=LHR&dstap1=SEN&dstap2=LTN&dstap4=STN&dstFreeAirport=&depdate=23.10.2020&arrdate=30.4.2021&minDaysStay=5&maxDaysStay=10&nextday=0&autoprice=true&currency=EUR&wizzxclub=false&supervolotea=false&schengen=false&transfer=false&samedep=true&samearr=true&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&maxChng=1&isOneway=return&resultSubmit=Search'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.body.results)

    for link in soup.find('div', class_="result"):
        if soup.find('span', class_="caption tam").text == "There":
            print (soup.find('span', class_="from").text)


if __name__ == '__main__':
    app.run()
