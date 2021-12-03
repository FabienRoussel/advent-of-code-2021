from setuptools import setup, find_packages

setup(
    name='kpi-ocac',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='',
    author='CercleFormation',
    author_email='cercle.formation.sas@octo.com ',
    description='Projet streamlit pour la visualisation de KPI OCAC',
    install_requires=['pandas==1.3.3',
                      'python-dotenv==0.19.1',
                      'streamlit==1.2.0',
                      'plotly==5.4.0',
                      'numerize'],
    extras_require={'dev': ['flake8==4.0.1',
                            'pytest==6.2.5']},
    python_requires='>=3.9',
)
