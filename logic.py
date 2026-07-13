import requests
import pyttsx3


def fact():
    url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        fact_text = data.get("text", "Факт не найден")
    else:
        return "Не удалось получить факт повторите попытку"
    


if __name__ == "__main__":
    text = fact()
    print(text)
