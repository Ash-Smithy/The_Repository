def calculate_total_score():
    total_score = 0

    user = input("Enter the user: ")
    #Mech Cat
    dribbling_ground_play = int(input("Dribbling/Ground play rating (1-10): "))
    flicks_shadow_defence = int(input("Flicks against easy Shadow defence rating (1-10): "))
    favourite_ground_mech = int(input("Favourite ground mech rating (1-10): "))
    shoot_from_different_passes = int(input("Shoot from different passes rating (1-10): "))

    #Wall Play cat
    power_shot_off_wall = int(input("DIA power shot off wall rating (1-10): "))
    airdribble = int(input("C: Airdribble rating (1-10): "))
    airdribble_double_tap = int(input("GCL airdribble double tap rating (1-10): "))

    #backboard Defence cat
    clear_from_corner = int(input("DIA: clear from corner rating (1-10): "))
    powerful_clear_upfield = int(input("C: poweful clear upfield rating (1-10): "))

    #Aerials Cat
    self_setup_low_aerial_shot = int(input("Self setup low aerial shot rating rating (1-10): "))
    high_aerial_off_our_setup = int(input("High aerial off out setup rating (1-10): "))

    #Reads category
    low_backboard_read = int(input("DIA: low backboard read rating (1-10): "))
    high_backboard_read = int(input("Champ : high backboard read rating (1-10): "))
    one_touch_pass = int(input("Champ: one touch pass rating (1-10): "))
    showoff_rating = int(input("Showoff rating (1-10): "))

    #3's cat
    rotations = int(input("Rotations rating (1-10): "))
    speed_and_accuracy = int(input("Their speeed and accuracy rating (1-10): "))
    decision_making = int(input("decision making rating (1-10): "))
    ease_of_play_around_them = int(input("Ease of play around them rating (1-10): "))

    #Calculate total score
    total_score += (dribbling_ground_play+flicks_shadow_defence+favourite_ground_mech+favourite_ground_mech+shoot_from_different_passes)
    total_score += (power_shot_off_wall+airdribble+airdribble_double_tap)
    total_score += (clear_from_corner+powerful_clear_upfield)
    total_score += (self_setup_low_aerial_shot+high_aerial_off_our_setup)
    total_score += (low_backboard_read+high_backboard_read+one_touch_pass+showoff_rating)
    total_score += (rotations+speed_and_accuracy+decision_making+ease_of_play_around_them)


    with open("total_score.txt","a+") as file:
        file.write("\n"+user+"'s Total Score: "+ str(total_score))
        file.close()
    print("File created!")

calculate_total_score()
