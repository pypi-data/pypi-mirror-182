# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['synonym_cli']

package_data = \
{'': ['*']}

install_requires = \
['gazpacho>=1.1,<2.0',
 'importlib-metadata>=5.2.0,<6.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['syn = synonym_cli.__main__:cli']}

setup_kwargs = {
    'name': 'synonym-cli',
    'version': '0.1.0',
    'description': 'Synonyms and antonyms of words from Thesaurus are now in your terminal, with rich output.',
    'long_description': '![screenshot](https://user-images.githubusercontent.com/16024979/162848437-8da9d5d4-a234-44d3-94d8-048f92b015a6.png)\n\n<div align="center">\n<a alt="Github" href="https://github.com/agmmnn/synonym-cli"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/synonym-cli"></a>\n<a href="https://pypi.org/project/synonym-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/synonym-cli"></a>\n</div>\n\n# synonym-cli\n\n<div align="center">\n\nSynonyms and antonyms of words from [Thesaurus.com](https://www.thesaurus.com/) and other sources are now in your terminal, with [rich](https://github.com/Textualize/rich) output.\n\n</div>\n\n# Install:\n\n```\npip install synonym-cli\n```\n\n## Usage:\n\n```\nsyn <word>\n```\n\n```\n$ syn nominate\n┌──────────────────────────────────────────────────────────────────────────────────┐\n│ ❯ designate, select (verb)                                                       │\n├──────────────────────────────────────────────────────────────────────────────────┤\n│ 🔵synonyms: appoint, assign, choose, decide, draft, elect, elevate, name,        │\n│ present, propose, recommend, submit, suggest, tap, call, commission, denominate, │\n│ empower, intend, make, mean, offer, proffer, purpose, slate, slot, specify,      │\n│ tender, term, cognominate, put down for, put up, tab                             │\n│                                                                                  │\n│ 🟤antonyms: condemn, dissuade, ignore, refuse, reject, deny, discourage, stop,   │\n│ take back, pass over                                                             │\n└──────────────────────────────────────────────────────────────────────────────────┘\n\n```\n\n## Different Languages `--lang`, `-l`\n\nMulti-language support with Thesaurus AlterVista. API key is required, if you don\'t have any apikey yet, get a free key from, [thesaurus.altervista.org/openapi](https://thesaurus.altervista.org/openapi).\n\n```\n$ syn -l es expresión\n╭─┬──────────────────────────────────┬─┬──────────────────────────────────╮\n│-│elocución, dicción, estilo        │-│exteriorización, manifestación,   │\n│ │                                  │ │revelación, comunicación          │\n│-│gesto, rostro, cara, semblante,   │-│locución, frase, dicho, giro      │\n│ │aire, aspecto                     │ │                                  │\n╰─┴──────────────────────────────────┴─┴──────────────────────────────────╯\n\n$ syn -l ru фраза\n╭─────────┬────────────────────────────────────────┬────────────────┬─────╮\n│(синоним)│речь, слово, предложение, спич, тост,   │(сходный термин)│слово│\n│         │здравица, аллокуция, диатриба, рацея,   │                │     │\n│         │тирада, филиппика, изложение, слог,     │                │     │\n│         │стиль, перо                             │                │     │\n╰─────────┴────────────────────────────────────────┴────────────────┴─────╯\n```\n\n> AlterVista\'s Thesaurus API supports the following languages:\n\n> Czech: `cs`, Danish: `da`, English (US): `en`, French: `fr`, German (Germany): `de`, German (Switzerland): `de`, Greek: `el`, Hungarian: `hu`, Italian: `it`, Norwegian: `no`, Polish: `pl`, Portuguese: `pt`, Romanian: `ro`, Russian: `ru`, Slovak: `sk`, Spanish: `es`.\n\n### Set Default Language\n\nYou can set the default language with the `--setlang <lang_code>` argument, so you don\'t have to give the `-l` argument every time.\n\n```\n$ syn --setlang fr\n$ syn belle\n╭──────────────┬──────────────────────────────────────────────────────────╮\n│(Adjectif Nom)│adorable, admirable, brillante, charmante, céleste,       │\n│              │délicate, divine, délicieuse, éblouissante, élégante,     │\n│              │éclatante, exquise, féerique, harmonieuse, agréable,      │\n│              │ajustée, accordée, équilibrée, eurythmique, mélodieuse,   │\n│              │musicale, ordonnée, proportionnée, symétrique             │\n╰──────────────┴──────────────────────────────────────────────────────────╯\n```\n\n## Arguments\n\n```\n  -h, --help      show this help message and exit\n  -p, --plain     returns plain text output\n  -l, --lang      <language>\n  --setkey        set apikey for altervista api\n  --setlang       set default language (currently default is \'en\')\n  --show          show settings file\n  -v, --version   show program\'s version number and exit\n```\n',
    'author': 'agmmnn',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/agmmnn/synonym-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
