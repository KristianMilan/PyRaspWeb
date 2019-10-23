# Author: Junior Tada
from app import app
import sys

# run server
try:
	app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
except KeyboardInterrupt:
	print('\nHasta la vista baby!')
	sys.exit(0)