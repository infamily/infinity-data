import os
import re
import sys
import yaml
import argparse, pathlib

from typology import Concept
from boltons.iterutils import remap
from syntrans.utils import ordered_load
from syntrans.utils import ordered_dump


def concept(concept_id, refresh=False, folder='.concept'):
    '''
    Since we only use concept's aliases, save them to files in .concept folder.
    '''

    def save(concept_id, folder='.concept'):
        '''
        upserts concept to local database at folder
        '''
        if not os.path.exists(folder):
            os.makedirs(folder)

        try:
            _concept = Concept(concept_id)
        except:
            raise Warning('Could not retrieve concept.')
        _concept.aliases['__id__'] = _concept.id
        _concept.aliases['__url__'] = _concept.url
        with open('{}/{}'.format(folder, concept_id), 'w') as f:
            f.write(yaml.dump(_concept.aliases, allow_unicode=True, default_flow_style=False))

    if not os.path.exists('{}/{}'.format('.concept', concept_id)) or refresh:
        save(concept_id)
        print('GET: ', concept_id)

    item = yaml.load(open('{}/{}'.format(folder, concept_id), 'r').read(), Loader=yaml.Loader)
    return item

def conceptualize(string):
    '''
    Sentence is a list of concepts start and end symbols.
    '''
    def split_words(s):
        return re.split(', |,| ,| ', s)

    concept_list = []

    for word in split_words(string):
        _concept = concept(word)
        concept_list.append(_concept)

    return concept_list

def represent(meaning, lang):
    '''
    Represent the meaning in target language.
    '''
    representations = []
    for _concept in meaning:
        name = _concept.get(lang)
        if name is not None:
            if isinstance(name, list):
                name = name[0]
            name = '{}'.format(name)
        else:
            name = _concept['__id__']

        representations.append(name)

    return ' • '.join(representations)

def translate(data, lang):
    '''
    Go over strings in data structure, and represent them in language of choice.
    '''

    def visit(path, key, value):
        if isinstance(key, str):
            key_meaning = conceptualize(key)
            key = represent(key_meaning, lang)
        if isinstance(value, str):
            value_meaning = conceptualize(value)
            value = represent(value_meaning, lang)
        return key, value

    remapped = remap(data, visit=visit)
    return remapped


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='Source text file to parse.')
    parser.add_argument('-l', '--language', help='Language reference, e.g., en, lt, ja, ru, cn.')
    parser.add_argument('-r', '--refresh', help='Pass non-null to refresh.')
    args = parser.parse_args()

    CWD = pathlib.Path(os.getcwd())
    LANGUAGE = args.language or 'en'
    CONCEPT = args.refresh

    SOURCE = args.source
    if args.source:
        s = pathlib.Path(SOURCE)
        if s.expanduser() == s and not str(s).startswith(s._flavour.sep):
            s = pathlib.Path(os.path.join(CWD, s))
            SOURCE = s

    if CONCEPT:
        concept(CONCEPT, refresh=True)
        print('Done.')

    elif SOURCE:
        data = ordered_load(open(SOURCE, 'r'), yaml.SafeLoader)
        translation = translate(data, LANGUAGE)

        print(
            ordered_dump(
                translation, allow_unicode=True, default_flow_style=False, Dumper=yaml.SafeDumper))



if __name__ == '__main__':
    main()
