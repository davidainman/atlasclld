<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%! from atlasclld.models import ATLAsFeatureSet %>
<%block name="title">Feature Sets</%block>
<h2>Feature Sets</h2>
<p>
    ATLAs contains 17 feature sets, which are designed to capture linguistic variation within a typological domain. Each feature set description typically contains sections providing detailed information on the typological domain covered (What), motivation for its inclusion in the database (Why), the methodology used (How), a full list of associated features accompanied by explanations and examples (Features and Derived features), and finally results of the survey (Results). Each feature set has one or more authors who are primarily responsible for the feature set description, conceptualization and coding supervision, and a number of other contributors that have provided feedback, contributed to the conceptualization, and/or coded languages for the features in question. Detailed information on the authors’ and other contributors’ roles can be found in each feature set description.
</p>
<div class="clearfix"> </div>
${ctx.render()}
