from setuptools import setup, find_packages

setup(name='something_with_pokemon',
      version='0.0',
      description='Pokemon thing',
      packages=find_packages(exclude=['something_with_pokemon']),
      author_email='cstawer2005@mail.ru',
      zip_safe=False)
