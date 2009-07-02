from setuptools import setup, find_packages
setup(
    name = "PyWITS",
    version = "0.1",
    description = 'WITS0 Serial API',
    author = 'Kenneth Miller',
    author_email = 'xkenneth@gmail.com',
    url = 'xkenneth.blogspot.com',
    install_requires = ['pyserial'],
    packages = find_packages(),
)
