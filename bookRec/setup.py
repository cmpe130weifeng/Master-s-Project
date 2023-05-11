from setuptools import setup

# open the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books-Recommender-System"
AUTHOR_USER_NAME = "weifeng"
SRC_REPO = "src" # source code (folder)
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy'] #require packages


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/cmpe130weifeng/Master-s-Project",
    author_email="weifeng.ma@sjsu.edu",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
