# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hydrogym',
 'hydrogym.distributed',
 'hydrogym.firedrake',
 'hydrogym.firedrake.envs',
 'hydrogym.firedrake.envs.cavity',
 'hydrogym.firedrake.envs.cylinder',
 'hydrogym.firedrake.envs.pinball',
 'hydrogym.firedrake.envs.step',
 'hydrogym.firedrake.utils']

package_data = \
{'': ['*']}

install_requires = \
['control>=0.9.2,<0.10.0',
 'dmsuite>=0.1.1,<0.2.0',
 'evotorch>=0.3.0,<0.4.0',
 'gmsh>=4.11.1,<5.0.0',
 'gym>=0.26.2,<0.27.0',
 'modred>=2.1.0,<3.0.0',
 'torch==1.13']

setup_kwargs = {
    'name': 'hydrogym',
    'version': '0.1.2.1',
    'description': 'A Reinforcement Learning Benchmarking Environment for Fluid Dynamics',
    'long_description': '<p align="center">\n\t<a rel="nofollow">\t\n\t\t<img src="docs/source/_static/imgs/logo.svg" />\n\t</a>\n</p>\n\n# About this Package\n\nHydroGym is an open-source library of challenge problems in data-driven modeling and control of fluid dynamics.\n\n## Features\n* __Hierarchical:__ Designed for analysis and controller design **from a high-level black-box interface to low-level operator access**\n    - High-level: `hydrogym.env.FlowEnv` classes implement the OpenAI `gym.Env` interface\n    - Intermediate: Typical CFD interface with `hydrogym.FlowConfig` and `hydrogym.TransientSolver` classes\n    - Low-level: Access to linearized operators and sparse scipy or PETSc CSR matrices\n* __Modeling and anlysis tools:__ Global stability analysis (via SLEPc) and modal decompositions (via modred)\n* __Scalable:__ Individual environments parallelized with MPI with a **highly scalable [Ray](https://github.com/ray-project/ray) backend reinforcement learning training**.\n\n# Installation\n\nTo begin using Hydrogym we can install its latest release via [PyPI](https://pypi.org/project/hydrogym/) with pip\n\n```bash\npip install hydrogym\n```\n\nwhich provides the core functionality, and is able to launch reinforcement learning training on a Ray-cluster without an underlying Firedrake install. If you want to play around with Hydrogym locally on e.g. your laptop, we recommend a local Firedrake install. The instructions for which can be found in the [Installation Docs](https://hydrogym.readthedocs.io/en/latest/installation.html).\n\n# Quickstart Guide\n\n Having installed Hydrogym into our virtual environment experimenting with Hydrogym is as easy as starting the Python interpreter\n \n ```bash\n python\n ```\n \n and then setting up a Hydrogym environment instance\n \n```python\nimport hydrogym as hgym\nenv = hgym.env.CylEnv(Re=100) # Cylinder wake flow configuration\nfor i in range(num_steps):\n    action = 0.0   # Put your control law here\n    (lift, drag), reward, done, info = env.step(action)\n```\n\nTo test that you can run individual environment instances in a multithreaded fashion, run the steady-state Newton solver on the cylinder wake with 4 processors:\n\n```bash\ncd /path/to/hydrogym/examples/cylinder\nmpiexec -np 4 python pd-control.py\n```\n\nFor more detail, check out:\n\n* A quick tour of features in `notebooks/overview.ipynb`\n* Example codes for various simulation, modeling, and control tasks in `examples`\n* The [ReadTheDocs](https://hydrogym.readthedocs.io/en/latest/)\n\n# Flow configurations\n\nThere are currently a number of main flow configurations, the most prominent of which are:\n\n- Periodic cyclinder wake at Re=100\n- Chaotic pinball at Re=130\n- Open cavity at Re=7500\n\nwith visualizations of the flow configurations available in the [docs](docs/FlowConfigurations.md).\n',
    'author': 'Jared Callaham et al.',
    'author_email': 'None',
    'maintainer': 'Jared Callaham',
    'maintainer_email': 'jared.callaham@gmail.com',
    'url': 'https://github.com/dynamicslab/hydrogym',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
