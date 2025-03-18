from setuptools import setup, find_packages

setup(
    name="dataAnalyticsFunctions",  # パッケージ名（フォルダ名と同じ）
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib.pyplot",
        "seaborn"
    ],
    author="Akinari Hashimoto",
    author_email="akinari020637@gmail.com",
    description="using data analytics",
    url="https://github.com/AkinariHashimoto/dataAnalyticsFunctions",  # GitHubリポジトリのURL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)