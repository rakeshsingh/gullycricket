from gullycricket import app


@app.route('/')
def index():
    return 'Hello Flask'
