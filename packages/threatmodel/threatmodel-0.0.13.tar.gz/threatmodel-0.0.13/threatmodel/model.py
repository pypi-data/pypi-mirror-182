from typing import Dict, List, Optional, TYPE_CHECKING, cast
from tabulate import tabulate

from .asset import Asset
from .component import Component
from .element import Element
from .mitigation import Mitigation
from .node import Construct, TagMixin
from .data_flow import DataFlow
from .common import is_notebook, is_ci
from .diagram import DataFlowDiagram
from .table_format import TableFormat
from .threatlib import DEFAULT_THREATLIB
from .otm import OpenThreatModel, OpenThreatModelProject

if TYPE_CHECKING:
    from .threat import Threat, Threatlib,  Risk, Treatment


class Model(Construct, TagMixin):
    @staticmethod
    def of(construct: "Construct") -> "Model":
        def lookup(c: "Construct") -> "Model":
            if isinstance(c, Model):
                return c

            if c.node.scope is None:
                raise ValueError(
                    "No model could be identified for the construct at path"
                )

            return lookup(c.node.scope)

        return lookup(construct)

    def __init__(self, name: str, description: str = "", owner: str = "", owner_contact: str = "", threatlib: Optional["Threatlib"] = None) -> None:
        super().__init__(None, name)

        self.description = description
        self.owner = owner
        self.owner_contact = owner_contact

        if threatlib is None:
            self.threatlib = DEFAULT_THREATLIB
        else:
            self.threatlib = threatlib

        self._risks: Dict[str, "Risk"] = dict()

    @property
    def assets(self) -> List["Asset"]:
        return cast(List["Asset"], list(filter(lambda c: isinstance(c, Asset), self.node.find_all())))

    @property
    def components(self) -> List["Component"]:
        return cast(List["Component"], list(filter(lambda c: isinstance(c, Component), self.node.find_all())))

    @property
    def data_flows(self) -> List["DataFlow"]:
        return cast(List["DataFlow"], list(filter(lambda c: isinstance(c, DataFlow), self.node.find_all())))

    @property
    def mitigations(self) -> List["Mitigation"]:
        return cast(List["Mitigation"], list(filter(lambda c: isinstance(c, Mitigation), self.node.find_all())))

    @property
    def otm(self) -> "OpenThreatModel":
        return OpenThreatModel(
            project=OpenThreatModelProject(
                name=self.name,
                id=self.id
            ),
            data_flows=[df.otm for df in self.data_flows],
        )

    def is_notebook(self) -> bool:
        return is_notebook()

    def is_ci(self) -> bool:
        return is_ci()

    def get_threat_by_id(self, id: str) -> Optional["Threat"]:
        return self.threatlib.get(id)

    def get_risk_by_id(self, id: str) -> "Risk":
        return self._risks[id]

    def treat_risk(self, id: str, treatment: "Treatment") -> None:
        self._risks[id].treat(treatment)

    def risks_table(self, table_format: TableFormat = TableFormat.SIMPLE) -> str:
        headers = ["SID", "Severity", "Category",
                   "Name", "Affected", "Treatment"]
        table = []
        for risk in self._risks.values():
            table.append([risk.id, risk.severity, risk.category, risk.name,
                         risk.target, risk.treatment])

        return tabulate(table, headers=headers, tablefmt=str(table_format))

    def data_flow_diagram(self, auto_view=True):
        diagram = DataFlowDiagram(self.name)

        for df in self.data_flows:
                diagram.add_data_flow(
                    df.source.id, 
                    df.destination.id, 
                    f"{df.protocol}: {df.name}", 
                    **df.overwrite_edge_attrs,
                )
        
        for c in self.components:    
                diagram.add_asset(
                    c.id, 
                    c.name, 
                    c.shape, 
                    **c.overwrite_node_attrs,
        )

        if auto_view is False or self.is_ci():
            diagram.save()
            return

        if self.is_notebook():
            try:
                from IPython import display
                display.display(diagram)
            except ImportError:
                diagram.view()
        else:
            diagram.view()

    def evaluate(self) -> None:
        for c in self.node.find_all():
            if isinstance(c, Element):
                self._add_risk(*c.risks)

    def _add_risk(self, *risks: "Risk") -> None:
        for risk in risks:
            self._risks[risk.id] = risk

