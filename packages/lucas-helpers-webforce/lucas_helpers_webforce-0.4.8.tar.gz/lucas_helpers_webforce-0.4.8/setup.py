from setuptools import setup

with open('README.md', 'r') as puntero:
    long_description = puntero.read()


setup(
    name='lucas_helpers_webforce',
    packages=['lucas_helpers_webforce'],  # this must be the same as the name above
    version='0.4.8',
    description='description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Webforce',
    author_email='',
    # use the URL to the github repo
    url='',
    download_url='',
    keywords=['testing', 'logging', 'example'],
    classifiers=[],
    license='MIT',
    install_requires=[
        'celery==5.2.7',
        'flower==1.2.0',
        'importlib-metadata==4.13.0',
        'mysqlclient==2.1.1',
        'PyMySQL==1.0.2',
        'pytz==2022.6',
        'redis==4.4.0',
        'SQLAlchemy==1.4.44',
        'twilio==7.15.4'
    ],
)