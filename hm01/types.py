from typing import Iterator, Protocol

from hm01.basics import IntangibleSubgraph

class AbstractCluterer(Protocol):
    def cluster(self, graph) -> Iterator[IntangibleSubgraph]:
        pass

    def cluster_without_singletons(self, graph) -> Iterator[IntangibleSubgraph]:
        for cluster in self.cluster(graph):
            if cluster.n() > 1:
                yield cluster