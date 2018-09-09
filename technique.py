import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask_socketio import SocketIO, send, emit

UPLOAD_FOLDER = '/Users/youngyona/PycharmProjects/technique/tmp'
ALLOWED_EXTENSIONS = set(['mp4'])

template_dir = "/Users/youngyona/PycharmProjects/technique/client/templates"

static_dir = "/Users/youngyona/PycharmProjects/technique/client/static"

print(template_dir)
print(static_dir)
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
socketio = SocketIO(app)

state = "ready"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'front' not in request.files:
            flash('No file part')
            return redirect(request.url)
        front = request.files['front']
        # if user does not select file, browser also
        # submit an empty part without filename
        if front.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if front and allowed_file(front.filename):
            front.filename = "front.mp4"
            front.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(front.filename)))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename_front))

        if 'side' not in request.files:
            flash('No file part')
            return redirect(request.url)
        side = request.files['side']
        # if user does not select file, browser also
        # submit an empty part without filename
        if side.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if side and allowed_file(side.filename):
            side.filename = "side.mp4"
            side.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(side.filename)))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename_side))

    return render_template('home.html')


# @app.route('/uploads/<filename>')
# def uploaded_file(filename_front):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename_front)


@app.route('/ready', methods=['GET', 'POST'])
def standby():
    return render_template('ready.html')


@socketio.on('alert_button')
def handle_alert_event(json):
    emit('alert', "video is processing")
    # it will forward the json to all clients.
    print('received json: {0}'.format(str(json)))
    return render_template('process.html')


if __name__ == '__main__':
    app.run()
    socketio.run(app)
