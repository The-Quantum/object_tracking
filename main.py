import cv2
import numpy as np
import math

from source_code.object_detection import ObjectDetection

Object_detection = ObjectDetection()

#cap = cv2.VideoCapture("source_code/los_angeles.mp4")
cap = cv2.VideoCapture(0)

count = 0
center_point_prev_frame = []
track_object = {}
track_id = 0

while True:

    success, frame = cap.read()
    count += 1
    if not success :
        break
    center_point_current_frame = []

    class_ids, scores, boxes = Object_detection.detect(frame)

    for box in boxes :
        print(box)
        x, y, w, h = box
        cx = int((x+ x+ w)/2)
        cy = int((y+ y+ w)/2)

        center_point_current_frame.append((cx, cy))
        print("Frame N°", count, box, x, y, w, h)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    if count <= 2 :
        for pt in center_point_current_frame:
            for pt2 in center_point_prev_frame :
                distance = math.hypot(pt2[0]-pt[0], pt2[1]-pt[1])

                if distance < 20 :
                    track_object[track_id] = pt
                    track_id += 1
    
    else :
        track_object_copy = track_object.copy()
        center_point_current_frame_copy = center_point_current_frame.copy()
        
        for object_id, pt2 in track_object_copy.items() :

            object_exist = False

            for pt in center_point_current_frame_copy:
                distance = math.hypot(pt2[0]-pt[0], pt2[1]-pt[1])

                if distance < 20 :
                    track_object[object_id] = pt
                    object_exist = True
                    if pt in center_point_current_frame :
                        center_point_current_frame.remove(pt)
                    continue

            if not object_exist:
                track_object.pop(object_id)

        for pt in center_point_current_frame :
            track_object[track_id] = pt
            track_id +=1 

    for object_id, pt in track_object.items() :
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1]-7), 0, 1, (0, 0, 255), 2)

    print("Current frame", center_point_current_frame)
    print("Prev Frame:", center_point_prev_frame)

    
    cv2.imshow("Frame", frame)

    center_point_prev_frame = center_point_current_frame.copy()
    if cv2.waitKey(1) == ord("q"):
        break


    

cap.release()
cv2.destroyAllWindows()

