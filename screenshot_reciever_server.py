from flask import Flask, request
import datetime
import logging
from waitress import serve
import sys

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)


@app.route("/upload-screenshot", methods=["POST"])
def upload_screenshot():
    image_file = request.files.get("screenshot")
    if image_file:
        file_name = "./screenshots/" + request.remote_addr + "_" + str(
            datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")) + ".png"
        image_file.save(file_name)
        return "Screenshot received and saved successfully", 200
    else:
        return "No screenshot found in the request", 400


if __name__ == "__main__":
    serve(app, host=sys.argv[1], port=sys.argv[2])
