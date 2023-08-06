# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['np_logging']
install_requires = \
['np_config>=0.1,<0.2']

setup_kwargs = {
    'name': 'np-logging',
    'version': '0.2.1',
    'description': 'Pre-configured file, web, and email logging for Mindscope neuropixels projects, repackaging code from AIBS mpeconfig.',
    'long_description': "**For use on internal Allen Institute network**\n\n```\nimport logging\nimport np_logging\n```\n\n`np_logging.setup()` runs automatically on import to add handlers and loggers from a default config,\nthen the built-in python `logging` module can be used as normal.\n\nThe default config provides the loggers `web` and `email`, in addition to the default\n`root` which includes file handlers for `logging.INFO` and `logging.DEBUG`  levels, plus\nconsole logging. \n\nUsage example:\n```\nlogging.getLogger('web').info('test: web server')\nlogging.getLogger('email').info('test: email logger')\nlogging.debug('test: root logger')\n```\n\nBy default, a message is logged reporting the\n      elapsed time and cause of termination. If an exception was raised, the\n      traceback is included.\n\n\n- user configs can be specified according to the python logging [library dict schema](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema)\n\n- the default config is fetched from the\nZooKeeper server `eng-mindscope:2181`\n- configs can be added via ZooNavigator webview:\n  [http://eng-mindscope:8081](http://eng-mindscope:8081)\n- or more conveniently, via an extension for VSCode such as [gaoliang.visual-zookeeper](https://marketplace.visualstudio.com/items?itemName=gaoliang.visual-zookeeper)\n\nZooKeeper configs can be fetched via their path:\n```\ntest_config: dict = np_logging.fetch_zk_config(\n    '/projects/np_logging_test/defaults/logging'\n)\n```\n\nIf the package can't connect to ZooKeeper, it will alert the user and fall back to a\nfile containing a default logging dict.\n\nOnce a logging config dict has been modified as necessary...\n```\ntest_config['handlers']['email_handler']['toaddrs'] = username@alleninstitute.org\n```\nre-run the logging setup with the new config dict:\n```\nnp_logging.setup(\n    config: dict = test_config,\n    project_name = 'test',\n)\n```\n\n- `project_name` should be supplied to use the web logger - if unspecified, the name of the\n  current working directory is used\n- the web log can be viewed at [http://eng-mindscope:8080](http://eng-mindscope:8080)\n\n\n\nOther input arguments to `np_logging.setup()`:\n- `log_at_exit` (default `True`)\n\n    - If `True`, a message is logged when the program terminates, reporting total\n      elapsed time.\n\n- `email_at_exit` (default `False`)\n\n    - If `True`, an email is sent when the program terminates, reporting the\n      elapsed time and cause of termination. If an exception was raised, the\n      traceback is included.\n      \n    - If `logging.error`, the email is only sent if the program terminates via an exception.\n\n",
    'author': 'Ben Hardcastle',
    'author_email': 'ben.hardcastle@alleninstitute.org',
    'maintainer': 'Ben Hardcastle',
    'maintainer_email': 'ben.hardcastle@alleninstitute.org',
    'url': None,
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
