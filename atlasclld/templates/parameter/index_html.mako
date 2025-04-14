<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">Features</%block>
<%! from atlasclld.models import ATLAsParameter %>
<h2>Features</h2>
<p>
    ATLAs includes 265 features organized in 17 feature sets. Each feature is a single structural property and is coded for the entire language sample. Features may be single-valued (a language can have only one state), multi-valued (a language can have more than one state), or give count or proportion information (e.g. NounPoss-02 lists the kinds of possession classes present in a language and how many of each kind there are).
</p>
<p>
    Recurrent states for many features in ATLAs are &lt;NA&gt; and &lt;?&gt;. &lt;NA&gt; stands for “Not Applicable” and is a state for conditioned questions when the condition is not fulfilled. E.g., if the language has no singular-plural verb stem alternation, a number of subsequent features within this feature set are coded with &lt;NA&gt; for this language. Missing information, either because no information is present in the available sources, or because the information available is contradictory and did not allow us to reach a conclusion, is represented with &lt;?&gt;. Usually, an accompanying comment explains the reason and the sources consulted are listed in the Source field.
</p>
<p>
    Features in ATLAs are divided in main and derived. Main features are for the most part coded directly by consulting linguistic sources, such as grammars and dictionaries. Derived features offer different conceptualizations or aggregations of the same data included in the base features and are coded automatically from on one or more base features. Often, this groups states of multi-state features to capture broader similarities. In other cases, derived features are designed in order to be independent from other features. Detailed descriptions and motivations for derived features are given in the corresponding feature set.
</p>
<div class="clearfix"> </div>
${ctx.render()}
