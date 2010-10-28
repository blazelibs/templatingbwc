from setuptools import setup, find_packages

import templatingbwp
version = templatingbwp.VERSION

setup(
    name = "TemplatingBWP",
    version = version,
    description = "A BlazeWeb component with template themes",
    author = "Randy Syring",
    author_email = "rsyring@gmail.com",
    url='http://pypi.python.org/pypi/TemplatingBWP',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
      ],
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    include_package_data=True,
    install_requires = [
        'BlazeForm>=0.3.0dev',
        'BlazeWeb>=0.3.0dev',
    ],
    zip_safe=False
)
