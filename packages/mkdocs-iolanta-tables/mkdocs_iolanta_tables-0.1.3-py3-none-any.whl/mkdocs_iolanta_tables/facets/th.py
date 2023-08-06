from iolanta.facet import Facet
from mkdocs_iolanta_tables.models import TABLE
from octadocs.iolanta import render


class Th(Facet):
    """Render a table column header."""

    def render(self):
        """Render the column."""
        return render(
            node=self.iri,
            iolanta=self.iolanta,
            environments=[TABLE.th],
        )
