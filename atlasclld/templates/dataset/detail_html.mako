<%inherit file="../home_comp.mako"/>
<%block name="title">${_('Home')}</%block>

<%def name="sidebar()">
    <div class="well">
        <!--<h3>Sidebar</h3>-->
        <p>
            ATLAs is a regularly updated database. To submit corrections or queries about the data present in ATLAs, please click on the bell icons that appear on features, which allow you to send an email to the editorial team. You may also find information about how to reach us on the <a href="${request.route_url('contact')}">contact page</a>.
        </p>
    </div>
</%def>

<h2>Welcome to ATLAs online</h2>

<p class="lead">
    The Areal Typology of Languages of the Americas (ATLAs) is a database of typological features targeting areal linguistic structures in North and South America, collected from language descriptions by a team of <a href="${request.route_url('contributors')}">21 authors</a>.
</p>
<p>
    ATLAs was first published in 2025 in (TODO:link) Scientific Data. We periodically publish corrections, and thus any citation of the ATLAs data should include a link to the version used, as listed on ${h.external_link('https://doi.org/10.5281/zenodo.14504419', label='Zenodo')}.
</p>
<p>
    The language sample of ATLAs includes 325 languages, of which 115 are in North America and 105 in South America. Their geographic distribution and family affiliation can be seen in the map below.
</p>
<div class="span12 alert">
    <img src="${request.static_url('atlasclld:static/atlas-map.png')}"
         class="img-polaroid"/>
    <div>
        <small>
            The ATLAs language sample.
        </small>
    </div>
</div>
<p>
    The features of ATLAs were designed in order to maximize areal signal, with depth of coverage taking a priority over breadth. Some common typological features are thus not included. However, those features which are present are organized into feature sets, which as a whole are intended to cover their linguistic domain exhaustively. This design choice maximizes the chance that areally-relevant variation present within the typological domains surveyed is captured. To the extent possible, we tried not to include grammatical structures which could be identified as the result of recent contact between Indigenous American and European languages.
</p>
<p>
    Features are further designed with the intention of maximizing logical independence, or making it possible to staightforwardly manipulate the data in order to attain logically independent variables. Many features contain &lt;NA&gt; states — not applicable — in order to avoid features that encode the same information multiple times. For example, if a language has no verbal indexation, its verbal alignment is &lt;NA&gt; — not applicable — rather than &lt;neutral&gt; — a neutral alignment.
</p>

<h3>How to use ATLAs online</h3>

<p>
    ATLAs online requires a browser with Javascript enabled.
</p>
<p>
    Data in ATLAs is organized into feature sets, which cover a typological domain or theme, and each feature set includes multiple features. Feature set descriptions provide lists of associated features, their linguistic motivation, coding methodology, and results, and can be accessed through the tab "Feature Sets" in the navigation bar. Alternatively, features can be accessed directly, without going through feature sets description, in the "Features" tab of the same navigation bar. 
</p>
<p>
    You can also browse and search for languages through the tab "Languages" on the navigation bar. Here, features can be viewed collectively for individual languages.
</p>
<p>
    The contributors to the database are given in the "Contributors" tab, which associates individual authors and contributors with particular feature sets.
</p>
<p>
    Finally, you can search for references through the "References" tab.
</p>

<h3>How to cite ATLAs</h3>
<p>
    If you are citing the ATLAs database as a whole without using any associated data, you should cite the database as published in ${h.external_link('https://www.nature.com/articles/s41597-025-05169-4', label='Scientific Data')}.
</p>
<p>
    If you are using data from multiple feature sets of ATLAs, you should cite the database as a whole, as published in  ${h.external_link('https://www.nature.com/articles/s41597-025-05169-4', label='Scientific Data')}, as well as ${h.external_link('https://doi.org/10.5281/zenodo.14504419', label='the specific version of the database from Zenodo')} you are using.
</p>
<p>
    If you are citing a particular feature set description (without using any associated data), you can cite only the specific feature set, as seen in the feature set page.
</p>
<p>
    If you are using data from a specific feature set, then you should cite the feature set in question, as well as the database publication in ${h.external_link('https://www.nature.com/articles/s41597-025-05169-4', label='Scientific Data')} and ${h.external_link('https://doi.org/10.5281/zenodo.14504419', label='the specific version of the database from Zenodo')}. 
</p>

<h3>Terms of use</h3>
<p>
    The content of this web site is published under a Creative Commons Licence. We invite scholars and users to use this data for further linguistic study, and look forward to comments, feedback, and questions.
</p>

<h3>Funding</h3>
<p>
    ATLAs was funded by the Swiss National Science Foundation Sinergia Project "Out of Asia" (CRSII5_183578), the University of Zurich, and the Swiss National Centre of Competence in Research Evolving Language.
</p>
<div class="span12">
    <table width="100%">
        <tr>
            <td style="text-align: center" width="33%">
                <a href="https://www.snf.ch/"><img src="${req.static_url('atlasclld:static/snsf_entire.png')}"
                     alt="https://www.snf.ch/" width="210"></a>
            </td>
            <td style="text-align: center" width="33%">
                <a href="https://uzh.ch/"><img src="${req.static_url('atlasclld:static/uzh_entire.png')}"
                     alt="https://uzh.ch/" width="200"></a>
            </td>
            <td style="text-align: center" width="33%">
                <a href="https://evolvinglanguage.ch/"><img src="${req.static_url('atlasclld:static/evolang_entire.png')}" alt="https://evolvinglanguage.ch/" width="170"></a>
            </td>
    </table>
</div>