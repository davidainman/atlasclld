<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%! active_menu_item = "languages" %>
<%block name="title">Languages</%block>
<%block name="head">
    <link href="${request.static_url('clld:web/static/css/select2.css')}" rel="stylesheet">
    <script src="${request.static_url('clld:web/static/js/select2.js')}"></script>
</%block>

<h2>Languages</h2>

<p>
    ATLAs includes 325 languages, of which 220 are spoken in the Americas. Language names and glottocodes are according to ${h.external_link('https://glottolog.org/', label='Glottolog')} ${h.external_link('https://zenodo.org/records/10804357', label='v5.0')}.
</p>
<div class="clearfix"> </div>
${ctx.render()}
