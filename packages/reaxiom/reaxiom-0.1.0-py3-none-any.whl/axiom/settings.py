import os
import json
__home = os.environ['HOME']
axiom_hidden_file = os.path.join(__home, '.axiom', 'setting.json')
if not os.path.exists(axiom_hidden_file):
    config = {
        'home': __home,
        'axiom_path': os.path.join(__home, 'reaxiom'),
        'axiom_cache': os.path.join(__home, 'reaxiom', 'cache'),
        'huggingface_cache': os.path.join(__home, 'reaxiom', 'huggingface_cache'),
        'huggingface_obj': 'test_obj',
    }
    json.dump(config, open(axiom_hidden_file, 'w'))
else:
    config = json.load(open(axiom_hidden_file))


