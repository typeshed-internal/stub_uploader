## 3.5.0.20250712 (2025-07-12)

Correct type hints for networkx/algorithms/flow/mincost.pyi (#14395)

## 3.5.0.20250709 (2025-07-09)

networkx: All return types from python-type-stubs (#14256)

## 3.5.0.20250701 (2025-07-01)

[networkx] completed type annotation for `equivalence_classes` (#14352)

## 3.5.0.20250610 (2025-06-10)

[networkx] Correct argument type for from_nested_tuple (#14218)

## 3.5.0.20250531 (2025-05-31)

Bump networkx to 3.5 (#14196)

## 3.4.2.20250527 (2025-05-27)

Bump `importlib` to 3.14 (#14138)

## 3.4.2.20250523 (2025-05-23)

networkx: Add symbols from python-type-stubs (#14084)

## 3.4.2.20250515 (2025-05-15)

Update nx_pylab.pyi: allow node_color to be a list of strings as well (#14057)

networkx: type `is_*` and  `has_*` functions (#14054)

## 3.4.2.20250514 (2025-05-14)

networkx: consistent `Unknown | None = None` (#14027)

## 3.4.2.20250513 (2025-05-13)

networkx: `ignore_missing_stub = false` (#13968)

## 3.4.2.20250509 (2025-05-09)

networkx: add all missing `__all__` (#13956)

## 3.4.2.20250507 (2025-05-07)

networkx: Most nodelist params are collections (#13945)

## 3.4.2.20250426 (2025-04-26)

Fix generics in NetworkX (#13864)

## 3.4.2.20250319 (2025-03-19)

[networkx] Fix a few annotations in AtlasView and Graph (#13656)

## 3.4.2.20250312 (2025-03-12)

[networkx] Fix argument type of node_connected_component (#13612)

## 3.4.2.20250304 (2025-03-04)

Add edges() override in MultiGraph to support the "keys" argument (#13567)

Enable Ruff PLC (Pylint Convention) (#13306)

## 3.4.2.20250227 (2025-02-27)

[networkx] Add annotations for `MultiDiGraph` (#13319)

Extract NetworkX types from docstrings (#13458)

## 3.4.2.20241227 (2024-12-27)

Enable Ruff PGH rules (#13304)

## 3.4.2.20241115 (2024-11-15)

Update networkx stubs for 3.4.2 (#13001)

## 3.3.0.20241112 (2024-11-12)

Remove numpy pins from several stubs (#12993)

## 3.3.0.20241020 (2024-10-20)

Update mypy to 1.12.0 (#12859)

## 3.3.0.20241009 (2024-10-09)

Bump networkx to 3.3 (#11727)

## 3.2.1.20240918 (2024-09-18)

 fix: weight parameter type for networkx.algorithms.shortest_paths (#12663)

## 3.2.1.20240907 (2024-09-07)

Fix networkx `DiDegreeView.__call__()` can return `int` (#12472)

Fix networkx `DiDegreeView.__call__()`

`DiDegreeView.__call__()` can return an integer if a single node is specified, as is also documented in the docstrings of the method:

https://github.com/networkx/networkx/blob/89718e0514bded93ded5b00aed755a4474c1dc6f/networkx/classes/digraph.py#L1198-L1199

Implementation:

https://github.com/networkx/networkx/blob/89718e0514bded93ded5b00aed755a4474c1dc6f/networkx/classes/reportviews.py#L436-L437

## 3.2.1.20240820 (2024-08-20)

Pin numpy in various stubs (#12554)

## 3.2.1.20240813 (2024-08-13)

Add graph attribute to networkx.Graph (#12505)

## 3.2.1.20240811 (2024-08-11)

networkx: Fix stubtest errors and remove numpy version pin (#12477)

## 3.2.1.20240806 (2024-08-06)

Bump mypy to 1.11.1 (#12463)

## 3.2.1.20240703 (2024-07-03)

add stubs for networx.has_path (#12252)

## 3.2.1.20240618 (2024-06-18)

Pin various stubs to numpy to < 2 (#12152)

Fixes #12146

## 3.2.1.20240531 (2024-05-31)

[networks] Fix some functions requiring DiGraph objects (#12066)

## 3.2.1.20240518 (2024-05-18)

add networkx.topological_generations (#11927)

## 3.2.1.20240425 (2024-04-25)

[networkx] Fix incremental_closeness_centrality argument type (#11828)

## 3.2.1.20240424 (2024-04-24)

Annotate a few NetworkX algorithm types (#11811)

## 3.2.1.20240331 (2024-03-31)

Remove bare Incomplete annotations in third-party stubs (#11671)

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

