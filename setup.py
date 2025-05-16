from setuptools import setup, find_packages

setup(
    name="dag_executor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "tqdm",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'dag-exec=cli.main:main',
        ],
    },
)