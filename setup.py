from setuptools import find_packages, setup

try:
    from setupext_janitor import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

cmd_classes = {}
if CleanCommand is not None:
    cmd_classes['clean'] = CleanCommand

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-pep8',
]

setup_requires = [
    'pytest-runner',
    'sphinx'
]

documentation_requires = ['recommonmark']

from sphinx.setup_command import BuildDoc
cmdclass = {'sphinx': BuildDoc}

from extendable_json import version_string as version
name = "Extendable JSON"

setup(
    name = name,
    version=version,
    release=version,
    author="Steven Swanson",
    author_email="Steven@SwanOhana.net",
    description="Drop in replacement of json, to quickly extend serializing capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kiln707/extendable_json",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    cmdclass=cmdclass,
    # these are optional and override conf.py settings
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', version),
            'source_dir': ('setup.py', 'docs'),
            'builder': ['HTML', 'markdown']}},
    setup_requires='pytest-runner',
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    install_requires=[
        'flask'
    ],
)
