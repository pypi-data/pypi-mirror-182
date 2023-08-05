from setuptools import setup

setup(
    name="huggingface-download-cli",
    version="1.0.3",
    author="xihajun",
    author_email="junfan@krai.ai",
    description="A utility to download files from the Hugging Face Model Hub",
    packages=["hf_download"],
    entry_points={
        "console_scripts": ["hf_download=hf_download.main:main"]
    },
    install_requires=[],
)
