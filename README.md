## About

`limited_process` is a tiny Python package that allows you to perform operations that will automatically time 
out after some number of seconds. It's a bare-bones wrapper on `multiprocessing`, implemented for the sake of 
convenience.

As a convenience, the default callback is a `datafy.get` operation on your URI.

## Installation
`pip install git+git://github.com/ResidentMario/limited-process` to install.

## Development

To hack on `datafy`, clone this library locally. Install its development dependencies (`pytest`, `datafy`) via 
`pip`. If you have `conda`, you can run `conda env create -f envs/devenv.yml` to do this for you.

To execute the test suite, run `pytest tests.py` on the command line from the `/tests` folder.

Pull requests welcome.