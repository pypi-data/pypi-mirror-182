from setuptools import setup, find_packages
setup(name='pgWitgets',
      version='1.0',
      url='https://github.com/the-gigi/pgWitgets',
      license='MIT',
      author='alexCoder23',
      author_email='alekesybeldem@gmail.com',
      description='pgWitgets',
      packages=find_packages(exclude=['pgWitgets']),
      long_description=open('README.md').read(),
      zip_safe=False)
