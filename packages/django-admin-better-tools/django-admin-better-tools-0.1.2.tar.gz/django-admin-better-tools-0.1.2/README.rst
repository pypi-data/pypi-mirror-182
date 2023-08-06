django-admin-better-tools
=========================

Overview
--------

django-admin-better-tools is a collection of extensions/tools for the default django
administration interface, it includes:

* a full featured and customizable dashboard;
* a customizable menu bar;
* tools to make admin theming easier.

The code is hosted on `Github Repo <https://github.com/riso-tech/django-admin-tools/>`_.

The project was forked from `David Jean Louis <http://www.izimobil.org/>`_ and was previously hosted on `Origin Github Repo <https://github.com/django-admin-tools/django-admin-tools/>`_.

Requirements
------------

django-admin-tools is compatible with Django 1.11 LTS up to Django 4.0 as well Python 2.7, 3.5+.

Installation
------------

To install django-admin-tools, run the following command inside this directory:

    pip install django-admin-better-tools

In Settings file, add the following to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        ...
    )

In Settings file, add the following to your Context Processors:

.. code-block:: python

    context_processors = (
        ...
        "admin_tools.context_processors.admin_tools",
        ...
    )

Screenshots
-----------

The django admin login screen:

.. image:: http://www.izimobil.org/django-admin-tools/images/capture-1.png
   :alt: The django admin login screen


The admin index dashboard:

.. image:: http://www.izimobil.org/django-admin-tools/images/capture-2.png
   :alt: The admin index dashboard


The admin menu:

.. image:: http://www.izimobil.org/django-admin-tools/images/capture-3.png
   :alt: The admin menu

Dashboard modules can be dragged, collapsed, closed etc.:

.. image:: http://www.izimobil.org/django-admin-tools/images/capture-4.png
   :alt: Dashboard modules can be dragged, collapsed, closed etc.

The app index dashboard:

.. image:: http://www.izimobil.org/django-admin-tools/images/capture-5.png
   :alt: The app index dashboard

