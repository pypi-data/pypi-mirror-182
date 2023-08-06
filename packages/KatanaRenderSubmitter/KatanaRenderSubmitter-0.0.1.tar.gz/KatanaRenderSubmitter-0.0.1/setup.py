from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Render submitter for Katana'

# Setting up
setup(
    name="KatanaRenderSubmitter",
    version=VERSION,
    author="jlonghurst",
    author_email="<jlonghurst@thelightersguild.com>",
    description=DESCRIPTION,
    py_modules=["core", 'ui', 'util'],
    install_requires=[],
    #package_dir={'bin': 'katana_render_submitter'},
    packages=['katana_render_submitter', 'katana_render_submitter/Tabs'],
    classifiers=["Programming Language :: Python :: 3"],
)