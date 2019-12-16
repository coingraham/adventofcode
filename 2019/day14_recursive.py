from collections import defaultdict
import time
from collections import deque
from math import ceil

another = """1 ORE => 2 A
1 A => 1 B
1 A, 1 B => 1 FUEL"""

test0 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

test1 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

test2 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

real = """118 ORE => 7 GTPZ
6 RNQJN, 4 NQKVW => 4 DTQRC
2 GBXJL => 3 XHBR
4 BPZM => 9 LVDRH
131 ORE => 3 RHBL
2 LFZS => 2 FPRJW
6 GTPZ => 4 VTBTK
8 GPMP, 2 BPNFJ, 3 LFZS => 2 SFGCR
3 GPMP => 4 SPRCM
16 XCDZP, 1 NQKSL => 4 NQKVW
2 BXGD, 3 VJHSV, 1 MGNCW => 8 MGLH
1 XLNTJ => 1 KXBGP
9 PJQWR, 19 NQKVW, 10 GJHWN => 7 ZBGDF
3 VTBTK => 6 CJNQ
12 PJQWR => 1 JNHBR
16 BPZM => 9 MVCH
1 KWPXQ, 1 LVDRH => 6 LFZS
6 VTBTK => 6 XCDZP
1 PZFG, 2 LFZS, 2 CJNQ, 2 FPRJW, 17 MVCH, 7 MGNCW, 26 KXBGP => 6 TBTL
2 DTQRC, 7 NBNLC => 8 BPZM
102 ORE => 3 WNTQ
1 WNTQ => 9 NQKSL
5 XZMH, 1 LPLMR, 13 BXGD => 8 JPFL
1 NQKSL, 6 XCDZP, 2 FCDVQ => 9 GJHWN
6 XZMH => 4 GLDL
23 ZTWR, 4 BPZM => 2 MGNCW
11 GPMP, 19 ZBGDF => 2 XZMH
2 MGNCW, 4 XCDZP, 17 KQLT => 4 VJHSV
1 CJNQ => 7 QHPH
1 RHBL => 8 GBXJL
2 MVCH, 3 KDNT, 6 NBNLC, 26 QHPH, 2 KRKB, 1 MCPDH, 4 XZMH, 6 XHBR => 1 HZMWJ
9 XDLZ => 1 QSXKS
4 GLDL => 6 WJNP
5 MVCH => 3 MCPDH
14 TKGM => 5 LPLMR
1 WVQN => 2 PJQWR
4 KWPXQ => 6 FCDVQ
10 DTQRC, 27 TBTL, 9 HZMWJ, 41 XVGP, 2 TPZFL, 54 WNTQ, 85 RHBL, 5 WCZK, 2 QVSB, 28 SPRCM => 1 FUEL
15 RNQJN, 1 PJQWR, 2 NBNLC => 4 TKGM
126 ORE => 5 WVQN
10 NBNLC => 3 BWMD
2 SFGCR, 1 NQKSL, 1 KRKB => 1 WGQTF
2 MLWN => 5 ZTWR
12 DTQRC, 3 NQKVW, 9 NBNLC => 8 BPNFJ
10 SFGCR, 1 PZFG, 2 ZVFVH, 12 WJNP, 14 WGQTF, 1 JNHBR, 8 FPRJW => 3 QVSB
2 MCPDH => 8 XVGP
19 JPFL => 4 TPZFL
5 GBXJL => 6 MLWN
9 TKGM => 5 KDNT
1 NQKVW, 15 PJQWR => 9 XDLZ
2 QHPH, 2 JNHBR => 1 ZVFVH
189 ORE => 6 KWPXQ
5 KRKB, 3 MGLH => 6 WCZK
3 NBNLC, 8 BWMD => 7 KRKB
1 ZBGDF, 6 XDLZ => 4 GPMP
11 XDLZ, 1 QSXKS => 2 BXGD
2 KRKB, 1 GJHWN => 1 XLNTJ
3 ZTWR => 4 RNQJN
15 FCDVQ, 3 MLWN => 4 NBNLC
1 KDNT, 1 XZMH, 8 BXGD => 1 KQLT
2 WJNP => 3 PZFG"""

input = real.splitlines()

formulas = [x for x in input]

reactions = {}
resource_totals = defaultdict(int)

for i in formulas:
    a, b = i.split(" => ")
    a_list = a.split(", ")
    how_many, name = b.split(" ")
    reactions[name] = {"requirement": int(how_many)}

    for c in a_list:
        m, n = c.split(" ")
        if "children" not in reactions[name]:
            reactions[name].update(dict(children=[]))
        reactions[name]["children"].append((n, int(m)))


def get_child_resources(node):
    adjustment = (resource_totals[node] + (reactions[node]["requirement"] - 1)) // reactions[node]["requirement"]
    resource_totals[node] -= reactions[node]["requirement"] * adjustment
    for k, v in [(j[0], j[1]) for j in reactions[node]["children"]]:
        resource_totals[k] += adjustment * v
        # time.sleep(1)
        if k == "ORE":
            pass
        else:
            get_child_resources(k)


# Part One
# resource_totals["FUEL"] = 1
# get_child_resources("FUEL")
# print(resource_totals["ORE"])

# Part Two
max = 1000000000000
over = int
for f in range(1000, 1000000000000, 1000):
    resource_totals.clear()
    resource_totals["FUEL"] = f
    get_child_resources("FUEL")
    if resource_totals["ORE"] > max:
        over = f
        break

for f in range(int(over) - 100, 0, int(-100)):
    resource_totals.clear()
    resource_totals["FUEL"] = f
    get_child_resources("FUEL")
    if resource_totals["ORE"] < max:
        over = f
        break

for f in range(over + 10, 1000000000000, 10):
    resource_totals.clear()
    resource_totals["FUEL"] = f
    get_child_resources("FUEL")
    if resource_totals["ORE"] > max:
        over = f
        break

for f in range(int(over) - 1, 0, int(-1)):
    resource_totals.clear()
    resource_totals["FUEL"] = f
    get_child_resources("FUEL")
    if resource_totals["ORE"] < max:
        print(f)
        break



