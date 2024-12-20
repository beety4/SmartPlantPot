import cv2
import time
import os
from influxdb import InfluxDBClient

def capture_photos_from_webcam(save_directory, capture_interval=14400):

    client = InfluxDBClient(host='', port=8086, username='', password='', database='')

    cap = cv2.VideoCapture(0)

    save_directory ="/home/pi/timelapse"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)


    if not cap.isOpened():
        print("no webcam")
        exit()

    try:
        while True:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"photo_{timestamp}.jpg"

            ret, frame = cap.read()
            if ret:
                cv2.imwrite(os.path.join(save_directory, filename), frame)
                print(f"{filename} ok.")

                json_body = [
                        {
                            "measurement":"photos",
                            "tags":{
                                "source":"webcam"
                                },
                            "fields":{
                                "filename":filename,
                                "timestamp":timestamp
                                }
                            }
                        ]
                client.write_points(json_body)
                print(f"{filename} store ok")
            else:
                print("no capture")

            time.sleep(capture_interval)

    except KeyboardInterrupt:
        print("stop")

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    save_directory = "/home/pi/timelapse"
    capture_interval = 14400

    capture_photos_from_webcam(save_directory, capture_interval)
