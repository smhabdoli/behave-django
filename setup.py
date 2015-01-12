from setuptools import setup


setup(
    name='django_behave',
    packages=['django_behave'],
    version='0.0.1',
    description='Django Test Service using the Behave BDD module',
    author='SMH Abdoli',
    author_email='smhabdoli@gmail.com',
    url='https://github.com/smhabdoli/django-behave',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Development Status :: Alpha',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[
        'Django',
        'selenium',
        'parse',
        'behave',
    ]
)
