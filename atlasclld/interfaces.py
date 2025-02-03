from collections import Counter

from clld.interfaces import IValueSet, IValue, IDomainElement, IMapMarker
from clld.web.icon import MapMarker
from clldutils.svg import data_url, style
from atlasclld.util import ATLAsPie

class AtlasMapMarker(MapMarker):
    @staticmethod
    def pie(*slices):
        return data_url(ATLAsPie(
            [float(p[0]) for p in slices],
            [p[1] for p in slices],
            stroke_circle=True,
        ))

    def __call__(self, ctx, req):
        if IDomainElement.providedBy(ctx):
            slices = Counter()
            icon = ctx.jsondata['icon']
            if icon :
                for value in ctx.values:
                    slices[icon] += value.frequency or 1
                return self.pie(*[(v, k) for k, v in slices.most_common()])

        elif IValueSet.providedBy(ctx):
            slices = Counter()
            for value in ctx.values:
                icon = value.domainelement.jsondata['icon']
                if icon and icon.startswith("#"):
                    slices[icon] += value.frequency or 1
            return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValue.providedBy(ctx):
            slices = Counter()
            icon = ctx.domainelement.jsondata['icon']
            if icon and icon.startswith("#"):
                slices[icon] = ctx.frequency or 1
                return self.pie(*[(v, k) for k, v in slices.most_common()])

        else:
            slices = Counter()
            icon = '#ffffff'
            slices[icon] = 1
            return self.pie(*[(v, k) for k, v in slices.most_common()])


def includeme(config):
    config.registerUtility(AtlasMapMarker(), IMapMarker)