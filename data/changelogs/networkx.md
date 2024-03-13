## 3.2.1.20240313 (2024-03-13)

networkx: add another overload to OutEdgeView.__call__(). (#11578)

It's common to call the 'edges' property of a DiGraph with an 'nbunch'
argument and no other arguments (see the Examples section of
https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.out_edges.html).
None of the existing overloads allow this.

## 3.2.1.20240210 (2024-02-10)

Fix networkx stub; location of subgraph_view, etc. (#11385)

## 3.2.1.20240205 (2024-02-05)

A new shade of Black (#11362)

## 3.2.1.20240201 (2024-02-01)

Bump networkx to 3.2.1 (#11336)

## 3.1.0.20240116 (2024-01-16)

Add more networkx annotations for networkx.algorithms.dag (#11224)

## 3.1.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 3.1.0.20231220 (2023-12-20)

Add some missing networkx annotations (#11181)

Fix annotation for networkx.subgraph_view (#11180)

## 3.1.0.0 (2023-12-16)

Add networkx stubs (#10544)

Co-authored-by: Avasam <samuel.06@hotmail.com>
Co-authored-by: Audrey Dutcher <audrey@rhelmot.io>

