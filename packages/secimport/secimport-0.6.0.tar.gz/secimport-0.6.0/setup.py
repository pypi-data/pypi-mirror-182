# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['secimport',
 'secimport.backends.bpftrace_backend',
 'secimport.backends.common',
 'secimport.backends.dtrace_backend']

package_data = \
{'': ['*'],
 'secimport': ['profiles/*'],
 'secimport.backends.bpftrace_backend': ['actions/*', 'filters/*', 'probes/*'],
 'secimport.backends.dtrace_backend': ['actions/*',
                                       'filters/*',
                                       'headers/*',
                                       'probes/*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'fire>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['secimport = secimport.cli:main']}

setup_kwargs = {
    'name': 'secimport',
    'version': '0.6.0',
    'description': 'A sandbox/supervisor for python modules.',
    'long_description': '# secimport\nA sandbox that grants privilleges per module in your code, making 3rd pary and open source and untrusted code to run in trusted environments.<br>\nIt does using backends like bpftrace (eBPF) and dtrace under the hood.<br>\n<p align="center">\n<a href="https://infosecwriteups.com/sandboxing-python-modules-in-your-code-1e590d71fc26?source=friends_link&sk=5e9a2fa4d4921af0ec94f175f7ee49f9">Medium Article</a>\n</p>\n<p align="center">\n <a href="https://github.com/avilum/secimport"><img style="max-height: 100px" src="https://user-images.githubusercontent.com/19243302/177835749-6aec7200-718e-431a-9ab5-c83c6f68565e.png" alt="secimport"></a>\n</p>\n\n# How is works?\n`secimport` uses USDT (Userland Statically Defined Tracing) probes in the runtime (Python interpreter for example). OS kernel using eBPF and dtrace instrumentation scripts.<br>\nYou can use `secimport` to:\n- Trace which syscalls are called by each module in your code, or by your entire application.\n- Restrict specific modules/packages inside your production environment like 3rd party, open source or code from untrusted source.\n- Audit the flow of your python application at user-space/os/kernel level.\n- Kill or audit upon violoation of your specified behavior. Killing is optional.\n<br><br>\n# Quick Start\nThere are several methods to create and run a sandbox:\n1. By modifying your imports\n    - Inside your code using `module = secimport.secure_import(\'module_name\', ...)`.\n      - Replacing the regular `import` statement with `secure_import`\n      - Only modules that were imported with `secure_import` will be traced.\n2. By running it as a parent process for your application\n      -  Generate a YAML policy from your code, by specifying the modules and the policy you want, for every module that you would like to restrict in any way.\n         - Convert that YAML policy to dscript/bpftrace sandbox code.\n      - Run you tailor-made sandbox\n          - Use `dtrace` or `bpftrace` to run your main python application, with your tailor-made sandbox.\n          - No need for `secure_import`, you can keep using regular `import`s and not change your code at all.\n<br><br>\n# Docker\nThe easiest way to try secimport is by using our <a href="docker/README.md">Docker for MacOS and Linux</a>. It includes python, secimport and bpftrace backend.<br>\n`dtrace` backend is not available in docker, and can be tried directly on the compatible hosts ( <a href="docs/MAC_OS_USERS.md">Mac OS</a> , Windows, Solaris, Unix, some Linux distributions).\n<br><br>\n\n# References:\n- Read about the available backends in secimport:\n  - https://www.brendangregg.com/DTrace/DTrace-cheatsheet.pdf\n    - `dtrace`\n  - https://www.brendangregg.com/blog/2018-10-08/dtrace-for-linux-2018.html\n    - `bpftrace` (dtrace 2.0) that uses LLVM and compiled our script to BCC.\n       - https://github.com/iovisor/bpftrace\n- <a href="docs/EXAMPLES.md">Examples</a>\n\n- Guides\n  - <a href="docs/TRACING_PROCESSES.md">Tracing Processes Guide</a>\n  - <a href="docs/INSTALL.md">Installation</a>\n  - <a href="docs/MAC_OS_USERS.md">Mac OS Users</a> - Disabling SIP (System Intergity Protection)\n  - <a href="docs/FAQ.md">F.A.Q</a>\n  <br><br>\n\n\n# Example Use Cases\n<a href="docs/EXAMPLES.md">EXAMPLES.md</a> contains advanced usage and many interactive session examples: YAML profies, networking, filesystem, processing blocking & more.\n\n## Simple Usage\n- <a href="examples/python_imports/">Running Sandbox Using Python Imports</a>\n- <a href="docs/CLI.md">`secimport` CLI usage</a>\n    - The easiest option to start with inside docker.\n    - `python -m secimport.cli --help`\n- See <a href="YAML_PROFILES.md">YAML Profiles Usage</a>>\n<br><br>\n### How pickle can be exploited in your 3rd party packages (and how to block it)\n```python\n# Not your code, but you load and run it frmo 3rd some party package.\n\nimport pickle\nclass Demo:\n    def __reduce__(self):\n        return (eval, ("__import__(\'os\').system(\'echo Exploited!\')",))\n \npickle.dumps(Demo())\nb"\\x80\\x04\\x95F\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x8c\\x08builtins\\x94\\x8c\\x04eval\\x94\\x93\\x94\\x8c*__import__(\'os\').system(\'echo Exploited!\')\\x94\\x85\\x94R\\x94."\n\n# Your code, at some day...\npickle.loads(b"\\x80\\x04\\x95F\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x8c\\x08builtins\\x94\\x8c\\x04eval\\x94\\x93\\x94\\x8c*__import__(\'os\').system(\'echo Exploited!\')\\x94\\x85\\x94R\\x94.")\nExploited!\n0\n```\nWith `secimport`, you can control such action to do whatever you want:\n```python\nimport secimport\npickle = secimport.secure_import("pickle")\npickle.loads(b"\\x80\\x04\\x95F\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x8c\\x08builtins\\x94\\x8c\\x04eval\\x94\\x93\\x94\\x8c*__import__(\'os\').system(\'echo Exploited!\')\\x94\\x85\\x94R\\x94.")\n\n[1]    28027 killed     ipython\n```\nA log file is automatically created, containing everything you need to know:\n```\n$ less /tmp/.secimport/sandbox_pickle.log\n\n  @posix_spawn from /Users/avilumelsky/Downloads/Python-3.10.0/Lib/threading.py\n    DETECTED SHELL:\n        depth=8\n        sandboxed_depth=0\n        sandboxed_module=/Users/avilumelsky/Downloads/Python-3.10.0/Lib/pickle.py  \n\n    TERMINATING SHELL:\n        libsystem_kernel.dylib`__posix_spawn+0xa\n        ...\n                libsystem_kernel.dylib`__posix_spawn+0xa\n                libsystem_c.dylib`system+0x18b\n                python.exe`os_system+0xb3\n    KILLED\n:\n```\nMore examples are available at <a href="docs/EXAMPLES.md">EXAMPLES.md</a>.\n\n<br><br>\n# Roadmap\n- ✔️ Allow/Block list configuration\n- ✔️ Create a .yaml configuration per module in the code\n  - ✔️ Use secimport to compile that yml\n  - ✔️ Create a single dcript policy\n  - ✔️ Run an application with that policy using dtrace, without using `secure_import`\n- ✔️ <b>Add eBPF basic support using bpftrace</b>\n  - ✔️ bpftrace backend tests\n- <b>Extandible Language Template</b>\n  - Implement bpftrace probes for new languages\n- <b>Go support</b> (bpftrace/dtrace hooks)\n  - Implement a template for golang\'s call stack\n- <b>Node support</b> (bpftrace/dtrace hooks)\n  - Implement a template for Node\'s call stack and event loop\n- Multi Process support: Use current_module_str together with thread ID to distinguish between events in different processes\n- Update all linux syscalls in the templates (filesystem, networking, processing) to improve the sandbox blocking of unknowns.\n',
    'author': 'Avi Lumelsky',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/avilum/secimport',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
