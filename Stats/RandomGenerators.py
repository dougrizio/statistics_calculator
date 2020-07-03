import random


def random_seed(seed = None, decimal = 1, start = 0, stop = 100, step = 1):

    #can be used with or with out a seed, decimal = 1 will generate decimals

    if seed is not None:
        random.seed(seed)

    if decimal == 1:
        random_num = random.uniform(start, stop)
    else:
        random_num = random.randrange(start, stop, step)


    return random_num


def list_generator(seed = None, decimal = 1, start = 0, stop = 100):
# can be used with or without a seed, start and stop can be overridden
      random_list = []
      list_seed = seed
      random.seed(list_seed)


      for i in range(start, stop):
        if decimal == 1:
          random_num = random.uniform(0, 100)
        else:
            random_num = random.randrange(start,stop, 1)
        random_list.append(random_num)
     #For testing
     # print(len(random_list))
      return random_list


  #attach CSV reader?
def random_item(test_list):
     # used above function for testing
     #test_list = list_generator(12)

     choice = random.choice(test_list)
     return choice


def random_seed_choice():
      # used above function for testing
      test_list = list_generator(12)
      print("Sample list: " + str(test_list))
      random.seed(6)
      choice = random.choice(test_list)
      return choice


  #for seed and not seed
def n_items_no_seed(test_list, sample_size, seed = None):

      if seed is not None:
          random.seed(seed)

      number_of_choices = sample_size

      #test_list = list_generator(seed)

      sample = random.choices(test_list, k=number_of_choices)
      return sample




# change to what func you want to test
data = list_generator(decimal = 0, stop = 15)
msg = n_items_no_seed(data, sample_size = 7)

print("Sample_list: " + str(data))
print("Selections: " + str(msg))



















