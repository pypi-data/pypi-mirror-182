from typing import TYPE_CHECKING

from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst.roles import set_classes
from docutils import nodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class OverrideAdmonition(BaseAdmonition):
    optional_arguments = 1

    def run(self):
        if self.node_class is nodes.admonition or not self.arguments:
            return super().run()

        # All other admonition types can have a title (the first optional
        # argument). If we have a title, it needs to be included in the
        # admonition node's content so it can be parsed along with everything
        # else.

        set_classes(self.options)
        self.assert_has_content()
        text = f"{self.arguments[0]}\n" + "\n".join(self.content)
        admonition_node = self.node_class(text, **self.options)
        self.add_name(admonition_node)

        title_text = self.arguments[0]
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        title = nodes.paragraph(title_text, "", *textnodes)
        title["classes"] = ["h5", "admonition-title"]

        title.source, title.line = self.state_machine.get_source_and_line(self.lineno)
        admonition_node += title
        admonition_node += messages

        self.state.nested_parse(self.content, self.content_offset, admonition_node)

        return [admonition_node]


class Attention(OverrideAdmonition):

    node_class = nodes.attention


class Caution(OverrideAdmonition):

    node_class = nodes.caution


class Danger(OverrideAdmonition):

    node_class = nodes.danger


class Error(OverrideAdmonition):

    node_class = nodes.error


class Hint(OverrideAdmonition):

    node_class = nodes.hint


class Important(OverrideAdmonition):

    node_class = nodes.important


class Note(OverrideAdmonition):

    node_class = nodes.note


class Tip(OverrideAdmonition):

    node_class = nodes.tip


class Warning(OverrideAdmonition):

    node_class = nodes.warning


def setup(app: "Sphinx") -> None:
    app.add_directive("attention", Attention, override=True)
    app.add_directive("caution", Caution, override=True)
    app.add_directive("danger", Danger, override=True)
    app.add_directive("error", Error, override=True)
    app.add_directive("hint", Hint, override=True)
    app.add_directive("important", Important, override=True)
    app.add_directive("note", Note, override=True)
    app.add_directive("tip", Tip, override=True)
    app.add_directive("warning", Warning, override=True)
