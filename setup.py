from setuptools import setup, find_packages

setup(
    name="port-scanner",
    version="2.0.0",
    author="bad-antics",
    description="Fast multi-threaded port scanner with service detection",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=["requests", "colorama", "pyyaml", "rich"],
)
