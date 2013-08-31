from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(
    name='socialschools-cms',
    version=version,
    description='SocialSchools CMS app with defaults for django-cms',
    author='Pratik Vyas',
    author_email='pratik.vyas@changer.nl',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().split(),
)
