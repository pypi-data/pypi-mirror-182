# linkmaths_quarto
Ce package est conçu pour générer une mise en forme des documents linkpact sous différents formats.

Des templates de rédections sont initiés pour permettre à l'utilisateur de produire des rendus au bon format
sans se soucier de la mise en forme.




# comment creer un package python?
- pip install -q build
- https://www.youtube.com/watch?v=JkeNVaiUq_c


# instalation du package : 
- $ pip install linkmaths_quarto


# le package en ligne est ici :
- https://pypi.org/manage/project/linkmaths-quarto/collaboration/
- vous pouvez directement télécharger le package et récupérer les fichiers


# mise à jour du package :
- commit
- increment de version
- $ pip install .
- $ python -m build
- $ python -m twine upload --repository pypi dist/*
- $ pip upgrade linkmaths_quarto

NB: pour le upload, user=GuyNYAMSI, PWD=MEMEQUEGMAIL

# il est possible de tester avant de déployer
- $ pip uninstall linkmaths_quarto
- python -m twine upload --repository test.pypi dist/*
- $ pip install -i https://test.pypi.org/simple linkmaths_quarto

