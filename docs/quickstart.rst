
Quickstart
=============

To use tasting, follow some simple steps.

.. toctree::
   :maxdepth: 2


Annotate a "QA-able" piece of functionality with ``@tasting.checkpoint``
----------------------------------------------------------------------------

When you find it, add the ``checkpoint`` annotation, with a description for the team reading the report.

For example, you might annotate a function implementing a REST API as::

   @tasting.checkpoint("Create or Update Blog Posts")
   def blog_post(request):
       # Your view code here, likely calling other code

When you change a function needing QA attention use ``@tasting.needs.qa``
----------------------------------------------------------------------------

Any checkpoint that calls the function (directly or indirectly) will be reported for attention::

   @tasting.needs.qa("Now make slugs with a different algorithm")
   def generate_slug(name):
       # Your new slug generator. Any problems?

Run pytest with the ``--tasting`` flag
--------------------------------------------

This generates a report named ``tasting.output`` containing all combinations of needs and checkpoints encountered during execution.

.. code-block:: json

   {
     "results": [
       {
         "needs": "qa",
         "reason": "Now make slugs with a different algorithm",
         "checkpoint": "Create or Update Blog Posts"
       }
     ]
   }
