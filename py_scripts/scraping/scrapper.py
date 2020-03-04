import requests
import bs4
import json



def scrape():
    url = "https://bnonews.com/index.php/2020/01/timeline-coronavirus-epidemic/"
    response = requests.get(url)
    html = bs4.BeautifulSoup(response.text, "lxml")
    raw = html.find("div", attrs={"id": ["mvp-content-main"]})
    dates = raw.find_all("h4")
    infos = raw.find_all("ul")
    data = {}
    total = {}
    conversion_list = {'Hebei province': 'China', 'Hubei province': 'China','city of Huangshi': 'China','Hubei province at 7 a': 'China', 'Diamond Princess cruise ship': 'United States', 'Germany: 3': 'Germany' }
    for i in range(len(dates)):
        index = len(dates)-i-1
        day = dates[index].text
        statements = infos[index].find_all("li")
        data[day] = {}
        for s in statements:
            statement = s.text.strip()
            parsed_data = parse_statement(statement)
            if not parsed_data["usable"]:
                continue

            loc = parsed_data["location"]
            if loc in conversion_list:
                loc = conversion_list[loc]
            if loc not in total:
                total[loc] = {"total-cases": 0, "total-deaths": 0}
            if loc not in data[day]:
                data[day][loc] = {"delta-cases": 0, "delta-deaths": 0}

            data[day][loc]["delta-cases"] += parsed_data["cases"] - parsed_data["deaths"]
            data[day][loc]["delta-deaths"] += parsed_data["deaths"]
            total[loc]["total-cases"] += data[day][loc]["delta-cases"]
            total[loc]["total-deaths"] += parsed_data["deaths"]
            data[day][loc]["total-cases"] = total[loc]["total-cases"]
            data[day][loc]["total-deaths"] = total[loc]["total-deaths"]
    with open("case-data.json", "w") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)



def parse_statement(s):

    def find_num(s, i):
        str_num = []
        k = i - 2  # accounting for the space
        while k > -1:
            if s[k].isdigit():
                str_num.append(s[k])
                k -= 1
            else:
                break

        if len(str_num) > 0:
            str_num.reverse()
            return int(''.join(str_num))

    # break down into sentences
    sentence = str(s.split(".")[0].strip())

    # extract location and case and deaths
    data = {"cases": 0, "deaths": 0, "usable" : False}

    i = sentence.find("new case")
    if i != -1:
        data["cases"] = find_num(sentence, i)
    i = sentence.find("new death")
    if i != -1:
        data["deaths"] = find_num(sentence, i)

    if " in " in sentence:
        data["usable"] = True
        location = sentence.split(" in ")[1].strip()
        if "(Source)" in location:
            location = location[:-len("(source)")]

        if "the" in location:
            location = location[3:]

        data["location"] = location.strip()
        if location.find(",") > -1:
            loc = location.split(",")[-1].strip()
            if len(loc.split(" ")) > 0:
                data["usable"] = False
            data["location"] = loc.strip()

    return data

scrape()

