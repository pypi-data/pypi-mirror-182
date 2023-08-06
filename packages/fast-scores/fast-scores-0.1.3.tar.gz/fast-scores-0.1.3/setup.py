# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fast_scores']

package_data = \
{'': ['*']}

install_requires = \
['cchardet>=2.1.7,<3.0.0',
 'fastlid>=0.1.9,<0.2.0',
 'joblib>=1.0.1,<2.0.0',
 'logzero>=1.7.0,<2.0.0',
 'msgpack>=1.0.2,<2.0.0',
 'nltk>=3.6.2,<4.0.0',
 'numpy>=1.21.0,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'simplemma>=0.3.0,<0.4.0',
 'sklearn>=0.0,<0.1']

setup_kwargs = {
    'name': 'fast-scores',
    'version': '0.1.3',
    'description': ' ',
    'long_description': '# fast-scores\n[![tests](https://github.com/ffreemt/fast-scores/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/fast_scores.svg)](https://badge.fury.io/py/fast_scores)\n\nCalculate correlatioin matrix fast\n\n## Preinstall fasttext\n\n```\npip install fasttext\n```\n\nFor Windows without a C/C++ compiler:\n* Download a proper whl (e.g., `fasttext‑0.9.2‑cp36‑cp36m‑win_amd64.whl` for 64bits Python 3.6 etc)  from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext)\n```bash\npip install fasttext*.whl\n```\nor (for python 3.8)\n```\npip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/fasttext-0.9.2-cp38-cp38-win_amd64.whl\n```\n## Installation\n```\npip install fast-scores\n```\n\n## Usage\n\n```shell\n# from fast-scores\\tests\\test_gen_cmat.py\n\nfrom fast_scores.gen_cmat import gen_cmat\n\ntext_en = "test this\\nbla bla\\n love"\ntext_zh = "测试\\n 爱\\n吃了吗\\n你好啊"\n\nlist1 = [elm.strip() for elm in text_en.splitlines() if elm.strip()]\nlist2 = [elm.strip() for elm in text_zh.splitlines() if elm.strip()]\n\ncmat = gen_cmat(list1, list2)  # len(list2) x len(list1)\nprint(cmat)\n# [[0.75273851 0.         0.        ]\n#  [0.         0.         0.86848247]\n#  [0.         0.         0.        ]\n#  [0.         0.         0.        ]]\n\nlen_y, len_x = cmat.shape\n\nassert cmat.max() > 0.86  # 0.868\n_ = divmod(cmat.argmax(), len_x)\nassert cmat[_] == cmat.max()\n\n```',
    'author': 'freemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/fast-scores',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
