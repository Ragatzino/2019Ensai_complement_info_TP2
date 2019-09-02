import requests
from lxml import etree


if __name__ == "__main__":
    response = requests.get('https://fr.wikipedia.org/wiki/Ginkgo_biloba')
    tree = etree.HTML(response.text)
    result = tree.xpath('//h1/i')
    print(result[0].text)
