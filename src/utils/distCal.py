import requests

def get_distance(location1, location2):
    url = "https://distanceto.p.rapidapi.com/distance/route"

    payload = {
        "route": [
            {
                "country": "IND",
                "name": location1
            },
            {
                "country": "IND",
                "name": location2
            }
        ]
    }
    
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9028be3cb3msh43e10f4518dbd83p17eaddjsn422df5dafa4b",
        "X-RapidAPI-Host": "distanceto.p.rapidapi.com"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return int(data['route']['car']['distance'])
    except requests.exceptions.RequestException as e:
        return 9999999999

# result = get_distance("Margao", "Panjim")
# print(result)
