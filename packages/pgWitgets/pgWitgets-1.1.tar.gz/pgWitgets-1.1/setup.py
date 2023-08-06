from setuptools import setup, find_packages
setup(name='pgWitgets',
      version='1.1',
      url='https://github.com/alexCoder23/pgWitgets',
      license='MIT',
      author='alexCoder23',
      author_email='alekesybeldem@gmail.com',
      description='pgWitgets',
      packages=find_packages(exclude=['pgWitgets']),
      long_description=open('README.md').read(),
      install_reqires=['pygame'],
      zip_safe=False)
