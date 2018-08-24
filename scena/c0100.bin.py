from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Gina",                   # 1
        "Old Man Conte",          # 2
        "Abel",                   # 3
        "Mimi",                   # 4
        "Pluna",                  # 5
        "Lenalee",                # 6
        "Haas",                   # 7
        "Sally",                  # 8
        "Koppe",                  # 9
        "Zeit",                   # 10
        "KeA",                    # 11
        "Patrol Officer Kate",    # 12
        "Patrol Officer Frantz",  # 13
        "CGF Member",             # 14
        "Policeman",              # 15
        "State Guard Soldier",    # 16
        "Citizen",                # 17
        "Citizen",                # 18
        "車",                     # 19
        "Ryｹ",                   # 20
        "Henri",                  # 21
        "KeA",                    # 22
        "White Falcon",           # 23
        "Chief Sergei",           # 24
        "State Guard Soldier",    # 25
        "市民１",                 # 26
        "市民２",                 # 27
        "市民３",                 # 28
        "市民４",                 # 29
        "市民５",                 # 30
        "市民６",                 # 31
        "市民７",                 # 32
        "イベント用モンスター",   # 33
        "イベント用モンスター",   # 34
        "イベント用モンスター",   # 35
        "イベント用モンスター",   # 36
        "イベント用モンスター",   # 37
        "車",                     # 38
        "暴走車",                 # 39
        "パトカー1",              # 40
        "パトカー2",              # 41
        "パトカー3",              # 42
        "車",                     # 43
        "車",                     # 44
        "車",                     # 45
        "Randy",                  # 46
        "Noｱl",                  # 47
        "Wazy",                   # 48
        "SE制御",                 # 49
        "Policeman",              # 50
        "Policeman",              # 51
        "Policeman",              # 52
        "Policeman",              # 53
        "Policeman",              # 54
        "Balloon Vendor",         # 55
        "Mueller",                # 56
        "Olivier",                # 57
        "bc0100",                 # 58
        "bc0100",                 # 59
        "Central Square",         # 60
        "West Street",            # 61
        "Governmental District",  # 62
        "Residential Street",     # 63
        "Entertainment District", # 64
        "East Street",            # 65
        "Downtown",               # 66
        "Waterfront Area",        # 67
        "IBC",                    # 68
        "Station Street",         # 69
        "Back Street",            # 70
        "St. Ursula Byroad",      # 71
        "East Crossbell Highway", # 72
        "West Crossbell HIghway", # 73
        "Mainz Mountain Road",    # 74
        "Orchis Tower",           # 75
    ))

    ATBonus("ATBonus_B6C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_B7C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_10743", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_C5C", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0100", "Sepith_10743", 60, 30, 10, 0,
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

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "Central Square")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "West Street")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "Governmental District")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "Residential Street")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "East Street")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "Downtown")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "IBC")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "Station Street")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "Back Street")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_10_2BD6",        # 0A, 10
        "Function_11_2BE6",        # 0B, 11
        "Function_12_3C9D",        # 0C, 12
        "Function_13_3CDA",        # 0D, 13
        "Function_14_3D21",        # 0E, 14
        "Function_15_3D6B",        # 0F, 15
        "Function_16_4525",        # 10, 16
        "Function_17_469C",        # 11, 17
        "Function_18_4701",        # 12, 18
        "Function_19_471D",        # 13, 19
        "Function_20_487B",        # 14, 20
        "Function_21_48C4",        # 15, 21
        "Function_22_48D7",        # 16, 22
        "Function_23_4B07",        # 17, 23
        "Function_24_52EF",        # 18, 24
        "Function_25_5393",        # 19, 25
        "Function_26_5A6E",        # 1A, 26
        "Function_27_5ABB",        # 1B, 27
        "Function_28_5B24",        # 1C, 28
        "Function_29_5D0A",        # 1D, 29
        "Function_30_5D1D",        # 1E, 30
        "Function_31_78E2",        # 1F, 31
        "Function_32_7912",        # 20, 32
        "Function_33_7951",        # 21, 33
        "Function_34_7B83",        # 22, 34
        "Function_35_7CD3",        # 23, 35
        "Function_36_8340",        # 24, 36
        "Function_37_8394",        # 25, 37
        "Function_38_83AD",        # 26, 38
        "Function_39_869F",        # 27, 39
        "Function_40_86E6",        # 28, 40
        "Function_41_86F9",        # 29, 41
        "Function_42_8C4C",        # 2A, 42
        "Function_43_8CA1",        # 2B, 43
        "Function_44_8CF6",        # 2C, 44
        "Function_45_8D4B",        # 2D, 45
        "Function_46_8DA0",        # 2E, 46
        "Function_47_8DD0",        # 2F, 47
        "Function_48_8FA8",        # 30, 48
        "Function_49_9380",        # 31, 49
        "Function_50_9C6B",        # 32, 50
        "Function_51_9CE5",        # 33, 51
        "Function_52_A1E5",        # 34, 52
        "Function_53_A21C",        # 35, 53
        "Function_54_A24D",        # 36, 54
        "Function_55_A27E",        # 37, 55
        "Function_56_A2AF",        # 38, 56
        "Function_57_A2E0",        # 39, 57
        "Function_58_A311",        # 3A, 58
        "Function_59_A342",        # 3B, 59
        "Function_60_A529",        # 3C, 60
        "Function_61_A571",        # 3D, 61
        "Function_62_A590",        # 3E, 62
        "Function_63_A5AF",        # 3F, 63
        "Function_64_A5E3",        # 40, 64
        "Function_65_A624",        # 41, 65
        "Function_66_A665",        # 42, 66
        "Function_67_A6AE",        # 43, 67
        "Function_68_B00D",        # 44, 68
        "Function_69_B04A",        # 45, 69
        "Function_70_B087",        # 46, 70
        "Function_71_B0C4",        # 47, 71
        "Function_72_B101",        # 48, 72
        "Function_73_B13E",        # 49, 73
        "Function_74_B17B",        # 4A, 74
        "Function_75_B1B8",        # 4B, 75
        "Function_76_B1D7",        # 4C, 76
        "Function_77_B1F4",        # 4D, 77
        "Function_78_B26E",        # 4E, 78
        "Function_79_B2C1",        # 4F, 79
        "Function_80_B314",        # 50, 80
        "Function_81_B367",        # 51, 81
        "Function_82_B3BA",        # 52, 82
        "Function_83_B40D",        # 53, 83
        "Function_84_B427",        # 54, 84
        "Function_85_C8AB",        # 55, 85
        "Function_86_C8E8",        # 56, 86
        "Function_87_C9D8",        # 57, 87
        "Function_88_CA21",        # 58, 88
        "Function_89_CAF1",        # 59, 89
        "Function_90_CBF8",        # 5A, 90
        "Function_91_CC12",        # 5B, 91
        "Function_92_CC44",        # 5C, 92
        "Function_93_CC8B",        # 5D, 93
        "Function_94_CCD2",        # 5E, 94
        "Function_95_CD27",        # 5F, 95
        "Function_96_CD7C",        # 60, 96
        "Function_97_CDD1",        # 61, 97
        "Function_98_CFFC",        # 62, 98
        "Function_99_D0F8",        # 63, 99
        "Function_100_D17C",       # 64, 100
        "Function_101_D26E",       # 65, 101
        "Function_102_D79F",       # 66, 102
        "Function_103_DC34",       # 67, 103
        "Function_104_E2ED",       # 68, 104
        "Function_105_E838",       # 69, 105
        "Function_106_EF85",       # 6A, 106
        "Function_107_EFB6",       # 6B, 107
        "Function_108_F6B2",       # 6C, 108
        "Function_109_F832",       # 6D, 109
        "Function_110_102CD",      # 6E, 110
        "Function_111_103FC",      # 6F, 111
        "Function_112_10528",      # 70, 112
        "Function_113_1068A",      # 71, 113
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
            "Two days after the\x01",
            "dramatic arrest at\x01",
            "Altair Lodge...\x02",
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

    def lambda_2BA5():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2BA5)
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

    def Function_10_2BD6(): pass

    label("Function_10_2BD6")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 50, 0)
    Return()

    # Function_10_2BD6 end

    def Function_11_2BE6(): pass

    label("Function_11_2BE6")

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

    def lambda_2D37():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D37)
    Sleep(100)

    def lambda_2D54():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D54)
    Sleep(100)

    def lambda_2D71():
        OP_97(0x1A5, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_2D71)
    Sleep(100)

    def lambda_2D8E():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D8E)
    Sleep(100)

    def lambda_2DAB():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DAB)
    Sound(835, 2, 60, 0)
    OP_68(0, 1100, -7700, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    NpcTalk(
        0x1B,
        "Boy's Voice",
        "Heeey, KeA!\x02",
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

    def lambda_2ED8():

        label("loc_2ED8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2ED8")

    QueueWorkItem2(0x101, 2, lambda_2ED8)

    def lambda_2EEA():

        label("loc_2EEA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EEA")

    QueueWorkItem2(0x102, 2, lambda_2EEA)

    def lambda_2EFC():

        label("loc_2EFC")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EFC")

    QueueWorkItem2(0x1A5, 2, lambda_2EFC)

    def lambda_2F0E():

        label("loc_2F0E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F0E")

    QueueWorkItem2(0x109, 2, lambda_2F0E)

    def lambda_2F20():

        label("loc_2F20")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F20")

    QueueWorkItem2(0x105, 2, lambda_2F20)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x1A5, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    ChrTalk(
        0x1A5,
        "#12P#01110FAh, Ryｹ and Henri!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PYou're late! We were\x01",
            "waitin' for ya by the\x01",
            "bakery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PClass is about to start!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#12P#01109FEhehe, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHey Ryｹ and Henri.\x01",
            "You're looking good as\x01",
            "ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha. Thanks for being\x01",
            "such good friends with\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#5PAh, long time no see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PHehe, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PAnd KeA said the Support\x01",
            "Section's starting up\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, fortunately.\x02\x03",
            "#00000FWe've powered up quite a\x01",
            "bit, so look forward to\x01",
            "it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PHehe. You sure can talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWell, I guess you guys\x01",
            "are almost as good as\x01",
            "the bracers nowadays...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PRyｹ, don't be so rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F*chuckle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWe're pretty popular\x01",
            "with kids too, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3280():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3280)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#5PHuh? Who's that lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PI don't recognize her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PAnd Randy and Tio aren't\x01",
            "here either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FThey had business to\x01",
            "attend to and aren't\x01",
            "back yet.\x02\x03",
            "#00100FThis is Noｱl and Wazy.\x01",
            "They're new Support\x01",
            "Section members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FHaha, nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PYeah, same here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5P...But, huh? Is that a\x01",
            "guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PYou have kind of a girly\x01",
            "face...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PRyｹ!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHehe. I wonder.\x02\x03",
            "#10302FIf you think I'm a\x01",
            "woman, then maybe I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Wazy. Don't tease the\x01",
            "kids.\x02\x03",
            "#00000FBut you three should get\x01",
            "moving, right?\x02",
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

    def lambda_3530():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_3530)
    Sleep(50)

    def lambda_3540():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3540)
    Sleep(150)

    ChrTalk(
        0x1A5,
        (
            "#6P#01105FOh, that's right!\x02\x03",
            "#01109FWell, see you guys\x01",
            "later!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A5, 500)

    def lambda_359A():

        label("loc_359A")

        TurnDirection(0xFE, 0x1A5, 500)
        Yield()
        Jump("loc_359A")

    QueueWorkItem2(0x101, 2, lambda_359A)

    ChrTalk(
        0x101,
        "#00009FYeah, do your best KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FWatch out for cars, ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#6P#01110FYup!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PAlright, then let's stop\x01",
            "by Momo's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PYeah, let's hurry!\x02",
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
            "#11P#10109FHaha... They sure are\x01",
            "lively kinds, huh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#11P#10300FDo they live on West\x01",
            "Street?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3744():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3744)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, the other one is\x01",
            "from Residential Street\x01",
            "though.\x02\x03",
            "#00004FWell then, we should\x01",
            "probably get to work\x01",
            "ourselves.\x02\x03",
            "#00000FFor starters, let's stop\x01",
            "by the Orbal Store over\x01",
            "there and Police HQ...\x02\x03",
            "And if possible, let's\x01",
            "take a look around the\x01",
            "city as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10100FI see. Patrolling,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FHaha, it's not that big a\x01",
            "deal, but...\x02\x03",
            "#00100FBecause we can get unexpected\x01",
            "information, patrolling is\x01",
            "important, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FChief will contact us via\x01",
            "ENIGMA in a bit.\x02\x03",
            "Until then, let's head to\x01",
            "various places of\x01",
            "interest within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10102FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10304FHaha. Shall we go, then?\x02",
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
            "The Crossbell City map\x01",
            "is now available.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pushing START in the city opens\x01",
            "it. (Pushing START again displays\x01",
            "the Crossbell State map.)\x02",
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
            "Also, the map can be used\x01",
            "to quickly move to any\x01",
            "area within the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please select the area to\x01",
            "which you wish to go from the\x01",
            "list on left side of the map.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, depending on the\x01",
            "situation, there will be times\x01",
            "when the map is unusable.\x02",
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

    # Function_11_2BE6 end

    def Function_12_3C9D(): pass

    label("Function_12_3C9D")


    def lambda_3CA2():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA2)
    WaitChrThread(0xFE, 1)

    def lambda_3CC0():
        OP_95(0xFE, -3400, 0, -5700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3C9D end

    def Function_13_3CDA(): pass

    label("Function_13_3CDA")

    Sleep(50)

    def lambda_3CE2():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CE2)
    WaitChrThread(0xFE, 1)

    def lambda_3D00():
        OP_95(0xFE, -2800, 0, -4800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D00)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_13_3CDA end

    def Function_14_3D21(): pass

    label("Function_14_3D21")

    OP_92(0xFE, 0xFFFFE318, 0xFFFFF31C, 0x1F4)

    def lambda_3D33():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D33)
    WaitChrThread(0xFE, 1)

    def lambda_3D51():
        OP_95(0xFE, -17400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D51)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3D21 end

    def Function_15_3D6B(): pass

    label("Function_15_3D6B")

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

    def lambda_3E9E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E9E)
    Sleep(50)

    def lambda_3EAE():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EAE)
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
        "#11P#00005FOh, is that chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FIt's about time he\x01",
            "called.\x02",
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
            "#00000FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey, nice work.\x02\x03",
            "As we discussed this morning,\x01",
            "it's time for you to come to\x01",
            "the police academy.\x02\x03",
            "You know the place, right?\x02",
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
            "#00000FIt's past the gate\x01",
            "halfway down West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh yeah, I left the gate\x01",
            "open for you.\x02\x03",
            "By the way... You've\x01",
            "finished patrolling the\x01",
            "city, right?\x02\x03",
            "Honestly, how do things\x01",
            "look?\x02",
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
            "#00011FAh...\x02",
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
            "#00003F...Right.\x02\x03",
            "#00001FFor various reasons, I\x01",
            "get the feeling\x01",
            "something will happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You should sharpen that\x01",
            "intuition of yours.\x01",
            "You'll need it.\x02\x03",
            "Well then, I'll be\x01",
            "waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FUnderstood.\x02",
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
        (
            "#6P#00100FSo it was chief after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSounds like he said\x01",
            "something worrisome.\x02",
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
            "#11P#00006FYeah. I think he's also\x01",
            "feeling the change in\x01",
            "the city.\x02\x03",
            "#00001FWe should report to him\x01",
            "about Heiyue and Lechter\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FWell, are we going to\x01",
            "the police academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah. Let's leave via\x01",
            "the west entrance.\x02",
        )
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
            "West Crossbell Highway\x01",
            "can now be selected from\x01",
            "the Crossbell City Map.\x07\x00\x02",
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

    # Function_15_3D6B end

    def Function_16_4525(): pass

    label("Function_16_4525")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_462A")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xA, 0xFF)
    SetChrPos(0xA, -6880, 0, 810, 0)

    def lambda_45F6():

        label("loc_45F6")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_45F6")

    QueueWorkItem2(0xA, 2, lambda_45F6)
    SetChrPos(0xB, -6300, 0, -170, 0)
    EndChrThread(0xB, 0xFF)

    def lambda_461D():

        label("loc_461D")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_461D")

    QueueWorkItem2(0xB, 2, lambda_461D)

    label("loc_462A")

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

    # Function_16_4525 end

    def Function_17_469C(): pass

    label("Function_17_469C")

    SetChrPos(0xFE, -35510, -2590, -4520, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23860, -640, -4420)
    OP_9F(0x1, -14350, 750, -1880)
    OP_9F(0x1, -11380, 0, 7200)
    OP_9F(0x1, -14250, 0, 13970)
    OP_9F(0x1, -28100, 0, 29400)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_17_469C end

    def Function_18_4701(): pass

    label("Function_18_4701")

    Sound(458, 0, 100, 0)
    Sound(468, 2, 100, 0)
    Sleep(5000)
    Sound(494, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_4701 end

    def Function_19_471D(): pass

    label("Function_19_471D")

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

    # Function_19_471D end

    def Function_20_487B(): pass

    label("Function_20_487B")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_20_487B end

    def Function_21_48C4(): pass

    label("Function_21_48C4")

    Sleep(2300)
    Sound(458, 0, 70, 0)
    Sleep(4300)
    Sound(494, 0, 70, 0)
    Return()

    # Function_21_48C4 end

    def Function_22_48D7(): pass

    label("Function_22_48D7")

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

    # Function_22_48D7 end

    def Function_23_4B07(): pass

    label("Function_23_4B07")

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
            "#30WYear 1204 of the Septian Calendar─ early autumn.\x02\x03",
            "The West Zemuria Trade Conference, proposed by\x01",
            "newly elected Crossbell City Mayor and IBC\x01",
            "President Dieter Crois, began.\x02\x03",
            "From the Erebonian Empire to the west, in addition\x01",
            "to Blood and Iron Chancellor Giliath Osborne,\x01",
            "Prince Olivert, known as a man of the world...\x02\x03",
            "From the Republic of Calvard to the east,\x01",
            "President Samuel Rocksmith, supported by the\x01",
            "populist faction...\x02\x03",
            "From the Principality of Remiferia located to the\x01",
            "northeast, Archduke Albert, who governs despite\x01",
            "his young age...\x02\x03",
            "From Liberl Kingdom to the southwest, Crown\x01",
            "Princess Klaudia, the queen's representative...\x02\x03",
            "At that moment, the VIPs of each state were\x01",
            "gathering in Crossbell.\x02",
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

    # Function_23_4B07 end

    def Function_24_52EF(): pass

    label("Function_24_52EF")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5327"),
        (1, "loc_532F"),
        (2, "loc_5337"),
        (3, "loc_533F"),
        (4, "loc_5347"),
        (5, "loc_534F"),
        (6, "loc_5357"),
        (SWITCH_DEFAULT, "loc_535F"),
    )


    label("loc_5327")

    Sleep(100)
    Jump("loc_5367")

    label("loc_532F")

    Sleep(200)
    Jump("loc_5367")

    label("loc_5337")

    Sleep(300)
    Jump("loc_5367")

    label("loc_533F")

    Sleep(400)
    Jump("loc_5367")

    label("loc_5347")

    Sleep(500)
    Jump("loc_5367")

    label("loc_534F")

    Sleep(600)
    Jump("loc_5367")

    label("loc_5357")

    Sleep(700)
    Jump("loc_5367")

    label("loc_535F")

    Sleep(800)
    Jump("loc_5367")

    label("loc_5367")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5392")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_5367")

    label("loc_5392")

    Return()

    # Function_24_52EF end

    def Function_25_5393(): pass

    label("Function_25_5393")

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

    # Function_25_5393 end

    def Function_26_5A6E(): pass

    label("Function_26_5A6E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, 0, -4000)
    OP_9F(0x1, 11500, 0, 1000)
    OP_9F(0x1, 12000, 0, 30000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5AAA():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5AAA)
    Return()

    # Function_26_5A6E end

    def Function_27_5ABB(): pass

    label("Function_27_5ABB")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3700, 0, -20000)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 10580, 0, 4180)
    OP_9F(0x1, 12000, 0, 10000)
    OP_9F(0x1, 12000, 0, 15000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5B13():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B13)
    Return()

    # Function_27_5ABB end

    def Function_28_5B24(): pass

    label("Function_28_5B24")

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

    def lambda_5C9B():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5C9B)
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

    # Function_28_5B24 end

    def Function_29_5D0A(): pass

    label("Function_29_5D0A")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(3600)
    Sound(494, 0, 50, 0)
    Return()

    # Function_29_5D0A end

    def Function_30_5D1D(): pass

    label("Function_30_5D1D")

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

    def lambda_5FCB():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5FCB)
    Sleep(50)

    def lambda_5FDB():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5FDB)
    Sleep(50)

    def lambda_5FEB():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5FEB)
    Sleep(50)

    def lambda_5FFB():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5FFB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005FWhat's that?\x02",
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

    def lambda_6132():

        label("loc_6132")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_6132")

    QueueWorkItem2(0x1E, 2, lambda_6132)

    def lambda_6144():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFE9BC, 0xFFFF9A70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6144)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 3, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6186():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6186)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_61AE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_61AE)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_61D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61D6)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_61FE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_61FE)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6226():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6226)
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
        "#00011F#6P#NW-What!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10111F#6P#NA-A white hawk?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#12PNo. It looks like a\x01",
            "falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey now, what're ya\x01",
            "doin' in the middle of a\x01",
            "city like this?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1E, 0x3)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x0)
    OP_68(-27800, -6900, -26700, 3000)
    MoveCamera(37, 19, 0, 3000)

    def lambda_6368():
        OP_9E(0xFE, 0xFFFF97B4, 0xFFFF9A70, 0x493E0, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6368)
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

    def lambda_6509():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6509)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_6552():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6552)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_659B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_659B)
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

    def lambda_6699():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE2B4, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6699)
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
            "Scree.\x02\x03",
            "Scree, scree, scree.\x02",
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
            "#5P#00001FI-It can't be... Does it\x01",
            "have business with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PIt seems like it's the\x01",
            "same as when Zeit\x01",
            "speaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PHmm, if PeTiote was here,\x01",
            "we could understand what\x01",
            "he's saying, but...\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    ClearChrFlags(0x1D, 0x80)

    def lambda_68DD():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA628, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_68DD)

    def lambda_68F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_68F7)
    WaitChrThread(0x1D, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x1D,
        "#01105F#5PHuh? What's the matter?\x02",
    )

    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)

    def lambda_6971():
        OP_96(0xFE, 0xFFFF90AC, 0xFFFFDFF8, 0xFFFF9750, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6971)
    Sleep(300)

    def lambda_698E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_698E)
    Sleep(100)

    def lambda_699E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_699E)
    Sleep(100)

    def lambda_69AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_69AE)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x87, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FWah! A white bird!\x02\x03",
            "#01109FHis sharp beak is so\x01",
            "cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#08009FScree㈱\x02\x03",
            "#08000FScree, scree, scree㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#6P#01103FHmm, hmm.\x02\x03",
            "#01102FI see, so that's what it\x01",
            "was.\x02",
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
            "#5P#00012F(KeA... I guess she\x01",
            "understands him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(A-Amazing...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    def lambda_6B6D():

        label("loc_6B6D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6B6D")

    QueueWorkItem2(0x1D, 2, lambda_6B6D)

    ChrTalk(
        0x1D,
        (
            "#6P#01100FUm, this little guy says\x01",
            "his name is "Sieg".\x02\x03",
            "He says he has a message\x01",
            "for you guys, and he\x01",
            "wants you to take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FO-Oh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1E, 500)

    ChrTalk(
        0x104,
        (
            "#00305F#5PAh, he really does have\x01",
            "a note attached to his\x01",
            "leg.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C61():
        OP_95(0xFE, -27600, -8200, -26600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C61)
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    def lambda_6C85():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6C85)
    WaitChrThread(0x101, 1)
    EndChrThread(0x1D, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the memo that\x01",
            "was fastened to the\x01",
            "white falcon's leg.\x07\x00\x02",
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
            "Dear Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "Pardon my rudeness for\x01",
            "contacting you, but your fame\x01",
            "has reached my ears.\x02\x03",
            "If you have time, would you\x01",
            "be willing to consult with me\x01",
            "privately?\x02\x03",
            "I will be waiting for you\x01",
            "this evening at the meeting\x01",
            "terrace of Crossbell Airport.\x02\x03",
            "P.S.: In case you cannot make\x01",
            "it, it is all right if you do\x01",
            "not reply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F#5P...............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00101F#11PT-This is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106F#5PWith the contents being what they\x01",
            "are and with an unknown sender...\x01",
            "This is just too suspicious!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302F#11PHowever, the handwriting\x01",
            "is beautiful and the\x01",
            "tone is so polite...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301F#5PMost importantly, the\x01",
            "white falcon crest that's\x01",
            "stamped on this memo is...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1E,
        (
            "#08000F#12PScree.\x02\x03",
            "Scree, scree, scree.\x02",
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

    def lambda_709F():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE4A8, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_709F)
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

    def lambda_7125():

        label("loc_7125")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_7125")

    QueueWorkItem2(0x1E, 2, lambda_7125)
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

    def lambda_735A():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFEF98, 0xFFFF64EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_735A)
    Sleep(300)

    def lambda_7377():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7377)
    Sleep(100)

    def lambda_7387():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7387)
    Sleep(100)

    def lambda_7397():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7397)
    Sleep(100)

    def lambda_73A7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_73A7)
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
            "#11P#00011FUmm... KeA, what did he\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    ChrTalk(
        0x1D,
        (
            "#6P#01111FHmm. "Whether to come or\x01",
            "not is up to you", he\x01",
            "says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FIs that so...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_752A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_752A)
    Sleep(50)

    def lambda_753A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_753A)
    Sleep(50)

    def lambda_754A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_754A)
    Sleep(50)

    def lambda_755A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_755A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#11PS-So? What will you do?\x02\x03",
            "#00101FI think it's impossible,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PYeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PBut, this white falcon\x01",
            "crest... It looked like\x01",
            "that bird just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PAhaha. Now I'm looking\x01",
            "forward to this even\x01",
            "more.\x02",
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
            "#6P#00003F─The sender took the trouble to\x01",
            "invite us. We should accept.\x02\x03",
            "#00000FThere's still time until evening,\x01",
            "so let's finish whatever else we\x01",
            "have to do before then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5PI-I'm kind of nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PWell, I don't think we\x01",
            "need to go in uniform,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHaha. Well, once we're through with\x01",
            "everything, let's head to Crossbell\x01",
            "Airport past the South entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FI don't really get it\x01",
            "but, good luck everyone!\x02",
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

    # Function_30_5D1D end

    def Function_31_78E2(): pass

    label("Function_31_78E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7911")

    def lambda_78F2():
        OP_9E(0xFE, 0xFFFF99A8, 0xFFFF9A70, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_78F2)
    WaitChrThread(0x1E, 1)
    Jump("Function_31_78E2")

    label("loc_7911")

    Return()

    # Function_31_78E2 end

    def Function_32_7912(): pass

    label("Function_32_7912")


    def lambda_7917():
        OP_9E(0xFE, 0xFFFF9494, 0xFFFF93CC, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7917)
    WaitChrThread(0x1E, 1)

    def lambda_7936():
        OP_9E(0xFE, 0xFFFF90AC, 0xFFFF93CC, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7936)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_32_7912 end

    def Function_33_7951(): pass

    label("Function_33_7951")

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
            "#1KThe next day, 8:00 AM──\x02",
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

    def lambda_7B09():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7B09)
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

    # Function_33_7951 end

    def Function_34_7B83(): pass

    label("Function_34_7B83")

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

    # Function_34_7B83 end

    def Function_35_7CD3(): pass

    label("Function_35_7CD3")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EB9")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_7E88():

        label("loc_7E88")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7E88")

    QueueWorkItem2(0xA, 2, lambda_7E88)

    def lambda_7E9A():

        label("loc_7E9A")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7E9A")

    QueueWorkItem2(0xB, 2, lambda_7E9A)

    def lambda_7EAC():

        label("loc_7EAC")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_7EAC")

    QueueWorkItem2(0x13, 2, lambda_7EAC)

    label("loc_7EB9")

    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_7EFE():
        OP_9B(0x0, 0x101, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7EFE)
    Sleep(50)

    def lambda_7F16():
        OP_9B(0x0, 0x102, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7F16)
    Sleep(50)

    def lambda_7F2E():
        OP_9B(0x0, 0x103, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7F2E)
    Sleep(50)

    def lambda_7F46():
        OP_9B(0x0, 0x104, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7F46)
    Sleep(50)

    def lambda_7F5E():
        OP_9B(0x0, 0x105, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7F5E)
    Sleep(50)

    def lambda_7F76():
        OP_9B(0x0, 0x109, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F76)
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
        "#00005F#5PThis sound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#5PThey're sirens.\x02",
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
        "#10101F#5PThree ambulances...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PI wonder if they're\x01",
            "carrying derailment\x01",
            "accident victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PWell, considering the\x01",
            "timing, there can't be\x01",
            "any doubt, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...It looks like Cecil\x01",
            "and the others will be\x01",
            "busy.\x02\x03",
            "#00001FLet's hurry to the scene\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#5PYeah.\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8312")
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

    label("loc_8312")

    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 6)
    OP_24(0x3B2)
    EventEnd(0x5)
    Return()

    # Function_35_7CD3 end

    def Function_36_8340(): pass

    label("Function_36_8340")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13000, 500, -2870)
    OP_9F(0x1, -350, 0, -7080)
    OP_9F(0x1, 4300, 0, -18000)
    OP_9F(0x1, 4500, 0, -30000)
    OP_9F(0x1, 4500, 0, -40000)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_36_8340 end

    def Function_37_8394(): pass

    label("Function_37_8394")

    Sound(465, 0, 80, 0)
    Sleep(4000)
    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 80, 0)
    Return()

    # Function_37_8394 end

    def Function_38_83AD(): pass

    label("Function_38_83AD")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8592")
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_8561():

        label("loc_8561")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8561")

    QueueWorkItem2(0xA, 2, lambda_8561)

    def lambda_8573():

        label("loc_8573")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8573")

    QueueWorkItem2(0xB, 2, lambda_8573)

    def lambda_8585():

        label("loc_8585")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8585")

    QueueWorkItem2(0x13, 2, lambda_8585)

    label("loc_8592")

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

    # Function_38_83AD end

    def Function_39_869F(): pass

    label("Function_39_869F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13630, 0, 14510)
    OP_9F(0x1, -11670, 0, 9100)
    OP_9F(0x1, -12500, 0, 4800)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x8)
    Return()

    # Function_39_869F end

    def Function_40_86E6(): pass

    label("Function_40_86E6")

    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 50, 0)
    Return()

    # Function_40_86E6 end

    def Function_41_86F9(): pass

    label("Function_41_86F9")

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
            "#6P#10302FWell then, it was the casino in\x01",
            "Entertainment District and the\x01",
            "two stores in Downtown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah. There could be\x01",
            "clues in other places\x01",
            "too, but...\x02\x03",
            "#00001FFor now, we don't have\x01",
            "time to go outside the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FLuckily, this morning we\x01",
            "didn't receive any new\x01",
            "support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FProbably, due to what\x01",
            "happened yesterday, even\x01",
            "HQ is still in chaos.\x02\x03",
            "#00101FIt appears the CGF\x01",
            "received considerable\x01",
            "damage too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8A64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8A64)

    def lambda_8A71():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8A71)
    Sleep(50)

    def lambda_8A81():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A81)
    Sleep(50)

    def lambda_8A91():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8A91)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00106F...I'm sorry.\x02\x03",
            "#00108FConsidering your position,\x01",
            "we shouldn't think of it as\x01",
            "someone else's problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5P...No. It's our duty as\x01",
            "CGF to be ready for\x01",
            "dangers like this.\x02\x03",
            "#10100FAnd at least for the time\x01",
            "being, I am a Support\x01",
            "Section member, after all.\x02\x03",
            "Let's go... ...To catch\x01",
            "Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11P...Yeah!\x02",
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

    # Function_41_86F9 end

    def Function_42_8C4C(): pass

    label("Function_42_8C4C")


    def lambda_8C51():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C51)

    def lambda_8C6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C6B)
    WaitChrThread(0xFE, 1)

    def lambda_8C80():
        OP_95(0xFE, -27400, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C80)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_42_8C4C end

    def Function_43_8CA1(): pass

    label("Function_43_8CA1")


    def lambda_8CA6():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CA6)

    def lambda_8CC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CC0)
    WaitChrThread(0xFE, 1)

    def lambda_8CD5():
        OP_95(0xFE, -28000, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CD5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_8CA1 end

    def Function_44_8CF6(): pass

    label("Function_44_8CF6")


    def lambda_8CFB():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CFB)

    def lambda_8D15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8D15)
    WaitChrThread(0xFE, 1)

    def lambda_8D2A():
        OP_95(0xFE, -29400, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D2A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_44_8CF6 end

    def Function_45_8D4B(): pass

    label("Function_45_8D4B")


    def lambda_8D50():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D50)

    def lambda_8D6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8D6A)
    WaitChrThread(0xFE, 1)

    def lambda_8D7F():
        OP_95(0xFE, -30000, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D7F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_8D4B end

    def Function_46_8DA0(): pass

    label("Function_46_8DA0")


    def lambda_8DA5():
        OP_95(0xFE, -28700, -8200, -23700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DA5)

    def lambda_8DBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8DBF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_8DA0 end

    def Function_47_8DD0(): pass

    label("Function_47_8DD0")

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

    def lambda_8F71():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8F71)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(457, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8DD0 end

    def Function_48_8FA8(): pass

    label("Function_48_8FA8")

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
            "Just the other day, those wills\x01",
            "knocked this Crossbell to the\x01",
            "depths of fear and despair.\x02\x03",
            "I think you wise citizens may\x01",
            "have realized this...\x02",
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
            "Here and now, I dare to\x01",
            "accuse those powers by\x01",
            "name.\x02\x03",
            "The "Erebonian Imperial\x01",
            "Government"... That is\x01",
            "one of the wicked wills.\x02",
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

    # Function_48_8FA8 end

    def Function_49_9380(): pass

    label("Function_49_9380")

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

    def lambda_947A():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_947A)
    Sleep(50)

    def lambda_9497():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9497)
    Sleep(50)

    def lambda_94B4():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_94B4)
    Sleep(50)

    def lambda_94D1():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_94D1)
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

    def lambda_9564():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9564)
    Sleep(50)

    def lambda_9574():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9574)
    Sleep(50)

    def lambda_9584():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9584)
    Sleep(50)

    def lambda_9594():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9594)
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
        "#00005F#11PKeA?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1D,
        "#6P#01123F#3623V#30W#15A......h......!\x02",
    )

    CloseMessageWindow()
    OP_24(0xE27)
    OP_C9(0x1, 0x80000000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_961C():
        OP_96(0xFE, 0xFFFFA498, 0xFFFFDFF8, 0xFFFF9F84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_961C)
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

    def lambda_96A3():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96A3)

    def lambda_96BC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96BC)

    def lambda_96C9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_96C9)
    OP_6F(0x79)
    SetCameraDistance(12500, 50000)

    ChrTalk(
        0x101,
        "#11P#00011FWhoah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FKeA...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PIt's true that many things\x01",
            "are goin' on, but there's\x01",
            "nothin' to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#01114F#30W...Yeah...\x02",
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
            "#11P#00004F...It's all right, KeA.\x02\x03",
            "#00008FIt's true we don't know what\x01",
            "will happen to Crossbell in\x01",
            "the future, but...\x02\x03",
            "#00002FThat doesn't change the fact\x01",
            "that we'll always be right\x01",
            "by your side, KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "#5P#01105F#30WLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FRight... At least that\x01",
            "much is for certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PWe came right back even\x01",
            "when we went away\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FSo, KeA. Don't worry and\x01",
            "wait for us, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#01121F#40WElie, Tio, Randy...\x02",
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

    def lambda_9A1D():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFF9F84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9A1D)
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
            "#3624V#30WYeah...#800W!\x01",
            "#30WStay safe, everyone!\x02",
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
            "Wazy is no longer a\x01",
            "party member.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BA8")
    Jump("loc_9BAD")

    label("loc_9BA8")

    OP_29(0x8E, 0x4, 0x40)

    label("loc_9BAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BBE")
    Jump("loc_9BC3")

    label("loc_9BBE")

    OP_29(0x8F, 0x4, 0x40)

    label("loc_9BC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BD4")
    Jump("loc_9BD9")

    label("loc_9BD4")

    OP_29(0x90, 0x4, 0x40)

    label("loc_9BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BEA")
    Jump("loc_9BEF")

    label("loc_9BEA")

    OP_29(0x91, 0x4, 0x40)

    label("loc_9BEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9C00")
    Jump("loc_9C05")

    label("loc_9C00")

    OP_29(0x92, 0x4, 0x40)

    label("loc_9C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9C16")
    Jump("loc_9C1B")

    label("loc_9C16")

    OP_29(0x93, 0x4, 0x40)

    label("loc_9C1B")

    SubItemNumber(0x328, 10)
    SubItemNumber(0x340, 1)
    SubItemNumber(0x375, 1)
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

    # Function_49_9380 end

    def Function_50_9C6B(): pass

    label("Function_50_9C6B")

    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9C93():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9C93)

    def lambda_9CAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9CAD)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_9CDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9CDC)
    Return()

    # Function_50_9C6B end

    def Function_51_9CE5(): pass

    label("Function_51_9CE5")

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
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WAs you all already know─\x02\x03",
            "The other day, former Mayor Crois\x01",
            "declared the founding of the Independent\x01",
            "State of Crossbell.\x02\x03",
            "A military organization called the State\x01",
            "Guard was established. I feel some are\x01",
            "growing used to the new order...\x02",
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
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─However, everyone! I\x01",
            "want you to think again!\x02\x03",
            "To consider whether this\x01",
            "situation is one the\x01",
            "citizens have chosen!\x07\x00\x02",
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

    # Function_51_9CE5 end

    def Function_52_A1E5(): pass

    label("Function_52_A1E5")

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

    # Function_52_A1E5 end

    def Function_53_A21C(): pass

    label("Function_53_A21C")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A22C():
        OP_95(0xFE, -2800, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A22C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_53_A21C end

    def Function_54_A24D(): pass

    label("Function_54_A24D")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A25D():
        OP_95(0xFE, -1500, 0, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A25D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_54_A24D end

    def Function_55_A27E(): pass

    label("Function_55_A27E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A28E():
        OP_95(0xFE, -2500, 0, 10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A28E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_55_A27E end

    def Function_56_A2AF(): pass

    label("Function_56_A2AF")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A2BF():
        OP_95(0xFE, 1300, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2BF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_56_A2AF end

    def Function_57_A2E0(): pass

    label("Function_57_A2E0")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A2F0():
        OP_95(0xFE, 2300, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2F0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_57_A2E0 end

    def Function_58_A311(): pass

    label("Function_58_A311")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A321():
        OP_95(0xFE, -2800, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A321)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_58_A311 end

    def Function_59_A342(): pass

    label("Function_59_A342")

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

    # Function_59_A342 end

    def Function_60_A529(): pass

    label("Function_60_A529")

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

    # Function_60_A529 end

    def Function_61_A571(): pass

    label("Function_61_A571")


    def lambda_A576():
        OP_95(0xFE, -1600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A576)
    WaitChrThread(0xB, 1)
    Return()

    # Function_61_A571 end

    def Function_62_A590(): pass

    label("Function_62_A590")


    def lambda_A595():
        OP_95(0xFE, -2900, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A595)
    WaitChrThread(0xF, 1)
    Return()

    # Function_62_A590 end

    def Function_63_A5AF(): pass

    label("Function_63_A5AF")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A5C9():
        OP_95(0xFE, 6300, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A5C9)
    WaitChrThread(0xE, 1)
    Return()

    # Function_63_A5AF end

    def Function_64_A5E3(): pass

    label("Function_64_A5E3")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A60A():
        OP_95(0xFE, -1100, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A60A)
    WaitChrThread(0xC, 1)
    Return()

    # Function_64_A5E3 end

    def Function_65_A624(): pass

    label("Function_65_A624")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A64B():
        OP_95(0xFE, 400, 0, 12100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A64B)
    WaitChrThread(0xD, 1)
    Return()

    # Function_65_A624 end

    def Function_66_A665(): pass

    label("Function_66_A665")

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

    # Function_66_A665 end

    def Function_67_A6AE(): pass

    label("Function_67_A6AE")

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
        "#00013F#12PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PIt's like the Barrier\x01",
            "that was enveloping\x01",
            "Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F#12PIt is probably similar\x01",
            "in nature.\x02\x03",
            "#00201F...And it is likely the\x01",
            "bell's resonance that is\x01",
            "generating this haze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PHey now, what the─\x02",
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

    def lambda_AB55():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AB55)

    def lambda_AB62():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AB62)
    Sleep(50)

    def lambda_AB72():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB72)

    def lambda_AB7F():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_AB7F)
    Sleep(50)

    def lambda_AB8F():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AB8F)

    def lambda_AB9C():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AB9C)
    Sleep(50)

    def lambda_ABAC():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ABAC)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#11P─Careful. We're\x01",
            "surrounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10410F#11PMoreover, these are...\x02",
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

    def lambda_ACD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_ACD7)
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

    def lambda_AD91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_AD91)
    Sleep(300)

    def lambda_ADA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_ADA5)
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
        (
            "#6P#00107FThe ones from the Tower\x01",
            "of Stargaze!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00207FThey are the same magic\x01",
            "golems, but they look\x01",
            "far more dangerous!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00307FAnyway, let's smash 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00007FYeah, let's crush them!\x02",
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

    # Function_67_A6AE end

    def Function_68_B00D(): pass

    label("Function_68_B00D")


    def lambda_B012():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B012)
    WaitChrThread(0xFE, 1)

    def lambda_B030():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B030)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_B00D end

    def Function_69_B04A(): pass

    label("Function_69_B04A")


    def lambda_B04F():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B04F)
    WaitChrThread(0xFE, 1)

    def lambda_B06D():
        OP_96(0xFE, 0x64, 0x0, 0xFFFFEB4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B06D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_B04A end

    def Function_70_B087(): pass

    label("Function_70_B087")


    def lambda_B08C():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B08C)
    WaitChrThread(0xFE, 1)

    def lambda_B0AA():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0AA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_B087 end

    def Function_71_B0C4(): pass

    label("Function_71_B0C4")


    def lambda_B0C9():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0C9)
    WaitChrThread(0xFE, 1)

    def lambda_B0E7():
        OP_96(0xFE, 0x190, 0x0, 0xFFFFE50C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0E7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_B0C4 end

    def Function_72_B101(): pass

    label("Function_72_B101")


    def lambda_B106():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B106)
    WaitChrThread(0xFE, 1)

    def lambda_B124():
        OP_96(0xFE, 0xFFFFF4AC, 0x0, 0xFFFFE7C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B124)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_B101 end

    def Function_73_B13E(): pass

    label("Function_73_B13E")


    def lambda_B143():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B143)
    WaitChrThread(0xFE, 1)

    def lambda_B161():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE3E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B161)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_B13E end

    def Function_74_B17B(): pass

    label("Function_74_B17B")


    def lambda_B180():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B180)
    WaitChrThread(0xFE, 1)

    def lambda_B19E():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFE37C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B19E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_B17B end

    def Function_75_B1B8(): pass

    label("Function_75_B1B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1D6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_75_B1B8")

    label("loc_B1D6")

    Return()

    # Function_75_B1B8 end

    def Function_76_B1D7(): pass

    label("Function_76_B1D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F3")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_76_B1D7")

    label("loc_B1F3")

    Return()

    # Function_76_B1D7 end

    def Function_77_B1F4(): pass

    label("Function_77_B1F4")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_B225():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B225)
    Sleep(1000)
    SetChrFlags(0xFE, 0x20)

    def lambda_B246():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFE764, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B246)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_B1F4 end

    def Function_78_B26E(): pass

    label("Function_78_B26E")

    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B2AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B2AD)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_78_B26E end

    def Function_79_B2C1(): pass

    label("Function_79_B2C1")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B300():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B300)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_79_B2C1 end

    def Function_80_B314(): pass

    label("Function_80_B314")

    PlayEffect(0x0, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B353():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B353)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_80_B314 end

    def Function_81_B367(): pass

    label("Function_81_B367")

    PlayEffect(0x0, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B3A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B3A6)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_81_B367 end

    def Function_82_B3BA(): pass

    label("Function_82_B3BA")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B3F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B3F9)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_82_B3BA end

    def Function_83_B40D(): pass

    label("Function_83_B40D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B426")
    Sound(986, 0, 80, 0)
    Sleep(1000)
    Jump("Function_83_B40D")

    label("loc_B426")

    Return()

    # Function_83_B40D end

    def Function_84_B427(): pass

    label("Function_84_B427")

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

    def lambda_B888():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B888)

    def lambda_B895():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B895)

    def lambda_B8A2():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B8A2)

    def lambda_B8AF():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B8AF)

    def lambda_B8BC():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B8BC)

    def lambda_B8C9():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B8C9)

    def lambda_B8D6():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B8D6)
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

    def lambda_B9DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B9DC)
    Sleep(300)

    def lambda_B9F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B9F0)
    Sleep(300)

    def lambda_BA04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_BA04)
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

    def lambda_BA8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA8B)

    def lambda_BA98():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BA98)
    Sleep(50)

    def lambda_BAA8():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BAA8)
    Sleep(50)

    def lambda_BAB8():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BAB8)
    Sleep(50)

    def lambda_BAC8():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAC8)
    Sleep(50)

    def lambda_BAD8():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_BAD8)
    Sleep(50)

    def lambda_BAE8():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BAE8)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#5P#00010FTch... Why are those\x01",
            "monsters in the city!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FD-Don't tell me... Did\x01",
            ""uncle" and Bell release\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FN-No way... That would\x01",
            "be absolutely\x01",
            "unforgivable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FHowever, that seems the\x01",
            "most plausible\x01",
            "possibility.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#12P#10408FIt seems Bell is\x01",
            "involved with all of\x01",
            "this too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BC96():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BC96)

    def lambda_BCA3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BCA3)

    ChrTalk(
        0x103,
        "#11P#00201FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10707F...More are coming!\x02",
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

    def lambda_BEE7():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEE7)

    def lambda_BEF4():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BEF4)

    def lambda_BF01():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF01)

    def lambda_BF0E():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BF0E)

    def lambda_BF1B():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BF1B)

    def lambda_BF28():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BF28)

    def lambda_BF35():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BF35)
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
        "#11P#00011F...Damn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00311FTch... This is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10110F...We have to break\x01",
            "through somehow!\x02",
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

    def lambda_C05C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C05C)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x28, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x28, 0x3)
    Sleep(50)
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C0D7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C0D7)
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

    def lambda_C1CA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C1CA)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C1EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C1EF)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C217():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C217)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C23C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C23C)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C264():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C264)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C289():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C289)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C2AE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C2AE)
    Sleep(1000)

    def lambda_C2BE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C2BE)

    def lambda_C2CB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C2CB)

    def lambda_C2D8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_C2D8)

    def lambda_C2E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_C2E5)

    def lambda_C2F2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_C2F2)
    OP_68(14800, 1000, -3800, 2000)
    MoveCamera(45, 17, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_C334():
        OP_96(0xFE, 0x3AFC, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C334)

    def lambda_C34E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_C34E)
    Sleep(200)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)

    def lambda_C36A():
        OP_96(0xFE, 0x38A4, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C36A)

    def lambda_C384():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C384)
    WaitChrThread(0x1F, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    WaitChrThread(0x10A, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#6P#NChief!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00102F#6P#NDudley!\x02",
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
        "Heh, you finally came.\x02",
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
            "#3465V#30WWe'll talk later! Follow\x01",
            "us!\x02",
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
        "#00302F#6P#NAye aye sir!\x02",
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

    def lambda_C717():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C717)
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

    def lambda_C771():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C771)
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
            "Afterwards, Lloyd and the others were\x01",
            "guided along a complicated route through\x01",
            "the city, covered in the bluish mist...\x02\x03",
            "And from somewhere in Downtown, they\x01",
            "reached Geofront D-Division.\x07\x00\x02",
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

    # Function_84_B427 end

    def Function_85_C8AB(): pass

    label("Function_85_C8AB")


    def lambda_C8B0():
        OP_95(0xFE, 12000, 0, -6200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8B0)
    WaitChrThread(0xFE, 1)

    def lambda_C8CE():
        OP_95(0xFE, 26000, 0, -6200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8CE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_C8AB end

    def Function_86_C8E8(): pass

    label("Function_86_C8E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C9D7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C9CF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4B(0xFE, 0x1)
    OP_4B(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C937():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C937)
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

    label("loc_C9CF")

    Sleep(300)
    Jump("Function_86_C8E8")

    label("loc_C9D7")

    Return()

    # Function_86_C8E8 end

    def Function_87_C9D8(): pass

    label("Function_87_C9D8")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_CA09():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA09)
    Sleep(1000)
    Return()

    # Function_87_C9D8 end

    def Function_88_CA21(): pass

    label("Function_88_CA21")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_CA6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CAF0")
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
    Jump("loc_CA6F")

    label("loc_CAF0")

    Return()

    # Function_88_CA21 end

    def Function_89_CAF1(): pass

    label("Function_89_CAF1")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(987, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_CB3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBF7")
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
    Jump("loc_CB3F")

    label("loc_CBF7")

    Return()

    # Function_89_CAF1 end

    def Function_90_CBF8(): pass

    label("Function_90_CBF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC11")
    Sound(501, 0, 100, 0)
    Sleep(1500)
    Jump("Function_90_CBF8")

    label("loc_CC11")

    Return()

    # Function_90_CBF8 end

    def Function_91_CC12(): pass

    label("Function_91_CC12")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC43")
    SetChrChipByIndex(0xFE, 0x15)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1000, 0x0, 0x5)
    Jump("Function_91_CC12")

    label("loc_CC43")

    Return()

    # Function_91_CC12 end

    def Function_92_CC44(): pass

    label("Function_92_CC44")

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

    # Function_92_CC44 end

    def Function_93_CC8B(): pass

    label("Function_93_CC8B")

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

    # Function_93_CC8B end

    def Function_94_CCD2(): pass

    label("Function_94_CCD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CD26")
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
    Jump("Function_94_CCD2")

    label("loc_CD26")

    Return()

    # Function_94_CCD2 end

    def Function_95_CD27(): pass

    label("Function_95_CD27")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CD7B")
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
    Jump("Function_95_CD27")

    label("loc_CD7B")

    Return()

    # Function_95_CD27 end

    def Function_96_CD7C(): pass

    label("Function_96_CD7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDD0")
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
    Jump("Function_96_CD7C")

    label("loc_CDD0")

    Return()

    # Function_96_CD7C end

    def Function_97_CDD1(): pass

    label("Function_97_CDD1")

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

    # Function_97_CDD1 end

    def Function_98_CFFC(): pass

    label("Function_98_CFFC")

    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x28, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_D02A():
        OP_95(0xFE, -3200, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_D02A)
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

    def lambda_D0E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_D0E4)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_98_CFFC end

    def Function_99_D0F8(): pass

    label("Function_99_D0F8")

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

    def lambda_D168():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_D168)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_99_D0F8 end

    def Function_100_D17C(): pass

    label("Function_100_D17C")

    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2A, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_D1AA():
        OP_95(0xFE, 9900, 0, 7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D1AA)
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

    def lambda_D25A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_D25A)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_100_D17C end

    def Function_101_D26E(): pass

    label("Function_101_D26E")

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
            "#12P#12400FHonestly, you're unbelievable...\x01",
            "You always, always do whatever\x01",
            "the hell you want.\x02\x03",
            "Even though you obviously have\x01",
            "not a single clue about what\x01",
            "kind of place Crossbell is.\x02\x03",
            "#12406FI wish you'd consider your own\x01",
            "position a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13902FHmph, so I made you worry about me,\x01",
            "yes?\x02\x03",
            "#13904FHowever, I wanted to see this city\x01",
            "before I died, no matter what.\x02\x03",
            "Thanks to that, I feel like a\x01",
            "caught a glimpse of the reason this\x01",
            "place is called the Demon City.\x02\x03",
            "#13908F...It seems "he" is operating\x01",
            "behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400F...Hmm. It seems you\x01",
            "found something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13900FHmph, thanks to you,\x01",
            "Mueller, I also had a fun\x01",
            "encounter.\x02\x03",
            "#13905FBy the way, how did things\x01",
            "go on your end?\x02\x03",
            "#13904FBecause it's you, you\x01",
            "skillfully advanced things\x01",
            "in my absence, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400FYes. Communications are\x01",
            "already taken care of.\x02\x03",
            "#12406FAlthough, thanks to you,\x01",
            "we're a bit behind\x01",
            "schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13904FHmph, let's hurry then.\x02\x03",
            "#13900FAfter all, one must not\x01",
            "keep lovely ladies\x01",
            "waiting.\x02",
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
            "Quest [Search for\x01",
            "Musician]\x07\x00",
            " completed!\x02",
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

    # Function_101_D26E end

    def Function_102_D79F(): pass

    label("Function_102_D79F")

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

    def lambda_D986():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_D986)
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

    def lambda_DA18():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_DA18)
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

    def lambda_DAA7():
        OP_9B(0x1, 0xFE, 0x0, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_DAA7)
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
        (
            "#5PAah, shut up ya small\x01",
            "fry!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2E,
        "Yuri",
        "#5PReggie, shake 'em off!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2E,
        "Reggie",
        "#5PEasy as pie!\x02",
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

    def lambda_DC05():
        OP_96(0x2E, 0x2F26, 0x0, 0x88B8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_DC05)
    Sleep(1500)
    StopSound(975, 1000, 100)
    Sleep(1000)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_102_D79F end

    def Function_103_DC34(): pass

    label("Function_103_DC34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_68(4270, -700, 10240, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DC93")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_DCD2")

    label("loc_DC93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DCB5")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_DCD2")

    label("loc_DCB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DCD2")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_DCD2")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DE1C")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x104, 15940, 0, -2710, 270)

    def lambda_DDAE():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DDAE)

    def lambda_DDC8():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDC8)
    Sleep(100)

    def lambda_DDE5():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDE5)
    Sleep(50)

    def lambda_DE02():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DE02)
    Jump("loc_DFBF")

    label("loc_DE1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DEF0")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x109, 15940, 0, -2710, 270)

    def lambda_DE82():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DE82)

    def lambda_DE9C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE9C)
    Sleep(100)

    def lambda_DEB9():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DEB9)
    Sleep(50)

    def lambda_DED6():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DED6)
    Jump("loc_DFBF")

    label("loc_DEF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DFBF")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x105, 15940, 0, -2710, 270)

    def lambda_DF56():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DF56)

    def lambda_DF70():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF70)
    Sleep(100)

    def lambda_DF8D():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF8D)
    Sleep(50)

    def lambda_DFAA():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFAA)

    label("loc_DFBF")

    OP_68(9660, 1900, -4450, 3000)
    MoveCamera(47, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "This is Central Square,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "As I thought, it's\x01",
            "lively because it's a\x01",
            "major thoroughfare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. Times Department\x01",
            "Store that you mentioned\x01",
            "is right nearby, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FShall we head there\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PHmm. I'll leave that up\x01",
            "to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PAnyway, I'm having fun\x01",
            "just being next to Elie\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWe understand that\x01",
            "plenty well already.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00109FThank you, Shing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E200")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302FWell anyway, let's have\x01",
            "a look around, shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29E")

    label("loc_E200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E24E")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FWell anyway, shall we\x01",
            "have a look around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29E")

    label("loc_E24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E29E")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FWell anyway, let's have\x01",
            "a look around, shall we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E29E")

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

    # Function_103_DC34 end

    def Function_104_E2ED(): pass

    label("Function_104_E2ED")

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
            "Hey, Lloyd. Why are you\x01",
            "in such a rush?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're in the middle of\x01",
            "chasing after a certain\x01",
            "character, but...\x02\x03",
            "#00001FHas a black Reinford\x01",
            "transport passed by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "A black transport...?\x02\x03",
            "Yeah. Now that you mention\x01",
            "it, a car like that did\x01",
            "pass by not long ago.\x02\x03",
            "If I remember correctly,\x01",
            "it went towards East\x01",
            "Street...\x02",
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
            "#00105FEast Street...is it?\x02\x03",
            "It wasn't towards West\x01",
            "Street, in the direction\x01",
            "of the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "No, I saw it too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm... It seems his\x01",
            "destination was the\x01",
            "Republic, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAn imperial driving a\x01",
            "Reinford transport...\x02\x03",
            "#00200FIf we had assumed he\x01",
            "would flee to the\x01",
            "Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man. This guy's gonna\x01",
            "be a pain to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAnyway, thank you. This\x01",
            "really helps us out,\x01",
            "Frantz.\x02\x03",
            "#00001F...We should hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYes, if we're chasing\x01",
            "after him, we should use\x01",
            "our orbal car.\x02\x03",
            "#10101FLet's hurry to Tangram\x01",
            "Gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I don't really get it,\x01",
            "but do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Good luck to you!\x02",
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

    # Function_104_E2ED end

    def Function_105_E838(): pass

    label("Function_105_E838")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEEB")
    Fade(500)
    OP_68(-19610, -6700, -24820, 0)
    MoveCamera(9, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10990, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E93A")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x104, -18650, -8200, -21550, 225)

    def lambda_E8E0():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E8E0)

    def lambda_E8F5():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E8F5)
    Sleep(100)

    def lambda_E90D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E90D)
    Sleep(50)

    def lambda_E925():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E925)
    Jump("loc_EA8D")

    label("loc_E93A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E9E6")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x109, -18650, -8200, -21550, 225)

    def lambda_E98C():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E98C)

    def lambda_E9A1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E9A1)
    Sleep(100)

    def lambda_E9B9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E9B9)
    Sleep(50)

    def lambda_E9D1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E9D1)
    Jump("loc_EA8D")

    label("loc_E9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EA8D")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x105, -18650, -8200, -21550, 225)

    def lambda_EA38():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_EA38)

    def lambda_EA4D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EA4D)
    Sleep(100)

    def lambda_EA65():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA65)
    Sleep(50)

    def lambda_EA7D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EA7D)

    label("loc_EA8D")

    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PW-What's with that huge\x01",
            "dog?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 3, 0, 106)
    OP_68(-23520, -6700, -24320, 3000)
    MoveCamera(51, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13660, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EB4F")

    def lambda_EB1F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB1F)
    Sleep(50)

    def lambda_EB2F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB2F)
    Sleep(50)

    def lambda_EB3F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EB3F)
    Sleep(300)
    Jump("loc_EBC6")

    label("loc_EB4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EB8D")

    def lambda_EB5D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB5D)
    Sleep(50)

    def lambda_EB6D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB6D)
    Sleep(50)

    def lambda_EB7D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EB7D)
    Sleep(300)
    Jump("loc_EBC6")

    label("loc_EB8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EBC6")

    def lambda_EB9B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB9B)
    Sleep(50)

    def lambda_EBAB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EBAB)
    Sleep(50)

    def lambda_EBBB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EBBB)
    Sleep(300)

    label("loc_EBC6")

    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005FZeit... What is he doing\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*. Maybe he\x01",
            "wanted a breath of fresh\x01",
            "air.\x02",
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
        "#6P#00105FShing... What's wrong?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_ECEA")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00309FHah. You're scared of\x01",
            "Zeit, aren't you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDC6")

    label("loc_ECEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ED7C")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FAhaha. He's scared of\x01",
            "Zeit, isn't he.\x02\x03",
            "#10104F(I didn't get along with\x01",
            "him at first either, so\x01",
            "I can relate.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDC6")

    label("loc_ED7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EDC6")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304FHaha, it looks like\x01",
            "you're scared of Zeit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDC6")


    ChrTalk(
        0x1A2,
        (
            "W-What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I-I'm not afraid of\x01",
            "anything, see.\x02",
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
            "Alright guys, I've had\x01",
            "enough of this place.\x01",
            "Let's move on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, got it.\x02\x03",
            "#00012F(Haha. He's obviously\x01",
            "faking, but I admire his\x01",
            "courage.)\x02",
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
    Jump("loc_EF6D")

    label("loc_EEEB")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "H-Hey. I've had enough of\x01",
            "that place. We're heading\x01",
            "back to the square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, got it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EF6D")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    EventEnd(0x4)
    Return()

    # Function_105_E838 end

    def Function_106_EF85(): pass

    label("Function_106_EF85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFB5")

    def lambda_EF95():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EF95)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_106_EF85")

    label("loc_EFB5")

    Return()

    # Function_106_EF85 end

    def Function_107_EFB6(): pass

    label("Function_107_EFB6")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3CE")
    OP_68(90, 4400, 25340, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16660, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F068")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F107")

    label("loc_F068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F0BA")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F107")

    label("loc_F0BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F107")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F107")

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
            "#00000FWell then, we've finally\x01",
            "arrived at the\x01",
            "department store, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F25F")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FAre there any other\x01",
            "places you want to take\x01",
            "him to?\x02\x03",
            "#00303FOnce we're inside, we\x01",
            "won't have time to see\x01",
            "anyplace else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F391")

    label("loc_F25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F2FE")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10105FAre there any other\x01",
            "places you want to take\x01",
            "him to?\x02\x03",
            "#10103FOnce we're inside, we\x01",
            "won't have time to see\x01",
            "any place else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F391")

    label("loc_F2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F391")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FAre there any other\x01",
            "places you want to take\x01",
            "him to?\x02\x03",
            "Once we're inside, we\x01",
            "won't have time to see\x01",
            "any place else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F391")


    ChrTalk(
        0x1A2,
        (
            "#6PSo what'll it be? I'll\x01",
            "leave it to you guys.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 108)
    Jump("loc_F6B1")

    label("loc_F3CE")

    OP_68(10, 400, 21490, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15710, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F44E")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F4ED")

    label("loc_F44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F4A0")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F4ED")

    label("loc_F4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F4ED")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F4ED")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F58E")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FIs it time to enter the\x01",
            "department store?\x02\x03",
            "#00303FOnce we're inside, we\x01",
            "won't have time to see\x01",
            "anyplace else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6AC")

    label("loc_F58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F623")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FIs it time to enter the\x01",
            "department store?\x02\x03",
            "#10103FOnce we're inside, we\x01",
            "won't have time to see\x01",
            "any place else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6AC")

    label("loc_F623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F6AC")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FIs it time to enter the\x01",
            "department store?\x02\x03",
            "Once we're inside, we\x01",
            "won't have time to see\x01",
            "any place else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6AC")

    Call(0, 108)
    EventEnd(0x5)

    label("loc_F6B1")

    Return()

    # Function_107_EFB6 end

    def Function_108_F6B2(): pass

    label("Function_108_F6B2")

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
            "Enter the department store\x01",      # 0
            "Show him other places\x01",           # 1
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
        (0, "loc_F733"),
        (1, "loc_F792"),
        (SWITCH_DEFAULT, "loc_F81A"),
    )


    label("loc_F733")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FHmm. I think we've\x01",
            "showed him enough for\x01",
            "now. Let's head inside.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 109)
    Jump("loc_F81A")

    label("loc_F792")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FHmm. There's still other\x01",
            "places I want to take\x01",
            "him to.\x02\x03",
            "#00000FLet's hold off on going\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 6)
    Jump("loc_F81A")

    label("loc_F81A")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -180, 0, 15990, 180)
    EventEnd(0x5)
    Return()

    # Function_108_F6B2 end

    def Function_109_F832(): pass

    label("Function_109_F832")

    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("chr/ch02900.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)

    ChrTalk(
        0x1A2,
        (
            "#6PAlright, it's decided\x01",
            "then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*. Then, shall we\x01",
            "enter?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13670, 1900, 7350, 0)
    MoveCamera(22, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F963")
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
    Jump("loc_FA8E")

    label("loc_F963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F9FB")
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
    Jump("loc_FA8E")

    label("loc_F9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FA8E")
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

    label("loc_FA8E")

    OP_0D()
    Sound(100, 0, 40, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FB5F")

    def lambda_FABB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FABB)
    Sleep(100)

    def lambda_FAD3():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FAD3)
    Sleep(500)

    def lambda_FAEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FAEB)
    Sleep(200)

    def lambda_FAFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FAFF)

    def lambda_FB10():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FB10)

    def lambda_FB25():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FB25)
    Sleep(1000)

    def lambda_FB3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FB3D)

    def lambda_FB4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FB4E)
    Jump("loc_FCBE")

    label("loc_FB5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC11")

    def lambda_FB6D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB6D)
    Sleep(100)

    def lambda_FB85():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FB85)
    Sleep(500)

    def lambda_FB9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB9D)
    Sleep(200)

    def lambda_FBB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FBB1)

    def lambda_FBC2():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FBC2)

    def lambda_FBD7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FBD7)
    Sleep(1000)

    def lambda_FBEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FBEF)

    def lambda_FC00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FC00)
    Jump("loc_FCBE")

    label("loc_FC11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FCBE")

    def lambda_FC1F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC1F)
    Sleep(100)

    def lambda_FC37():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FC37)
    Sleep(500)

    def lambda_FC4F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC4F)
    Sleep(200)

    def lambda_FC63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FC63)

    def lambda_FC74():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FC74)

    def lambda_FC89():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC89)
    Sleep(1000)

    def lambda_FCA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FCA1)

    def lambda_FCB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FCB2)

    label("loc_FCBE")

    WaitChrThread(0x102, 1)
    Sound(100, 0, 40, 0)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FEA2")

    ChrTalk(
        0x36,
        (
            "#10100FYeah, it looks like they\x01",
            "entered the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        "#10303F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x37, 500)
    Sleep(300)

    ChrTalk(
        0x36,
        "#11P#10105FWazy, something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10301FYeah. I feel like there\x01",
            "was some kind of presence\x01",
            "I felt while tailing them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10105FA presence... Could it\x01",
            "be Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10303FYeah, you're probably\x01",
            "right, but...\x02\x03",
            "#10300FAnyway, I can't tell\x01",
            "specifically.\x02\x03",
            "Let's head inside in a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10103FY-Yeah... roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_102B5")

    label("loc_FEA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_100DA")

    ChrTalk(
        0x37,
        (
            "#10300FHmm, looks like they've\x01",
            "entered the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x37, 0x35, 500)
    Sleep(300)

    ChrTalk(
        0x37,
        (
            "#11P#10305FRandy, is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FYeah. I felt some kinda\x01",
            "presence while tailing\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FYou too, huh... I felt\x01",
            "it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FYeah. Most likely it's\x01",
            "Heiyue keepin' an eye on\x01",
            "us, but...\x02\x03",
            "#00301FHow to say this... I\x01",
            "feel like that wasn't\x01",
            "all.\x02\x03",
            "#00306FI can't say specifically\x01",
            "what it was, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FHaha. I agree.\x02\x03",
            "#10300FAnyway, all we can do\x01",
            "now is wait and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303FYeah, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_102B5")

    label("loc_100DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_102B5")

    ChrTalk(
        0x36,
        (
            "#10100FYeah, it looks like they\x01",
            "entered the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x36, 0x35, 500)
    Sleep(300)

    ChrTalk(
        0x36,
        (
            "#11P#10105FRandy, is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FYeah. I felt some kinda\x01",
            "presence while tailing\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10101FA presence... Could it\x01",
            "be Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FYeah, possibly. But...\x02\x03",
            "#00306FIt's just, to be honest,\x01",
            "I've no idea what it was\x01",
            "specifically.\x02\x03",
            "#00300FAnyway, let's head\x01",
            "inside ourselves in a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10101FR-Right... Roger that.\x02",
    )

    CloseMessageWindow()

    label("loc_102B5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0170", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_109_F832 end

    def Function_110_102CD(): pass

    label("Function_110_102CD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10397")

    ChrTalk(
        0x1A2,
        (
            "Umm, is the department\x01",
            "store that way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, no, the station's\x01",
            "this way...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "Then, let's turn back at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yeah... Sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_103E8")

    label("loc_10397")


    ChrTalk(
        0x101,
        (
            "#00000FThere's no need to go to\x01",
            "Station Street. Let's\x01",
            "return to the square.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103E8")

    SetChrPos(0x0, 3740, 0, -19810, 0)
    EventEnd(0x4)
    Return()

    # Function_110_102CD end

    def Function_111_103FC(): pass

    label("Function_111_103FC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D4")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FHey, Lloyd...\x01",
            "Governmental District is\x01",
            "this way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. Let's turn\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "Wasn't the department\x01",
            "store this way?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_10514")

    label("loc_104D4")


    ChrTalk(
        0x101,
        (
            "#00000FThis is the way to\x01",
            "Governmental District,\x01",
            "isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10514")

    SetChrPos(0x0, 13290, 0, 26680, 180)
    EventEnd(0x4)
    Return()

    # Function_111_103FC end

    def Function_112_10528(): pass

    label("Function_112_10528")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1063F")
    TurnDirection(0x1A2, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "This arcade...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Could this be the Back\x01",
            "Street entrance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. You know it well,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...For now, we don't\x01",
            "have any business there\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "(Hmm. The old Revache\x01",
            "building Cao and the others\x01",
            "mentioned is there...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10676")

    label("loc_1063F")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any\x01",
            "business in Back Street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10676")

    SetChrPos(0x0, -14110, -10, 14420, 135)
    EventEnd(0x4)
    Return()

    # Function_112_10528 end

    def Function_113_1068A(): pass

    label("Function_113_1068A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWest Street is further\x01",
            "ahead.\x02\x03",
            "#00003FI don't want to wander\x01",
            "too far from department\x01",
            "store. Let's turn around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_113_1068A end

    SaveToFile()

Try(main)
