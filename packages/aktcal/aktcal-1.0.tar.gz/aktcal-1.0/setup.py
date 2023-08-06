from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(
    name='aktcal',
    version='1.0',
    description='This is a simple library that performs basic python arithmetic operations.',
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Scofield1/easycal',
    author='Abdulrauf Adebayo',
    author_email='adebayoabdulrauf1@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']
)
