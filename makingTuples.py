my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def makingTuples(dict):
    items = dict.items()
    return items
    # [(k, v) for k, v in dict.items()]
    # return

print(makingTuples(my_dict))