# Author: Junior Tada
from app import app

# run server
app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)