import waitress
import app
print("waitress")
waitress.serve(app.app, host='0.0.0.0', port=80)