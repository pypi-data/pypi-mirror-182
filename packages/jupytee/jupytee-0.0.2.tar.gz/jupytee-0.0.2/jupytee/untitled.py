"""Magics to support ChatGPT interactions in IPython/Jupyter.
"""

__version__ = "0.0.1"

from .jupytee import 

def load_ipython_extension(ipython):
    ipython.register_magics(Abracadabra)