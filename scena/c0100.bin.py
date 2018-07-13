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

    Sepith("Sepith_10AEC", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_C5C", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0100", "Sepith_10AEC", 60, 30, 10, 0,
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
        "Function_10_2BDB",        # 0A, 10
        "Function_11_2BEB",        # 0B, 11
        "Function_12_3E38",        # 0C, 12
        "Function_13_3E75",        # 0D, 13
        "Function_14_3EBC",        # 0E, 14
        "Function_15_3F06",        # 0F, 15
        "Function_16_474C",        # 10, 16
        "Function_17_48C3",        # 11, 17
        "Function_18_4928",        # 12, 18
        "Function_19_4944",        # 13, 19
        "Function_20_4AA2",        # 14, 20
        "Function_21_4AEB",        # 15, 21
        "Function_22_4AFE",        # 16, 22
        "Function_23_4D2E",        # 17, 23
        "Function_24_552C",        # 18, 24
        "Function_25_55D0",        # 19, 25
        "Function_26_5CAB",        # 1A, 26
        "Function_27_5CF8",        # 1B, 27
        "Function_28_5D61",        # 1C, 28
        "Function_29_5F47",        # 1D, 29
        "Function_30_5F5A",        # 1E, 30
        "Function_31_7AC4",        # 1F, 31
        "Function_32_7AF4",        # 20, 32
        "Function_33_7B33",        # 21, 33
        "Function_34_7D65",        # 22, 34
        "Function_35_7EB5",        # 23, 35
        "Function_36_8524",        # 24, 36
        "Function_37_8578",        # 25, 37
        "Function_38_8591",        # 26, 38
        "Function_39_8883",        # 27, 39
        "Function_40_88CA",        # 28, 40
        "Function_41_88DD",        # 29, 41
        "Function_42_8E07",        # 2A, 42
        "Function_43_8E5C",        # 2B, 43
        "Function_44_8EB1",        # 2C, 44
        "Function_45_8F06",        # 2D, 45
        "Function_46_8F5B",        # 2E, 46
        "Function_47_8F8B",        # 2F, 47
        "Function_48_9163",        # 30, 48
        "Function_49_954F",        # 31, 49
        "Function_50_9E38",        # 32, 50
        "Function_51_9EB2",        # 33, 51
        "Function_52_A3BE",        # 34, 52
        "Function_53_A3F5",        # 35, 53
        "Function_54_A426",        # 36, 54
        "Function_55_A457",        # 37, 55
        "Function_56_A488",        # 38, 56
        "Function_57_A4B9",        # 39, 57
        "Function_58_A4EA",        # 3A, 58
        "Function_59_A51B",        # 3B, 59
        "Function_60_A702",        # 3C, 60
        "Function_61_A74A",        # 3D, 61
        "Function_62_A769",        # 3E, 62
        "Function_63_A788",        # 3F, 63
        "Function_64_A7BC",        # 40, 64
        "Function_65_A7FD",        # 41, 65
        "Function_66_A83E",        # 42, 66
        "Function_67_A887",        # 43, 67
        "Function_68_B200",        # 44, 68
        "Function_69_B23D",        # 45, 69
        "Function_70_B27A",        # 46, 70
        "Function_71_B2B7",        # 47, 71
        "Function_72_B2F4",        # 48, 72
        "Function_73_B331",        # 49, 73
        "Function_74_B36E",        # 4A, 74
        "Function_75_B3AB",        # 4B, 75
        "Function_76_B3CA",        # 4C, 76
        "Function_77_B3E7",        # 4D, 77
        "Function_78_B461",        # 4E, 78
        "Function_79_B4B4",        # 4F, 79
        "Function_80_B507",        # 50, 80
        "Function_81_B55A",        # 51, 81
        "Function_82_B5AD",        # 52, 82
        "Function_83_B600",        # 53, 83
        "Function_84_B61A",        # 54, 84
        "Function_85_CAAF",        # 55, 85
        "Function_86_CAEC",        # 56, 86
        "Function_87_CBDC",        # 57, 87
        "Function_88_CC25",        # 58, 88
        "Function_89_CCF5",        # 59, 89
        "Function_90_CDFC",        # 5A, 90
        "Function_91_CE16",        # 5B, 91
        "Function_92_CE48",        # 5C, 92
        "Function_93_CE8F",        # 5D, 93
        "Function_94_CED6",        # 5E, 94
        "Function_95_CF2B",        # 5F, 95
        "Function_96_CF80",        # 60, 96
        "Function_97_CFD5",        # 61, 97
        "Function_98_D200",        # 62, 98
        "Function_99_D2FC",        # 63, 99
        "Function_100_D380",       # 64, 100
        "Function_101_D472",       # 65, 101
        "Function_102_D9A3",       # 66, 102
        "Function_103_DE3B",       # 67, 103
        "Function_104_E516",       # 68, 104
        "Function_105_EACC",       # 69, 105
        "Function_106_F215",       # 6A, 106
        "Function_107_F246",       # 6B, 107
        "Function_108_F99B",       # 6C, 108
        "Function_109_FB15",       # 6D, 109
        "Function_110_10642",      # 6E, 110
        "Function_111_10782",      # 6F, 111
        "Function_112_108BD",      # 70, 112
        "Function_113_10A33",      # 71, 113
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
            "Two days after the dramatic\x01",
            "arrest at the Altair Lodge──\x02",
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

    def lambda_2BAA():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2BAA)
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

    def Function_10_2BDB(): pass

    label("Function_10_2BDB")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 50, 0)
    Return()

    # Function_10_2BDB end

    def Function_11_2BEB(): pass

    label("Function_11_2BEB")

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

    def lambda_2D3C():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D3C)
    Sleep(100)

    def lambda_2D59():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D59)
    Sleep(100)

    def lambda_2D76():
        OP_97(0x1A5, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_2D76)
    Sleep(100)

    def lambda_2D93():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D93)
    Sleep(100)

    def lambda_2DB0():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DB0)
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

    def lambda_2EDD():

        label("loc_2EDD")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EDD")

    QueueWorkItem2(0x101, 2, lambda_2EDD)

    def lambda_2EEF():

        label("loc_2EEF")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2EEF")

    QueueWorkItem2(0x102, 2, lambda_2EEF)

    def lambda_2F01():

        label("loc_2F01")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F01")

    QueueWorkItem2(0x1A5, 2, lambda_2F01)

    def lambda_2F13():

        label("loc_2F13")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F13")

    QueueWorkItem2(0x109, 2, lambda_2F13)

    def lambda_2F25():

        label("loc_2F25")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_2F25")

    QueueWorkItem2(0x105, 2, lambda_2F25)
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
            "#5PYou're late, we were waitin'\x01",
            "for ya in front of the bakery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PClasses are starting soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#12P#01109FEhehe, sorry, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHi there, Ryｹ, Henri.\x01",
            "Always full of energy, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*, thank you for always\x01",
            "being good friends with KeA.\x02",
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
        "#5PHe he, been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PI've heard it from KeA; you're\x01",
            "startin' the Support Section again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, fortunately.\x02\x03",
            "#00000FWe're revamping it here and there,\x01",
            "so look forward to it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PHe he, listen at you talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PWell, as you're now guys, I guess\x01",
            "I can approve of you to be almost\x01",
            "as good as Bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PListen you, you're being arrogant as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F*cluckle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAs expected from the Support\x01",
            "Section. It looks like you're\x01",
            "very popular among children too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_3310():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3310)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#5POh, and you two over there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PYou are some new faces.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PAnd now that I think about it, Miss Tio\x01",
            "and Mr. Randy aren't with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FThey had some business to attend to\x01",
            "and they haven't returned yet.\x02\x03",
            "#00100FThese are Miss Noｱl and Wazy.\x01",
            "They're new members of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FUh uh, nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#5PYeah, nice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5P...Wait a sec.\x01",
            "Are you a man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PSomehow you've got\x01",
            "a woman-like face...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        "#11PH-Hey, Ryｹ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHu hu, I wonder...\x02\x03",
            "#10302FIf you think I am a woman,\x01",
            "couldn't it be true?\x02",
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
            "#00006F...Listen now, Wazy.\x01",
            "Don't puzzle the kids.\x02\x03",
            "#00000FMore importantly, shouldn't\x01",
            "you three hurry up?\x02",
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

    def lambda_362F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_362F)
    Sleep(50)

    def lambda_363F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_363F)
    Sleep(150)

    ChrTalk(
        0x1A5,
        (
            "#6P#01105FAh, yeah.\x02\x03",
            "#01109FThen, everyone!\x01",
            "Do your best with work!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A5, 500)

    def lambda_369F():

        label("loc_369F")

        TurnDirection(0xFE, 0x1A5, 500)
        Yield()
        Jump("loc_369F")

    QueueWorkItem2(0x101, 2, lambda_369F)

    ChrTalk(
        0x101,
        "#00009FYeah, do your best too, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FPay attention to cars, alright?\x02",
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
            "#5PAlright, then let's drop\x01",
            "by Momo's house.\x02",
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
            "#11P#10109FUh uh...\x01",
            "What an energetic kid.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        "#11P#10300FIs he from West Street?\x02",
    )

    CloseMessageWindow()

    def lambda_3847():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3847)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, the other one is from\x01",
            "Residential Street though.\x02\x03",
            "#00004F──Well then.\x01",
            "Let's start working.\x02\x03",
            "#00000FFor starters, let's drop by the Orbal\x01",
            "Store over there and police HQ...\x02\x03",
            "I think it would be better if we also\x01",
            "did a general round inside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10100FIndeed.\x01",
            "Patrolling, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104F*giggle*, it's not such\x01",
            "a great deal, however...\x02\x03",
            "#00100FBecause we could get unexpected information,\x01",
            "even patrolling around is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe should get a communication via\x01",
            "ENIGMA from the Chief in a little.\x02\x03",
            "Until we receive that, let's go to\x01",
            "various places inside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10102FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10304FHu hu, let's go then.\x02",
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
            "You have become able to use the Crossbell City map.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When pressing the START button on the field inside\x01",
            "the city, you can open the entire city map.\x01",
            "(If you press the START button once again,\x01",
            "the autonomous state map will be displayed.)\x02",
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
            "Furthermore, the map can be\x01",
            "used as a shortcut to move to\x01",
            "specific areas in the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please select an area you want to go\x01",
            "to from the city sectors on the left.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, depending on the situation, there will be\x01",
            "even times when you cannot use the city map.\x02",
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

    # Function_11_2BEB end

    def Function_12_3E38(): pass

    label("Function_12_3E38")


    def lambda_3E3D():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E3D)
    WaitChrThread(0xFE, 1)

    def lambda_3E5B():
        OP_95(0xFE, -3400, 0, -5700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E5B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_3E38 end

    def Function_13_3E75(): pass

    label("Function_13_3E75")

    Sleep(50)

    def lambda_3E7D():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E7D)
    WaitChrThread(0xFE, 1)

    def lambda_3E9B():
        OP_95(0xFE, -2800, 0, -4800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E9B)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_13_3E75 end

    def Function_14_3EBC(): pass

    label("Function_14_3EBC")

    OP_92(0xFE, 0xFFFFE318, 0xFFFFF31C, 0x1F4)

    def lambda_3ECE():
        OP_95(0xFE, -7400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ECE)
    WaitChrThread(0xFE, 1)

    def lambda_3EEC():
        OP_95(0xFE, -17400, 0, -3300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EEC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3EBC end

    def Function_15_3F06(): pass

    label("Function_15_3F06")

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

    def lambda_4039():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4039)
    Sleep(50)

    def lambda_4049():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4049)
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
        "#11P#00005FAh, could it be the Chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FIt wouldn't be strange to\x01",
            "receive a call from him now.\x02",
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
            "#00000FYes, Special Support Section,\x01",
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
            "Hey, good job.\x02\x03",
            "Like I said this morning, I'll have\x01",
            "you come to the Police Academy.\x02\x03",
            "You know where it is, right?\x02",
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
            "#00000FIt's after passing the gate from\x01",
            "midway of West Crossbell Highway.\x02",
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
            "Yeah, I'll leave the gate open.\x02\x03",
            "By the way... I think you've done \x01",
            "a general round of the city, right?\x02\x03",
            "In all sincerity, how did it look?\x02",
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
            "#00003F...Yes, well.\x02\x03",
            "#00001FDue to various reasons, I have the\x01",
            "feeling something will happen.\x02",
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
            "You should sharpen that sense of intuition\x01",
            "of yours now more than ever.\x02\x03",
            "Then, I'll be waiting for you.\x07\x00\x02",
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
        "#6P#00100FAs I thought, it looks like it was the Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FIt appears he said\x01",
            "something worrisome...?\x02",
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
            "#11P#00006FYes, the Chief too seems to have\x01",
            "felt a change in the situation.\x02\x03",
            "#00001FIt seems I should've reported about\x01",
            "the Heiyue and Captain Lechter too.\x02",
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
            "#5P#10300FThen, should we go to\x01",
            "the Police Academy now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FYes, let's go on the highway from the west exit.\x02",
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
            "You became able to select\x01",
            ""West Crossbell Highway"\x01",
            "from Crossbell City Map.\x07\x00\x02",
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

    # Function_15_3F06 end

    def Function_16_474C(): pass

    label("Function_16_474C")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4851")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xA, 0xFF)
    SetChrPos(0xA, -6880, 0, 810, 0)

    def lambda_481D():

        label("loc_481D")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_481D")

    QueueWorkItem2(0xA, 2, lambda_481D)
    SetChrPos(0xB, -6300, 0, -170, 0)
    EndChrThread(0xB, 0xFF)

    def lambda_4844():

        label("loc_4844")

        TurnDirection(0xFE, 0x2D, 500)
        Yield()
        Jump("loc_4844")

    QueueWorkItem2(0xB, 2, lambda_4844)

    label("loc_4851")

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

    # Function_16_474C end

    def Function_17_48C3(): pass

    label("Function_17_48C3")

    SetChrPos(0xFE, -35510, -2590, -4520, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23860, -640, -4420)
    OP_9F(0x1, -14350, 750, -1880)
    OP_9F(0x1, -11380, 0, 7200)
    OP_9F(0x1, -14250, 0, 13970)
    OP_9F(0x1, -28100, 0, 29400)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_17_48C3 end

    def Function_18_4928(): pass

    label("Function_18_4928")

    Sound(458, 0, 100, 0)
    Sound(468, 2, 100, 0)
    Sleep(5000)
    Sound(494, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_4928 end

    def Function_19_4944(): pass

    label("Function_19_4944")

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

    # Function_19_4944 end

    def Function_20_4AA2(): pass

    label("Function_20_4AA2")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_20_4AA2 end

    def Function_21_4AEB(): pass

    label("Function_21_4AEB")

    Sleep(2300)
    Sound(458, 0, 70, 0)
    Sleep(4300)
    Sound(494, 0, 70, 0)
    Return()

    # Function_21_4AEB end

    def Function_22_4AFE(): pass

    label("Function_22_4AFE")

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

    # Function_22_4AFE end

    def Function_23_4D2E(): pass

    label("Function_23_4D2E")

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
            "#30W      Septian Calendar 1204──early autumn.\x02\x03",
            "Proposed by the new Crossbell Mayor,\x01",
            "the IBC president, Dieter Crois, the\x01",
            ""West Zemuria Trade Conference" began.\x02\x03",
            "From the West major power, the Empire,\x01",
            "the "Blood and Iron Chancellor" Giliath\x01",
            "Osborne and the man of the world, Prince Olivert──\x02\x03",
            "From the East major power, the Calvard\x01",
            "Republic, President Samuel Rocksmith,\x01",
            "who gained support from the masses──\x02\x03",
            "From the Principality of Remiferia located in\x01",
            "the north-east, the Archduke Albert, who, in\x01",
            "spite of his young age, governs the country──\x02\x03",
            "From the Liberl Kingdom in the south-west, the\x01",
            "Crown Princess Klaudia, representing the queen──\x02\x03",
            "All state guests of VIP rank kept\x01",
            "gathering in Crossbell at this very time.\x02",
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

    # Function_23_4D2E end

    def Function_24_552C(): pass

    label("Function_24_552C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5564"),
        (1, "loc_556C"),
        (2, "loc_5574"),
        (3, "loc_557C"),
        (4, "loc_5584"),
        (5, "loc_558C"),
        (6, "loc_5594"),
        (SWITCH_DEFAULT, "loc_559C"),
    )


    label("loc_5564")

    Sleep(100)
    Jump("loc_55A4")

    label("loc_556C")

    Sleep(200)
    Jump("loc_55A4")

    label("loc_5574")

    Sleep(300)
    Jump("loc_55A4")

    label("loc_557C")

    Sleep(400)
    Jump("loc_55A4")

    label("loc_5584")

    Sleep(500)
    Jump("loc_55A4")

    label("loc_558C")

    Sleep(600)
    Jump("loc_55A4")

    label("loc_5594")

    Sleep(700)
    Jump("loc_55A4")

    label("loc_559C")

    Sleep(800)
    Jump("loc_55A4")

    label("loc_55A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55CF")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_55A4")

    label("loc_55CF")

    Return()

    # Function_24_552C end

    def Function_25_55D0(): pass

    label("Function_25_55D0")

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

    # Function_25_55D0 end

    def Function_26_5CAB(): pass

    label("Function_26_5CAB")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, 0, -4000)
    OP_9F(0x1, 11500, 0, 1000)
    OP_9F(0x1, 12000, 0, 30000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5CE7():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5CE7)
    Return()

    # Function_26_5CAB end

    def Function_27_5CF8(): pass

    label("Function_27_5CF8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3700, 0, -20000)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 10580, 0, 4180)
    OP_9F(0x1, 12000, 0, 10000)
    OP_9F(0x1, 12000, 0, 15000)
    OP_9F(0x2, 0xFE, 7000, 0x6)

    def lambda_5D50():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D50)
    Return()

    # Function_27_5CF8 end

    def Function_28_5D61(): pass

    label("Function_28_5D61")

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

    def lambda_5ED8():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5ED8)
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

    # Function_28_5D61 end

    def Function_29_5F47(): pass

    label("Function_29_5F47")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(3600)
    Sound(494, 0, 50, 0)
    Return()

    # Function_29_5F47 end

    def Function_30_5F5A(): pass

    label("Function_30_5F5A")

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

    def lambda_6208():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6208)
    Sleep(50)

    def lambda_6218():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6218)
    Sleep(50)

    def lambda_6228():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6228)
    Sleep(50)

    def lambda_6238():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6238)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005FWhat...?\x02",
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

    def lambda_636B():

        label("loc_636B")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_636B")

    QueueWorkItem2(0x1E, 2, lambda_636B)

    def lambda_637D():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFE9BC, 0xFFFF9A70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_637D)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 3, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_63BF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63BF)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_63E7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_63E7)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_640F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_640F)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6437():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6437)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_645F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_645F)
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
        "#00011F#6P#NH-Huh!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10111F#6P#NA w-white hawk...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#12P...No, it looks\x01",
            "like a falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey now, what is he doin' in\x01",
            "the smack middle of the city...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1E, 0x3)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x0)
    OP_68(-27800, -6900, -26700, 3000)
    MoveCamera(37, 19, 0, 3000)

    def lambda_65A6():
        OP_9E(0xFE, 0xFFFF97B4, 0xFFFF9A70, 0x493E0, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_65A6)
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

    def lambda_6747():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6747)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B8A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BBC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1BEE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_6790():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6790)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C20), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C52), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x1E, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1CB6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_67D9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_67D9)
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

    def lambda_68D7():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE2B4, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_68D7)
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
            "Screee.\x02\x03",
            "Scree, scree, screee.\x02",
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
            "#5P#00001FC-Could it be...\x01",
            "That he has business with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PIt seems like when\x01",
            "Zeit speaks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PUhhm, if peTiote was here with us, \x01",
            "maybe we could understand him...\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    ClearChrFlags(0x1D, 0x80)

    def lambda_6B0B():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA628, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6B0B)

    def lambda_6B25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6B25)
    WaitChrThread(0x1D, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x1D,
        "#01105F#5POh, what's happened?\x02",
    )

    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    CloseMessageWindow()
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)

    def lambda_6B9C():
        OP_96(0xFE, 0xFFFF90AC, 0xFFFFDFF8, 0xFFFF9750, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6B9C)
    Sleep(300)

    def lambda_6BB9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6BB9)
    Sleep(100)

    def lambda_6BC9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BC9)
    Sleep(100)

    def lambda_6BD9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BD9)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x87, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FWow, a white bird!\x02\x03",
            "#01109FHe's got a sharp beak,\x01",
            "he's so cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#08009FScreee㈱\x02\x03",
            "#08000FScreee, scree, scree♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#6P#01103FHm, hm.\x02\x03",
            "#01102FI see, so that's it...\x02",
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
            "#5P#00012F(KeA...\x01",
            "Can she really understand him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(A-Amazing...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    def lambda_6D9D():

        label("loc_6D9D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6D9D")

    QueueWorkItem2(0x1D, 2, lambda_6D9D)

    ChrTalk(
        0x1D,
        (
            "#6P#01100FUhm, so, this little one\x01",
            "says he's called "Sieg".\x02\x03",
            "He's saying he's got a message\x01",
            "for you, so, will you accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FI-Is that so...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1E, 500)

    ChrTalk(
        0x104,
        (
            "#00305F#5POh, he actually has a memo\x01",
            "fastened to his leg, huh.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E9B():
        OP_95(0xFE, -27600, -8200, -26600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E9B)
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    def lambda_6EBF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6EBF)
    WaitChrThread(0x101, 1)
    EndChrThread(0x1D, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the memo that was\x01",
            "fastened to the bird's leg.\x07\x00\x02",
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
            "Dear Crossbell Police, Special Support Section.\x02\x03",
            "Pardon my rudeness for contacting you,\x01",
            "but your fame has reached my ears.\x02\x03",
            "If you have time, would you be\x01",
            "willing to consult with me privately?\x02\x03",
            "I am going to wait for you at the meeting\x01",
            "place terrace at Crossbell Airport, this evening.\x02\x03",
            "PS: In case you cannot make it,\x01",
            "it is all right if you do not reply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F#5P............\x02",
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
            "#10106F#5PIt says privately, and no sender.\x01",
            "It is too suspicious, however...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302F#11PHowever, the handwriting is beautiful\x01",
            "and the sentences are polite...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301F#5PAbove all, there's a white falcon\x01",
            "crest applied on the memo...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1E,
        (
            "#08000F#12PScreee.\x02\x03",
            "Scree, scree, screee.\x02",
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

    def lambda_72AF():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFE4A8, 0xFFFF93CC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_72AF)
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

    def lambda_7335():

        label("loc_7335")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_7335")

    QueueWorkItem2(0x1E, 2, lambda_7335)
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

    def lambda_756A():
        OP_96(0xFE, 0xFFFF92A0, 0xFFFFEF98, 0xFFFF64EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_756A)
    Sleep(300)

    def lambda_7587():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7587)
    Sleep(100)

    def lambda_7597():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7597)
    Sleep(100)

    def lambda_75A7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_75A7)
    Sleep(100)

    def lambda_75B7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_75B7)
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
            "#11P#00011FEhm...\x01",
            "KeA, what did he say?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x101, 500)

    ChrTalk(
        0x1D,
        (
            "#6P#01111FUhhm, he said that going\x01",
            "or not is up to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_7733():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7733)
    Sleep(50)

    def lambda_7743():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7743)
    Sleep(50)

    def lambda_7753():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7753)
    Sleep(50)

    def lambda_7763():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7763)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#11PW-What do we do?\x02\x03",
            "#00101FI think that's\x01",
            "impossible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PYeah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PHowever, a white falcon crest...\x01",
            "Even that bird looked like one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PAhaha, it makes you have\x01",
            "even more expectations.\x02",
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
            "#6P#00003F──It is a welcome invitation.\x01",
            "Let's accept it.\x02\x03",
            "#00000FBecause there's still time until evening,\x01",
            "we can finish other business too.\x02",
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
        "#10106F#5PI-I'm feeling nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PWell, I don't think goin'\x01",
            "in full dress is needed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHu hu, then, when we have finished our business, \x01",
            "let's go to the Crossbell Airport past the south exit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x1D,
        (
            "#6P#01110FI don't really get it, but\x01",
            "everyone, good luck!\x02",
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

    # Function_30_5F5A end

    def Function_31_7AC4(): pass

    label("Function_31_7AC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AF3")

    def lambda_7AD4():
        OP_9E(0xFE, 0xFFFF99A8, 0xFFFF9A70, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7AD4)
    WaitChrThread(0x1E, 1)
    Jump("Function_31_7AC4")

    label("loc_7AF3")

    Return()

    # Function_31_7AC4 end

    def Function_32_7AF4(): pass

    label("Function_32_7AF4")


    def lambda_7AF9():
        OP_9E(0xFE, 0xFFFF9494, 0xFFFF93CC, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7AF9)
    WaitChrThread(0x1E, 1)

    def lambda_7B18():
        OP_9E(0xFE, 0xFFFF90AC, 0xFFFF93CC, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7B18)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_32_7AF4 end

    def Function_33_7B33(): pass

    label("Function_33_7B33")

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

    def lambda_7CEB():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7CEB)
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

    # Function_33_7B33 end

    def Function_34_7D65(): pass

    label("Function_34_7D65")

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

    # Function_34_7D65 end

    def Function_35_7EB5(): pass

    label("Function_35_7EB5")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_809B")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_806A():

        label("loc_806A")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_806A")

    QueueWorkItem2(0xA, 2, lambda_806A)

    def lambda_807C():

        label("loc_807C")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_807C")

    QueueWorkItem2(0xB, 2, lambda_807C)

    def lambda_808E():

        label("loc_808E")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_808E")

    QueueWorkItem2(0x13, 2, lambda_808E)

    label("loc_809B")

    OP_68(-13300, 1500, 14200, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_80E0():
        OP_9B(0x0, 0x101, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80E0)
    Sleep(50)

    def lambda_80F8():
        OP_9B(0x0, 0x102, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80F8)
    Sleep(50)

    def lambda_8110():
        OP_9B(0x0, 0x103, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8110)
    Sleep(50)

    def lambda_8128():
        OP_9B(0x0, 0x104, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8128)
    Sleep(50)

    def lambda_8140():
        OP_9B(0x0, 0x105, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8140)
    Sleep(50)

    def lambda_8158():
        OP_9B(0x0, 0x109, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8158)
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
        "#00201F#5PThey are sirens.\x02",
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
            "#00108F#5PCould they be carrying the wounded\x01",
            "from the derailment accident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PWell, considering the timing,\x01",
            "I think there's no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...It seems that sister Cecil\x01",
            "and the others will be busy.\x02\x03",
            "#00001FLet's go to the scene too.\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84F6")
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

    label("loc_84F6")

    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 6)
    OP_24(0x3B2)
    EventEnd(0x5)
    Return()

    # Function_35_7EB5 end

    def Function_36_8524(): pass

    label("Function_36_8524")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13000, 500, -2870)
    OP_9F(0x1, -350, 0, -7080)
    OP_9F(0x1, 4300, 0, -18000)
    OP_9F(0x1, 4500, 0, -30000)
    OP_9F(0x1, 4500, 0, -40000)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_36_8524 end

    def Function_37_8578(): pass

    label("Function_37_8578")

    Sound(465, 0, 80, 0)
    Sleep(4000)
    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(465, 0, 80, 0)
    Return()

    # Function_37_8578 end

    def Function_38_8591(): pass

    label("Function_38_8591")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8776")
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x13, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)

    def lambda_8745():

        label("loc_8745")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8745")

    QueueWorkItem2(0xA, 2, lambda_8745)

    def lambda_8757():

        label("loc_8757")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8757")

    QueueWorkItem2(0xB, 2, lambda_8757)

    def lambda_8769():

        label("loc_8769")

        TurnDirection(0xFE, 0x2F, 500)
        Yield()
        Jump("loc_8769")

    QueueWorkItem2(0x13, 2, lambda_8769)

    label("loc_8776")

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

    # Function_38_8591 end

    def Function_39_8883(): pass

    label("Function_39_8883")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13630, 0, 14510)
    OP_9F(0x1, -11670, 0, 9100)
    OP_9F(0x1, -12500, 0, 4800)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x8)
    Return()

    # Function_39_8883 end

    def Function_40_88CA(): pass

    label("Function_40_88CA")

    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 50, 0)
    Return()

    # Function_40_88CA end

    def Function_41_88DD(): pass

    label("Function_41_88DD")

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
            "#6P#10302FWell then, it was the casino in the Entertainment\x01",
            "District and two stores in Downtown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah, there could be clues\x01",
            "in other places too, but...\x02\x03",
            "#00001FFor now, we don't have time\x01",
            "to go outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FLuckily, this morning we didn't\x01",
            "receive any new support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FProbably, due to what happened yesterday,\x01",
            "even HQ is still in chaos.\x02\x03",
            "#00101FIt appears that the CGF received\x01",
            "quite some damage too...\x02",
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

    def lambda_8C4B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8C4B)

    def lambda_8C58():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8C58)
    Sleep(50)

    def lambda_8C68():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C68)
    Sleep(50)

    def lambda_8C78():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C78)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00106F...I'm sorry.\x02\x03",
            "#00108FConsidering your position, it's\x01",
            "not someone else's business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5P...No, we CGF are ready for\x01",
            "those kind of dangers too.\x02\x03",
            "#10100FAnd also, I'm currently a\x01",
            "Support Section member.\x02\x03",
            "Let's go...\x01",
            "...To catch senior Randy!\x02",
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

    # Function_41_88DD end

    def Function_42_8E07(): pass

    label("Function_42_8E07")


    def lambda_8E0C():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E0C)

    def lambda_8E26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E26)
    WaitChrThread(0xFE, 1)

    def lambda_8E3B():
        OP_95(0xFE, -27400, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E3B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_42_8E07 end

    def Function_43_8E5C(): pass

    label("Function_43_8E5C")


    def lambda_8E61():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E61)

    def lambda_8E7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E7B)
    WaitChrThread(0xFE, 1)

    def lambda_8E90():
        OP_95(0xFE, -28000, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E90)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_8E5C end

    def Function_44_8EB1(): pass

    label("Function_44_8EB1")


    def lambda_8EB6():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EB6)

    def lambda_8ED0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8ED0)
    WaitChrThread(0xFE, 1)

    def lambda_8EE5():
        OP_95(0xFE, -29400, -8200, -26200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EE5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_44_8EB1 end

    def Function_45_8F06(): pass

    label("Function_45_8F06")


    def lambda_8F0B():
        OP_95(0xFE, -28700, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F0B)

    def lambda_8F25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8F25)
    WaitChrThread(0xFE, 1)

    def lambda_8F3A():
        OP_95(0xFE, -30000, -8200, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F3A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_8F06 end

    def Function_46_8F5B(): pass

    label("Function_46_8F5B")


    def lambda_8F60():
        OP_95(0xFE, -28700, -8200, -23700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F60)

    def lambda_8F7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8F7A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_8F5B end

    def Function_47_8F8B(): pass

    label("Function_47_8F8B")

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

    def lambda_912C():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_912C)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(457, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_8F8B end

    def Function_48_9163(): pass

    label("Function_48_9163")

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
            "Those wills, just the other day,\x01",
            "knocked down fear and sorrow\x01",
            "to the very bottom of Crossbell.\x02\x03",
            "I think that you all, wise citizens,\x01",
            "have slightly noticed...\x02",
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
            "I dare, today, in this place,\x01",
            "to accuse those powers by name.\x02\x03",
            ""Erebonian Imperial Government"...\x01",
            "This is one of the wicked wills.\x02",
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

    # Function_48_9163 end

    def Function_49_954F(): pass

    label("Function_49_954F")

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

    def lambda_9649():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9649)
    Sleep(50)

    def lambda_9666():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9666)
    Sleep(50)

    def lambda_9683():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9683)
    Sleep(50)

    def lambda_96A0():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_96A0)
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

    def lambda_9733():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9733)
    Sleep(50)

    def lambda_9743():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9743)
    Sleep(50)

    def lambda_9753():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9753)
    Sleep(50)

    def lambda_9763():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9763)
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

    def lambda_97EB():
        OP_96(0xFE, 0xFFFFA498, 0xFFFFDFF8, 0xFFFF9F84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_97EB)
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

    def lambda_9872():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9872)

    def lambda_988B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_988B)

    def lambda_9898():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9898)
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
            "#00302F#11PIt's true that many thing are goin' on,\x01",
            "but you don't have to be worried at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#01114F#30W...Yes...\x02",
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
            "#11P#00004F...It's fine, KeA.\x02\x03",
            "#00008FIt's true that we don't know\x01",
            "what will be of Crossbell in\x01",
            "the future, but...\x02\x03",
            "#00002FIt doesn't change the fact\x01",
            "that we'll always return\x01",
            "where you're, KeA.\x02",
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
            "#12P#00204FRight...\x01",
            "At least that is for certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PWe came right back even when\x01",
            "we went away before, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FSo, KeA. Don't worry and\x01",
            "wait for our return, eh?\x02",
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

    def lambda_9BE6():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFF9F84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9BE6)
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
            "#3624V#30WYes......#800W!\x01",
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
            "Wazy is not a party\x01",
            "member anymore.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9D75")
    Jump("loc_9D7A")

    label("loc_9D75")

    OP_29(0x8E, 0x4, 0x40)

    label("loc_9D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9D8B")
    Jump("loc_9D90")

    label("loc_9D8B")

    OP_29(0x8F, 0x4, 0x40)

    label("loc_9D90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9DA1")
    Jump("loc_9DA6")

    label("loc_9DA1")

    OP_29(0x90, 0x4, 0x40)

    label("loc_9DA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9DB7")
    Jump("loc_9DBC")

    label("loc_9DB7")

    OP_29(0x91, 0x4, 0x40)

    label("loc_9DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9DCD")
    Jump("loc_9DD2")

    label("loc_9DCD")

    OP_29(0x92, 0x4, 0x40)

    label("loc_9DD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9DE3")
    Jump("loc_9DE8")

    label("loc_9DE3")

    OP_29(0x93, 0x4, 0x40)

    label("loc_9DE8")

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

    # Function_49_954F end

    def Function_50_9E38(): pass

    label("Function_50_9E38")

    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)

    def lambda_9E60():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9E60)

    def lambda_9E7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9E7A)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_9EA9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9EA9)
    Return()

    # Function_50_9E38 end

    def Function_51_9EB2(): pass

    label("Function_51_9EB2")

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
            "#30WIt is as you all know too──\x02\x03",
            "The other day, former Mayor\x01",
            "Crois declared the founding of the\x01",
            ""Independent State of Crossbell".\x02\x03",
            "A military organization called State Guard\x01",
            "was established. I think there're persons\x01",
            "who are going to get used to it, however...\x02",
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
            "#30W──However, everyone!\x01",
            "I want you to think once more!\x02\x03",
            "To think if we really have\x01",
            ""chosen" this situation!\x07\x00\x02",
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

    # Function_51_9EB2 end

    def Function_52_A3BE(): pass

    label("Function_52_A3BE")

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

    # Function_52_A3BE end

    def Function_53_A3F5(): pass

    label("Function_53_A3F5")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A405():
        OP_95(0xFE, -2800, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A405)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_53_A3F5 end

    def Function_54_A426(): pass

    label("Function_54_A426")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A436():
        OP_95(0xFE, -1500, 0, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A436)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_54_A426 end

    def Function_55_A457(): pass

    label("Function_55_A457")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A467():
        OP_95(0xFE, -2500, 0, 10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A467)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_55_A457 end

    def Function_56_A488(): pass

    label("Function_56_A488")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A498():
        OP_95(0xFE, 1300, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A498)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_56_A488 end

    def Function_57_A4B9(): pass

    label("Function_57_A4B9")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A4C9():
        OP_95(0xFE, 2300, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4C9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_57_A4B9 end

    def Function_58_A4EA(): pass

    label("Function_58_A4EA")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A4FA():
        OP_95(0xFE, -2800, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_58_A4EA end

    def Function_59_A51B(): pass

    label("Function_59_A51B")

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

    # Function_59_A51B end

    def Function_60_A702(): pass

    label("Function_60_A702")

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

    # Function_60_A702 end

    def Function_61_A74A(): pass

    label("Function_61_A74A")


    def lambda_A74F():
        OP_95(0xFE, -1600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A74F)
    WaitChrThread(0xB, 1)
    Return()

    # Function_61_A74A end

    def Function_62_A769(): pass

    label("Function_62_A769")


    def lambda_A76E():
        OP_95(0xFE, -2900, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A76E)
    WaitChrThread(0xF, 1)
    Return()

    # Function_62_A769 end

    def Function_63_A788(): pass

    label("Function_63_A788")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A7A2():
        OP_95(0xFE, 6300, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A7A2)
    WaitChrThread(0xE, 1)
    Return()

    # Function_63_A788 end

    def Function_64_A7BC(): pass

    label("Function_64_A7BC")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A7E3():
        OP_95(0xFE, -1100, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A7E3)
    WaitChrThread(0xC, 1)
    Return()

    # Function_64_A7BC end

    def Function_65_A7FD(): pass

    label("Function_65_A7FD")

    OP_92(0xFE, 0x0, 0xFA0, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A824():
        OP_95(0xFE, 400, 0, 12100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A824)
    WaitChrThread(0xD, 1)
    Return()

    # Function_65_A7FD end

    def Function_66_A83E(): pass

    label("Function_66_A83E")

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

    # Function_66_A83E end

    def Function_67_A887(): pass

    label("Function_67_A887")

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
            "#00101F#12PIt's like the "barrier" that was\x01",
            "enveloping Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F#12PIt is probably of the same nature.\x02\x03",
            "#00201F...And it is likely the bell's resonance\x01",
            "what is originating this haze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PHey now, what for──\x02",
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

    def lambda_AD34():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD34)

    def lambda_AD41():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AD41)
    Sleep(50)

    def lambda_AD51():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AD51)

    def lambda_AD5E():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_AD5E)
    Sleep(50)

    def lambda_AD6E():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AD6E)

    def lambda_AD7B():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AD7B)
    Sleep(50)

    def lambda_AD8B():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AD8B)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PWhat...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#11P──Careful.\x01",
            "They're coming from around us.\x02",
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

    def lambda_AEC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_AEC2)
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

    def lambda_AF7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_AF7C)
    Sleep(300)

    def lambda_AF90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_AF90)
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
        "#6P#00107FThe ones from the "Tower of Stargaze"...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00207FThey are the same magic golems,\x01",
            "but they look far more dangerous...!\x02",
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

    # Function_67_A887 end

    def Function_68_B200(): pass

    label("Function_68_B200")


    def lambda_B205():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B205)
    WaitChrThread(0xFE, 1)

    def lambda_B223():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B223)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_B200 end

    def Function_69_B23D(): pass

    label("Function_69_B23D")


    def lambda_B242():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B242)
    WaitChrThread(0xFE, 1)

    def lambda_B260():
        OP_96(0xFE, 0x64, 0x0, 0xFFFFEB4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B260)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_B23D end

    def Function_70_B27A(): pass

    label("Function_70_B27A")


    def lambda_B27F():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B27F)
    WaitChrThread(0xFE, 1)

    def lambda_B29D():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B29D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_B27A end

    def Function_71_B2B7(): pass

    label("Function_71_B2B7")


    def lambda_B2BC():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2BC)
    WaitChrThread(0xFE, 1)

    def lambda_B2DA():
        OP_96(0xFE, 0x190, 0x0, 0xFFFFE50C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2DA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_B2B7 end

    def Function_72_B2F4(): pass

    label("Function_72_B2F4")


    def lambda_B2F9():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2F9)
    WaitChrThread(0xFE, 1)

    def lambda_B317():
        OP_96(0xFE, 0xFFFFF4AC, 0x0, 0xFFFFE7C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B317)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_B2F4 end

    def Function_73_B331(): pass

    label("Function_73_B331")


    def lambda_B336():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B336)
    WaitChrThread(0xFE, 1)

    def lambda_B354():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE3E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B354)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_B331 end

    def Function_74_B36E(): pass

    label("Function_74_B36E")


    def lambda_B373():
        OP_96(0xFE, 0xE10, 0x0, 0xFFFFCA18, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B373)
    WaitChrThread(0xFE, 1)

    def lambda_B391():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFE37C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B391)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_B36E end

    def Function_75_B3AB(): pass

    label("Function_75_B3AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3C9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_75_B3AB")

    label("loc_B3C9")

    Return()

    # Function_75_B3AB end

    def Function_76_B3CA(): pass

    label("Function_76_B3CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3E6")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_76_B3CA")

    label("loc_B3E6")

    Return()

    # Function_76_B3CA end

    def Function_77_B3E7(): pass

    label("Function_77_B3E7")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_B418():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B418)
    Sleep(1000)
    SetChrFlags(0xFE, 0x20)

    def lambda_B439():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFE764, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B439)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_B3E7 end

    def Function_78_B461(): pass

    label("Function_78_B461")

    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B4A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4A0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_78_B461 end

    def Function_79_B4B4(): pass

    label("Function_79_B4B4")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B4F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4F3)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_79_B4B4 end

    def Function_80_B507(): pass

    label("Function_80_B507")

    PlayEffect(0x0, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B546():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B546)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_80_B507 end

    def Function_81_B55A(): pass

    label("Function_81_B55A")

    PlayEffect(0x0, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B599():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B599)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_81_B55A end

    def Function_82_B5AD(): pass

    label("Function_82_B5AD")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_B5EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5EC)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_82_B5AD end

    def Function_83_B600(): pass

    label("Function_83_B600")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B619")
    Sound(986, 0, 80, 0)
    Sleep(1000)
    Jump("Function_83_B600")

    label("loc_B619")

    Return()

    # Function_83_B600 end

    def Function_84_B61A(): pass

    label("Function_84_B61A")

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

    def lambda_BA7B():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA7B)

    def lambda_BA88():
        TurnDirection(0xFE, 0x28, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA88)

    def lambda_BA95():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA95)

    def lambda_BAA2():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BAA2)

    def lambda_BAAF():
        TurnDirection(0xFE, 0x29, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BAAF)

    def lambda_BABC():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BABC)

    def lambda_BAC9():
        TurnDirection(0xFE, 0x2A, 0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BAC9)
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

    def lambda_BBCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BBCF)
    Sleep(300)

    def lambda_BBE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_BBE3)
    Sleep(300)

    def lambda_BBF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_BBF7)
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

    def lambda_BC7E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BC7E)

    def lambda_BC8B():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC8B)
    Sleep(50)

    def lambda_BC9B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC9B)
    Sleep(50)

    def lambda_BCAB():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BCAB)
    Sleep(50)

    def lambda_BCBB():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCBB)
    Sleep(50)

    def lambda_BCCB():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_BCCB)
    Sleep(50)

    def lambda_BCDB():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCDB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#5P#00010FKh...\x01",
            "Why're such things inside the city!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FD-Don't tell me that...\x01",
            ""Uncle" and Bell released them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FN-No way...\x01",
            "It would be absolutely unforgivable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FHowever, that seems the most\x01",
            "plausible possibility.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#12P#10408FIt seems that this "bell"\x01",
            "is related to it too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BE88():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BE88)

    def lambda_BE95():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BE95)

    ChrTalk(
        0x103,
        "#11P#00201FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10707F...Others are coming!\x02",
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

    def lambda_C0DE():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C0DE)

    def lambda_C0EB():
        TurnDirection(0xFE, 0x28, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C0EB)

    def lambda_C0F8():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C0F8)

    def lambda_C105():
        TurnDirection(0xFE, 0x29, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C105)

    def lambda_C112():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C112)

    def lambda_C11F():
        TurnDirection(0xFE, 0x2A, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C11F)

    def lambda_C12C():
        TurnDirection(0xFE, 0x2C, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C12C)
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
        "#5P#00311FTsk...this is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10110FKh...\x01",
            "We have to break through somehow!\x02",
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

    def lambda_C255():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C255)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x28, 0x1, 1300, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x28, 0x3)
    Sleep(50)
    SetChrChipByIndex(0x29, 0x14)
    SetChrSubChip(0x29, 0x0)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C2D0():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C2D0)
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

    def lambda_C3C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C3C3)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C3E8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3E8)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C410():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C410)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C435():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C435)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C45D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C45D)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C482():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C482)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_C4A7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C4A7)
    Sleep(1000)

    def lambda_C4B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C4B7)

    def lambda_C4C4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C4C4)

    def lambda_C4D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_C4D1)

    def lambda_C4DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_C4DE)

    def lambda_C4EB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_C4EB)
    OP_68(14800, 1000, -3800, 2000)
    MoveCamera(45, 17, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1)
    SetChrSubChip(0x1F, 0x0)

    def lambda_C52D():
        OP_96(0xFE, 0x3AFC, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C52D)

    def lambda_C547():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_C547)
    Sleep(200)
    SetChrChipByIndex(0x10A, 0x3)
    SetChrSubChip(0x10A, 0x0)

    def lambda_C563():
        OP_96(0xFE, 0x38A4, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C563)

    def lambda_C57D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C57D)
    WaitChrThread(0x1F, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    WaitChrThread(0x10A, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#6P#NChief...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00102F#6P#NMr. Dudley too...!\x02",
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
            "#3465V#30WWe'll talk later!\x01",
            "Follow us!\x02",
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
        "#00002F#6P#NYes...!!\x02",
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

    def lambda_C920():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C920)
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

    def lambda_C97A():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C97A)
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
            "Afterwards, Lloyd and the others ran\x01",
            "through a complicated route in the city\x01",
            "areas covered in the bluish mist...\x02\x03",
            "And from a part of Downtown,\x01",
            "they reached the Geofront D-Division.\x07\x00\x02",
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

    # Function_84_B61A end

    def Function_85_CAAF(): pass

    label("Function_85_CAAF")


    def lambda_CAB4():
        OP_95(0xFE, 12000, 0, -6200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CAB4)
    WaitChrThread(0xFE, 1)

    def lambda_CAD2():
        OP_95(0xFE, 26000, 0, -6200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CAD2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_CAAF end

    def Function_86_CAEC(): pass

    label("Function_86_CAEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBDB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CBD3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4B(0xFE, 0x1)
    OP_4B(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_CB3B():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CB3B)
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

    label("loc_CBD3")

    Sleep(300)
    Jump("Function_86_CAEC")

    label("loc_CBDB")

    Return()

    # Function_86_CAEC end

    def Function_87_CBDC(): pass

    label("Function_87_CBDC")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_CC0D():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CC0D)
    Sleep(1000)
    Return()

    # Function_87_CBDC end

    def Function_88_CC25(): pass

    label("Function_88_CC25")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1200, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_CC73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CCF4")
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
    Jump("loc_CC73")

    label("loc_CCF4")

    Return()

    # Function_88_CC25 end

    def Function_89_CCF5(): pass

    label("Function_89_CCF5")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(987, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_CD43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDFB")
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
    Jump("loc_CD43")

    label("loc_CDFB")

    Return()

    # Function_89_CCF5 end

    def Function_90_CDFC(): pass

    label("Function_90_CDFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE15")
    Sound(501, 0, 100, 0)
    Sleep(1500)
    Jump("Function_90_CDFC")

    label("loc_CE15")

    Return()

    # Function_90_CDFC end

    def Function_91_CE16(): pass

    label("Function_91_CE16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE47")
    SetChrChipByIndex(0xFE, 0x15)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1000, 0x0, 0x5)
    Jump("Function_91_CE16")

    label("loc_CE47")

    Return()

    # Function_91_CE16 end

    def Function_92_CE48(): pass

    label("Function_92_CE48")

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

    # Function_92_CE48 end

    def Function_93_CE8F(): pass

    label("Function_93_CE8F")

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

    # Function_93_CE8F end

    def Function_94_CED6(): pass

    label("Function_94_CED6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF2A")
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
    Jump("Function_94_CED6")

    label("loc_CF2A")

    Return()

    # Function_94_CED6 end

    def Function_95_CF2B(): pass

    label("Function_95_CF2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF7F")
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
    Jump("Function_95_CF2B")

    label("loc_CF7F")

    Return()

    # Function_95_CF2B end

    def Function_96_CF80(): pass

    label("Function_96_CF80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CFD4")
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
    Jump("Function_96_CF80")

    label("loc_CFD4")

    Return()

    # Function_96_CF80 end

    def Function_97_CFD5(): pass

    label("Function_97_CFD5")

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

    # Function_97_CFD5 end

    def Function_98_D200(): pass

    label("Function_98_D200")

    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x28, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_D22E():
        OP_95(0xFE, -3200, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_D22E)
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

    def lambda_D2E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_D2E8)
    WaitChrThread(0x28, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_98_D200 end

    def Function_99_D2FC(): pass

    label("Function_99_D2FC")

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

    def lambda_D36C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_D36C)
    WaitChrThread(0x29, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_99_D2FC end

    def Function_100_D380(): pass

    label("Function_100_D380")

    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2A, 0x20)
    BeginChrThread(0xFE, 0, 0, 76)

    def lambda_D3AE():
        OP_95(0xFE, 9900, 0, 7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D3AE)
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

    def lambda_D45E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_D45E)
    WaitChrThread(0x2A, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_100_D380 end

    def Function_101_D472(): pass

    label("Function_101_D472")

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
            "You always, always do whatever it pleases you.\x02\x03",
            "You don't even know\x01",
            "what kind of place\x01",
            "this Crossbell is.\x02\x03",
            "#12406FI'd wish you bore in mind\x01",
            "your own position a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13902FHmph, did I cause you trouble, perhaps?\x02\x03",
            "#13904FHowever, before I become unable to stir about,\x01",
            "I wanted to have a look at the city no matter what.\x02\x03",
            "Thanks to that, I somehow\x01",
            "have a feeling I understand why\x01",
            "this place is called "Demon City".\x02\x03",
            "#13908F...It appears that even "he"\x01",
            "is moving behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400F...Hm.\x01",
            "It seems you found something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13900FHmph, thanks to you, Mueller, I\x01",
            "also had an interesting encounter.\x02\x03",
            "#13905F...Oh, by the way, how did\x01",
            "things go on your end?\x02\x03",
            "#13904FSomeone like you have\x01",
            "made things advance cleverly\x01",
            "even in my absence, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        (
            "#12P#12400FYes, I already took contact.\x02\x03",
            "#12406FAfter all, because of you\x01",
            "we're a bit behind schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x40,
        (
            "#13904FHmph, then, let's make haste.\x02\x03",
            "#13900FIt's no good making the\x01",
            "lovely ladies wait.\x02",
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
            "Quest [Search for Musician] \x07\x00",
            "completed!\x02",
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

    # Function_101_D472 end

    def Function_102_D9A3(): pass

    label("Function_102_D9A3")

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

    def lambda_DB8A():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_DB8A)
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

    def lambda_DC1C():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_DC1C)
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

    def lambda_DCAB():
        OP_9B(0x1, 0xFE, 0x0, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_DCAB)
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
        "#5PAah, shut up ya small fries!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2E,
        "Yuri",
        "#5PReggie, shake them off!\x02",
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

    def lambda_DE0C():
        OP_96(0x2E, 0x2F26, 0x0, 0x88B8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_DE0C)
    Sleep(1500)
    StopSound(975, 1000, 100)
    Sleep(1000)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_102_D9A3 end

    def Function_103_DE3B(): pass

    label("Function_103_DE3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    OP_68(4270, -700, 10240, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DE9A")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_DED9")

    label("loc_DE9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DEBC")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_DED9")

    label("loc_DEBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DED9")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_DED9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E023")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x104, 15940, 0, -2710, 270)

    def lambda_DFB5():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DFB5)

    def lambda_DFCF():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DFCF)
    Sleep(100)

    def lambda_DFEC():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DFEC)
    Sleep(50)

    def lambda_E009():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E009)
    Jump("loc_E1C6")

    label("loc_E023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E0F7")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x109, 15940, 0, -2710, 270)

    def lambda_E089():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E089)

    def lambda_E0A3():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0A3)
    Sleep(100)

    def lambda_E0C0():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0C0)
    Sleep(50)

    def lambda_E0DD():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E0DD)
    Jump("loc_E1C6")

    label("loc_E0F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E1C6")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 14440, 0, -3610, 270)
    SetChrPos(0x102, 14440, 0, -3010, 270)
    SetChrPos(0x101, 15640, 0, -3910, 270)
    SetChrPos(0x105, 15940, 0, -2710, 270)

    def lambda_E15D():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E15D)

    def lambda_E177():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E177)
    Sleep(100)

    def lambda_E194():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E194)
    Sleep(50)

    def lambda_E1B1():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E1B1)

    label("loc_E1C6")

    OP_68(9660, 1900, -4450, 3000)
    MoveCamera(47, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        "So this is Central Square.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "As expected from being a principal\x01",
            "street, it's quite lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, even department store Times you were\x01",
            "mentioning, Shing, is within a stone's throw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FShould we go there immediately?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PHmm, well, I'll leave\x01",
            "everything to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI'm just happy by\x01",
            "staying near\x01",
            "Miss Elie like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, geez, we understood\x01",
            "that very well already.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E41C")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302FWell, anyway, \x01",
            "Should we swing by it then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4C7")

    label("loc_E41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E480")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FWell, anyway, should we have a\x01",
            "look around as much as possible?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4C7")

    label("loc_E480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E4C7")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FWell, anyway.\x01",
            "Let's tour it thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4C7")

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

    # Function_103_DE3B end

    def Function_104_E516(): pass

    label("Function_104_E516")

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
            "What happened to have you so flustered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're currently chasing\x01",
            "after a certain person...\x02\x03",
            "#00001FHaven't you seen a black Reinford\x01",
            "made wagon passing by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "A black wagon...?\x02\x03",
            "Yes, thinking about it, I feel like such\x01",
            "a vehicle passed by a little while ago.\x02\x03",
            "If I remember correctly, it went\x01",
            "towards the East Street direction...\x02",
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
            "It wasn't towards West Street,\x01",
            "headed to the Empire region?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "No, I'm sure I saw it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHm...it seems his destination\x01",
            "was the Republic region, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAn Imperial guiding a\x01",
            "Reinford made wagon...\x02\x03",
            "#00200FI thought that if he wanted to run away he\x01",
            "would have gone to the Empire region...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, it seems we can't deal\x01",
            "with him with ordinary means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAnyway, thank you.\x01",
            "You've been of help, Frantz.\x02\x03",
            "#00001F...It's better to hurry up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYes, if we're chasing after\x01",
            "him, it would be better to\x01",
            "use an orbal vehicle.\x02\x03",
            "#10101FLet's go quickly to\x01",
            "Tangram Gate!\x02",
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

    # Function_104_E516 end

    def Function_105_EACC(): pass

    label("Function_105_EACC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F186")
    Fade(500)
    OP_68(-19610, -6700, -24820, 0)
    MoveCamera(9, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10990, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EBCE")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x104, -18650, -8200, -21550, 225)

    def lambda_EB74():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_EB74)

    def lambda_EB89():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB89)
    Sleep(100)

    def lambda_EBA1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EBA1)
    Sleep(50)

    def lambda_EBB9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EBB9)
    Jump("loc_ED21")

    label("loc_EBCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EC7A")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x109, -18650, -8200, -21550, 225)

    def lambda_EC20():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_EC20)

    def lambda_EC35():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC35)
    Sleep(100)

    def lambda_EC4D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC4D)
    Sleep(50)

    def lambda_EC65():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EC65)
    Jump("loc_ED21")

    label("loc_EC7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ED21")
    SetChrPos(0x1A2, -18930, -8200, -23410, 225)
    SetChrPos(0x102, -19530, -8200, -22810, 225)
    SetChrPos(0x101, -17620, -8200, -22890, 225)
    SetChrPos(0x105, -18650, -8200, -21550, 225)

    def lambda_ECCC():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_ECCC)

    def lambda_ECE1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ECE1)
    Sleep(100)

    def lambda_ECF9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECF9)
    Sleep(50)

    def lambda_ED11():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ED11)

    label("loc_ED21")

    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PW-What's with that huge dog...?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 3, 0, 106)
    OP_68(-23520, -6700, -24320, 3000)
    MoveCamera(51, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13660, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EDE6")

    def lambda_EDB6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EDB6)
    Sleep(50)

    def lambda_EDC6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDC6)
    Sleep(50)

    def lambda_EDD6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EDD6)
    Sleep(300)
    Jump("loc_EE5D")

    label("loc_EDE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EE24")

    def lambda_EDF4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EDF4)
    Sleep(50)

    def lambda_EE04():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE04)
    Sleep(50)

    def lambda_EE14():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EE14)
    Sleep(300)
    Jump("loc_EE5D")

    label("loc_EE24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EE5D")

    def lambda_EE32():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE32)
    Sleep(50)

    def lambda_EE42():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE42)
    Sleep(50)

    def lambda_EE52():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE52)
    Sleep(300)

    label("loc_EE5D")

    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FZeit...in such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, maybe he wanted\x01",
            "to breath the outside air.\x02",
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
        "#6P#00105FShing...is something wrong?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EF7A")
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00309FAh haa, are you\x01",
            "scared of Zeit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F046")

    label("loc_EF7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EFFE")
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102FAhaha, it looks\x01",
            "he's scared of Zeit.\x02\x03",
            "#10104F(Since at first I was like\x01",
            "him too, I can relate.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F046")

    label("loc_EFFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F046")
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, it appears you\x01",
            "see Zeit as scary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F046")


    ChrTalk(
        0x1A2,
        "W-What're you saying...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "T-There's nothing I'm\x01",
            "scared of, you see!\x02",
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
            "Alright, guys. I'm tired of this\x01",
            "place, so let's go to the next one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, got it.\x02\x03",
            "#00012F(Ha ha, it's evidently false courage,\x01",
            "but he's got some admirable guts.)\x02",
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
    Jump("loc_F1FD")

    label("loc_F186")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "H-Hey... I'm done with this,\x01",
            "so let's go back to the square.\x02",
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

    label("loc_F1FD")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17980, -8200, -22080, 44)
    EventEnd(0x4)
    Return()

    # Function_105_EACC end

    def Function_106_F215(): pass

    label("Function_106_F215")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F245")

    def lambda_F225():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F225)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_106_F215")

    label("loc_F245")

    Return()

    # Function_106_F215 end

    def Function_107_F246(): pass

    label("Function_107_F246")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F69B")
    OP_68(90, 4400, 25340, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16660, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F2F8")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F397")

    label("loc_F2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F34A")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F397")

    label("loc_F34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F397")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F397")

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
            "#00000FWell then, we arrived at the\x01",
            "the department store...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F4F7")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FIs there any other places you\x01",
            "want to take the brat to?\x02\x03",
            "#00303FOnce we get inside, we\x01",
            "won't have anymore time to\x01",
            "guide 'im around outside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F653")

    label("loc_F4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F5A8")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10105FAren't there any other places\x01",
            "you want to take Shing to?\x02\x03",
            "#10103FOnce we enter in, we\x01",
            "won't have anymore time to\x01",
            "guide him around outside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F653")

    label("loc_F5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F653")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FAren't there any other places\x01",
            "you want to take Shing to, hm?\x02\x03",
            "Once we enter inside, we\x01",
            "won't have anymore time to\x01",
            "guide him around outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F653")


    ChrTalk(
        0x1A2,
        (
            "#6PWhat do you want to do?\x01",
            "I'll leave the decision to you.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 108)
    Jump("loc_F99A")

    label("loc_F69B")

    OP_68(10, 400, 21490, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15710, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F71B")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x104, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F7BA")

    label("loc_F71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F76D")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x109, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)
    Jump("loc_F7BA")

    label("loc_F76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F7BA")
    SetChrPos(0x101, -720, 0, 18470, 0)
    SetChrPos(0x105, 580, 0, 18180, 0)
    SetChrPos(0x1A2, -360, 0, 16800, 0)
    SetChrPos(0x102, 230, 0, 16780, 0)

    label("loc_F7BA")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F86A")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FShouldn't we enter the department store?\x02\x03",
            "#00303FOnce we get inside, we\x01",
            "won't have anymore time\x01",
            "to guide him around outside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F995")

    label("loc_F86A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F908")
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FShould we enter the department store?\x02\x03",
            "#10103FOnce we enter in, we\x01",
            "won't have anymore time\x01",
            "to guide him around outside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F995")

    label("loc_F908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F995")
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FIsn't it time to enter inside?\x02\x03",
            "Once we enter inside, we\x01",
            "won't have anymore time\x01",
            "to guide him around outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F995")

    Call(0, 108)
    EventEnd(0x5)

    label("loc_F99A")

    Return()

    # Function_107_F246 end

    def Function_108_F99B(): pass

    label("Function_108_F99B")

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
            "Enter the Department Store\x01",      # 0
            "Show Him Other Places\x01",           # 1
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
        (0, "loc_FA1C"),
        (1, "loc_FA78"),
        (SWITCH_DEFAULT, "loc_FAFD"),
    )


    label("loc_FA1C")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FLet's see, I think we showed\x01",
            "him enough for now.\x01",
            "Let's enter.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 109)
    Jump("loc_FAFD")

    label("loc_FA78")

    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FLet's see, maybe there are\x01",
            "other places we could show him.\x02\x03",
            "#00000FLet's postpone entering.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 6)
    Jump("loc_FAFD")

    label("loc_FAFD")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -180, 0, 15990, 180)
    EventEnd(0x5)
    Return()

    # Function_108_F99B end

    def Function_109_FB15(): pass

    label("Function_109_FB15")

    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("chr/ch02900.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)

    ChrTalk(
        0x1A2,
        "#6PAlright, it's decided then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, then let's\x01",
            "enter immediately.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13670, 1900, 7350, 0)
    MoveCamera(22, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FC4E")
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
    Jump("loc_FD79")

    label("loc_FC4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FCE6")
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
    Jump("loc_FD79")

    label("loc_FCE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FD79")
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

    label("loc_FD79")

    OP_0D()
    Sound(100, 0, 40, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FE4A")

    def lambda_FDA6():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FDA6)
    Sleep(100)

    def lambda_FDBE():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FDBE)
    Sleep(500)

    def lambda_FDD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FDD6)
    Sleep(200)

    def lambda_FDEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FDEA)

    def lambda_FDFB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FDFB)

    def lambda_FE10():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE10)
    Sleep(1000)

    def lambda_FE28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FE28)

    def lambda_FE39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FE39)
    Jump("loc_FFA9")

    label("loc_FE4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FEFC")

    def lambda_FE58():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE58)
    Sleep(100)

    def lambda_FE70():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FE70)
    Sleep(500)

    def lambda_FE88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FE88)
    Sleep(200)

    def lambda_FE9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FE9C)

    def lambda_FEAD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FEAD)

    def lambda_FEC2():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEC2)
    Sleep(1000)

    def lambda_FEDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FEDA)

    def lambda_FEEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FEEB)
    Jump("loc_FFA9")

    label("loc_FEFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FFA9")

    def lambda_FF0A():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF0A)
    Sleep(100)

    def lambda_FF22():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FF22)
    Sleep(500)

    def lambda_FF3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FF3A)
    Sleep(200)

    def lambda_FF4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FF4E)

    def lambda_FF5F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_FF5F)

    def lambda_FF74():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF74)
    Sleep(1000)

    def lambda_FF8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_FF8C)

    def lambda_FF9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FF9D)

    label("loc_FFA9")

    WaitChrThread(0x102, 1)
    Sound(100, 0, 40, 0)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_101BC")

    ChrTalk(
        0x36,
        (
            "#10100FYes, it seems they\x01",
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
        "#11P#10105FIs something wrong, Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10301FYes. While we were guarding their backs,\x01",
            "I felt like I sensed some presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10105FPresence...\x01",
            "Maybe the Heiyue men?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#10303FWell, it would be natural\x01",
            "to think it's them, but...\x02\x03",
            "#10300FWell, I can't tell\x01",
            "specifically.\x02\x03",
            "At any rate, let's enter the\x01",
            "department store in a bit too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10103FY-Yes...understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1062A")

    label("loc_101BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1041E")

    ChrTalk(
        0x37,
        (
            "#10300FHm, it seems they\x01",
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
        "#11P#10305FIs something wrong, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FYeah. While we were guardin' their backs, \x01",
            "I got a feelin' like I sensed some presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FHu hu, you too, eh...?\x01",
            "Somehow, I sensed it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FYeah, probably the Heiyue\x01",
            "lot keepin' an eye on us...\x02\x03",
            "#00301FHowever, it wasn't\x01",
            "only that...\x02\x03",
            "#00306FWell, I can't tell\x01",
            "more specifically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#11P#10304FHu hu, I agree with you.\x02\x03",
            "#10300FAnyway, for now we can only\x01",
            "keep watching the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#00303FYeah, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1062A")

    label("loc_1041E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1062A")

    ChrTalk(
        0x36,
        (
            "#10100FYes, it seems they\x01",
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
        "#11P#10105FIs something wrong, senior Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00301FYeah. While we were guardin' their backs,\x01",
            "I got a feelin' like I sensed some presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#11P#10101FPresence...\x01",
            "Maybe the Heiyue men?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#00303FWell, naturally I'd\x01",
            "think about 'em, but...\x02\x03",
            "#00306FHonestly speakin',\x01",
            "I don't know specifically.\x02\x03",
            "#00300FAt any rate, let's enter the\x01",
            "department store in a bit too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#10101FY-Yes...understood.\x02",
    )

    CloseMessageWindow()

    label("loc_1062A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0170", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_109_FB15 end

    def Function_110_10642(): pass

    label("Function_110_10642")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1071D")

    ChrTalk(
        0x1A2,
        (
            "Hmm, is the department\x01",
            "store that way...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, no, you'll go to the\x01",
            "train station this way...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Then, let's go back at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yeah...sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1076E")

    label("loc_1071D")


    ChrTalk(
        0x101,
        (
            "#00000FThere's no need to go to Station\x01",
            "Street. Let's return to the square.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1076E")

    SetChrPos(0x0, 3740, 0, -19810, 0)
    EventEnd(0x4)
    Return()

    # Function_110_10642 end

    def Function_111_10782(): pass

    label("Function_111_10782")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10876")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FHey, Lloyd... If we proceed on,\x01",
            "we'll be at the Governmental District.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FYou're right. Let's retrace our steps.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Wasn't the department store this way?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_108A9")

    label("loc_10876")


    ChrTalk(
        0x101,
        "#00000FThis way is the Governmental District.\x02",
    )

    CloseMessageWindow()

    label("loc_108A9")

    SetChrPos(0x0, 13290, 0, 26680, 180)
    EventEnd(0x4)
    Return()

    # Function_111_10782 end

    def Function_112_108BD(): pass

    label("Function_112_108BD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E8")
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
            "Could you be able to enter\x01",
            "Back Street from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, you know a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...For now though, we don't\x01",
            "have any business there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "(Hm, so it's there that the Revache's remnants\x01",
            "are, just like Cao and the others said...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10A1F")

    label("loc_109E8")


    ChrTalk(
        0x101,
        "#00000FWe don't have any business in Back Street.\x02",
    )

    CloseMessageWindow()

    label("loc_10A1F")

    SetChrPos(0x0, -14110, -10, 14420, 135)
    EventEnd(0x4)
    Return()

    # Function_112_108BD end

    def Function_113_10A33(): pass

    label("Function_113_10A33")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWest Street is further ahead.\x02\x03",
            "#00003FI don't want to go too far\x01",
            "off from the department\x01",
            "store. Let's go back.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_113_10A33 end

    SaveToFile()

Try(main)
