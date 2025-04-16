<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributors" %>
<%block name="title">Contributors</%block>


<h2>${_('Contributors')}</h2>
<p>
    ATLAs feature set descriptions and associated data are the result of a large team effort. All the people listed below have participated either as authors or as other contributors in one or more feature sets. Feature set authors are primarily responsible for the feature set description, conceptualization and coding supervision, while other contributors have provided feedback, participated in the conceptualization, and/or coded languages for the features in question. Detailed information on the authors’ and other contributors’ roles can be found in each feature set description.
</p>
<div>
    ${ctx.render()}
</div>
