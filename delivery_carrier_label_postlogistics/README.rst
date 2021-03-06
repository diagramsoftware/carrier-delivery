.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

PostLogistics Labels WebService
===============================

This module uses `PostLogistics BarCodes WebService`_ to generate labels
for your Delivery Orders.

It adds a `Create label` button on Delivery Orders.
A generated label will be an attachement of your Delivery Order.

To see it, please install documents module.

You can create multiple delivery method to match your diffent package types.


Configuration
-------------

.. important::
   A "Swiss Post Business customer" account is required to use this module.

   See `Swiss Post E-logistics`_


To configure:

* Go to `Configurations -> Settings -> Postlogistics`
* Set your login informations
* launch the Update PostLogistics Services

This will load available services and generate carrier options.

Now you can create a carrier method for PostLogistics WebService:

* First choose a Service group and save
* Add a Mandatory Carrier option using a Basic Service
* Save Carrier Method (this will update filters to show you only
  compatible services)
* Then add other `Optional as default` and `Optional` carrier option
  from listed
* Additional Service and Delivery instructions

.. _PostLogistics BarCodes WebService: http://www.poste.ch/post-startseite/\
post-geschaeftskunden/post-logistik/post-e-log/post-e-log-webservices.htm
.. _Swiss Post E-logistics: http://www.poste.ch/en/post-startseite/\
post-geschaeftskunden/post-logistik/post-e-log.htm


Recommended modules
-------------------

* PostLogistics labels - logo per Shop
  If you have multiple shops configure one logo per shop

Technical references
--------------------

`"Barcode" web service documentation`_

.. _"Barcode" web service documentation: http://www.poste.ch/post-barcode-cug\
.htm


Credits
=======

Contributors
------------

* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Guewen Baconnier <guewen.baconnier@camptocamp.com>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.
