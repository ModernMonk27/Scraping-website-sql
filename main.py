import smtplib
import ssl

import requests
import selectorlib

url = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrapping(website):
    response = requests.get(url, headers=HEADERS)
    result = response.text
    return result


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extroctor.yaml")
    return_file = extractor.extract(source)["tours"]
    return return_file


def send_email(message):
    password = "epnpanqngtewxbfl"
    username = "lakshmiaravind.atom@gmail.com"
    receiver = "lakshmiaravind.atom@gmail.com"

    host = "smtp.gmail.com"
    port = 487

    physc = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=physc) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email sent succsfully..!!")


def store(data):
    with open("data.txt", "a") as file:
        content = file.write(data + "\n")


def read(data):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    ultra_source = scrapping(url)
    extracted_file = extract(ultra_source)
    print(extracted_file)
    content = read(extracted_file)

    if extracted_file != "No upcoming tours":
        if extracted_file not in content:
            store(extracted_file)
            send_email("how are you Today..!!")


