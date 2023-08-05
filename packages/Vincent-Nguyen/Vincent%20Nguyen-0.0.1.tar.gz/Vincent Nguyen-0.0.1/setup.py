from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Vincent Nguyen',
    version='0.0.1',
    description='Random Library ',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Vincent Nguyen',
    author_email='thanhvinhnguyenduc@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='RANDOM',
    packages=find_packages(),
    install_requires=['']
)
