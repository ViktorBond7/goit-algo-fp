import sys
import os

COMMON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common"))
if COMMON_PATH not in sys.path:
    sys.path.append(COMMON_PATH)
