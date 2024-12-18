from setuptools import setup, find_packages

setup(
    name='sliding-window-rate-limiter',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.8',
    author='aashish Rayamajhi',
    author_email='ashishrayamajhi227@gmail.com',
    description='A flexible sliding window rate limiter for Python applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ashish2345/Rate-Limit-Sliding-Window',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)