from setuptools import setup, Extension, find_packages


class get_pybind_include(object):
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)

cmodule = Extension(
    'baz',
    sources=['src/foo/main.cpp'],
    include_dirs=[
        # Path to pybind11 headers
        get_pybind_include(),
        get_pybind_include(user=True)
    ],
    language='c++',
    extra_compile_args=['-Wall', '-O3', '-std=c++14']
)

print('Found packages')
print(find_packages('src'))

setup(
    name='foo',
    version="0.0.1",
    author='Harold Howe',
    author_email='hhowe29@gmail.com',
    description='Mixing C++ and python in the same package',
    packages=find_packages('src'),
    package_dir={'':'src'},
    ext_modules=[cmodule],
    install_requires=['pybind11>=2.2'],
    test_suite='tests',
    zip_safe=False,
)