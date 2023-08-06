from setuptools import setup

setup(
    name="chatgpc-cli",
    description="A natural language command line interface powered by chatgpc",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    version="0.3",
    dependencies = [ "openai" ],
    include_package_data=True,
    install_requires=["click"],
    license='MIT',
    entry_points="""
        [console_scripts]
        chatgpci=chatgpci:cli
    """,
)

