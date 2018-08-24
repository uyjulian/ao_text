from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2030.bin",                # FileName
        "r2030",                    # MapName
        "r2030",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x13,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 4, 0, 5],
    )

    BuildStringList((
        "r2030",                  # 0
        "Nepenthes Kids",         # 1
        "Nepenthes Kids",         # 2
        "鉄鋼ドリュー",           # 3
        "鉄鋼ドリュー",           # 4
        "Humming Gator",          # 5
        "バス",                   # 6
        "Man in White Robe",      # 7
        "Boy",                    # 8
        "CGF Member",             # 9
        "CGF Member",             # 10
        "CGF Member",             # 11
        "CGF Member",             # 12
        "CGF Member",             # 13
        "CGF Member",             # 14
        "CGF Member",             # 15
        "Jaeger",                 # 16
        "Jaeger",                 # 17
        "Jaeger",                 # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Shirley",                # 21
        "Military Beast",         # 22
        "Military Beast",         # 23
        "Military Beast",         # 24
        "Military Beast",         # 25
        "Military Beast",         # 26
        "車",                     # 27
        "新型装甲車",             # 28
        "メルカバ玖号機",         # 29
        "メルカバ光学迷彩",       # 30
        "メルカバ影",             # 31
        "SE制御",                 # 32
        "br2000",                 # 33
        "br2000",                 # 34
        "br2000",                 # 35
        "br2000",                 # 36
        "br2000",                 # 37
        "br2000",                 # 38
        "br2000",                 # 39
        "br2000",                 # 40
        "br2000",                 # 41
        "To Crossbell City",      # 42
        "To Doll Studio",         # 43
        "To Mining Town Mainz",   # 44
    ))

    ATBonus("ATBonus_90C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_92C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B07B", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_B08B", 5,   2,   0,   3,   0,   3,   2)
    Sepith("Sepith_B073", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_B083", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_B06B", 6,   0,   0,   3,   2,   4,   0)

    MonsterBattlePostion("MonsterBattlePostion_94C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_950", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_954", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_958", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_95C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_960", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_964", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_968", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_9D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_9D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_9D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_9DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_9E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_9E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_96C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_970", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_974", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_978", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_97C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_980", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_984", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_988", 8, 14, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_AB4", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_B07B", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C18", 0x0010, 52, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_B08B", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_B50", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_B073", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_CE0", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_B083", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_9EC", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_B06B", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_E74", 0x0000, 50, 6, 45, 0, 1, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "ms65500.dat", "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7451", "ed7453", "ATBonus_90C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DA8", 0x0C10, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms77400.dat", "ms77400.dat", "ms77400.dat", 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7453", "ed7453", "ATBonus_90C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DEC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7453", "ed7453", "ATBonus_90C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E30", 0x0042, 3, 6, 45, 3, 3, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7453", "ed7453", "ATBonus_92C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch77450.itc",               # 16
        "monster/ch77450.itc",               # 17
        "monster/ch69450.itc",               # 18
        "monster/ch69450.itc",               # 19
        "monster/ch76050.itc",               # 1A
        "monster/ch76051.itc",               # 1B
    ))

    DeclNpc(4294931017, 9,       57580,   270,  484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294893087, 0,       149949,  270,  484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294931017, 1009,    57580,   270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294893087, 1000,    149949,  270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294917296, 6500,    69500,   0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294960216, 38670,   1500,    0x1010000,    "BattleInfo_AB4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294915856, 65480,   6000,    0x1010000,    "BattleInfo_C18", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294933086, 55840,   0,       0x1010000,    "BattleInfo_B50", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294930296, 96550,   600,     0x1010000,    "BattleInfo_CE0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294932286, 114720,  0,       0x1010000,    "BattleInfo_CE0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(2700,    112600,  3810,    0x1010000,    "BattleInfo_9EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294894286, 151070,  0,       0x1010000,    "BattleInfo_AB4", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 25,  -29.84000015258789,    82.05000305175781,     -1.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.4919999837875366,    -16.410001754760742,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 41,  -15.0,                 110.0,                 -1.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.0,                   -7.3333330154418945,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 73,  -15.0,                 110.0,                 -1.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.0,                   -7.3333330154418945,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 80,  -43.689998626708984,   125.19000244140625,    -1.0,                  625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   23.883243560791016,    -5.7629170417785645,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 81,  -14.199999809265137,   31.329999923706055,    -1.0,                  1406.25,               [-4.265052311325235e-08, 0.20000000298023224,   0.0,                   0.0,                   -0.06666666269302368,  -1.2795156578704336e-07, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0886659622192383,    2.8400039672851562,    0.20000000298023224,   1.0])

    DeclActor(4294941296, 0,       116600,  1500,    4294941296, 1500,    116600,  0x007C, 0,  18, 0x0000)
    DeclActor(4294917296, 6000,    69500,   1200,    4294917296, 7000,    69500,   0x007C, 0,  6,  0x0000)
    DeclActor(4294931016, 10,      57580,   1200,    4294931016, 10,      57580,   0x007C, 0,  7,  0x0000)
    DeclActor(4294893086, 0,       149950,  1200,    4294893086, 0,       149950,  0x007C, 0,  8,  0x0000)
    DeclActor(4294942296, 0,       94440,   1500,    4294942296, 2000,    94440,   0x007C, 0,  9,  0x0000)
    DeclActor(4294943246, 0,       93390,   1200,    4294943246, 2000,    93390,   0x007C, 0,  9,  0x0000)
    DeclActor(4294907936, 0,       145870,  1200,    4294917866, 4294964296, 154830,  0x007C, 0,  19, 0x0000)
    DeclActor(4294909146, 6000,    65950,   1800,    4294908496, 6500,    65600,   0x007C, 0,  17, 0x0000)
    DeclActor(4294965486, 0,       23520,   1500,    4294965486, 2000,    23520,   0x007C, 0,  9,  0x0000)
    DeclActor(4294928666, 0,       101340,  1500,    4294928666, 1700,    101340,  0x007C, 0,  82, 0x0000)

    PlaceName(-1.0, 0.0, -15.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(38.25, 0.0, 116.25, 0x0000, 0x0000, "To Doll Studio")
    PlaceName(-86.0, 0.0, 235.0, 0x0000, 0x0000, "To Mining Town Mainz")
    PlaceName(-26.0, 0.0, 116.5999984741211, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_107C",         # 00, 0
        "Function_1_109B",         # 01, 1
        "Function_2_10BA",         # 02, 2
        "Function_3_10D9",         # 03, 3
        "Function_4_11BD",         # 04, 4
        "Function_5_17D8",         # 05, 5
        "Function_6_1DC6",         # 06, 6
        "Function_7_1FE1",         # 07, 7
        "Function_8_233D",         # 08, 8
        "Function_9_2699",         # 09, 9
        "Function_10_29D6",        # 0A, 10
        "Function_11_29DA",        # 0B, 11
        "Function_12_2C0C",        # 0C, 12
        "Function_13_2D3F",        # 0D, 13
        "Function_14_2E52",        # 0E, 14
        "Function_15_2E88",        # 0F, 15
        "Function_16_2ED9",        # 10, 16
        "Function_17_2F6D",        # 11, 17
        "Function_18_3016",        # 12, 18
        "Function_19_306A",        # 13, 19
        "Function_20_3131",        # 14, 20
        "Function_21_3B1E",        # 15, 21
        "Function_22_3B80",        # 16, 22
        "Function_23_3BF0",        # 17, 23
        "Function_24_3C0C",        # 18, 24
        "Function_25_3C52",        # 19, 25
        "Function_26_4174",        # 1A, 26
        "Function_27_4184",        # 1B, 27
        "Function_28_4197",        # 1C, 28
        "Function_29_41AA",        # 1D, 29
        "Function_30_41BD",        # 1E, 30
        "Function_31_47F3",        # 1F, 31
        "Function_32_48A0",        # 20, 32
        "Function_33_48DE",        # 21, 33
        "Function_34_491F",        # 22, 34
        "Function_35_4960",        # 23, 35
        "Function_36_49D3",        # 24, 36
        "Function_37_49F2",        # 25, 37
        "Function_38_50D6",        # 26, 38
        "Function_39_519A",        # 27, 39
        "Function_40_51FC",        # 28, 40
        "Function_41_520C",        # 29, 41
        "Function_42_628D",        # 2A, 42
        "Function_43_6821",        # 2B, 43
        "Function_44_6855",        # 2C, 44
        "Function_45_68A5",        # 2D, 45
        "Function_46_68F5",        # 2E, 46
        "Function_47_690F",        # 2F, 47
        "Function_48_7F71",        # 30, 48
        "Function_49_7FC1",        # 31, 49
        "Function_50_7FDA",        # 32, 50
        "Function_51_7FF3",        # 33, 51
        "Function_52_8077",        # 34, 52
        "Function_53_80EA",        # 35, 53
        "Function_54_816E",        # 36, 54
        "Function_55_81E1",        # 37, 55
        "Function_56_8254",        # 38, 56
        "Function_57_82BE",        # 39, 57
        "Function_58_82CE",        # 3A, 58
        "Function_59_85D1",        # 3B, 59
        "Function_60_85F6",        # 3C, 60
        "Function_61_861B",        # 3D, 61
        "Function_62_8640",        # 3E, 62
        "Function_63_8665",        # 3F, 63
        "Function_64_868A",        # 40, 64
        "Function_65_8AB4",        # 41, 65
        "Function_66_8AC4",        # 42, 66
        "Function_67_8E71",        # 43, 67
        "Function_68_90C4",        # 44, 68
        "Function_69_9C7D",        # 45, 69
        "Function_70_9CC2",        # 46, 70
        "Function_71_9D16",        # 47, 71
        "Function_72_9D7B",        # 48, 72
        "Function_73_9D96",        # 49, 73
        "Function_74_A3E0",        # 4A, 74
        "Function_75_A40E",        # 4B, 75
        "Function_76_A43C",        # 4C, 76
        "Function_77_A456",        # 4D, 77
        "Function_78_AE0A",        # 4E, 78
        "Function_79_AE2D",        # 4F, 79
        "Function_80_AE47",        # 50, 80
        "Function_81_AF52",        # 51, 81
        "Function_82_AFCA",        # 52, 82
    ))


    def Function_0_107C(): pass

    label("Function_0_107C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_109A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_107C")

    label("loc_109A")

    Return()

    # Function_0_107C end

    def Function_1_109B(): pass

    label("Function_1_109B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10B9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_109B")

    label("loc_10B9")

    Return()

    # Function_1_109B end

    def Function_2_10BA(): pass

    label("Function_2_10BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10D8")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_10BA")

    label("loc_10D8")

    Return()

    # Function_2_10BA end

    def Function_3_10D9(): pass

    label("Function_3_10D9")

    SetMapObjFlags(0x4, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_END)), "loc_112F")
    Jump("loc_11BC")

    label("loc_112F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1167")
    SetMapObjFlags(0x1, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    Jump("loc_11BC")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_1175")
    Jump("loc_11BC")

    label("loc_1175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11A7")
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    Jump("loc_11BC")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_END)), "loc_11BC")
    ClearMapObjFlags(0x4, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)

    label("loc_11BC")

    Return()

    # Function_3_10D9 end

    def Function_4_11BD(): pass

    label("Function_4_11BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1661")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124A")
    SetScenarioFlags(0x38, 0)

    label("loc_124A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1260")
    SetScenarioFlags(0x38, 1)

    label("loc_1260")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1276")
    SetScenarioFlags(0x38, 2)

    label("loc_1276")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128C")
    SetScenarioFlags(0x38, 3)

    label("loc_128C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A2")
    SetScenarioFlags(0x38, 4)

    label("loc_12A2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B8")
    SetScenarioFlags(0x38, 5)

    label("loc_12B8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CE")
    SetScenarioFlags(0x38, 6)

    label("loc_12CE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E4")
    SetScenarioFlags(0x38, 7)

    label("loc_12E4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FA")
    SetScenarioFlags(0x39, 0)

    label("loc_12FA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1310")
    SetScenarioFlags(0x39, 1)

    label("loc_1310")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1326")
    SetScenarioFlags(0x39, 2)

    label("loc_1326")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133C")
    SetScenarioFlags(0x39, 3)

    label("loc_133C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1352")
    SetScenarioFlags(0x39, 4)

    label("loc_1352")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1368")
    SetScenarioFlags(0x39, 5)

    label("loc_1368")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137E")
    SetScenarioFlags(0x39, 6)

    label("loc_137E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1394")
    SetScenarioFlags(0x39, 7)

    label("loc_1394")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AA")
    SetScenarioFlags(0x3A, 0)

    label("loc_13AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C0")
    SetScenarioFlags(0x3A, 1)

    label("loc_13C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D6")
    SetScenarioFlags(0x3A, 2)

    label("loc_13D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EC")
    SetScenarioFlags(0x3A, 3)

    label("loc_13EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1402")
    SetScenarioFlags(0x3A, 4)

    label("loc_1402")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1418")
    SetScenarioFlags(0x3A, 5)

    label("loc_1418")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142E")
    SetScenarioFlags(0x3A, 6)

    label("loc_142E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1444")
    SetScenarioFlags(0x3A, 7)

    label("loc_1444")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145A")
    SetScenarioFlags(0x3B, 0)

    label("loc_145A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1470")
    SetScenarioFlags(0x3B, 1)

    label("loc_1470")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1486")
    SetScenarioFlags(0x3B, 2)

    label("loc_1486")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149C")
    SetScenarioFlags(0x3B, 3)

    label("loc_149C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B2")
    SetScenarioFlags(0x3B, 4)

    label("loc_14B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C8")
    SetScenarioFlags(0x3B, 5)

    label("loc_14C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
    SetScenarioFlags(0x3B, 6)

    label("loc_14DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F4")
    SetScenarioFlags(0x3B, 7)

    label("loc_14F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150A")
    SetScenarioFlags(0x3D, 5)

    label("loc_150A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1520")
    SetScenarioFlags(0x3D, 6)

    label("loc_1520")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1536")
    SetScenarioFlags(0x3D, 7)

    label("loc_1536")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1571")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1661")

    label("loc_1571")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1594")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1661")

    label("loc_1594")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B7")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1661")

    label("loc_15B7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DA")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1661")

    label("loc_15DA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FD")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1661")

    label("loc_15FD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1620")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1661")

    label("loc_1620")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1643")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1661")

    label("loc_1643")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1661")
    SetScenarioFlags(0x3C, 7)

    label("loc_1661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1677")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B7")
    SetChrPos(0x0, -3510, 0, 21800, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 16)

    label("loc_16B7")

    Jump("loc_1721")

    label("loc_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EE")
    SetChrPos(0x0, -25760, 0, 94640, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 16)

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1721")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1721")
    SetChrPos(0x0, -24050, 0, 93390, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_1730")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 15)

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1744")
    ClearScenarioFlags(0x22, 0)
    Event(0, 20)
    Jump("loc_1795")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1758")
    ClearScenarioFlags(0x22, 1)
    Event(0, 30)
    Jump("loc_1795")

    label("loc_1758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_176C")
    ClearScenarioFlags(0x22, 2)
    Event(0, 37)
    Jump("loc_1795")

    label("loc_176C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1783")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 42)
    Jump("loc_1795")

    label("loc_1783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1795")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 0)
    Event(0, 47)

    label("loc_1795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C6")
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")
    Event(0, 64)
    Jump("loc_17C1")

    label("loc_17BE")

    Event(0, 58)

    label("loc_17C1")

    Jump("loc_17D7")

    label("loc_17C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D7")
    Event(0, 68)

    label("loc_17D7")

    Return()

    # Function_4_11BD end

    def Function_5_17D8(): pass

    label("Function_5_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17EA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17FE")
    OP_24(0x7A)
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1827")

    label("loc_17FE")

    SoundDistance(0x7A, 0xFFFF2C20, 0x0, 0x3087C, 0x2710, 0x13880, 0x64, 0x0)
    OP_E3(0xFFFFADBC, 0x0, 0x20E54)

    label("loc_1827")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A13")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1A85")
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    Jump("loc_1ABB")

    label("loc_1A85")

    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)

    label("loc_1ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B21")
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    SetMapObjFrame(0x15, "light", 0x0, 0x1)
    SetMapObjFrame(0x16, "light", 0x0, 0x1)

    label("loc_1B21")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B95")
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B90")
    OP_66(0x8, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0x2, 0x22)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x22, -1810, 0, 23520, 330)

    label("loc_1B90")

    Jump("loc_1BB7")

    label("loc_1B95")

    MiniGame(0x2F, 0x4, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_1BB7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1BE8")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C00")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1C00")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C18")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1C18")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C30")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C43")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1C43")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5B")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1C5B")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C83")
    ClearMapObjFlags(0x5, 0x4)
    OP_66(0x7, 0x1)

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1C96")
    ClearMapObjFlags(0x1C, 0x4)
    OP_66(0x7, 0x1)

    label("loc_1C96")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -49430, -3000, 154830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF3")
    OP_70(0x0, 0x0)
    Jump("loc_1CF7")

    label("loc_1CF3")

    OP_70(0x0, 0x1E)

    label("loc_1CF7")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D58")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -36280, 10, 57580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1D58")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DA4")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -74210, 0, 149950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1DA4")

    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x12, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_5_17D8 end

    def Function_6_1DC6(): pass

    label("Function_6_1DC6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F97")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC9")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1E23():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E23)

    def lambda_1E3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1E3D)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_E74", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1EAA"),
        (2, "loc_1EB9"),
        (1, "loc_1EC6"),
        (SWITCH_DEFAULT, "loc_1EC9"),
    )


    label("loc_1EAA")

    SetScenarioFlags(0x21B, 1)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1EC9")

    label("loc_1EB9")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1EC6")

    OP_B9(0x0)
    Return()

    label("loc_1EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6D, 1)"), scpexpr(EXPR_END)), "loc_1F22")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1F92")

    label("loc_1F22")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1F92")

    Jump("loc_1FD5")

    label("loc_1F97")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1FD5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1DC6 end

    def Function_7_1FE1(): pass

    label("Function_7_1FE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2198")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_2179")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2174")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2171")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2096():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2096)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2153")
    Call(1, 5)
    Jump("loc_216C")

    label("loc_2153")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2169")
    Call(1, 4)
    Jump("loc_216C")

    label("loc_2169")

    Call(1, 3)

    label("loc_216C")

    Jump("loc_2174")

    label("loc_2171")

    Call(1, 1)

    label("loc_2174")

    Jump("loc_218F")

    label("loc_2179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_218F")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_218F")

    TalkEnd(0xFF)
    Return()

    label("loc_2198")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_2322")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231D")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_231A")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_223F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_223F)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2315")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22FC")
    Call(1, 5)
    Jump("loc_2315")

    label("loc_22FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2312")
    Call(1, 4)
    Jump("loc_2315")

    label("loc_2312")

    Call(1, 3)

    label("loc_2315")

    Jump("loc_231D")

    label("loc_231A")

    Call(1, 1)

    label("loc_231D")

    Jump("loc_2338")

    label("loc_2322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2338")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2338")

    TalkEnd(0xFF)
    Return()

    # Function_7_1FE1 end

    def Function_8_233D(): pass

    label("Function_8_233D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24F4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_24D5")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D0")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_24CD")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23F2)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24AF")
    Call(1, 5)
    Jump("loc_24C8")

    label("loc_24AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24C5")
    Call(1, 4)
    Jump("loc_24C8")

    label("loc_24C5")

    Call(1, 3)

    label("loc_24C8")

    Jump("loc_24D0")

    label("loc_24CD")

    Call(1, 1)

    label("loc_24D0")

    Jump("loc_24EB")

    label("loc_24D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_24EB")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_24EB")

    TalkEnd(0xFF)
    Return()

    label("loc_24F4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_267E")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2679")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2676")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_259B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_259B)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2671")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2658")
    Call(1, 5)
    Jump("loc_2671")

    label("loc_2658")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_266E")
    Call(1, 4)
    Jump("loc_2671")

    label("loc_266E")

    Call(1, 3)

    label("loc_2671")

    Jump("loc_2679")

    label("loc_2676")

    Call(1, 1)

    label("loc_2679")

    Jump("loc_2694")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2694")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2694")

    TalkEnd(0xFF)
    Return()

    # Function_8_233D end

    def Function_9_2699(): pass

    label("Function_9_2699")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CB")
    SetScenarioFlags(0x31, 2)

    label("loc_26CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_270B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2700")
    Sound(2499, 255, 100, 0)
    Jump("loc_2706")

    label("loc_2700")

    Sound(3537, 255, 100, 0)

    label("loc_2706")

    Jump("loc_2711")

    label("loc_270B")

    Sound(3344, 255, 100, 0)

    label("loc_2711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2786")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2766"),
        (SWITCH_DEFAULT, "loc_2777"),
    )


    label("loc_2766")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2781")

    label("loc_2777")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2781")

    Jump("loc_29C3")

    label("loc_2786")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_27B8")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_27B8")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27EC"),
        (1, "loc_28F0"),
        (2, "loc_2981"),
        (SWITCH_DEFAULT, "loc_29B9"),
    )


    label("loc_27EC")

    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_74(0x2, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_281D")
    OP_70(0x2, 0x12C)
    OP_71(0x2, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_282D")

    label("loc_281D")

    OP_70(0x2, 0xF0)
    OP_71(0x2, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_282D")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2883")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2883")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A6")
    Sound(461, 0, 100, 0)

    label("loc_28A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28C6")
    OP_70(0x2, 0x14A)
    OP_71(0x2, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_28D6")

    label("loc_28C6")

    OP_70(0x2, 0x10E)
    OP_71(0x2, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_28D6")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x2, "light", 0x1, 0x1)
    OP_70(0x2, 0x0)
    Jump("loc_2711")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2962")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2925")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_293D")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2938")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_293D")

    label("loc_2938")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_293D")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_297C")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2972")
    OP_AF(0xFB)
    Jump("loc_297C")

    label("loc_2972")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_297C")

    Jump("loc_29C3")

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B4")

    label("loc_299A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_29AA")
    OP_AF(0xFB)
    Jump("loc_29B4")

    label("loc_29AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29B4")

    Jump("loc_29C3")

    label("loc_29B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29C3")

    Jump("loc_2711")

    label("loc_29C8")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_2699 end

    def Function_10_29D6(): pass

    label("Function_10_29D6")

    Call(1, 6)
    Return()

    # Function_10_29D6 end

    def Function_11_29DA(): pass

    label("Function_11_29DA")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC7")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus\x01",
            "stop sign, you can ride\x01",
            "the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to\x01",
            "various places the same way\x01",
            "you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_2AC7")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City North Exit\x01",      # 0
            "Mining Town Mainz\x01",              # 1
            "Cancel\x01",                         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5B")
    Call(0, 12)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2C04")

    label("loc_2B5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF3")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business in the\x01",
            "mining town area. Let's focus on\x01",
            "the accident investigation for now.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    label("loc_2BF3")

    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_2C04")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_11_29DA end

    def Function_12_2C0C(): pass

    label("Function_12_2C0C")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2D3B")
    Fade(500)
    OP_68(-31260, 600, 114980, 0)
    MoveCamera(26, 35, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xD, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xD)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xD, -40720, 0, 120460, 45)
    OP_D5(0xD, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2CF2():
        OP_95(0xFE, -31020, 0, 111190, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CF2)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xD, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2D3B")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_12_2C0C end

    def Function_13_2D3F(): pass

    label("Function_13_2D3F")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2E4E")
    Fade(500)
    OP_68(-27890, 600, 110180, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xD, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xD)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xD, -28790, 0, 98130, 0)
    OP_D5(0xD, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0xD, 1, 0, 14)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xD, 1)
    OP_79(0x1)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2E4E")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_2D3F end

    def Function_14_2E52(): pass

    label("Function_14_2E52")

    OP_95(0xD, -28360, 0, 100110, 4000, 0x0)
    OP_9E(0xD, 0xFFFF67A8, 0x19064, 0xFFFF15A0, 0xFA0, 0x1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_14_2E52 end

    def Function_15_2E88(): pass

    label("Function_15_2E88")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -24980, 0, 115700, 225)
    OP_31(0x1)
    OP_68(-24980, 600, 115700, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2E88 end

    def Function_16_2ED9(): pass

    label("Function_16_2ED9")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2F34")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F29")
    Sound(2502, 255, 100, 0)
    Jump("loc_2F2F")

    label("loc_2F29")

    Sound(2503, 255, 100, 0)

    label("loc_2F2F")

    Jump("loc_2F58")

    label("loc_2F34")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F52")
    Sound(3347, 255, 100, 0)
    Jump("loc_2F58")

    label("loc_2F52")

    Sound(3348, 255, 100, 0)

    label("loc_2F58")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2ED9 end

    def Function_17_2F6D(): pass

    label("Function_17_2F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7B")
    Call(0, 66)
    Return()

    label("loc_2F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2F88")
    Call(0, 67)
    Return()

    label("loc_2F88")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Descend with the rope\x01",      # 0
            "Step away\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FE9"),
        (1, "loc_3009"),
        (SWITCH_DEFAULT, "loc_3015"),
    )


    label("loc_2FE9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("m4150", 100, 0, 0)
    IdleLoop()
    Jump("loc_3015")

    label("loc_3009")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_3015")

    label("loc_3015")

    Return()

    # Function_17_2F6D end

    def Function_18_3016(): pass

    label("Function_18_3016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3066")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_3066")

    Call(0, 11)
    Return()

    # Function_18_3016 end

    def Function_19_306A(): pass

    label("Function_19_306A")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58780, 3500, 148420, 1500)
    MoveCamera(72, 40, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(24000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312C")
    OP_E2(0x2)
    MiniGame(0x6, 0xA, 0xFFFF1820, 0x0, 0x239CE, 0x0, 0xFFFF3EEA, 0xFFFFF448, 0x25CCE)

    label("loc_312C")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_306A end

    def Function_20_3131(): pass

    label("Function_20_3131")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("apl/ch51113.itc", 0x20)
    LoadChrToIndex("apl/ch51117.itc", 0x21)
    LoadEffect(0x2, "event/ev10001.eff")
    LoadEffect(0x9, "map/mprain00.eff")
    SoundLoad(3704)
    SoundLoad(3705)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    OP_E2(0x1)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x1E)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    OP_68(-68410, 3720, 152490, 0)
    MoveCamera(23, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36650, 0)
    OP_68(-52830, 3720, 134400, 7600)
    MoveCamera(25, 16, 0, 7600)
    OP_6E(510, 7600)
    SetCameraDistance(46660, 7600)
    ClearChrFlags(0x22, 0x80)
    OP_78(0x2, 0x22)
    OP_49()
    SetChrPos(0x22, -71290, 220, 191970, 145)
    OP_D5(0x22, 0x0, 0x23668, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    OP_93(0x22, 0x91, 0x0)
    BeginChrThread(0x22, 3, 0, 21)
    BeginChrThread(0x27, 1, 0, 23)
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(965, 0, 100, 0)
    BeginChrThread(0x27, 2, 0, 24)
    StopBGM(0x1B58)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(-45210, 6120, 66710, 0)
    MoveCamera(53, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(41940, 0)
    OP_68(-33170, 6120, 57750, 6500)
    MoveCamera(63, 28, 0, 6500)
    OP_6E(510, 6500)
    SetCameraDistance(34640, 6500)
    EndChrThread(0x22, 0x3)
    BeginChrThread(0x22, 3, 0, 22)
    SetChrPos(0xE, -33230, 4680, 58630, 180)
    SetChrPos(0xF, -31910, 4480, 57850, 180)
    Fade(500)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    VolumeBGM(0x28, 0x64)
    Sleep(100)
    VolumeBGM(0x64, 0x1770)
    OP_6F(0x79)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19000, 3500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xE,
        (
            "Huhu, well that takes care of that.\x01",
            "Is it about time for us to be\x01",
            "heading back?\x02\x03",
            "Whoops, before that, I guess I'll\x01",
            "pay a visit to that Old Mine or\x01",
            "whatever.\x02",
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
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#04804F#11PEhehe, be very careful.\x02\x03",
            "#04802FAnd as for me, I have a\x01",
            "mission to perform.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xE,
        (
            "#04704F#6PHuhu, do your very best.\x02\x03",
            "#04700FOh, right, our assignments\x01",
            "for the current plan have\x01",
            "been decided.\x02\x03",
            "The Seventh Anguis and I\x01",
            "will be in charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04805F#11PWow, so they're coming,\x01",
            "huh?\x02\x03",
            "#04804FWell, it seems a lot of\x01",
            "troublesome guys are\x01",
            "involved this time, too.\x02\x03",
            "#04800FSo that might be a good\x01",
            "decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04704F#6PHuhu, exactly.\x02\x03",
            "#04702FAlso, I leave the Astral\x01",
            "Code operation report to\x01",
            "you.\x02\x03",
            "I'm interested to see\x01",
            "its value in a low level\x01",
            "network environment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04806F#11PYes, yes. I'll put it\x01",
            "together when I get some\x01",
            "free time.\x02\x03",
            "#04800FThen─ For the\x01",
            "Grandmaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04704F#6PFor the Grandmaster.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0xE, 0x1)
    Sound(901, 0, 80, 0)
    Sleep(500)
    Sound(900, 2, 70, 0)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-33220, 6120, 58130, 1500)
    MoveCamera(59, 28, 0, 1500)
    OP_6E(510, 1500)
    OP_93(0xE, 0xE1, 0x15E)
    OP_6F(0x79)
    Sleep(300)
    SetCameraDistance(17000, 1000)
    PlayEffect(0x2, 0xFF, 0xE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(223, 0, 100, 0)
    StopSound(900, 2000, 40)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    SetCameraDistance(19500, 800)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xE, 0x80)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#04804F#11P...Hehe. Then, though no\x01",
            "one's watching, I think\x01",
            "I'll make a promise.\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x7D0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-31880, 5820, 57380, 2000)
    MoveCamera(74, 27, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(16770, 2000)
    Sleep(500)
    OP_93(0xF, 0xE1, 0x1F4)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xF, 0x21)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x1000)
    SetChrSubChip(0xF, 0x2)
    OP_0D()
    Sleep(500)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xF, 0x1)
    Sleep(150)
    SetChrSubChip(0xF, 0x0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xF,
        (
            "#3704V#30WEnforcer No. 0, Campanella "The\x01",
            "Fool"...\x02\x03",
            "#3705VStarting now, I'll watch over the\x01",
            ""Phantasmal Blaze Plan" as the\x01",
            "Grandmaster's proxy.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE79)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    Sound(966, 0, 50, 0)
    SetCameraDistance(17520, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sound(965, 0, 100, 0)
    StopSound(128, 1000, 90)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3131 end

    def Function_21_3B1E(): pass

    label("Function_21_3B1E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -68150, 320, 183420)
    OP_9F(0x1, -68100, 320, 164160)
    OP_9F(0x1, -65680, 320, 151380)
    OP_9F(0x1, -58980, 320, 141230)
    OP_9F(0x1, -44990, 320, 127010)
    OP_9F(0x1, -36840, 120, 117770)
    OP_9F(0x2, 0xFE, 11000, 0x6)
    Return()

    # Function_21_3B1E end

    def Function_22_3B80(): pass

    label("Function_22_3B80")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -31010, 120, 108760)
    OP_9F(0x1, -29550, 120, 96790)
    OP_9F(0x1, -30410, 120, 82580)
    OP_9F(0x1, -27420, 120, 72480)
    OP_9F(0x1, -28460, 120, 63070)
    OP_9F(0x1, -34760, 120, 51910)
    OP_9F(0x1, -35820, 120, 43510)
    OP_9F(0x2, 0xFE, 11000, 0x6)
    Return()

    # Function_22_3B80 end

    def Function_23_3BF0(): pass

    label("Function_23_3BF0")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    Sound(458, 0, 80, 0)
    Return()

    # Function_23_3BF0 end

    def Function_24_3C0C(): pass

    label("Function_24_3C0C")

    Sound(128, 2, 10, 0)
    Sleep(300)
    OP_25(0x80, 0x14)
    Sleep(300)
    OP_25(0x80, 0x1E)
    Sleep(300)
    OP_25(0x80, 0x28)
    Sleep(300)
    OP_25(0x80, 0x32)
    Sleep(300)
    OP_25(0x80, 0x3C)
    Sleep(300)
    OP_25(0x80, 0x46)
    Sleep(300)
    OP_25(0x80, 0x50)
    Sleep(300)
    OP_25(0x80, 0x5A)
    Sleep(300)
    OP_25(0x80, 0x64)
    Return()

    # Function_24_3C0C end

    def Function_25_3C52(): pass

    label("Function_25_3C52")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, -29810, 0, 94930, 0)
    SetChrPos(0x102, -28880, 0, 93870, 0)
    SetChrPos(0x109, -30760, 0, 93290, 0)
    SetChrPos(0x105, -29600, 0, 92570, 0)
    OP_68(-28230, 600, 99000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23710, 0)
    FadeToBright(1000, 0)
    OP_68(-26340, 900, 107250, 6000)
    MoveCamera(52, 16, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(35430, 6000)
    BeginChrThread(0x101, 0, 0, 26)
    BeginChrThread(0x102, 0, 0, 27)
    BeginChrThread(0x109, 0, 0, 28)
    BeginChrThread(0x105, 0, 0, 29)
    OP_0D()
    Sleep(5000)
    OP_68(-26340, 1500, 107250, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18910, 0)
    Fade(500)
    OP_0D()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006F#5P*sigh*...\x02\x03",
            "#00000FWe ended up walking this\x01",
            "far without the car.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00102F#11PWell, the scenery was\x01",
            "beautiful, so it's fine,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#10112F#6PR-Right. (A bit of a\x01",
            "pity, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh man. I didn't think\x01",
            "this post involved this\x01",
            "much walking.\x02\x03",
            "#10305FBy the way...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-24580, 2000, 106670, 2500)
    MoveCamera(61, 6, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(15380, 2500)
    OP_93(0x105, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_3EFF():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3EFF)
    Sleep(50)

    def lambda_3F0F():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F0F)
    Sleep(50)

    def lambda_3F1F():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F1F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#6P#NThe road continues up\x01",
            "that way too. Do you\x01",
            "know what's there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#6P...Yeah. Rosenberg\x01",
            "Studio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThere lives a doll maker\x01",
            "with a bit of a\x01",
            "history...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6P#NWow, so it's that doll\x01",
            "maker not too many know\x01",
            "about, huh?\x02\x03",
            "#10302FBy the way, was he\x01",
            "really planning to\x01",
            "exhibit in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, that happened too.\x02\x03",
            "#00008F(Even now, it's still not\x01",
            "clear who was behind all\x01",
            "of that.)\x02\x03",
            "#00001F(Though Renne's no longer\x01",
            "there... Should we go\x01",
            "check it out anyway?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -24650, 0, 106360, 90)
    SetScenarioFlags(0x129, 1)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_3C52 end

    def Function_26_4174(): pass

    label("Function_26_4174")

    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_26_4174 end

    def Function_27_4184(): pass

    label("Function_27_4184")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_27_4184 end

    def Function_28_4197(): pass

    label("Function_28_4197")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_28_4197 end

    def Function_29_41AA(): pass

    label("Function_29_41AA")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_29_41AA end

    def Function_30_41BD(): pass

    label("Function_30_41BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, -25150, 100, 94110, 293)
    SetChrPos(0x102, -25150, 100, 94110, 293)
    SetChrPos(0x109, -25150, 100, 94110, 293)
    SetChrPos(0x105, -25150, 100, 94110, 293)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x2, 0x1000)
    OP_78(0x2, 0x22)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x22, -28010, 0, 67330, 7)
    OP_D5(0x22, 0x0, 0x1B58, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-18810, -400, 90830, 0)
    MoveCamera(47, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(44480, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x22, 0, 0, 31)
    BeginChrThread(0x27, 1, 0, 36)
    OP_0D()
    Sleep(1500)
    OP_68(-22000, -400, 94790, 5500)
    MoveCamera(61, 25, 0, 5500)
    OP_6E(510, 5500)
    SetCameraDistance(31060, 5500)
    WaitChrThread(0x22, 0)
    OP_68(-26500, 1300, 94300, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    Fade(500)
    OP_0D()
    Sound(462, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x1, 0x8)
    OP_79(0x2)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x102, 0, 0, 33)
    BeginChrThread(0x105, 0, 0, 34)
    BeginChrThread(0x109, 0, 0, 35)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_4387():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4387)
    Sleep(50)

    def lambda_4397():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4397)
    Sleep(50)

    def lambda_43A7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_43A7)
    Sleep(50)

    ChrTalk(
        0x102,
        (
            "#00109F#6P*giggle*. It was clear\x01",
            "on the mountain path,\x01",
            "just like we heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, and the scenery\x01",
            "after the rain was\x01",
            "pretty, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHmm, but still, this car\x01",
            "is something else.\x02\x03",
            "#10102FEven on the mountain\x01",
            "path, it handled\x01",
            "perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PThat's ZCF for you. I bet\x01",
            "it'll sell well when it's\x01",
            "officially released.\x02\x03",
            "#10305FBy the way...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-24680, 1700, 97940, 2000)
    MoveCamera(53, 10, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22600, 2000)
    OP_93(0x105, 0x2D, 0x1F4)
    Sleep(300)

    def lambda_4567():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4567)
    Sleep(50)

    def lambda_4577():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4577)
    Sleep(50)

    def lambda_4587():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4587)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#12P#NThe road continues up\x01",
            "that way too. Do you\x01",
            "know what's there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#6P...Yeah. Rosenberg\x01",
            "Studio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#NThere lives a doll maker\x01",
            "with a bit of a\x01",
            "history...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#12P#NWow, so it's that doll\x01",
            "maker not too many know\x01",
            "about, huh?\x02\x03",
            "#10302FBy the way, was he\x01",
            "really planning to\x01",
            "exhibit in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, that happened too.\x02\x03",
            "#00008F(Even now, it's still not\x01",
            "clear who was behind all\x01",
            "of that.)\x02\x03",
            "#00001F(Though Renne's no longer\x01",
            "there... Should we go\x01",
            "check it out anyway?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -24660, 0, 97490, 0)
    ClearMapObjFlags(0x2, 0x1000)
    SetScenarioFlags(0x129, 2)
    ModifyEventFlags(0, 0, 0x80)
    SetChrFlags(0x22, 0x80)
    OP_E2(0x2)
    ClearMapFlags(0x8000000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_41BD end

    def Function_31_47F3(): pass

    label("Function_31_47F3")

    SetChrPos(0xFE, -28010, 50, 67330, 7)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -27850, 50, 72760)
    OP_9F(0x1, -29000, 50, 83000)
    OP_9F(0x1, -26000, 50, 88900)
    OP_9F(0x1, -25800, 50, 89350)
    OP_9F(0x1, -25650, 50, 89650)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_71(0x2, 0x5B, 0x78, 0x1, 0x8)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    Return()

    # Function_31_47F3 end

    def Function_32_48A0(): pass

    label("Function_32_48A0")


    def lambda_48A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48A5)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_32_48A0 end

    def Function_33_48DE(): pass

    label("Function_33_48DE")

    Sleep(1300)

    def lambda_48E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48E6)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_48DE end

    def Function_34_491F(): pass

    label("Function_34_491F")

    Sleep(2600)

    def lambda_4927():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4927)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_34_491F end

    def Function_35_4960(): pass

    label("Function_35_4960")

    Sleep(3900)

    def lambda_4968():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4968)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x1, 0x8)
    Sleep(600)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(300)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_35_4960 end

    def Function_36_49D3(): pass

    label("Function_36_49D3")

    Sound(458, 0, 80, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    StopSound(458, 2000, 70)
    Sleep(3000)
    Sound(492, 0, 80, 0)
    Return()

    # Function_36_49D3 end

    def Function_37_49F2(): pass

    label("Function_37_49F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_68(-24980, 600, 115700, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -23660, 0, 114990, 270)
    SetChrPos(0x102, -24900, 0, 116210, 180)
    SetChrPos(0x109, -23290, 0, 116420, 225)
    SetChrPos(0x105, -25100, 0, 114790, 45)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xD)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xD, -27600, 0, 73000, 0)
    OP_93(0xD, 0x0, 0x0)
    OP_D5(0xD, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    FadeToBright(1000, 0)
    OP_68(-27910, 2300, 105910, 0)
    MoveCamera(16, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(57480, 0)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0xD, 0, 0, 38)
    BeginChrThread(0x27, 1, 0, 40)
    OP_0D()
    Sleep(500)
    OP_68(-24460, 1900, 115550, 8500)
    MoveCamera(44, 12, 0, 8500)
    OP_6E(510, 8500)
    SetCameraDistance(46590, 8500)
    WaitChrThread(0xD, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)

    def lambda_4B87():

        label("loc_4B87")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4B87")

    QueueWorkItem2(0x101, 2, lambda_4B87)

    def lambda_4B99():

        label("loc_4B99")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4B99")

    QueueWorkItem2(0x102, 2, lambda_4B99)

    def lambda_4BAB():

        label("loc_4BAB")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4BAB")

    QueueWorkItem2(0x109, 2, lambda_4BAB)

    def lambda_4BBD():

        label("loc_4BBD")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4BBD")

    QueueWorkItem2(0x105, 2, lambda_4BBD)
    OP_68(-24330, 1500, 115590, 0)
    MoveCamera(69, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0xD, 0, 0, 39)
    Sound(471, 0, 100, 0)
    OP_0D()
    Sleep(1500)
    Sleep(1500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x109, 0x2)

    def lambda_4C2F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C2F)
    Sleep(50)

    def lambda_4C3F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C3F)
    Sleep(50)

    def lambda_4C4F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4C4F)
    Sleep(50)

    def lambda_4C5F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4C5F)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00109F#6P*giggle*. It was clear\x01",
            "on the mountain path,\x01",
            "just like we heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, and the scenery\x01",
            "after the rain was\x01",
            "pretty, eh?\x02\x03",
            "#00006FStill, even though we\x01",
            "have a car, we ended up\x01",
            "riding the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PHaha. I like buses too,\x01",
            "you know.\x02\x03",
            "#10102FIt was nice to take it\x01",
            "easy and relax for a\x01",
            "change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PIt was a fresh\x01",
            "experience, because I\x01",
            "hardly ever ride them.\x02\x03",
            "#10305FBy the way...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-23980, 2200, 113320, 2500)
    MoveCamera(77, 9, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(16970, 2500)
    OP_93(0x105, 0x87, 0x1F4)
    Sleep(300)

    def lambda_4E51():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E51)
    Sleep(50)

    def lambda_4E61():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4E61)
    Sleep(50)

    def lambda_4E71():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E71)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#6P#NThe road continues up\x01",
            "that way too. Do you\x01",
            "know what's there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#5P...Yeah. Rosenberg\x01",
            "Studio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#NThere lives a doll maker\x01",
            "with a bit of a\x01",
            "history...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#6P#NWow, so it's that doll\x01",
            "maker not too many know\x01",
            "about, huh?\x02\x03",
            "#10302FBy the way, was he\x01",
            "really planning to\x01",
            "exhibit in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah, that happened too.\x02\x03",
            "#00008F(Even now, it's still not\x01",
            "clear who was behind all\x01",
            "of that.)\x02\x03",
            "#00001F(Though Renne's no longer\x01",
            "there... Should we go\x01",
            "check it out anyway?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22190, 0, 113430, 90)
    SetMapObjFlags(0x1, 0x4)
    SetScenarioFlags(0x129, 3)
    ModifyEventFlags(0, 0, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_49F2 end

    def Function_38_50D6(): pass

    label("Function_38_50D6")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -27600, 0, 73000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -30000, 0, 87500)
    OP_9F(0x1, -29500, 0, 99500)
    OP_9F(0x1, -29000, 0, 109000)
    OP_9F(0x1, -30000, 0, 111500)
    OP_9F(0x1, -31500, 0, 113000)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x1)
    Return()

    # Function_38_50D6 end

    def Function_39_519A(): pass

    label("Function_39_519A")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1388, 0x1)
    ClearMapObjFlags(0x1, 0x1000)
    Return()

    # Function_39_519A end

    def Function_40_51FC(): pass

    label("Function_40_51FC")

    Sound(471, 0, 100, 0)
    Sleep(3000)
    Sound(473, 0, 100, 0)
    Return()

    # Function_40_51FC end

    def Function_41_520C(): pass

    label("Function_41_520C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(2718)
    SoundLoad(2719)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -15150, 0, 109800, 270)
    SetChrPos(0x102, -13650, 0, 109050, 270)
    SetChrPos(0x103, -12750, 0, 110950, 270)
    SetChrPos(0x104, -11800, 0, 110100, 270)
    SetChrPos(0x109, -12850, 0, 108000, 270)
    SetChrPos(0x105, -13100, 0, 111750, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-13750, 600, 110000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    OP_68(-14500, 600, 109900, 2000)

    def lambda_5327():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5327)
    Sleep(50)

    def lambda_533F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_533F)
    Sleep(50)

    def lambda_5357():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5357)
    Sleep(50)

    def lambda_536F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_536F)
    Sleep(50)

    def lambda_5387():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5387)
    Sleep(50)

    def lambda_539F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_539F)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    def lambda_5421():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5421)
    Sleep(50)

    def lambda_5431():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5431)
    Sleep(50)

    def lambda_5441():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5441)
    Sleep(50)

    def lambda_5451():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5451)
    Sleep(50)

    def lambda_5461():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5461)
    Sleep(50)

    def lambda_5471():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5471)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5PWhoops...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PCould a problem have\x01",
            "arisen somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
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
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2718V#30WAh, Lloyd!\x02\x03",
            "#2719V#30W*sigh*, it finally\x01",
            "connected.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA9F)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FFran? Thanks for your\x01",
            "hard work.\x02\x03",
            "#00005FCould you have been\x01",
            "calling my ENIGMA for\x01",
            "some time?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, but for some\x01",
            "reason, it just wouldn't\x01",
            "connect...\x02\x03",
            "I tried the others'\x01",
            "ENIGMAs as well.\x02",
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
            "#00008F(It seems there's a device in\x01",
            "the Doll Studio's basement\x01",
            "that jams orbal waves...)\x02\x03",
            "#00006FI'm sorry, we were visiting a\x01",
            "bit of a strange place...\x02\x03",
            "#00001FWhat's wrong? Was there an\x01",
            "urgent Support Request?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, it's not that...\x02\x03",
            "Actually, 30 minutes ago a train\x01",
            "derailment accident occurred\x01",
            "along West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#4SWha...\x02\x03",
            "#00007FIs that true!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, Section Two is already\x01",
            "heading there to survey the\x01",
            "scene.\x02\x03",
            "The CGF is enroute as well, so I\x01",
            "think there's no need for you and\x01",
            "the others to go as well, but...\x02\x03",
            "I thought I would contact you\x01",
            "just in case.\x02",
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
            "#00006FI see... Thank you,\x01",
            "Fran.\x02\x03",
            "#00000FPlease let us know if\x01",
            "any more information\x01",
            "comes in.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Rogeeer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 50, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#00200F#5P...Was there some kind\x01",
            "of problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PIt seemed like that call\x01",
            "was from Fran...\x02",
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
    Sound(802, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00013F#6PYeah...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained about the derailment\x01",
            "accident that occurred along\x01",
            "West Crossbell Highway.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00307F#11PWhat did you say!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PA derailment... The\x01",
            "orbal railway, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. She said that since Section Two and\x01",
            "the CGF are already on their way, she\x01",
            "thought we could leave things to them...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x103,
        (
            "#00206F#5P...Still, it is\x01",
            "worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PYeah. In this tense\x01",
            "situation, the timin's\x01",
            "just too good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, it seems a bit\x01",
            "difficult to think of it\x01",
            "as a mere accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#11PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PWhat do we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWe'll compile and report\x01",
            "our intel on Ouroboros\x01",
            "by the end of the day.\x02\x03",
            "#00001FFor now, let's try going\x01",
            "to the scene of the\x01",
            "accident.\x02\x03",
            "#00000FWas it a Cryptid, or the\x01",
            "doing of some\x01",
            "organization?\x02\x03",
            "We should at least be\x01",
            "able to help survey the\x01",
            "scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PLet's hurry then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6038")

    ChrTalk(
        0x104,
        (
            "#00306F#11PLooks like we could get\x01",
            "there in a flash with\x01",
            "our car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60D6")

    label("loc_6038")


    ChrTalk(
        0x104,
        (
            "#00305F#11POur car... We parked it\x01",
            "somewhere far away, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5PLet's contact the CGF on\x01",
            "patrol and have it delivered\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60D6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Train Accident Site]\x01",
            "was added to the orbal\x01",
            "car destinations.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_616B")
    Jump("loc_61D9")

    label("loc_616B")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The car was returned to\x01",
            "the Special Support\x01",
            "Section's rear entrance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61D9")

    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetChrPos(0x0, -17150, 0, 109800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 5)
    ModifyEventFlags(0, 1, 0x80)
    OP_29(0xA8, 0x4, 0x2)
    OP_29(0xA8, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6239")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6234")
    Jump("loc_6239")

    label("loc_6234")

    OP_29(0x85, 0x4, 0x40)

    label("loc_6239")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_624A")
    Jump("loc_624F")

    label("loc_624A")

    OP_29(0x86, 0x4, 0x40)

    label("loc_624F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6260")
    Jump("loc_6265")

    label("loc_6260")

    OP_29(0x87, 0x4, 0x40)

    label("loc_6265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6276")
    Jump("loc_627B")

    label("loc_6276")

    OP_29(0x89, 0x4, 0x40)

    label("loc_627B")

    ModifyEventFlags(1, 3, 0x80)
    ReplaceBGM("ed7150", "ed7151")
    OP_24(0x323)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_41_520C end

    def Function_42_628D(): pass

    label("Function_42_628D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch31252.itc", 0x23)
    LoadChrToIndex("chr/ch31253.itc", 0x24)
    LoadChrToIndex("apl/ch50515.itc", 0x25)
    LoadChrToIndex("chr/ch41900.itc", 0x28)
    LoadChrToIndex("chr/ch41950.itc", 0x29)
    LoadChrToIndex("chr/ch41952.itc", 0x2A)
    LoadEffect(0x1, "battle/sc008100.eff")
    LoadEffect(0x2, "event/ev10012.eff")
    LoadEffect(0x3, "battle/sc008104.eff")
    LoadEffect(0x4, "battle/btgun00.eff")
    SoundLoad(577)
    SoundLoad(586)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(866)
    SoundLoad(869)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x17, 0x28)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x23, 0x80)
    OP_78(0x4, 0x23)
    OP_49()
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x122, 0x122, 0x0, 0x0)
    SetMapObjFrame(0x4, "mark01", 0x0, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0xFA, 0x0)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x5A)
    OP_71(0xF, 0x51, 0x64, 0x1, 0x20)
    SetChrPos(0x23, -69020, 0, 189390, 15)
    SetChrPos(0x10, -71510, 10, 189980, 315)
    SetChrPos(0x11, -69320, 10, 193620, 315)
    SetChrPos(0x12, -70100, 2900, 188000, 315)
    SetChrPos(0x17, -92500, 10000, 217700, 135)
    SetChrPos(0x18, -89350, 9750, 213100, 135)
    SetChrPos(0x19, -93000, 10000, 212550, 135)
    OP_68(-91900, 10600, 212840, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(60, 30, 0, 5000)
    SetCameraDistance(21250, 5000)
    OP_82(0x64, 0x0, 0xBB8, 0x157C)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    BeginChrThread(0x18, 0, 0, 43)
    BeginChrThread(0x18, 3, 0, 45)
    BeginChrThread(0x19, 0, 0, 43)
    BeginChrThread(0x19, 3, 0, 45)

    def lambda_6522():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6522)
    PlayEffect(0x2, 0x0, 0x17, 0x5, 0, 1000, 3800, 18, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(577, 2, 60, 0)
    Sound(586, 2, 60, 0)
    Sound(865, 2, 70, 0)
    Sound(861, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(577, 500, 60)
    StopSound(586, 500, 60)
    OP_68(-85350, 8250, 207210, 750)
    Sleep(500)
    StopEffect(0x0, 0x0)
    EndChrThread(0x17, 0x0)
    Fade(500)
    SetMapObjFrame(0xFF, "plant01", 0x0, 0x1)
    OP_68(-70000, 2000, 189650, 0)
    MoveCamera(70, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    MoveCamera(80, 30, 0, 7000)
    SetCameraDistance(26000, 7000)
    OP_82(0x64, 0x0, 0xBB8, 0x1B58)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    OP_25(0x361, 0x28)
    OP_25(0x35D, 0x28)
    BeginChrThread(0x27, 1, 0, 46)
    BeginChrThread(0x10, 0, 0, 43)
    BeginChrThread(0x10, 3, 0, 44)
    BeginChrThread(0x11, 0, 0, 43)
    BeginChrThread(0x11, 3, 0, 44)
    BeginChrThread(0x12, 0, 0, 43)
    BeginChrThread(0x12, 3, 0, 44)
    Sound(577, 2, 70, 0)
    Sound(586, 2, 60, 0)
    OP_87(0x1, 0x0, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    StopSound(577, 500, 70)
    StopSound(586, 500, 60)
    Sleep(1000)
    Sound(869, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0x23, 0x0, 900, 3300, 100, -60, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0x23, 0x0, -300, 3300, 100, -60, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0x23, 0x0, 900, 3100, 100, -60, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0x23, 0x0, -300, 3100, 100, -60, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    Sound(577, 2, 70, 0)
    Sound(586, 2, 60, 0)
    OP_87(0x1, 0x0, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    StopSound(577, 1000, 60)
    StopSound(586, 1000, 60)
    OP_24(0x361)
    OP_24(0x35D)
    EndChrThread(0x27, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x241)
    OP_24(0x24A)
    OP_24(0x35D)
    OP_24(0x361)
    OP_24(0x362)
    OP_24(0x365)
    SetScenarioFlags(0x22, 1)
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_628D end

    def Function_43_6821(): pass

    label("Function_43_6821")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6854")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6848")
    OP_4C(0xFE, 0x3)
    Jump("loc_684C")

    label("loc_6848")

    OP_4B(0xFE, 0x3)

    label("loc_684C")

    Sleep(500)
    Jump("Function_43_6821")

    label("loc_6854")

    Return()

    # Function_43_6821 end

    def Function_44_6855(): pass

    label("Function_44_6855")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68A4")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("Function_44_6855")

    label("loc_68A4")

    Return()

    # Function_44_6855 end

    def Function_45_68A5(): pass

    label("Function_45_68A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68F4")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    Jump("Function_45_68A5")

    label("loc_68F4")

    Return()

    # Function_45_68A5 end

    def Function_46_68F5(): pass

    label("Function_46_68F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_690E")
    Sound(356, 0, 70, 0)
    Sleep(1000)
    Jump("Function_46_68F5")

    label("loc_690E")

    Return()

    # Function_46_68F5 end

    def Function_47_690F(): pass

    label("Function_47_690F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("chr/ch31253.itc", 0x24)
    LoadChrToIndex("apl/ch50515.itc", 0x25)
    LoadChrToIndex("chr/ch31251.itc", 0x26)
    LoadChrToIndex("chr/ch31252.itc", 0x27)
    LoadChrToIndex("chr/ch41900.itc", 0x28)
    LoadChrToIndex("chr/ch41951.itc", 0x29)
    LoadChrToIndex("chr/ch41952.itc", 0x2A)
    LoadChrToIndex("chr/ch03451.itc", 0x2D)
    LoadChrToIndex("chr/ch03456.itc", 0x2E)
    LoadChrToIndex("chr/ch03452.itc", 0x2F)
    LoadChrToIndex("chr/ch03454.itc", 0x30)
    LoadEffect(0x0, "event/ev14004.eff")
    LoadEffect(0x1, "battle/sc008100.eff")
    LoadEffect(0x2, "battle/cr414000.eff")
    LoadEffect(0x3, "battle/cr034001.eff")
    LoadEffect(0x4, "battle/btgun00.eff")
    LoadEffect(0x5, "battle/cr034000.eff")
    LoadEffect(0x6, "event/ev14002.eff")
    LoadEffect(0x7, "event/ev15000.eff")
    LoadEffect(0x8, "event/ev14003.eff")
    LoadEffect(0x9, "eff/cutin34.eff")
    LoadEffect(0xA, "event/ev10012.eff")
    SoundLoad(577)
    SoundLoad(586)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(291)
    SoundLoad(870)
    SoundLoad(875)
    SoundLoad(868)
    SoundLoad(534)
    SoundLoad(3913)
    SoundLoad(3918)
    SoundLoad(3915)
    SoundLoad(3914)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x2)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x27)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x28)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x29)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x29)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x2D)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    OP_78(0x4, 0x23)
    OP_49()
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "mark01", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x122, 0x122, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0xFA, 0x0)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x5A)
    OP_71(0xF, 0x51, 0x64, 0x1, 0x20)
    SetChrPos(0x10, -72050, 0, 190750, 325)
    SetChrPos(0x11, -70300, 0, 192250, 325)
    SetChrPos(0x12, -72100, 150, 192850, 325)
    SetChrPos(0x13, -74100, 450, 193650, 325)
    SetChrPos(0x14, -72650, 500, 195350, 325)
    SetChrPos(0x15, -71510, 10, 189980, 315)
    SetChrPos(0x16, -69320, 10, 193620, 315)
    SetChrPos(0x23, -69020, 0, 189390, 15)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    SetMapObjFrame(0xFF, "plant01", 0x0, 0x1)
    BeginChrThread(0x15, 0, 0, 43)
    BeginChrThread(0x15, 3, 0, 44)
    BeginChrThread(0x16, 0, 0, 43)
    BeginChrThread(0x16, 3, 0, 44)
    OP_68(-71900, 1400, 193200, 0)
    MoveCamera(90, 20, -10, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-75350, 3400, 196850, 3000)
    MoveCamera(90, 20, -10, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20000, 3000)

    def lambda_6D2C():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D2C)
    Sleep(50)

    def lambda_6D44():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D44)
    Sleep(50)

    def lambda_6D5C():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6D5C)
    Sleep(50)

    def lambda_6D74():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6D74)
    Sleep(50)

    def lambda_6D8C():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D8C)
    Sound(577, 2, 60, 0)
    Sound(586, 2, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_87(0x1, 0x0, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    BeginChrThread(0x27, 1, 0, 46)
    FadeToBright(1000, 0)
    Sleep(2750)
    OP_0D()
    Fade(500)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    StopEffect(0x0, 0x0)
    SetMapObjFrame(0xFF, "plant01", 0x1, 0x1)
    SetChrPos(0x17, -92500, 10000, 217700, 175)
    SetChrPos(0x18, -89350, 9750, 213100, 135)
    SetChrPos(0x19, -93000, 10000, 212550, 135)
    EndChrThread(0x27, 0x1)
    Sound(865, 2, 60, 0)
    Sound(861, 2, 50, 0)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    BeginChrThread(0x18, 0, 0, 43)
    BeginChrThread(0x18, 3, 0, 45)
    BeginChrThread(0x19, 0, 0, 43)
    BeginChrThread(0x19, 3, 0, 45)

    def lambda_6EA2():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6EA2)
    PlayEffect(0xA, 0x0, 0x17, 0x5, 0, 1000, 3800, 335, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x1C, -92000, 10000, 228900, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-91450, 10600, 213250, 0)
    MoveCamera(20, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(19000, 1000)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-92000, 11600, 225000, 500)
    MoveCamera(30, 20, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(22000, 500)

    def lambda_6F8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_6F8C)

    def lambda_6F9D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6F9D)
    Sleep(250)
    OP_6B(0x1C)
    MoveCamera(80, 25, 0, 3500)
    OP_6E(500, 3500)
    SetCameraDistance(17000, 1500)
    WaitChrThread(0x1C, 1)
    OP_95(0x1C, -89150, 10050, 214300, 8000, 0x0)
    OP_93(0x1C, 0x64, 0x0)
    SetChrSubChip(0x1C, 0x4)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFEB1B4, 0x2E7C, 0x343C8, 0x7D0, 0x1F40)
    OP_95(0x1C, -79250, 11900, 209450, 8000, 0x0)
    OP_93(0x1C, 0xE1, 0x1F4)
    StopSound(577, 500, 60)
    StopSound(586, 500, 50)
    OP_24(0x361)
    OP_24(0x35D)
    StopEffect(0x0, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    ClearChrFlags(0x18, 0x800)
    ClearChrFlags(0x19, 0x800)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x2E)
    OP_A1(0x1C, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_6B(0xFF)
    MoveCamera(100, 30, 0, 3000)
    SetCameraDistance(17000, 3000)
    Sound(580, 2, 100, 0)
    Sound(291, 2, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(3913, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    BeginChrThread(0x1C, 3, 0, 48)
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "plant01", 0x0, 0x1)
    EndChrThread(0x1C, 0x3)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x10, -83160, 6710, 206310, 315)
    SetChrPos(0x11, -85730, 7170, 205220, 315)
    SetChrPos(0x12, -83010, 6100, 204490, 315)
    SetChrPos(0x13, -81060, 5360, 204090, 315)
    SetChrPos(0x14, -82350, 5040, 201760, 315)

    def lambda_7159():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7159)

    def lambda_7172():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7172)

    def lambda_718B():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_718B)

    def lambda_71A4():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_71A4)

    def lambda_71BD():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_71BD)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    OP_68(-83010, 7100, 204490, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17450, 0)
    MoveCamera(65, 35, 0, 3000)
    SetCameraDistance(19500, 3000)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    PlayEffect(0x2, 0x1, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0x13, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x14, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        "#10A#11PAagh...!\x02",
    )

    EndChrThread(0x10, 0x0)
    BeginChrThread(0x10, 0, 0, 56)
    Sleep(500)
    StopEffect(0x1, 0x0)
    Sleep(500)
    Sound(871, 0, 100, 0)

    ChrTalk(
        0x11,
        "#6P#10AUwaaaah!?\x02",
    )

    EndChrThread(0x11, 0x0)
    BeginChrThread(0x11, 0, 0, 56)
    Sleep(500)
    Sound(514, 0, 70, 0)
    StopEffect(0x2, 0x0)
    OP_0D()
    OP_6F(0x79)
    StopSound(580, 500, 90)
    StopSound(291, 500, 100)
    OP_24(0x35D)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    EndChrThread(0x13, 0x0)
    SetChrSubChip(0x13, 0x3)
    Sleep(50)
    EndChrThread(0x14, 0x0)
    SetChrSubChip(0x14, 0x2)
    Sleep(500)
    OP_A6(0x14, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(250)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#11PH-Hide behind the\x01",
            "vehicle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04611FAH HA HA, it's useless!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    OP_93(0x12, 0x82, 0x0)
    OP_93(0x13, 0x82, 0x0)
    OP_93(0x14, 0x82, 0x0)
    OP_68(-86150, 9100, 207750, 0)
    MoveCamera(10, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-86150, 8600, 207750, 500)
    MoveCamera(10, 20, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(16000, 2000)
    SetChrChipByIndex(0x1C, 0x2D)
    SetChrSubChip(0x1C, 0x4)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFEAFD4, 0x1EFA, 0x32B36, 0x3E8, 0x1F40)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0x1C, 0x1)
    OP_93(0x1C, 0x96, 0x1F4)
    SetChrChipByIndex(0x12, 0x26)

    def lambda_7515():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7515)
    SetChrChipByIndex(0x13, 0x26)

    def lambda_752E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_752E)
    SetChrChipByIndex(0x14, 0x26)

    def lambda_7547():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7547)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x2F)
    OP_A1(0x1C, 0xDAC, 0x3, 0x0, 0x1, 0x2)
    BeginChrThread(0x1C, 3, 0, 49)
    BeginChrThread(0x27, 1, 0, 57)
    Sleep(1000)
    EndChrThread(0x1C, 0x3)
    ClearChrFlags(0x1C, 0x4)
    OP_6B(0x1C)
    TurnDirection(0x1C, 0x12, 0)
    EndChrThread(0x12, 0x1)
    Sound(250, 0, 100, 0)
    OP_9A(0x1C, 0x12, 0x0, 0x7530, 0x0)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    Sound(874, 0, 100, 0)
    PlayEffect(0x3, 0x1, 0x12, 0x3, 0, 1000, -500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x0, 0x1C, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0x1C, 0x0, 0x7D0, 0x7530, 0x0)
    OP_A1(0x1C, 0xDAC, 0x3, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0x12, 0x25)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopEffect(0x1, 0x2)
    TurnDirection(0x1C, 0x13, 0)
    SetChrSubChip(0x1C, 0x2)
    EndChrThread(0x13, 0x1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Sound(250, 0, 100, 0)
    OP_9A(0x1C, 0x13, 0x0, 0x7530, 0x0)
    Sound(874, 0, 100, 0)
    PlayEffect(0x3, 0x2, 0x13, 0x3, 0, 1000, -500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x0, 0x1C, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0x1C, 0x0, 0x7D0, 0x7530, 0x0)
    OP_A1(0x1C, 0xDAC, 0x3, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0x13, 0x25)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopEffect(0x2, 0x2)
    TurnDirection(0x1C, 0x14, 0)
    SetChrSubChip(0x1C, 0x2)
    EndChrThread(0x14, 0x1)
    Sound(250, 0, 100, 0)
    OP_9A(0x1C, 0x14, 0x0, 0x7530, 0x0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x1C, 0x800)
    Sound(874, 0, 100, 0)
    PlayEffect(0x3, 0x3, 0x14, 0x3, 0, 1000, -500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x0, 0x1C, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0x1C, 0x0, 0x7D0, 0x7530, 0x0)
    OP_A1(0x1C, 0xDAC, 0x3, 0x3, 0x4, 0x5)
    StopEffect(0x3, 0x2)
    SetChrFlags(0x1C, 0x4)
    BeginChrThread(0x1C, 3, 0, 50)
    SetCameraDistance(18000, 100)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    Sound(3918, 255, 100, 0)

    ChrTalk(
        0x1C,
        (
            "#04612F#12P#4S#10AAH HA HA HA HA HA HA HA\x01",
            "HAH!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P#9AEeeeek!!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(514, 0, 100, 0)
    StopEffect(0x3, 0x2)
    SetChrChipByIndex(0x14, 0x25)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_24(0xF4E)
    Sleep(300)

    ChrTalk(
        0x15,
        "Aaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "A-A monster!?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x27, 0x1)
    StopSound(870, 300, 100)
    Sound(873, 0, 100, 0)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-74200, 2700, 193300, 0)
    MoveCamera(75, 25, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_6B(0x1C)
    OP_71(0x4, 0x11E, 0x11E, 0x1, 0x0)
    OP_93(0x1C, 0x7D, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)

    def lambda_78FD():

        label("loc_78FD")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_78FD")

    QueueWorkItem2(0x15, 2, lambda_78FD)

    def lambda_790F():

        label("loc_790F")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_790F")

    QueueWorkItem2(0x16, 2, lambda_790F)
    OP_0D()
    Sound(577, 2, 60, 0)
    Sound(586, 2, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_87(0x1, 0x0, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    BeginChrThread(0x15, 0, 0, 43)
    BeginChrThread(0x15, 3, 0, 44)
    BeginChrThread(0x16, 0, 0, 43)
    BeginChrThread(0x16, 3, 0, 44)
    BeginChrThread(0x27, 1, 0, 46)
    SetChrChip(0x0, 0x1C, 0x64, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFED784, 0x5F0, 0x2FE36, 0x1F4, 0x2710)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFEDA72, 0x38E, 0x2F792, 0x1F4, 0x2710)
    MoveCamera(75, 20, -5, 2000)
    SetCameraDistance(18000, 2000)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x2D)
    OP_95(0x1C, -69790, 290, 196460, 10000, 0x0)
    OP_95(0x1C, -68210, 2230, 195940, 10000, 0x0)
    OP_95(0x1C, -65780, 2230, 193590, 10000, 0x0)
    OP_95(0x1C, -64500, 2000, 193120, 10000, 0x0)
    StopEffect(0x0, 0x2)
    StopSound(577, 500, 60)
    StopSound(586, 500, 50)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x27, 0x1)
    OP_93(0x1C, 0xE1, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFEF2AA, 0xDAC, 0x2E504, 0x7D0, 0x2710)
    Sound(844, 0, 100, 0)
    OP_9D(0x1C, 0xFFFEF14C, 0xAF0, 0x2E022, 0x3E8, 0x2710)
    OP_93(0x1C, 0x1E, 0x3E8)
    SetChrChipByIndex(0x1C, 0x2F)
    OP_A1(0x1C, 0xDAC, 0x2, 0x0, 0x1)
    Fade(500)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "plant01", 0x1, 0x1)
    ClearChrFlags(0x1C, 0x800)
    SetChrChip(0x1, 0x1C, 0x0, 0x0)
    BeginChrThread(0x1C, 3, 0, 49)
    BeginChrThread(0x27, 1, 0, 57)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_68(-69300, 3400, 188450, 0)
    MoveCamera(165, 30, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    Sound(3915, 255, 100, 0)

    ChrTalk(
        0x1C,
        "#04602F#11P#4S#8AGGGGOOOOOOOOO!!\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x9, 0x2, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_24(0xF4B)
    Sound(875, 2, 100, 0)
    OP_A1(0x1C, 0xDAC, 0x2, 0x3, 0x4)
    BeginChrThread(0x1C, 3, 0, 50)
    PlayEffect(0x7, 0x1, 0xFF, 0x0, -69000, 3000, 189000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    MoveCamera(140, 20, -10, 3000)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    Sleep(2250)
    StopSound(875, 500, 100)
    StopEffect(0x1, 0x2)
    SetChrFlags(0x1C, 0x800)
    PlayEffect(0x5, 0x0, 0x1C, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, -68900, 3000, 189700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_93(0x1C, 0x13B, 0x3E8)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(200, 0, 80, 0)
    Sound(874, 0, 100, 0)
    StopSound(870, 500, 100)
    Sound(873, 0, 100, 0)
    OP_71(0x4, 0x12D, 0x168, 0x0, 0x8)
    PlayEffect(0x6, 0x1, 0xFF, 0x0, -68900, 3000, 189700, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x8, 0x2, 0x23, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_0D()
    Sound(868, 2, 100, 0)
    Fade(500)
    ClearChrFlags(0x1C, 0x800)
    EndChrThread(0x1C, 0x3)
    SetChrPos(0x1C, -69150, 2700, 186750, 180)
    Sound(372, 0, 100, 0)
    Sound(200, 0, 80, 0)
    SetChrChipByIndex(0x1C, 0x30)
    SetChrSubChip(0x1C, 0x3)
    OP_6B(0xFF)
    OP_68(-69150, 3400, 186750, 0)
    MoveCamera(347, 0, 1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    OP_68(-69150, 3200, 186750, 8000)
    MoveCamera(347, 1, 1, 8000)
    SetCameraDistance(22500, 8000)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x1B, 0x4)
    SetChrPos(0x17, -76820, 2680, 199740, 125)
    SetChrPos(0x18, -79130, 3730, 200790, 125)
    SetChrPos(0x19, -78720, 4610, 204020, 125)
    SetChrPos(0x1A, -83060, 5360, 202090, 125)
    SetChrPos(0x1B, -85280, 6320, 202930, 125)
    BeginChrThread(0x19, 1, 0, 53)
    BeginChrThread(0x17, 1, 0, 51)
    BeginChrThread(0x18, 1, 0, 52)
    BeginChrThread(0x1A, 1, 0, 54)
    BeginChrThread(0x1B, 1, 0, 55)
    OP_0D()
    SetChrSubChip(0x1C, 0x4)
    Sound(534, 0, 80, 0)
    Sound(3914, 255, 100, 0)

    ChrTalk(
        0x1C,
        (
            "#04612F#5P#4S#26AYahoo! Ah ha ha ha ha ha\x01",
            "ha ha ha hah!!!\x02",
        )
    )

    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_6B(0xFF)
    WaitChrThread(0x17, 1)
    StopSound(868, 3000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x241)
    OP_24(0x24A)
    OP_24(0x35D)
    OP_24(0x361)
    OP_24(0x123)
    OP_24(0x366)
    OP_24(0x36B)
    OP_24(0x364)
    OP_24(0xF4A)
    SetScenarioFlags(0x22, 0)
    NewScene("r203B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_690F end

    def Function_48_7F71(): pass

    label("Function_48_7F71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FC0")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 800, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x2, 0x3)
    Jump("Function_48_7F71")

    label("loc_7FC0")

    Return()

    # Function_48_7F71 end

    def Function_49_7FC1(): pass

    label("Function_49_7FC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FD9")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_49_7FC1")

    label("loc_7FD9")

    Return()

    # Function_49_7FC1 end

    def Function_50_7FDA(): pass

    label("Function_50_7FDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FF2")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_50_7FDA")

    label("loc_7FF2")

    Return()

    # Function_50_7FDA end

    def Function_51_7FF3(): pass

    label("Function_51_7FF3")

    Sleep(100)
    SetChrChipByIndex(0x17, 0x29)
    OP_95(0x17, -73100, 160, 192020, 6000, 0x0)
    OP_95(0x17, -72020, 10, 186980, 6000, 0x0)
    OP_95(0x17, -68300, 0, 184320, 6000, 0x0)
    OP_95(0x17, -66940, 250, 180890, 6000, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x2)
    OP_82(0x64, 0x0, 0xBB8, 0x186A0)
    BeginChrThread(0x17, 0, 0, 43)
    BeginChrThread(0x17, 3, 0, 45)
    Return()

    # Function_51_7FF3 end

    def Function_52_8077(): pass

    label("Function_52_8077")

    Sleep(200)
    SetChrChipByIndex(0x18, 0x29)
    OP_95(0x18, -73100, 160, 192020, 6000, 0x0)
    OP_95(0x18, -72020, 10, 186980, 6000, 0x0)
    OP_95(0x18, -68300, 0, 184320, 6000, 0x0)
    OP_95(0x18, -68540, 250, 180650, 6000, 0x0)
    OP_93(0x18, 0xB4, 0x1F4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x2)
    BeginChrThread(0x18, 0, 0, 43)
    BeginChrThread(0x18, 3, 0, 45)
    Return()

    # Function_52_8077 end

    def Function_53_80EA(): pass

    label("Function_53_80EA")

    SetChrChipByIndex(0x19, 0x29)
    OP_95(0x19, -76870, 3450, 202160, 6000, 0x0)
    OP_95(0x19, -73100, 160, 192020, 6000, 0x0)
    OP_95(0x19, -72020, 10, 186980, 6000, 0x0)
    OP_95(0x19, -68300, 0, 184320, 6000, 0x0)
    OP_95(0x19, -66050, 250, 182510, 6000, 0x0)
    OP_93(0x19, 0xB4, 0x1F4)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x2)
    BeginChrThread(0x19, 0, 0, 43)
    BeginChrThread(0x19, 3, 0, 45)
    Return()

    # Function_53_80EA end

    def Function_54_816E(): pass

    label("Function_54_816E")

    Sleep(300)
    SetChrChipByIndex(0x1A, 0x29)
    OP_95(0x1A, -78780, 2440, 196980, 6000, 0x0)
    OP_95(0x1A, -72020, 10, 186980, 6000, 0x0)
    OP_95(0x1A, -68300, 0, 184320, 6000, 0x0)
    OP_95(0x1A, -69830, 250, 181040, 6000, 0x0)
    OP_93(0x1A, 0xB4, 0x1F4)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrSubChip(0x1A, 0x2)
    BeginChrThread(0x1A, 0, 0, 43)
    BeginChrThread(0x1A, 3, 0, 45)
    Return()

    # Function_54_816E end

    def Function_55_81E1(): pass

    label("Function_55_81E1")

    Sleep(400)
    SetChrChipByIndex(0x1B, 0x29)
    OP_95(0x1B, -78780, 2440, 196980, 6000, 0x0)
    OP_95(0x1B, -72020, 10, 186980, 6000, 0x0)
    OP_95(0x1B, -68300, 0, 184320, 6000, 0x0)
    OP_95(0x1B, -68110, 250, 182500, 6000, 0x0)
    OP_93(0x1B, 0xB4, 0x1F4)
    SetChrChipByIndex(0x1B, 0x2A)
    SetChrSubChip(0x1B, 0x2)
    BeginChrThread(0x1B, 0, 0, 43)
    BeginChrThread(0x1B, 3, 0, 45)
    Return()

    # Function_55_81E1 end

    def Function_56_8254(): pass

    label("Function_56_8254")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8266():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8266)

    def lambda_827F():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_827F)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_8254 end

    def Function_57_82BE(): pass

    label("Function_57_82BE")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Return()

    # Function_57_82BE end

    def Function_58_82CE(): pass

    label("Function_58_82CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, -4250, 0, 21950, 315)
    SetChrPos(0x102, -2900, 0, 21700, 315)
    SetChrPos(0x103, -3550, 0, 20500, 315)
    SetChrPos(0x109, -2400, 0, 20150, 315)
    SetChrPos(0x105, -1600, 0, 21200, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-2400, 600, 20150, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(-6000, 1000, 23900, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_839C():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_839C)
    Sleep(100)

    def lambda_83B4():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_83B4)
    Sleep(100)

    def lambda_83CC():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_83CC)
    Sleep(100)

    def lambda_83E4():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_83E4)
    Sleep(100)

    def lambda_83FC():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_83FC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 2, 0, 59)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x102, 2, 0, 61)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 2, 0, 63)
    WaitChrThread(0x109, 1)
    BeginChrThread(0x109, 2, 0, 62)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 2, 0, 60)
    Sleep(1500)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00013F#11PThe high ground before\x01",
            "the waterfall... there!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58700, 6400, 66250, 5000)
    MoveCamera(30, 17, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(18000, 5000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_84F5():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_84F5)
    Sleep(30)

    def lambda_8505():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8505)
    Sleep(30)

    def lambda_8515():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8515)
    Sleep(30)

    def lambda_8525():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8525)
    Sleep(30)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201F...Just like Cao's intel\x01",
            "said.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107FLet's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -7000, 0, 24750, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x166, 4)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_58_82CE end

    def Function_59_85D1(): pass

    label("Function_59_85D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85F5")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    Jump("Function_59_85D1")

    label("loc_85F5")

    Return()

    # Function_59_85D1 end

    def Function_60_85F6(): pass

    label("Function_60_85F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_861A")
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    Jump("Function_60_85F6")

    label("loc_861A")

    Return()

    # Function_60_85F6 end

    def Function_61_861B(): pass

    label("Function_61_861B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_863F")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    Jump("Function_61_861B")

    label("loc_863F")

    Return()

    # Function_61_861B end

    def Function_62_8640(): pass

    label("Function_62_8640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8664")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Jump("Function_62_8640")

    label("loc_8664")

    Return()

    # Function_62_8640 end

    def Function_63_8665(): pass

    label("Function_63_8665")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8689")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    Jump("Function_63_8665")

    label("loc_8689")

    Return()

    # Function_63_8665 end

    def Function_64_868A(): pass

    label("Function_64_868A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    ClearChrFlags(0x22, 0x80)
    OP_78(0x2, 0x22)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x101, -5000000, 0, 0, 0)
    SetChrPos(0x102, -5000000, 0, 0, 0)
    SetChrPos(0x103, -5000000, 0, 0, 0)
    SetChrPos(0x109, -5000000, 0, 0, 0)
    SetChrPos(0x105, -5000000, 0, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x22, -200, -4500, 3000, 0)
    OP_D5(0x22, 0x0, 0x0, 0x0, 0x0)
    OP_68(-200, 500, 5000, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(-1810, 600, 23500, 5000)
    MoveCamera(90, 25, 0, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0x27, 1, 0, 65)
    OP_9F(0x0, 0x22)
    OP_9F(0x1, -200, -4500, 3000)
    OP_9F(0x1, -210, -300, 13600)
    OP_9F(0x1, -410, 0, 20120)
    OP_9F(0x1, -1810, 0, 23520)
    OP_9F(0x2, 0x22, 5000, 0x6)
    OP_71(0x2, 0x5B, 0x78, 0x1, 0x8)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -7100, 0, 24800, 315)
    SetChrPos(0x102, -5750, 0, 24550, 0)
    SetChrPos(0x103, -6400, 0, 23350, 270)
    SetChrPos(0x109, -3550, 0, 23000, 45)
    SetChrPos(0x105, -4400, 0, 24000, 270)
    SetChrPos(0x22, -1810, 0, 23520, 330)
    OP_68(-3550, 1000, 23000, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    OP_68(-6000, 1000, 23900, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22500, 3000)
    BeginChrThread(0x101, 2, 0, 59)
    Sleep(300)
    BeginChrThread(0x102, 2, 0, 61)
    Sleep(300)
    BeginChrThread(0x103, 2, 0, 62)
    Sleep(300)
    BeginChrThread(0x105, 2, 0, 60)
    Sound(461, 0, 100, 0)
    Sleep(100)
    OP_71(0x2, 0x14B, 0x168, 0x1, 0x8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x109, -5250, 0, 23000, 2000, 0x0)
    OP_93(0x109, 0x13B, 0x1F4)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00013F#11PThe high ground before\x01",
            "the waterfall... there!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58700, 6400, 66250, 5000)
    MoveCamera(30, 17, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(18000, 5000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_89CC():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_89CC)
    Sleep(30)

    def lambda_89DC():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_89DC)
    Sleep(30)

    def lambda_89EC():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_89EC)
    Sleep(30)

    def lambda_89FC():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_89FC)
    Sleep(30)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201F...Just like Cao's intel\x01",
            "said.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107FLet's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -7000, 0, 24750, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 3)
    SetScenarioFlags(0x166, 4)
    OP_66(0x8, 0x1)
    ClearMapFlags(0x10000000)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_64_868A end

    def Function_65_8AB4(): pass

    label("Function_65_8AB4")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(492, 0, 70, 0)
    Return()

    # Function_65_8AB4 end

    def Function_66_8AC4(): pass

    label("Function_66_8AC4")

    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-57850, 7400, 65600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -57350, 6000, 65950, 270)
    SetChrPos(0x102, -57500, 6000, 67000, 225)
    SetChrPos(0x103, -56850, 6000, 64950, 270)
    SetChrPos(0x109, -56500, 6000, 67200, 225)
    SetChrPos(0x105, -56000, 6000, 66000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10306F#11PLooks like he really did\x01",
            "go below the cliffs from\x01",
            "here.\x02\x03",
            "#10308FHowever... What in the\x01",
            "world's down there, I\x01",
            "wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#5PIt looks like the rope\x01",
            "descends between a gap\x01",
            "in the rocks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAnyway, we have no\x01",
            "choice but to descend.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Descend immediately\x01",      # 0
            "Prepare for now\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8CC5"),
        (1, "loc_8E4C"),
        (SWITCH_DEFAULT, "loc_8E70"),
    )


    label("loc_8CC5")


    def lambda_8CCA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8CCA)
    Sleep(50)

    def lambda_8CDA():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8CDA)
    Sleep(50)

    def lambda_8CEA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8CEA)
    Sleep(50)

    def lambda_8CFA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8CFA)
    Sleep(50)

    def lambda_8D0A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D0A)
    Sleep(50)

    def lambda_8D1A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8D1A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00001F#6P─Alright. Everybody\x01",
            "ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PI'm okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PNo problem here either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#11PSame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5P─Let's go. We've got to\x01",
            "catch Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAlright... Let's be\x01",
            "careful as we descend.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("m4150", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E70")

    label("loc_8E4C")

    SetChrPos(0x0, -57350, 6000, 65950, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_8E70")

    label("loc_8E70")

    Return()

    # Function_66_8AC4 end

    def Function_67_8E71(): pass

    label("Function_67_8E71")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The rope connected to\x01",
            "the cliff below has been\x01",
            "severed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90C1")

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703FIt seems to have been\x01",
            "severed with something\x01",
            "sharp as well.\x02\x03",
            "#10701FI wonder where this rope\x01",
            "led...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403FActually, Randy used this\x01",
            "to climb down to the Old\x01",
            "Mine a while back.\x02\x03",
            "#10400FIf you go through it, it\x01",
            "actually exits in the\x01",
            "Mainz area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703FI see, there's a path\x01",
            "like that, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FCould Red Constellation\x01",
            "have cut the rope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FActually, that's highly\x01",
            "possible under these\x01",
            "circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FHow cunning of them.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CE, 1)

    label("loc_90C1")

    EventEnd(0x3)
    Return()

    # Function_67_8E71 end

    def Function_68_90C4(): pass

    label("Function_68_90C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03154.itc", 0x1E)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x18, 0x24)
    OP_49()
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    OP_71(0x18, 0x1, 0x78, 0x0, 0x20)
    OP_75(0x18, 0x1, 0x0)
    OP_FF(0x18, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0x25, 0x80)
    OP_78(0x19, 0x25)
    OP_49()
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_71(0x19, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0x19, 0x307, 0x307, 0x307)
    ClearChrFlags(0x26, 0x80)
    OP_78(0x1D, 0x26)
    OP_49()
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    OP_75(0x1D, 0x1, 0x0)
    OP_FF(0x1D, 0x2EE, 0x2EE, 0x2EE)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sleep(1000)
    SetChrPos(0x101, -5000000, 0, 0, 0)
    SetChrPos(0x103, -5000000, 0, 0, 0)
    SetChrPos(0x105, -5000000, 0, 0, 0)
    SetChrPos(0x106, -5000000, 0, 0, 0)
    SetChrPos(0x107, -5000000, 0, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x24, -30250, 20000, 104050, 325)
    OP_D5(0x24, 0x0, 0x4F588, 0x0, 0x0)
    SetChrPos(0x25, -30250, 20000, 104050, 325)
    OP_D5(0x25, 0x0, 0x4F588, 0x0, 0x0)
    SetChrPos(0x26, -30250, 0, 104050, 325)
    OP_D5(0x26, 0x0, 0x4F588, 0x0, 0x0)
    OP_68(-33250, -400, 124450, 0)
    MoveCamera(10, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    OP_68(-30250, 5000, 104050, 6000)
    MoveCamera(30, 40, 0, 6000)
    SetCameraDistance(60000, 6000)

    def lambda_92C9():
        OP_96(0xFE, 0xFFFF89D6, 0xDAC, 0x19672, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_92C9)

    def lambda_92E3():
        OP_96(0xFE, 0xFFFF89D6, 0xDAC, 0x19672, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_92E3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F40)
    BeginChrThread(0x24, 0, 0, 69)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(132, 1000, 100)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x24, 0x0)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetMapObjFrame(0x1A, "Null_fream", 0x2, "start")
    Sleep(1000)
    SetChrPos(0x101, -27200, 0, 93550, 90)
    SetChrPos(0x105, -26350, 0, 92850, 90)
    SetChrPos(0x103, -27900, 0, 91700, 90)
    SetChrPos(0x106, -28550, 0, 92550, 90)
    SetChrPos(0x107, -27150, 0, 90550, 45)
    SetChrSubChip(0x107, 0x5)
    OP_68(-26350, 1600, 92850, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_68(-26350, 3600, 92850, 6000)
    MoveCamera(30, 15, 0, 6000)
    SetCameraDistance(23000, 6000)
    SetChrPos(0x24, -30250, 3500, 104050, 325)
    OP_D5(0x24, 0x0, 0x4F588, 0x0, 0x0)
    SetChrPos(0x25, -30250, 3500, 104050, 325)
    OP_D5(0x25, 0x0, 0x4F588, 0x0, 0x0)
    SetChrPos(0x26, -30250, 0, 104050, 325)
    OP_D5(0x26, 0x0, 0x4F588, 0x0, 0x0)

    def lambda_946D():
        OP_96(0xFE, 0xFFFF89D6, 0x3C8C, 0x19672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_946D)

    def lambda_9487():
        OP_96(0xFE, 0xFFFF89D6, 0x3C8C, 0x19672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9487)
    BeginChrThread(0x24, 0, 0, 71)
    BeginChrThread(0x25, 0, 0, 70)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    BeginChrThread(0x105, 3, 0, 72)
    Sound(935, 0, 70, 0)
    SetMapObjFrame(0x1B, "Null_fream", 0x2, "start")
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1A, 0x1000)
    SetMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1B, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    EndChrThread(0x105, 0x3)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x101, 0x107, 0)
    TurnDirection(0x103, 0x101, 0)
    TurnDirection(0x105, 0x101, 0)
    TurnDirection(0x106, 0x101, 0)
    TurnDirection(0x107, 0x101, 0)
    SetChrSubChip(0x107, 0x5)
    OP_68(-27500, 1200, 92100, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10404F#11PNow then, regarding the\x01",
            "resistance forces in the\x01",
            "mountain path area...\x02\x03",
            "#10402FShould we head towards\x01",
            "Mainz first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PRight, I'm worried about\x01",
            "the situation in Mainz\x01",
            "as well...\x02\x03",
            "#00008FBut...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-27500, 1700, 92100, 2000)
    MoveCamera(43, 12, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_9673():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9673)
    Sleep(1000)

    def lambda_9683():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9683)
    Sleep(50)

    def lambda_9693():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9693)
    Sleep(50)

    def lambda_96A3():
        OP_93(0x106, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_96A3)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10401F#12PI understand... That\x01",
            "'place' is quite\x01",
            "disturbing, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThe Rosenberg Doll Studio,\x01",
            "one of the Thirteen\x01",
            "Workshops, right?\x02\x03",
            "#00201FPreviously, he said he\x01",
            "would have talked to us\x01",
            "another time, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6PI see...\x02\x03",
            "#10703F...Actually, I tried\x01",
            "infiltrating once before,\x01",
            "but...\x02\x03",
            "#10710FIts underground structure was\x01",
            "so staggering and complex\x01",
            "that I had to give up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#00012F#5PY-You did that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CHmm. Jｶrg, eh?\x02\x03",
            "#01200FI haven't seen his face for\x01",
            "some time, but looks like he's\x01",
            "in his usual good health.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9949():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9949)
    Sleep(50)

    def lambda_9959():
        TurnDirection(0x103, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9959)
    Sleep(50)

    def lambda_9969():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9969)
    Sleep(50)

    def lambda_9979():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9979)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#00011F#5PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#5PZeit, are you acquainted\x01",
            "with that old man as\x01",
            "well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CYes. We're familiar with\x01",
            "each other's circumstances\x01",
            "to some degree.\x02\x03",
            "#01200FHe's affiliated with the\x01",
            "Snake and an amazing old-\x01",
            "fashioned craftsman.\x02\x03",
            "There's no doubt that he's\x01",
            "a character you can trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PI'd like to know more information\x01",
            "about Ouroboros, so it might be\x01",
            "worth paying him a visit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B59():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9B59)
    Sleep(50)

    def lambda_9B69():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9B69)
    Sleep(50)

    def lambda_9B79():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9B79)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        (
            "#00202F#12PWhy don't we make a stop\x01",
            "there before going to\x01",
            "Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x18, 0x1000)
    SetMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x19, 0x1000)
    SetMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1D, 0x1000)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrPos(0x0, -26420, 0, 95890, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 0)
    OP_29(0xAF, 0x1, 0x8)
    ModifyEventFlags(1, 3, 0x80)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x3B6)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_68_90C4 end

    def Function_69_9C7D(): pass

    label("Function_69_9C7D")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x19, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x18, 0x2, 0x7D0)
    OP_75(0x1D, 0x2, 0x7D0)
    Sleep(1000)
    StopSound(950, 1000, 40)
    OP_79(0x19)
    Return()

    # Function_69_9C7D end

    def Function_70_9CC2(): pass

    label("Function_70_9CC2")

    OP_75(0x18, 0x1, 0x7D0)
    OP_75(0x1D, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x19, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    StopSound(497, 4000, 80)
    OP_79(0x19)
    OP_71(0x19, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_70_9CC2 end

    def Function_71_9D16(): pass

    label("Function_71_9D16")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_71_9D16 end

    def Function_72_9D7B(): pass

    label("Function_72_9D7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D95")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_72_9D7B")

    label("loc_9D95")

    Return()

    # Function_72_9D7B end

    def Function_73_9D96(): pass

    label("Function_73_9D96")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x6)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x101, -14950, 0, 109800, 270)
    SetChrPos(0x106, -13650, 0, 109050, 270)
    SetChrPos(0x103, -12750, 0, 110950, 270)
    SetChrPos(0x105, -11800, 0, 110100, 270)
    SetChrPos(0x107, -13000, 0, 112000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-13750, 1000, 110000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    OP_68(-15750, 1000, 110000, 2000)

    def lambda_9EE8():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9EE8)
    Sleep(10)

    def lambda_9F00():
        OP_9B(0x0, 0x106, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9F00)
    Sleep(10)

    def lambda_9F18():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9F18)
    Sleep(10)

    def lambda_9F30():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F30)
    Sleep(10)

    def lambda_9F48():
        OP_9B(0x0, 0x107, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_9F48)
    Sleep(10)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_0D()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x7D0)
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x103,
        "#00201F#5PThis presence...!?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x106,
        (
            "#10707F#11PMilitary monsters,\x01",
            "incoming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWhat!?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    Fade(500)
    OP_68(-15250, 1000, 110000, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(35000, 0)
    OP_68(-15250, 1000, 110000, 4000)
    MoveCamera(75, 20, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(30000, 4000)
    Sound(805, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x107, 0x24)
    SetChrSubChip(0x107, 0x0)
    OP_93(0x101, 0xD2, 0x0)
    OP_93(0x103, 0x1E, 0x0)
    OP_93(0x105, 0x4B, 0x0)
    OP_93(0x106, 0x78, 0x0)
    OP_93(0x107, 0x12C, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1D, -26000, 0, 98450, 45)
    SetChrPos(0x1E, -4220, 4000, 94720, 315)
    SetChrPos(0x1F, 700, 3530, 112320, 270)
    SetChrPos(0x20, -11670, 8540, 123840, 180)
    SetChrPos(0x21, -27000, 0, 116250, 135)
    BeginChrThread(0x1D, 3, 0, 74)
    BeginChrThread(0x27, 1, 0, 76)

    def lambda_A176():
        OP_96(0xFE, 0xFFFFB2A8, 0x0, 0x19834, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A176)
    Sleep(300)
    BeginChrThread(0x1E, 3, 0, 74)

    def lambda_A199():
        OP_96(0xFE, 0xFFFFD634, 0xFA0, 0x18BE6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A199)
    Sleep(300)
    BeginChrThread(0x1F, 3, 0, 74)

    def lambda_A1BC():
        OP_96(0xFE, 0xFFFFE34A, 0x1F4, 0x1B198, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A1BC)
    Sleep(300)

    def lambda_A1D9():
        OP_9D(0xFE, 0xFFFFC888, 0x7D0, 0x1CB60, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A1D9)
    Sleep(300)
    Sound(809, 0, 60, 0)
    BeginChrThread(0x21, 3, 0, 74)

    def lambda_A205():
        OP_96(0xFE, 0xFFFFB082, 0x0, 0x1B8D2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A205)
    WaitChrThread(0x1D, 1)
    EndChrThread(0x1D, 0x3)
    SetChrChipByIndex(0x1D, 0x1E)
    BeginChrThread(0x1D, 3, 0, 75)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x1E, 0x3)
    SetChrChipByIndex(0x1E, 0x1E)
    BeginChrThread(0x1E, 3, 0, 75)
    WaitChrThread(0x1F, 1)
    EndChrThread(0x1F, 0x3)
    SetChrChipByIndex(0x1F, 0x1E)
    BeginChrThread(0x1F, 3, 0, 75)
    WaitChrThread(0x20, 1)
    SetChrChipByIndex(0x20, 0x1E)
    BeginChrThread(0x20, 3, 0, 75)
    WaitChrThread(0x21, 1)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x27, 0x1)
    SetChrChipByIndex(0x21, 0x1E)
    BeginChrThread(0x21, 3, 0, 75)
    Sound(948, 0, 60, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#6PGuh... These guys!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10407F#5PHere they come!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x1F, 0x3)
    EndChrThread(0x20, 0x3)
    EndChrThread(0x21, 0x3)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x6)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x6)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x6)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x6)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x6)
    Sound(250, 0, 60, 0)

    def lambda_A305():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A305)

    def lambda_A322():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3A98)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A322)

    def lambda_A33F():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A33F)

    def lambda_A35C():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A35C)

    def lambda_A379():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A379)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(25000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_E30", 0x30200011, 0x0, 0x0, 0x1B, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    Call(0, 77)
    Return()

    # Function_73_9D96 end

    def Function_74_A3E0(): pass

    label("Function_74_A3E0")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A40D")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_A3F6")

    label("loc_A40D")

    Return()

    # Function_74_A3E0 end

    def Function_75_A40E(): pass

    label("Function_75_A40E")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A43B")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_A424")

    label("loc_A43B")

    Return()

    # Function_75_A40E end

    def Function_76_A43C(): pass

    label("Function_76_A43C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A455")
    Sound(845, 0, 80, 0)
    Sleep(500)
    Jump("Function_76_A43C")

    label("loc_A455")

    Return()

    # Function_76_A43C end

    def Function_77_A456(): pass

    label("Function_77_A456")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x107, 0x24)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x1)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x1)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x1)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x1)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x1)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_68(-16250, 1000, 110000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -16950, 0, 109800, 270)
    SetChrPos(0x106, -15650, 0, 109050, 270)
    SetChrPos(0x103, -14750, 0, 110950, 270)
    SetChrPos(0x105, -13800, 0, 110100, 270)
    SetChrPos(0x107, -15000, 0, 112000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1D, -21250, 0, 109450, 89)
    SetChrPos(0x1E, -22650, 0, 110900, 89)
    SetChrPos(0x1F, -23350, 0, 108100, 89)
    SetChrPos(0x20, -25350, 0, 109450, 89)
    SetChrPos(0x21, -20150, 0, 112150, 135)
    BeginChrThread(0x1D, 3, 0, 75)
    BeginChrThread(0x1E, 3, 0, 75)
    BeginChrThread(0x1F, 3, 0, 75)
    BeginChrThread(0x20, 3, 0, 75)
    BeginChrThread(0x21, 3, 0, 75)
    FadeToBright(1000, 0)
    OP_0D()
    OP_9B(0x1, 0x21, 0xB4, 0xFA, 0x3E8, 0x0)
    OP_9B(0x1, 0x1F, 0xB4, 0xFA, 0x3E8, 0x0)
    OP_9B(0x1, 0x1E, 0xB4, 0xFA, 0x3E8, 0x0)
    SetChrChipByIndex(0x21, 0x1F)
    BeginChrThread(0x21, 3, 0, 74)
    BeginChrThread(0x27, 1, 0, 78)

    def lambda_A675():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A675)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x1F)
    BeginChrThread(0x20, 3, 0, 74)

    def lambda_A6FF():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A6FF)
    Sleep(500)
    SetChrChipByIndex(0x1F, 0x1F)
    BeginChrThread(0x1F, 3, 0, 74)

    def lambda_A726():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A726)
    Sleep(500)
    SetChrChipByIndex(0x1E, 0x1F)
    BeginChrThread(0x1E, 3, 0, 74)

    def lambda_A74D():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A74D)
    Sleep(300)
    SetChrChipByIndex(0x1D, 0x1F)
    BeginChrThread(0x1D, 3, 0, 74)

    def lambda_A774():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A774)

    ChrTalk(
        0x101,
        "#00005F#11PWhat!?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    SetChrPos(0x1D, -68250, 0, 156100, 0)
    SetChrPos(0x1E, -67130, 0, 153980, 0)
    SetChrPos(0x1F, -69080, 0, 153530, 0)
    SetChrPos(0x20, -68260, 0, 151500, 0)
    SetChrPos(0x21, -66520, 0, 150830, 0)
    OP_68(-68330, 3500, 153190, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-68330, 850, 175360, 5000)
    MoveCamera(45, 20, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(40000, 5000)

    def lambda_A86F():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A86F)
    Sleep(50)

    def lambda_A887():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A887)
    Sleep(50)

    def lambda_A89F():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A89F)
    Sleep(50)

    def lambda_A8B7():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A8B7)
    Sleep(50)

    def lambda_A8CF():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A8CF)
    Sleep(4500)
    OP_0D()
    EndChrThread(0x27, 0x1)
    Fade(500)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x101, -38850, 0, 120000, 315)
    SetChrPos(0x103, -37350, 0, 120000, 315)
    SetChrPos(0x106, -38300, 0, 118050, 315)
    SetChrPos(0x105, -36900, 0, 117900, 315)
    SetChrPos(0x107, -36050, 0, 120100, 315)
    OP_68(-37500, 1000, 118590, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-42100, 1000, 123390, 2000)
    MoveCamera(0, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20000, 2000)
    BeginChrThread(0x27, 2, 0, 79)

    def lambda_A9FD():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A9FD)
    Sleep(50)

    def lambda_AA15():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AA15)
    Sleep(50)

    def lambda_AA2D():
        OP_9B(0x0, 0x106, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_AA2D)
    Sleep(50)

    def lambda_AA45():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AA45)
    Sleep(50)

    def lambda_AA5D():
        OP_9B(0x0, 0x107, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AA5D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    EndChrThread(0x27, 0x2)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00013F#11PDid they flee towards\x01",
            "the tunnel path...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(250)

    ChrTalk(
        0x106,
        (
            "#10703F#6P... Could it be that\x01",
            "there have been movements\x01",
            "in the Mainz region?\x02\x03",
            "#10701FLike Red Constellation\x01",
            "starting a Resistance-\x01",
            "hunt...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_ABBB():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ABBB)
    Sleep(0)

    def lambda_ABCB():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ABCB)
    Sleep(0)

    def lambda_ABDB():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ABDB)
    Sleep(0)

    def lambda_ABEB():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_ABEB)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        "#00007F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PHmm... That could very well\x01",
            "be the case.\x02\x03",
            "#10401FSo then, the force we engaged\x01",
            "could have been the rear-\x01",
            "guard patrolling the area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI think that's likely...\x02\x03",
            "#00201FThey seemed to have withdrawn\x01",
            "to a nearby area with some\x01",
            "kind of goal in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PGuh... Let's head\x01",
            "towards Mainz!\x02\x03",
            "If we don't act soon,\x01",
            "the resistance will be\x01",
            "in danger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#11P#3CYes, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_37()
    SetChrPos(0x0, -43100, 0, 124250, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 3)
    OP_29(0xAF, 0x1, 0xA)
    ModifyEventFlags(0, 2, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_77_A456 end

    def Function_78_AE0A(): pass

    label("Function_78_AE0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE2C")
    Sound(845, 0, 40, 0)
    Sleep(100)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Jump("Function_78_AE0A")

    label("loc_AE2C")

    Return()

    # Function_78_AE0A end

    def Function_79_AE2D(): pass

    label("Function_79_AE2D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE46")
    Sound(845, 0, 40, 0)
    Sleep(440)
    Jump("Function_79_AE2D")

    label("loc_AE46")

    Return()

    # Function_79_AE2D end

    def Function_80_AE47(): pass

    label("Function_80_AE47")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AECA")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business in the\x01",
            "mining town area. Let's focus on\x01",
            "the accident investigation for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF39")

    ChrTalk(
        0x101,
        (
            "#00000FLet's visit the Doll\x01",
            "Studio first, before\x01",
            "going to Mainz.\x02\x03",
            "We might learn\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF39")

    OP_5A()
    SetChrPos(0x0, -38960, 10, 120380, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x4)
    Return()

    # Function_80_AE47 end

    def Function_81_AF52(): pass

    label("Function_81_AF52")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FRandy should've gone below the\x01",
            "cliff from a rope on higher\x01",
            "ground. Hurry, after him!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -9050, 0, 28880, 90)
    EventEnd(0x4)
    Return()

    # Function_81_AF52 end

    def Function_82_AFCA(): pass

    label("Function_82_AFCA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South - Crossbell City 159 selge\x01",
            "North - Mining Town Mainz 152 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_82_AFCA end

    SaveToFile()

Try(main)
