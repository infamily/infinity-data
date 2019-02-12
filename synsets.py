import yaml
from tqdm import tqdm
from typology import Concept
from utils import ordered_dump

# import multiprocessing

MAX_ID = 60000

def write_concept(i):

    concept_id = 'WD:Q{}'.format(i)

    try:
        concept = Concept(concept_id)

        line = [concept_id] + [
            '{lang_id}:{token}'.format(
                lang_id=key,
                token=concept.aliases[key][0])
            for key in concept.aliases
        ]

        yml = ordered_dump(
            line,
            allow_unicode=True,
            default_flow_style=True,
            Dumper=yaml.SafeDumper)

        f.write('- ' + yml)

    except:
        print('skipping {}'.format(i))


with open('synsets.yml', 'a') as f:

    for i in tqdm(range(1, MAX_ID)):
        write_concept(i)
