from setuptools import setup
setup(
    name = 'limited_process',
    packages = ['limited_process'], # this must be the same as the name above
    install_requires=['datafy'],
    py_modules=['limited_process'],
    version = '0.0.1',
    description = 'Time out network requests that take too long.',
    author = 'Aleksey Bilogur',
    author_email = 'aleksey.bilogur@gmail.com',
    url = 'https://github.com/ResidentMario/limited_process',
    download_url = 'https://github.com/ResidentMario/limited_process/tarball/0.0.1',
    keywords = ['data', 'requests'],
    classifiers = [],
)