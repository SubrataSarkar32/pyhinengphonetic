==============
pyhinengphonetic
==============
Python implementation to convert unicode hindi text to speable english text for pyttsx and to english phonetic
Below is license of 
pyAvroPhonetic
 from which it has been derived
License
=======

Copyright (C) 2016 Subrata Sarkar <subrtosarkar32@gmail.com>.

::

    This file is part of pyhinengphonetic.

    pyhinengphonetic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pyhinengphonetic is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pyhinengphonetic. If not, see <http://www.gnu.org/licenses/>.

The full license text can be found in ``LICENSE``.

Usage
=====

::

    from pyhinengphonetic import conparse
    conparse.convert_to_pyttsx_speakable(u'\u0915\u0948\u0938\u0947 \u0939\u0947')
    conparse.speak(u'\u0915\u0948\u0938\u0947 \u0939\u0947')

Installation
============

Using Git:

::

    $ git clone https://github.com/SubrataSarkar32/pyhinengphonetic.git
    $ cd pyhinengphonetic
    $ sudo python setup.py install


Using Pip:

::

    $ sudo pip install pyhinengphonetic

Contributing
============

**Fork** -> **Do your changes** -> **Send a Pull Request**. It's that
easy!

Coding style follows `PEP 8`_ along with `PEP 257`_ for Docstring
conventions.

Also, if you find any bugs, please report them in the Issues queue. As
always, before you report any new issue, please check that it has not
been already posted by someone else.

.. _Avro Phonetic: http://omicronlab.com
.. _Mehdi Hasan Khan: https://github.com/omicronlab
.. _Rifat Nabi: https://github.com/torifat
.. _jsAvroPhonetic: https://github.com/torifat/jsAvroPhonetic
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. |Master| image:: https://travis-ci.org/kaustavdm/pyAvroPhonetic.png?branch=master
   :target: https://travis-ci.org/kaustavdm/pyAvroPhonetic
.. |Develop| image:: https://travis-ci.org/kaustavdm/pyAvroPhonetic.png?branch=develop
   :target: https://travis-ci.org/kaustavdm/pyAvroPhonetic
.. _Md Enzam Hossain: https://github.com/ienzam
.. _Sarim Khan: https://github.com/sarim

Below is the lisence of pyAvroPhonetic:
==============
pyAvroPhonetic
==============

A Python implementation of the popular Bengali phonetic-typing software
`Avro Phonetic`_.

Branch: Master: |Master| | Develop: |Develop|

Overview
========

pyAvroPhonetic provides a Python package that can be imported and used
by other Python programs or scripts. It implements the *Avro Phonetic
Dictionary Search Library* by `Mehdi Hasan Khan`_.

*N.B. This package is still experimental and is not (yet) fit for
production use.*

Inspirations
------------

This package is inspired from `Rifat Nabi`_\'s `jsAvroPhonetic`_. So
far, the code is a direct (and shameless) translation of
jsAvroPhonetic into Python.

Installation
============

Using Git:

::

    $ git clone https://github.com/kaustavdm/pyAvroPhonetic
    $ cd pyAvroPhonetic
    $ sudo python setup.py install


Using Pip:

::

    $ sudo pip install PyAvroPhonetic


Usage
=====

At present only a subset of features have been implemented. When
implemented, the parser can be accessed as:

::

    >>> from pyavrophonetic import avro
    >>> avro.parse('aami banglay gaan gai')

Contributing
============

**Fork** -> **Do your changes** -> **Send a Pull Request**. It's that
easy!

Coding style follows `PEP 8`_ along with `PEP 257`_ for Docstring
conventions.

Also, if you find any bugs, please report them in the Issues queue. As
always, before you report any new issue, please check that it has not
been already posted by someone else.

Acknowledgements
================

 - Mehdi Hasan Khan for originally developing and maintaining Avro
   Phonetic
 - Rifat Nabi for porting it to Javascript
 - `Md Enzam Hossain`_ for helping me understand the ins and outs of
   the Avro dictionary and the way it works
 - `Sarim Khan`_ for writing ibus-avro which helped to clarify my
   concepts further

License
=======

Copyright (C) 2013 Kaustav Das Modak <kaustav.dasmodak@yahoo.co.in>.

::

    This file is part of pyAvroPhonetic.

    pyAvroPhonetic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pyAvroPhonetic is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pyAvroPhonetic.  If not, see <http://www.gnu.org/licenses/>.

The full license text can be found in ``LICENSE``.

.. _Avro Phonetic: http://omicronlab.com
.. _Mehdi Hasan Khan: https://github.com/omicronlab
.. _Rifat Nabi: https://github.com/torifat
.. _jsAvroPhonetic: https://github.com/torifat/jsAvroPhonetic
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. |Master| image:: https://travis-ci.org/kaustavdm/pyAvroPhonetic.png?branch=master
   :target: https://travis-ci.org/kaustavdm/pyAvroPhonetic
.. |Develop| image:: https://travis-ci.org/kaustavdm/pyAvroPhonetic.png?branch=develop
   :target: https://travis-ci.org/kaustavdm/pyAvroPhonetic
.. _Md Enzam Hossain: https://github.com/ienzam
.. _Sarim Khan: https://github.com/sarim
