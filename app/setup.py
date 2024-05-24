from setuptools import setup, find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()


setup(
    name='app.app',
    version=version,
    package_dir={'': 'src'},
    packages=find_namespace_packages(include=['cltl.*', 'cltl_service.*', 'myapp.*', 'myapp_service.*'], where='src'),
    data_files=[('VERSION', ['VERSION'])],
    url="https://github.com/leolani/cltl-template-app",
    license='MIT License',
    author='',
    author_email='',
    description='Template app for Leolani',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
    install_requires=[''],
)
