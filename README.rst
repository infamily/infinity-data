Syntrans
========

This toolkit is based on the idea of `Default Interlingual Synsets <https://0oo.li/method/895/default-interlingual-synsets>`_

You can write a hierarchy or graph in a YAML file, using precise concept meaning references from various namespaces of semantic web, notably, `WikiData <https://www.wikidata.org/>`_, automatically them converted into their representations in a language of
choice.

The aim is to continue with introducing default meanings for tokens in languages, so as to convert not to arbitrary first expressions, but to the default expressions for concepts in each language. Since, those default expressions are likely to coincide with the multi-meaning traditional expressions, we want to come up with a way to emphasize default meanings in such texts, perhaps prepending words with a symbol like in the ``examples/test.yml``, though, language references would also be required.


Usage
=====
Install it with ``pip install synsets``, then you can translate YAML documents with keys like in the ``examples`` directory, for example, using WikiData concept IDs with namespace ``WD:`` or other namespaces supported by `Metawiki
<https://github.com/wefindx/metawiki/>`_ package.

::

    syntrans -h
    usage: syntrans [-h] [-c CONCEPT] [-s SOURCE] [-l LANGUAGE] [-r REFRESH]

    optional arguments:
      -h, --help            show this help message and exit
      -s SOURCE, --source SOURCE
                            Source text file to parse.
      -l LANGUAGE, --language LANGUAGE
                            Language reference, e.g., en, lt, ja, ru, cn.
      -r CONCEPT, --concept CONCEPT
                            Single concept to refresh cache from source.

For example, let's translate the sample text.

Example source:

::

    $ cat examples/sample.yml
    WD:Q4503831:
      - WD:Q1156970 WD:Q7949 WD:Q8 WD:Q245962
      - WD:Q1378301 WD:Q3 WD:Q15290 WD:Q185957 WD:Q468777 WD:Q245962

Example to English:

::

    $ syntrans -s examples/sample.yml -l en

    goal:
    - humanity • truth • happiness • implementation
      - universal set • life • good • quality • existence • implementation

Example to Japanese:

::

    syntrans -s examples/sample.yml -l ja

    目標:
    - 人類 • 真理 • 幸福 • 実装
      - 普遍集合 • 生命 • 善 • 品質 • 存在 • 実装

Refresh concept from web:

``syntrans -r WD:Q1156970``

Delete ``.concept`` folder to refresh all cached concepts.
