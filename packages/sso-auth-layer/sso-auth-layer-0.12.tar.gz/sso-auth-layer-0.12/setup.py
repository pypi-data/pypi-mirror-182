from setuptools import setup,find_packages

setup(name='sso-auth-layer',
      version='0.12',
      description='User Authentication using SSO',
      packages=['sso-auth-user'],
      author_email='adhomse99@gmail.com',
      install_requires=['requests'],
      zip_safe=False)
