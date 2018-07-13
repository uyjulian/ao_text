from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1010.bin",                # FileName
        "r1010",                    # MapName
        "r1010",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x06,                       # PreInitFunctionIndex
        b'\x00\xff\x04',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 5, 0, 6],
    )

    BuildStringList((
        "r1010",                  # 0
        "Patrol Officer Frantz",  # 1
        "Dahlia",                 # 2
        "Policeman",              # 3
        "Policeman",              # 4
        "Policeman",              # 5
        "CGF Member",             # 6
        "CGF Member",             # 7
        "Grace",                  # 8
        "Reins",                  # 9
        "車",                     # 10
        "暴走車",                 # 11
        "Patrol Car",             # 12
        "Armored Vehicle",        # 13
        "パトカー２",             # 14
        "パトカー３",             # 15
        "装甲車２",               # 16
        "Yuri",                   # 17
        "Sykes",                  # 18
        "Reggie",                 # 19
        "Patrol Officer Kate",    # 20
        "2nd Lt. Mireille",       # 21
        "波紋",                   # 22
        "Ebony Drome",            # 23
        "Ebony Drome",            # 24
        "ガンテ",                 # 25
        "ガンテ",                 # 26
        "クロベルガ蟲",           # 27
        "Cryptid",                # 28
        "SE制御",                 # 29
        "br1000",                 # 30
        "br1000",                 # 31
        "br1000",                 # 32
        "br1000",                 # 33
        "br1000",                 # 34
        "br1000",                 # 35
        "br1000",                 # 36
        "br1000",                 # 37
        "br1000",                 # 38
        "br1000",                 # 39
        "To Crossbell City",      # 40
        "To Bellguard Gate",      # 41
    ))

    ATBonus("ATBonus_904", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_924", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_AAD1", 5,   5,   0,   3,   0,   0,   0)
    Sepith("Sepith_AAD9", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_AAA1", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_AA99", 2,   0,   3,   4,   0,   0,   3)
    Sepith("Sepith_AA91", 4,   2,   3,   0,   3,   0,   0)
    Sepith("Sepith_AAE9", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_964", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_968", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_96C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_970", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_974", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_978", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_97C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_980", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_9C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_9C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_9CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_9D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_9D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_9D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_9DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_944", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_948", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_94C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_950", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_954", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_958", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_95C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_960", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9E8", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_9EC", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_9F0", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_9F4", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_9F8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_9FC", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_A00", 0, 0, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_C5C", 0x0000, 50, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_AAD1", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71500.dat", "ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_B94", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_AAD9", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_D24", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_AAA1", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_ACC", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_AA99", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_A04", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_AA91", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
        )
    )

    BattleInfo(
        "BattleInfo_DEC", 0x0000, 84, 6, 60, 6, 1, 30, 0, "br1000", "Sepith_AAE9", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_964", "MonsterBattlePostion_9C4", "ed7450", "ed7453", "ATBonus_904"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_F10", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7451", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E88", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7453", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_ECC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_944", "MonsterBattlePostion_9C4", "ed7453", "ed7453", "ATBonus_904"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F54", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_9E4", "MonsterBattlePostion_9E4", "ed7454", "ed7453", "ATBonus_924"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch30000.itc",                   # 02
        "chr/ch31200.itc",                   # 03
        "chr/ch31300.itc",                   # 04
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
        "monster/ch60950.itc",               # 10
        "monster/ch60951.itc",               # 11
        "monster/ch74850.itc",               # 12
        "monster/ch74851.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch71550.itc",               # 16
        "monster/ch71551.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
    ))

    DeclNpc(4294922787, 0,       11819,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294916947, 0,       12060,   180,  389,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294906377, 4294959296, 69760,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294896436, 4294959296, 60049,   315,  389,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294895356, 4294959296, 61029,   135,  389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294899407, 4294959296, 74919,   135,  389,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294896296, 4294959296, 67230,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294941717, 0,       4294935356, 270,  485,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294883576, 4294965296, 610,     270,  485,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294941717, 0,       4294935356, 270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294883576, 4294965296, 610,     270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(14569,   500,     4294929447, 0,    484,  0x0, 0,   16,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(7550,    4294965946, 0,       0x1010000,    "BattleInfo_C5C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294950546, 4294947586, 0,       0x1010000,    "BattleInfo_B94", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(10290,   4294923356, 0,       0x1010000,    "BattleInfo_D24", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294956066, 4294928606, 0,       0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294931056, 4294929946, 4294963296, 0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294915906, 4294963277, 0,       0x1010000,    "BattleInfo_B94", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294920156, 30310,   0,       0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294899706, 39710,   4294964296, 0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294911006, 61040,   4294959296, 0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294900576, 72450,   4294959296, 0x1010000,    "BattleInfo_ACC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294890056, 59790,   4294959296, 0x1010000,    "BattleInfo_A04", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294885486, 4294954216, 4294965296, 0x1010000,    "BattleInfo_C5C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294965206, 4294952126, 0,       0x1010000,    "BattleInfo_DEC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294898646, 4294964516, 4294965296, 0x1010000,    "BattleInfo_DEC", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 28,  -44.0,                 0.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.222537994384766,     1.5556354522705078,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 33,  -54.5,                 60.0,                  -9.0,                  900.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   10.90000057220459,     -5.0,                  1.8000000715255737,    1.0])
    DeclEvent(0x0040, 0, 25,  -0.8899999856948853,   -52.72999954223633,    -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   0.11124999821186066,   6.591249942779541,     0.25,                  1.0])
    DeclEvent(0x0000, 0, 26,  3.690000057220459,     25.489999771118164,    2.5,                   576.0,                 [0.04419415816664696,  0.23570235073566437,   -0.0,                  0.0,                   -0.044194187968969345, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.9634333848953247,    -6.877790451049805,    -0.5,                  1.0])
    DeclEvent(0x0000, 0, 61,  -64.08999633789062,    0.0,                   -3.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.817999839782715,    -0.0,                  0.6000000238418579,    1.0])

    DeclActor(4294886376, 4294959296, 60600,   1200,    4294886376, 4294960296, 60600,   0x007C, 0,  7,  0x0000)
    DeclActor(4294894796, 4294964296, 40000,   1200,    4294894796, 4294965296, 40000,   0x007C, 0,  8,  0x0000)
    DeclActor(4294929196, 4294963296, 4294932436, 1200,    4294929196, 4294964296, 4294932436, 0x007C, 0,  9,  0x0000)
    DeclActor(14570,   0,       4294929446, 1200,    14570,   1000,    4294929446, 0x007C, 0,  10, 0x0000)
    DeclActor(4294941716, 0,       4294935356, 1200,    4294941716, 0,       4294935356, 0x007C, 0,  11, 0x0000)
    DeclActor(4294883576, 4294965296, 610,     1200,    4294883576, 4294965296, 610,     0x007C, 0,  12, 0x0000)
    DeclActor(4294924416, 10,      3570,    1200,    4294924416, 2009,    3570,    0x007C, 0,  23, 0x0000)

    PlaceName(17.0, 0.0, 39.25, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-133.0, -2.0, 6.0, 0x0000, 0x0000, "To Bellguard Gate")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_1120",         # 00, 0
        "Function_1_11D0",         # 01, 1
        "Function_2_11ED",         # 02, 2
        "Function_3_120C",         # 03, 3
        "Function_4_122B",         # 04, 4
        "Function_5_1261",         # 05, 5
        "Function_6_13B8",         # 06, 6
        "Function_7_20FF",         # 07, 7
        "Function_8_2251",         # 08, 8
        "Function_9_23A3",         # 09, 9
        "Function_10_24FD",        # 0A, 10
        "Function_11_2719",        # 0B, 11
        "Function_12_2A77",        # 0C, 12
        "Function_13_2DD5",        # 0D, 13
        "Function_14_2DEE",        # 0E, 14
        "Function_15_2DF2",        # 0F, 15
        "Function_16_30A0",        # 10, 16
        "Function_17_336A",        # 11, 17
        "Function_18_3415",        # 12, 18
        "Function_19_34B9",        # 13, 19
        "Function_20_3557",        # 14, 20
        "Function_21_35E5",        # 15, 21
        "Function_22_38A2",        # 16, 22
        "Function_23_3942",        # 17, 23
        "Function_24_3C7B",        # 18, 24
        "Function_25_3D0F",        # 19, 25
        "Function_26_3D8B",        # 1A, 26
        "Function_27_4023",        # 1B, 27
        "Function_28_422C",        # 1C, 28
        "Function_29_4C77",        # 1D, 29
        "Function_30_5557",        # 1E, 30
        "Function_31_55E7",        # 1F, 31
        "Function_32_5600",        # 20, 32
        "Function_33_5E65",        # 21, 33
        "Function_34_6E5A",        # 22, 34
        "Function_35_6F2B",        # 23, 35
        "Function_36_706D",        # 24, 36
        "Function_37_7D7E",        # 25, 37
        "Function_38_7DC4",        # 26, 38
        "Function_39_7E0A",        # 27, 39
        "Function_40_7E88",        # 28, 40
        "Function_41_7EEA",        # 29, 41
        "Function_42_7F22",        # 2A, 42
        "Function_43_7F5A",        # 2B, 43
        "Function_44_7FE2",        # 2C, 44
        "Function_45_801A",        # 2D, 45
        "Function_46_8056",        # 2E, 46
        "Function_47_8092",        # 2F, 47
        "Function_48_80CE",        # 30, 48
        "Function_49_8108",        # 31, 49
        "Function_50_814A",        # 32, 50
        "Function_51_8198",        # 33, 51
        "Function_52_A82C",        # 34, 52
        "Function_53_A843",        # 35, 53
        "Function_54_A85A",        # 36, 54
        "Function_55_A871",        # 37, 55
        "Function_56_A888",        # 38, 56
        "Function_57_A8A2",        # 39, 57
        "Function_58_A902",        # 3A, 58
        "Function_59_A941",        # 3B, 59
        "Function_60_A999",        # 3C, 60
        "Function_61_A9FB",        # 3D, 61
    ))


    def Function_0_1120(): pass

    label("Function_0_1120")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1158"),
        (1, "loc_1164"),
        (2, "loc_1170"),
        (3, "loc_117C"),
        (4, "loc_1188"),
        (5, "loc_1194"),
        (6, "loc_11A0"),
        (SWITCH_DEFAULT, "loc_11AC"),
    )


    label("loc_1158")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1164")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1170")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_117C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1188")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_1194")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_11B8")

    label("loc_11CF")

    Return()

    # Function_0_1120 end

    def Function_1_11D0(): pass

    label("Function_1_11D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11EC")
    OP_A1(0xFE, 0x1F4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_11D0")

    label("loc_11EC")

    Return()

    # Function_1_11D0 end

    def Function_2_11ED(): pass

    label("Function_2_11ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_120B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_11ED")

    label("loc_120B")

    Return()

    # Function_2_11ED end

    def Function_3_120C(): pass

    label("Function_3_120C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_122A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_120C")

    label("loc_122A")

    Return()

    # Function_3_120C end

    def Function_4_122B(): pass

    label("Function_4_122B")

    SetMapObjFlags(0x23, 0x2000000)
    SetMapObjFlags(0x24, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1260")
    ClearMapObjFlags(0x23, 0x2000000)
    ClearMapObjFlags(0x24, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)

    label("loc_1260")

    Return()

    # Function_4_122B end

    def Function_5_1261(): pass

    label("Function_5_1261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B9")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)

    label("loc_12B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DC")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_12F0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)
    Jump("loc_1382")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1304")
    ClearScenarioFlags(0x22, 1)
    Event(0, 32)
    Jump("loc_1382")

    label("loc_1304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1315")
    ClearScenarioFlags(0x22, 2)
    Jump("loc_1382")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1326")
    ClearScenarioFlags(0x22, 3)
    Jump("loc_1382")

    label("loc_1326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1337")
    ClearScenarioFlags(0x22, 4)
    Jump("loc_1382")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_134B")
    ClearScenarioFlags(0x22, 5)
    Event(0, 35)
    Jump("loc_1382")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_135F")
    ClearScenarioFlags(0x22, 6)
    Event(0, 36)
    Jump("loc_1382")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1373")
    ClearScenarioFlags(0x23, 1)
    Event(0, 51)
    Jump("loc_1382")

    label("loc_1373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1382")
    ClearScenarioFlags(0x23, 2)
    Event(0, 34)

    label("loc_1382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B4")
    SetChrPos(0x0, -43690, 10, 2760, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 24)

    label("loc_13B4")

    Call(0, 13)
    Return()

    # Function_5_1261 end

    def Function_6_13B8(): pass

    label("Function_6_13B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_13CA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13F1")
    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_145A")

    label("loc_13F1")

    OP_78(0x7, 0x23)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x23, 0x8)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x23, 0x1)
    SetChrPos(0x23, -890, 0, -52730, 0)
    OP_93(0x23, 0x0, 0x0)
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -890, -1000, -52730, 3000, 3000, 90000)

    label("loc_145A")

    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B8F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1C47")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_1CC5")

    label("loc_1C47")

    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D56")
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x8C, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, 7750, 1500, 27600, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, 5350, 1500, 30010, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1D5C")

    label("loc_1D56")

    SetMapObjFlags(0x8, 0x4)

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC6")
    ClearChrFlags(0x13, 0x80)
    OP_78(0x22, 0x13)
    ClearMapObjFlags(0x22, 0x4)
    SetChrPos(0x13, -77790, -8000, 64980, 180)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x22, "light", 0x0, 0x1)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x26, 0x15)
    ClearMapObjFlags(0x26, 0x4)
    SetChrPos(0x15, -74280, -8000, 56340, 315)
    OP_D5(0x15, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFrame(0x26, "light", 0x0, 0x1)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x27, 0x16)
    ClearMapObjFlags(0x27, 0x4)
    SetChrPos(0x16, -56100, -8000, 69080, 251)
    OP_D5(0x16, 0x0, 0x3D478, 0x0, 0x0)
    SetMapObjFrame(0x27, "light", 0x0, 0x1)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x21, 0x14)
    ClearMapObjFlags(0x21, 0x4)
    SetChrPos(0x14, -72640, -8000, 68520, 225)
    OP_D5(0x14, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0x21, "light", 0x0, 0x1)
    SetMapObjFrame(0x21, "mark01", 0x0, 0x1)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x25, 0x17)
    ClearMapObjFlags(0x25, 0x4)
    SetChrPos(0x17, -65900, -8000, 59320, 260)
    OP_D5(0x17, 0x0, 0x3F7A0, 0x0, 0x0)
    SetMapObjFrame(0x25, "light", 0x0, 0x1)
    SetMapObjFrame(0x25, "mark01", 0x0, 0x1)

    label("loc_1EC6")

    MiniGame(0x2F, 0x6, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFB")
    OP_70(0x0, 0x0)
    Jump("loc_1EFF")

    label("loc_1EFB")

    OP_70(0x0, 0x1E)

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F12")
    OP_70(0x1, 0x0)
    Jump("loc_1F16")

    label("loc_1F12")

    OP_70(0x1, 0x1E)

    label("loc_1F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")
    OP_70(0x2, 0x0)
    Jump("loc_1F2D")

    label("loc_1F29")

    OP_70(0x2, 0x1E)

    label("loc_1F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F40")
    OP_70(0x3, 0x0)
    Jump("loc_1F44")

    label("loc_1F40")

    OP_70(0x3, 0x1E)

    label("loc_1F44")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FA5")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -25580, 0, -31940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1FA5")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FF1")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -83720, -2000, 610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1FF1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2009")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2009")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_2021")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203E")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_203E")

    OP_10(0x2, 0x1)
    OP_10(0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_END)), "loc_2053")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)

    label("loc_2053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2066")
    OP_1B(0x2, 0x0, 0x16)

    label("loc_2066")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_207E")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_207E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209D")
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_20C3")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_END)), "loc_20B7")
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_20C3")

    label("loc_20B7")

    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20DD")
    ClearMapObjFlags(0x28, 0x4)
    ClearMapObjFlags(0x29, 0x4)

    label("loc_20DD")

    OP_1C(0x0, 0x1E, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x1F, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x20, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    Return()

    # Function_6_13B8 end

    def Function_7_20FF(): pass

    label("Function_7_20FF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FB")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x44, 1)"), scpexpr(EXPR_END)), "loc_2184")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_21F6")

    label("loc_2184")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x44),
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

    label("loc_21F6")

    Jump("loc_2245")

    label("loc_21FB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_2245")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_20FF end

    def Function_8_2251(): pass

    label("Function_8_2251")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_22D6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2348")

    label("loc_22D6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2348")

    Jump("loc_2397")

    label("loc_234D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_2397")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2251 end

    def Function_9_23A3(): pass

    label("Function_9_23A3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CD")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x40\x01\x07\x02",
            "#57IWater Sepith x40\x01\x07\x02",
            "#58IFire Sepith x40\x01\x07\x02",
            "#59IWind Sepith x40\x01\x07\x02",
            "#60ITime Sepith x40\x01\x07\x02",
            "#61ISpace Sepith x40\x01\x07\x02",
            "#62IMirage Sepith x40\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E2, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_24EB")

    label("loc_24CD")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_24EB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_23A3 end

    def Function_10_24FD(): pass

    label("Function_10_24FD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2600")
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x22, 0x0, 0)
    OP_98(0x22, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_255A():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_255A)

    def lambda_2574():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_2574)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x22, 1)
    Battle("BattleInfo_F10", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x22, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_25E1"),
        (2, "loc_25F0"),
        (1, "loc_25FD"),
        (SWITCH_DEFAULT, "loc_2600"),
    )


    label("loc_25E1")

    SetScenarioFlags(0x216, 1)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_2600")

    label("loc_25F0")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_25FD")

    OP_B9(0x0)
    Return()

    label("loc_2600")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x68, 1)"), scpexpr(EXPR_END)), "loc_2659")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_26C9")

    label("loc_2659")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_26C9")

    Jump("loc_270D")

    label("loc_26CE")

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

    label("loc_270D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_24FD end

    def Function_11_2719(): pass

    label("Function_11_2719")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28D1")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_28B2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AD")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_28AA")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_27CF)
    TurnDirection(0x1E, 0x0, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    PlayEffect(0x7, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A5")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_288C")
    Call(1, 5)
    Jump("loc_28A5")

    label("loc_288C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28A2")
    Call(1, 4)
    Jump("loc_28A5")

    label("loc_28A2")

    Call(1, 3)

    label("loc_28A5")

    Jump("loc_28AD")

    label("loc_28AA")

    Call(1, 1)

    label("loc_28AD")

    Jump("loc_28C8")

    label("loc_28B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_28C8")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_28C8")

    TalkEnd(0xFF)
    Return()

    label("loc_28D1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_2A5C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A57")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2A54")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2979():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_2979)
    TurnDirection(0x20, 0x0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    PlayEffect(0x7, 0x1, 0x20, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A36")
    Call(1, 5)
    Jump("loc_2A4F")

    label("loc_2A36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A4C")
    Call(1, 4)
    Jump("loc_2A4F")

    label("loc_2A4C")

    Call(1, 3)

    label("loc_2A4F")

    Jump("loc_2A57")

    label("loc_2A54")

    Call(1, 1)

    label("loc_2A57")

    Jump("loc_2A72")

    label("loc_2A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_2A72")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2A72")

    TalkEnd(0xFF)
    Return()

    # Function_11_2719 end

    def Function_12_2A77(): pass

    label("Function_12_2A77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C2F")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2C10")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0B")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2C08")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2B2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_2B2D)
    TurnDirection(0x1F, 0x0, 0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    PlayEffect(0x7, 0x1, 0x1F, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_E88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C03")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BEA")
    Call(1, 5)
    Jump("loc_2C03")

    label("loc_2BEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C00")
    Call(1, 4)
    Jump("loc_2C03")

    label("loc_2C00")

    Call(1, 3)

    label("loc_2C03")

    Jump("loc_2C0B")

    label("loc_2C08")

    Call(1, 1)

    label("loc_2C0B")

    Jump("loc_2C26")

    label("loc_2C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2C26")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2C26")

    TalkEnd(0xFF)
    Return()

    label("loc_2C2F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2DBA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB5")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2DB2")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2CD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2CD7)
    TurnDirection(0x21, 0x0, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    PlayEffect(0x7, 0x1, 0x21, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_ECC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D94")
    Call(1, 5)
    Jump("loc_2DAD")

    label("loc_2D94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2DAA")
    Call(1, 4)
    Jump("loc_2DAD")

    label("loc_2DAA")

    Call(1, 3)

    label("loc_2DAD")

    Jump("loc_2DB5")

    label("loc_2DB2")

    Call(1, 1)

    label("loc_2DB5")

    Jump("loc_2DD0")

    label("loc_2DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_2DD0")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2DD0")

    TalkEnd(0xFF)
    Return()

    # Function_12_2A77 end

    def Function_13_2DD5(): pass

    label("Function_13_2DD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DED")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_2DED")

    Return()

    # Function_13_2DD5 end

    def Function_14_2DEE(): pass

    label("Function_14_2DEE")

    Call(1, 6)
    Return()

    # Function_14_2DEE end

    def Function_15_2DF2(): pass

    label("Function_15_2DF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_2F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEB")

    ChrTalk(
        0xFE,
        (
            "W-What the heck was\x01",
            "that ghastly voice!?\x02\x03",
            "It seemed just like\x01",
            "a yell from hell...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCam down, Frantz.\x02\x03",
            "#00001FWe'll go investigate now.\x01",
            "I leave this place to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yeah...got it.\x01",
            "Be careful Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F3D")

    label("loc_2EEB")


    ChrTalk(
        0xFE,
        (
            "W-What the heck was\x01",
            "that ghastly voice...\x02\x03",
            "Everyone, please\x01",
            "be very careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3D")

    Jump("loc_309C")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_309C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302A")

    ChrTalk(
        0xFE,
        (
            "It seems that the train ended\x01",
            "up derailing completely.\x02\x03",
            "It's a blessing there were no\x01",
            "dead, but it will take some\x01",
            "time until things are repaired.\x02\x03",
            "If you're going to investigate,\x01",
            "please do your best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_309C")

    label("loc_302A")


    ChrTalk(
        0xFE,
        (
            "It seems that the train ended\x01",
            "up derailing completely.\x02\x03",
            "If you're going to investigate,\x01",
            "please do your best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309C")

    TalkEnd(0xFE)
    Return()

    # Function_15_2DF2 end

    def Function_16_30A0(): pass

    label("Function_16_30A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317A")

    ChrTalk(
        0xFE,
        (
            "Senior Randy, Miss Noｱl...\x01",
            "What was the yell we just heard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FDunno, but...\x01",
            "Seems we should be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FWe leave the watchout to you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ma'am, roger that!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3221")

    label("loc_317A")


    ChrTalk(
        0xFE,
        (
            "Whatever that yell was just now,\x01",
            "we can't interrupt the repair works\x01",
            "that are being done quickly on the site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please leave the guarding of this place to us!\x02",
    )

    CloseMessageWindow()

    label("loc_3221")

    Jump("loc_3366")

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EC")

    ChrTalk(
        0xFE,
        (
            "The train accident scene\x01",
            "is just down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya and the people from \x01",
            "the police are already doing an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, please pass through.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3366")

    label("loc_32EC")


    ChrTalk(
        0xFE,
        (
            "Commander Sonya and the people from \x01",
            "the police are already doing an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, please pass through.\x02",
    )

    CloseMessageWindow()

    label("loc_3366")

    TalkEnd(0xFE)
    Return()

    # Function_16_30A0 end

    def Function_17_336A(): pass

    label("Function_17_336A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3411")

    ChrTalk(
        0xFE,
        (
            "I hope that the mass media person\x01",
            "who just went in doesn't interfere\x01",
            "with the repair works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in that regard, she\x01",
            "seemed to understand that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    TalkEnd(0xFE)
    Return()

    # Function_17_336A end

    def Function_18_3415(): pass

    label("Function_18_3415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_34B5")

    ChrTalk(
        0xFE,
        (
            "Cooperating with the CGF\x01",
            "and even working together\x01",
            "is quite rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The scene is in a horrible state...\x01",
            "We police too must do what we can.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B5")

    TalkEnd(0xFE)
    Return()

    # Function_18_3415 end

    def Function_19_34B9(): pass

    label("Function_19_34B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_3553")

    ChrTalk(
        0xFE,
        (
            "The Section Two men from the police\x01",
            "are hunting down the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, for now it seems they\x01",
            "haven't confirmed anything specific.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3553")

    TalkEnd(0xFE)
    Return()

    # Function_19_34B9 end

    def Function_20_3557(): pass

    label("Function_20_3557")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_35E1")

    ChrTalk(
        0xFE,
        (
            "Commander Sonya is commanding\x01",
            "the repairs on site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you plan to join the investigation,\x01",
            "you have to go greet her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E1")

    TalkEnd(0xFE)
    Return()

    # Function_20_3557 end

    def Function_21_35E5(): pass

    label("Function_21_35E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3737")

    ChrTalk(
        0xFE,
        (
            "This is the West Crossbell Highway...\x01",
            "Confirmed a roar of an unidentified\x01",
            "creature just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As per Commander Sonya orders,\x01",
            "we're to prioritize railway repair works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, you must make haste to transport\x01",
            "as many heavy machineries as possible.\x01",
            "I repeat, transport heavy machineries...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_3804")

    label("loc_3737")


    ChrTalk(
        0xFE,
        (
            "We leave that to you.\x01",
            "We'll prioritize the railway repair\x01",
            "works with Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we finish quick, it's possible\x01",
            "we'll come running to support you.\x01",
            "Until then, please take care of things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3804")

    Jump("loc_389E")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_389E")

    ChrTalk(
        0xFE,
        (
            "In a continuous situation of state border tension,\x01",
            "a troublesome accident has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I wonder if it's really a coincidence?\x02",
    )

    CloseMessageWindow()

    label("loc_389E")

    TalkEnd(0xFE)
    Return()

    # Function_21_35E5 end

    def Function_22_38A2(): pass

    label("Function_22_38A2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FFor now, we'll leave the railway\x01",
            "repair works to Commander Sonya.\x02\x03",
            "#00001FWe'll identify the nature\x01",
            "of that mysterious roar!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -64870, -8000, 77770, 180)
    EventEnd(0x4)
    Return()

    # Function_22_38A2 end

    def Function_23_3942(): pass

    label("Function_23_3942")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3974")
    SetScenarioFlags(0x31, 2)

    label("loc_3974")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_39B4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39A9")
    Sound(2499, 255, 100, 0)
    Jump("loc_39AF")

    label("loc_39A9")

    Sound(3537, 255, 100, 0)

    label("loc_39AF")

    Jump("loc_39BA")

    label("loc_39B4")

    Sound(3344, 255, 100, 0)

    label("loc_39BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3A2D")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A0D"),
        (SWITCH_DEFAULT, "loc_3A1E"),
    )


    label("loc_3A0D")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3A28")

    label("loc_3A1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A28")

    Jump("loc_3C68")

    label("loc_3A2D")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3A5F")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_3A5F")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A91"),
        (1, "loc_3B95"),
        (2, "loc_3C26"),
        (SWITCH_DEFAULT, "loc_3C5E"),
    )


    label("loc_3A91")

    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC2")
    OP_70(0x4, 0x12C)
    OP_71(0x4, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3AD2")

    label("loc_3AC2")

    OP_70(0x4, 0xF0)
    OP_71(0x4, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3AD2")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B28")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B28")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4B")
    Sound(461, 0, 100, 0)

    label("loc_3B4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6B")
    OP_70(0x4, 0x14A)
    OP_71(0x4, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3B7B")

    label("loc_3B6B")

    OP_70(0x4, 0x10E)
    OP_71(0x4, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3B7B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x4, "light", 0x1, 0x1)
    OP_70(0x4, 0x0)
    Jump("loc_39BA")

    label("loc_3B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3C07")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3BCA")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3BE2")

    label("loc_3BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3BDD")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3BE2")

    label("loc_3BDD")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3BE2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C21")

    label("loc_3C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3C17")
    OP_AF(0xFB)
    Jump("loc_3C21")

    label("loc_3C17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C21")

    Jump("loc_3C68")

    label("loc_3C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C59")

    label("loc_3C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3C4F")
    OP_AF(0xFB)
    Jump("loc_3C59")

    label("loc_3C4F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C59")

    Jump("loc_3C68")

    label("loc_3C5E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C68")

    Jump("loc_39BA")

    label("loc_3C6D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_23_3942 end

    def Function_24_3C7B(): pass

    label("Function_24_3C7B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3CD6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CCB")
    Sound(2502, 255, 100, 0)
    Jump("loc_3CD1")

    label("loc_3CCB")

    Sound(2503, 255, 100, 0)

    label("loc_3CD1")

    Jump("loc_3CFA")

    label("loc_3CD6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CF4")
    Sound(3347, 255, 100, 0)
    Jump("loc_3CFA")

    label("loc_3CF4")

    Sound(3348, 255, 100, 0)

    label("loc_3CFA")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_3C7B end

    def Function_25_3D0F(): pass

    label("Function_25_3D0F")

    Battle("BattleInfo_F54", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D56")
    OP_90(0x0, -7830, 0, -50540, 270)
    EventEnd(0x5)
    SetChrFlags(0x23, 0x8000)
    Jump("loc_3D8A")

    label("loc_3D56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D69")
    Jump("loc_3D8A")

    label("loc_3D69")

    ModifyEventFlags(0, 2, 0x80)
    SetMapObjFlags(0x7, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_3D8A")

    Return()

    # Function_25_3D0F end

    def Function_26_3D8B(): pass

    label("Function_26_3D8B")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(1860, 9890, 23710, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1680, 2500, 23480, 45)
    SetChrPos(0x103, 2120, 2500, 22540, 45)
    SetChrPos(0x104, 610, 2500, 23840, 45)
    SetChrPos(0x105, 310, 2500, 22140, 45)
    SetChrPos(0x106, -430, 2500, 23430, 45)
    SetChrPos(0x107, 1310, 2490, 21170, 45)
    SetChrSubChip(0x107, 0x5)
    OP_68(1860, 3290, 23710, 4500)
    MoveCamera(45, 23, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(20000, 4500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001FA "barrier" on Crossbell City, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FFor the time being, we can't\x01",
            "do anything about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PWell,  we didn't even\x01",
            "find a way to get inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FYeah, it should be wise\x01",
            "to find another route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#6PI think this is also a place\x01",
            "patrolled by the State Guard, so\x01",
            "it would be better to not overstay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, you're right...\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 2070, 2500, 23540, 225)
    SetScenarioFlags(0x1BD, 0)
    ModifyEventFlags(0, 3, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_26_3D8B end

    def Function_27_4023(): pass

    label("Function_27_4023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422B")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008FSo, we made a general round but,\x01",
            "for now, every direction is blocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOf course we can't go to Crossbell City, \x01",
            "but also it looks so for Bellguard Gate \x01",
            "and even the Police Academy area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#6PThat's a problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PHm, isn't there some other\x01",
            "place where we can go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#12PMaybe it would be better to look for a place\x01",
            "somewhat away from the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYou're right...\x01",
            "Let's search a little more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422B")

    Return()

    # Function_27_4023 end

    def Function_28_422C(): pass

    label("Function_28_422C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -38880, 0, -3420, 315)
    SetChrPos(0x102, -37220, 0, -2870, 315)
    SetChrPos(0x103, -37980, 0, -5050, 315)
    SetChrPos(0x104, -37250, 0, -4040, 315)
    SetChrPos(0x109, -35720, 0, -4900, 315)
    SetChrPos(0x105, -36260, 0, -6090, 315)
    OP_68(-40900, 1200, -650, 0)
    MoveCamera(90, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 2000)

    def lambda_4315():
        OP_95(0xFE, -40880, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4315)
    Sleep(30)

    def lambda_4332():
        OP_95(0xFE, -39220, 0, -870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4332)
    Sleep(30)

    def lambda_434F():
        OP_95(0xFE, -39980, 0, -3050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_434F)
    Sleep(30)

    def lambda_436C():
        OP_95(0xFE, -39250, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_436C)
    Sleep(30)

    def lambda_4389():
        OP_95(0xFE, -37720, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4389)
    Sleep(30)

    def lambda_43A6():
        OP_95(0xFE, -38260, 0, -4090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43A6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-47350, 600, 11150, 4000)
    MoveCamera(45, 23, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#12P#NThat's...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10300F#12P#NIt seems that the accident\x01",
            "scene is over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-47400, 800, 10050, 5000)
    MoveCamera(45, 20, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(18950, 5000)
    SetChrPos(0x101, -41650, 0, 3020, 315)
    SetChrPos(0x102, -41010, 0, 1770, 315)
    SetChrPos(0x103, -42180, 0, 1820, 315)
    SetChrPos(0x104, -40030, 0, 660, 315)
    SetChrPos(0x109, -41520, 0, 250, 315)
    SetChrPos(0x105, -42770, 0, 320, 315)

    def lambda_4573():
        OP_95(0xFE, -47650, 0, 9020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4573)
    Sleep(30)

    def lambda_4590():
        OP_95(0xFE, -47010, 0, 7770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4590)
    Sleep(30)

    def lambda_45AD():
        OP_95(0xFE, -48180, 0, 7820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45AD)
    Sleep(30)

    def lambda_45CA():
        OP_95(0xFE, -46030, 0, 6660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45CA)
    Sleep(30)

    def lambda_45E7():
        OP_95(0xFE, -47520, 0, 6250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_45E7)
    Sleep(30)

    def lambda_4604():
        OP_95(0xFE, -48770, 0, 6320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4604)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_464B():

        label("loc_464B")

        TurnDirection(0x8, 0x101, 500)
        Yield()
        Jump("loc_464B")

    QueueWorkItem2(0x8, 2, lambda_464B)

    def lambda_465D():

        label("loc_465D")

        TurnDirection(0x9, 0x101, 500)
        Yield()
        Jump("loc_465D")

    QueueWorkItem2(0x9, 2, lambda_465D)
    WaitChrThread(0x101, 1)

    def lambda_4673():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4673)
    WaitChrThread(0x102, 1)

    def lambda_4684():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4684)
    WaitChrThread(0x103, 1)

    def lambda_4695():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4695)
    WaitChrThread(0x104, 1)

    def lambda_46A6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_46A6)
    WaitChrThread(0x109, 1)

    def lambda_46B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_46B7)
    WaitChrThread(0x105, 1)

    def lambda_46C8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_46C8)
    WaitChrThread(0x101, 2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#5PHi, Lloyd, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PFrantz, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PSenior Randy, Miss Noｱl too.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PLikewise, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PSeems there's no doubt the\x01",
            "accident scene is just ahead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYes, Commander Sonya and the people from\x01",
            "the police are already doing an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSection Two Inspector Donovan\x01",
            "and Mr. Raymond are there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, it seems it ended\x01",
            "up derailing completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems it'll take some time\x01",
            "until things are repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PExcuse me...\x01",
            "What about damage to the passengers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PLuckily it appears there were no dead,\x01",
            "but some were heavily wounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThose who seemed to be in need of treatment\x01",
            "were carried away in ambulances some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PYeah, we saw those before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PAnd the other passengers were by buses?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, they were split in two:\x01",
            "Those going to Crossbell City,\x01",
            "and those going to Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThere was a big chaos until a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P...I can imagine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh boy.\x01",
            "A troublesome accident has happened, eh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PAt any rate, let's go to\x01",
            "the accident scene too.\x02\x03",
            "#00000FCan we pass through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, since it's you guys, no one\x01",
            "would have anything to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PPlease, pass through!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -47350, 0, 9050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, -44510, 0, 11820, 180)
    SetChrPos(0x9, -50350, 0, 12060, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x163, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_422C end

    def Function_29_4C77(): pass

    label("Function_29_4C77")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -45010, 0, 2540, 315)
    SetChrPos(0x102, -44060, 0, 3260, 315)
    SetChrPos(0x103, -45070, 0, 1560, 315)
    SetChrPos(0x104, -43100, 0, 2350, 315)
    SetChrPos(0x109, -43180, 0, 1320, 315)
    SetChrPos(0x105, -44250, 0, 510, 315)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -28900, 0, -19150, 315)
    OP_D5(0x11, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    VolumeBGM(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-38050, 2100, -2550, 0)
    MoveCamera(114, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30200, 0)
    OP_68(-41150, 1100, 3800, 8000)
    MoveCamera(84, 20, 0, 8000)
    SetCameraDistance(19700, 8000)
    BeginChrThread(0x11, 3, 0, 30)
    BeginChrThread(0x24, 1, 0, 31)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(462, 0, 100, 0)
    OP_71(0x4, 0x12D, 0x14A, 0x1, 0x8)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x11, -41260, 0, 4180, 315)
    OP_D5(0x11, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x1000)
    OP_70(0x4, 0x78)
    SetChrFlags(0x11, 0x80)
    OP_68(-44400, 1300, 2600, 0)
    MoveCamera(80, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17200, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x8, -46510, 0, 9480, 180)
    SetChrPos(0x9, -48380, 0, 8780, 180)
    OP_68(-45400, 1300, 3600, 3000)

    def lambda_4F55():
        OP_95(0xFE, -45600, 0, 4870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F55)

    def lambda_4F6F():
        OP_95(0xFE, -46440, 0, 4150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F6F)
    WaitChrThread(0x8, 1)

    def lambda_4F8D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4F8D)
    WaitChrThread(0x9, 1)

    def lambda_4F9E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4F9E)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#5PHi, Lloyd, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PFrantz, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PSenior Randy, Miss Noｱl too.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PLikewise, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PSeems there's no doubt the\x01",
            "accident scene is just ahead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes, Commander Sonya and the people from\x01",
            "the police are already doing an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSection Two Inspector Donovan\x01",
            "and Mr. Raymond are there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, it seems it ended\x01",
            "up derailing completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems it'll take some time\x01",
            "until things are repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PExcuse me...\x01",
            "What about damage to the passengers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PLuckily it appears there were no dead,\x01",
            "but some were heavily wounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PThose who seemed to be in need of treatment\x01",
            "were carried away in ambulances some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PYeah, we saw those before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PAnd the other passengers were by buses?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, they were split in two:\x01",
            "Those going to Crossbell City,\x01",
            "and those going to Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThere was a big chaos until a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P...I can imagine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11POh boy.\x01",
            "A troublesome accident has happened, eh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAt any rate, let's go to\x01",
            "the accident scene too.\x02\x03",
            "#00000FCan we pass through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, since it's you guys, no one\x01",
            "would have anything to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PPlease, pass through!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -47350, 0, 9050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, -44510, 0, 11820, 180)
    SetChrPos(0x9, -50350, 0, 12060, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x163, 0)
    ModifyEventFlags(0, 0, 0x80)
    ClearMapFlags(0x8000000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_29_4C77 end

    def Function_30_5557(): pass

    label("Function_30_5557")

    SetChrPos(0xFE, -28900, 0, -19150, 315)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -32900, 0, -12300)
    OP_9F(0x1, -33800, 0, -5850)
    OP_9F(0x1, -34550, 0, -1950)
    OP_9F(0x1, -39400, 0, 3050)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_30_5557 end

    def Function_31_55E7(): pass

    label("Function_31_55E7")

    Sound(458, 0, 100, 0)
    Sleep(3000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 70, 0)
    Return()

    # Function_31_55E7 end

    def Function_32_5600(): pass

    label("Function_32_5600")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    OP_68(-63850, -5700, 68650, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -64849, -8000, 71050, 180)
    SetChrPos(0x102, -65200, -8000, 73050, 180)
    SetChrPos(0x103, -63350, -8000, 71700, 180)
    SetChrPos(0x104, -62850, -8000, 73020, 180)
    SetChrPos(0x109, -64450, -8000, 72300, 180)
    SetChrPos(0x105, -63850, -8000, 73650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -64569, -8000, 76920, 180)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -63420, -8000, 77430, 180)
    SetMapObjFlags(0x21, 0x1000)

    def lambda_571D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_571D)
    Sleep(50)

    def lambda_5735():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5735)

    def lambda_574A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_574A)
    Sleep(50)

    def lambda_5762():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5762)

    def lambda_5777():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5777)
    Sleep(50)

    def lambda_578F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_578F)

    def lambda_57A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57A4)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_68(-63640, -7200, 68080, 3500)

    def lambda_57D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    def lambda_5803():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5803)
    Sleep(50)

    def lambda_5813():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5813)
    Sleep(50)

    def lambda_5823():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5823)
    Sleep(50)

    def lambda_5833():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5833)
    Sleep(50)

    def lambda_5843():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5843)
    Sleep(50)

    def lambda_5853():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5853)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006F#12PMiss Grace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P"As you can expect, we're coming too!"...\x01",
            "You aren't going to say that, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106F#5P"Eeh, isn't that ok?"...\x01",
            "I'd like to say this, though.\x02\x03",
            "#02100FIt really seems dangerous,\x01",
            "so I'll hold back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI plan to put together a news flash\x01",
            "and go back to Crossbell City for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI'll gather other reports immediately\x01",
            "and resume data collection at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#12PI think that is safe to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PWell, if she got attacked we\x01",
            "wouldn't be able to cover for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103F#5PI don't know what monster it is,\x01",
            "but if it really made a train derail,\x01",
            "that's not your common foe...\x02\x03",
            "#02101FPlease, be extremely careful!\x01",
            "And give me the materials later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PThank you!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x1F4)
    OP_68(-61720, -7200, 67040, 4000)
    MoveCamera(54, 18, 0, 4000)
    OP_6E(510, 4000)

    def lambda_5BBD():

        label("loc_5BBD")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_5BBD")

    QueueWorkItem2(0x101, 2, lambda_5BBD)

    def lambda_5BCF():

        label("loc_5BCF")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_5BCF")

    QueueWorkItem2(0x102, 2, lambda_5BCF)

    def lambda_5BE1():

        label("loc_5BE1")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_5BE1")

    QueueWorkItem2(0x103, 2, lambda_5BE1)

    def lambda_5BF3():

        label("loc_5BF3")

        TurnDirection(0xFE, 0xF, 150)
        Yield()
        Jump("loc_5BF3")

    QueueWorkItem2(0x104, 2, lambda_5BF3)

    def lambda_5C05():

        label("loc_5C05")

        TurnDirection(0xFE, 0xF, 100)
        Yield()
        Jump("loc_5C05")

    QueueWorkItem2(0x109, 2, lambda_5C05)

    def lambda_5C17():

        label("loc_5C17")

        TurnDirection(0xFE, 0xF, 200)
        Yield()
        Jump("loc_5C17")

    QueueWorkItem2(0x105, 2, lambda_5C17)

    def lambda_5C29():
        OP_95(0xFE, -55190, -8000, 61950, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5C29)
    Sleep(800)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_5C4D():
        OP_95(0xFE, -54530, -8000, 62580, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5C4D)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-63110, -7200, 66900, 1000)
    MoveCamera(54, 18, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_5CC4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CC4)

    def lambda_5CD1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5CD1)
    Sleep(50)

    def lambda_5CE1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5CE1)
    Sleep(50)

    def lambda_5CF1():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5CF1)
    Sleep(50)

    def lambda_5D01():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D01)
    Sleep(50)

    def lambda_5D11():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5D11)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──All right, let's start the pursuit.\x02\x03",
            "#00013FFirst, let's head straight\x01",
            "west on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#5PJa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PWe must catch it no matter what!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -65000, -8000, 65000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x21, 0x1000)
    SetScenarioFlags(0x163, 2)
    OP_29(0xA8, 0x1, 0x6)
    ModifyEventFlags(0, 4, 0x80)
    OP_C9(0x0, 0x200000)
    OP_1B(0x2, 0x0, 0x16)
    OP_E2(0x2)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    EventEnd(0x5)
    Return()

    # Function_32_5600 end

    def Function_33_5E65(): pass

    label("Function_33_5E65")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -57760, -8000, 63610, 0)
    SetChrPos(0x106, -57240, -8000, 62560, 0)
    SetChrPos(0x103, -58560, -8000, 62060, 0)
    SetChrPos(0x104, -57710, -8000, 61210, 0)
    SetChrPos(0x107, -56060, -8000, 61660, 0)
    SetChrPos(0x105, -59860, -8000, 61460, 0)
    OP_68(-57500, -7100, 65300, 0)
    MoveCamera(25, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)

    def lambda_5F34():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F34)
    Sleep(50)

    def lambda_5F4C():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5F4C)
    Sleep(50)

    def lambda_5F64():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F64)
    Sleep(50)

    def lambda_5F7C():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F7C)
    Sleep(50)

    def lambda_5F94():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5F94)
    Sleep(50)

    def lambda_5FAC():
        OP_9B(0x1, 0xFE, 0xFFE7, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FAC)
    FadeToBright(1000, 0)
    OP_68(-60310, -7100, 69090, 4000)
    SetCameraDistance(24500, 4000)
    MoveCamera(25, 18, 0, 4000)
    Sleep(3500)
    Fade(1000)
    OP_68(-64099, -5100, 77200, 0)
    OP_68(-64099, -7100, 77200, 3500)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00205F#6PBy the way, the vehicles from the derail\x01",
            "accident have been completely removed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, even the broken pieces\x01",
            "have been cleared up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PStill, that accident should've been\x01",
            "quite the serious matter, but...\x02\x03",
            "#00301FSince nothing but severe stuff happens,\x01",
            "it had some kind of weak impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10403F#6P...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#12PThe transcontinental railway service too\x01",
            "is currently completely halted.\x02\x03",
            "#10708FIt appears that occasionally State\x01",
            "Guard freight trains pass through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PI see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00005F#5P...Wait.\x02\x03",
            "#00013FThat means it's possible\x01",
            "to go to and fro on the tracks...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrFlags(0x107, 0x20)

    def lambda_6346():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6346)
    Sleep(50)

    def lambda_6356():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6356)
    Sleep(50)

    def lambda_6366():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6366)
    Sleep(50)

    def lambda_6376():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6376)
    Sleep(50)

    def lambda_6386():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6386)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x106,
        "#10712F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PI see...\x01",
            "There was that option too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#3C#11PHowever, the Crossbell City area\x01",
            "is enveloped in a "barrier" now.\x02\x03",
            "#01201FIt's impossible to enter the city\x01",
            "without getting noticed, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah...I know.\x02\x03",
            "#00000FBut, what about the west side?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0xFFFFFDA8, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#6PMr. Lloyd, are you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PDo you want to infiltrate Bellguard\x01",
            "Gate via the railway tracks!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Yeah, I thought that.\x02\x03",
            "#00001FI was thinking why not talking in\x01",
            "person to Commander Sonya once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PMrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PIt is true that if she could become our ally,\x01",
            "she would be an extremely reliable person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#6PHowever, she wasn't against switching \x01",
            "over to the State Guard, right?\x02\x03",
            "#10401FAs you'd expect, it seems to be risky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#11P...I agree too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5POf course, because she's in a certain position\x01",
            "we'd only get arrested by visiting her directly.\x02\x03",
            "#00008FHowever, if somehow we managed to infiltrate\x01",
            "the Gate and take contact behind close doors..\x02\x03",
            "#00001FPerhaps she could tell\x01",
            "her real intentions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12P...Considerin' Mireille and the others,\x01",
            "there should be not a few people who\x01",
            "have some doubts in the State Guard.\x02\x03",
            "#00300FIf it's 'bout people with such a strong\x01",
            "sense of justice, maybe all the more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6PUhhm, then I wouldn't\x01",
            "be against it too, but...\x02\x03",
            "#10401FIf Commander Sonya is there, then\x01",
            ""she" is going to be there too, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x107, 0x20)

    def lambda_6A40():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6A40)
    Sleep(50)

    def lambda_6A50():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A50)
    Sleep(50)

    def lambda_6A60():
        TurnDirection(0x106, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6A60)
    Sleep(50)

    def lambda_6A70():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A70)
    Sleep(50)

    def lambda_6A80():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6A80)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x103,
        "#00201F#5PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11P...That too, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#11PMiss Noｱl...right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#11PHm, according to what I've heard, her\x01",
            "determination seems to be firm, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5P...I know.\x02\x03",
            "#00006FHowever, it's true that the road we're\x01",
            "proceeding on is terribly difficult.\x02\x03",
            "#00003FEven if we're in disagreement with her...\x01",
            "Sooner or later we'll have to get over it.\x02\x03",
            "#00013F──And that's even if we'll have\x01",
            "to argue with her directly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x107, 0x20)

    def lambda_6C79():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6C79)
    Sleep(50)

    def lambda_6C89():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C89)
    Sleep(50)

    def lambda_6C99():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6C99)
    Sleep(50)

    def lambda_6CA9():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6CA9)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x103,
        "#00208F#6PMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P...Right. We can't just\x01",
            "avoid the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHu hu, if you thought that much about it,\x01",
            "then I won't say anything anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#11PIn any case, let's open the fence\x01",
            "and exit on the railway tracks.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#00000F#5PYeah...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(113, 0, 50, 0)
    Sound(114, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x0, -64000, -8000, 75000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetScenarioFlags(0x1A3, 1)
    OP_29(0xAF, 0x1, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    ModifyEventFlags(0, 3, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_33_5E65 end

    def Function_34_6E5A(): pass

    label("Function_34_6E5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_68(5500, 5000, 27500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_68(5500, 5500, 27500, 8000)
    MoveCamera(45, 30, 0, 8000)
    SetCameraDistance(30000, 8000)
    OP_71(0x8, 0x208, 0x2BC, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(100)
    Sound(223, 0, 100, 0)
    Sleep(1200)
    FadeToDark(1000, 16777215, -1)
    Sound(181, 0, 100, 0)
    Sleep(1500)
    FadeToBright(1000, 16777215)
    OP_0D()
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_6E5A end

    def Function_35_6F2B(): pass

    label("Function_35_6F2B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -134100, -2000, 14320, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x23, 0x12)
    OP_49()
    SetChrPos(0x12, -134100, -2000, 14320, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x23, 0x1000)
    SetMapObjFrame(0x23, "light", 0x0, 0x1)
    OP_74(0x23, 0x1E)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_E2(0x3)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x103, 0x80)
    OP_68(-113630, -2100, 10940, 0)
    MoveCamera(25, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(48250, 0)
    Sound(458, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0x12, 3, 0, 38)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 37)
    SetCameraDistance(53860, 3000)
    Sleep(1500)
    Sound(494, 0, 100, 0)
    OP_6F(0x10)
    Sleep(500)
    SetScenarioFlags(0x23, 4)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_6F2B end

    def Function_36_706D(): pass

    label("Function_36_706D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x1E)
    LoadChrToIndex("chr/ch47500.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    LoadEffect(0x0, "event/ev14100.eff")
    ClearChrFlags(0x11, 0x80)
    OP_78(0x4, 0x11)
    OP_49()
    SetChrPos(0x11, -64480, -2000, -450, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x23, 0x12)
    OP_49()
    SetChrPos(0x12, -43460, 0, 1050, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x23, 0x1000)
    SetMapObjFrame(0x23, "light", 0x0, 0x1)
    OP_74(0x23, 0x1E)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-40740, 440, -3760, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x3)
    OP_6B(0x12)
    BeginChrThread(0x12, 3, 0, 39)
    BeginChrThread(0x24, 1, 0, 48)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 40)

    NpcTalk(
        0x12,
        "Reggie",
        (
            "#6A#40WW-What...\x01",
            "T-the breaks aren't working!?\x02",
        )
    )

    Sleep(1500)

    NpcTalk(
        0x12,
        "Sykes - Yuri",
        "#6A#40WW-Whaaat!?\x02",
    )

    Sleep(1500)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6B(0xFF)
    OP_68(-28010, 600, -20980, 2000)
    MoveCamera(59, 23, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(29550, 2000)
    OP_71(0x4, 0xB5, 0xB5, 0x0, 0x0)
    OP_71(0x23, 0xB5, 0xB5, 0x0, 0x0)
    OP_64(0x12)
    FadeToDark(300, 0, 100)
    OP_6F(0x79)

    NpcTalk(
        0x11,
        "Lloyd",
        (
            "#00005FIt seems they've got\x01",
            "some kind of trouble...!\x02\x03",
            "#00003F(What do we do!?\x01",
            "At this rate, there could\x01",
            "be a big accident...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KEmergency Navigation\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pass in Front to Stop Them\x01",              # 0
            "Bump Them From Behind to Stop Them\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7454")
    SetScenarioFlags(0x178, 6)

    NpcTalk(
        0x11,
        "Lloyd",
        (
            "#00007FNoｱl!\x01",
            "Increase the speed and pass them!\x02\x03",
            "#00003FIt's somewhat dangerous, but...\x01",
            "Let's stop them by using the car body as a barrier!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Noｱl",
        "#10107F...Roger!\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x6)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_750A")

    label("loc_7454")


    NpcTalk(
        0x11,
        "Lloyd",
        (
            "#00007FNoｱl!\x01",
            "Increase the speed and  \x01",
            "bump them from behind!\x02\x03",
            "#00003FIf they fall in that pond, the\x01",
            "damage could be minimum...!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Noｱl",
        "#10107F...Roger!\x02",
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x7)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_750A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_7609")
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x24, 1, 0, 49)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    Fade(500)
    OP_68(-11870, 600, -31810, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23270, 0)
    BeginChrThread(0x11, 3, 0, 44)
    BeginChrThread(0x12, 3, 0, 41)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()

    NpcTalk(
        0x12,
        "Yuri - Sykes - Reggie",
        "#5S#8A#30WUwahaaaaa...!!\x02",
    )

    Sleep(1200)
    BeginChrThread(0x12, 3, 0, 43)
    OP_0D()
    OP_68(-7500, 600, -37130, 2000)
    MoveCamera(38, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(25520, 2000)
    OP_64(0x12)
    OP_0D()
    Jump("loc_771F")

    label("loc_7609")

    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x24, 1, 0, 50)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x23, 0xB5, 0xF0, 0x1, 0x20)
    Fade(500)
    OP_68(-11870, 600, -31810, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23270, 0)
    BeginChrThread(0x12, 3, 0, 41)
    OP_63(0x12, 0x0, 3100, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    BeginChrThread(0x11, 3, 0, 42)

    NpcTalk(
        0x12,
        "Yuri - Sykes - Reggie",
        "#5S#8A#30WUwahaaaaa...!!\x02",
    )

    Sleep(1200)
    OP_82(0x1F4, 0x64, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    WaitChrThread(0x12, 3)
    BeginChrThread(0x12, 3, 0, 43)
    OP_68(-7500, 600, -37130, 2000)
    MoveCamera(38, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(25520, 2000)
    OP_64(0x12)
    OP_0D()

    label("loc_771F")

    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x24, 0x1000)
    OP_78(0x24, 0x1D)
    OP_74(0x24, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    OP_49()
    SetChrPos(0x1D, -880, -1000, -42770, 170)
    OP_D5(0x1D, 0x0, 0x29810, 0x0, 0x0)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x0)
    OP_71(0x23, 0x5B, 0x78, 0x1, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_68(-6410, 600, -43900, 3000)
    MoveCamera(63, 27, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(19600, 3000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, -2000, -43030, 270)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2000, -2000, -43030, 270)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2000, -2000, -43030, 270)
    OP_49()

    def lambda_782B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_782B)

    def lambda_783C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_783C)

    def lambda_784D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_784D)
    OP_0D()
    OP_6F(0x79)
    Sleep(2000)
    Sound(485, 0, 100, 0)
    Sleep(50)
    Sound(100, 0, 50, 0)
    OP_71(0x23, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1500)
    BeginChrThread(0x1A, 3, 0, 47)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 46)
    Sleep(1000)
    BeginChrThread(0x18, 3, 0, 45)
    WaitChrThread(0x18, 3)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "*pant, pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "A-Are we alive...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I-I thought I was a goner...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-5890, 600, -39990, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25880, 0)
    SetChrPos(0x101, -7160, 0, -37760, 180)
    SetChrPos(0x102, -8730, 0, -37900, 135)
    SetChrPos(0x103, -9140, 0, -39620, 135)
    SetChrPos(0x109, -7560, 0, -35730, 180)
    SetChrPos(0x104, -5260, 0, -35940, 180)
    SetChrPos(0x105, -6310, 0, -35420, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x11, -8550, 0, -30480, 135)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00106F*phew*...\x01",
            "Somehow they look fine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 6)), scpexpr(EXPR_END)), "loc_7B98")
    OP_2C(0x8B, 0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FM-Maybe that's my fault because\x01",
            "I made us pass in front of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FN-No.\x01",
            "It's absolutely better it turned into\x01",
            "an accident than a big disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAnd in the first place, they turned the \x01",
            "steering wheel. They got what they deserved.\x02\x03",
            "#00200FWell, I am glad that everything ended\x01",
            "with our car not getting a scratch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C62")

    label("loc_7B98")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FU-Uhhm...\x01",
            "Maybe bumping into them\x01",
            "was really too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FR-Right...\x01",
            "For being forcible,\x01",
            "maybe it was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FWell, they got what they deserved.\x02",
    )

    CloseMessageWindow()

    label("loc_7C62")


    ChrTalk(
        0x104,
        (
            "#00309FWell, they should be grateful\x01",
            "just for bein' alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, they've got the devil's luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUhhm...\x02\x03",
            "#00000FOh, well. For the time being, let's\x01",
            "report to 2nd Lt. Mireille and to the\x01",
            "District Crime Prevention Section.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_64(0x18)
    OP_64(0x19)
    OP_64(0x1A)
    SetMapObjFlags(0x24, 0x4)
    ClearScenarioFlags(0x178, 6)
    Call(0, 51)
    Return()

    # Function_36_706D end

    def Function_37_7D7E(): pass

    label("Function_37_7D7E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_37_7D7E end

    def Function_38_7DC4(): pass

    label("Function_38_7DC4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -134100, -2000, 14320)
    OP_9F(0x1, -108810, -2000, 13590)
    OP_9F(0x1, -100530, -2000, 9110)
    OP_9F(0x1, -85050, -2000, -6880)
    OP_9F(0x2, 0xFE, 15000, 0x6)
    Return()

    # Function_38_7DC4 end

    def Function_39_7E0A(): pass

    label("Function_39_7E0A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -43460, 0, 1050)
    OP_9F(0x1, -40270, 0, -4210)
    OP_9F(0x1, -33620, 0, -5910)
    OP_9F(0x1, -36270, 0, -12500)
    OP_9F(0x1, -30300, 0, -15190)
    OP_9F(0x1, -29950, 0, -23990)
    OP_9F(0x1, -21680, 0, -25620)
    OP_9F(0x1, -14580, 0, -30740)
    OP_9F(0x2, 0xFE, 9000, 0x6)
    Return()

    # Function_39_7E0A end

    def Function_40_7E88(): pass

    label("Function_40_7E88")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -62310, -2000, -10)
    OP_9F(0x1, -51780, 0, 500)
    OP_9F(0x1, -40680, 0, -580)
    OP_9F(0x1, -34230, 0, -8310)
    OP_9F(0x1, -32860, 0, -16350)
    OP_9F(0x1, -29710, 0, -21610)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_40_7E88 end

    def Function_41_7EEA(): pass

    label("Function_41_7EEA")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -18370, 0, -31800)
    OP_9F(0x1, -13420, 0, -30030)
    OP_9F(0x1, -9100, 0, -32729)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_41_7EEA end

    def Function_42_7F22(): pass

    label("Function_42_7F22")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -21840, 0, -26500)
    OP_9F(0x1, -13400, 0, -26670)
    OP_9F(0x1, -10840, 0, -29640)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_42_7F22 end

    def Function_43_7F5A(): pass

    label("Function_43_7F5A")

    OP_95(0x12, -5160, 0, -36470, 10000, 0x0)
    OP_95(0x12, -3160, 0, -38680, 10000, 0x0)
    OP_95(0x12, -1500, -2000, -40300, 10000, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -1500, -2000, -40300, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_95(0x12, -880, -2000, -42770, 3000, 0x0)
    Return()

    # Function_43_7F5A end

    def Function_44_7FE2(): pass

    label("Function_44_7FE2")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -22220, 0, -26340)
    OP_9F(0x1, -8890, 0, -25820)
    OP_9F(0x1, -6490, 0, -28390)
    OP_9F(0x2, 0xFE, 18000, 0x6)
    Return()

    # Function_44_7FE2 end

    def Function_45_801A(): pass

    label("Function_45_801A")


    def lambda_801F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_801F)
    OP_9B(0x1, 0x18, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x18, -3500, -2000, -42500, 1000, 0x0)
    OP_93(0x18, 0x10E, 0x1F4)
    Return()

    # Function_45_801A end

    def Function_46_8056(): pass

    label("Function_46_8056")


    def lambda_805B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_805B)
    OP_9B(0x1, 0x19, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x19, -3500, -2000, -43700, 1000, 0x0)
    OP_93(0x19, 0x10E, 0x1F4)
    Return()

    # Function_46_8056 end

    def Function_47_8092(): pass

    label("Function_47_8092")


    def lambda_8097():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_8097)
    OP_9B(0x1, 0x1A, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_95(0x1A, -3500, -2000, -41300, 1000, 0x0)
    OP_93(0x1A, 0x10E, 0x1F4)
    Return()

    # Function_47_8092 end

    def Function_48_80CE(): pass

    label("Function_48_80CE")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(493, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sound(487, 0, 50, 0)
    Return()

    # Function_48_80CE end

    def Function_49_8108(): pass

    label("Function_49_8108")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(1200)
    Sound(976, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_49_8108 end

    def Function_50_814A(): pass

    label("Function_50_814A")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(492, 0, 100, 0)
    Sleep(800)
    Sound(196, 0, 70, 0)
    Sound(880, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(1200)
    Sound(976, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_814A end

    def Function_51_8198(): pass

    label("Function_51_8198")

    EventBegin(0x0)
    SetChrPos(0x11, -8560, 0, -31050, 135)
    OP_D5(0x11, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x22, 0x1000)
    ClearMapObjFlags(0x22, 0x4)
    OP_78(0x22, 0x13)
    SetMapObjFrame(0x22, "light", 0x0, 0x1)
    OP_74(0x22, 0x1E)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x13, -13410, 0, -31470, 135)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x21, 0x1000)
    ClearMapObjFlags(0x21, 0x4)
    OP_78(0x21, 0x14)
    SetMapObjFrame(0x21, "light", 0x0, 0x1)
    SetMapObjFrame(0x21, "mark01", 0x0, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_49()
    SetChrPos(0x14, -100, 0, -32439, 180)
    OP_D5(0x14, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-4280, 600, -28840, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26770, 0)
    LoadChrToIndex("chr/ch30600.itc", 0x21)
    LoadChrToIndex("chr/ch32600.itc", 0x22)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -10800, 0, -42330, 90)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -12000, 0, -40540, 45)
    SetChrPos(0x12, -14390, 0, -36830, 180)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0x23, 0x1, 0x1E, 0x1, 0x0)
    SetChrPos(0x18, -8910, 0, -42330, 270)
    SetChrPos(0x19, -8910, 0, -41130, 225)
    SetChrPos(0x1A, -8910, 0, -43530, 315)
    SetChrPos(0x101, -9870, 0, -39550, 222)
    SetChrPos(0x102, -9930, 0, -38020, 225)
    SetChrPos(0x103, -14020, 0, -39900, 0)
    SetChrPos(0x109, -11940, 0, -36430, 270)
    SetChrPos(0x104, -7980, 0, -38440, 225)
    SetChrPos(0x105, -8620, 0, -37660, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_E2(0x3)
    OP_68(-10480, 600, -38660, 7000)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-9700, 600, -39930, 0)
    MoveCamera(49, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20920, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x1B,
        "#2PResidential Street residents, "High Bloods"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#2PI'm taking you in for speeding\x01",
            "and various other charges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Hmph.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Tch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "*A-ATCHOO*!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThe case seems settled, for now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x1C,
        (
            "#07900FGood work everyone.\x01",
            "We were able to catch the runaway\x01",
            "vehicle thanks to your help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    ChrTalk(
        0x1B,
        (
            "#2P2nd Lt. Mireille, thank you\x01",
            "for your cooperation!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(100)

    ChrTalk(
        0x1B,
        (
            "#2PI think you're in a busy moment with\x01",
            "the emergency state of the border, but...\x01",
            "Allow me to express my gratitude!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#07904FUh uh, likewise.\x02\x03",
            "#07900FYou have made decrease by one\x01",
            "the worry factors for the CGF...\x02\x03",
            "#07902FI have to properly thank\x01",
            "the Support Section too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x1C, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        "#00309FHa ha, no problem.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00105FBy the way...\x01",
            "Tio, Miss Noｱl,\x01",
            "how is their car?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10450, 600, -37570, 2000)
    MoveCamera(38, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22020, 2000)

    def lambda_8761():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8761)
    Sleep(50)

    def lambda_8771():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8771)
    Sleep(50)

    def lambda_8781():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8781)
    Sleep(50)

    def lambda_8791():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8791)
    Sleep(50)

    def lambda_87A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87A1)
    Sleep(50)

    def lambda_87B1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_87B1)
    Sleep(50)

    def lambda_87C1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_87C1)
    Sleep(50)

    def lambda_87D1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_87D1)
    Sleep(50)

    def lambda_87E1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_87E1)
    Sleep(50)

    def lambda_87F1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_87F1)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10100FWell, the main cause\x01",
            "was the broken brakes.\x02\x03",
            "#10106FIt seems that the maintenance\x01",
            "was simply sloppy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1A, 500)
    Sleep(100)

    ChrTalk(
        0x19,
        (
            "Reggie, you...\x01",
            "We entrusted that to you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well, it may be that I skipped\x01",
            "it a little bit as of late...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00200FAlso, it appears that the orbal\x01",
            "engine short-circuited.\x02\x03",
            "#00203FIn case they want to repair it,\x01",
            "I think the cost to buy a new\x01",
            "one will be a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FIt's a waste, but... I think there's\x01",
            "nothing to do but decommission it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x103, 500)
    Sleep(100)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        "N-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Tch, it was the new model from Verne\x01",
            "that Yuri went the extra mile to provide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Hmph, to me, one or two\x01",
            "cars are cheap stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "We'll just have to go to an\x01",
            "orbal store and get one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x1A)

    ChrTalk(
        0x1A,
        (
            "Ha ha, that's our Yuri!\x01",
            "You're so generous.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x19,
        (
            "Then, let's go\x01",
            "buy it now.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8540, 600, -39680, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(21910, 2000)

    def lambda_8BB8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BB8)
    Sleep(50)

    def lambda_8BC8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BC8)
    Sleep(50)

    def lambda_8BD8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BD8)
    Sleep(50)

    def lambda_8BE8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8BE8)
    Sleep(50)

    def lambda_8BF8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8BF8)
    Sleep(50)

    def lambda_8C08():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C08)
    Sleep(50)

    def lambda_8C18():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8C18)
    Sleep(50)

    def lambda_8C28():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8C28)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00007FW-Wait!\x02\x03",
            "#00003FBefore that, you were\x01",
            "clearly speeding this time!\x02\x03",
            "#00001FFirst of all, you'll receive a penalty and...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8CBE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8CBE)
    Sleep(50)

    def lambda_8CCE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8CCE)
    Sleep(50)

    def lambda_8CDE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8CDE)
    Sleep(1000)

    ChrTalk(
        0x18,
        "Hmph, a penalty you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "To us foreigners, you shouldn't\x01",
            "be able to give a great penalty\x01",
            "according to autonomous state law.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E3F")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "QS_1105 Runaway Vehicle Crackdown 1? (For Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not Cleared]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2B")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_8E3F")

    label("loc_8E2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3F")
    OP_29(0x69, 0x3, 0x10)

    label("loc_8E3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8ED9")

    ChrTalk(
        0x18,
        (
            "It's going to end with paying a fine\x01",
            "at best, like the other time, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FOh boy, this ending again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FCC")

    label("loc_8ED9")


    ChrTalk(
        0x18,
        (
            "It's going to end with paying a\x01",
            "fine at best anyway, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        "#00305FI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell, it's true that with the laws in force\x01",
            "it appears the situation is that the strong\x01",
            "hand can't be taken against foreigners...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FCC")

    TurnDirection(0x104, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x19,
        "Uh uh, that's exactly it.\x02",
    )

    CloseMessageWindow()

    def lambda_8FFA():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8FFA)
    Sleep(50)

    def lambda_900A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_900A)
    Sleep(50)

    def lambda_901A():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_901A)
    Sleep(500)

    ChrTalk(
        0x18,
        (
            "We're busy too and it'll\x01",
            "probably be a bother for\x01",
            "you too to take us to HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "So, I'll pay the fine or whatever here.\x01",
            "That way, there won't be any complaints, right?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Ha ha, Yuri's smart!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FY-You guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...It is disgusting having\x01",
            "to agree they are right.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x1B)

    ChrTalk(
        0x102,
        "#00103F...No, it won't go that way.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_91DC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_91DC)
    Sleep(50)

    def lambda_91EC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_91EC)
    Sleep(50)

    def lambda_91FC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_91FC)
    Sleep(500)

    ChrTalk(
        0x19,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter "uncle" became the new mayor,\x01",
            "Crossbell autonomous state law\x01",
            "has been constantly reformed.\x02\x03",
            "#00103FI heard that the other day too a part of \x01",
            "the autonomous state law was revisioned.\x02\x03",
            "#00101FBecause of that, penalties for\x01",
            "criminal acts done by foreigners\x01",
            "have been strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "What did you...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "In this case, a 1 month of driving\x01",
            "license suspension applies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "That's appropriate.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9408():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9408)
    Sleep(50)

    def lambda_9418():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9418)
    Sleep(50)

    def lambda_9428():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9428)
    Sleep(500)

    ChrTalk(
        0x19,
        "T-The driving license is suspended for a month!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...That means that even\x01",
            "if we bought a new car\x01",
            "we couldn't drive it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "M-Maybe we really\x01",
            "went too far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "...D-Don't screw with me...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Why do I have to get\x01",
            "such a penalty!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4SDo you think that the likes of\x01",
            "you police of an autonomous\x01",
            "state have the right to judge ME!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "...Ha, ha ha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "There's no way something like the\x01",
            "Crossbell police could judge us!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x1A,
        (
            "Y-Yuri, Sykes.\x01",
            "You know...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    Sleep(100)

    ChrTalk(
        0x18,
        (
            "Shut up, Reggie!\x01",
            "They're trying to ruin\x01",
            "our trip, you know!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1B, 500)
    Sleep(100)

    ChrTalk(
        0x18,
        (
            "In this case, I'll use my dad's\x01",
            "influence and put pressure on\x01",
            "the autonomous state governm──\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-8700, 600, -39850, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18880, 0)
    OP_0D()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x1B,
        "#5S...Give it a rest now!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_985D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_985D)
    Sleep(50)

    def lambda_986D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_986D)
    Sleep(50)

    def lambda_987D():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_987D)
    Sleep(50)

    def lambda_988D():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_988D)
    Sleep(50)

    def lambda_989D():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_989D)
    Sleep(50)

    def lambda_98AD():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_98AD)
    Sleep(50)

    def lambda_98BD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_98BD)
    Sleep(50)

    def lambda_98CD():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_98CD)
    Sleep(50)

    def lambda_98DD():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_98DD)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "On this occasion, the penalty\x01",
            "and so on aren't a big problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "How much of a scare did\x01",
            "you cause to innocent people\x01",
            "with your driving...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Did you even\x01",
            "think about that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "W-What's suddenly got into her...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "H-Hmph...\x01",
            "We don't give a damn about\x01",
            "how the commoners are scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Also, it's just a mere orbal car──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Then...\x01",
            "Weren't you yourselves afraid!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Even in this accident, if the\x01",
            "Support Section didn't help you, \x01",
            "you could've lost your lives!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "I-It's true that when we plunged into\x01",
            "the lake I thought I was a goner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...Ha, ha ha, what're you saying?\x01",
            "No way that could've happened to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It doesn't matter who you're!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "There're people unrelated to \x01",
            "who suddenly are hurt by getting\x01",
            "involved in an accidents or crimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "As a police officer,\x01",
            "I saw cases like that\x01",
            "many times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Your dangerous driving\x01",
            "has given that much\x01",
            "fear to strangers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "And even so, you\x01",
            "weren't afraid!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Continuing to cause trouble without even\x01",
            "thinking about other people's feelings...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x1B,
        "#4S"Those of Noble Blood"? What a joke!!\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x1B,
        "#4SAren't you ashamed as persons!?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x18,
        "#100W...Gh...gh...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSenior Kate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "...In any case, I'll take\x01",
            "you to headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Be sure to firmly repent in the month \x01",
            "your license is going to be suspended!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Come on, if you understood,\x01",
            "get in the patrol car, get in!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x1A,
        "H-Hey, Yuri, Sykes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    Sleep(100)

    ChrTalk(
        0x19,
        "Yeah, honestly, this time we...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "......Tch......\x02",
    )

    CloseMessageWindow()
    OP_68(-10780, 600, -37980, 3000)
    MoveCamera(37, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(18880, 3000)
    BeginChrThread(0x18, 1, 0, 57)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 52)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 53)
    Sleep(100)
    BeginChrThread(0x104, 1, 0, 54)
    Sleep(100)
    BeginChrThread(0x105, 1, 0, 55)
    Sleep(100)

    def lambda_9FA4():

        label("loc_9FA4")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_9FA4")

    QueueWorkItem2(0x103, 1, lambda_9FA4)
    Sleep(100)
    BeginChrThread(0x109, 1, 0, 56)
    Sleep(100)

    def lambda_9FC2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9FC2)
    Sleep(50)

    def lambda_9FD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9FD2)
    Sleep(2500)

    def lambda_9FE2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FE2)
    Sleep(50)

    def lambda_9FF2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FF2)
    Sleep(50)

    def lambda_A002():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A002)
    Sleep(1000)

    def lambda_A012():

        label("loc_A012")

        TurnDirection(0xFE, 0x18, 0)
        Yield()
        Jump("loc_A012")

    QueueWorkItem2(0x109, 1, lambda_A012)
    WaitChrThread(0x18, 1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x22, 0x169, 0x186, 0x1, 0x0)
    Sleep(500)
    OP_79(0x23)
    Sleep(300)

    def lambda_A04B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A04B)

    def lambda_A060():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_A060)
    Sleep(300)

    ChrTalk(
        0x19,
        "H-Hey, Yuri!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "W-Waaait!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x1A, 1, 0, 59)
    WaitChrThread(0x19, 1)

    def lambda_A0A8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A0A8)

    def lambda_A0BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_A0BD)
    WaitChrThread(0x1A, 1)

    def lambda_A0D2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A0D2)

    def lambda_A0E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_A0E7)
    Sleep(500)
    Sound(461, 0, 100, 0)
    OP_71(0x22, 0x187, 0x1A4, 0x1, 0x0)
    Sleep(800)
    OP_79(0x23)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_68(-9990, 600, -38760, 3000)
    OP_6F(0x79)
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha, it seems it took\x01",
            "quite a toll on them.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00104F(Yes... Miss Kate had a\x01",
            "staggering threatening attitude.)\x02\x03",
            "#00102F(They aren't used to get yelled at normally,\x01",
            "so maybe it was a good medicine for them.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x1B,
        (
            "Everyone from the SSS, 2nd Lt. Mireille...\x01",
            "Once again, I thank you for your cooperation!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A293():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A293)
    Sleep(50)

    def lambda_A2A3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2A3)
    Sleep(50)

    def lambda_A2B3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2B3)
    Sleep(50)

    def lambda_A2C3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2C3)
    Sleep(50)

    def lambda_A2D3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A2D3)
    Sleep(50)

    def lambda_A2E3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A2E3)
    Sleep(50)

    def lambda_A2F3():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A2F3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FYes, thank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, thank goodness\x01",
            "it was quite fun.\x02\x03",
            "#10304FI could experience\x01",
            "a car chase too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F...I don't think it was fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#07903FPatrol Officer Kate... Your words\x01",
            "have resounded in my heart too.\x02\x03",
            "#07902FLet's both do our best\x01",
            "to protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)
    Sleep(100)

    ChrTalk(
        0x1B,
        "Uh uh, yes!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...Then, I'll excuse myself!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2670, 2900, -21660, 0)
    MoveCamera(31, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27790, 0)
    SetChrPos(0x101, -1680, 0, -23640, 0)
    SetChrPos(0x102, -3300, 0, -25110, 0)
    SetChrPos(0x103, -240, 0, -24520, 0)
    SetChrPos(0x109, -3620, 0, -26890, 0)
    SetChrPos(0x104, -1950, 0, -25950, 0)
    SetChrPos(0x105, -4710, 0, -25570, 0)
    SetChrPos(0x1C, -3020, 0, -22920, 0)
    SetChrPos(0x13, -2650, 0, -18410, 0)
    OP_68(-2670, 600, -21660, 5000)
    BeginChrThread(0x13, 1, 0, 60)
    StopBGM(0xFA0)
    Sound(457, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_68(-2220, 600, -22860, 3000)
    SetCameraDistance(22640, 3000)
    OP_6F(0x79)
    SetChrFlags(0x13, 0x80)
    TurnDirection(0x1C, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x1C,
        (
            "#07903FThen, I'll go deliver their orbal\x01",
            "car to the appropriate place.\x02\x03",
            "#07900FCan I have you accompany me?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A608():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A608)
    Sleep(50)

    def lambda_A618():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A618)
    Sleep(50)

    def lambda_A628():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A628)
    Sleep(50)

    def lambda_A638():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A638)
    Sleep(50)

    def lambda_A648():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A648)
    Sleep(50)

    def lambda_A658():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A658)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00304FWell, we've come this far, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAllow us to come with you!\x02",
    )

    CloseMessageWindow()
    StopSound(128, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others helped the\x01",
            "CGF with the runaway vehicle hauling work...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And resumed their activities at Bellguard Gate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Runaway Vehicle Pursuit]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8B, 0x1, 0x8)
    OP_29(0x8B, 0x1, 0x9)
    OP_29(0x8B, 0x4, 0x10)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x1C, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_37()
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t2000", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_51_8198 end

    def Function_52_A82C(): pass

    label("Function_52_A82C")

    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_52_A82C end

    def Function_53_A843(): pass

    label("Function_53_A843")

    OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_53_A843 end

    def Function_54_A85A(): pass

    label("Function_54_A85A")

    OP_9B(0x1, 0x104, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_54_A85A end

    def Function_55_A871(): pass

    label("Function_55_A871")

    OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_55_A871 end

    def Function_56_A888(): pass

    label("Function_56_A888")

    OP_93(0x109, 0x5A, 0x1F4)
    OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(2500)
    Return()

    # Function_56_A888 end

    def Function_57_A8A2(): pass

    label("Function_57_A8A2")

    OP_9B(0x1, 0x18, 0x0, 0x320, 0x5DC, 0x0)
    OP_95(0x18, -9870, 0, -39550, 1500, 0x0)

    def lambda_A8CA():
        TurnDirection(0x19, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A8CA)
    OP_95(0x18, -12250, 0, -33890, 1500, 0x0)
    OP_95(0x18, -13950, 0, -33830, 1500, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    Return()

    # Function_57_A8A2 end

    def Function_58_A902(): pass

    label("Function_58_A902")

    OP_9B(0x0, 0x19, 0x0, 0x7D0, 0xBB8, 0x0)
    OP_95(0x19, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x19, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    Return()

    # Function_58_A902 end

    def Function_59_A941(): pass

    label("Function_59_A941")

    OP_95(0x1A, -8910, 0, -41130, 3000, 0x0)
    OP_95(0x1A, -10610, 0, -39800, 3000, 0x0)
    OP_95(0x1A, -12250, 0, -33890, 3000, 0x0)
    OP_95(0x1A, -13950, 0, -33830, 3000, 0x0)
    OP_93(0x1A, 0x0, 0x1F4)
    Return()

    # Function_59_A941 end

    def Function_60_A999(): pass

    label("Function_60_A999")

    OP_9F(0x0, 0x13)
    OP_9F(0x1, -2650, 0, -18410)
    OP_9F(0x1, -2370, 0, -5440)
    OP_9F(0x1, 2900, 0, 3350)
    OP_9F(0x1, 610, 640, 12550)
    OP_9F(0x1, 610, 2500, 19990)
    OP_9F(0x1, 2510, 2500, 24560)
    OP_9F(0x2, 0x13, 5500, 0x6)
    Return()

    # Function_60_A999 end

    def Function_61_A9FB(): pass

    label("Function_61_A9FB")

    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00001FWe can't do any detours.\x01",
            "In any case, let's head to the accident site.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -60010, -1990, 470, 89)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_61_A9FB end

    SaveToFile()

Try(main)
