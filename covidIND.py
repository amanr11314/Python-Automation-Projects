import bs4 as bb
import requests as rq

r2 = rq.get("https://www.mohfw.gov.in/")
soup2 = bb.BeautifulSoup(r2.text, "html.parser")
table = soup2.find('div', {'class': 'content newtab'})

def getRows():
    # rows = getRows()
    # for l in rows:
    #     print(l)
    headingsTag = table.findChildren('strong')
    rows = []
    count = 0
    for h in headingsTag:
        if(h.string is None):
            rows.append('Cured / Discharged / Migrated')
        else:
            rows.append(h.string)
        # print(h.string)
        count += 1
        if(count == 6):
            break

    return rows

all_state_records = []
all_state_records.append(getRows())


def getRecords():
    # for i in all_state_records:
    #     print(i)
    data = table.findChildren('tr')
    for record in data:
        r1 = record.findAll('td')
        row = []
        for value in r1:
            row.append(value.string)
        if(len(row)):
            all_state_records.append(row)

getRecords()

for i in all_state_records:
    print(i)
