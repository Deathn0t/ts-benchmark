from distutils.core import setup

install_requires = [
    'scikit-optimize',
    'scikit-learn',
    'tqdm',
    'tensorflow',
    'keras',
]

extras_require = {
    'tf': ['tensorflow>=1.11.0'],
}

setup(
    name='ts-benchmark',
    version='0.0.1',
    packages=['ts-benchmark',],
    license=open('LICENSE.md').read(),
    long_description=open('README.md').read(),
    install_requires=install_requires,
    extras_require=extras_require,
)
