from sqlalchemy.orm import joinedload, contains_eager, subqueryload

from clld.web import datatables
from clld.web.datatables.base import Col, LinkCol, DetailsRowLinkCol, DataTable, IdCol
from clld.web.datatables.base import RefsCol as BaseRefsCol
from clld.web.datatables.value import ValueNameCol
from clld.db.meta import DBSession
from clld.db.models import common
from clld.db.models import (
    Value,
    ValueSet,
    ValueSetReference,
)
from sqlalchemy.orm import aliased
from clld.db.util import get_distinct_values, icontains
from clld.web.util.helpers import linked_contributors, link, contactmail, external_link, map_marker_img
from clld.web.util.htmllib import HTML, literal

from atlasclld.models import ATLAsLanguage, ATLAsParameter, ATLAsFeatureSet, ATLAsValue

# special columns
class CommentCol(Col):
    __kw__ = {'bSortable': False, 'bSearchable': False, 'sTitle': ''}

    def format(self, item):
        return contactmail(
            self.dt.req, item.valueset, title="suggest changes")


class AuthorsCol(Col):
    def format(self, item):
        req = self.dt.req
        contribution = self._get_object(item) if self._get_object else item
        chunks = []
        for i, c in enumerate(contribution.primary_contributors):
            if i > 0:
                chunks.append(", ")
            chunks.append(link(req, c))
        if len(chunks) > 2:
            chunks[-2] = " and "
        return HTML.span(*chunks)


class AtlasIdCol(LinkCol):
    __kw__ = {'sClass': 'right', 'input_size': 'mini'}
    
    def get_attrs(self, item):
        return {'label': self.get_obj(item).id}
    
    def search(self, qs):
        if self.model_col:
            return icontains(self.model_col, qs)


class AtlasLanguageCol(LinkCol):
    def search(self, qs):
        return icontains(common.Language.name, qs)

    def order(self):
        return common.Language.name


class AtlasAuthorsCol(Col):
    __kw__ = {'bSearchable': False, 'bSortable': False}

    def format(self, item):
        return HTML.ul(
            *[HTML.li(link(
                self.dt.req, c.contribution)) for c in item.contribution_assocs if c.primary])


class AtlasContributionsCol(Col):
    __kw__ = {'bSearchable': False, 'bSortable': False}

    def format(self, item):
        return HTML.ul(
            *[HTML.li(link(
                self.dt.req, c.contribution)) for c in item.contribution_assocs if not c.primary])


class ContributorsCol(Col):
    def format(self, item):
        req = self.dt.req
        contribution = self._get_object(item) if self._get_object else item
        chunks = []

        for i, c in enumerate(contribution.secondary_contributors):
            if i == 0 and contribution.primary_contributors:
                chunks.append(" with ")
            if i > 0:
                chunks.append(", ")
            chunks.append(link(req, c))
        if len(chunks) > 2:
            chunks[-2] = " and "
        return HTML.span(*chunks)


class RefsCol(BaseRefsCol):

    """Listing sources for the corresponding ValueSet."""

    def get_obj(self, item):
        return item.valueset


class FeaturesetCol(LinkCol):
    def search(self, qs):
        return icontains(ATLAsFeatureSet.name, qs)

    def order(self):
        return ATLAsParameter.featureset_pk


# personalized tables
class Features(datatables.Parameters):
    __constraints__ = [ATLAsFeatureSet]

    def base_query(self, query):
        query = query.join(ATLAsFeatureSet)
        if self.atlasfeatureset:
            query = query.filter(ATLAsParameter.featureset_pk == self.ATLAsfeatureset.pk)
        return query

    def col_defs(self):
        return [
            AtlasIdCol(self, "ID", sTitle="ID", model_col=ATLAsParameter.id, sClass="left"),
            LinkCol(self, "Name", model_col=ATLAsParameter.name, sClass="left"),
            Col(self, "Question", model_col=ATLAsParameter.question, sClass="left"),
            FeaturesetCol(
                self,
                "FeatureSet",
                sTitle="Feature Set",
                sClass="left",
                get_object=lambda i: i.featureset,
                choices=get_distinct_values(ATLAsFeatureSet.name),
            ),
        ]

