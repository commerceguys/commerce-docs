---
title: Receipt emails
taxonomy:
    category: docs
---

## Overview

These settings are managed on an Order Type basis so that you can have different settings for different types of orders and manage order notifications in a granular way.


## Enable / Disable Customer Order Receipts & Store Notification Emails

Visit the Commerce configuration page and go to the Order types page in the Orders section.

![Select Order types](commerce2-order-configuration.png)

Click on **Edit** on the order type you wish to configure

![Select Order Type](commerce2-order-type-selection.png)

Locate the **Emails** section

![Check / uncheck notification](commerce2-email-section.png)

 - Check / uncheck the **Email the customer a receipt when an order is placed** box.
 - Enter the store notification email address into the **Send a copy of the receipt to this email:** field. You can enter multiple comma separated addresses into this field eg "one@example.com, two@example.com, three@example.com"

## Editing / Translating the Email Text

Use the template file located in `/commerce/modules/order/templates/commerce-order-receipt.html.twig`.

You can copy this file to your theme and then edit the text as desired. You can also use the file as a translation reference when searching for strings to translate in the user interface translation UI.
