Objektorientering
=================

Detta repository innehåller övningar tänkta som en introduktion till
programmering i Python.

Övningarna
----------
Övningarna finns i moduler i paketet exercises.
Förväntad funktion finns i de docstrings som hör ihop med funktionerna.

För att köra linter och enhetstester kan du använda följande kommandon.

.. code-block::

  python manage.py lint
  python manage.py test

För vissa övningar förväntas du själv skriva enhetstester. Detta görs med
fördel i testfiler med beskrivande namn. (De måste ha formen :code:`test_*.py`.)

.. code-block::

  python manage.py test --coverage

Kör testerna med code coverage-analys. Används med fördel för att få en
uppfattning om vilken kod du har kvar att skriva tester till. En HTML-rapport
skapas på sökvägen :code:`./tmp/coverage/index.html`.

Innan du börjar
---------------
Skapa den virtuella körmiljön. Beroende på ditt system kan du behöva välja
tydlig och köra :code:`python3` istället för :code:`python`.

.. code-block::

  python -m venv venv

Aktivera den virtuella körmiljön:

.. code-block::

  . venv/bin/activate

Om du använder Windows:

.. code-block::

  venv/Script/activate.bat

Installera de paket som behövs för uppgiften:

.. code-block::

  pip install -r requirements.txt