class Featuresets(datatables.Contributions):
    def col_defs(self):
        return [
            AtlasIdCol(self, "FeatureSet ID", sTitle="ID", model_col=ATLAsFeatureSet.id, sClass="left"),
            LinkCol(self, "Name", sTitle="Name", model_col=ATLAsFeatureSet.name, sClass="left"),
            AuthorsCol(self, "Authors", model_col=ATLAsFeatureSet.authors),
            ContributorsCol(self, "Contributors"),
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            AtlasIdCol(self, "ID", sTitle="Glottocode", sClass="left", model_col=ATLAsLanguage.id),
            LinkCol(self, "Name", sClass="left", model_col=ATLAsLanguage.name),
            Col(self, "Family", sTitle="Family", model_col=ATLAsLanguage.family_name, sClass="left"),
            Col(self, "Macroarea", model_col=ATLAsLanguage.macroarea, sClass="left"),
        ]


class AtlasValueNameCol(ValueNameCol):
    def get_attrs(self, item):
        label = str(item.value) or 'NO_LABEL'
        label = HTML.span(map_marker_img(self.dt.req, item), literal('&nbsp;'), label)
        return {'label': label, 'title': str(item.value)}


class Values(datatables.Values):
    
    def base_query(self, query):
        query = datatables.Values.base_query(self, query)
        if self.parameter:
            query = query.options(joinedload(Value.valueset).joinedload(common.ValueSet.language))
        return query

    def col_defs(self):
        if self.parameter:
            if self.parameter.datatype == "frequency":
                if self.parameter.featureset.id == "Align":
                    return [
                        AtlasLanguageCol(
                            self,
                            "Language ID",
                            sTitle="Language",
                            model_col=ATLAsLanguage.id,
                            sClass="left",
                            get_object=lambda i: i.valueset.language,
                        ),
                        AtlasValueNameCol(self, "Value", sClass="left", choices=[de.name for de in self.parameter.domain]),
                        Col(self, "Proportion", model_col=ATLAsValue.frequency, sClass="left"),
                        Col(self, "Remark", model_col=ATLAsValue.remark, sClass="left"),
                        RefsCol(self, 'Source'),
                        CommentCol(self, 'c'),
                        ]
                else:
                    return [
                        AtlasLanguageCol(
                            self,
                            "Language ID",
                            sTitle="Language",
                            model_col=ATLAsLanguage.id,
                            sClass="left",
                            get_object=lambda i: i.valueset.language,
                        ),
                        AtlasValueNameCol(self, "Value", sClass="left", choices=[de.name for de in self.parameter.domain]),
                        Col(self, "Count", model_col=ATLAsValue.count, sClass="left"),
                        Col(self, "Remark", model_col=ATLAsValue.remark, sClass="left"),
                        RefsCol(self, 'Source'),
                        CommentCol(self, 'c'),
                        ]
            else:
                return [
                    AtlasLanguageCol(
                        self,
                        "Language ID",
                        sTitle="Language",
                        model_col=ATLAsLanguage.id,
                        sClass="left",
                        get_object=lambda i: i.valueset.language,
                    ),
                    AtlasValueNameCol(self, "Value", sClass="left", choices=[de.name for de in self.parameter.domain]),
                    Col(self, "Remark", model_col=ATLAsValue.remark, sClass="left"),
                    RefsCol(self, 'Source'),
                    CommentCol(self, 'c'),
                ]
        if self.language:
            return [
                AtlasIdCol(
                     self, 
                     "Parameter ID", 
                     sTitle="Feature ID", 
                     sClass="left", 
                     model_col=ATLAsParameter.id,
                     get_object=lambda i: i.valueset.parameter),
                LinkCol(
                    self,
                    "Feature ID",
                    sTitle="Feature",
                    model_col=ATLAsParameter.name,
                    sClass="left",
                    get_object=lambda i: i.valueset.parameter,
                ),
                AtlasValueNameCol(
                    self, "Value", model_col=ATLAsValue.value, sClass="left", bSortable=False, bSearchable=False),
                Col(self, "Remark", model_col=ATLAsValue.remark, sClass="left"),
                RefsCol(self, 'Source'),
                CommentCol(self, 'c'),
            ]


class Contributors(datatables.Contributors):
    def col_defs(self):
        return [
            LinkCol(self, "Name", model_col=common.Contributor.name, sClass="left"),
            AtlasAuthorsCol(self, "Author"),
            AtlasContributionsCol(self, "Contributor"),
        ]
    def base_query(self, query):
        return query.filter(common.Contributor.id != 'auto')


def includeme(config):
    # the name of the datatable must be the same as the name given to the route pattern
    config.register_datatable("values", Values)
    config.register_datatable("languages", Languages)
    config.register_datatable("parameters", Features)
    config.register_datatable("contributions", Featuresets)
    config.register_datatable("contributors", Contributors)
