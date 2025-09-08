import requests

def ping():

    response = requests.get('https://restful-booker.herokuapp.com/ping')
    
    print(response.status_code)

    print(response.text)


def autenticaçao():
    corpo={
        "usurname":"admin",
        "password":"password123"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth",json = corpo)
    return response.json()["token"]


def booking(nome="fulano",sobrenome="ciclano",valor=0,
        pago = False,checkin = "2025-08-20", checkout ="2025-08-20",
        adicionais= "cafe da manhã"):
    corpo= {
        "firstname" : nome,
        "lastname" : sobrenome,
        "totalprice" : valor,
        "depositpaid" : pago,
        "bookingdates" : {
        "checkin" : checkin,
        "checkout" :checkout
        },
        "additionalneeds" : adicionais
        }
    response = requests.post("https://restful-booker.herokuapp.com/booking", json=corpo)
    return response.json()['bookingid']


def busca_booking(bookingid):

    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{bookingid}")
    return response.json()

print(busca_booking(10))