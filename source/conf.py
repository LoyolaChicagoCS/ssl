import sys
import os
import sphinx_rtd_theme

# Project Information
project = "Software and Systems Laboratory"
copyright = "2012-Present, Software and Systems Laboratory"
author = "Software and Systems Laboratory"
version = os.environ.get("BOOK_VERSION", "beta")
release = version

# General Configuration
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
]
source_suffix = {".rst": "restructuredtext"}
source_encoding = "utf-8-sig"
# source_parsers =
master_doc = "index"
# exclude_patterns = []
templates_path = ["_templates"]
# template_bridge =
rst_epilog = (
    """
.. |pdf-version| replace:: `printable PDF  <https://github.com/LoyolaChicagoCS/ssl/releases/download/%(version)s/SoftwareSystemsLaboratory.pdf>`__

.. |epub-version| replace:: `eBook <https://github.com/LoyolaChicagoCS/ssl/releases/download/%(version)s/SoftwareSystemsLaboratory.epub>`__

.. |SSL| replace:: :abbr:`SSL (Software Systems Laboratory)`

.. |STEAM| replace:: :abbr:`STEAM (Science, Technology, Engineering, Arts, and Mathematics)`

.. |ZettelGeist| replace:: :doc:`/research/incubation/zettelgeist`

.. |Metrics Dashboard| replace:: :doc:`/research/in-progress/metrics-dashboard`

.. |Shape Analysis| replace:: :doc:`/research/collaborations/shape-analysis`

.. |VoltKey| replace:: :doc:`/research/in-progress/voltkey`

.. |Hermes| replace:: :doc:`/research/incubation/hermes`

.. |LUTE| replace:: :doc:`/research/incubation/lute`

.. |TE| replace:: :doc:`/research/in-progress/test-effectiveness`

.. |NLC| replace:: `/research/incubation/nlc`

.. |FLIC| replace:: `/research/incubation/flic`
"""
    % vars()
)
# rst_prolog =
# primary_domain =
# default_role =
# keep_warnings =
# suppress_warnings =
# needs_sphinx =
# needs_extensions =
# manpages_url =
nitpicky = True
# nipicl_ignore =
# numfig =
# numfig_format =
# numfig_secnum_depth =
# smartquotes =
# smartquotes_action =
# smartquotes_excludes =
# user_agent =
tls_verify = True
# tls_cacerts =
# today =
# today_fmt =
highlight_language = "python3"
# highlight_options = # See Pygments documentation
pygments_style = "sphinx"
# add_function_parentheses =
# add_module_names =
show_authors = False
# modindex_common_prefix =
# trim_footnote_reference_space =
# trim_doctest_flags =
# strip_signature_backslash =

# Options for Internationalization
# language =
# locale_dirs =
# gettext_compact =
# gettext_uuid =
# gettext_location =
# gettext_auto_build =
# gettext_additional_targets =
# figure_language_filename =

# Options for Math
math_number_all = True
# math_eqref_foirmat =
# math_numfig =

# Options for HTML Output
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # "canonical_url": "",
    "analytics_id": "UA-5482792-29",
    # "logo_only": False,
    # "display_version": True,
    "prev_next_buttons_location": "none",
    # "style_external_links": False,
    # "vcs_pageview_mode": "",
    # "style_nav_header_background": "white",
    # "collapse_navigation": True,
    # "sticky_navigation": True,
    # "navigation_depth": 4,
    # "includehidden": True,
    # "titles_only": False
}
# html_theme_path =
# html_style =
html_title = "%(project)s v%(release)s" % vars()
# html_short_title =
# html_baseurl =
# html_codeblock_linenos_styl =
html_context = {
    "css_files": [
        "_static/theme_overrides.css",  # override wide tables in RTD theme
    ],
}
# html_logo =
# html_favicon =
# html_css_files =
# html_js_files =
html_static_path = ["_static"]
# html_extra_path =
# html_last_updated_fmt =
# html_use_smartypants =
# html_add_permalinks =
# html_sidebars =
# html_additional_pages =
# html_domain_indices =
# html_use_index =
# html_split_index =
# html_copy_source =
# html_show_sourcelink =
# html_sourcelink_suffix =
# html_use_opensearch =
# html_file_suffix =
# html_link_suffix =
html_show_copyright = False
html_show_sphinx = False
# html_output_encoding =
# html_compact_lists =
# html_secnumber_suffix =
# html_search_language =
# html_search_options =
# html_search_scorer =
# html_scaled_image_link =
# html_math_renderer =
html4_writer = False

