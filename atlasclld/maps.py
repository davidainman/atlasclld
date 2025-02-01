from clld.web.maps import ParameterMap, FilterLegend, Layer, Legend
from clld.web.util.helpers import JS, map_marker_img
from clld.web.util.htmllib import HTML, literal
from atlasclld.adapters import GeoJsonFeature

class FeatureMap(ParameterMap):
    def __init__(self, ctx, req, eid='map', col=None, dt=None):
        self.col, self.dt = col, dt
        ParameterMap.__init__(self, ctx, req, eid=eid)

    def get_options(self):
        if (self.ctx.datatype == "multi-valued" or self.ctx.datatype == "frequency"):
            return {'max_zoom': 6, 'icon_size': 35}
        else:
            return {'max_zoom': 6, 'icon_size': 17}

    def get_layers(self):
        #if self.ctx.multivalued:
        yield Layer(
            self.ctx.id,
            self.ctx.name,
            GeoJsonFeature(self.ctx).render(self.ctx, self.req, dump=False)
        )
        # else:
        #     for layer in super(FeatureMap, self).get_layers():
        #         yield layer

    def get_legends(self):
        #if self.ctx.multivalued:
        def value_li(de):
            return HTML.label(
                map_marker_img(self.req, de),
                literal(de),
                style='margin-left: 1em; margin-right: 1em;')

        yield Legend(self, 'values', map(value_li, self.ctx.domain), label='Legend')

        # for legend in super(FeatureMap, self).get_legends():
        #     yield legend
        #
        # yield FilterLegend(self, 'WILLSEE?', col=self.col, dt=self.dt)


def includeme(config):
    config.register_map("parameter", FeatureMap)

