from setuptools import setup, find_packages

setup(
    author= "Minghuan Ma",
    author_email = "maming3@xiaomi.com",
    version = "1.0.0",
    url="https://git.n.xiaomi.com/miphone-test-framework/gps-auto-test/gps-devices-resource",
    name="gliese_plugin",
    install_requires=["pluggy>=0.3,<1.0", "requests", "transitions", "geopy"],
    entry_points={"console_scripts": ["gliese_plugin=gliese_plugin.host:main"]},
    packages=find_packages(),
)
