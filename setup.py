from setuptools import setup
setup(
    name = 'limited_requests',
    packages = ['limited_requests'], # this must be the same as the name above
    install_requires=['datafy'],
    py_modules=['limited_requests'],
    version = '0.0.1',
    description = 'Time out network requests that take too long.',
    author = 'Aleksey Bilogur',
    author_email = 'aleksey.bilogur@gmail.com',
    url = 'https://github.com/ResidentMario/limited_requests',
    download_url = 'https://github.com/ResidentMario/limited_requests/tarball/0.0.1',
    keywords = ['data', 'requests'],
    classifiers = [],
)