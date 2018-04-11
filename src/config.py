import os
import sys


BOT_TOKEN = ""

ROOT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

INLINE_QUERY_VARIANTS_DIR = os.path.join(DATA_DIR, 'inline_query_variants')
