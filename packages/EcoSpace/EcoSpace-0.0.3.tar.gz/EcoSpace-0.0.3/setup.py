from distutils.core import setup
import setuptools

long_description = '''官方链接
EcoSpace 官方链接：https://www.ecospace.top

Official link
EcoSpace Official link：https://www.ecospace.top
'''

packages = ['EcoSpace']
setup(name = 'EcoSpace',
    version = '0.0.3',
    author = 'EcoSpace',
    author_email = 'getmail@ecospace.top',
    description = 'EcoSpace官方库',
    long_description = long_description,
    packages = packages, 
    package_dir = {'requests': 'requests'},)