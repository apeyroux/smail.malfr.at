from setuptools import setup

setup(
    name='smail',
    packages=['smail'],
    include_package_data=True,
    package_dir={'smail': 'src'},
    zip_safe=False,
    entry_points={'console_scripts': ['smail = smail.__main__:main']}
)
