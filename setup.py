from setuptools import setup, find_packages

setup(
    name="experimental.omnipresence",
    version="1.0.0",
    description="Monkeypatches Plone to support omnipresence",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords="",
    author="Asko Soukka",
    author_email="asko.soukka@iki.fi",
    url="https://github.com/datakurre/experimental.omnipresence/",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["experimental"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "collective.monkeypatcher",
    ],
    extras_require={"test": [
        "plone.app.testing",
    ]},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
)
