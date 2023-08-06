# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_chartjs']

package_data = \
{'': ['*']}

install_requires = \
['flask>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'flask-chartjs-manager',
    'version': '0.1.2',
    'description': '',
    'long_description': '# Flask-ChartJS\n\nFlask-ChartJS provides a simple interface to use ChartJS javascript library with Flask.\n\n## Installation\n\nInstall the extension with pip:\n\n```bash\npip install flask-chartjs\n```\n\n## Usage\n\nOnce installed the Flask-ChartJS is easy to use.Let\'s walk through setting up a basic application. Also please note that this is a very basic guide: we will be taking shortcuts here that you should never take in a real application.\n\nTo begin we\'ll set up a Flask app:\n\n```python\nimport flask\n\napp = flask.Flask(**name**)\n```\n\nFlask-ChartJS works via a ChartJS object. To kick things off, we\'ll set up the login manager by instantiating it and telling it about our Flask app:\n\n```python\nfrom flask_chartjs import ChartJS\n\nchartjs = ChartJS()\nchartjs.init_app(app)\n```\n\nThis will make available the `load_chartjs` function into the templates context so you could load the javascript package easily, like this.\n\n```html\n<head>\n  {{ load_chartjs() }}\n</head>\n```\n\nNow we will construct a basic chart.\n\n```python\nfrom flask_chartjs import Chart, DataSet\nfrom flask import render_template\n\n@app.get(\'/chart-example\')\ndef chart_example():\n    chart = Chart(\'income-outcome\', \'bar\') # Requires at least an ID and a chart type.\n    dataset_income = DataSet(\'Income\', [100,200,300])\n    dataset_outcome = DataSet(\'OutCome\', [50,100,150])\n    chart.data.add_labels(\'jan\', \'feb\', \'mar\')\n    chart.data.add_dataset(dataset_income)\n    chart.data.add_dataset(dataset_outcome)\n\n    return render_template(\'path/to/template.html\', my_chart=chart)\n\n```\n\nOnce created you can pass it to a render_template and use it likewise.\n\n```html\n<!-- load_chartjs() must be called before this line -->\n<div class="my-classes">{{ my_chart() }}</div>\n```\n',
    'author': 'Sebastian Salinas',
    'author_email': 'seba.salinas.delrio@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
