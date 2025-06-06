from clld import interfaces
from atlasclld.md import BibTex, TxtCitation
from clld.web.adapters import GeoJsonParameter
from clld.db.meta import DBSession
from clld.db.models import common
from clldutils.svg import data_url, style
from atlasclld.util import ATLAsPie
from sqlalchemy.orm import joinedload


class GeoJsonFeature(GeoJsonParameter):
    def feature_iterator(self, ctx, req):
        for vs in DBSession.query(common.ValueSet).filter(common.ValueSet.parameter_pk == ctx.pk).options(
                joinedload(common.ValueSet.language)):
            yield vs

    def feature_properties(self, ctx, req, valueset):
        res = {
            'values': list(valueset.values),
            'label': valueset.language.name }
        if valueset.parameter.datatype == 'integer':
            val = valueset.values[0]
            if not val.domainelement.jsondata.get('icon'):
                res['icon'] = data_url(ATLAsPie([1], ['#ffffff'], width=2.6, opacity=0.0, stroke_circle=True))
            if val.domainelement and val.domainelement.jsondata.get('icon'):
                res['icon'] = data_url(ATLAsPie([1], [val.domainelement.jsondata['icon']], width=25, opacity=1, stroke_circle=True))
        if valueset.parameter.datatype != 'integer' and not valueset.values[0].domainelement.jsondata.get('icon'):
            res['icon'] = data_url(ATLAsPie([1], ['#ffffff'], width=3, opacity=0.0, stroke_circle=True))
        return res

    def featurecollection_properties(self, ctx, req):
        marker = req.registry.getUtility(interfaces.IMapMarker)
        res = {
            'name': getattr(ctx, 'name', 'Values'),
            'domain': [
                {'icon': marker(ctx, req), 'id': de.id, 'name': de.name}
                for de in getattr(ctx, 'domain', [])
            ]
        }
        return res

def includeme(config):
    config.register_adapter(GeoJsonFeature, interfaces.IParameter)
    for cls in [BibTex, TxtCitation]:
        for if_ in [interfaces.IRepresentation, interfaces.IMetadata]:
            for adapts in [interfaces.IContribution, interfaces.IDataset]:
                config.register_adapter(cls, adapts, if_, name=cls.mimetype)
