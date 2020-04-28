import requests
from bs4 import BeautifulSoup


def get_cases(c_name, type_of_data):
  '''
  type of data can be the following
  graph-active-cases-total
  graph-cases-daily
  graph-deaths-daily
  '''
  #copy this to your sublime cause repl.it is jarphat and wont challing
  url = f"https://www.worldometers.info/coronavirus/country/{c_name}/"
  source = requests.get(url).text
  soup = BeautifulSoup(source, 'lxml')
  x = soup.find('div', {'id': type_of_data}).parent
  y = x.find('script', {'type': 'text/javascript'}).text
  # print(type(y))
  y = y.split("},")
  dates = y[3].split('categories:')[1]
  dates = dates[2:].split("]")[0].split(",")
  values = y[7].split('data:')[1].split('}],')[
      0][2:].split(']')[0].split(",")
  to_ret = dict(zip(dates, values))
  return to_ret


# get_cases('nepal', 'graph-active-cases-total')

#to store values of things

def get_stats(c_name):
  values=[]
  update = requests.get('http://www.worldometers.info/coronavirus/').content
  soup = BeautifulSoup(update, 'lxml')


  for country in soup.find_all('a',{'class':'mt_a'}):
    if country.text==c_name:
      country1 = country.parent.parent
      break
  for val in country1:
    try:
      values.append(val.text)
    except:
      pass

  val_names=['country','tot-cases','new-cases','tot-death','new-death','tot-recovered','active','serious','tot-tests']
  values = values[:-1]
  x = values[10]
  values = values[:-4]
  values.append(x)
  return dict(zip(val_names,values))




#yo file lai copy garera rakh tero sublime ma arko naam rakhera
#ani yeslai import gar tero code ma get_stats bhanne fxn le #string linxa ani return garxa list
print(get_stats('India'))
# print(get_total_cases('nepal'))
