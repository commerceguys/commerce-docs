---
title: Checkout Form builder
taxonomy:
    category: docs
---

Here's the real definition of Checkout from Ryan Szrama:
>Checkout is a multi-step order edit form that involves the creation of additional entities (via customer profile checkout panes) and usually results in the creation of a payment transaction.

What does that mean to you? It means checkout and the form builder are just a large edit form for orders that create things like customer profiles and use things like payment gateways to move the order status around.

Drupal Commerce comes with a drag-and-drop checkout form builder that lets you decide what information you need to collect from or display to customers during the checkout process. It supports [single and multi-page checkout](../04.Checkout-Single-vs-Multiple-Page) depending on your requirements and can be easily extended with new components through the use of contributed or custom modules.

In the checkout system, a checkout page is a distinct step in the checkout process that contains one or more checkout panes that are represented as fieldsets or divs as part of the form representing the checkout page they're on. You do not have to use every checkout pane defined on your site, and some contributed modules will define new ones that you can use if needed.

## Default checkout pages and panes

### Checkout Settings

To see the available checkout pages and panes, go to Store -> Configuration -> Checkout settings.
![Checkout Settings](Checkout-Form-1.png)

The checkout form tab is selected by default, showing the checkout form builder pictured below.
![Checkout Form](Checkout-Form-2.png)

The default checkout pages are represented in the table by rows with bold titles and no drag-and-drop handle or configuration link:
* **Checkout** &mdash; the initial form used to collect basic order details.
* **Review order** &mdash; a review of all the order details with the pane for submitting payment.
* **Payment** &mdash; only used to redirect for off-site payment methods.
* **Checkout complete** &mdash; the final landing page showing the checkout completion message.

### Shopping cart contents

This checkout pane displays the contents of the shopping cart or order being completed on the checkout form. It actually displays the contents through a default View that you can customize to alter the display of the cart contents here in the checkout form. In the pane's configuration form, you can even direct the pane to use a different View entirely.

### Account information

This checkout pane is only visible for anonymous users, allowing them to specify an e-mail address to use for their order. For authenticated users, the pane is not shown, because Drupal Commerce initializes the order e-mail address field to the same e-mail address on file in their user account. Upon checkout completion, anonymous users who supplied an existing e-mail address will be notified that the order was associated with their existing account, while other anonymous users will have an account created for them. This behavior is configurable in the checkout completion rules.

**Note:** The Commerce Checkout Login module enhances this checkout pane by allowing customers who specify an existing e-mail address to supply their password and login immediately before continuing with checkout.

### Billing information

This checkout pane functions as an add/edit form for the billing customer profile to be associated with the order. By default, this pane will always result in the creation of a new billing customer profile, with addressbook functionality like reusing previous addresses being supplied by a contributed module.

Any fields you add to your Billing information customer profile type will appear here for the customer to supply, making it an easy way to collect details pertinent to the billing process. Additionally, changing the label of the associated customer profile reference field in the order settings will also change the title of this checkout pane on the front and back-end. Multilingual sites will need to configure field translation to ensure these labels appear in the proper language for the customer.

**Note:** A similar checkout pane will appear if you install the Commerce Shipping module, which defines a Shipping information customer profile type.

### Review order

This checkout pane displays a full summary of the order details, including data from any other checkout pane on the form that exposes it to this pane. It will include by default the cart contents again, the user's account information, and the billing address. Other checkout panes may or may not expose data to this pane, and any that does may be directed to the relevant checkbox on the pane's configuration form.

### Payment

This checkout pane presents all payment methods available to the customer in a radio select list. If the selected payment method requires additional information from the customer, such as credit card details, the pane will be updated via Ajax to include all the fields necessary to collect and transmit the payment details to the payment service.

### Off-site payment redirect

This checkout pane will only appear if the customer selected an off-site payment method, such as PayPal WPS. It appears as a message indicating the user will be redirected to the payment service, and a JavaScript auto-redirect will go ahead and submit the redirection form if JavaScript is enabled. Otherwise the customer will have to submit the form manually.

If payment was dealt with completely on-site, the user will automatically be advanced to the next checkout page.

### Completion message

This checkout pane displays a simple checkout completion message that links to the order details page in the user's account. Even anonymous users will be able to view their completed orders for the duration of their current session. The checkout completion message is configurable via the pane's configuration form for single language sites, but multilingual sites will want to leave it set to the default message and translate the default string to the desired message through the translation interface.
