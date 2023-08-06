import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="raga-ai-py",
    version="0.0.1",
    author="Manab ROy",
    author_email="manabroy72@gmail.com",
    packages=["raga_ai_py"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/manabroyown/raga-ai-py",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)