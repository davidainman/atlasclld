import collections
import functools

from pyramid.config import Configurator

from clld_glottologfamily_plugin import util

from clldutils import svg
from clld.interfaces import (
    IMapMarker,
    IValueSet,
    IValue,
    IDomainElement,
    ILanguage,
    IParameter,
    IUnit,
    IContributor,
    IContribution,
    ICtxFactoryQuery,
)
from clldutils.svg import pie, icon, data_url
from clld.web.adapters.base import adapter_factory
from clld.web.util.helpers import link
from clld.web.app import CtxFactoryQuery, menu_item
from clld import common

from markdown.extensions.toc import TocExtension
from markdown.extensions import footnotes

# we must make sure custom models are known at database initialization!
from atlasclld import models
from atlasclld.interfaces import OaaMapMarker


def map_marker(ctx, req):
    """allow for user-selectable markers.

    we have to look up a possible custom selection from the url params.
    """
    icon = None

    if IValue.providedBy(ctx):
        icon = req.params.get(
            "v%s" % ctx.domainelement.number, ctx.domainelement.jsondata["icon"]
        )
    elif IDomainElement.providedBy(ctx):
        icon = req.params.get("v%s" % ctx.number, ctx.jsondata["icon"])
    elif ILanguage.providedBy(ctx):
        # hard coded icon
        icon = req.params.get(ctx.id, "c0000dd")
        # icon = req.params.get(ctx.id, ctx.genus.icon)

    if icon:
        if "'" in icon:
            icon = icon.split("'")[0]
        if len(icon) > 4 and len(icon) != 7:
            icon = icon[:4]
        if len(icon) == 4:
            icon = icon[0] + 2 * icon[1] + 2 * icon[2] + 2 * icon[3]
        if icon.startswith("a"):
            return svg.data_url(svg.icon("c000000", opacity="0"))
        try:
            return svg.data_url(svg.icon(icon))
        except KeyError:
            return ""


class CtxFactory(CtxFactoryQuery):

    def refined_query(self, query, model, req):
        if model == common.Contribution:
            query = query.options()
        if model == models.ATLAsLanguage:
            pass
        return query

class LanguageByFamilyMapMarker(util.LanguageByFamilyMapMarker):
    def __call__(self, ctx, req):
        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)


def render_parameter(req, objid, table, session, ids=None, **kw):
    obj = common.Parameter.get(objid)
    return link(req, obj, label='{}: {}'.format(obj.id, obj.question))


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    settings["route_patterns"] = { 'credits': '/about/credits'}
    settings['clld_markdown_plugin'] = {
        'model_map': {
            'ValueTable': common.ValueSet,
            'Contributor': common.Contributor,
        },
        'renderer_map': {
            'ParameterTable': render_parameter,
        },
        'function_map': {},
        'keep_link_labels': True,
        'extensions': [TocExtension(baselevel=2, toc_depth=3), 'footnotes']
    }
    config = Configurator(settings=settings)

    config.include("clld.web.app")
    config.include('clld_markdown_plugin')

    config.include("clldmpg")

    config.add_route("featuresets", "/contributions")
    config.register_resource('contribution', models.ATLAsFeatureSet, IContribution, with_index=True)

    config.add_route("features", "/parameters")
    config.register_resource('parameter', models.ATLAsParameter, IParameter, with_index=True)

    # config.add_route("ATLAsvalues", "/values")
    # config.register_resource("value", models.ATLAsValue, IValue, with_index=True)

    config.registry.registerUtility(CtxFactory(), ICtxFactoryQuery)
    config.registry.registerUtility(OaaMapMarker(), IMapMarker)
    config.add_route("references", "/sources")
    # config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)
    config.register_menu(
        ('dataset', functools.partial(menu_item, 'dataset', label='Home')),
        ('featuresets', functools.partial(menu_item, 'featuresets', label='Feature Sets')),
        ('parameters', functools.partial(menu_item, 'features', label='Features')),
        ('languages', functools.partial(menu_item, 'languages', label='Languages')),
        ('contributors', functools.partial(menu_item, 'contributors', label='Contributors')),
        ('references', functools.partial(menu_item, 'references', label='References')),
    )

    return config.make_wsgi_app()
