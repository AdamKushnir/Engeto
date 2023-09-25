"""
projekt_3.py: druhy projekt do Engeto Online Python Akademie
author: Adam Kušnir
email: adamkushnir@outlook.cz
discord: Adam K. ASYPRO_AK#2480
"""

from bs4 import BeautifulSoup
import sys, time, requests, re

s = requests.Session()
s.headers.update({
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
})

def get_html(url: str) -> str:
    flag = True
    while flag:
        try: 
            site = s.get(url, timeout=5)
            flag = False
        except Exception as e: 
            time.sleep(1)
    return site.text


def get_data(tables: list, is_full: bool):
    all_td = tables[0].find_all("td")
    out_data = {}
    
    if is_full:
        registered = all_td[3].text.replace("\xa0", "")
        envelopes = all_td[4].text.replace("\xa0", "")
        valid = all_td[7].text.replace("\xa0", "")
    else:
        registered = all_td[0].text.replace("\xa0", "")
        envelopes = all_td[1].text.replace("\xa0", "")
        valid = all_td[4].text.replace("\xa0", "")

    for table in tables[1:]:
        for tr in table.find_all("tr"):
            td_list = tr.find_all("td")
            if len(td_list) != 5:
                continue
            if td_list[0].text == "-":
                continue 
            out_data[td_list[1].text.replace(',', ' ')] = td_list[2].text.replace("\xa0", "")

    return registered, envelopes, valid, out_data


def sub_table(table_obj):
    registered, envelopes, valid = 0, 0, 0
    out_dict = {}
    for td in table_obj.find_all("td", {"class": "cislo"}):
        soup = BeautifulSoup(get_html("https://www.volby.cz/pls/ps2017nss/" + td.a["href"]), "html.parser")
        table_list = soup.find_all("table", {"class": "table"})
        get_data(table_list, False) 
        registered_add, envelopes_add, valid_add, add_dict = get_data(table_list, False) 

        registered += int(registered_add)
        envelopes += int(envelopes_add)
        valid += int(valid_add)

        for el in add_dict:
            if el in out_dict:
                out_dict[el] += int(add_dict[el])
            else:
                out_dict[el] = int(add_dict[el])
    return registered, envelopes, valid, out_dict



def td_processing(url: str):
    soup = BeautifulSoup(get_html("https://www.volby.cz/pls/ps2017nss/" + url), "html.parser")
    table_list = soup.find_all("table", {"class": "table"})
    if len(table_list) == 1:
        registered, envelopes, valid, out_dict = sub_table(table_list[0])
    else:
        registered, envelopes, valid, out_dict = get_data(table_list, True) 

    return registered, envelopes, valid, out_dict


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Incorrect len of elements")
        exit(1)

    if len(re.findall(r'.*[.]csv', sys.argv[2])) != 1:
        print("Incorrect file name")
        exit(1)

    try:
        with open(sys.argv[2], "w") as file:
            pass
    except:
        print("Unable to open file")
        exit(1)


    main_link = sys.argv[1]
    
    is_file_have_not_header = True
    NAMES = []
    
    try:
        html_code = get_html(main_link)
    except:
        print("Incorrect link")
        exit(1)
    
    soup = BeautifulSoup(html_code, "html.parser")

    for table in soup.find_all("div", {"class": "t3"}):
        for tr in table.find_all("tr"):
            td_list = tr.find_all("td")
            if len(td_list) != 3:
                continue
            if td_list[0].text == "-":
                continue

            registered, envelopes, valid, out_dict = td_processing(td_list[2].a['href'])
            {
                "code" : td_list[0].text,
                "location" : td_list[1].text,
            }

            with open(sys.argv[2], "a") as file:

                if is_file_have_not_header:
                    NAMES = list(out_dict.keys())
                    file.write(", ".join(["code", "location", "registered", "envelopes", "valid"] + NAMES) + "\n")
                    is_file_have_not_header = False

                
                prepared_array = [str(out_dict[el]) for el in NAMES]
                file.write(", ".join([td_list[0].text, td_list[1].text, str(registered), str(envelopes), str(valid)] + prepared_array) + "\n")