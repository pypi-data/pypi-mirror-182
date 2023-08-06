from setuptools import setup, find_packages


setup(
    name='td_grpc_reader',
    version='0.7',
    license='MIT',
    author="Emre Yiğit",
    author_email='emre.yigit01@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/bobmerevel/td_grpc_reader',
    keywords='example project',
    install_requires=[
        'urllib3',
        'grpcio-tools'
    ],

)