from setuptools import setup

setup(
    name='my-nellie-plugin',
    version='0.1.4',
    py_modules=['plugin_module'],

    install_requires=[
        'nellie',
        'numpy',
    ],

    entry_points={
        'nellie.plugins': [
            'Custom Plugin Name = plugin_module:nellie_plugin_function',
        ],
    },

    author='Your Name',
    author_email='your.email@example.com',
    description='A plugin for Nellie that does XYZ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-nellie-plugin',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
