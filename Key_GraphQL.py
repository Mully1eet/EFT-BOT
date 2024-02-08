from graphql_request import run_query

new_keys = """
{
  items(name:"ключ", lang:ru){
  name   
  }
}
"""

kvest_keys = """
{
   tasks(lang:ru) {
     name
     trader{
     name
      }
      neededKeys
    {
    keys{
      id
      name
      image8xLink
      sellFor{
    price
    vendor{
      name
      }
    
    
  }
    }
  }
   }
 }

"""

result_key_id = run_query(new_keys)
result_keyKvest_id = run_query(kvest_keys)
#raise ValueError(result_keyKvest_id)
all_key = result_key_id.get('data')['items']
# raise ValueError(all_key)
kvest = result_keyKvest_id.get('data')['tasks']
print(kvest)
wiki_link = 'https://escapefromtarkov.fandom.com/ru/wiki/'


def find_keys_kvest(target_key):
    max_price = -1
    name_traider = ''
    for i in kvest:
        neededKeys = i.get('neededKeys')

        if neededKeys is None or neededKeys =='None' or len(neededKeys) ==0:
            continue
            # print(neededKeys)
        for j in neededKeys:
              j_key = j['keys']
              for h in j_key:
                if h['name'] == target_key:
                    sell_For = h['sellFor']
                    for k in sell_For:
                        if max_price < k['price']:
                            max_price = k['price']
                            name_traider = k['vendor']['name']
                    text = f'Данный ключ: {target_key}\nНужен для квеста: {i["name"]}\nКвест выдает: {i["trader"]["name"]}\nLink: {wiki_link+i["name"].replace(" ","_" )}\nЦена ключа: {max_price} руб\nВыгодно всего у: {name_traider}'
                    url_image = h['image8xLink']
                    return text, url_image

    text_test = '1'
    for key in range(len(all_key)):
        if all_key[key]['name'] == target_key:
            text = f'Ключ "{target_key}" не нужен для квестов'
            text_test = '2'
    if text_test == '1':
        return 'Ты еблан?', ''
    else:
        return text, ''







