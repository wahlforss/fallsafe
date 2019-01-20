#global variables to be put in the file this would be called from

#prediction contains string whether falling fallen or standing
def alert_the_user(frame_number, prediction):    
    flag = 0
    count_fallen_seconds = 0
    if prediction == 'standing':
        #keep updating the start and end frame to current frame if the person is still standing
        start_frame = frame_number
        end_frame = frame_number
        count_fallen_seconds = 0
    elif prediction == 'falling':
        # the below feature can be used if required
        count_falling_seconds += 1
        end_frame = frame_number
    else:
        end_frame = frame_number
        count_fallen_seconds += 1
        if(count_fallen_seconds > 70):
            print("raise alarm")
