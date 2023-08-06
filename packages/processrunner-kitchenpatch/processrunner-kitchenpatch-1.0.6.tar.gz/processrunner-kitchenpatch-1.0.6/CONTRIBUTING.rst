Publishing ProcessRunner-KitchenPatch
========================
Information on contributing may get added later.

Publishing
----------
Configure Twine and the PyPi RC file at `~/.pypirc` .

.. code-block:: ini

    [distutils]
    index-servers=
        test-kitchenpatch
        kitchenpatch

    # Use twine upload --repository test dist/*
    [test-kitchenpatch]
    repository = https://test.pypi.org/legacy/
    username = __token__
    password = <your token>

    # Use twine upload --repository production dist/*
    [kitchenpatch]
    repository = https://upload.pypi.org/legacy/
    username = __token__
    password = <your token>

1. Make sure you're at the project root

2. Ensure all commits are made, pushed, and the Git environment clear

.. code-block:: bash

    git stash

3. Set the new version in the pyproject.toml file

4. Tag the current version

.. code-block:: bash

    git tag -a x.y.z -m "Version release message"

5. Build the release package. The resulting files will be in `./dist/`.

.. code-block:: bash

    ./make-dist.sh

6. Push to PyPi's test environment first and ensure everything looks good on
the web site.

.. code-block:: bash

    python -m twine upload --repository test-kitchenpatch dist/*

7. Then push to PyPi's official repo.

.. code-block:: bash

    python -m twine upload --repository kitchenpatch dist/*
