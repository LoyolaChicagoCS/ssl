Testing Effectiveness
=======================

As part of our overall interest in code quality, we're interested in looking at test effectiveness. To improve testing effectiveness, we must not only look at techniques such as code coverage but, more broadly, at the quality of the tests themselves.  We've started by looking at this within major codebases such as the Scala core library and, specifically, how to test stateful abstractions.

In testing stateful abstractions, it is often necessary to record interactions, such as method invocations, and express assertions over these interactions. Following the Test Spy design pattern, we can reify such interactions programmatically through additional mutable state. Alternatively, a mocking framework, such as Mockito, can automatically generate test spies that allow us to record the interactions and express our expectations in a declarative domain-specific language.  According to our study of the test code for Scala's Iterator trait, the latter approach can lead to a significant reduction of test code complexity in terms of metrics such as code size (in some cases over 70% smaller), cyclomatic complexity, and amount of additional mutable state required. In this tools paper, we argue that the resulting test code is not only more maintainable, readable, and intentional, but also a better stylistic match for the Scala community than manually implemented, explicitly stateful test spies.

Key Papers
------------

.. list-table::
   :widths: 25 15

   * - Konstantin Läufer, John O’Sullivan, and |George-K-Thiruvathukal|. 2019. *Tests as Maintainable Assets Via Auto-generated Spies*. In Proceedings of Tenth ACM SIGPLAN Scala Symposium, London, United Kingdom, July 17, 2019 (Scala ’19), https://ecommons.luc.edu/cs_facpubs/230/
     - :index:`testing`, :index:`software quality`, :index:`maintainability`, :index:`software engineering`, :index:`programming languages`
