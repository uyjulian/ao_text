from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0100", "c0100_1", "c1000_1", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x06',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100",                  # 0
        "Gina",                 # 1
        "Conte old man",             # 2
        "Abel",                 # 3
        "Mimi",                   # 4
        "Pruna",               # 5
        "Linally",               # 6
        "Haas",                 # 7
        "Sally",                 # 8
        "Coppe",                 # 9
        "Zeit",               # 10
        "Keya",                 # 11
        "Kate policing",             # 12
        "Police investigation",           # 13
        "A security guard",               # 14
        "Policeman",                   # 15
        "Defense Forces soldier",             # 16
        "Citizen",                   # 17
        "Citizen",                   # 18
        "car",                     # 19
        "Ryu",                 # 20
        "Henry",                 # 21
        "Keya",                 # 22
        "White falcon",             # 23
        "Sergey Manager",           # 24
        "Defense Forces soldier",             # 25
        "Citizen 1",                 # 26
        "Citizen 2",                 # 27
        "Citizen 3",                 # 28
        "Citizen 4",                 # 29
        "Citizen 5",                 # 30
        "Citizen 6",                 # 31
        "Citizen 7",                 # 32
        "Event monster",   # 33
        "Event monster",   # 34
        "Event monster",   # 35
        "Event monster",   # 36
        "Event monster",   # 37
        "car",                     # 38
        "Runaway vehicle",                 # 39
        "Police car 1",              # 40
        "Police car 2",              # 41
        "Police car 3",              # 42
        "car",                     # 43
        "car",                     # 44
        "car",                     # 45
        "Randy",               # 46
        "Noel",                 # 47
        "Waji",                   # 48
        "SE control",                 # 49
        "Policeman",                   # 50
        "Policeman",                   # 51
        "Policeman",                   # 52
        "Policeman",                   # 53
        "Policeman",                   # 54
        "Balloon store",                 # 55
        "Muller",               # 56
        "Olivier",               # 57
        "bc0100",                 # 58
        "bc0100",                 # 59
        "Central square",               # 60
        "Nishi dori",                 # 61
        "Administrative district",                 # 62
        "Residential area",                 # 63
        "Entertainment district",                 # 64
        "East Street",                 # 65
        "old Town",                 # 66
        "Harbor district",                 # 67
        "IBC",                 # 68
        "Beside the station",               # 69
        "Back street",                 # 70
        "Ursula interchange",           # 71
        "East Crossbell Highway",       # 72
        "West Crossbell Highway",       # 73
        "Mainz Mountain Road",           # 74
        "Orchis Tower",         # 75
    ))

    ATBonus("ATBonus_B6C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_B7C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_10368", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_BBC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BCC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BD8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C1C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C20", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_C24", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_C28", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_C2C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_C30", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_C34", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C38", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_B9C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BA8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_BAC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BB8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C3C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C40", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C44", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C48", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C50", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C54", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C58", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_C5C", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0100", "Sepith_10368", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_BBC", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B9C", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_BBC", "MonsterBattlePostion_C1C", "ed7450", "ed7453", "ATBonus_B6C"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_CF8", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bc0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C3C", "MonsterBattlePostion_C1C", "ed7544", "ed7453", "ATBonus_B7C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch48500.itc",                   # 08
        "chr/ch48600.itc",                   # 09
        "chr/ch02702.itc",                   # 0A
        "chr/ch30600.itc",                   # 0B
        "chr/ch30000.itc",                   # 0C
        "chr/ch39200.itc",                   # 0D
        "chr/ch08200.itc",                   # 0E
        "chr/ch48700.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch02707.itc",                   # 12
        "chr/ch41800.itc",                   # 13
        "chr/ch31200.itc",                   # 14
        "chr/ch22000.itc",                   # 15
        "chr/ch32300.itc",                   # 16
    ))

    DeclNpc(30000,   0,       4294965497, 270,  261,  0x0, 0,   0,   0,   0,   2,   1,   0,   255,  0)
    DeclNpc(4294961206, 150,     4449,    270,  325,  0x0, 0,   1,   0,   255, 255, 1,   1,   255,  0)
    DeclNpc(4294961197, 0,       4294957887, 90,   389,  0x0, 0,   2,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(4294967007, 0,       4294956977, 225,  261,  0x0, 0,   3,   0,   0,   3,   1,   4,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   6,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   1,   9,   255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   7,   0,   0,   0,   1,   10,  255,  0)
    DeclNpc(4294961197, 0,       4294957887, 90,   389,  0x0, 0,   4,   0,   0,   0,   1,   3,   255,  0)
    DeclNpc(4294944487, 1299,    4294948467, 180,  261,  0x0, 0,   13,  0,   0,   4,   1,   20,  255,  0)
    DeclNpc(4294941856, 1299,    4294950256, 180,  405,  0x0, 0,   10,  0,   255, 255, 1,   11,  255,  0)
    DeclNpc(4294941856, 1299,    4294949126, 0,    389,  0x0, 0,   14,  0,   0,   0,   1,   19,  255,  0)
    DeclNpc(4294966086, 0,       4294964906, 180,  389,  0x0, 0,   11,  0,   0,   0,   1,   12,  255,  0)
    DeclNpc(4294966086, 0,       4294964906, 180,  389,  0x0, 0,   12,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(1750,    0,       4294965737, 180,  389,  0x0, 0,   20,  0,   0,   0,   1,   14,  255,  0)
    DeclNpc(4294948577, 0,       3960,    180,  385,  0x0, 0,   12,  0,   0,   1,   1,   15,  255,  0)
    DeclNpc(4294966086, 0,       4294964906, 180,  385,  0x0, 0,   19,  0,   0,   0,   1,   16,  255,  0)
    DeclNpc(4294958767, 0,       2119,    90,   389,  0x0, 0,   21,  0,   0,   0,   1,   17,  255,  0)
    DeclNpc(4294959276, 0,       910,     90,   389,  0x0, 0,   22,  0,   0,   0,   1,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294958226, 13520,   0,       0x10100E1,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294962406, 4294963226, 0,       0x10100B4,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6530,    4294967186, 0,       0x10100B4,    "BattleInfo_C5C", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 11,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 105, -20.649999618530273,   -24.65999984741211,    -8.199999809265137,    625.0,                 [0.07071065157651901,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.28355100750923157,  6.407801151275635,     4.099999904632568,     1.0])
    DeclEvent(0x0000, 0, 107, 0.12999999523162842,   18.799999237060547,    0.0,                   100.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -0.012999999336898327, -9.399999618530273,    -0.0,                  1.0])

    DeclActor(0,       0,       4294965696, 1000,    0,       2500,    0,       0x007C, 1,  24, 0x0000)
    DeclActor(4294961166, 4294963096, 4294946286, 1000,    4294961166, 4294964096, 4294946286, 0x007C, 1,  25, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "Central square")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "Nishi dori")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "Administrative district")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "Residential area")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "Entertainment district")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "East Street")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "old Town")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "Harbor district")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "IBC")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "Beside the station")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "Back street")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_F1C",          # 00, 0
        "Function_1_FCC",          # 01, 1
        "Function_2_10A5",         # 02, 2
        "Function_3_10F2",         # 03, 3
        "Function_4_111D",         # 04, 4
        "Function_5_1148",         # 05, 5
        "Function_6_1173",         # 06, 6
        "Function_7_12BD",         # 07, 7
        "Function_8_2196",         # 08, 8
        "Function_9_2976",         # 09, 9
        "Function_10_2BD0",        # 0A, 10
        "Function_11_2BE0",        # 0B, 11
        "Function_12_3CCF",        # 0C, 12
        "Function_13_3D0C",        # 0D, 13
        "Function_14_3D53",        # 0E, 14
        "Function_15_3D9D",        # 0F, 15
        "Function_16_44F4",        # 10, 16
        "Function_17_466B",        # 11, 17
        "Function_18_46D0",        # 12, 18
        "Function_19_46EC",        # 13, 19
        "Function_20_484A",        # 14, 20
        "Function_21_4893",        # 15, 21
        "Function_22_48A6",        # 16, 22
        "Function_23_4AD6",        # 17, 23
        "Function_24_523A",        # 18, 24
        "Function_25_52DE",        # 19, 25
        "Function_26_59B9",        # 1A, 26
        "Function_27_5A06",        # 1B, 27
        "Function_28_5A6F",        # 1C, 28
        "Function_29_5C55",        # 1D, 29
        "Function_30_5C68",        # 1E, 30
        "Function_31_7758",        # 1F, 31
        "Function_32_7788",        # 20, 32
        "Function_33_77C7",        # 21, 33
        "Function_34_79F2",        # 22, 34
        "Function_35_7B42",        # 23, 35
        "Function_36_818F",        # 24, 36
        "Function_37_81E3",        # 25, 37
        "Function_38_81FC",        # 26, 38
        "Function_39_84EE",        # 27, 39
        "Function_40_8535",        # 28, 40
        "Function_41_8548",        # 29, 41
        "Function_42_8A19",        # 2A, 42
        "Function_43_8A6E",        # 2B, 43
        "Function_44_8AC3",        # 2C, 44
        "Function_45_8B18",        # 2D, 45
        "Function_46_8B6D",        # 2E, 46
        "Function_47_8B9D",        # 2F, 47
        "Function_48_8D75",        # 30, 48
        "Function_49_9147",        # 31, 49
        "Function_50_9A2C",        # 32, 50
        "Function_51_9AA6",        # 33, 51
        "Function_52_9F67",        # 34, 52
        "Function_53_9F9E",        # 35, 53
        "Function_54_9FCF",        # 36, 54
        "Function_55_A000",        # 37, 55
        "Function_56_A031",        # 38, 56
        "Function_57_A062",        # 39, 57
        "Function_58_A093",        # 3A, 58
        "Function_59_A0C4",        # 3B, 59
        "Function_60_A2AB",        # 3C, 60
        "Function_61_A2F3",        # 3D, 61
        "Function_62_A312",        # 3E, 62
        "Function_63_A331",        # 3F, 63
        "Function_64_A365",        # 40, 64
        "Function_65_A3A6",        # 41, 65
        "Function_66_A3E7",        # 42, 66
        "Function_67_A430",        # 43, 67
        "Function_68_AD47",        # 44, 68
        "Function_69_AD84",        # 45, 69
        "Function_70_ADC1",        # 46, 70
        "Function_71_ADFE",        # 47, 71
        "Function_72_AE3B",        # 48, 72
        "Function_73_AE78",        # 49, 73
        "Function_74_AEB5",        # 4A, 74
        "Function_75_AEF2",        # 4B, 75
        "Function_76_AF11",        # 4C, 76
        "Function_77_AF2E",        # 4D, 77
        "Function_78_AFA8",        # 4E, 78
        "Function_79_AFFB",        # 4F, 79
        "Function_80_B04E",        # 50, 80
        "Function_81_B0A1",        # 51, 81
        "Function_82_B0F4",        # 52, 82
        "Function_83_B147",        # 53, 83
        "Function_84_B161",        # 54, 84
        "Function_85_C598",        # 55, 85
        "Function_86_C5D5",        # 56, 86
        "Function_87_C6C5",        # 57, 87
        "Function_88_C70E",        # 58, 88
        "Function_89_C7DE",        # 59, 89
        "Function_90_C8E5",        # 5A, 90
        "Function_91_C8FF",        # 5B, 91
        "Function_92_C931",        # 5C, 92
        "Function_93_C978",        # 5D, 93
        "Function_94_C9BF",        # 5E, 94
        "Function_95_CA14",        # 5F, 95
        "Function_96_CA69",        # 60, 96
        "Function_97_CABE",        # 61, 97
        "Function_98_CCE9",        # 62, 98
        "Function_99_CDE5",        # 63, 99
        "Function_100_CE69",       # 64, 100
        "Function_101_CF5B",       # 65, 101
        "Function_102_D424",       # 66, 102
        "Function_103_D8C4",       # 67, 103
        "Function_104_DF69",       # 68, 104
        "Function_105_E4A5",       # 69, 105
        "Function_106_EBD0",       # 6A, 106
        "Function_107_EC01",       # 6B, 107
        "Function_108_F316",       # 6C, 108
        "Function_109_F473",       # 6D, 109
        "Function_110_FF6C",       # 6E, 110
        "Function_111_10093",      # 6F, 111
        "Function_112_10190",      # 70, 112
        "Function_113_102C6",      # 71, 113
    ))


    def Function_0_F1C(): pass

    label("Function_0_F1C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_F54"),
        (1, "loc_F60"),
        (2, "loc_F6C"),
        (3, "loc_F78"),
        (4, "loc_F84"),
        (5, "loc_F90"),
        (6, "loc_F9C"),
        (SWITCH_DEFAULT, "loc_FA8"),
    )


    label("loc_F54")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F60")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F6C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F78")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F84")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F90")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_F9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FA8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FCB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FB4")

    label("loc_FCB")

    Return()

    # Function_0_F1C end

    def Function_1_FCC(): pass

    label("Function_1_FCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -300, 800, 24250, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xD7, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -18720, 0, 3960, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_1_FCC")

    label("loc_10A4")

    Return()

    # Function_1_FCC end

    def Function_2_10A5(): pass

    label("Function_2_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10F1")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_2_10A5")

    label("loc_10F1")

    Return()

    # Function_2_10A5 end

    def Function_3_10F2(): pass

    label("Function_3_10F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_111C")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_3_10F2")

    label("loc_111C")

    Return()

    # Function_3_10F2 end

    def Function_4_111D(): pass

    label("Function_4_111D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1147")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_4_111D")

    label("loc_1147")

    Return()

    # Function_4_111D end

    def Function_5_1148(): pass

    label("Function_5_1148")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1172")
    OP_94(0xFE, 0xFFFFBE2E, 0x2184, 0xFFFFB38E, 0x1054, 0x3E8)
    Sleep(300)
    Jump("Function_5_1148")

    label("loc_1172")

    Return()

    # Function_5_1148 end

    def Function_6_1173(): pass

    label("Function_6_1173")

    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    SetMapObjFlags(0x1E, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11BD")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11D1")
    ClearMapObjFlags(0x15, 0x2000000)
    Jump("loc_12BC")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_11E5")
    ClearMapObjFlags(0xC, 0x2000000)
    Jump("loc_12BC")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1211")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)
    Jump("loc_12BC")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1285")
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)
    Jump("loc_12BC")

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1299")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_12AD")
    ClearMapObjFlags(0x13, 0x2000000)
    Jump("loc_12BC")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_12BC")
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_12BC")

    Return()

    # Function_6_1173 end

    def Function_7_12BD(): pass

    label("Function_7_12BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137F")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1352")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_1371")

    label("loc_1352")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1371")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_1371")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_137F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1433")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1406")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1425")

    label("loc_1406")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1425")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1425")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_1433")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E7")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BA")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_14D9")

    label("loc_14BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D9")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_14D9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_14E7")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159B")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156E")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_158D")

    label("loc_156E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158D")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_158D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_159B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164F")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1622")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1641")

    label("loc_1622")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1641")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1641")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_164F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1703")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_16F5")

    label("loc_16D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F5")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_16F5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_1703")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B7")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178A")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_17A9")

    label("loc_178A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A9")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_17A9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_17B7")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186B")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183E")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_185D")

    label("loc_183E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185D")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_185D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_186B")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_191F")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F2")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1911")

    label("loc_18F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1911")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1911")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_191F")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D3")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A6")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_19C5")

    label("loc_19A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C5")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_19C5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A82")

    label("loc_19D3")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A82")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5A")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_1A79")

    label("loc_1A5A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A79")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_1A79")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A82")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AEF")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    OP_93(0xC, 0x87, 0x0)
    OP_93(0xD, 0x87, 0x0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1B20")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1F16")

    label("loc_1B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B66")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -4450, 0, -9880, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1F16")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9A")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1BA4")

    label("loc_1B9A")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_1BA4")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 180)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1F16")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C02")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C71")
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -6100, 0, -9410, 225)
    SetChrPos(0xB, -6780, 0, -8620, 225)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CA0")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, -5000, 0, -9410, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CB8")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CE7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE2")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)

    label("loc_1CE2")

    Jump("loc_1F16")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D3C")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1D8B")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_1F16")

    label("loc_1D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E12")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E03")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -24750, 1300, -16680, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E03")
    SetChrFlags(0x12, 0x10)

    label("loc_1E03")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E91")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4E")
    SetChrChipByIndex(0x11, 0x12)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -26150, -8200, -23200, 180)
    BeginChrThread(0x11, 0, 0, 0)

    label("loc_1E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E82")
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E82")
    SetChrFlags(0xE, 0x10)

    label("loc_1E82")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1ECE")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1F16")

    label("loc_1ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEF")
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_1EEF")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -22230, 1300, -20180, 315)
    BeginChrThread(0x11, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)

    label("loc_1F16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F30")
    Event(0, 30)

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F46")
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_1F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F73")
    SetMapFlags(0x10000000)
    Event(0, 103)

    label("loc_1F73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB6")
    SetChrPos(0xC, 4760, 0, 17660, 90)
    SetChrPos(0xD, 6740, 0, 17590, 270)
    SetChrFlags(0x16, 0x80)

    label("loc_1FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD1")
    Event(0, 15)

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FFC")
    SetMapFlags(0x10000000)
    Event(2, 0)

    label("loc_1FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2013")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 9)
    Jump("loc_2195")

    label("loc_2013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_2027")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)
    Jump("loc_2195")

    label("loc_2027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_203B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 19)
    Jump("loc_2195")

    label("loc_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_204F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 22)
    Jump("loc_2195")

    label("loc_204F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_2066")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x1, 4)
    Event(0, 23)
    Jump("loc_2195")

    label("loc_2066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_207A")
    ClearScenarioFlags(0x22, 5)
    Event(0, 25)
    Jump("loc_2195")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_208E")
    ClearScenarioFlags(0x22, 6)
    Event(0, 28)
    Jump("loc_2195")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_20A5")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x1, 4)
    Event(0, 33)
    Jump("loc_2195")

    label("loc_20A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_20B9")
    ClearScenarioFlags(0x23, 0)
    Event(0, 34)
    Jump("loc_2195")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_20CD")
    ClearScenarioFlags(0x23, 1)
    Event(0, 38)
    Jump("loc_2195")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_20E1")
    ClearScenarioFlags(0x23, 2)
    Event(0, 41)
    Jump("loc_2195")

    label("loc_20E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_20F5")
    ClearScenarioFlags(0x23, 3)
    Event(0, 47)
    Jump("loc_2195")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2109")
    ClearScenarioFlags(0x23, 4)
    Event(0, 48)
    Jump("loc_2195")

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_211D")
    ClearScenarioFlags(0x23, 5)
    Event(0, 49)
    Jump("loc_2195")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2131")
    ClearScenarioFlags(0x23, 6)
    Event(0, 51)
    Jump("loc_2195")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_2145")
    ClearScenarioFlags(0x23, 7)
    Event(0, 59)
    Jump("loc_2195")

    label("loc_2145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_2159")
    ClearScenarioFlags(0x24, 0)
    Event(0, 67)
    Jump("loc_2195")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_216D")
    ClearScenarioFlags(0x24, 1)
    Event(0, 97)
    Jump("loc_2195")

    label("loc_216D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_2186")
    ClearScenarioFlags(0x24, 2)
    SetMapFlags(0x10000000)
    Event(0, 102)
    Jump("loc_2195")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_2195")
    ClearScenarioFlags(0x24, 3)
    Event(0, 101)

    label("loc_2195")

    Return()

    # Function_7_12BD end

    def Function_8_2196(): pass

    label("Function_8_2196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_21AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)

    label("loc_21AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_226F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5A, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_231E")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5A, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2380")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x26, 0x82, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_2380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2398")
    ClearMapFlags(0x2000)
    Jump("loc_239F")

    label("loc_2398")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23F3")
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x1A)
    SetMapObjFlags(0xF, 0x1000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -7790, 0, 16480, 90)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0xF, 0x1E)
    OP_70(0xF, 0x0)
    Jump("loc_2458")

    label("loc_23F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240B")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_2458")

    label("loc_240B")

    ClearMapObjFlags(0x13, 0x4)
    OP_78(0x13, 0x1A)
    SetMapObjFlags(0x13, 0x1000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -8010, 0, 16230, 225)
    OP_D5(0x1A, 0x0, 0x36EE8, 0x0, 0x0)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x0)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFlags(0x13, 0x400)

    label("loc_2458")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2472")
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)

    label("loc_2472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251E")
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    LoadEffect(0xA, "map/mpbell02.eff")
    PlayEffect(0xA, 0x6, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x0, 0x1D, 0x0, 0x20)
    SetMapObjFrame(0x14, "bell_add", 0x1, 0x1)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x258, 0x0, 0x20)

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_254D")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    Jump("loc_256E")

    label("loc_254D")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)

    label("loc_256E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_257C")
    Jump("loc_25DD")

    label("loc_257C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2590")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_2590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_259E")
    Jump("loc_25DD")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25B2")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25C0")
    Jump("loc_25DD")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25D4")
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_25DD")

    label("loc_25D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25DD")

    label("loc_25DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F6")
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_25FC")

    label("loc_25F6")

    SetMapObjFlags(0xA, 0x4)

    label("loc_25FC")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2614")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2614")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263E")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_263E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2668")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_2668")

    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2915")
    OP_10(0x2, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_291B")

    label("loc_2915")

    OP_10(0x2, 0x1)
    OP_10(0xD, 0x0)

    label("loc_291B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2961")
    OP_1B(0x0, 0x0, 0x6E)
    OP_1B(0x2, 0x0, 0x6F)
    OP_1B(0x3, 0x0, 0x70)
    OP_1B(0x4, 0x0, 0x71)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)

    label("loc_2961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2975")
    Sound(828, 1, 60, 0)

    label("loc_2975")

    Return()

    # Function_8_2196 end

    def Function_9_2976(): pass

    label("Function_9_2976")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "At Altair Lodge\x01",
            "Two days after the arrest play ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0xB, -4900, 0, -9350, 270)
    SetChrPos(0x2D, 20000, 0, -5000, 270)
    OP_D5(0x2D, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x11, -22250, 1300, -20200, 315)
    BeginChrThread(0x11, 0, 0, 0)
    OP_68(0, 1900, 3650, 0)
    MoveCamera(55, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    MoveCamera(15, 25, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(35000, 8000)
    PlayBGM("ed7150", 0)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(958, 0, 100, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(4450, 1000, -6100, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_68(-23000, 2200, -19700, 10000)
    MoveCamera(55, 15, 0, 10000)
    SetCameraDistance(15000, 10000)
    BeginChrThread(0x38, 1, 0, 10)

    def lambda_2B9F():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2B9F)
    OP_0D()
    OP_6F(0x79)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2976 end

    def Function_10_2BD0(): pass

    label("Function_10_2BD0")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 50, 0)
    Return()

    # Function_10_2BD0 end

    def Function_11_2BE0(): pass

    label("Function_11_2BE0")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis402.itp")
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    SoundLoad(835)
    SetChrPos(0x101, -600, 0, -12000, 0)
    SetChrPos(0x102, -400, 0, -13400, 0)
    SetChrPos(0x109, 600, 0, -12000, 0)
    SetChrPos(0x105, 800, 0, -13400, 0)
    SetChrPos(0x1A5, -1700, 0, -12700, 0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -12400, 0, -3300, 90)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -13500, 0, -3300, 90)
    SetChrPos(0xB, -5300, 0, -10200, 320)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -6100, 0, -9410, 140)
    OP_68(0, 1100, -11700, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_2D31():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D31)
    Sleep(100)

    def lambda_2D4E():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D4E)
    Sleep(100)

    def lambda_2D6B():
        OP_97(0x1A5, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_2D6B)
    Sleep(100)

    def lambda_2D88():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D88)
    Sleep(100)

    def lambda_2DA5():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DA5)
    Sound(835, 2, 60, 0)
    OP_68(0, 1100, -7700, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    NpcTalk(
        0x1B,
        "Boys' Voices",
        "Hey, Kea!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_63(0x1A5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-10700, 1100, -4300, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-2200, 1100, -6700, 3000)
    MoveCamera(357, 19, 0, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0x1B, 3, 0, 12)
    BeginChrThread(0x1C, 3, 0, 13)

    def lambda_2ED6():

        label("loc_2ED6")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2ED6")

    QueueWorkItem2(0x101, 2, lambda_2ED6)

    def lambda_2EE8():

        label("loc_2EE8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EE8")

    QueueWorkItem2(0x102, 2, lambda_2EE8)

    def lambda_2EFA():

        label("loc_2EFA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EFA")

    QueueWorkItem2(0x1A5, 2, lambda_2EFA)

    def lambda_2F0C():

        label("loc_2F0C")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F0C")

    QueueWorkItem2(0x109, 2, lambda_2F0C)

    def lambda_2F1E():

        label("loc_2F1E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F1E")

    QueueWorkItem2(0x105, 2, lambda_2F1E)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x1A5, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    ChrTalk(
        0x1A5,
        "#12P#01110FOh, Henry to Ryu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5POh oh, in front of a bakery\x01",
            "It was a meeting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PLesson will start soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#12P#01109FWell, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHey, Henry to Ryu.\x01",
            "You are fine as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHehu, always with Kea\x01",
            "Thank you for making friends.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#5POh, it is a long time no see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PTo, it is long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PI heard it from Keao\x01",
            "The support department, I have to start again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, thanks for your help.\x02\x03",
            "#00000FI am doing various power-ups\x01",
            "Please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PWell, to say it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWell, if it was my older brothers\x01",
            "About the same as a hypocrite\x01",
            "May I admit it? ~.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PTherefore, Ryu, he said he was great ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FCouscous……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAs expected.\x01",
            "It seems very popular among children.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3291():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3291)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#5POh my gosh sister ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PIt is a face you do not see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PBy the way, to Mr. Tio\x01",
            "Randy is not even there ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FTwo people have errands\x01",
            "I have not come back yet.\x02\x03",
            "#00100FThis is Mr. Noel to Wazy.\x01",
            "They are newcomers from the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FHuh, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5POh, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5P…… That, that.\x01",
            "Are you a guy like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PSomething like Onna\x01",
            "I'm kao … ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PWait a minute, Ryu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHow about you, huh?\x02\x03",
            "#10302FIf you think you are a woman\x01",
            "You may be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F…… That's why Wadi.\x01",
            "Do not distract your children.\x02\x03",
            "#00000FThan three of them\x01",
            "Do not you have to hurry?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3585():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_3585)
    Sleep(50)

    def lambda_3595():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3595)
    Sleep(150)

    ChrTalk(
        0x1A5,
        (
            "#6P#01105FOh, that was it.\x02\x03",
            "#01109FWell then everyone!\x01",
            "Do your best at work!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A5, 500)

    def lambda_35FE():

        label("loc_35FE")

        TurnDirection(0xFE, 0x1A5, 500)
        Yield()
        Jump("loc_35FE")

    QueueWorkItem2(0x101, 2, lambda_35FE)

    ChrTalk(
        0x101,
        "#00009FOh, Kaaaa go for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FWatch out for cars, are not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#6P#01110FWow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5POkay, so\x01",
            "Would you like to drop in at our house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PYes, let's hurry!\x02",
    )

    CloseMessageWindow()
    OP_68(-5200, 1100, -6700, 4000)
    BeginChrThread(0x1B, 3, 0, 14)
    Sleep(400)
    BeginChrThread(0x1C, 3, 0, 14)
    Sleep(50)
    SetChrFlags(0x1A5, 0x1000)
    BeginChrThread(0x1A5, 3, 0, 14)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1A5, 3)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, -8000, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#11P#10109FHehu ……\x01",
            "You are energetic children.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        "#11P#10300FA girl living in Nishi-dori?\x02",
    )

    CloseMessageWindow()

    def lambda_3797():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3797)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00002FOh, another one\x01",
            "I live in a residential area, though.\x02\x03",
            "#00004F── Well then.\x01",
            "Let us also begin work.\x02\x03",
            "#00000FTentatively, there is an oval store there\x01",
            "As I came to the police headquarters … …\x02\x03",
            "If possible, the city also has a common road.\x01",
            "You may as well try turning around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10100FI see.\x01",
            "Is that a patrol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FHuhu, that far\x01",
            "It's not exaggeration … ….\x02\x03",
            "#00100FBecause unexpected information comes in\x01",
            "Traveling is also important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAfter a while from the section manager\x01",
            "A call will be made to Enigma.\x02\x03",
            "By that time in the city\x01",
            "Let's go to the place you care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10102FOK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10304FHuh, let's go then.\x02",
    )

    CloseMessageWindow()
    StopSound(835, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis302.itp")
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell city map is now available.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you press the START button on the field in the city\x01",
            "You can open the whole map of the city.\x01",
            "(Press the START button again\x01",
            "We display a map of autonomous state. )\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, in the city using a map\x01",
            "Move the shortcut by area\x01",
            "It is possible to.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the list of blocks on the left\x01",
            "Please select the area you want to go to.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, depending on the situation\x01",
            "There are times when the city map can not be used.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0xA, -6100, 0, -9410, 90)
    SetChrPos(0xB, -290, 0, -10320, 225)
    BeginChrThread(0xB, 0, 0, 3)
    OP_D7(0x1E)
    OP_D7(0x1F)
    RemoveParty(0xA4, 0xFF)
    SetChrPos(0x0, -1500, 0, -16820, 90)
    OP_C9(0x1, 0x1000)
    SetScenarioFlags(0x126, 4)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_11_2BE0 end

    def Function_12_3CCF(): pass

    label("Function_12_3CCF")


    def lambda_3CD4():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CD4)
    WaitChrThread(0xFE, 1)

    def lambda_3CF2():
        OP_95(0xFE, -3400, 0, -5700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CF2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3CCF end

    def Function_13_3D0C(): pass

    label("Function_13_3D0C")

    Sleep(50)

    def lambda_3D14():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D14)
    WaitChrThread(0xFE, 1)

    def lambda_3D32():
        OP_95(0xFE, -2800, 0, -4800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D32)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_13_3D0C end

    def Function_14_3D53(): pass

    label("Function_14_3D53")

    OP_92(0xFE, 0xFFFFE318, 0xFFFFF31C, 0x1F4)

    def lambda_3D65():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D65)
    WaitChrThread(0xFE, 1)

    def lambda_3D83():
        OP_95(0xFE, -17400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D83)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3D53 end

    def Function_15_3D9D(): pass

    label("Function_15_3D9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(803)
    OP_68(14000, 1200, 6000, 0)
    MoveCamera(57, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 15000, 0, 6000, 270)
    SetChrPos(0x102, 12800, 0, 6000, 90)
    SetChrPos(0x109, 13700, 0, 4700, 0)
    SetChrPos(0x105, 13700, 0, 7300, 180)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetCameraDistance(18500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3ED0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3ED0)
    Sleep(50)

    def lambda_3EE0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EE0)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#11P#00005FOh, is the section chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FEven if it hangs around\x01",
            "It's strange time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00000FYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ou, thanks.\x02\x03",
            "As I said in the morning, it will not be long\x01",
            "I will have you come to the police school.\x02\x03",
            "Do you know the place?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FYes, of course.\x02\x03",
            "#00000FFrom the middle of the West Crossbell Highway\x01",
            "I'm in the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, keep the gate open.\x02\x03",
            "by the way……\x01",
            "You should have walked around the street all the way.\x02\x03",
            "How frankly did you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FAh……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F……I agree.\x02\x03",
            "#00001FTo various queen smell situation\x01",
            "I feel like I'm getting started.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That olfaction, more than ever\x01",
            "Sharpen it.\x02\x03",
            "Well then it will be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FOK.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00100FAfter all I seem to have been the section chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSomething to worry about\x01",
            "I guess they were saying … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00006FOh, the section chief is also various\x01",
            "It seems that I feel a change in the situation.\x02\x03",
            "#00001FBlack Month and Captain Rector\x01",
            "It seems better to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FSo, it is about time.\x01",
            "You go to the police school?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FOh, let's get out on the highway from the West Exit.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the city map of Crossbell\x01",
            "\"West Crossbell Highway\"\x01",
            "You can now select.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 15000, 0, 6000, 270)
    OP_69(0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 30000, 0, -1800, 270)
    BeginChrThread(0x8, 0, 0, 2)
    SetScenarioFlags(0x126, 5)
    OP_29(0xA1, 0x1, 0x4)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_15_3D9D end

    def Function_16_44F4(): pass

    label("Function_16_44F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x8, 0x2D)
    OP_49()
    SetChrPos(0x2D, -35510, -2590, -4520, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F9")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xA, 0xFF)
    SetChrPos(0xA, -6880, 0, 810, 0)

    def lambda_45C5():

        label("loc_45C5")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_45C5")

    QueueWorkItem2(0xA, 2, lambda_45C5)
    SetChrPos(0xB, -6300, 0, -170, 0)
    EndChrThread(0xB, 0xFF)

    def lambda_45EC():

        label("loc_45EC")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_45EC")

    QueueWorkItem2(0xB, 2, lambda_45EC)

    label("loc_45F9")

    FadeToBright(1000, 0)
    BeginChrThread(0x2D, 3, 0, 17)
    BeginChrThread(0x38, 1, 0, 18)
    OP_68(-17900, 2700, -500, 0)
    MoveCamera(355, 30, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(28000, 0)
    OP_68(-15700, 3700, -300, 7500)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_44F4 end

    def Function_17_466B(): pass

    label("Function_17_466B")

    SetChrPos(0xFE, -35510, -2590, -4520, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23860, -640, -4420)
    OP_9F(0x1, -14350, 750, -1880)
    OP_9F(0x1, -11380, 0, 7200)
    OP_9F(0x1, -14250, 0, 13970)
    OP_9F(0x1, -28100, 0, 29400)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_17_466B end

    def Function_18_46D0(): pass

    label("Function_18_46D0")

    Sound(458, 0, 100, 0)
    Sound(468, 2, 100, 0)
    Sleep(5000)
    Sound(494, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_46D0 end

    def Function_19_46EC(): pass

    label("Function_19_46EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0xA, 0x8)
    SetChrChipByIndex(0xB, 0x9)
    SetChrChipByIndex(0x8, 0xF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x15, 0x2D)
    OP_49()
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_71(0x15, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xC8, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x2D, 11000, 0, 30000, 180)
    OP_D5(0x2D, 0x0, 0x2BF20, 0x0, 0x0)
    BeginChrThread(0x2D, 1, 0, 20)
    BeginChrThread(0x38, 1, 0, 21)
    OP_68(-3500, 4300, -8650, 0)
    MoveCamera(55, -5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(-3500, 2500, -8650, 10000)
    MoveCamera(40, 5, 0, 10000)
    SetCameraDistance(18000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_46EC end

    def Function_20_484A(): pass

    label("Function_20_484A")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_20_484A end

    def Function_21_4893(): pass

    label("Function_21_4893")

    Sleep(2300)
    Sound(458, 0, 70, 0)
    Sleep(4300)
    Sound(494, 0, 70, 0)
    Return()

    # Function_21_4893 end

    def Function_22_48A6(): pass

    label("Function_22_48A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrChipByIndex(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x3)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrChipByIndex(0x39, 0xC)
    BeginChrThread(0x39, 0, 0, 0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3A, 0xC)
    BeginChrThread(0x3A, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0xF, 0x1A)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrPos(0x1A, -7800, 0, 16500, 90)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x39, 7000, 0, -7700, 270)
    SetChrPos(0x3A, 5750, 0, -7700, 90)
    SetChrPos(0x2D, 8850, 0, -8650, 225)
    OP_D5(0x2D, 0x0, 0x36EE8, 0x0, 0x0)
    OP_68(-15350, 1900, -2500, 0)
    MoveCamera(345, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(3000, 1400, -6000, 10000)
    MoveCamera(40, 15, 0, 10000)
    SetCameraDistance(22000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_48A6 end

    def Function_23_4AD6(): pass

    label("Function_23_4AD6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadChrToIndex("chr/ch24000.itc", 0x1F)
    LoadChrToIndex("chr/ch22300.itc", 0x20)
    LoadChrToIndex("chr/ch21000.itc", 0x21)
    LoadChrToIndex("chr/ch27900.itc", 0x22)
    LoadChrToIndex("chr/ch22800.itc", 0x23)
    LoadChrToIndex("chr/ch20500.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x20)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x21)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrChipByIndex(0x24, 0x22)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 0)
    SetChrChipByIndex(0x25, 0x23)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    BeginChrThread(0x25, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x24)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x39, 0xC)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    BeginChrThread(0x39, 0, 0, 0)
    SetChrChipByIndex(0x3A, 0xC)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    BeginChrThread(0x3A, 0, 0, 0)
    SetChrChipByIndex(0x3B, 0xC)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    BeginChrThread(0x3B, 0, 0, 0)
    SetChrChipByIndex(0x3C, 0xC)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    BeginChrThread(0x3C, 0, 0, 0)
    SetChrChipByIndex(0x3D, 0xC)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    BeginChrThread(0x3D, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0xD, 0x2E)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x7, 0x3E)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W\x01",
            "Seiya calendar 1204 __ - early autumn.\x02\x03",
            "As the new Crosbel Mayor, IBC President,\x01",
            "Dieter Crois advocated\x01",
            "The \"West Zemria Trade Council\" began.\x02\x03",
            "From the western great country, Eleven Empire\x01",
            "\"Chief Iron Blood\" In addition to Gillius Osborne,\x01",
            "man of the world#4RSquat#Olivaruto known as ──\x02\x03",
            "From the east major country, Calvado\x01",
            "I am attracting support as an ordinary people\x01",
            "President Samuel Rock Smith ──\x02\x03",
            "From the Republic of the Republic in the northeast\x01",
            "Albert Daimyo, governor of the country at young age\x02\x03",
            "From the Liber Kingdom in the southwest\x01",
            "As Queen's representative, King Claudia ----\x02\x03",
            "Both of the VIP guests in the national guest class\x01",
            "It was just gathering at the crossbell now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0x9, 1050, 0, -3100, 90)
    SetChrPos(0x8, 500, 0, -7750, 135)
    SetChrPos(0xA, -1900, 0, -5000, 315)
    SetChrPos(0xF, -3700, 0, -5100, 45)
    SetChrPos(0xB, -2700, 0, -4550, 0)
    SetChrPos(0xE, -2950, 0, -3350, 180)
    SetChrPos(0xC, -1900, 0, -10200, 180)
    SetChrPos(0xD, -1900, 0, -11500, 0)
    SetChrPos(0x39, 15900, 0, 6000, 270)
    SetChrPos(0x3A, 2450, 0, -5250, 90)
    SetChrPos(0x3B, 1150, 0, -9850, 90)
    SetChrPos(0x3C, -5750, 0, -4450, 270)
    SetChrPos(0x3D, 9500, 0, -9350, 315)
    SetChrPos(0x21, -3850, 0, -11600, 135)
    SetChrPos(0x22, 400, 0, -5900, 135)
    SetChrPos(0x23, 0, 0, -5100, 135)
    SetChrPos(0x24, -1650, 0, -7950, 90)
    SetChrPos(0x25, -2050, 0, -13250, 90)
    SetChrPos(0x26, -2700, 0, -7000, 180)
    SetChrPos(0x2D, -6000, 0, -9150, 135)
    OP_D5(0x2D, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x2E, -7800, 0, 16500, 90)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x3E, -1700, 0, -2050, 200)
    OP_D5(0x3E, 0x0, 0x1ADB0, 0x0, 0x0)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0xA, 1, 0, 24)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0xC, 1, 0, 24)
    BeginChrThread(0xD, 1, 0, 24)
    BeginChrThread(0x21, 1, 0, 24)
    BeginChrThread(0x22, 1, 0, 24)
    BeginChrThread(0x23, 1, 0, 24)
    BeginChrThread(0x24, 1, 0, 24)
    BeginChrThread(0x25, 1, 0, 24)
    BeginChrThread(0x26, 1, 0, 24)
    OP_68(-12000, 6200, 12900, 0)
    MoveCamera(15, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20750, 0)
    OP_68(-12000, 7200, 12900, 5000)
    MoveCamera(15, -2, 0, 5000)
    SetCameraDistance(22750, 5000)
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-500, 1000, -6500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 5000)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4AD6 end

    def Function_24_523A(): pass

    label("Function_24_523A")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5272"),
        (1, "loc_527A"),
        (2, "loc_5282"),
        (3, "loc_528A"),
        (4, "loc_5292"),
        (5, "loc_529A"),
        (6, "loc_52A2"),
        (SWITCH_DEFAULT, "loc_52AA"),
    )


    label("loc_5272")

    Sleep(100)
    Jump("loc_52B2")

    label("loc_527A")

    Sleep(200)
    Jump("loc_52B2")

    label("loc_5282")

    Sleep(300)
    Jump("loc_52B2")

    label("loc_528A")

    Sleep(400)
    Jump("loc_52B2")

    label("loc_5292")

    Sleep(500)
    Jump("loc_52B2")

    label("loc_529A")

    Sleep(600)
    Jump("loc_52B2")

    label("loc_52A2")

    Sleep(700)
    Jump("loc_52B2")

    label("loc_52AA")

    Sleep(800)
    Jump("loc_52B2")

    label("loc_52B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52DD")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_52B2")

    label("loc_52DD")

    Return()

    # Function_24_523A end

    def Function_25_52DE(): pass

    label("Function_25_52DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadChrToIndex("chr/ch24000.itc", 0x1F)
    LoadChrToIndex("chr/ch22300.itc", 0x20)
    LoadChrToIndex("chr/ch21000.itc", 0x21)
    LoadChrToIndex("chr/ch27900.itc", 0x22)
    LoadChrToIndex("chr/ch22800.itc", 0x23)
    LoadChrToIndex("chr/ch20500.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x20)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x21)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrChipByIndex(0x24, 0x22)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 0)
    SetChrChipByIndex(0x25, 0x23)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    BeginChrThread(0x25, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x24)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x39, 0xC)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    BeginChrThread(0x39, 0, 0, 0)
    SetChrChipByIndex(0x3A, 0xC)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    BeginChrThread(0x3A, 0, 0, 0)
    SetChrChipByIndex(0x3B, 0xC)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    BeginChrThread(0x3B, 0, 0, 0)
    SetChrChipByIndex(0x3C, 0xC)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    BeginChrThread(0x3C, 0, 0, 0)
    SetChrChipByIndex(0x3D, 0xC)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    BeginChrThread(0x3D, 0, 0, 0)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x17, 0x2E)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "light", 0x0, 0x1)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0xD, 0x2F)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x18, 0x30)
    OP_49()
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0x18, "light", 0x0, 0x1)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x19, 0x31)
    OP_49()
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    SetMapObjFrame(0x19, "light", 0x0, 0x1)
    ClearChrFlags(0x32, 0x80)
    OP_78(0x1A, 0x32)
    OP_49()
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    SetMapObjFrame(0x1A, "light", 0x0, 0x1)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x1B, 0x33)
    OP_49()
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFrame(0x1B, "light", 0x0, 0x1)
    ClearChrFlags(0x34, 0x80)
    OP_78(0xE, 0x34)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x7, 0x3E)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x8, 850, 0, -7200, 135)
    SetChrPos(0x9, 1850, 0, -2700, 90)
    SetChrPos(0xA, -250, 0, -4300, 135)
    SetChrPos(0xF, -500, 0, -5400, 90)
    SetChrPos(0xB, 600, 0, -5700, 90)
    SetChrPos(0xC, -550, 0, -8800, 90)
    SetChrPos(0xD, -700, 0, -9700, 90)
    SetChrPos(0xE, -1600, 0, -3350, 90)
    SetChrPos(0x39, 15900, 0, 6000, 270)
    SetChrPos(0x3A, 2450, 0, -5250, 90)
    SetChrPos(0x3B, 1150, 0, -9850, 90)
    SetChrPos(0x3C, -5750, 0, -4450, 270)
    SetChrPos(0x3D, 9500, 0, -9350, 315)
    SetChrPos(0x21, -2400, 0, -9300, 135)
    SetChrPos(0x22, 150, 0, -2900, 135)
    SetChrPos(0x23, 200, 0, -1900, 135)
    SetChrPos(0x24, -1650, 0, -7950, 90)
    SetChrPos(0x25, -1050, 0, -11000, 90)
    SetChrPos(0x26, -2700, 0, -7000, 135)
    SetChrPos(0x2D, 35000, 0, -4000, 270)
    OP_D5(0x34, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2E, 45000, 0, -4000, 270)
    OP_D5(0x34, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2F, 3700, 0, -20000, 0)
    OP_D5(0x2F, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x30, 3700, 0, -30000, 0)
    OP_D5(0x30, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x31, 3700, 0, -40000, 0)
    OP_D5(0x31, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x32, 3700, 0, -30000, 0)
    OP_D5(0x30, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x33, 3700, 0, -40000, 0)
    OP_D5(0x31, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x34, -6000, 0, -9150, 135)
    OP_D5(0x34, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x3E, -1700, 0, -2050, 200)
    OP_D5(0x3E, 0x0, 0x1ADB0, 0x0, 0x0)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0xA, 1, 0, 24)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0xC, 1, 0, 24)
    BeginChrThread(0xD, 1, 0, 24)
    BeginChrThread(0x21, 1, 0, 24)
    BeginChrThread(0x22, 1, 0, 24)
    BeginChrThread(0x23, 1, 0, 24)
    BeginChrThread(0x24, 1, 0, 24)
    BeginChrThread(0x25, 1, 0, 24)
    BeginChrThread(0x26, 1, 0, 24)
    BeginChrThread(0x2D, 1, 0, 26)
    BeginChrThread(0x2E, 1, 0, 26)
    OP_68(11000, 600, 800, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(47, 10, 0, 25000)
    SetCameraDistance(28000, 25000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(458, 0, 100, 0)
    Sleep(3500)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x2F, 1, 0, 27)
    BeginChrThread(0x30, 1, 0, 27)
    BeginChrThread(0x31, 1, 0, 27)
    Sleep(3500)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    ClearChrFlags(0x2D, 0x80)
    ClearMapObjFlags(0xC, 0x4)
    SetChrPos(0x2D, 3700, 0, -20000, 0)
    OP_D5(0x2D, 0x0, 0x0, 0x0, 0x0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x2D, 1, 0, 27)
    BeginChrThread(0x32, 1, 0, 27)
    BeginChrThread(0x33, 1, 0, 27)
    Sleep(3000)
    Sound(494, 0, 60, 0)
    Sleep(2000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_52DE end

    def Function_26_59B9(): pass

    label("Function_26_59B9")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, 0, -4000)
    OP_9F(0x1, 11500, 0, 1000)
    OP_9F(0x1, 12000, 0, 30000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_59F5():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59F5)
    Return()

    # Function_26_59B9 end

    def Function_27_5A06(): pass

    label("Function_27_5A06")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3700, 0, -20000)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 10580, 0, 4180)
    OP_9F(0x1, 12000, 0, 10000)
    OP_9F(0x1, 12000, 0, 15000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5A5E():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A5E)
    Return()

    # Function_27_5A06 end

    def Function_28_5A6F(): pass

    label("Function_28_5A6F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0xF, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x12, -24750, 1300, -16680, 180)
    SetChrPos(0x2D, 20000, 0, -5000, 270)
    OP_D5(0x2D, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(-13500, 1900, 4250, 0)
    MoveCamera(25, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_68(750, 1900, -5250, 10000)
    MoveCamera(50, 10, 0, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x38, 1, 0, 29)

    def lambda_5BE6():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5BE6)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_5A6F end

    def Function_29_5C55(): pass

    label("Function_29_5C55")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(3600)
    Sound(494, 0, 50, 0)
    Return()

    # Function_29_5C55 end

    def Function_30_5C68(): pass

    label("Function_30_5C68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13800.itc", 0x1E)
    LoadChrToIndex("chr/ch13801.itc", 0x1F)
    LoadChrToIndex("chr/ch13802.itc", 0x20)
    LoadChrToIndex("chr/ch08200.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50005.itc", 0x23)
    SoundLoad(847)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis244.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu08000.itp")
    OP_68(-28700, -7200, -23400, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x109, -28700, -8200, -21000, 180)
    SetChrPos(0x101, -28700, -8200, -21000, 180)
    SetChrPos(0x102, -28700, -8200, -21000, 180)
    SetChrPos(0x104, -28700, -8200, -21000, 180)
    SetChrPos(0x105, -28700, -8200, -21000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1E, 0x20)
    SetChrPos(0x1E, -28700, -3700, -41000, 0)
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -28700, -8200, -20000, 180)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-28700, -7200, -25400, 5000)
    FadeToBright(2000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x105, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 46)
    WaitChrThread(0x109, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Sound(846, 0, 100, 0)
    Sleep(300)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5F16():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F16)
    Sleep(50)

    def lambda_5F26():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5F26)
    Sleep(50)

    def lambda_5F36():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5F36)
    Sleep(50)

    def lambda_5F46():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5F46)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005Fthat……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PA bird's cry?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7519", 0)
    Fade(250)
    OP_68(-28700, -3900, -33700, 0)
    MoveCamera(43, 23, -11, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(-28700, -3900, -29700, 3000)
    MoveCamera(49, 23, -17, 3000)
    SetCameraDistance(14500, 3000)
    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -27600, -8200, -25400, 180)
    SetChrPos(0x102, -26200, -8200, -25400, 180)
    SetChrPos(0x104, -27700, -8200, -24100, 180)
    SetChrPos(0x109, -26300, -8200, -24100, 180)
    SetChrPos(0x105, -25100, -8200, -25700, 180)
    ClearChrFlags(0x1E, 0x80)

    def lambda_607A():

        label("loc_607A")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_607A")

    QueueWorkItem2(0x1E, 2, lambda_607A)

    def lambda_608C():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFE9BC, 0xFFFF9A70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_608C)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 3, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_60CE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60CE)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_60F6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_60F6)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_611E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_611E)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6146():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6146)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_616E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_616E)
    Sleep(2000)
    Fade(500)
    OP_68(-26800, -5900, -25400, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#6P#NWhat! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10111F#6P#NAnd then a white hawk …?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#12P……Disagreeable\x01",
            "It looks like falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey, what do you mean?\x01",
            "In the middle of such a city ……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1E, 0x3)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x0)
    OP_68(-27800, -6900, -26700, 3000)
    MoveCamera(37, 19, 0, 3000)

    def lambda_62AA():
        OP_9E(0xFE, 0xFFFF97B4, 0xFFFF9A70, 0x493E0, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_62AA)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1644), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1676), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16A8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16DA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x170C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x173E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17A2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17D4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1806), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x189C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x18CE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1932), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1996), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19C8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19FA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A2C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A5E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A90), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AC2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AF4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B26), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_644B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_644B)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_6494():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6494)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_64DD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_64DD)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CE8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D1A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D7E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1DB0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1DE2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E14), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E46), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E78), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1EAA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1EDC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F0E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x1E, 1)
    StopSound(847, 700, 60)
    Fade(250)
    EndChrThread(0x1E, 0x2)
    SetChrPos(0x1E, -28000, -7000, -27700, 0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x1)

    def lambda_65DB():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE2B4, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_65DB)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)
    WaitChrThread(0x1E, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1E,
        (
            "Pewie.\x02\x03",
            "Pui, Pui, Pewie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#5P#00001FWell, maybe ….\x01",
            "Is there something we have for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PWhen Zeit speaks\x01",
            "It feels like the same thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PWell, Tio if it's fine\x01",
            "It seems I understand what you are talking about ……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    ClearChrFlags(0x1D, 0x80)

    def lambda_681B():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA628, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_681B)

    def lambda_6835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6835)
    WaitChrThread(0x1D, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x1D,
        "#01105F#5POh, what's wrong?\x02",
    )

    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)

    def lambda_68AE():
        OP_96(0xFE, 0xFFFF90AC, 0xFFFFDFF8, 0xFFFF9750, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_68AE)
    Sleep(300)

    def lambda_68CB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68CB)
    Sleep(100)

    def lambda_68DB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68DB)
    Sleep(100)

    def lambda_68EB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_68EB)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x87, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FWow, it's a white trick!\x02\x03",
            "#01109FBeaked sharp pointed\x01",
            "Cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#08009FPew eyed\x02\x03",
            "#08000FPuii, Pui, Pui ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#6P#01103FHmm, hmm.\x02\x03",
            "#01102FI see, I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00012F(Keya …\x01",
            "After all I wonder? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(That's awesome, is not it? …)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    def lambda_6AC3():

        label("loc_6AC3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6AC3")

    QueueWorkItem2(0x1D, 2, lambda_6AC3)

    ChrTalk(
        0x1D,
        (
            "#6P#01100FWell, this girl,\x01",
            "It's called \"Sieg\".\x02\x03",
            "Because there are messages in Lloyd's\x01",
            "I'm telling you to accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FWell, maybe ….\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1E, 500)

    ChrTalk(
        0x104,
        (
            "#00305F#5POh, surely on the legs\x01",
            "The memo is bound up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BB7():
        OP_95(0xFE, -27600, -8200, -26600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BB7)
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    def lambda_6BDB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BDB)
    WaitChrThread(0x101, 1)
    EndChrThread(0x1D, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is on the leg of white falcon\x01",
            "I took the memo attached.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dear Sir Crossbell Police, Mission Support Division\x02\x03",
            "Hearing the reputation of everyone\x01",
            "Incomplete#4RBrute#But I contacted you.\x02\x03",
            "If you have time confidentially\x01",
            "Would you please take a look at the consultation?\x02\x03",
            "Today evening, Crossbell Airport,\x01",
            "We are waiting at the waiting terrace.\x02\x03",
            "Postscript If you can not conveniently\x01",
            "You do not have to answer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00101F#11PHere, this …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106F#5PContents and nice, sender unknown and nice\x01",
            "I am too suspicious but … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302F#11PBut it's a beautiful handwriting,\x01",
            "The sentences are also polite feeling.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301F#5PMore than anything, it is pushed by memos\x01",
            "The emblem of that white falcon is …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1E,
        (
            "#08000F#12PPewie.\x02\x03",
            "Pui, Pui, Pewie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    Sound(847, 2, 70, 0)

    def lambda_6F79():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE4A8, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6F79)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    Sleep(100)
    SetChrSubChip(0x1E, 0x0)
    Sleep(100)
    SetChrSubChip(0x1E, 0x1)
    WaitChrThread(0x1E, 1)
    OP_68(-27800, -5900, -30700, 5000)
    MoveCamera(43, 19, 0, 5000)
    SetCameraDistance(16000, 5000)
    Fade(250)
    SetChrPos(0x1E, -28000, -7500, -27700, 0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x1)

    def lambda_6FFF():

        label("loc_6FFF")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_6FFF")

    QueueWorkItem2(0x1E, 2, lambda_6FFF)
    BeginChrThread(0x1E, 3, 0, 32)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D1A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CE8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B26), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AF4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1AC2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A90), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A5E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A2C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19FA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x19C8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1996), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1932), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x18CE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x189C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1806), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17D4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x17A2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x173E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x170C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16DA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x16A8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1676), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1644), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x1E, 3)

    def lambda_7234():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFEF98, 0xFFFF64EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7234)
    Sleep(300)

    def lambda_7251():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7251)
    Sleep(100)

    def lambda_7261():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7261)
    Sleep(100)

    def lambda_7271():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7271)
    Sleep(100)

    def lambda_7281():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7281)
    StopSound(847, 2000, 60)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0xFF)
    SetChrFlags(0x1E, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(-27800, -6900, -26700, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    TurnDirection(0x101, 0x1D, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00011FEr …\x01",
            "Kaor, what is he?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    ChrTalk(
        0x1D,
        (
            "#6P#01111FWell, I do not go or go\x01",
            "It depends on Lloyd's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FReally……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_7401():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7401)
    Sleep(50)

    def lambda_7411():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7411)
    Sleep(50)

    def lambda_7421():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7421)
    Sleep(50)

    def lambda_7431():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7431)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#11PWhere are you going to do?\x02\x03",
            "#00101FNo way\x01",
            "I do not think there is nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5POh, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PBut, the emblem of white falcons ……\x01",
            "It seems that the current child was like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PHaha, no, no more\x01",
            "I will expect it.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(450)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#6P#00003F── It is a great teaser.\x01",
            "I will accept it here.\x02\x03",
            "#00000FI still have time until the evening\x01",
            "Even after I've done errands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PI knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5PI was nervous …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PWell, as expected\x01",
            "I do not think we need to go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHuff, then then when you finish\x01",
            "Shall we go to the south exit crossbar airport?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FI do not really know.\x01",
            "Everyone, do your best.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetChrFlags(0x1D, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -27700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 7)
    OP_29(0xA3, 0x1, 0x11)
    OP_C9(0x1, 0x1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_24(0x34F)
    EventEnd(0x5)
    Return()

    # Function_30_5C68 end

    def Function_31_7758(): pass

    label("Function_31_7758")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7787")

    def lambda_7768():
        OP_9E(0xFE, 0xFFFF99A8, 0xFFFF9A70, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7768)
    WaitChrThread(0x1E, 1)
    Jump("Function_31_7758")

    label("loc_7787")

    Return()

    # Function_31_7758 end

    def Function_32_7788(): pass

    label("Function_32_7788")


    def lambda_778D():
        OP_9E(0xFE, 0xFFFF9494, 0xFFFF93CC, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_778D)
    WaitChrThread(0x1E, 1)

    def lambda_77AC():
        OP_9E(0xFE, 0xFFFF90AC, 0xFFFF93CC, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_77AC)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_32_7788 end

    def Function_33_77C7(): pass

    label("Function_33_77C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KThe next day, 8: 00 -\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    SetChrPos(0xF, -6100, 0, 9400, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, 9400, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x2D, -20000, 0, -5000, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-3650, 1900, 15980, 0)
    MoveCamera(45, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(-3650, 1900, 16000, 10000)
    MoveCamera(25, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(40000, 10000)
    PlayBGM("ed7125", 0)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    Sound(494, 0, 80, 0)

    def lambda_7978():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7978)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    MoveCamera(35, 15, 0, 4000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_77C7 end

    def Function_34_79F2(): pass

    label("Function_34_79F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9400, 270)
    OP_68(-5400, 1900, 7000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-1000, 1900, 0, 10000)
    MoveCamera(30, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(27000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_79F2 end

    def Function_35_7B42(): pass

    label("Function_35_7B42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(946)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -16750, 0, 18400, 135)
    SetChrPos(0x102, -17500, 0, 17650, 135)
    SetChrPos(0x103, -18500, 0, 17650, 135)
    SetChrPos(0x104, -16750, 0, 19400, 135)
    SetChrPos(0x109, -17750, 0, 19400, 135)
    SetChrPos(0x105, -18500, 0, 18650, 135)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0x10, 0x2F)
    OP_49()
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x11, 0x30)
    OP_49()
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x12, 0x31)
    OP_49()
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    SetChrPos(0x2F, -27000, -170, -3600, 90)
    SetChrPos(0x30, -35000, -1500, -3600, 90)
    SetChrPos(0x31, -43000, -2830, -3600, 90)
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D28")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_7CF7():

        label("loc_7CF7")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7CF7")

    QueueWorkItem2(0xA, 2, lambda_7CF7)

    def lambda_7D09():

        label("loc_7D09")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7D09")

    QueueWorkItem2(0xB, 2, lambda_7D09)

    def lambda_7D1B():

        label("loc_7D1B")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7D1B")

    QueueWorkItem2(0x13, 2, lambda_7D1B)

    label("loc_7D28")

    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_7D6D():
        OP_9B(0x0, 0x101, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D6D)
    Sleep(50)

    def lambda_7D85():
        OP_9B(0x0, 0x102, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7D85)
    Sleep(50)

    def lambda_7D9D():
        OP_9B(0x0, 0x103, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7D9D)
    Sleep(50)

    def lambda_7DB5():
        OP_9B(0x0, 0x104, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7DB5)
    Sleep(50)

    def lambda_7DCD():
        OP_9B(0x0, 0x105, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7DCD)
    Sleep(50)

    def lambda_7DE5():
        OP_9B(0x0, 0x109, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DE5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    OP_0D()
    Sound(946, 2, 40, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PThis sound ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#5PIt sounds like a siren.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_25(0x3B2, 0x3C)
    Fade(1000)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x109, 0xB4, 0x0)
    OP_93(0x105, 0xB4, 0x0)
    OP_68(-10000, 500, -900, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(8150, 500, -19200, 10000)
    MoveCamera(30, 20, 0, 10000)
    BeginChrThread(0x38, 1, 0, 37)
    BeginChrThread(0x2F, 3, 0, 36)
    BeginChrThread(0x30, 3, 0, 36)
    BeginChrThread(0x31, 3, 0, 36)
    WaitChrThread(0x2F, 3)
    WaitChrThread(0x30, 3)
    WaitChrThread(0x31, 3)
    StopSound(946, 3000, 50)
    OP_0D()
    Fade(500)
    OP_93(0x101, 0x87, 0x0)
    OP_93(0x102, 0x87, 0x0)
    OP_93(0x103, 0x87, 0x0)
    OP_93(0x104, 0x87, 0x0)
    OP_93(0x109, 0x87, 0x0)
    OP_93(0x105, 0x87, 0x0)
    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10101F#5PThere are as many as three ambulances ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PAfter all the injured person of derailment accident\x01",
            "I wonder if they are carrying …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PWell, this timing\x01",
            "I guess there is no mistake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P…… Cecil's older sisters too\x01",
            "It seems to be busy.\x02\x03",
            "#00001FLet's hurry to the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5POh.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8161")
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x13, 0x2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0x13, 0x8000)

    label("loc_8161")

    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 6)
    OP_24(0x3B2)
    EventEnd(0x5)
    Return()

    # Function_35_7B42 end

    def Function_36_818F(): pass

    label("Function_36_818F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13000, 500, -2870)
    OP_9F(0x1, -350, 0, -7080)
    OP_9F(0x1, 4300, 0, -18000)
    OP_9F(0x1, 4500, 0, -30000)
    OP_9F(0x1, 4500, 0, -40000)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_36_818F end

    def Function_37_81E3(): pass

    label("Function_37_81E3")

    Sound(465, 0, 80, 0)
    Sleep(4000)
    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 80, 0)
    Return()

    # Function_37_81E3 end

    def Function_38_81FC(): pass

    label("Function_38_81FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(946)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x8, 0x2D)
    OP_49()
    SetChrPos(0x2D, -21060, 0, 22140, 135)
    OP_D5(0x2D, 0x0, 0x20F58, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0x10, 0x2F)
    OP_49()
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x11, 0x30)
    OP_49()
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x31, 0x80)
    OP_78(0x12, 0x31)
    OP_49()
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    SetChrPos(0x2F, -27000, -170, -3600, 90)
    SetChrPos(0x30, -35000, -1500, -3600, 90)
    SetChrPos(0x31, -43000, -2830, -3600, 90)
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_83E1")
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_83B0():

        label("loc_83B0")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83B0")

    QueueWorkItem2(0xA, 2, lambda_83B0)

    def lambda_83C2():

        label("loc_83C2")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83C2")

    QueueWorkItem2(0xB, 2, lambda_83C2)

    def lambda_83D4():

        label("loc_83D4")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_83D4")

    QueueWorkItem2(0x13, 2, lambda_83D4)

    label("loc_83E1")

    Sound(946, 2, 60, 0)
    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_68(-13580, 1500, 1970, 5000)
    MoveCamera(6, 27, 0, 5000)
    SetCameraDistance(24500, 5000)
    BeginChrThread(0x2D, 3, 0, 39)
    BeginChrThread(0x38, 1, 0, 40)
    WaitChrThread(0x2D, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(700)
    Fade(1000)
    OP_68(-10000, 500, -900, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(8150, 500, -19200, 10000)
    MoveCamera(30, 20, 0, 10000)
    BeginChrThread(0x38, 1, 0, 37)
    BeginChrThread(0x2F, 3, 0, 36)
    BeginChrThread(0x30, 3, 0, 36)
    BeginChrThread(0x31, 3, 0, 36)
    WaitChrThread(0x2F, 3)
    WaitChrThread(0x30, 3)
    StopSound(946, 2000, 50)
    WaitChrThread(0x31, 3)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x3B2)
    SetScenarioFlags(0x22, 6)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_81FC end

    def Function_39_84EE(): pass

    label("Function_39_84EE")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13630, 0, 14510)
    OP_9F(0x1, -11670, 0, 9100)
    OP_9F(0x1, -12500, 0, 4800)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x8)
    Return()

    # Function_39_84EE end

    def Function_40_8535(): pass

    label("Function_40_8535")

    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 50, 0)
    Return()

    # Function_40_8535 end

    def Function_41_8548(): pass

    label("Function_41_8548")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-28700, -7200, -23400, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x109, -28700, -8200, -21000, 180)
    SetChrPos(0x101, -28700, -8200, -21000, 180)
    SetChrPos(0x102, -28700, -8200, -21000, 180)
    SetChrPos(0x103, -28700, -8200, -21000, 180)
    SetChrPos(0x105, -28700, -8200, -21000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-28700, -7200, -25400, 5000)
    FadeToBright(2000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 46)
    WaitChrThread(0x109, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#6P#10302FWell, at the entertainment district casino\x01",
            "Was it two in old town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11POh, clues to other places too\x01",
            "There may be, but …\x02\x03",
            "#00001FTentatively outside the city\x01",
            "I do not seem to have any leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FFortunately, this morning a new support request\x01",
            "It seems I did not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FPerhaps because of the incident of yesterday\x01",
            "The headquarters is also confused.\x02\x03",
            "#00101FThe guard is quite\x01",
            "It seems I got damaged … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5P………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8864():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8864)

    def lambda_8871():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8871)
    Sleep(50)

    def lambda_8881():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8881)
    Sleep(50)

    def lambda_8891():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8891)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00106F……I'm sorry.\x02\x03",
            "#00108FFrom the standpoint of you\x01",
            "You do not have to do anything else ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5P…… No, that kind of danger\x01",
            "The guard#6RWe#Because it is a job title.\x02\x03",
            "#10100FBesides, to the end now\x01",
            "I am a member of the Special Affairs Support Division.\x02\x03",
            "let's go……\x01",
            "Get Randy seniors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11P……Ah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -28700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_29(0xA9, 0x1, 0x7)
    OP_29(0xA9, 0x4, 0x10)
    OP_29(0xAA, 0x4, 0x2)
    OP_29(0xAA, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_8548 end

    def Function_42_8A19(): pass

    label("Function_42_8A19")


    def lambda_8A1E():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A1E)

    def lambda_8A38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A38)
    WaitChrThread(0xFE, 1)

    def lambda_8A4D():
        OP_95(0xFE, -27400, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A4D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_42_8A19 end

    def Function_43_8A6E(): pass

    label("Function_43_8A6E")


    def lambda_8A73():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8A73)

    def lambda_8A8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A8D)
    WaitChrThread(0xFE, 1)

    def lambda_8AA2():
        OP_95(0xFE, -28000, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AA2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_8A6E end

    def Function_44_8AC3(): pass

    label("Function_44_8AC3")


    def lambda_8AC8():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AC8)

    def lambda_8AE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AE2)
    WaitChrThread(0xFE, 1)

    def lambda_8AF7():
        OP_95(0xFE, -29400, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8AF7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_44_8AC3 end

    def Function_45_8B18(): pass

    label("Function_45_8B18")


    def lambda_8B1D():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B1D)

    def lambda_8B37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B37)
    WaitChrThread(0xFE, 1)

    def lambda_8B4C():
        OP_95(0xFE, -30000, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B4C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_8B18 end

    def Function_46_8B6D(): pass

    label("Function_46_8B6D")


    def lambda_8B72():
        OP_95(0xFE, -28700, -8200, -23700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B72)

    def lambda_8B8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B8C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_8B6D end

    def Function_47_8B9D(): pass

    label("Function_47_8B9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -4510, 0, -8420, 180)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x13, 0x2D)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x2D, -20000, 0, -5000, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-5400, 1900, 7000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-700, 2500, 3000, 10000)
    MoveCamera(30, 5, 0, 10000)
    SetCameraDistance(27000, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Sound(457, 0, 80, 0)

    def lambda_8D3E():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8D3E)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(457, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8B9D end

    def Function_48_8D75(): pass

    label("Function_48_8D75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41500.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x9, 0x2E)
    OP_49()
    SetChrPos(0x2E, -1000, 0, 18000, 180)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x3)
    OP_4B(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2500, 0, 16000, 180)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 2400, 0, 16000, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x21, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 350, 0, 13000, 0)
    SetChrChipByIndex(0x22, 0x4)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -2800, 0, 11500, 0)
    SetChrChipByIndex(0x23, 0x2)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -1500, 0, 11100, 0)
    SetChrChipByIndex(0x24, 0x3)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 0, 0, 11100, 0)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 1300, 0, 12000, 0)
    SetChrChipByIndex(0x26, 0x5)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 2300, 0, 11600, 0)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -2800, 0, 13100, 0)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(0, 1700, 13700, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    MoveCamera(30, 25, 0, 15000)
    SetCameraDistance(17000, 15000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That will, just the other day,\x01",
            "Fear and sorrow of this crossbell\x01",
            "I knocked down to the bottom.\x02\x03",
            "If you are an intelligent citizen,\x01",
            "I think that I have noticed … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x9, 0x2)
    Sleep(600)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I dare, today in this place\x01",
            "Let's impeach that power by name.\x02\x03",
            "\"Eleven Empire Government\" … …\x01",
            "That is one of its wicked will.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_8D75 end

    def Function_49_9147(): pass

    label("Function_49_9147")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    LoadChrToIndex("apl/ch51080.itc", 0x21)
    SoundLoad(3623)
    SoundLoad(3624)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01104.itp")
    OP_68(-27200, -7200, -23000, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -27800, -8200, -24700, 90)
    SetChrPos(0x102, -26000, -8200, -24100, 90)
    SetChrPos(0x103, -26600, -8200, -25300, 90)
    SetChrPos(0x104, -27200, -8200, -23500, 90)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -28700, -8200, -20000, 180)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9241():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9241)
    Sleep(50)

    def lambda_925E():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_925E)
    Sleep(50)

    def lambda_927B():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_927B)
    Sleep(50)

    def lambda_9298():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9298)
    OP_68(-27200, -7200, -24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x1D, 3, 0, 50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)

    def lambda_932B():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_932B)
    Sleep(50)

    def lambda_933B():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_933B)
    Sleep(50)

    def lambda_934B():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_934B)
    Sleep(50)

    def lambda_935B():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_935B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x1D, 3)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)

    ChrTalk(
        0x101,
        "#00005F#11PKeya?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1D,
        "#6P#01123F#3623V#30W#15A~~~ っ ~~~ ……!\x02",
    )

    CloseMessageWindow()
    OP_24(0xE27)
    OP_C9(0x1, 0x80000000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_93ED():
        OP_96(0xFE, 0xFFFFA498, 0xFFFFDFF8, 0xFFFF9F84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_93ED)
    Sleep(300)
    Fade(250)
    OP_68(-24900, -7100, -24000, 0)
    MoveCamera(327, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13500, 0)
    OP_68(-22900, -7100, -24700, 1000)
    MoveCamera(323, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    WaitChrThread(0x1D, 1)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9474():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9474)

    def lambda_948D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_948D)

    def lambda_949A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_949A)
    OP_6F(0x79)
    SetCameraDistance(12500, 50000)

    ChrTalk(
        0x101,
        "#11P#00011FWow …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FKeya …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhere are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PIt certainly happens a lot.\x01",
            "Is not it worried?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#01114F#30W………Yup……………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetCameraDistance(12500, 1000)
    Sound(898, 0, 60, 0)
    Fade(250)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x1)
    OP_93(0x101, 0x5A, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00004F…… It's all right, Ka'a.\x02\x03",
            "#00008FCertainly this time,\x01",
            "What happens to the crossbell\x01",
            "I do not understand it ….\x02\x03",
            "#00002FWe are always\x01",
            "I will return to Ka'aa\x01",
            "It will never change.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "#5P#01105F#30WLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FI agree……\x01",
            "That is certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PEven when we went before\x01",
            "You came home properly, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FSo Ka'aa-chan.\x01",
            "Please wait with peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#01121F#40WEli, Tio, Randy ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1D)
    MoveCamera(326, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x10E, 0x0)

    def lambda_97D4():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFF9F84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_97D4)
    WaitChrThread(0x1D, 1)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x1D,
        (
            "#3624V#30WYup……#800WIt is!\x01",
            "#30WEveryone, be careful!\x02",
        )
    )

    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE28)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wadi from party members\x01",
            "I got out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x8000)
    SetChrPos(0x0, -25340, -8200, -24760, 90)
    OP_69(0xFF, 0x0)
    OP_29(0xAC, 0x4, 0x10)
    OP_29(0xAD, 0x4, 0x2)
    OP_29(0xAD, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9969")
    Jump("loc_996E")

    label("loc_9969")

    OP_29(0x8E, 0x4, 0x40)

    label("loc_996E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_997F")
    Jump("loc_9984")

    label("loc_997F")

    OP_29(0x8F, 0x4, 0x40)

    label("loc_9984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9995")
    Jump("loc_999A")

    label("loc_9995")

    OP_29(0x90, 0x4, 0x40)

    label("loc_999A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99AB")
    Jump("loc_99B0")

    label("loc_99AB")

    OP_29(0x91, 0x4, 0x40)

    label("loc_99B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99C1")
    Jump("loc_99C6")

    label("loc_99C1")

    OP_29(0x92, 0x4, 0x40)

    label("loc_99C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_99D7")
    Jump("loc_99DC")

    label("loc_99D7")

    OP_29(0x93, 0x4, 0x40)

    label("loc_99DC")

    SubItemNumber('废弃材料', 10)
    SubItemNumber('苦西红柿酱', 1)
    SubItemNumber('金属探测器', 1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    PlayBGM("ed7151", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7151")
    ReplaceBGM("ed7101", "ed7151")
    ReplaceBGM("ed7116", "ed7151")
    ReplaceBGM("ed7117", "ed7151")
    EventEnd(0x5)
    Return()

    # Function_49_9147 end

    def Function_50_9A2C(): pass

    label("Function_50_9A2C")

    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9A54():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9A54)

    def lambda_9A6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9A6E)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_9A9D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9A9D)
    Return()

    # Function_50_9A2C end

    def Function_51_9AA6(): pass

    label("Function_51_9AA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadEffect(0x0, "event/ev17033.eff")
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x9, 0x2E)
    OP_49()
    SetChrPos(0x2E, -1000, 0, 18000, 180)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x5)
    SetChrPos(0x0, 13600, 0, -14000, 0)
    SetChrPos(0x1, 13600, 0, -14000, 0)
    SetChrPos(0x2, 13600, 0, -14000, 0)
    SetChrPos(0x3, 13600, 0, -14000, 0)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 3000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x21, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 350, 0, 13000, 0)
    SetChrChipByIndex(0x22, 0x4)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -8300, 0, 5000, 0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x2)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7000, 0, 4600, 0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x3)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -8000, 0, 4100, 0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 8800, 0, 5000, 0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x5)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 9800, 0, 4600, 0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -13800, 0, 8100, 0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1600, 8700, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    BeginChrThread(0x2E, 3, 0, 52)
    OP_68(0, 1600, 13700, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(250)
    OP_70(0x9, 0x7)
    Sleep(500)
    SetMessageWindowPos(50, 120, -1, -1)
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WAs you are all well aware\x02\x03",
            "The other day, Mayor of former Clois\x01",
            "The foundation of \"Crossbell independent country\"\x01",
            "It was declared.\x02\x03",
            "A military organization called Defense Army was also established,\x01",
            "People who are getting used to the new regime too\x01",
            "I guess there are … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x9, 0x8)
    Sleep(600)
    SetMessageWindowPos(50, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W── But, everyone!\x01",
            "I would like to think again once again!\x02\x03",
            "In fact, we\x01",
            "I wonder if you truly \"chose\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x2E, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    WaitChrThread(0x25, 3)
    WaitChrThread(0x26, 3)
    WaitChrThread(0x27, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_9AA6 end

    def Function_52_9F67(): pass

    label("Function_52_9F67")

    Sleep(3000)
    BeginChrThread(0x25, 3, 0, 56)
    Sleep(100)
    BeginChrThread(0x26, 3, 0, 57)
    Sleep(2000)
    BeginChrThread(0x27, 3, 0, 58)
    Sleep(3000)
    BeginChrThread(0x22, 3, 0, 53)
    Sleep(100)
    BeginChrThread(0x23, 3, 0, 54)
    Sleep(100)
    BeginChrThread(0x24, 3, 0, 55)
    Return()

    # Function_52_9F67 end

    def Function_53_9F9E(): pass

    label("Function_53_9F9E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9FAE():
        OP_95(0xFE, -2800, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FAE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_53_9F9E end

    def Function_54_9FCF(): pass

    label("Function_54_9FCF")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9FDF():
        OP_95(0xFE, -1500, 0, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FDF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_54_9FCF end

    def Function_55_A000(): pass

    label("Function_55_A000")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A010():
        OP_95(0xFE, -2500, 0, 10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A010)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_55_A000 end

    def Function_56_A031(): pass

    label("Function_56_A031")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A041():
        OP_95(0xFE, 1300, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A041)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_56_A031 end

    def Function_57_A062(): pass

    label("Function_57_A062")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A072():
        OP_95(0xFE, 2300, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A072)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_57_A062 end

    def Function_58_A093(): pass

    label("Function_58_A093")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A0A3():
        OP_95(0xFE, -2800, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0A3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_58_A093 end

    def Function_59_A0C4(): pass

    label("Function_59_A0C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20000.itc", 0x1E)
    LoadEffect(0x0, "event/ev17033.eff")
    SoundLoad(828)
    SetChrPos(0x0, 13600, 0, -14000, 0)
    SetChrPos(0x1, 13600, 0, -14000, 0)
    SetChrPos(0x2, 13600, 0, -14000, 0)
    SetChrPos(0x3, 13600, 0, -14000, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 3000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 3000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_68(0, 2500, 4000, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 2000, 4000, 10000)
    MoveCamera(50, 29, 0, 10000)
    SetCameraDistance(24000, 10000)
    Sound(828, 2, 80, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 60)
    StopSound(828, 1000, 70)
    StopEffect(0x0, 0x2)
    Sleep(5500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x33C)
    SetScenarioFlags(0x22, 1)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_A0C4 end

    def Function_60_A2AB(): pass

    label("Function_60_A2AB")

    BeginChrThread(0x9, 3, 0, 66)
    Sleep(300)
    OP_4B(0xE, 0xFF)
    BeginChrThread(0xE, 3, 0, 63)
    Sleep(500)
    OP_4B(0xC, 0xFF)
    BeginChrThread(0xC, 3, 0, 64)
    Sleep(50)
    OP_4B(0xD, 0xFF)
    BeginChrThread(0xD, 3, 0, 65)
    Sleep(500)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0xB, 3, 0, 61)
    Sleep(300)
    OP_4B(0xF, 0xFF)
    BeginChrThread(0xF, 3, 0, 62)
    Return()

    # Function_60_A2AB end

    def Function_61_A2F3(): pass

    label("Function_61_A2F3")


    def lambda_A2F8():
        OP_95(0xFE, -1600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A2F8)
    WaitChrThread(0xB, 1)
    Return()

    # Function_61_A2F3 end

    def Function_62_A312(): pass

    label("Function_62_A312")


    def lambda_A317():
        OP_95(0xFE, -2900, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A317)
    WaitChrThread(0xF, 1)
    Return()

    # Function_62_A312 end

    def Function_63_A331(): pass

    label("Function_63_A331")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A34B():
        OP_95(0xFE, 6300, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A34B)
    WaitChrThread(0xE, 1)
    Return()

    # Function_63_A331 end

    def Function_64_A365(): pass

    label("Function_64_A365")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A38C():
        OP_95(0xFE, -1100, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A38C)
    WaitChrThread(0xC, 1)
    Return()

    # Function_64_A365 end

    def Function_65_A3A6(): pass

    label("Function_65_A3A6")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A3CD():
        OP_95(0xFE, 400, 0, 12100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A3CD)
    WaitChrThread(0xD, 1)
    Return()

    # Function_65_A3A6 end

    def Function_66_A3E7(): pass

    label("Function_66_A3E7")

    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -6900, 0, 4200, 270)
    OP_0D()
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_66_A3E7 end

    def Function_67_A430(): pass

    label("Function_67_A430")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch03250.itc", 0x24)
    LoadChrToIndex("monster/ch85152.itc", 0x27)
    LoadEffect(0x0, "event/ev17060.eff")
    SoundLoad(828)
    OP_32(0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x101, 3600, 0, -27000, 0)
    SetChrPos(0x102, 3600, 0, -27000, 0)
    SetChrPos(0x103, 2200, 0, -27000, 0)
    SetChrPos(0x104, 3600, 0, -27000, 0)
    SetChrPos(0x109, 3600, 0, -27000, 0)
    SetChrPos(0x105, 2200, 0, -27000, 0)
    SetChrPos(0x106, 2200, 0, -27000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrChipByIndex(0x28, 0x10)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x10)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4300, 0, -9500, 270)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x10)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -7500, 0, -6600, 105)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 2500, 4000, 0)
    MoveCamera(57, 5, -20, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_F0(0x0, 0x1)
    Sound(828, 2, 80, 0)
    MoveCamera(23, 10, -15, 9000)
    SetCameraDistance(24000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5500)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 70)
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(250)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 71)
    Sleep(250)
    BeginChrThread(0x106, 3, 0, 73)
    Sleep(250)
    BeginChrThread(0x109, 3, 0, 74)
    OP_6F(0x79)
    Fade(500)
    OP_68(2900, 1300, -17000, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(-900, 1500, -2000, 5000)
    MoveCamera(43, 13, 0, 5000)
    SetCameraDistance(18000, 5000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#12PThis is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PI wrapped Crossbell City\x01",
            "It is similar to \"barrier\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F#12PI think it's the same type\x02\x03",
            "#00201F…… And the resonance of the bell\x01",
            "I wonder if this moya is occurring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12POi oi, what the hell for\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x38, 1, 0, 83)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A8B5():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8B5)

    def lambda_A8C2():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A8C2)
    Sleep(50)

    def lambda_A8D2():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A8D2)

    def lambda_A8DF():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_A8DF)
    Sleep(50)

    def lambda_A8EF():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A8EF)

    def lambda_A8FC():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A8FC)
    Sleep(50)

    def lambda_A90C():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A90C)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PThis is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#11P── Take care.\x01",
            "I come from around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10410F#11PAnd they are….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x38, 0x1)
    Fade(500)
    OP_68(-7500, 1100, -6600, 0)
    MoveCamera(337, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    OP_F0(0x0, 0xD)
    SetCameraDistance(12000, 2000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    BeginChrThread(0x28, 0, 0, 75)
    BeginChrThread(0x29, 0, 0, 75)
    BeginChrThread(0x2A, 0, 0, 75)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AA37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_AA37)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Sleep(300)
    OP_68(-1900, 1300, -7000, 3000)
    MoveCamera(47, 15, 0, 3000)
    SetCameraDistance(14000, 3000)
    PlayEffect(0x0, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(985, 0, 70, 0)
    Sleep(2000)

    def lambda_AAF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_AAF1)
    Sleep(300)

    def lambda_AB05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_AB05)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00107FThe ones that were at the Stargaze Tower!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00207FIt is the same magical golem\x01",
            "It seems to be far more dangerous …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00307FAnyway, let's take them out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00007FYeah! Get ready!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x28, 3, 0, 77)
    BeginChrThread(0x29, 3, 0, 77)
    BeginChrThread(0x2A, 3, 0, 77)
    Sleep(260)
    Sound(951, 0, 70, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(11500, 500)
    Sleep(500)
    Sound(532, 0, 100, 0)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x2A, 0xFF)
    SetChrBattleFlags(0x6, 0x8)
    Battle("BattleInfo_CF8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_49()
    ClearChrBattleFlags(0x6, 0x8)
    Call(0, 84)
    Return()

    # Function_67_A430 end

    def Function_68_AD47(): pass

    label("Function_68_AD47")


    def lambda_AD4C():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD4C)
    WaitChrThread(0xFE, 1)

    def lambda_AD6A():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD6A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_AD47 end

    def Function_69_AD84(): pass

    label("Function_69_AD84")


    def lambda_AD89():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD89)
    WaitChrThread(0xFE, 1)

    def lambda_ADA7():
        OP_96(0xFE, 0x64, 0x0, 0xFFFFEB4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADA7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_AD84 end

    def Function_70_ADC1(): pass

    label("Function_70_ADC1")


    def lambda_ADC6():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADC6)
    WaitChrThread(0xFE, 1)

    def lambda_ADE4():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADE4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_ADC1 end

    def Function_71_ADFE(): pass

    label("Function_71_ADFE")


    def lambda_AE03():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE03)
    WaitChrThread(0xFE, 1)

    def lambda_AE21():
        OP_96(0xFE, 0x190, 0x0, 0xFFFFE50C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE21)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_ADFE end

    def Function_72_AE3B(): pass

    label("Function_72_AE3B")


    def lambda_AE40():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE40)
    WaitChrThread(0xFE, 1)

    def lambda_AE5E():
        OP_96(0xFE, 0xFFFFF4AC, 0x0, 0xFFFFE7C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE5E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_AE3B end

    def Function_73_AE78(): pass

    label("Function_73_AE78")


    def lambda_AE7D():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE7D)
    WaitChrThread(0xFE, 1)

    def lambda_AE9B():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE3E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE9B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_AE78 end

    def Function_74_AEB5(): pass

    label("Function_74_AEB5")


    def lambda_AEBA():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEBA)
    WaitChrThread(0xFE, 1)

    def lambda_AED8():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFE37C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_AEB5 end

    def Function_75_AEF2(): pass

    label("Function_75_AEF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF10")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_75_AEF2")

    label("loc_AF10")

    Return()

    # Function_75_AEF2 end

    def Function_76_AF11(): pass

    label("Function_76_AF11")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF2D")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_76_AF11")

    label("loc_AF2D")

    Return()

    # Function_76_AF11 end

    def Function_77_AF2E(): pass

    label("Function_77_AF2E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_AF5F():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF5F)
    Sleep(1000)
    SetChrFlags(0xFE, 0x20)

    def lambda_AF80():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFE764, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF80)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_AF2E end

    def Function_78_AFA8(): pass

    label("Function_78_AFA8")

    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_AFE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFE7)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_78_AFA8 end

    def Function_79_AFFB(): pass

    label("Function_79_AFFB")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B03A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B03A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_79_AFFB end

    def Function_80_B04E(): pass

    label("Function_80_B04E")

    PlayEffect(0x0, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B08D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B08D)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_80_B04E end

    def Function_81_B0A1(): pass

    label("Function_81_B0A1")

    PlayEffect(0x0, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B0E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0E0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_81_B0A1 end

    def Function_82_B0F4(): pass

    label("Function_82_B0F4")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B133():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B133)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_82_B0F4 end

    def Function_83_B147(): pass

    label("Function_83_B147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B160")
    Sound(986, 0, 80, 0)
    Sleep(1000)
    Jump("Function_83_B147")

    label("loc_B160")

    Return()

    # Function_83_B147 end

    def Function_84_B161(): pass

    label("Function_84_B161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(3465)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    AddParty(0x9, 0xFF, 0xFF)
    OP_32(0x9, 0x0, 0x5F)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x467, 0xFF)
    OP_42(0x9, 0x5ED, 0xFF)
    OP_42(0x9, 0x651, 0xFF)
    OP_38(0x9, 0x81, 0x2)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x2)
    OP_38(0x9, 0x85, 0x2)
    OP_38(0x9, 0x86, 0x1)
    OP_42(0x9, 0x72, 0x1)
    OP_42(0x9, 0xAD, 0x2)
    OP_42(0x9, 0x93, 0x3)
    OP_42(0x9, 0x8A, 0x4)
    OP_42(0x9, 0x90, 0x5)
    OP_42(0x9, 0x69, 0x6)
    AddCraft(0x9, 0xF8)
    AddCraft(0x9, 0x17A)
    AddCraft(0x9, 0x148)
    SetChrChipPat(0x9, 0x6, 0x145)
    SetChrChipPat(0x9, 0x6, 0x148)
    SetChrChipPat(0x9, 0x6, 0x146)
    LoadChrToIndex("apl/ch50539.itc", 0x0)
    LoadChrToIndex("apl/ch50506.itc", 0x1)
    LoadChrToIndex("apl/ch50509.itc", 0x2)
    LoadChrToIndex("chr/ch00950.itc", 0x3)
    LoadChrToIndex("chr/ch00951.itc", 0x4)
    LoadChrToIndex("chr/ch00952.itc", 0x5)
    LoadChrToIndex("chr/ch00050.itc", 0x6)
    LoadChrToIndex("chr/ch00051.itc", 0x7)
    LoadChrToIndex("chr/ch00150.itc", 0x8)
    LoadChrToIndex("chr/ch00151.itc", 0x9)
    LoadChrToIndex("chr/ch00250.itc", 0xA)
    LoadChrToIndex("chr/ch00251.itc", 0xB)
    LoadChrToIndex("chr/ch00350.itc", 0xC)
    LoadChrToIndex("chr/ch00351.itc", 0xD)
    LoadChrToIndex("chr/ch02950.itc", 0xE)
    LoadChrToIndex("chr/ch02951.itc", 0xF)
    LoadChrToIndex("chr/ch03150.itc", 0x10)
    LoadChrToIndex("chr/ch03151.itc", 0x11)
    LoadChrToIndex("chr/ch03250.itc", 0x12)
    LoadChrToIndex("chr/ch03251.itc", 0x13)
    LoadChrToIndex("monster/ch85150.itc", 0x14)
    LoadChrToIndex("monster/ch85151.itc", 0x15)
    LoadChrToIndex("monster/ch85153.itc", 0x16)
    LoadChrToIndex("monster/ch85152.itc", 0x17)
    LoadEffect(0x0, "event/ev17060.eff")
    LoadEffect(0x1, "event/ev17061.eff")
    LoadEffect(0x2, "battle/btgun00.eff")
    LoadEffect(0x3, "event/ev606_00.eff")
    LoadEffect(0x4, "battle\\ms00001.eff")
    SoundLoad(828)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x101, 0x6)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x8)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xA)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xE)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x10)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x12)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x101, -900, 0, -4000, 0)
    SetChrPos(0x102, 100, 0, -5300, 0)
    SetChrPos(0x103, -1400, 0, -5700, 0)
    SetChrPos(0x104, 400, 0, -6900, 0)
    SetChrPos(0x109, -1100, 0, -7300, 0)
    SetChrPos(0x105, -2900, 0, -6200, 0)
    SetChrPos(0x106, -2500, 0, -7200, 0)
    SetChrPos(0x10A, 25500, 0, -3000, 270)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4300, 0, -9500, 270)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x16)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -7500, 0, -6600, 105)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    SetChrFlags(0x2C, 0x8000)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x2C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 25100, 0, -4300, 270)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_B5C2():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5C2)

    def lambda_B5CF():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5CF)

    def lambda_B5DC():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B5DC)

    def lambda_B5E9():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B5E9)

    def lambda_B5F6():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B5F6)

    def lambda_B603():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B603)

    def lambda_B610():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B610)
    OP_68(-1900, 1300, -7000, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    OP_F0(0x0, 0x1)
    PlayEffect(0x1, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(828, 2, 80, 0)
    SetCameraDistance(14000, 3000)
    Sound(985, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_B716():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B716)
    Sleep(300)

    def lambda_B72A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B72A)
    Sleep(300)

    def lambda_B73E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_B73E)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    def lambda_B7C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B7C5)

    def lambda_B7D2():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B7D2)
    Sleep(50)

    def lambda_B7E2():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B7E2)
    Sleep(50)

    def lambda_B7F2():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B7F2)
    Sleep(50)

    def lambda_B802():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B802)
    Sleep(50)

    def lambda_B812():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_B812)
    Sleep(50)

    def lambda_B822():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B822)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#5P#00010FDamn\x01",
            "How come such a city! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FWell, no way … ….\x01",
            "Does the uncle let it go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FSounds like that … ….\x01",
            "Absolutely not allowed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FBut as a possibility\x01",
            "That seems most likely.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#12P#10408FApparently this \"bell\" also\x01",
            "It seems to be related, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B9A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B9A7)

    def lambda_B9B4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B9B4)

    ChrTalk(
        0x103,
        "#11P#00201FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10707FMore coming!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-1900, 1300, -6700, 3000)
    MoveCamera(40, 25, 0, 3000)
    SetCameraDistance(17500, 3000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x28, 5300, 0, -3000, 225)
    SetChrPos(0x29, 5300, 0, -8000, 270)
    SetChrPos(0x2A, -7300, 0, -7400, 90)
    SetChrPos(0x2B, -6000, 0, -2400, 135)
    SetChrPos(0x2C, -1500, 0, -12000, 0)
    SetChrChipByIndex(0x28, 0x14)
    SetChrSubChip(0x28, 0x0)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x14)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x28, 0, 0, 75)
    BeginChrThread(0x29, 0, 0, 75)
    BeginChrThread(0x2A, 0, 0, 75)
    BeginChrThread(0x2B, 0, 0, 75)
    BeginChrThread(0x2C, 0, 0, 75)
    SetChrChipByIndex(0x101, 0x6)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x8)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xA)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xE)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x10)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x12)
    SetChrSubChip(0x106, 0x0)

    def lambda_BBFA():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BBFA)

    def lambda_BC07():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC07)

    def lambda_BC14():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BC14)

    def lambda_BC21():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC21)

    def lambda_BC2E():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BC2E)

    def lambda_BC3B():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BC3B)

    def lambda_BC48():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BC48)
    Sound(985, 0, 100, 0)
    BeginChrThread(0x2A, 3, 0, 80)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 78)
    Sleep(300)
    BeginChrThread(0x2C, 3, 0, 82)
    Sleep(300)
    Sound(985, 0, 50, 0)
    BeginChrThread(0x29, 3, 0, 79)
    Sleep(300)
    BeginChrThread(0x2B, 3, 0, 81)
    WaitChrThread(0x2B, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#00011FCrap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00311FTch. This is bad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10110FDamn\x01",
            "I have to break through somehow!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 1200)
    BeginChrThread(0x2A, 1, 0, 94)
    BeginChrThread(0x28, 3, 0, 87)
    Sound(951, 0, 80, 0)
    Sleep(200)
    BeginChrThread(0x2B, 1, 0, 95)
    BeginChrThread(0x29, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2C, 1, 0, 96)
    Sleep(600)
    Sound(987, 0, 100, 0)
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrChipByIndex(0x28, 0x14)
    SetChrSubChip(0x28, 0x0)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BD6D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BD6D)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x28, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x28, 0x3)
    Sleep(50)
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BDE8():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_BDE8)
    Sound(567, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x29, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x29, 0x3)
    EndChrThread(0x2A, 0x0)
    EndChrThread(0x2A, 0x1)
    SetChrChipByIndex(0x2A, 0x14)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2A, 0x20)
    EndChrThread(0x2B, 0x0)
    EndChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 0x14)
    SetChrSubChip(0x2B, 0x0)
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2B, 0x20)
    EndChrThread(0x2C, 0x0)
    EndChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 0x14)
    SetChrSubChip(0x2C, 0x0)
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x20)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BEDB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEDB)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF00():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BF00)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF28():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF28)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF4D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BF4D)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BF75)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BF9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BF9A)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BFBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BFBF)
    Sleep(1000)

    def lambda_BFCF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BFCF)

    def lambda_BFDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_BFDC)

    def lambda_BFE9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_BFE9)

    def lambda_BFF6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_BFF6)

    def lambda_C003():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_C003)
    OP_68(14800, 1000, -3800, 2000)
    MoveCamera(45, 17, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_C045():
        OP_96(0xFE, 0x3AFC, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C045)

    def lambda_C05F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_C05F)
    Sleep(200)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)

    def lambda_C07B():
        OP_96(0xFE, 0x38A4, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C07B)

    def lambda_C095():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C095)
    WaitChrThread(0x1F, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    WaitChrThread(0x10A, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#6P#NDirector!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00102F#6P#NAnd Dudley!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1F,
        "Hmph. You finally showed up\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x10A,
        (
            "#3465V#30WThe story is back!\x01",
            "Come with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD89)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#00002F#6P#NRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00302F#6P#NYou got it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 1000, 0, -4500, 90)
    SetChrPos(0x102, 1000, 0, -4500, 90)
    SetChrPos(0x103, 1000, 0, -6000, 90)
    SetChrPos(0x104, 1000, 0, -6000, 90)
    SetChrPos(0x109, 1000, 0, -6000, 90)
    SetChrPos(0x105, 1000, 0, -4500, 90)
    SetChrPos(0x106, 1000, 0, -4500, 90)
    SetChrPos(0x2A, -300, 0, -7400, 90)
    SetChrPos(0x2B, -1500, 0, -2400, 90)
    SetChrPos(0x2C, -1000, 0, -12000, 90)
    OP_68(9300, 1000, -4800, 2000)
    MoveCamera(41, 15, 0, 2000)
    SetCameraDistance(14500, 2000)
    SetChrChipByIndex(0x10A, 0x5)
    SetChrSubChip(0x10A, 0x0)
    BeginChrThread(0x10A, 0, 0, 88)
    Sleep(100)
    BeginChrThread(0x1F, 0, 0, 89)
    BeginChrThread(0x38, 1, 0, 90)
    BeginChrThread(0x38, 2, 0, 83)
    BeginChrThread(0x28, 0, 0, 86)
    BeginChrThread(0x28, 1, 0, 92)
    Sleep(100)
    BeginChrThread(0x29, 0, 0, 86)
    BeginChrThread(0x29, 1, 0, 93)
    Sleep(100)
    BeginChrThread(0x2A, 0, 0, 86)
    BeginChrThread(0x2A, 1, 0, 92)
    Sleep(100)
    BeginChrThread(0x2B, 0, 0, 86)
    BeginChrThread(0x2B, 1, 0, 93)
    Sleep(100)
    BeginChrThread(0x2C, 0, 0, 86)
    BeginChrThread(0x2C, 1, 0, 93)
    Sleep(1500)
    MoveCamera(46, 20, 5, 12000)
    SetCameraDistance(14000, 12000)
    BeginChrThread(0x103, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x106, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 85)
    WaitChrThread(0x104, 3)
    EndChrThread(0x10A, 0x0)
    EndChrThread(0x28, 0x0)
    BeginChrThread(0x28, 1, 0, 92)
    EndChrThread(0x2A, 0x0)
    BeginChrThread(0x2A, 1, 0, 92)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)
    OP_93(0x10A, 0x5A, 0x1F4)

    def lambda_C43E():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C43E)
    Sleep(300)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 1, 0, 93)
    EndChrThread(0x2B, 0x0)
    BeginChrThread(0x2B, 1, 0, 93)
    EndChrThread(0x2C, 0x0)
    BeginChrThread(0x2C, 1, 0, 93)
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x5A, 0x1F4)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_C498():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C498)
    Sleep(500)
    EndChrThread(0x38, 0x2)
    StopSound(828, 2000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x106, 0xFF)
    EndChrThread(0x10A, 0xFF)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "City area where pale moya comes out\x01",
            "Run through complicated routes ……\x02\x03",
            "From one corner of old town\x01",
            "I reached the Geo Front D section.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("m0302", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_84_B161 end

    def Function_85_C598(): pass

    label("Function_85_C598")


    def lambda_C59D():
        OP_95(0xFE, 12000, 0, -6200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C59D)
    WaitChrThread(0xFE, 1)

    def lambda_C5BB():
        OP_95(0xFE, 26000, 0, -6200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C5BB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_C598 end

    def Function_86_C5D5(): pass

    label("Function_86_C5D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C6C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C6BC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4B(0xFE, 0x1)
    OP_4B(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C624():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C624)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 1300, 1500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x2710, 0x0)
    Sleep(900)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Sleep(600)
    OP_4C(0xFE, 0x1)
    BeginChrThread(0xFE, 3, 0, 91)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_C6BC")

    Sleep(300)
    Jump("Function_86_C5D5")

    label("loc_C6C4")

    Return()

    # Function_86_C5D5 end

    def Function_87_C6C5(): pass

    label("Function_87_C6C5")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_C6F6():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C6F6)
    Sleep(1000)
    Return()

    # Function_87_C6C5 end

    def Function_88_C70E(): pass

    label("Function_88_C70E")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_C75C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C7DD")
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_C75C")

    label("loc_C7DD")

    Return()

    # Function_88_C70E end

    def Function_89_C7DE(): pass

    label("Function_89_C7DE")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(987, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_C82C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8E4")
    SetChrSubChip(0x1F, 0x5)
    Sleep(150)
    SetChrSubChip(0x1F, 0x6)
    Sleep(100)
    SetChrSubChip(0x1F, 0x7)
    Sleep(100)
    SetChrSubChip(0x1F, 0x4)
    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x1F, 0x3)
    Sleep(70)
    SetChrSubChip(0x1F, 0x2)
    Sleep(70)
    SetChrSubChip(0x1F, 0x1)
    Sleep(70)
    SetChrSubChip(0x1F, 0x0)
    Sleep(70)
    SetChrSubChip(0x1F, 0x1)
    Sleep(70)
    SetChrSubChip(0x1F, 0x2)
    Sleep(70)
    SetChrSubChip(0x1F, 0x3)
    Sleep(70)
    SetChrSubChip(0x1F, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    Sound(987, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Jump("loc_C82C")

    label("loc_C8E4")

    Return()

    # Function_89_C7DE end

    def Function_90_C8E5(): pass

    label("Function_90_C8E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8FE")
    Sound(501, 0, 100, 0)
    Sleep(1500)
    Jump("Function_90_C8E5")

    label("loc_C8FE")

    Return()

    # Function_90_C8E5 end

    def Function_91_C8FF(): pass

    label("Function_91_C8FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C930")
    SetChrChipByIndex(0xFE, 0x15)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1000, 0x0, 0x5)
    Jump("Function_91_C8FF")

    label("loc_C930")

    Return()

    # Function_91_C8FF end

    def Function_92_C931(): pass

    label("Function_92_C931")

    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 3, 0, 91)
    OP_99(0xFE, 0x10A, 0x1388, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Return()

    # Function_92_C931 end

    def Function_93_C978(): pass

    label("Function_93_C978")

    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 3, 0, 91)
    OP_99(0xFE, 0x1F, 0x1388, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 75)
    Return()

    # Function_93_C978 end

    def Function_94_C9BF(): pass

    label("Function_94_C9BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA13")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x2EE, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_94_C9BF")

    label("loc_CA13")

    Return()

    # Function_94_C9BF end

    def Function_95_CA14(): pass

    label("Function_95_CA14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA68")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_95_CA14")

    label("loc_CA68")

    Return()

    # Function_95_CA14 end

    def Function_96_CA69(): pass

    label("Function_96_CA69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CABD")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 91)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Jump("Function_96_CA69")

    label("loc_CABD")

    Return()

    # Function_96_CA69 end

    def Function_97_CABE(): pass

    label("Function_97_CABE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch85150.itc", 0x1E)
    LoadChrToIndex("monster/ch85151.itc", 0x1F)
    LoadChrToIndex("monster/ch85153.itc", 0x20)
    LoadEffect(0x0, "event/ev17061.eff")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x28, -6800, 0, -600, 90)
    SetChrPos(0x29, -8600, 0, 4700, 270)
    SetChrPos(0x2A, 9900, 0, 700, 0)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    OP_52(0x28, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    OP_52(0x29, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x28, 3, 0, 98)
    BeginChrThread(0x29, 3, 0, 99)
    BeginChrThread(0x2A, 3, 0, 100)
    OP_68(0, 1100, 4000, 0)
    MoveCamera(53, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    OP_71(0x16, 0x208, 0x2BC, 0x0, 0x0)
    MoveCamera(31, 21, 0, 11000)
    SetCameraDistance(29000, 11000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(371, 0, 70, 0)
    Sleep(500)
    Fade(500)
    StopSound(828, 2000, 40)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "bell_add", 0x0, 0x1)
    OP_0D()
    StopEffect(0x6, 0x2)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1770)
    OP_11(0x7B, 0xB4, 0xD5, 0x26, 0x82, 0x1770)
    Sleep(2000)
    StopEffect(0x7, 0x2)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_97_CABE end

    def Function_98_CCE9(): pass

    label("Function_98_CCE9")

    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x28, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_CD17():
        OP_95(0xFE, -3200, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_CD17)
    WaitChrThread(0x28, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0x28, 0x20)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x28, 0xB4, 0x1F4)
    BeginChrThread(0x28, 0, 0, 75)
    Sleep(2500)
    Sound(985, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x28, 0x0)
    PlayEffect(0x0, 0x1, 0x28, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x28, 0x20)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_CDD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_CDD1)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_98_CCE9 end

    def Function_99_CDE5(): pass

    label("Function_99_CDE5")

    BeginChrThread(0x29, 0, 0, 75)
    Sleep(5000)
    EndChrThread(0x29, 0x0)
    Sound(985, 0, 50, 0)
    PlayEffect(0x0, 0x2, 0x29, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x29, 0x20)
    SetChrSubChip(0x29, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_CE55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_CE55)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_99_CDE5 end

    def Function_100_CE69(): pass

    label("Function_100_CE69")

    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2A, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_CE97():
        OP_95(0xFE, 9900, 0, 7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_CE97)
    WaitChrThread(0x2A, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0x2A, 0x20)
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x2A, 0, 0, 75)
    Sleep(3000)
    EndChrThread(0x2A, 0x0)
    Sound(985, 0, 50, 0)
    PlayEffect(0x0, 0x3, 0x2A, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x2A, 0x20)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_CF47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_CF47)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_100_CE69 end

    def Function_101_CF5B(): pass

    label("Function_101_CF5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("chr/ch46600.itc", 0x1F)
    OP_68(-13800, 1900, 8170, 0)
    MoveCamera(323, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8940, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x40, 0x80)
    SetChrChipByIndex(0x40, 0x1E)
    SetChrSubChip(0x40, 0x0)
    SetChrPos(0x40, -15530, 0, 9880, 90)
    ClearChrFlags(0x3F, 0x80)
    SetChrChipByIndex(0x3F, 0x1F)
    SetChrSubChip(0x3F, 0x0)
    SetChrPos(0x3F, -14080, 0, 9690, 270)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x3F,
        (
            "#12P#12400FHey, you called a guy ……\x01",
            "Always doing whatever you want always.\x02\x03",
            "This crossbell is\x01",
            "What kind of place is it?\x01",
            "It is not unknown, either.\x02\x03",
            "#12406FA little about your own position\x01",
            "I would like you to be saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13902FHuh, I wonder if I worried.\x02\x03",
            "#13904FHowever, before it gets stuck\x01",
            "I really want to see this town.\x02\x03",
            "Thanks to this\x01",
            "The reason why he is called a magical capital\x01",
            "I feel I understood something.\x02\x03",
            "#13908F…… something \"He\"\x01",
            "It seems to move under the water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400F……HM.\x01",
            "It seems there was harvest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13900FThanks to Hu, Muller\x01",
            "There was also a fun encounter.\x02\x03",
            "#13905F…… Oh, that's right.\x01",
            "How about the setup?\x02\x03",
            "#13904FBecause it's about you,\x01",
            "You can also do it well while I am away\x01",
            "I guess it might have been advanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400FOh, I have already contacted you.\x02\x03",
            "#12406FBecause of you, on schedule\x01",
            "A slight delay has come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13904FHurry, let's hurry.\x02\x03",
            "#13900FBeautiful ladies\x01",
            "It is not something to make you wait.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Searching for performers】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x76, 0x1, 0x4)
    OP_29(0x76, 0x1, 0x5)
    OP_29(0x76, 0x4, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 6)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_101_CF5B end

    def Function_102_D424(): pass

    label("Function_102_D424")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(975)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x2E)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    OP_49()
    SetChrPos(0x2E, 28000, 0, -3910, 270)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xC, 0x2F)
    OP_78(0xD, 0x30)
    OP_78(0xE, 0x31)
    OP_49()
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    OP_74(0xD, 0x1E)
    OP_74(0xE, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    OP_71(0xD, 0x79, 0xB4, 0x1, 0x20)
    OP_71(0xE, 0x79, 0xB4, 0x1, 0x20)
    SetChrFlags(0x2F, 0x8000)
    SetChrFlags(0x30, 0x8000)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x2F, 4040, 0, -21980, 0)
    SetChrPos(0x30, -22270, -380, -4230, 90)
    SetChrPos(0x31, -19750, 0, 20850, 135)
    OP_D5(0x2F, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(16840, 1900, -3910, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(8180, 1900, -4370, 2000)
    Sound(487, 0, 100, 0)

    def lambda_D60B():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D60B)
    WaitChrThread(0x2E, 1)
    OP_71(0xF, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0xF)
    Sound(975, 2, 100, 0)
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x1)
    Sleep(200)
    Fade(500)
    OP_68(4140, 1520, -17770, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27440, 0)
    Sound(459, 0, 100, 0)
    Sound(492, 0, 100, 0)

    def lambda_D69D():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_D69D)
    OP_71(0xC, 0x5B, 0x78, 0x0, 0x0)
    OP_68(-17750, 1520, -3100, 4000)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x30)
    OP_9F(0x1, -22270, -380, -4230)
    OP_9F(0x1, -15910, 0, -4019)
    OP_9F(0x2, 0x30, 5000, 0x6)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x0)
    MoveCamera(60, 33, 0, 2000)
    Sleep(100)
    OP_68(-11170, 1520, 9140, 3000)

    def lambda_D72C():
        OP_9B(0x1, 0xFE, 0x0, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_D72C)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x31, 1)
    OP_71(0xE, 0x5B, 0x78, 0x0, 0x0)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(9190, 1900, -2740, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)

    NpcTalk(
        0x2E,
        "Sykes",
        "#5PAh, it's a habit of Zako!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2E,
        "Yuri",
        "#5PResign, please shake it!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2E,
        "Reggie",
        "#5PA little cool!\x02",
    )

    CloseMessageWindow()
    Sound(493, 0, 100, 0)
    OP_71(0xF, 0xB5, 0xF0, 0x1, 0x20)
    OP_9B(0x1, 0x2E, 0x0, 0xFFFFF830, 0x1388, 0x0)
    Sleep(200)
    OP_68(11190, 1900, 12940, 3000)
    MoveCamera(61, 33, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(20320, 3000)
    Sound(486, 0, 100, 0)
    OP_9F(0x0, 0x2E)
    OP_9F(0x1, 14290, 0, -3910)
    OP_9F(0x1, 10690, 0, -310)
    OP_9F(0x1, 10290, 0, 2350)
    OP_9F(0x2, 0x2E, 11000, 0x6)

    def lambda_D895():
        OP_96(0x2E, 0x2F26, 0x0, 0x88B8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D895)
    Sleep(1500)
    StopSound(975, 1000, 100)
    Sleep(1000)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_102_D424 end

    def Function_103_D8C4(): pass

    label("Function_103_D8C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_68(4270, -700, 10240, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D923")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D962")

    label("loc_D923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D945")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_D962")

    label("loc_D945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D962")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_D962")

    OP_68(4310, -700, 10200, 3000)
    MoveCamera(39, 20, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(50260, 3000)
    Sound(835, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(9660, 1900, -4450, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12460, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DAAC")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x104, 15940, 0, -2710, 270)

    def lambda_DA3E():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DA3E)

    def lambda_DA58():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA58)
    Sleep(100)

    def lambda_DA75():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA75)
    Sleep(50)

    def lambda_DA92():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA92)
    Jump("loc_DC4F")

    label("loc_DAAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DB80")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x109, 15940, 0, -2710, 270)

    def lambda_DB12():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DB12)

    def lambda_DB2C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB2C)
    Sleep(100)

    def lambda_DB49():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB49)
    Sleep(50)

    def lambda_DB66():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DB66)
    Jump("loc_DC4F")

    label("loc_DB80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DC4F")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x105, 15940, 0, -2710, 270)

    def lambda_DBE6():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DBE6)

    def lambda_DC00():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC00)
    Sleep(100)

    def lambda_DC1D():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC1D)
    Sleep(50)

    def lambda_DC3A():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DC3A)

    label("loc_DC4F")

    OP_68(9660, 1900, -4450, 3000)
    MoveCamera(47, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        "Is this the central square?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "As expected it is only a main street\x01",
            "It's quite lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, Shin said that\x01",
            "The Times department store is also a staple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FShould I head right away?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PHmm, well\x01",
            "I will leave it to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PAnyway, I am like this\x01",
            "Just by being with Elie's sister\x01",
            "I'm happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, already\x01",
            "I understood that well enough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00109FThanks, Shin.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DE7B")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302FWell, anyway.\x01",
            "Why do not you turn around properly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1A")

    label("loc_DE7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DED1")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FWell anyhow, preferably\x01",
            "Let's turn around variously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1A")

    label("loc_DED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DF1A")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FWell anyway.\x01",
            "Let's go round variously as appropriate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1A")

    StopSound(835, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_1B(0x0, 0x0, 0x6E)
    OP_1B(0x2, 0x0, 0x6F)
    OP_1B(0x3, 0x0, 0x70)
    OP_1B(0x4, 0x0, 0x71)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x154, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11440, 0, -3410, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_103_D8C4 end

    def Function_104_DF69(): pass

    label("Function_104_DF69")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2150, 1900, -5340, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12200, 0)
    SetChrPos(0x101, -1290, 0, -4460, 0)
    SetChrPos(0x102, -2420, 0, -4740, 0)
    SetChrPos(0x104, -1390, 0, -5860, 0)
    SetChrPos(0x103, -220, 0, -4800, 0)
    SetChrPos(0x105, -20, 0, -6070, 0)
    SetChrPos(0x109, -2650, 0, -6050, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "Hey, Lloyd.\x01",
            "What hurried you so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI'm chasing a person now.\x01",
            "It's a place though ….\x02\x03",
            "#00001FMade here by Rhinefault\x01",
            "Did not a black truck pass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "A black truck … …?\x02\x03",
            "Oh, that reminds me a while ago\x01",
            "I feel like I got such a car.\x02\x03",
            "To be sure, To the east side of the street\x01",
            "I feel I'm missing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FEast Street ……?\x02\x03",
            "Head towards the Empire\x01",
            "Is not it Nishi Dori?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Yes, I also saw it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm … … apparently the destination\x01",
            "It seems that it was for the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FTransport car made by Rheinfault\x01",
            "Empire driving … …\x02\x03",
            "#00200FIf it were to escape, it would be towards the Empire\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, quite easy to do\x01",
            "It seems like you do not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAnyway, thank you.\x01",
            "It was saved, Franz.\x02\x03",
            "#00001F… … It seems better to hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYeah, if you chase\x01",
            "People who used power guided vehicles\x01",
            "It might be nice.\x02\x03",
            "#10101FHurry up to the tangram gate\x01",
            "Let's go over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I do not quite understand it,\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I pray for a good fight!\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x1)
    SetScenarioFlags(0x19B, 7)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1290, 0, -4460, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_104_DF69 end

    def Function_105_E4A5(): pass

    label("Function_105_E4A5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB4D")
    Fade(500)
    OP_68(-19610, -6700, -24820, 0)
    MoveCamera(9, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10990, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E5A7")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x104, -18650, -8200, -21550, 225)

    def lambda_E54D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E54D)

    def lambda_E562():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E562)
    Sleep(100)

    def lambda_E57A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E57A)
    Sleep(50)

    def lambda_E592():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E592)
    Jump("loc_E6FA")

    label("loc_E5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E653")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x109, -18650, -8200, -21550, 225)

    def lambda_E5F9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E5F9)

    def lambda_E60E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E60E)
    Sleep(100)

    def lambda_E626():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E626)
    Sleep(50)

    def lambda_E63E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E63E)
    Jump("loc_E6FA")

    label("loc_E653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E6FA")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x105, -18650, -8200, -21550, 225)

    def lambda_E6A5():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E6A5)

    def lambda_E6BA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E6BA)
    Sleep(100)

    def lambda_E6D2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6D2)
    Sleep(50)

    def lambda_E6EA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E6EA)

    label("loc_E6FA")

    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PWhat, that doggy dog … …!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 3, 0, 106)
    OP_68(-23520, -6700, -24320, 3000)
    MoveCamera(51, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13660, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E7C0")

    def lambda_E790():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E790)
    Sleep(50)

    def lambda_E7A0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7A0)
    Sleep(50)

    def lambda_E7B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E7B0)
    Sleep(300)
    Jump("loc_E837")

    label("loc_E7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E7FE")

    def lambda_E7CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7CE)
    Sleep(50)

    def lambda_E7DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7DE)
    Sleep(50)

    def lambda_E7EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E7EE)
    Sleep(300)
    Jump("loc_E837")

    label("loc_E7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E837")

    def lambda_E80C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E80C)
    Sleep(50)

    def lambda_E81C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E81C)
    Sleep(50)

    def lambda_E82C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E82C)
    Sleep(300)

    label("loc_E837")

    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FZeit … in such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, outside air\x01",
            "I wonder if I wanted to suck it.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-21260, -6700, -23460, 3000)
    OP_9B(0x1, 0x1A2, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sound(812, 0, 100, 0)
    OP_6F(0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00105FShin … … what's wrong?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E94F")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00309FHaha, well then\x01",
            "Do not you fear Zeit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA2C")

    label("loc_E94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E9E3")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FHaha, apparently\x01",
            "It seems that Zeit is scared.\x02\x03",
            "#10104F(Because I was not good at the beginning\x01",
            "I understand your feelings. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA2C")

    label("loc_E9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EA2C")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304FGhost, apparently\x01",
            "You can see that Zeit is scared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA2C")


    ChrTalk(
        0x1A2,
        "What is it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Boku, scary things\x01",
            "It is because it is not.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1A2, 0x3)
    Sleep(1000)
    OP_93(0x1A2, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Come on, you guys.\x01",
            "This is good, so I will go to the next place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that's OK.\x02\x03",
            "#00012F(But I'm totally bear to see it, but\x01",
            "It is the guts looked up. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    SetScenarioFlags(0x1C5, 5)
    OP_29(0x73, 0x1, 0xB)
    Jump("loc_EBB8")

    label("loc_EB4D")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "Hey ….\x01",
            "I will return to the square as it is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, that's OK.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EBB8")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    EventEnd(0x4)
    Return()

    # Function_105_E4A5 end

    def Function_106_EBD0(): pass

    label("Function_106_EBD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC00")

    def lambda_EBE0():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EBE0)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_106_EBD0")

    label("loc_EC00")

    Return()

    # Function_106_EBD0 end

    def Function_107_EC01(): pass

    label("Function_107_EC01")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F02A")
    OP_68(90, 4400, 25340, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16660, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_ECB3")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_ED52")

    label("loc_ECB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ED05")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_ED52")

    label("loc_ED05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ED52")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_ED52")

    OP_68(180, 4350, 26590, 3000)
    MoveCamera(359, 11, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(21260, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(10, 400, 21490, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(15710, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000FWell, to the department store\x01",
            "I arrived ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EE9C")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FStill others, a kid\x01",
            "Where is the place to take me?\x02\x03",
            "#00303FOnce inside,\x01",
            "The time you are guiding outside\x01",
            "It seems to be gone, but … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF0")

    label("loc_EE9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EF51")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10105FStill others, Take Shin\x01",
            "Is not there a place you want to visit?\x02\x03",
            "#10103FOnce inside,\x01",
            "The time you are guiding outside\x01",
            "It seems that it will be gone ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF0")

    label("loc_EF51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EFF0")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FStill others, with Singh\x01",
            "Is there a place you want to go to?\x02\x03",
            "Once inside,\x01",
            "The time you are guiding outside\x01",
            "It seems to be gone, but.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF0")


    ChrTalk(
        0x1A2,
        (
            "#6PWhat are you going to do?\x01",
            "I will leave it to you all.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 108)
    Jump("loc_F315")

    label("loc_F02A")

    OP_68(10, 400, 21490, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15710, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F0AA")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F149")

    label("loc_F0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F0FC")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F149")

    label("loc_F0FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F149")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F149")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F1EA")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FIs it going to enter a department store soon?\x02\x03",
            "#00303FOnce inside,\x01",
            "The time you are guiding outside\x01",
            "It seems to be gone, but … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F310")

    label("loc_F1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F286")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FDo you go to department stores soon?\x02\x03",
            "#10103FOnce inside,\x01",
            "The time you are guiding outside\x01",
            "It seems that it will be gone ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F310")

    label("loc_F286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F310")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FIt is time to enter a department store?\x02\x03",
            "Once inside,\x01",
            "The time you are guiding outside\x01",
            "It seems to be gone, but.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F310")

    Call(0, 108)
    EventEnd(0x5)

    label("loc_F315")

    Return()

    # Function_107_EC01 end

    def Function_108_F316(): pass

    label("Function_108_F316")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Enter the department store\x01",                # 0
            "I still guide other places\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F38A"),
        (1, "loc_F3DB"),
        (SWITCH_DEFAULT, "loc_F45B"),
    )


    label("loc_F38A")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FI see.\x01",
            "I think that we were able to guide you all the way\x01",
            "Shall we go inside?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 109)
    Jump("loc_F45B")

    label("loc_F3DB")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FThat's right, I still want to show you around.\x01",
            "There may be places.\x02\x03",
            "#00000FLet's put it in the back.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 6)
    Jump("loc_F45B")

    label("loc_F45B")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -180, 0, 15990, 180)
    EventEnd(0x5)
    Return()

    # Function_108_F316 end

    def Function_109_F473(): pass

    label("Function_109_F473")

    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("chr/ch02900.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)

    ChrTalk(
        0x1A2,
        "#6POkay, I have decided!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHuhu, that is it.\x01",
            "Shall we go in?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13670, 1900, 7350, 0)
    MoveCamera(22, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F5A3")
    SetChrChipByIndex(0x36, 0x1F)
    SetChrChipByIndex(0x37, 0x20)
    SetChrSubChip(0x36, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x36, -16070, 0, 6000, 45)
    SetChrPos(0x37, -16550, 0, 7310, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x104, 980, 800, 25780, 0)
    Jump("loc_F6CE")

    label("loc_F5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F63B")
    SetChrChipByIndex(0x35, 0x1E)
    SetChrChipByIndex(0x37, 0x20)
    SetChrSubChip(0x35, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x35, 0x8000)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x35, -16550, 0, 7310, 45)
    SetChrPos(0x37, -16070, 0, 6000, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x109, 980, 800, 25780, 0)
    Jump("loc_F6CE")

    label("loc_F63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F6CE")
    SetChrChipByIndex(0x35, 0x1E)
    SetChrChipByIndex(0x36, 0x1F)
    SetChrSubChip(0x35, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x35, 0x8000)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x35, -16550, 0, 7310, 45)
    SetChrPos(0x36, -16070, 0, 6000, 45)
    SetChrPos(0x1A2, -350, 800, 24290, 0)
    SetChrPos(0x102, 500, 800, 24290, 0)
    SetChrPos(0x101, -1000, 800, 25780, 0)
    SetChrPos(0x105, 980, 800, 25780, 0)

    label("loc_F6CE")

    OP_0D()
    Sound(100, 0, 40, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F79F")

    def lambda_F6FB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6FB)
    Sleep(100)

    def lambda_F713():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F713)
    Sleep(500)

    def lambda_F72B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F72B)
    Sleep(200)

    def lambda_F73F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F73F)

    def lambda_F750():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F750)

    def lambda_F765():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F765)
    Sleep(1000)

    def lambda_F77D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F77D)

    def lambda_F78E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F78E)
    Jump("loc_F8FE")

    label("loc_F79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F851")

    def lambda_F7AD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F7AD)
    Sleep(100)

    def lambda_F7C5():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F7C5)
    Sleep(500)

    def lambda_F7DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F7DD)
    Sleep(200)

    def lambda_F7F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F7F1)

    def lambda_F802():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F802)

    def lambda_F817():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F817)
    Sleep(1000)

    def lambda_F82F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F82F)

    def lambda_F840():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F840)
    Jump("loc_F8FE")

    label("loc_F851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F8FE")

    def lambda_F85F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F85F)
    Sleep(100)

    def lambda_F877():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F877)
    Sleep(500)

    def lambda_F88F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F88F)
    Sleep(200)

    def lambda_F8A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F8A3)

    def lambda_F8B4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F8B4)

    def lambda_F8C9():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8C9)
    Sleep(1000)

    def lambda_F8E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F8E1)

    def lambda_F8F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F8F2)

    label("loc_F8FE")

    WaitChrThread(0x102, 1)
    Sound(100, 0, 40, 0)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FAF8")

    ChrTalk(
        0x36,
        (
            "#10100FYeah, apparently\x01",
            "It seems that you entered the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        "#10303F…………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x37, 500)
    Sleep(300)

    ChrTalk(
        0x36,
        "#11P#10105FWhat's wrong, Wa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10301FOh, while alarming behind you,\x01",
            "I felt something I felt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10105FSigns …\x01",
            "Was that the black moon people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10303FOh, of course\x01",
            "I suppose it will be … …\x02\x03",
            "#10300FWell, just concrete things\x01",
            "I have no idea.\x02\x03",
            "Tentatively, we\x01",
            "Let's join a department store after a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10103FWell, yeah …. OK.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF54")

    label("loc_FAF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FD65")

    ChrTalk(
        0x37,
        (
            "#10300FHmm, apparently\x01",
            "You seem to have gone into the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303F…………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x37, 0x35, 500)
    Sleep(300)

    ChrTalk(
        0x37,
        "#11P#10305FWhat's wrong, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FOh, when I am wary of behind\x01",
            "I feel like I feel something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FHuh, you too ……\x01",
            "I also felt somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FOh, probably the people of the black moon\x01",
            "I guess watching it … …\x02\x03",
            "#00301FSomehow, everything\x01",
            "It feels like it is not only that.\x02\x03",
            "#00306FWell, the most specific thing is\x01",
            "I do not know anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FHuh, I am the same view.\x02\x03",
            "#10300FAnyway, now it is still\x01",
            "It looks like it only seems to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303FOh, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF54")

    label("loc_FD65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FF54")

    ChrTalk(
        0x36,
        (
            "#10100FYeah, apparently\x01",
            "It seems that you entered the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303F…………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x35, 500)
    Sleep(300)

    ChrTalk(
        0x36,
        "#11P#10105FWhat's wrong, Randy-senpai?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FOh, when I am wary of behind\x01",
            "I feel like I feel something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10101FSigns …\x01",
            "Is that the black moon people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FOh, naturally it too\x01",
            "I suppose … …\x02\x03",
            "#00306FHowever, honesty\x01",
            "I do not have any concrete details.\x02\x03",
            "#00300FTentatively, we also\x01",
            "Let's join the department store after a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10101FWell, okay … ok.\x02",
    )

    CloseMessageWindow()

    label("loc_FF54")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0170", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_109_F473 end

    def Function_110_FF6C(): pass

    label("Function_110_FF6C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10043")

    ChrTalk(
        0x1A2,
        (
            "Um, department stores\x01",
            "Is it on that side … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, no way,\x01",
            "This station is towards the station ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Then, come back quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1007F")

    label("loc_10043")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no need to get out of the station.\x01",
            "Let's return to the square.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1007F")

    SetChrPos(0x0, 3740, 0, -19810, 0)
    EventEnd(0x4)
    Return()

    # Function_110_FF6C end

    def Function_111_10093(): pass

    label("Function_111_10093")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10157")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FHey, Lloyd … ….\x01",
            "Going to this place is an administrative district.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FThat's right, let's turn back.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Department store, was not this?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_1017C")

    label("loc_10157")


    ChrTalk(
        0x101,
        "#00000FThis is the direction of the administrative district.\x02",
    )

    CloseMessageWindow()

    label("loc_1017C")

    SetChrPos(0x0, 13290, 0, 26680, 180)
    EventEnd(0x4)
    Return()

    # Function_111_10093 end

    def Function_112_10190(): pass

    label("Function_112_10190")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10291")
    TurnDirection(0x1A2, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "This arcade is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Perhaps,\x01",
            "Do you put it in the back street from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, do not you know well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FTentatively,\x01",
            "There is no business here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "(Hmm, Tsao said that\x01",
            "Here is the trace of Rubathe … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_102B2")

    label("loc_10291")


    ChrTalk(
        0x101,
        "#00000FThere is no use in the back street.\x02",
    )

    CloseMessageWindow()

    label("loc_102B2")

    SetChrPos(0x0, -14110, -10, 14420, 135)
    EventEnd(0x4)
    Return()

    # Function_112_10190 end

    def Function_113_102C6(): pass

    label("Function_113_102C6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe future is Nishi Dori.\x02\x03",
            "#00003FNot much from department store\x01",
            "It can not go away,\x01",
            "Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_113_102C6 end

    SaveToFile()

Try(main)
