import graphviz

class DataFlowDiagram(graphviz.Digraph):
    def __init__(self, title: str) -> None:
        super().__init__(title, engine='fdp')

        self.attr("graph", fontname="Arial", fontsize="12", overlap="false", beautify="true")
        self.attr("node", fontname="Arial", fontsize="12", margin="0.02")

    def add_data_flow(self, tail_name: str, head_name: str, label: str, **overwrites: str) -> None:
        self.edge(tail_name, head_name, label,
                  fontname="Arial",
                  fontsize="8",
                  arrowhead="normal",
                  arrowsize="0.5",
                  **overwrites
                  )
    
    def add_asset(self, name: str, label: str, shape: str, **overwrites: str) -> None:
        self.node(name, label, shape=shape, **overwrites)

