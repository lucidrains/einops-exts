from setuptools import setup, find_packages

setup(
  name = 'einops-exts',
  packages = find_packages(exclude=[]),
  version = '0.0.4',
  license='MIT',
  description = 'Einops Extensions',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/einops-exts',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'tensor manipulation'
  ],
  install_requires=[
    'einops>=0.4',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
