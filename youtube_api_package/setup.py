from setuptools import setup, find_packages

setup(
    name='youtube_api_package',                # Name of your package
    version='0.1.0',                           # Versioning follows semantic versioning
    packages=find_packages(),                   # Automatically finds packages
    install_requires=[
        'google-api-python-client',             # Dependency for YouTube Data API
        'youtube-transcript-api'                # Dependency for YouTube Transcript API
    ],
    author='Your Name',                         # Your name
    author_email='your.email@example.com',     # Your email
    description='A package to interact with YouTube Data and Transcript APIs',  # Short description
    long_description=open('README.md').read(), # Long description from README.md
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/youtube_api_package',  # URL to your package repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                   # Python version requirement
)
