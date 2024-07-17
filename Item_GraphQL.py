from graphql_request import run_query


# all_item = """
# {
# items(lang:ru){
#   name
#   types
# }
# }
# """
all_item = """
    {
    items(lang:ru){
      name
      image8xLink
      usedInTasks{
        name
        wikiLink
        trader{
          name
        }
      }
      sellFor{
        price
        vendor{ 
          name
        }
      }
    
    }
    }
    """
result_all_item = run_query(all_item)


result_all_item = result_all_item.get('data')['items']

def search_task():
     max_price = -1
     name_traider = ''
     item_in_task = {}
     str_task_object = ''
     for i in result_all_item:
          sellfor = i['sellFor']
          for h in sellfor:
               if max_price < h['price']:
                    max_price = h['price']
                    name_traider = h['vendor']['name']
          for k in i['usedInTasks']:
               wiki_link = f'<a href="{k["wikiLink"]}"> {k["name"]} </a>'
               str_task_object = f'{str_task_object} {wiki_link} дает {k['trader']['name']}\n'
          item_in_task[i['name']] = [str_task_object,i['image8xLink'],max_price,name_traider]
          str_task_object = ''
     return item_in_task




def return_item_task(dict_item_task,target_item):
     return f"{target_item}: нужен в квесте\n{dict_item_task[target_item][0]}\nЦена предмета: {dict_item_task[target_item][2]} руб\nВыгодно всего у: {dict_item_task[target_item][3]}", dict_item_task[target_item][1]