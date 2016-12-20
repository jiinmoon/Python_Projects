
from urllib.request import Request, urlopen
import json, codecs

json_url = "https://shopicruit.myshopify.com/admin/orders.json?page={}&access_token=c32313df0d0ef512ca64d5b336a0d7c6"

def main():

  page_number = 1
  response = urlopen(json_url.format(page_number))

  reader = codecs.getreader("utf-8")
  json_data = json.load(reader(response))

  sum = 0
  while(not len(json_data['orders']) == 0):

    for i in range(len(json_data['orders'])):
      print("ID: {} | Total Price: ${}".format(json_data["orders"][i]["id"], json_data["orders"][i]["total_price"]))
      sum += float(json_data["orders"][i]["total_price"])

    page_number += 1
    response = urlopen(json_url.format(page_number))
    json_data = json.load(reader(response))

  print("Total Order Revenue: CAD ${:0.2f}".format(sum))


if __name__ == '__main__':
  main()