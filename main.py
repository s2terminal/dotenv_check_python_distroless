import os
import pprint

env_sorted = dict(sorted(dict(os.environ).items(), key=lambda kv: kv[0]))
pprint.pp(env_sorted)
