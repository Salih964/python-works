from random import shuffle

def shuffle_and_print(list_to_shuffle):
 
  shuffle(list_to_shuffle)
  print("Shuffled list:", list_to_shuffle)

# Example usage
my_list = [1, 2, 3, 4, 5]
shuffle_and_print(my_list)
