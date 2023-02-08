import http.client
import json

store_server = str("itunes.apple.com")

def make_store_uri(country_code: str, genre: str, section: str) -> str:
    """
    
    """
    store_uri = f"/WebObjects/MZStoreServices.woa/ws/charts?cc={country_code}&g={genre}&name={section}&limit=400"
    
    return store_uri


def fetch(url, appID):
    """
    Request an URL
    """
    conn = http.client.HTTPSConnection(store_server)
    headers = { "Cache-Control" : "no-cache" }
    conn.request("GET", url, None, headers)
    response = conn.getresponse()

    data = response.read()

    ranking = json.loads(data)

    conn.close()

    # JSON document
    posicion = process_result(ranking, appID)

    return posicion


def process_result(result, appID):
    """
    Process JSON and recover results
    """
    entries = result["resultIds"]

    try:
        position = entries.index(appID)
        return (position + 1)
    except ValueError:
        return "---"