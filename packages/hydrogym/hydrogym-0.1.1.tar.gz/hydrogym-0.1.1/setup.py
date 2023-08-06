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
    'version': '0.1.1',
    'description': 'A Reinforcement Learning Benchmarking Environment for Fluid Dynamics',
    'long_description': '<p align="center">\n\t<a rel="nofollow">\t\n\t\t<img src="docs/source/_static/imgs/logo.svg" />\n\t</a>\n</p>\n\n\nHydroGym provides is an open-source library of challenge problems in data-driven modeling and control of fluid dynamics.\n\n### Features\n* __Hierarchical:__ Designed for analysis and controller design from a high-level black-box interface to low-level operator access\n    - High-level: `hydrogym.env.FlowEnv` classes implement the OpenAI `gym.Env` interface\n    - Intermediate: Typical CFD interface with `hydrogym.FlowConfig` and `hydrogym.TransientSolver` classes\n    - Low-level: Access to linearized operators and sparse scipy or PETSc CSR matrices\n* __Differentiable:__ Adjoint-enabled for PDE-constrained optimization via pyadjoint (extensible to PyTorch, Jax, etc... planned for future)\n* __Modeling and anlysis tools:__ Global stability analysis (via SLEPc) and modal decompositions (via modred)\n* __Scalable:__ Since linear algebra backend is PETSc, fully parallelized with MPI (including pyadjoint, SLEPc, modred)\n\n# Quick Start\n\nTo begin using Hydrogym we need to first recursively clone the Hydrogym repository\n\n```bash\ngit clone --recursive https://github.com/dynamicslab/hydrogym.git\n```\n\nAfter which we can build the package with its dependencies with\n\n```bash\npython old_setup.py build_ext\n```\n\nby default it will build with Firedrake as its simulation engine. With our wheel built, we then only need to install it\n\n```bash\npip install .\n```\n\nwith which we then have the latest version of Hydrogym, and all of its dependencies inside of the virtualenv, installed.\n\n```bash\nsource $VENV/bin/activate\n```\n\nIf you try to run something and get an error like "python: command not found" you probably missed this step.\n\nThen you can get running in the interpreter as easy as:\n\n\n```python\nimport hydrogym as gym\nenv = gym.env.CylEnv(Re=100) # Cylinder wake flow configuration\nfor i in range(num_steps):\n\taction = 0.0   # Put your control law here\n    (lift, drag), reward, done, info = env.step(action)\n```\n\nOr to test that you can run things in parallel, try to run the steady-state Newton solver on the cylinder wake with 4 processors:\n\n```bash\ncd /home/hydrogym/examples/cylinder\nmpiexec -np 4 python solve-steady.py\n```\n\nFor more detail, check out:\n\n* A quick tour of features in `notebooks/overview.ipynb`\n* Example codes for various simulation, modeling, and control tasks in `examples`\n\n# Flow configurations\n\nThere are currently a number of main flow configurations, the most prominent of which are:\n\n- Periodic cyclinder wake at Re=100\n- Chaotic pinball at Re=130\n- Open cavity at Re=7500\n\nwith visualizations of the flow configurations available in the [docs](docs/FlowConfigurations.md). For the time being the cylinder wake is the most well-developed flow configuration, although the pinball should also be pretty reliable.  The cavity is in development (the boundary conditions are a little iffy and there\'s no actuation implemented yet) and the backwards-facing step is still planned.\n',
    'author': 'Jared Callaham',
    'author_email': 'jared.callaham@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dynamicslab/hydrogym',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
