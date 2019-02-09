# infinity-data

`git clone git@github.com:infamily/infinity-data.git`
`virtualenv -ppython3 .env && . .env/bin/activate`
`pip install -r requirements.txt`

## Translate data/tree.yml to a language:

`python translate.py [lang]`

## Refresh concept from web:
`python translate.py refresh [concept_id]`

Delete `.concept` folder to refresh all concepts.
