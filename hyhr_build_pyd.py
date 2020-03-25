from distutils.core import setup
from Cython.Build import cythonize
 
setup(
  name = 'hyhr',
  ext_modules = cythonize(['hyhr_ui.py', 'hyhr_encrypt.py', 'hyhr_key.py', 'hyhr_RegisterKey.py']
  ),
)