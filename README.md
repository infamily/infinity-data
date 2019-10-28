# Project Synsets

The project's **goal** is to create a renderer, as a piece of code, that can render a tree written in YAML and using concept references with language namespaces, automatically convert the content to a language of choice. Take a look at the **[idea](https://infty.xyz/#/en/@/topic/895)** and **[plan](https://dynalist.io/d/_OLqWbcscbx5xGq2SpOTiu3d)** of the project.

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
