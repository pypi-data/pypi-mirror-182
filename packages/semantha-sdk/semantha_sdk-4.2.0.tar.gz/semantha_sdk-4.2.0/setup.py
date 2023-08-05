# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['semantha_sdk',
 'semantha_sdk.api',
 'semantha_sdk.model',
 'semantha_sdk.request',
 'semantha_sdk.response',
 'semantha_sdk.rest']

package_data = \
{'': ['*']}

install_requires = \
['requests==2.28.1']

setup_kwargs = {
    'name': 'semantha-sdk',
    'version': '4.2.0',
    'description': 'This is a python client sdk for accessing semantha (the semantic platform)',
    'long_description': '![](https://www.semantha.de/wp-content/uploads/semantha-inverted.svg)\n\n# semantha® SDK\n\nThe semantha SDK is a high-level REST client to access the [semantha](http://semantha.ai) API.\nThe SDK is still under development.\nAn overview of the current progress (i.e. implemented and tested resources and endpoints) may be found at the end of this document (State of Development).\n\n### Disclaimer\n**IMPORTANT:** The SDK is under development and interfaces may change at any time without notice. Use with caution and on own risk.\n\n### Access\nTo access semantha\'s API you will need an API and a server url.\nBoth can be requested via [this contact form](https://www.semantha.de/request/).\n\n\n\n### Basic Usage\n\n#### Import\n```\nimport semantha_sdk\n```\n#### Authentication\n```\nsemantha = semantha_sdk.login(url="<semantha platform server URL>", key="<your key>")\n# or\nsemantha = semantha_sdk.login(url="<semantha platform server URL>", key_file="<path to your key file (json format)>")\n```\n#### End-point Access\n```\n# end-points (resp. resources) can be used like objects\ncurrent_user = semantha.current_user\nmy_domain = semantha.domains.get_one("my_domain")\n\n# they may have sub-resources, which can be retrieved as objects as well\nreference_documents = my_domains.reference_documents\n```\n#### CRUD on End-points\n```\n# CRUD operations are functions\ndomain_settings = my_domain.get_settings()\nmy_domain.reference_documents.delete_all()\n```\n#### Function Return Types & semantha Data Model\n```\n# some functions only return None, e.g.\nmy_domain.reference_documents.delete_all() # returns NoneType\n\n# others return built in types, e.g\nroles_list = current_user.get_user_roles() # returns list[str]\n\n# but most return objects of the semantha Data Model\n# (all returned objects are instances of frozen dataclasses)\nsettings = my_domain.get_settings() # returns instance of DomainSettings\n# attributes can be accessed as properties, e.g.\nsettings.enable_tagging # returns true or false\n# Data Model objects may be complex\ndocument = my_domain.references.post(file=a, reference_document=b) # returns instance of Document\n# the following returns the similarity value of the first references of the first sentence of the\n# the first paragraph on the first page of the document (if a reference was found for this sentence)\nsimilarity = pages[0].contents[0].paragraphs[0].references[0].similarity # returns float\n```\n\n### State of Development\nThe following resources and end-points are fully functional and (partially) tested:\nCurrentUser\n* get_user_data\n* get_user_roles\n\nDomains\n* get_all\n* get_one --> returns sub-resource Domain\n\t* get_configuration\n\t* get_settings\n\t* References\n\t\t* post\n\t* ReferenceDocuments\n\t\t* get_all\n\t\t* get_one\n\t\t* delete_all\n\t\t* delete_one\n\t\t* post\n\t\t* get_paragraph\n\t\t* delete_paragraph\n\t\t* get_sentence\n\t\t* get_named_entities\n\t\t* get_statistic\n\nModel/Domains\n* get_one --> returns sub-resource DomainModel\n\t* Boostwords\n\t\t* get_all\n\t\t* get_one\n\t\t* delete_all\n\t\t* get_one\n',
    'author': 'Tom Kaminski',
    'author_email': 'tom.kaminski@semantha.de',
    'maintainer': 'semantha support',
    'maintainer_email': 'support@semantha.de',
    'url': 'https://semantha.de',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
