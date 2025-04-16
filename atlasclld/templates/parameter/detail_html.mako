<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%! from atlasclld.models import ATLAsValue %>
<% values_dt = request.get_datatable('values', ATLAsValue, parameter=ctx) %>
<%block name="title">${ctx.id}</%block>

<%block name="head">
    ${util.head_coloris()|n}
</%block>

<div class="row-fluid">
    <div class="span8">
        <h1>${ctx.name}</h1>
        % if ctx.question:
        <h2 class="question">${ctx.id}: ${ctx.question}</h2>
        % endif
        <p>
            This feature is described in the feature set 
            <a href="${request.resource_url(ctx.featureset)}">${ctx.featureset}</a>.
        </p>
        <p> 
            It is authored by ${h.linked_contributors(request, ctx.featureset)}.
            ${h.cite_button(request, ctx.featureset)}
        </p>
        ## clld.web.util.helpers alt_representation creates download widget with info button
        <div>${h.alt_representations(request, ctx, doc_position='right', exclude=['snippet.html'])|n}</div>
    </div>
    <p></p>
    % if ctx.id != 'MonPl-06':
    <div class="span4">
        <%util:well title="Values">
            <table class="table table-condensed">
            % for de in ctx.domain:
            <tr>
                <td>${util.coloris_icon_picker(u.icon_from_req(de, request))|n}</td>
                <td>${de}</td>
                <td class="right">${len(de.values)}</td>
            </tr>
            % endfor
            </table>
            ${util.parameter_map_reloader([u.icon_from_req(de, request) for de in ctx.domain])|n}
            <!--${u.value_table(ctx, request)}-->
        </%util:well>
    </div>
    % endif
</div>
% if ctx.id != 'MonPl-06':
${request.get_map('parameter', dt=values_dt).render()}
% endif
${values_dt.render()}




