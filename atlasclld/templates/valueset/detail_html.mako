<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributions" %>


<h2>${_('Datapoint:')} ${h.link(request, ctx.language)}/${h.link(request, ctx.parameter)}</h2>

% if ctx.description:
${h.text2html(h.Markup(ctx.markup_description) if ctx.markup_description else ctx.description, mode='p')}
% endif

<h4 class="question">${ctx.parameter.question}</h4>
<table id="Value" cellpadding="0" cellspacing="0" border="0" class="table table-bordered order-column compact stripe dataTable no-footer" role="grid">
    <thead>
        <tr role="row">
            <th class="left" tabindex="0" rowspan="1" colspan="1">ID</th>
            <th class="left" tabindex="0" rowspan="1" colspan="1">Value</th>

% if ctx.parameter.datatype == 'frequency':
% if ctx.parameter.featureset.id == 'Align':
            <th class="left" tabindex="0" rowspan="1" colspan="1">Proportion</th>
% else:
            <th class="left" tabindex="0" rowspan="1" colspan="1">Count</th>
% endif
% endif
            <th class="left" tabindex="0" rowspan="1" colspan="1">Remark</th>
        </tr>
    </thead>
    <tbody>
        % for i, value in enumerate(ctx.values):
        <tr role="row" class="odd">
        <td class=" left">
            ${h.map_marker_img(request, value)} ${value}
        </td>
        <td class=" left">
            ${ctx.values[i].value}
        </td>
% if ctx.parameter.datatype == 'frequency':
% if ctx.parameter.featureset.id == 'Align':
        <td class=" left">
            ${ctx.values[i].frequency}
        </td>
% else:
        <td class=" left">
            ${ctx.values[i].count}
        </td>
% endif
% endif
        <td class=" left">
            ${ctx.values[i].remark}
        </td>
        % endfor
    </tbody>
</table>
<%def name="sidebar()">
<div class="well well-small">
<dl>
    <dt class="contribution">${_('Feature set')}:</dt>
    <dd class="contribution">
        ${h.link(request, ctx.contribution)}
        by
        ${h.linked_contributors(request, ctx.contribution)}
        ${h.button('cite', onclick=h.JSModal.show(ctx.contribution.name, request.resource_url(ctx.contribution, ext='md.html')))}
    </dd>
    <dt class="language">${_('Language')}:</dt>
    <dd class="language">${h.link(request, ctx.language)}</dd>
    <dt class="parameter">${_('Feature')}:</dt>
    <dd class="parameter">${h.link(request, ctx.parameter)}</dd>
    % if ctx.references or ctx.source:
    <dt class="source">${_('Source')}:</dt>
        % if ctx.source:
        <dd>${ctx.source}</dd>
        % endif
        % if ctx.references:
        <dd class="source">${h.linked_references(request, ctx)|n}</dd>
        % endif
    % endif
    ${util.data(ctx, with_dl=False)}
</dl>
</div>
</%def>
