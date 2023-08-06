# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['ghost_pwa']
setup_kwargs = {
    'name': 'ghost-pwa',
    'version': '1.2.0',
    'description': '',
    'long_description': '# Ghost Theme PWA\n\nThis theme enables you to "Install" your site as a Progressive Web App.\n\nRequires either Chrome or Firefox to install the app.\n\nBrowsing works better with Chrome. Editing works better with Firefox.\n\n## Unpacked theme\n\nApply to an existing theme:\n\n1. `cd` to the theme dir,\n2. Copy `make_pwa` to the dir,\n3. Run `make_pwa/make_pwa`,\n4. Pack the directory, excluding the `make_pwa` folder.\n    - Example: `zip -r casper-pwa.zip --exclude=make_pwa *`\n5. In the example above, `casper-pwa.zip` is the output theme archive.\n\n## Theme ZIP\n\nIf you just have a ZIP archive, run:\n\n```\n$ make_pwa <archive file>\n```\n\nExample:\n\n```\n$ make_pwa Casper-3.0.7.zip\n```\n\nThe output is:\n\n```\n$ ls\nCasper-3.0.7-PWA.zip\n```\n\n## Verifying\n\nTest your PWA here: https://www.seochecker.it/pwa-tester-online\n\n## Use online\n\nTo use this online, you can open a notebook in Google Colab and apply the steps\ndescribed above.\n\nDownload a ZIP file with your current theme. Next, upload it to Colab. Finally,\nrun the script on the ZIP file, and download the result. Voila! You can now\nupload the PWA ZIP file to your Ghost installation.\n\nNotebook example (sketch - work in progress): https://colab.research.google.com/drive/1cPrGzrS15Nz_7OhIt8Y8FfOD_wqM0H67#scrollTo=Usage\n',
    'author': 'Patryk Kocielnik',
    'author_email': 'patryk@kocielnik.pl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
