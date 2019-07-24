from app import app # assumption: a Flask instance app is created in __init__.py of the app package

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # ip address for running in Docker container
    # default ip is localhost, this does not work inside a container
