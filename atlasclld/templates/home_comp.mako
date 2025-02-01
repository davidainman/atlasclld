<%inherit file="atlasclld.mako"/>
<%namespace name="util" file="util.mako"/>
<%! active_menu_item = "dataset" %>

<%def name="contextnav()">
    ${util.contextnavitem('credits', label='Acknowledgments')}
    ${util.contextnavitem('legal', label='Legal')}
    ${util.contextnavitem('download', label='Download')}
    ${util.contextnavitem('contact', label='Contact')}
</%def>
${next.body()}