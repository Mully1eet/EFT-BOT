from Key_GraphQL import run_query


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
      types
      image8xLink
      usedInTasks{
        name
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
# print(result_all_item)


result_all_item = result_all_item.get('data')['items']
print(result_all_item)
