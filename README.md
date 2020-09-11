# Project Synsets

The project's **goal** is to create a renderer, as a piece of code, that can render a tree written in YAML and using concept references with language namespaces, automatically convert the content to a language of choice. Take a look at the **[idea](https://0oo.li/method/895/default-interlingual-synsets)** and **[plan](https://0oo.li/project/896/project-synsets#)** of the project.

```
git clone git@github.com:wefindx/synsets.git
python -m venv .env && . .env/bin/activate
pip install -r requirements.txt
```
**Translate data/tree.yml to a language:**

`python translate.py [lang]`

**Refresh concept from web:**
`python translate.py refresh [concept_id]`

Delete `.concept` folder to refresh all concepts.
