# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypaystack2', 'pypaystack2.api']

package_data = \
{'': ['*']}

install_requires = \
['mkdocstrings[python]>=0.19.1,<0.20.0', 'requests>=2.28.0,<3.0.0']

setup_kwargs = {
    'name': 'pypaystack2',
    'version': '1.0.2',
    'description': 'A fork of PyPaystack. A simple python wrapper for Paystack API.',
    'long_description': '# PyPaystack2\n\nA fork of [PyPaystack](https://github.com/edwardpopoola/pypaystack). A simple python wrapper for Paystack API.\n\n## Installation\n\n1. Create your [Paystack account](https://paystack.com/) to get your Authorization key that is required to use this package.\n2. Store your authorization key in your environment variable as `PAYSTACK_AUTHORIZATION_KEY` or pass it into the pypaystack api wrappers at instantiation.\n3. Install pypaystack2 package.\n\n```bash\npip install -U pypaystack2\n```\n\n## What\'s Pypaystack2\n\nSo Paystack provides restful API endpoints for developers from different platforms\nto integrate their services into their projects. So for python developers, to use\nthese endpoints, you might opt for a package like `requests` to handle all the\nAPI calls which involves a lot of boilerplate. Pypaystack2 abstracts this process\nby handling all these complexities under the hood and exposing simple APIs for\nyour python project. for example\n\n```python\nfrom pypaystack2.api import Miscellaneous # assumes you have installed pypaystack2\nfrom pypaystack2.utils import Country\nmiscellaneous_wrapper = Miscellaneous() # assumes that your paystack auth key is in \n# your environmental variables i.e. PAYSTACK_AUTHORIZATION_KEY=your_key otherwise instantiate \n# the Miscellaneous API wrapper as it is done below.\n# miscellaneous_wrapper = Miscellaneous(auth_key=your_paystack_auth_key)\nresponse = miscellaneous_wrapper.get_banks(country=Country.NIGERIA,use_cursor=False) # Requires internet connection.\nprint(response)\n```\n\nWith the code snippet above, you have successfully queried Paystack\'s Miscellaneous API\nto get a list of banks supported by paystack. A `requests` equivalent of the above will\nbe like\n\n```python\nimport requests # assumes you have requests installed.\nheaders = {\n  "Content-Type":"application/json",\n  "Authorization": "Bearer <your_auth_key>"\n  }\npaystack_url = \'https://api.paystack.co/bank?perPage=50&country=ng&use_cursor=false\'\nresponse = requests.get(paystack_url,headers=headers) # requires internet connection\nprint(response.json())\n```\n\nWhile both approaches achieve the same goal, `pypaystack2` uses `requests` under the hood and\nmanages the headers and URL routes to endpoints, so you can focus more on the actions. with the `miscellaneous_wrapper`\nin the example above. you can call all endpoints associated with the Miscellaneous API with methods\nprovided like `.get_banks`, `.get_providers`, `.get_countries` and `.get_states`.\n\nPypaystack2 provides wrappers to all of Paystack APIs in its `pypaystack2.api` subpackage.\neach of the wrappers is a python class named to closely match the Paystack API. so say you want\nto use Paystack\'s Invoices API, you\'d  import the wrapper with `from pypaystack2.api import Invoice`\nfor the Invoices API. All endpoints available on the Invoices API are available as methods\nin the `Invoice` wrapper. Say you wanted to create an invoice by sending a\n`POST` request to Paystack\'s Invoice API endpoint `/paymentrequest`, you\'ll call\n`Invoice` wrapper\'s `.create` method.\n\n```python\nfrom pypaystack2.api import Invoice\ninvoice_wrapper = Invoice()\nresponse = invoice_wrapper.create(customer="CUS_xwaj0txjryg393b",amount=1000) # Creates an invoice with a charge of ₦100\n```\n\nFrom here you can check out the tutorials section to get more examples and get familiar or surf the\ndocumentation for wrappers and methods you\'ll need for your next project. Hurray!\n',
    'author': 'Gbenga Adeyi',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
