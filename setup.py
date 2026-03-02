from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.2",
    description="This contains code in ./src directory of the project",
    author="Vinit Gohil",
    packages=find_packages(where="src"),
    package_dir={"":"./src"},
    include_dirs=["./src*"],
    install_requires=["setuptools"],
    entry_points={
        "packages":[
            "main=dab_project.main:main"
        ]
    }
)