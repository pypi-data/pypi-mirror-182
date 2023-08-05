import random, math, time, os, sys

def search_list(list_name, string_name):
  "Searches a given list for a given piece of information. If found, will return 'Done'"
  if string_name not in list_name:
    return "Not in list"
  else:
    for b in list_name:
      if b == string_name:
        return "Done"
      else:
        return "Not done, for now!"

def random_choice(list):
  "Returns a random choice from a given list."
  return random.choice(list)

def random_number(min, max):
  "Returns a random number between 2 given numbers."
  return random.randint(min, max)

def wait(amount_of_seconds):
  "Waits a given amount of seconds."
  int(amount_of_seconds)
  for wait in range(amount_of_seconds):
    time.sleep(1)

def clear_console():
  "Clears the console."
  os.system("clear")

def infinity():
  "Represents infinity."
  return math.inf

def typewrite_print(text):
  "Typewrites given text as a print."
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

def typewrite_input(text):
  "Typewrites given text as an input."
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
  input()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
