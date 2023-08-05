from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(

    name='AliProductExtractor',
    packages=['AliProductExtractor'],
    version='0.2',
    license='MIT',
    description="It will get the product data from ali express",

    long_description=long_description,
    author='Sardar Badar Saghir',
    author_email='dataentrybadar@gmail.com',
    url='https://github.com/BadarSaghir/AliProductExtractor',
    download_url='https://github.com/BadarSaghir/AliProductExtractor/releases/download/0.1/AliProductExtractor.zip',
    # Keywords that define your package best
    keywords=['Ali express', 'Ali  express product',
              'Ali express product scraper', 'scraper Ali express', 'scraper', 'extractor'],
    install_requires=[
        'selenium==4.0.0a1',
        'webdriver_manager==3.8.5'

    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.10',
    ],
)
