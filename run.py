from application.hello import app
import os

app.run(host=str(os.environ['BIND']), port=int(os.environ['PORT']), debug=True)
