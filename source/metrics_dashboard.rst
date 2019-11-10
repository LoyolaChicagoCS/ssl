Metrics Dashboard
===================

There is an emerging consensus in the scientific software community that progress in scientific research is dependent on the quality and accessibility of software at all levels.
Continued progress depends on embracing the best traditional--and emergent--practices in software engineering, especially agile practices that intersect with the more formal tradition of software engineering.

As a first step in our larger exploratory project to study in-process quality metrics for software development projects in Computational Science and Engineering (CSE), we have developed the Metrics Dashboard, a platform for producing and observing metrics by mining open-source software repositories on GitHub. 

The Metrics Dashboard focuses on metrics indicative of team progress and project health instead of privileging individual metrics, e.g. number of commits, etc. The Metrics Dashboard allows the user to submit the URL of a hosted repository for batch analysis, whose results are then cached. Upon completion, the user can interactively study various metrics over time (at varying granularity), numerically and visually. The initial version of the system is up and running as a public cloud service (SaaS) and supports project size (KLOC), defect density, defect spoilage, and productivity. While our system is by no means the first to support software metrics, we believe it may be one of the first community-focused extensible resources that can be used by any hosted project.


Presentations
--------------

Research Software
------------------

http://luc-metrics.herokuapp.com/

Key Papers
------------

.. list-table::
   :widths: 25 15

   * - Nasir U. Eisty, George K. Thiruvathukal, and Jeffrey C. Carver, Use of Software Process in Research Software Development: A Survey, Proceedings of the Evaluation and Assessment on Software Engineering (EASE) 2019.  2019, https://ecommons.luc.edu/cs_facpubs/214/
     - :index:`software process`, :index:`empirical study`, :index:`software engineering`

   * - Nasir U. Eisty, George K. Thiruvathukal, and Jeffrey C. Carver, *A Survey of Software Metric Use in Research Software Development*, IEEE 14th International Conference on e-Science (e-Science), 2018, pp. 212-222, https://ecommons.luc.edu/cs_facpubs/206/
     - :index:`empirical software engineering`, :index:`survey`, :index:`software metrics`

   * - George K. Thiruvathukal, Shilpika, Nicholas J. Hayward, and Konstantin Läufer, Metrics Dashboard: A Hosted Platform for Software Quality Metrics, https://arxiv.org/abs/1804.02053
     - :index:`software engineering`, :index:`tools`, :index:`software metrics`, :index:`metrics dashboard`, :index:`data science`
