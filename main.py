from game_data import data
import art
import random
import replit 
# def compare(n1, n2):
#   if n1 > n2 :
#     print("okay")
#     return True
#   else:
#     print("Opps")
#     return False

print(art.logo)



end_of_game = False
while not end_of_game: 
  current_score = 0
  second = random.choices(data)
  sec_name = second[0]['name']
  print("Hello, welcome. Which has more followers?")
  # print(f"A is {sec_name} ")
  stop = False
  while not stop:
    first = second
    # first = random.choices(data)
    
    second = random.choices(data) 
    first_name = first[0]['name']
    first_des = first[0]['description']
    first_coun = first[0]['country']
    first_foll = first[0]['follower_count']
    first_values = first_name + ", " + first_des + ", from " + first_coun 
    sec_name = second[0]['name']
    sec_des = second[0]['description']
    sec_country = second[0]['country']
    sec_foll = second[0]['follower_count']
    second_values = sec_name + ", " + sec_des + ", from " + sec_country
    # print(f"A is {first_foll} ")
    # print(f"B is {sec_foll} ")
    print(f"Your current score is {current_score}")
    print(f"Your A: {first_values} \n")
    print(art.vs)
    print(f"Your B: {second_values} \n")
    choice = input("A or B ?: ").lower()
    if choice == "a":
      if first_foll > sec_foll:
        print("Yay, you got it right. On to the next!! 😚\n")
        second = first
        current_score += 1
        # stop = True
        replit.clear()
        
      else:
        print("Eyah, you can always try again 🥲\n")
        stop = True
        # end_of_game = True
    elif choice == "b":
        if sec_foll > first_foll:
          print("Okay Babe, I see you doing great 😉\n")
          first = second
          current_score += 1
          replit.clear()
          # stop = True
        else:
          print("shame, and you were so close too 😆")
          stop = True
          sick = True
          # end_of_game = True
    else:
        print("Opps, end of the road 🥶")
        stop = True
        # end_of_game = True
        
    
  print(f"Your current score is {current_score} ")
  yas = input("Do you want to start again? 'y' or 'n': ")
  if yas == 'y':
    replit.clear()
    end_of_game = False
  else:
    print("Bye dear 👋, later 😘")
    end_of_game = True