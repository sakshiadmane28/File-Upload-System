from flask import Flask, render_template, request
import boto3
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

BUCKET_NAME = "YOUR-BUCKET-NAME"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "txt", "docx"}
s3 = boto3.client("s3")


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = ""

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            message = "Please choose a file."
        elif not allowed_file(file.filename):
            message = "Allowed: PDF, PNG, JPG, TXT and DOCX."
        else:
            filename = secure_filename(file.filename)
            try:
                s3.upload_fileobj(
                    file,
                    BUCKET_NAME,
                    filename,
                    ExtraArgs={
                        "ContentType": file.content_type
                        or "application/octet-stream"
                    },
                )
                message = f"{filename} uploaded successfully."
            except ClientError as error:
                code = error.response["Error"]["Code"]
                message = f"Upload failed. AWS error: {code}"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
