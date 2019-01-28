from setuptools import setup, find_packages


setup(
    name='ml_nlp_tk',
    version='1.0.0',
    description='Tool for NLP - handle file and text',
    long_description="Github : https://github.com/mindlayer/ml-nlp-tk",
    url='https://github.com/mindlayer/ml-nlp-tk',
    author='Eric Lam',
    author_email='hello@mindlayer.io',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='nlp file io string text mining',
    packages=find_packages()
)
