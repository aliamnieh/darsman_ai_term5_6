# main.py

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui_folder'))

from ui import ui  

def main():
    ui.run()  

if __name__ == "__main__":
    main()
