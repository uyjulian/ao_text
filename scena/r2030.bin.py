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

    Sepith("Sepith_B1D9", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_B1E9", 5,   2,   0,   3,   0,   3,   2)
    Sepith("Sepith_B1D1", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_B1E1", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_B1C9", 6,   0,   0,   3,   2,   4,   0)

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
        "BattleInfo_AB4", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_B1D9", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C18", 0x0010, 52, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_B1E9", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_B50", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_B1D1", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_94C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_CE0", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_B1E1", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_96C", "MonsterBattlePostion_9CC", "ed7450", "ed7453", "ATBonus_90C"),
        )
    )

    BattleInfo(
        "BattleInfo_9EC", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_B1C9", 30, 40, 20, 10,
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
        "Function_7_1FE2",         # 07, 7
        "Function_8_2340",         # 08, 8
        "Function_9_269E",         # 09, 9
        "Function_10_29D7",        # 0A, 10
        "Function_11_29DB",        # 0B, 11
        "Function_12_2BFF",        # 0C, 12
        "Function_13_2D32",        # 0D, 13
        "Function_14_2E45",        # 0E, 14
        "Function_15_2E7B",        # 0F, 15
        "Function_16_2ECC",        # 10, 16
        "Function_17_2F60",        # 11, 17
        "Function_18_300C",        # 12, 18
        "Function_19_3060",        # 13, 19
        "Function_20_3125",        # 14, 20
        "Function_21_3B5A",        # 15, 21
        "Function_22_3BBC",        # 16, 22
        "Function_23_3C2C",        # 17, 23
        "Function_24_3C48",        # 18, 24
        "Function_25_3C8E",        # 19, 25
        "Function_26_41F6",        # 1A, 26
        "Function_27_4206",        # 1B, 27
        "Function_28_4219",        # 1C, 28
        "Function_29_422C",        # 1D, 29
        "Function_30_423F",        # 1E, 30
        "Function_31_489C",        # 1F, 31
        "Function_32_4949",        # 20, 32
        "Function_33_4987",        # 21, 33
        "Function_34_49C8",        # 22, 34
        "Function_35_4A09",        # 23, 35
        "Function_36_4A7C",        # 24, 36
        "Function_37_4A9B",        # 25, 37
        "Function_38_517F",        # 26, 38
        "Function_39_5243",        # 27, 39
        "Function_40_52A5",        # 28, 40
        "Function_41_52B5",        # 29, 41
        "Function_42_63DB",        # 2A, 42
        "Function_43_696F",        # 2B, 43
        "Function_44_69A3",        # 2C, 44
        "Function_45_69F3",        # 2D, 45
        "Function_46_6A43",        # 2E, 46
        "Function_47_6A5D",        # 2F, 47
        "Function_48_80CA",        # 30, 48
        "Function_49_811A",        # 31, 49
        "Function_50_8133",        # 32, 50
        "Function_51_814C",        # 33, 51
        "Function_52_81D0",        # 34, 52
        "Function_53_8243",        # 35, 53
        "Function_54_82C7",        # 36, 54
        "Function_55_833A",        # 37, 55
        "Function_56_83AD",        # 38, 56
        "Function_57_8417",        # 39, 57
        "Function_58_8427",        # 3A, 58
        "Function_59_8738",        # 3B, 59
        "Function_60_875D",        # 3C, 60
        "Function_61_8782",        # 3D, 61
        "Function_62_87A7",        # 3E, 62
        "Function_63_87CC",        # 3F, 63
        "Function_64_87F1",        # 40, 64
        "Function_65_8C29",        # 41, 65
        "Function_66_8C39",        # 42, 66
        "Function_67_8FFE",        # 43, 67
        "Function_68_9258",        # 44, 68
        "Function_69_9DE8",        # 45, 69
        "Function_70_9E2D",        # 46, 70
        "Function_71_9E81",        # 47, 71
        "Function_72_9EE6",        # 48, 72
        "Function_73_9F01",        # 49, 73
        "Function_74_A552",        # 4A, 74
        "Function_75_A580",        # 4B, 75
        "Function_76_A5AE",        # 4C, 76
        "Function_77_A5C8",        # 4D, 77
        "Function_78_AF6E",        # 4E, 78
        "Function_79_AF91",        # 4F, 79
        "Function_80_AFAB",        # 50, 80
        "Function_81_B09B",        # 51, 81
        "Function_82_B126",        # 52, 82
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1F92")

    Jump("loc_1FD6")

    label("loc_1F97")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1FD6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1DC6 end

    def Function_7_1FE2(): pass

    label("Function_7_1FE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_219A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_217B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2176")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2173")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2098():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2098)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2155")
    Call(1, 5)
    Jump("loc_216E")

    label("loc_2155")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_216B")
    Call(1, 4)
    Jump("loc_216E")

    label("loc_216B")

    Call(1, 3)

    label("loc_216E")

    Jump("loc_2176")

    label("loc_2173")

    Call(1, 1)

    label("loc_2176")

    Jump("loc_2191")

    label("loc_217B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2191")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2191")

    TalkEnd(0xFF)
    Return()

    label("loc_219A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_2325")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2320")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_231D")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2242():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2242)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2318")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22FF")
    Call(1, 5)
    Jump("loc_2318")

    label("loc_22FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2315")
    Call(1, 4)
    Jump("loc_2318")

    label("loc_2315")

    Call(1, 3)

    label("loc_2318")

    Jump("loc_2320")

    label("loc_231D")

    Call(1, 1)

    label("loc_2320")

    Jump("loc_233B")

    label("loc_2325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_233B")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_233B")

    TalkEnd(0xFF)
    Return()

    # Function_7_1FE2 end

    def Function_8_2340(): pass

    label("Function_8_2340")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24F8")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_24D9")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D4")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_24D1")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_23F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23F6)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24CC")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24B3")
    Call(1, 5)
    Jump("loc_24CC")

    label("loc_24B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24C9")
    Call(1, 4)
    Jump("loc_24CC")

    label("loc_24C9")

    Call(1, 3)

    label("loc_24CC")

    Jump("loc_24D4")

    label("loc_24D1")

    Call(1, 1)

    label("loc_24D4")

    Jump("loc_24EF")

    label("loc_24D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_24EF")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_24EF")

    TalkEnd(0xFF)
    Return()

    label("loc_24F8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2683")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267E")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_267B")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_25A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_25A0)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2676")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_265D")
    Call(1, 5)
    Jump("loc_2676")

    label("loc_265D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2673")
    Call(1, 4)
    Jump("loc_2676")

    label("loc_2673")

    Call(1, 3)

    label("loc_2676")

    Jump("loc_267E")

    label("loc_267B")

    Call(1, 1)

    label("loc_267E")

    Jump("loc_2699")

    label("loc_2683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2699")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2699")

    TalkEnd(0xFF)
    Return()

    # Function_8_2340 end

    def Function_9_269E(): pass

    label("Function_9_269E")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26D0")
    SetScenarioFlags(0x31, 2)

    label("loc_26D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2710")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2705")
    Sound(2499, 255, 100, 0)
    Jump("loc_270B")

    label("loc_2705")

    Sound(3537, 255, 100, 0)

    label("loc_270B")

    Jump("loc_2716")

    label("loc_2710")

    Sound(3344, 255, 100, 0)

    label("loc_2716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2789")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2769"),
        (SWITCH_DEFAULT, "loc_277A"),
    )


    label("loc_2769")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2784")

    label("loc_277A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2784")

    Jump("loc_29C4")

    label("loc_2789")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_27BB")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_27BB")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27ED"),
        (1, "loc_28F1"),
        (2, "loc_2982"),
        (SWITCH_DEFAULT, "loc_29BA"),
    )


    label("loc_27ED")

    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_74(0x2, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_281E")
    OP_70(0x2, 0x12C)
    OP_71(0x2, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_282E")

    label("loc_281E")

    OP_70(0x2, 0xF0)
    OP_71(0x2, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_282E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2884")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2884")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A7")
    Sound(461, 0, 100, 0)

    label("loc_28A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28C7")
    OP_70(0x2, 0x14A)
    OP_71(0x2, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_28D7")

    label("loc_28C7")

    OP_70(0x2, 0x10E)
    OP_71(0x2, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_28D7")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x2, "light", 0x1, 0x1)
    OP_70(0x2, 0x0)
    Jump("loc_2716")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2963")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2926")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_293E")

    label("loc_2926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2939")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_293E")

    label("loc_2939")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_293E")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_297D")

    label("loc_2963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2973")
    OP_AF(0xFB)
    Jump("loc_297D")

    label("loc_2973")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_297D")

    Jump("loc_29C4")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29B5")

    label("loc_299B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_29AB")
    OP_AF(0xFB)
    Jump("loc_29B5")

    label("loc_29AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29B5")

    Jump("loc_29C4")

    label("loc_29BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29C4")

    Jump("loc_2716")

    label("loc_29C9")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_269E end

    def Function_10_29D7(): pass

    label("Function_10_29D7")

    Call(1, 6)
    Return()

    # Function_10_29D7 end

    def Function_11_29DB(): pass

    label("Function_11_29DB")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD9")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus stop signboard,\x01",
            "you will be able to ride the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to various places\x01",
            "the same way you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_2AD9")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
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
            "Quit\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6E")
    Call(0, 12)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2BF7")

    label("loc_2B6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE6")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business in the\x01",
            "Mining Town area. Let's focus on the\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    label("loc_2BE6")

    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_2BF7")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_11_29DB end

    def Function_12_2BFF(): pass

    label("Function_12_2BFF")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2D2E")
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

    def lambda_2CE5():
        OP_95(0xFE, -31020, 0, 111190, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CE5)
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

    label("loc_2D2E")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_12_2BFF end

    def Function_13_2D32(): pass

    label("Function_13_2D32")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2E41")
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

    label("loc_2E41")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_2D32 end

    def Function_14_2E45(): pass

    label("Function_14_2E45")

    OP_95(0xD, -28360, 0, 100110, 4000, 0x0)
    OP_9E(0xD, 0xFFFF67A8, 0x19064, 0xFFFF15A0, 0xFA0, 0x1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_14_2E45 end

    def Function_15_2E7B(): pass

    label("Function_15_2E7B")

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

    # Function_15_2E7B end

    def Function_16_2ECC(): pass

    label("Function_16_2ECC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2F27")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F1C")
    Sound(2502, 255, 100, 0)
    Jump("loc_2F22")

    label("loc_2F1C")

    Sound(2503, 255, 100, 0)

    label("loc_2F22")

    Jump("loc_2F4B")

    label("loc_2F27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F45")
    Sound(3347, 255, 100, 0)
    Jump("loc_2F4B")

    label("loc_2F45")

    Sound(3348, 255, 100, 0)

    label("loc_2F4B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2ECC end

    def Function_17_2F60(): pass

    label("Function_17_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6E")
    Call(0, 66)
    Return()

    label("loc_2F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2F7B")
    Call(0, 67)
    Return()

    label("loc_2F7B")

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
            "Use the Rope and Go Down\x01",      # 0
            "Step Away\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FDF"),
        (1, "loc_2FFF"),
        (SWITCH_DEFAULT, "loc_300B"),
    )


    label("loc_2FDF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("m4150", 100, 0, 0)
    IdleLoop()
    Jump("loc_300B")

    label("loc_2FFF")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_300B")

    label("loc_300B")

    Return()

    # Function_17_2F60 end

    def Function_18_300C(): pass

    label("Function_18_300C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_305C")
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

    label("loc_305C")

    Call(0, 11)
    Return()

    # Function_18_300C end

    def Function_19_3060(): pass

    label("Function_19_3060")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
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
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3120")
    OP_E2(0x2)
    MiniGame(0x6, 0xA, 0xFFFF1820, 0x0, 0x239CE, 0x0, 0xFFFF3EEA, 0xFFFFF448, 0x25CCE)

    label("loc_3120")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_3060 end

    def Function_20_3125(): pass

    label("Function_20_3125")

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
            "Uh uh, my business here\x01",
            "is finished. Should it be\x01",
            "about time to go back?\x02\x03",
            "Oops, before that, I\x01",
            "guess I'll drop by the\x01",
            "old mine or whatever...\x02",
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
            "#04804F#11PUhuhu, please be very careful.\x02\x03",
            "#04802FAs for me, I have a\x01",
            "mission to perform now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xE,
        (
            "#04704F#6PUh uh, do your very worst.\x02\x03",
            "#04700FOh, right, our assignments for the\x01",
            "current plan have been decided.\x02\x03",
            "You, I and the 7th Anguis are\x01",
            "going to be in charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04805F#11PEeh, that person is coming?\x02\x03",
            "#04804FWell, this time it seems that a lot\x01",
            "of bothersome guys are acting.\x02\x03",
            "#04800FIt could be a good decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04704F#6PUh uh, exactly.\x02\x03",
            "#04702FAlso, I leave to you the operation\x01",
            "report for the "Astral Code".\x02\x03",
            "I'm interested in how much it can\x01",
            "show its worth in a low level\x01",
            "network environment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04806F#11PYes, yes.\x01",
            "I'll put it together when I've got free time.\x02\x03",
            "#04800FThen──\x01",
            "For the sake of our outstanding "Grandmaster".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04704F#6PFor the sake of our great "Grandmaster".\x02",
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
            "#04804F#11P...Uh uh.\x01",
            "Then, although no one is watching,\x01",
            "I think I'll make a promise.\x02",
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
            "#3704V#30WEnforcer No. 0,\x01",
            "Campanella "The Fool"──\x02\x03",
            "#3705VI'll now start to watch over\x01",
            "the "Phantasmal Blaze Plan"\x01",
            "as the Grandmaster's proxy.\x02",
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

    # Function_20_3125 end

    def Function_21_3B5A(): pass

    label("Function_21_3B5A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -68150, 320, 183420)
    OP_9F(0x1, -68100, 320, 164160)
    OP_9F(0x1, -65680, 320, 151380)
    OP_9F(0x1, -58980, 320, 141230)
    OP_9F(0x1, -44990, 320, 127010)
    OP_9F(0x1, -36840, 120, 117770)
    OP_9F(0x2, 0xFE, 11000, 0x6)
    Return()

    # Function_21_3B5A end

    def Function_22_3BBC(): pass

    label("Function_22_3BBC")

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

    # Function_22_3BBC end

    def Function_23_3C2C(): pass

    label("Function_23_3C2C")

    Sleep(500)
    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(457, 0, 80, 0)
    Sleep(5000)
    Sound(458, 0, 80, 0)
    Return()

    # Function_23_3C2C end

    def Function_24_3C48(): pass

    label("Function_24_3C48")

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

    # Function_24_3C48 end

    def Function_25_3C8E(): pass

    label("Function_25_3C8E")

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
            "#00006F#5P*whew*...\x02\x03",
            "#00000FIn the end, we came walking up\x01",
            "to here without using the car.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00102F#11PWell, the scenery was beautiful,\x01",
            "so I think it was nice, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#10112F#6PR-Right.\x01",
            "(A bit of a pity, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh boy, I didn't think it was a duty\x01",
            "post that made you walk this much.\x02\x03",
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

    def lambda_3F60():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F60)
    Sleep(50)

    def lambda_3F70():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F70)
    Sleep(50)

    def lambda_3F80():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F80)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#6P#NThe road continues in that direction too...\x01",
            "Is something over there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#6P...Yeah...\x01",
            "The "Rosenberg Studio".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThere lives a doll maker\x01",
            "with a bit of a history...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6P#NEeh, that doll studio highly regarded \x01",
            "among a selected few, eh?\x02\x03",
            "#10302FBy the way, weren't they planning to\x01",
            "actually exhibit one doll in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah...that happened too.\x02\x03",
            "#00008F(In the end, it's not yet clear\x01",
            "whose deed that was.)\x02\x03",
            "#00001F(Renne is not there anymore, but...\x01",
            "Should we go check the situation?)\x02",
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

    # Function_25_3C8E end

    def Function_26_41F6(): pass

    label("Function_26_41F6")

    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_26_41F6 end

    def Function_27_4206(): pass

    label("Function_27_4206")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_27_4206 end

    def Function_28_4219(): pass

    label("Function_28_4219")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_28_4219 end

    def Function_29_422C(): pass

    label("Function_29_422C")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xF, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_29_422C end

    def Function_30_423F(): pass

    label("Function_30_423F")

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

    def lambda_4409():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4409)
    Sleep(50)

    def lambda_4419():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4419)
    Sleep(50)

    def lambda_4429():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4429)
    Sleep(50)

    ChrTalk(
        0x102,
        (
            "#00109F#6P*giggle*, like we heard, the mountain\x01",
            "path region has clear weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, the scenery after\x01",
            "the rain was pretty, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHmm, but still, this\x01",
            "car is something else.\x02\x03",
            "#10102FIt doesn't even sway at all on\x01",
            "places like the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PThat's ZCF for you. It seems\x01",
            "it will sell if they put it on sale.\x02\x03",
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

    def lambda_45EF():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45EF)
    Sleep(50)

    def lambda_45FF():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_45FF)
    Sleep(50)

    def lambda_460F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_460F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#12P#NThe road continues in that direction too...\x01",
            "Is something over there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#6P...Yeah...\x01",
            "The "Rosenberg Studio".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#NThere lives a doll maker\x01",
            "with a bit of a history...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#12P#NEeh, that doll studio highly regarded \x01",
            "among a selected few, eh?\x02\x03",
            "#10302FBy the way, weren't they planning to\x01",
            "actually exhibit one doll in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah...that happened too.\x02\x03",
            "#00008F(In the end, it's not yet clear\x01",
            "whose deed that was.)\x02\x03",
            "#00001F(Renne is not there anymore, but...\x01",
            "Should we go check the situation?)\x02",
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

    # Function_30_423F end

    def Function_31_489C(): pass

    label("Function_31_489C")

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

    # Function_31_489C end

    def Function_32_4949(): pass

    label("Function_32_4949")


    def lambda_494E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_494E)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_32_4949 end

    def Function_33_4987(): pass

    label("Function_33_4987")

    Sleep(1300)

    def lambda_498F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_498F)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_4987 end

    def Function_34_49C8(): pass

    label("Function_34_49C8")

    Sleep(2600)

    def lambda_49D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49D0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_34_49C8 end

    def Function_35_4A09(): pass

    label("Function_35_4A09")

    Sleep(3900)

    def lambda_4A11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A11)
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

    # Function_35_4A09 end

    def Function_36_4A7C(): pass

    label("Function_36_4A7C")

    Sound(458, 0, 80, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    StopSound(458, 2000, 70)
    Sleep(3000)
    Sound(492, 0, 80, 0)
    Return()

    # Function_36_4A7C end

    def Function_37_4A9B(): pass

    label("Function_37_4A9B")

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

    def lambda_4C30():

        label("loc_4C30")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4C30")

    QueueWorkItem2(0x101, 2, lambda_4C30)

    def lambda_4C42():

        label("loc_4C42")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4C42")

    QueueWorkItem2(0x102, 2, lambda_4C42)

    def lambda_4C54():

        label("loc_4C54")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4C54")

    QueueWorkItem2(0x109, 2, lambda_4C54)

    def lambda_4C66():

        label("loc_4C66")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4C66")

    QueueWorkItem2(0x105, 2, lambda_4C66)
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

    def lambda_4CD8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4CD8)
    Sleep(50)

    def lambda_4CE8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CE8)
    Sleep(50)

    def lambda_4CF8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4CF8)
    Sleep(50)

    def lambda_4D08():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4D08)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00109F#6P*giggle*, like we heard, the mountain\x01",
            "path region has clear weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, the scenery after\x01",
            "the rain was pretty, eh?\x02\x03",
            "#00006FStill, although we have a car,\x01",
            "in the end we rode the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PUh uh.\x01",
            "I like buses.\x02\x03",
            "#10102FTheir relaxing feeling\x01",
            "is nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PBecause I rarely ride on them,\x01",
            "it was a rather fresh change.\x02\x03",
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

    def lambda_4ED9():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4ED9)
    Sleep(50)

    def lambda_4EE9():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4EE9)
    Sleep(50)

    def lambda_4EF9():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4EF9)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10300F#6P#NThe road continues in that direction too...\x01",
            "Is something over there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00008F#5P...Yeah...\x01",
            "The "Rosenberg Studio".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P#NThere lives a doll maker\x01",
            "with a bit of a history...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10305F#6P#NEeh, that doll studio highly regarded \x01",
            "among a selected few, eh?\x02\x03",
            "#10302FBy the way, weren't they planning to\x01",
            "actually exhibit one doll in that Auktion?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah...that happened too.\x02\x03",
            "#00008F(In the end, it's not yet clear\x01",
            "whose deed that was.)\x02\x03",
            "#00001F(Renne is not there anymore, but...\x01",
            "Should we go check the situation?)\x02",
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

    # Function_37_4A9B end

    def Function_38_517F(): pass

    label("Function_38_517F")

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

    # Function_38_517F end

    def Function_39_5243(): pass

    label("Function_39_5243")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1388, 0x1)
    ClearMapObjFlags(0x1, 0x1000)
    Return()

    # Function_39_5243 end

    def Function_40_52A5(): pass

    label("Function_40_52A5")

    Sound(471, 0, 100, 0)
    Sleep(3000)
    Sound(473, 0, 100, 0)
    Return()

    # Function_40_52A5 end

    def Function_41_52B5(): pass

    label("Function_41_52B5")

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

    def lambda_53D0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53D0)
    Sleep(50)

    def lambda_53E8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53E8)
    Sleep(50)

    def lambda_5400():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5400)
    Sleep(50)

    def lambda_5418():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5418)
    Sleep(50)

    def lambda_5430():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5430)
    Sleep(50)

    def lambda_5448():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5448)
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

    def lambda_54CA():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54CA)
    Sleep(50)

    def lambda_54DA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_54DA)
    Sleep(50)

    def lambda_54EA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_54EA)
    Sleep(50)

    def lambda_54FA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_54FA)
    Sleep(50)

    def lambda_550A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_550A)
    Sleep(50)

    def lambda_551A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_551A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5POops...\x02",
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
            "#10302F#5PCould some problem have\x01",
            "arised somewhere?\x02",
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
            "#00001FYes, Special Support Section,\x01",
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
            "#2718V#30WAh, Mr. Lloyd!\x02\x03",
            "#2719V#30W*haah*, I could finally reach you.\x02",
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
            "#00002FFran? Thank you for your hard work.\x02\x03",
            "#00005FCould it be that you've been\x01",
            "at the ENIGMA for some time?\x02",
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
            "Yes, but who knows why,\x01",
            "I couldn't get through at all...\x02\x03",
            "I tried with the others'\x01",
            "ENIGMA too.\x02",
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
            "#00008F(It seems that in the Doll Studio\x01",
            "underground there was a device\x01",
            "that jammed the orbal waves...)\x02\x03",
            "#00006FI'm sorry, we were visiting\x01",
            "a bit of a unique place...\x02\x03",
            "#00001FHas something happened?\x01",
            "Was there an urgent Support Request?\x02",
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
            "Actually, 30 minutes ago a train derailment\x01",
            "accident took place at the West Crossbell Highway.\x02",
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
            "Yes, Crime Investigations Section Two has already\x01",
            "headed there for an on-site inspection.\x02\x03",
            "The CGF too is on the move and\x01",
            "I think there is no need for Mr.\x01",
            "Lloyd and the others to go to, but...\x02\x03",
            "I thought to contact\x01",
            "you just in case.\x02",
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
            "#00006FI see...\x01",
            "Thank you, Fran.\x02\x03",
            "#00000FIf you have some additional information,\x01",
            "I want you to convey it to us too.\x02",
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
        "#00200F#5P...Any problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PIt seemed it was\x01",
            "a call from Fran...\x02",
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
        "#00013F#6PYes...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained about the derailment accident that\x01",
            "took place at the West Crossbell Highway.\x07\x00\x02",
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
        "#00307F#11PWhat did you say...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PA derailment...\x01",
            "The orbal railway, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. She said that since Section Two\x01",
            "and the CGF are already heading there,\x01",
            "we can leave things to them...\x02",
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
        "#00206F#5P...As you can expect, it is worrisome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PYeah, the timin' is too good in\x01",
            "the current suspicious situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, it seems a tad difficult to\x01",
            "think about it as a mere accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#11PMr. Lloyd...\x02",
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
            "#00006F#6PWe should report all the intel about\x01",
            "the "Society" by today's end.\x02\x03",
            "#00001FLet's try going to the\x01",
            "accident site now.\x02\x03",
            "#00000FWas it the act of those "Cryptids"\x01",
            "or some kind of organization...?\x02\x03",
            "We should at least able to help\x01",
            "on the on-site inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PThen, let's make haste.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_615A")

    ChrTalk(
        0x104,
        (
            "#00306F#11PFor this, it seems the best would be\x01",
            "to go there in a jiffy with the car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6203")

    label("loc_615A")


    ChrTalk(
        0x104,
        (
            "#00305F#11PThe car... we stopped it in a\x01",
            "totally different place, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#5PLet's contact the CGF on patrol and\x01",
            "have it delivered to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6203")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Train Accident Site" was added \x01",
            "to the orbal car destinations.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6299")
    Jump("loc_6327")

    label("loc_6299")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The car that was parked in a different place went\x01",
            "back to the Special Support Section back entrance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6327")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6387")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6382")
    Jump("loc_6387")

    label("loc_6382")

    OP_29(0x85, 0x4, 0x40)

    label("loc_6387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6398")
    Jump("loc_639D")

    label("loc_6398")

    OP_29(0x86, 0x4, 0x40)

    label("loc_639D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_63AE")
    Jump("loc_63B3")

    label("loc_63AE")

    OP_29(0x87, 0x4, 0x40)

    label("loc_63B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_63C4")
    Jump("loc_63C9")

    label("loc_63C4")

    OP_29(0x89, 0x4, 0x40)

    label("loc_63C9")

    ModifyEventFlags(1, 3, 0x80)
    ReplaceBGM("ed7150", "ed7151")
    OP_24(0x323)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_41_52B5 end

    def Function_42_63DB(): pass

    label("Function_42_63DB")

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

    def lambda_6670():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6670)
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

    # Function_42_63DB end

    def Function_43_696F(): pass

    label("Function_43_696F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69A2")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6996")
    OP_4C(0xFE, 0x3)
    Jump("loc_699A")

    label("loc_6996")

    OP_4B(0xFE, 0x3)

    label("loc_699A")

    Sleep(500)
    Jump("Function_43_696F")

    label("loc_69A2")

    Return()

    # Function_43_696F end

    def Function_44_69A3(): pass

    label("Function_44_69A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69F2")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("Function_44_69A3")

    label("loc_69F2")

    Return()

    # Function_44_69A3 end

    def Function_45_69F3(): pass

    label("Function_45_69F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A42")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    Jump("Function_45_69F3")

    label("loc_6A42")

    Return()

    # Function_45_69F3 end

    def Function_46_6A43(): pass

    label("Function_46_6A43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A5C")
    Sound(356, 0, 70, 0)
    Sleep(1000)
    Jump("Function_46_6A43")

    label("loc_6A5C")

    Return()

    # Function_46_6A43 end

    def Function_47_6A5D(): pass

    label("Function_47_6A5D")

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

    def lambda_6E7A():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6E7A)
    Sleep(50)

    def lambda_6E92():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E92)
    Sleep(50)

    def lambda_6EAA():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6EAA)
    Sleep(50)

    def lambda_6EC2():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6EC2)
    Sleep(50)

    def lambda_6EDA():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6EDA)
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

    def lambda_6FF0():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6FF0)
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

    def lambda_70DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_70DA)

    def lambda_70EB():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_70EB)
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

    def lambda_72A7():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_72A7)

    def lambda_72C0():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_72C0)

    def lambda_72D9():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_72D9)

    def lambda_72F2():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_72F2)

    def lambda_730B():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_730B)
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
        "#11PH-Hide behind the vehicle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04611FAH HA HA, it's useleeess!\x02",
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

    def lambda_7665():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7665)
    SetChrChipByIndex(0x13, 0x26)

    def lambda_767E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_767E)
    SetChrChipByIndex(0x14, 0x26)

    def lambda_7697():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7697)
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
        "#04612F#12P#4S#10AAH HA HA HA HA HA HA HA HAH!!\x02",
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
        "Iiiih...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Y-You monster...!?\x02",
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

    def lambda_7A54():

        label("loc_7A54")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_7A54")

    QueueWorkItem2(0x15, 2, lambda_7A54)

    def lambda_7A66():

        label("loc_7A66")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_7A66")

    QueueWorkItem2(0x16, 2, lambda_7A66)
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
            "#04612F#5P#4S#26AHyahhoo!\x01",
            "Ah ha ha ha ha ha ha ha ha hah!!!\x02",
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

    # Function_47_6A5D end

    def Function_48_80CA(): pass

    label("Function_48_80CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8119")
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 100, 800, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x2, 0x3)
    Jump("Function_48_80CA")

    label("loc_8119")

    Return()

    # Function_48_80CA end

    def Function_49_811A(): pass

    label("Function_49_811A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8132")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_49_811A")

    label("loc_8132")

    Return()

    # Function_49_811A end

    def Function_50_8133(): pass

    label("Function_50_8133")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_814B")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_50_8133")

    label("loc_814B")

    Return()

    # Function_50_8133 end

    def Function_51_814C(): pass

    label("Function_51_814C")

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

    # Function_51_814C end

    def Function_52_81D0(): pass

    label("Function_52_81D0")

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

    # Function_52_81D0 end

    def Function_53_8243(): pass

    label("Function_53_8243")

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

    # Function_53_8243 end

    def Function_54_82C7(): pass

    label("Function_54_82C7")

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

    # Function_54_82C7 end

    def Function_55_833A(): pass

    label("Function_55_833A")

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

    # Function_55_833A end

    def Function_56_83AD(): pass

    label("Function_56_83AD")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_83BF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_83BF)

    def lambda_83D8():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83D8)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_83AD end

    def Function_57_8417(): pass

    label("Function_57_8417")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Return()

    # Function_57_8417 end

    def Function_58_8427(): pass

    label("Function_58_8427")

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

    def lambda_84F5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84F5)
    Sleep(100)

    def lambda_850D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_850D)
    Sleep(100)

    def lambda_8525():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8525)
    Sleep(100)

    def lambda_853D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_853D)
    Sleep(100)

    def lambda_8555():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8555)
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
        "#00013F#11PThe high ground before the waterfall...there!\x02",
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

    def lambda_864D():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_864D)
    Sleep(30)

    def lambda_865D():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_865D)
    Sleep(30)

    def lambda_866D():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_866D)
    Sleep(30)

    def lambda_867D():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_867D)
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
            "#00201F...Just like according\x01",
            "to Mr. Cao's intel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107FLet's go...!\x02",
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

    # Function_58_8427 end

    def Function_59_8738(): pass

    label("Function_59_8738")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_875C")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    Jump("Function_59_8738")

    label("loc_875C")

    Return()

    # Function_59_8738 end

    def Function_60_875D(): pass

    label("Function_60_875D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8781")
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    Jump("Function_60_875D")

    label("loc_8781")

    Return()

    # Function_60_875D end

    def Function_61_8782(): pass

    label("Function_61_8782")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87A6")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    Jump("Function_61_8782")

    label("loc_87A6")

    Return()

    # Function_61_8782 end

    def Function_62_87A7(): pass

    label("Function_62_87A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87CB")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Jump("Function_62_87A7")

    label("loc_87CB")

    Return()

    # Function_62_87A7 end

    def Function_63_87CC(): pass

    label("Function_63_87CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87F0")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    Jump("Function_63_87CC")

    label("loc_87F0")

    Return()

    # Function_63_87CC end

    def Function_64_87F1(): pass

    label("Function_64_87F1")

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
        "#00013F#11PThe high ground before the waterfall...there!\x02",
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

    def lambda_8B32():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8B32)
    Sleep(30)

    def lambda_8B42():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8B42)
    Sleep(30)

    def lambda_8B52():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8B52)
    Sleep(30)

    def lambda_8B62():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8B62)
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
            "#00201F...Just like according\x01",
            "to Mr. Cao's intel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0x102,
        "#00107FLet's go...!\x02",
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

    # Function_64_87F1 end

    def Function_65_8C29(): pass

    label("Function_65_8C29")

    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(492, 0, 70, 0)
    Return()

    # Function_65_8C29 end

    def Function_66_8C39(): pass

    label("Function_66_8C39")

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
            "#10306F#11PIt really seems he went down\x01",
            "the cliff from this place.\x02\x03",
            "#10308FHowever...\x01",
            "I wonder what's down there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#5PThe rope seems to go down\x01",
            "into the rocky ravine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P...In any case, it seems the only\x01",
            "thing we can do is to go down.\x02",
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
            "Descend Immediately\x01",      # 0
            "Make Preparations\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8E3F"),
        (1, "loc_8FD9"),
        (SWITCH_DEFAULT, "loc_8FFD"),
    )


    label("loc_8E3F")


    def lambda_8E44():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E44)
    Sleep(50)

    def lambda_8E54():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E54)
    Sleep(50)

    def lambda_8E64():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E64)
    Sleep(50)

    def lambda_8E74():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E74)
    Sleep(50)

    def lambda_8E84():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E84)
    Sleep(50)

    def lambda_8E94():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E94)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00001F#6P──All right.\x01",
            "Everyone, are you ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PI am okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PNo problem here too.\x02",
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
            "#00101F#5P──Let's go.\x01",
            "We must catch Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAll right...everyone, be careful\x01",
            "and go down the rope.\x02",
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
    Jump("loc_8FFD")

    label("loc_8FD9")

    SetChrPos(0x0, -57350, 6000, 65950, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_8FFD")

    label("loc_8FFD")

    Return()

    # Function_66_8C39 end

    def Function_67_8FFE(): pass

    label("Function_67_8FFE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The rope connected to the\x01",
            "cliff below has been severed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9255")

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703FIt seems it was severed\x01",
            "with a sharp edged too.\x02\x03",
            "#10701FI wonder where this\x01",
            "rope connected to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403FWell, actually Randy used\x01",
            "this before to go down to\x01",
            "the old abandoned mine.\x02\x03",
            "#10400FIf you go through that, so\x01",
            "can exit to the Mainz area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10703FI see, there's such a route...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FCould it be the "Red Constellation"\x01",
            "that has cut the rope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FReally, it's highly possible\x01",
            "under these circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402FUh uh, how cunning of them.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CE, 1)

    label("loc_9255")

    EventEnd(0x3)
    Return()

    # Function_67_8FFE end

    def Function_68_9258(): pass

    label("Function_68_9258")

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

    def lambda_945D():
        OP_96(0xFE, 0xFFFF89D6, 0xDAC, 0x19672, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_945D)

    def lambda_9477():
        OP_96(0xFE, 0xFFFF89D6, 0xDAC, 0x19672, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9477)
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

    def lambda_9601():
        OP_96(0xFE, 0xFFFF89D6, 0x3C8C, 0x19672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9601)

    def lambda_961B():
        OP_96(0xFE, 0xFFFF89D6, 0x3C8C, 0x19672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_961B)
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
            "#10404F#11PWell then, the Resistance\x01",
            "is on the mountain path area...\x02\x03",
            "#10402FFirst of all, should we\x01",
            "head towards Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PRight, I'm worried about\x01",
            "Mainz situation too...\x02\x03",
            "#00008FHowever...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-27500, 1700, 92100, 2000)
    MoveCamera(43, 12, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_97FB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97FB)
    Sleep(1000)

    def lambda_980B():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_980B)
    Sleep(50)

    def lambda_981B():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_981B)
    Sleep(50)

    def lambda_982B():
        OP_93(0x106, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_982B)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10401F#12PI understand...\x01",
            "That place too bothers you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThe "Rosenberg Doll Studio", one\x01",
            "of the "Thirteen Workshops", right?\x02\x03",
            "#00201FPreviously, he said he maybe would\x01",
            "have talked to us on another\x01",
            "occasion, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6PIs that so...?\x02\x03",
            "#10703F...Actually, before, I tried\x01",
            "to infiltrate inside, but...\x02\x03",
            "#10710FIts underground structure was so staggering\x01",
            "complex that I had to give up.\x02",
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
            "#01203F#12P#3CHm, Jｶrg, eh?\x02\x03",
            "#01200FI haven't seen him in a while, but\x01",
            "it seems he's healthy as always.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9AC6():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9AC6)
    Sleep(50)

    def lambda_9AD6():
        TurnDirection(0x103, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9AD6)
    Sleep(50)

    def lambda_9AE6():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9AE6)
    Sleep(50)

    def lambda_9AF6():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9AF6)
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
            "with that old mister too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CHm, we know each other's\x01",
            "circumstances to a certain degree.\x02\x03",
            "#01200FHe's a member of the "Snake" and an\x01",
            "amazing old-fashioned craftsman.\x02\x03",
            "No doubt he's a character\x01",
            "you can trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PI'd like to know more information\x01",
            "about the "Society", so it could\x01",
            "be worth paying him a visit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9CBC():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9CBC)
    Sleep(50)

    def lambda_9CCC():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9CCC)
    Sleep(50)

    def lambda_9CDC():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9CDC)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        (
            "#00202F#12PWhy don't we make a stop there\x01",
            "before going to Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, let's do that.\x02",
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

    # Function_68_9258 end

    def Function_69_9DE8(): pass

    label("Function_69_9DE8")

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

    # Function_69_9DE8 end

    def Function_70_9E2D(): pass

    label("Function_70_9E2D")

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

    # Function_70_9E2D end

    def Function_71_9E81(): pass

    label("Function_71_9E81")

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

    # Function_71_9E81 end

    def Function_72_9EE6(): pass

    label("Function_72_9EE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F00")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_72_9EE6")

    label("loc_9F00")

    Return()

    # Function_72_9EE6 end

    def Function_73_9F01(): pass

    label("Function_73_9F01")

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

    def lambda_A053():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A053)
    Sleep(10)

    def lambda_A06B():
        OP_9B(0x0, 0x106, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_A06B)
    Sleep(10)

    def lambda_A083():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A083)
    Sleep(10)

    def lambda_A09B():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A09B)
    Sleep(10)

    def lambda_A0B3():
        OP_9B(0x0, 0x107, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A0B3)
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
        "#00201F#5PThis presence is...!?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x106,
        "#10707F#11PMilitary monsters, incoming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWhat...!?\x02",
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

    def lambda_A2E7():
        OP_96(0xFE, 0xFFFFB2A8, 0x0, 0x19834, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A2E7)
    Sleep(300)
    BeginChrThread(0x1E, 3, 0, 74)

    def lambda_A30A():
        OP_96(0xFE, 0xFFFFD634, 0xFA0, 0x18BE6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A30A)
    Sleep(300)
    BeginChrThread(0x1F, 3, 0, 74)

    def lambda_A32D():
        OP_96(0xFE, 0xFFFFE34A, 0x1F4, 0x1B198, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A32D)
    Sleep(300)

    def lambda_A34A():
        OP_9D(0xFE, 0xFFFFC888, 0x7D0, 0x1CB60, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A34A)
    Sleep(300)
    Sound(809, 0, 60, 0)
    BeginChrThread(0x21, 3, 0, 74)

    def lambda_A376():
        OP_96(0xFE, 0xFFFFB082, 0x0, 0x1B8D2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A376)
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
        "#00010F#6PKh...these guys!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10407F#5PHere they come...!\x02",
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

    def lambda_A477():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A477)

    def lambda_A494():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3A98)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A494)

    def lambda_A4B1():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A4B1)

    def lambda_A4CE():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A4CE)

    def lambda_A4EB():
        OP_9D(0xFE, 0xFFFFC46E, 0x0, 0x1ADB0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A4EB)
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

    # Function_73_9F01 end

    def Function_74_A552(): pass

    label("Function_74_A552")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A568")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A57F")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_A568")

    label("loc_A57F")

    Return()

    # Function_74_A552 end

    def Function_75_A580(): pass

    label("Function_75_A580")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A596")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5AD")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_A596")

    label("loc_A5AD")

    Return()

    # Function_75_A580 end

    def Function_76_A5AE(): pass

    label("Function_76_A5AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5C7")
    Sound(845, 0, 80, 0)
    Sleep(500)
    Jump("Function_76_A5AE")

    label("loc_A5C7")

    Return()

    # Function_76_A5AE end

    def Function_77_A5C8(): pass

    label("Function_77_A5C8")

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

    def lambda_A7E7():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A7E7)
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

    def lambda_A871():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A871)
    Sleep(500)
    SetChrChipByIndex(0x1F, 0x1F)
    BeginChrThread(0x1F, 3, 0, 74)

    def lambda_A898():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A898)
    Sleep(500)
    SetChrChipByIndex(0x1E, 0x1F)
    BeginChrThread(0x1E, 3, 0, 74)

    def lambda_A8BF():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A8BF)
    Sleep(300)
    SetChrChipByIndex(0x1D, 0x1F)
    BeginChrThread(0x1D, 3, 0, 74)

    def lambda_A8E6():
        OP_95(0xFE, -29350, 0, 113100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A8E6)

    ChrTalk(
        0x101,
        "#00005F#11PWhat...!?\x02",
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

    def lambda_A9E4():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A9E4)
    Sleep(50)

    def lambda_A9FC():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A9FC)
    Sleep(50)

    def lambda_AA14():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_AA14)
    Sleep(50)

    def lambda_AA2C():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_AA2C)
    Sleep(50)

    def lambda_AA44():
        OP_9B(0x1, 0xFE, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AA44)
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

    def lambda_AB72():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AB72)
    Sleep(50)

    def lambda_AB8A():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AB8A)
    Sleep(50)

    def lambda_ABA2():
        OP_9B(0x0, 0x106, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_ABA2)
    Sleep(50)

    def lambda_ABBA():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ABBA)
    Sleep(50)

    def lambda_ABD2():
        OP_9B(0x0, 0x107, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_ABD2)
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
        "#00013F#11PDid they flee towards the tunnel path...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(250)

    ChrTalk(
        0x106,
        (
            "#10703F#6P...Could it be that there\x01",
            "was some movements\x01",
            "in the Mainz region?\x02\x03",
            "#10701FLike the "Red Constellation" have begun\x01",
            "a Resistance-hunt in earnest...?\x02",
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

    def lambda_AD40():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AD40)
    Sleep(0)

    def lambda_AD50():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AD50)
    Sleep(0)

    def lambda_AD60():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AD60)
    Sleep(0)

    def lambda_AD70():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AD70)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        "#00007F#5PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PHm...it's possible.\x02\x03",
            "#10401FAnd that means that those\x01",
            "now were perhaps patrolling\x01",
            "to guard the corps rear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI think it's highly likely...\x02\x03",
            "#00201FThey seemed to have withdrawn\x01",
            "with some kind of aim in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PKh...\x01",
            "Let's hurry to the Mainz region!\x02\x03",
            "If we dawdle, the Resistance\x01",
            "is going to be in danger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#11P#3CHm, let's go.\x02",
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

    # Function_77_A5C8 end

    def Function_78_AF6E(): pass

    label("Function_78_AF6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF90")
    Sound(845, 0, 40, 0)
    Sleep(100)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Jump("Function_78_AF6E")

    label("loc_AF90")

    Return()

    # Function_78_AF6E end

    def Function_79_AF91(): pass

    label("Function_79_AF91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFAA")
    Sound(845, 0, 40, 0)
    Sleep(440)
    Jump("Function_79_AF91")

    label("loc_AFAA")

    Return()

    # Function_79_AF91 end

    def Function_80_AFAB(): pass

    label("Function_80_AFAB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B00E")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business in the\x01",
            "Mining Town area. Let's focus on the\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B00E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B082")

    ChrTalk(
        0x101,
        (
            "#00000FBefore going to Mainz, let's\x01",
            "visit the Doll Studio first.\x02\x03",
            "We could get some information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B082")

    OP_5A()
    SetChrPos(0x0, -38960, 10, 120380, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x4)
    Return()

    # Function_80_AFAB end

    def Function_81_B09B(): pass

    label("Function_81_B09B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FRandy should have gone down below the\x01",
            "cliff from the rope on the higher ground.\x01",
            "Hurry, let's chase him!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -9050, 0, 28880, 90)
    EventEnd(0x4)
    Return()

    # Function_81_B09B end

    def Function_82_B126(): pass

    label("Function_82_B126")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South - Crossbell City  159 selge\x01",
            "North - Mining Town Mainz  152 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_82_B126 end

    SaveToFile()

Try(main)
