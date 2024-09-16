Use polymorphism to create child classes of a "base" class that still leverage its essential properties while adding 
custom properties and functions (or implementations of those properties and functions) that represent their own unique 
properties and capabilities.

The classic example often used is that a dog, a cat, and a fish are all animals, so an Animal class is the parent 
class while the Dog, Cat, and Fish classes would be child classes. Certain properties will belong to all three of 
these child classes and several other animals, such as average_length, average_weight, preferred_habitat, etc. It 
would not make sense, on the other hand, for the Animal class to have a fur_length property, as some animals (such 
as a fish in our example) don't have fur at all. Such properties should be reserved for the individual animals or 
subclasses of animals that typically have fur.

In our example, we need to take a payment. Payments can come in many forms (credit card, cash, cash app, check, etc.), 
and each method of payment has its own properties (cash, for example, won't have a card number associated with it, nor 
will a credit card have an email address associated with it like a cash app would). We define a parent class - Payment - 
which only has an amount attribute (common accross all payment methods). We then have the CreditCard and Paypal child 
classes implement their own unique versions of the process_payment method that exists on the Payment parent class. In 
the parent class, Payment, that method only has the word "pass" in it. This means that any child classes leveraging 
this parent class will be expected to implement their own versions of the process_payment method.