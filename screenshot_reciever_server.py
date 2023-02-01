import datetime
import logging
import sys

from flask import Flask, request
from waitress import serve

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

png_file_start_bytes = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'


@app.route("/upload-screenshot", methods=["POST"])
def upload_screenshot():
    image_file = request.files.get("screenshot")
    if image_file:
        file_name = "./screenshots/" + request.remote_addr + "_" + str(
            datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")) + ".png"

        if image_file.read(8) == png_file_start_bytes:
            with open(file_name, "wb") as f:
                f.write(png_file_start_bytes + image_file.read())
            return "Screenshot received and saved successfully", 200
        else:
            print("Request file in 'screenshot' isn't png. No saved")

    else:
        return "No screenshot found in the request", 400


if __name__ == "__main__":
    serve(app, host=sys.argv[1], port=sys.argv[2])
