from setup import create_app

import os
import sys
from inspect import getsourcefile

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
root_dir = os.path.join(current_dir, os.pardir)
sys.path.append(root_dir)


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)