<%! from clld.web.util import doi %>${', '.join(c.name for c in list(ctx.primary_contributors))}. ${request.dataset.published.year if request.dataset.published else ctx.updated.year}. ${getattr(ctx, 'citation_name', str(ctx))}.
In: ${request.dataset.formatted_editors()|n} (eds.)
% if req.registry.settings.get('clld.zenodo_version_tag') and req.registry.settings.get('clld.zenodo_version_doi'):
${request.dataset.name} (${req.registry.settings['clld.zenodo_version_tag']}) [Data set]. Zenodo.
${doi.url(req.registry.settings['clld.zenodo_version_doi'])}
% elif req.registry.settings.get('clld.zenodo_concept_doi'):
${request.dataset.name} [Data set]. Zenodo.
${doi.url(req.registry.settings['clld.zenodo_concept_doi'])}
% else:
${request.dataset.description}.
${request.dataset.publisher_place}: ${request.dataset.publisher_name}.
% endif
(Available online at ${request.dataset.domain}${request.resource_path(ctx)}, Accessed on ${h.datetime.date.today()}.)