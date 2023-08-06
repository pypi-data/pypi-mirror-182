"""THIS IS SO GROSS I'M SORRY."""

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


super_visit_hint = HTML5Translator.visit_hint
super_depart_hint = HTML5Translator.depart_hint
super_visit_title = HTML5Translator.visit_title
super_depart_title = HTML5Translator.depart_title
super_visit_paragraph = HTML5Translator.visit_paragraph
super_depart_paragraph = HTML5Translator.depart_paragraph


def visit_title(self, node: nodes.title):
    if isinstance(node.parent, nodes.hint) and node.parent.index(node) == 0:
        raise nodes.SkipNode

    if isinstance(node.parent, nodes.section):
        if str(node) == getattr(self, "_previous_title", ""):
            raise nodes.SkipNode

        self._previous_title = str(node)

    super_visit_title(self, node)


def depart_title(self, node: nodes.title):
    super_depart_title(self, node)
    if isinstance(node.parent, nodes.hint):
        self.body.append('<details class="admonition-body">')
        self.body.append("<summary></summary>")


def visit_block_quote(self, node: nodes.block_quote):
    self.body.append('<blockquote class="blockquote p-4 border rounded">')


def depart_block_quote(self, node: nodes.block_quote):
    self.body.append("</blockquote>")


def visit_attribution(self, node: nodes.attribution):
    self.body.append('<footer class="blockquote-footer">')


def depart_attribution(self, node: nodes.attribution):
    self.body.append("</footer>")


def visit_definition_list(self, node: nodes.definition_list):
    self.body.append('<dl class="row">')


def depart_definition_list(self, node: nodes.definition_list):
    self.body.append("</dl>")


def visit_term(self, node: nodes.term):
    self.body.append('<dt class="col-sm-4">')


def depart_term(self, node: nodes.term):
    self.body.append("</dt>")


def visit_definition(self, node: nodes.definition):
    self.body.append('<dd class="col-sm-8">')


def depart_definition(self, node: nodes.definition):
    self.body.append("</dd>")


def visit_admonition(self, node: nodes.Element, name: str = ""):
    self.body.append(
        self.starttag(
            node, "div", CLASS=("admonition py-3 px-4 my-4 rounded border " + name)
        )
    )


def depart_admonition(self, node: nodes.Element):
    self.body.append("</div>\n")


def visit_attention(self, node: nodes.note):
    visit_admonition(self, node, "attention")


def visit_caution(self, node: nodes.note):
    visit_admonition(self, node, "caution")


def visit_danger(self, node: nodes.note):
    visit_admonition(self, node, "danger")


def visit_error(self, node: nodes.note):
    visit_admonition(self, node, "error")


def visit_important(self, node: nodes.note):
    visit_admonition(self, node, "important")


def visit_tip(self, node: nodes.note):
    visit_admonition(self, node, "tip")


def visit_warning(self, node: nodes.note):
    visit_admonition(self, node, "warning")


def visit_note(self, node: nodes.note):
    visit_admonition(self, node, "note")


def visit_paragraph(self, node: nodes.paragraph):
    self.body.append(self.starttag(node, "p", CLASS=" ".join(node["classes"])))


def depart_paragraph(self, node: nodes.paragraph):
    super_depart_paragraph(self, node)
    if "admonition-title" in node["classes"] and isinstance(node.parent, nodes.hint):
        self.body.append("<details>")
        self.body.append("<summary></summary>")


def depart_hint(self, node: nodes.hint):
    self.body.append("</details>")
    super_depart_hint(self, node)


def setup(app: Sphinx) -> None:
    app.add_node(
        nodes.title,
        html=(visit_title, depart_title),
        override=True,
    )
    app.add_node(
        nodes.hint,
        html=(super_visit_hint, depart_hint),
        override=True,
    )
    app.add_node(
        nodes.block_quote, html=(visit_block_quote, depart_block_quote), override=True
    )
    app.add_node(
        nodes.attribution, html=(visit_attribution, depart_attribution), override=True
    )
    app.add_node(
        nodes.definition_list,
        html=(visit_definition_list, depart_definition_list),
        override=True,
    )
    app.add_node(nodes.term, html=(visit_term, depart_term), override=True)
    app.add_node(
        nodes.definition, html=(visit_definition, depart_definition), override=True
    )
    app.add_node(
        nodes.admonition, html=(visit_admonition, depart_admonition), override=True
    )
    app.add_node(
        nodes.attention, html=(visit_attention, depart_admonition), override=True
    )
    app.add_node(nodes.caution, html=(visit_caution, depart_admonition), override=True)
    app.add_node(nodes.danger, html=(visit_danger, depart_admonition), override=True)
    app.add_node(nodes.error, html=(visit_error, depart_admonition), override=True)
    app.add_node(
        nodes.important, html=(visit_important, depart_admonition), override=True
    )
    app.add_node(nodes.note, html=(visit_note, depart_admonition), override=True)
    app.add_node(nodes.tip, html=(visit_tip, depart_admonition), override=True)
    app.add_node(nodes.warning, html=(visit_warning, depart_admonition), override=True)
    app.add_node(
        nodes.paragraph, html=(visit_paragraph, depart_paragraph), override=True
    )