# Options for Single HTML output
# singlehtml_sidebars =

# Options for HTML Help Output
htmlhelp_basename = "SoftwareSystemsLaboratory"
# htmlhelp_file_suffix =
# htmlhelp_link_suffix =

# Options for Apple Help Output
# applehelp_bundle_name =
# applehelp_bundle_id =
# applehelp_dev_region =
# applehelp_bundle_version =
# applehelp_icon =
# applehelp_kb_product =
# applehelp_kb_url =
# applehelp_remote_url =
# applehelp_index_anchors =
# applehelp_min_term_length =
# applehelp_stopwords =
# applehelp_locale =
# applehelp_title =
# applehelp_codesign_identity =
# applehelp_codesign_flags =
# applehelp_indexer_path =
# applehelp_codesign_path =
# applehelp_disable_external_tools =

# Options for EPUB Output
epub_basename = "SoftwareSystemsLaboratory"
# epub_theme =
# epub_theme_options =
epub_title = "Software and Systems Laboratory"
# epub_description =
epub_author = "Software and Systems Laboratory"
# epub_contributor =
# epub_language =
epub_publisher = "Software and Systems Laboratory"
epub_copyright = "2012, Software and Systems Laboratory"
# epub_identifier =
# epub_scheme =
# epub_uid =
# epub_cover =
# epub_css_files =
# epub_guide =
# epub_pre_files =
# epub_post_files =
# epub_exclude_files =
# epub_tocdepth =
# epub_tocdup =
# epub_tocscope =
# epub_fix_images =
# epub_max_image_width =
# epub_show_urls =
# epub_use_index =
# epub_writing_mode =

# Options for LaTeX Output
# latex_engine =
latex_documents = [
    (
        "index",
        "SoftwareSystemsLaboratory.tex",
        "Software and Systems Laboratory",
        "Software and Systems Laboratory",
        "manual",
    ),
]
# latex_logo =
# latex_toplevel_sectioning =
# latex_appendices =
# latex_domain_indices =
# latex_show_pagerefs =
# latex_show_urls =
# latex_use_latex_multicolumn =
# latex_use_xindy =
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}
# latex_docclass =
# latex_additional_files =
# latex_theme =
# latex_theme_options =
# latex_theme_path =
# text_newlines =
# text_sectionchars =
# text_add_secnumbers =
# text_secnumber_suffix =

# Options for Manual Page Output
man_pages = [
    (
        "index",
        "softwareandsystemslaboratory",
        "Software and Systems Laboratory",
        ["Software and Systems Laboratory"],
        1,
    )
]
# man_show_urls

# Options for Texinfo Output
texinfo_documents = [
    (
        "index",
        "SoftwareSystemsLaboratory",
        "Software and Systems Laboratory",
        "Software and Systems Laboratory",
        "SoftwareSystemsLaboratory",
        "One line description of project.",
        "Miscellaneous",
    ),
]
# texinfo_appendices =
# texinfo_domain_indices =
# texinfo_show_urls =
# texinfo_no_detailmenu =
# texinfo_elements =

# Options for QtHelp output
# qthelp_basename =
# qthelp_namespace =
# qthelp_theme =
# qthelp_theme_options =

# Options for the LinkCheck Builder
# linkcheck_ignore =
# linkcheck_request_headers =
# linkcheck_retries =
# linkcheck_timeout =
# linkcheck_workers =
# linkcheck_anchors =
# linkcheck_anchors_ignore =
# linkcheck_auth =

# Options for the XML Builder
# xml_pretty =

# Options for the C Domain
# c_id_attributes =
# c_paren_attributes =
# c_allow_pre_v3 =
# c_warn_on_allowed_pre_v3 =

# Options for the C++ Domain
# cpp_index_common_prefix =
# cpp_id_attributes =
# cpp_paren_attributes =

# sphinx.ext.todo module config
todo_include_todos = True
