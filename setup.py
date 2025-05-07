from setuptools import setup, find_packages

setup(
    name='quick-deployer-sdk',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'requests>=2.28.0',
    ],
    author='Nirav Sutariya',
    author_email='sutariya_nirav@yahoo.com',
    description='A Python SDK for the QuickDeployer API, supporting API interactions for project and server management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/niravsutariya/python-quick-deployer-sdk',
    project_urls={
        'Homepage': 'https://github.com/niravsutariya/python-quick-deployer-sdk#readme',
        'Repository': 'https://github.com/niravsutariya/python-quick-deployer-sdk.git',
    },
    keywords=['quickdeployer', 'sdk', 'python', 'api'],
    license='MIT',
    include_package_data=True,
    package_data={
        '': ['README.md', 'LICENSE'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
)