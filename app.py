import os
from flask import Flask, send_file, after_this_request
import uuid

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "REST API for LH"


@app.route("/tts/<text>", methods=["GET"])
def tts(text):
    id = uuid.uuid4()
    command = (
        f"echo '{text}' | piper --model en_US-amy-medium --output_file tmp/{id}.wav"
    )
    os.system(command)

    @after_this_request
    def remove_file(response):
        try:
            os.remove(f"tmp/{id}.wav")
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response

    return send_file(f"tmp/{id}.wav", mimetype="audio/wav")


def create_app():
    return app


if __name__ == "__main__":
    app.run(debug=True)
