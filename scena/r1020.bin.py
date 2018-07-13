from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1020.bin",                # FileName
        "r1020",                    # MapName
        "r1020",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x06,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 3, 0, 4],
    )

    BuildStringList((
        "r1020",                  # 0
        "Large Redheaded Man",    # 1
        "支援課車",               # 2
        "暴走車",                 # 3
        "列車",                   # 4
        "Monster",                # 5
        "Monster",                # 6
        "Monster",                # 7
        "Monster",                # 8
        "Monster",                # 9
        "Monster",                # 10
        "Monster",                # 11
        "Monster",                # 12
        "ブラックハンター",       # 13
        "ブラックハンター",       # 14
        "ガンテ",                 # 15
        "ガンテ",                 # 16
        "オノクジャク",           # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "br1000",                 # 21
        "br1000",                 # 22
        "br1000",                 # 23
        "br1000",                 # 24
        "br1000",                 # 25
        "br1000",                 # 26
        "br1000",                 # 27
        "br1000",                 # 28
        "To Crossbell City",      # 29
        "To Bellguard Gate",      # 30
    ))

    ATBonus("ATBonus_690", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_6B0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_54F7", 0,   3,   0,   5,   2,   3,   0)
    Sepith("Sepith_5507", 0,   6,   0,   6,   0,   0,   1)
    Sepith("Sepith_552F", 17,  17,  17,  17,  17,  17,  17)
    Sepith("Sepith_54EF", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_54FF", 2,   2,   2,   3,   1,   1,   1)
    Sepith("Sepith_5537", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_6F0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_704", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_754", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_758", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_75C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_760", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_764", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_768", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_76C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 2, 13, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_790", 0x0000, 50, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_54F7", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
        )
    )

    BattleInfo(
        "BattleInfo_858", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_5507", 30, 40, 20, 10,
        (
            ("ms70500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70500.dat", "ms70500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70500.dat", "ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
        )
    )

    BattleInfo(
        "BattleInfo_C14", 0x0000, 50, 6, 90, 8, 1, 50, 0, "br1000", "Sepith_552F", 40, 30, 20, 10,
        (
            ("ms66403.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms66403.dat", "ms66403.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms66403.dat", "ms66403.dat", "ms66403.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms66403.dat", "ms66403.dat", "ms66403.dat", "ms66403.dat", 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
        )
    )

    BattleInfo(
        "BattleInfo_AB0", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_54EF", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
        )
    )

    BattleInfo(
        "BattleInfo_9E8", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_54FF", 30, 40, 20, 10,
        (
            ("ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
        )
    )

    BattleInfo(
        "BattleInfo_B78", 0x0000, 84, 6, 60, 6, 1, 30, 0, "br1000", "Sepith_5537", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7450", "ed7453", "ATBonus_690"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D64", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65100.dat", "ms65100.dat", "ms65100.dat", "ms65100.dat", "ms65100.dat", "ms65100.dat", 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7451", "ed7453", "ATBonus_6B0"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_DA8", 0x0000, 25, 6, 0, 0, 1, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70300.dat", "ms70300.dat", "ms70300.dat", "ms70300.dat", "ms70300.dat", "ms70300.dat", "ms70300.dat", "ms70300.dat", "MonsterBattlePostion_6F0", "MonsterBattlePostion_750", "ed7451", "ed7453", "ATBonus_690"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CDC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7453", "ed7453", "ATBonus_690"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D20", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_6D0", "MonsterBattlePostion_750", "ed7453", "ed7453", "ATBonus_690"),
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
        "apl/ch51103.itc",                   # 0F
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch70550.itc",               # 12
        "monster/ch70550.itc",               # 13
        "monster/ch65150.itc",               # 14
        "monster/ch65150.itc",               # 15
        "monster/ch70450.itc",               # 16
        "monster/ch70451.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
        "monster/ch66450.itc",               # 1C
        "monster/ch66450.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294854347, 0,       4294950046, 0,    453,  0x0, 17,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294857597, 0,       4294945247, 0,    453,  0x0, 6,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294850197, 0,       4294947846, 0,    453,  0x0, 21,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294860947, 0,       4294951597, 0,    453,  0x0, 3,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294849146, 0,       4294948946, 0,    453,  0x0, 42,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294854146, 0,       4294947647, 0,    453,  0x0, 40,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294860546, 0,       4294949747, 0,    453,  0x0, 46,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294853046, 0,       4294945147, 0,    453,  0x0, 31,  15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294936467, 0,       4294954796, 270,  485,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294900977, 4294966296, 4294930157, 270,  485,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294936467, 0,       4294954796, 270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294900977, 4294966296, 4294930157, 270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294896417, 4294966796, 4294924466, 180,  484,  0x0, 0,   16,  0,   0,   2,   255, 255, 255,  0)

    DeclMonster(4294951046, 4294934376, 0,       0x1010000,    "BattleInfo_790", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294939716, 4294957326, 0,       0x10100B4,    "BattleInfo_858", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294936436, 4294954496, 0,       0x1010087,    "BattleInfo_C14", 0,   28,  0xFFFF, 12, 13)
    DeclMonster(4294920156, 4294926566, 4294966296, 0x1010000,    "BattleInfo_AB0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294894576, 4294936936, 4294966296, 0x1010000,    "BattleInfo_858", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294900186, 4294925116, 4294966296, 0x1010000,    "BattleInfo_790", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294900936, 4440,    4294967286, 0x1010000,    "BattleInfo_AB0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294862106, 4294955946, 4294967286, 0x1010000,    "BattleInfo_9E8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294851906, 4294946946, 4294967286, 0x1010000,    "BattleInfo_9E8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294841786, 4294960196, 4294967286, 0x1010000,    "BattleInfo_858", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294952386, 4294948216, 0,       0x1010000,    "BattleInfo_B78", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294900416, 4294960436, 0,       0x1010000,    "BattleInfo_B78", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294866656, 4780,    0,       0x1010000,    "BattleInfo_B78", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294933116, 4294964586, 0,       0x18500B4,    "BattleInfo_D64", 0,   20,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 11,  -76.5,                 9.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.091523170471191,    2.386486530303955,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 20,  -76.5,                 9.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.091523170471191,    2.386486530303955,     0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 28,  -34.18000030517578,    -2.7100000381469727,   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   4.272500038146973,     0.3387500047683716,    0.25,                  1.0])

    DeclActor(4294896416, 4294966296, 4294924466, 1200,    4294896416, 0,       4294924466, 0x007C, 0,  5,  0x0000)
    DeclActor(4294864426, 4294967246, 4294944266, 1200,    4294864426, 950,     4294944266, 0x007C, 0,  6,  0x0000)
    DeclActor(4294936466, 0,       4294954796, 1200,    4294936466, 0,       4294954796, 0x007C, 0,  7,  0x0000)
    DeclActor(4294900976, 4294966296, 4294930156, 1200,    4294900976, 4294966296, 4294930156, 0x007C, 0,  8,  0x0000)

    PlaceName(25.0, 0.0, 10.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-160.0, 0.0, -16.0, 0x0000, 0x0000, "To Bellguard Gate")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 12
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 13

    ScpFunction((
        "Function_0_F08",          # 00, 0
        "Function_1_F24",          # 01, 1
        "Function_2_F43",          # 02, 2
        "Function_3_F62",          # 03, 3
        "Function_4_FC4",          # 04, 4
        "Function_5_1E75",         # 05, 5
        "Function_6_2091",         # 06, 6
        "Function_7_21E3",         # 07, 7
        "Function_8_2541",         # 08, 8
        "Function_9_289F",         # 09, 9
        "Function_10_28D3",        # 0A, 10
        "Function_11_28D7",        # 0B, 11
        "Function_12_2E24",        # 0C, 12
        "Function_13_2E34",        # 0D, 13
        "Function_14_3F3D",        # 0E, 14
        "Function_15_3F6E",        # 0F, 15
        "Function_16_3F9F",        # 10, 16
        "Function_17_4154",        # 11, 17
        "Function_18_42BF",        # 12, 18
        "Function_19_4340",        # 13, 19
        "Function_20_4397",        # 14, 20
        "Function_21_4802",        # 15, 21
        "Function_22_4945",        # 16, 22
        "Function_23_4A71",        # 17, 23
        "Function_24_4EB8",        # 18, 24
        "Function_25_4F0C",        # 19, 25
        "Function_26_4F97",        # 1A, 26
        "Function_27_4FDD",        # 1B, 27
        "Function_28_5023",        # 1C, 28
    ))


    def Function_0_F08(): pass

    label("Function_0_F08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F23")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_F08")

    label("loc_F23")

    Return()

    # Function_0_F08 end

    def Function_1_F24(): pass

    label("Function_1_F24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F42")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_F24")

    label("loc_F42")

    Return()

    # Function_1_F24 end

    def Function_2_F43(): pass

    label("Function_2_F43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F61")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_F43")

    label("loc_F61")

    Return()

    # Function_2_F43 end

    def Function_3_F62(): pass

    label("Function_3_F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F76")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_F99")

    label("loc_F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F8A")
    ClearScenarioFlags(0x22, 1)
    Event(0, 17)
    Jump("loc_F99")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F99")
    ClearScenarioFlags(0x22, 2)
    Event(0, 23)

    label("loc_F99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    Event(0, 21)
    Jump("loc_FC0")

    label("loc_FAF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC0")
    Event(0, 22)

    label("loc_FC0")

    Call(0, 9)
    Return()

    # Function_3_F62 end

    def Function_4_FC4(): pass

    label("Function_4_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_FD6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD6")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_FEE")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1006")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1017")
    Call(0, 16)

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1043")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103E")
    ClearChrFlags(0x26, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetChrFlags(0x26, 0x8000)

    label("loc_103E")

    Jump("loc_104D")

    label("loc_1043")

    SetChrFlags(0x26, 0x80)
    ModifyEventFlags(0, 2, 0x80)

    label("loc_104D")

    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BFA")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1CD6")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
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
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)
    ClearMapObjFlags(0x24, 0x4)
    ClearMapObjFlags(0x25, 0x4)
    ClearMapObjFlags(0x26, 0x4)
    ClearMapObjFlags(0x27, 0x4)
    ClearMapObjFlags(0x28, 0x4)
    Jump("loc_1D78")

    label("loc_1CD6")

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
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    SetMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x27, 0x4)
    SetMapObjFlags(0x28, 0x4)

    label("loc_1D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8B")
    OP_70(0x0, 0x0)
    Jump("loc_1D8F")

    label("loc_1D8B")

    OP_70(0x0, 0x1E)

    label("loc_1D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA2")
    OP_70(0x1, 0x0)
    Jump("loc_1DA6")

    label("loc_1DA2")

    OP_70(0x1, 0x1E)

    label("loc_1DA6")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E07")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -30830, 0, -12500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1E07")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E53")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -66320, -1000, -37140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1E53")

    OP_1C(0x0, 0x29, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x2A, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x2B, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_4_FC4 end

    def Function_5_1E75(): pass

    label("Function_5_1E75")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2046")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F78")
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x18, 0x0, 0)
    OP_98(0x18, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1ED2():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1ED2)

    def lambda_1EEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1EEC)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x18, 1)
    Battle("BattleInfo_DA8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F59"),
        (2, "loc_1F68"),
        (1, "loc_1F75"),
        (SWITCH_DEFAULT, "loc_1F78"),
    )


    label("loc_1F59")

    SetScenarioFlags(0x21B, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1F78")

    label("loc_1F68")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1F75")

    OP_B9(0x0)
    Return()

    label("loc_1F78")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xB2, 1)"), scpexpr(EXPR_END)), "loc_1FD1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_2041")

    label("loc_1FD1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB2),
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

    label("loc_2041")

    Jump("loc_2085")

    label("loc_2046")

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

    label("loc_2085")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1E75 end

    def Function_6_2091(): pass

    label("Function_6_2091")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1AA, 1)"), scpexpr(EXPR_END)), "loc_2116")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_2188")

    label("loc_2116")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
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

    label("loc_2188")

    Jump("loc_21D7")

    label("loc_218D")

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

    label("loc_21D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2091 end

    def Function_7_21E3(): pass

    label("Function_7_21E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_239B")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_237C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2377")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2374")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2299():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2299)
    TurnDirection(0x14, 0x0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    PlayEffect(0x7, 0x1, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_CDC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2356")
    Call(1, 5)
    Jump("loc_236F")

    label("loc_2356")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_236C")
    Call(1, 4)
    Jump("loc_236F")

    label("loc_236C")

    Call(1, 3)

    label("loc_236F")

    Jump("loc_2377")

    label("loc_2374")

    Call(1, 1)

    label("loc_2377")

    Jump("loc_2392")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2392")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2392")

    TalkEnd(0xFF)
    Return()

    label("loc_239B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_2526")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2521")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_251E")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2443():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2443)
    TurnDirection(0x16, 0x0, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    PlayEffect(0x7, 0x1, 0x16, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2519")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2500")
    Call(1, 5)
    Jump("loc_2519")

    label("loc_2500")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2516")
    Call(1, 4)
    Jump("loc_2519")

    label("loc_2516")

    Call(1, 3)

    label("loc_2519")

    Jump("loc_2521")

    label("loc_251E")

    Call(1, 1)

    label("loc_2521")

    Jump("loc_253C")

    label("loc_2526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_253C")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_253C")

    TalkEnd(0xFF)
    Return()

    # Function_7_21E3 end

    def Function_8_2541(): pass

    label("Function_8_2541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26F9")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_26DA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D5")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_26D2")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_25F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_25F7)
    TurnDirection(0x15, 0x0, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    PlayEffect(0x7, 0x1, 0x15, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_CDC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26CD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_26B4")
    Call(1, 5)
    Jump("loc_26CD")

    label("loc_26B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_26CA")
    Call(1, 4)
    Jump("loc_26CD")

    label("loc_26CA")

    Call(1, 3)

    label("loc_26CD")

    Jump("loc_26D5")

    label("loc_26D2")

    Call(1, 1)

    label("loc_26D5")

    Jump("loc_26F0")

    label("loc_26DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_26F0")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_26F0")

    TalkEnd(0xFF)
    Return()

    label("loc_26F9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_2884")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287F")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_287C")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_27A1)
    TurnDirection(0x17, 0x0, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    PlayEffect(0x7, 0x1, 0x17, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x17, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2877")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_285E")
    Call(1, 5)
    Jump("loc_2877")

    label("loc_285E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2874")
    Call(1, 4)
    Jump("loc_2877")

    label("loc_2874")

    Call(1, 3)

    label("loc_2877")

    Jump("loc_287F")

    label("loc_287C")

    Call(1, 1)

    label("loc_287F")

    Jump("loc_289A")

    label("loc_2884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_289A")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_289A")

    TalkEnd(0xFF)
    Return()

    # Function_8_2541 end

    def Function_9_289F(): pass

    label("Function_9_289F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28BC")
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)

    label("loc_28BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_28CD")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_28D2")

    label("loc_28CD")

    SetChrFlags(0x1B, 0x80)

    label("loc_28D2")

    Return()

    # Function_9_289F end

    def Function_10_28D3(): pass

    label("Function_10_28D3")

    Call(1, 6)
    Return()

    # Function_10_28D3 end

    def Function_11_28D7(): pass

    label("Function_11_28D7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    SoundLoad(451)
    SoundLoad(3830)
    SoundLoad(3831)
    OP_68(-79350, 1000, 13750, 0)
    MoveCamera(72, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -76000, 0, 11500, 315)
    SetChrPos(0x102, -77000, 0, 10500, 315)
    SetChrPos(0x109, -75000, 0, 10500, 315)
    SetChrPos(0x105, -76000, 0, 9500, 315)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -84500, 0, 27500, 0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x2, 0xB)
    OP_49()
    SetChrPos(0xB, -115000, -14000, 56000, 90)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(20500, 2000)

    def lambda_29ED():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29ED)
    Sleep(50)

    def lambda_2A05():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A05)
    Sleep(50)

    def lambda_2A1D():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A1D)
    Sleep(50)

    def lambda_2A35():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A35)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#11POh...\x02",
    )

    CloseMessageWindow()
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-84500, 1000, 27500, 4000)
    MoveCamera(45, 27, 0, 4000)
    SetCameraDistance(22600, 4000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        "#11P#30W............\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -85100, 0, 18100, 0)
    SetChrPos(0x102, -83900, 0, 18100, 0)
    SetChrPos(0x109, -83900, 0, 17000, 0)
    SetChrPos(0x105, -85100, 0, 17000, 0)
    OP_68(-84500, 1000, 25500, 4000)
    MoveCamera(45, 20, 0, 4000)
    SetCameraDistance(20500, 4000)

    def lambda_2B41():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B41)
    Sleep(100)

    def lambda_2B59():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B59)
    Sleep(100)

    def lambda_2B71():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2B71)
    Sleep(100)

    def lambda_2B89():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B89)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#12PGood morning.\x02\x03",
            "Could you have come for a\x01",
            "walk on the highway too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    ChrTalk(
        0x8,
        "#11P#3830V#40W──It's coming.\x02",
    )

    CloseMessageWindow()
    OP_24(0xEF6)

    ChrTalk(
        0x101,
        "#00005F#12PHuh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#3831V#11P#30WIt's a train from the Empire.\x01",
            "Watch it carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEF7)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Sound(490, 0, 100, 0)
    Sound(451, 2, 10, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_25(0x1C3, 0x14)
    Sleep(1000)
    OP_25(0x1C3, 0x1E)
    OP_68(-84500, 1000, 28500, 2500)

    def lambda_2D18():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D18)
    Sleep(50)

    def lambda_2D30():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D30)
    Sleep(50)

    def lambda_2D48():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D48)
    Sleep(50)

    def lambda_2D60():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D60)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    Sleep(1200)
    Sound(456, 0, 100, 0)
    StopSound(451, 1000, 30)
    Fade(500)
    BeginChrThread(0xB, 3, 0, 12)
    OP_68(-83250, 1000, 35400, 0)
    MoveCamera(350, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(7250, 0)
    OP_68(-83250, 1000, 31550, 3500)
    MoveCamera(43, 25, 0, 3500)
    SetCameraDistance(24000, 3500)
    OP_6F(0x79)
    OP_0D()
    Sleep(250)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xB, 0x3)
    SetChrFlags(0xB, 0x80)
    WaitBGM()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_28D7 end

    def Function_12_2E24(): pass

    label("Function_12_2E24")

    OP_9B(0x0, 0xFE, 0x0, 0x30D40, 0x4E20, 0x1)
    Return()

    # Function_12_2E24 end

    def Function_13_2E34(): pass

    label("Function_13_2E34")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    SoundLoad(3832)
    SoundLoad(3833)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    OP_68(-84500, 1000, 28500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    OP_6F(0x79)
    SetChrPos(0x101, -85100, 0, 25600, 0)
    SetChrPos(0x102, -83900, 0, 25600, 0)
    SetChrPos(0x109, -83900, 0, 24500, 0)
    SetChrPos(0x105, -85100, 0, 24500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -84500, 0, 27500, 0)
    FadeToBright(1000, 0)
    OP_68(-84500, 1000, 26500, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(250)

    ChrTalk(
        0x109,
        (
            "#10105F#12PA transcontinental train\x01",
            "from Erebonia, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PExcuse me, is there anything wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WNo?\x01",
            "There's nothing wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#30WBy the way, you lad over there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WIn that train──\x01",
            "How many passengers there were?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WWell, you should've kept an eye\x01",
            "even inside the cars, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#30WHow many, answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PW-Well...\x01",
            "(How could I know that...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 35, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KHow Many Passengers were Riding in It?\x07\x00\x02",
        )
    )

    MiniGame(0x34, 0xB6, 0x60, 0x63, 0x4, 0x0, 0x0, 0x0, 0x0)
    MiniGame(0x35, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322D")

    label("loc_31D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31FA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322D")

    label("loc_31FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3223")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322D")

    label("loc_3223")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_322D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_324F"),
        (1, "loc_3323"),
        (2, "loc_33CB"),
        (3, "loc_3490"),
        (SWITCH_DEFAULT, "loc_34F8"),
    )


    label("loc_324F")

    OP_2C(0xA1, 0x3)

    ChrTalk(
        0x8,
        "#11P#30WOoh, correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WI don't know if it's just a fluke, but it\x01",
            "seems you've got some good eyes, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI-It was a stroke of luck.\x01",
            "(I'd never thought I'd got it right...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F8")

    label("loc_3323")

    OP_2C(0xA1, 0x2)

    ChrTalk(
        0x8,
        "#11P#30WAlmost correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WEh eh, it seems you've got\x01",
            "some pretty good eyes, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PNo, that's not it...\x01",
            "(I almost got it right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F8")

    label("loc_33CB")

    OP_2C(0xA1, 0x1)

    ChrTalk(
        0x8,
        "#11P#30WClose, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WWell, it seems that you could at least\x01",
            "distinguish the people's shadows, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PYes, somehow...\x01",
            "(As expected, it was impossible...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F8")

    label("loc_3490")


    ChrTalk(
        0x8,
        "#11PWrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POr maybe you don't want to\x01",
            "answer seriously?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P............\x02",
    )

    CloseMessageWindow()
    Jump("loc_34F8")

    label("loc_34F8")


    ChrTalk(
        0x8,
        (
            "#11P#30WUh uh...\x01",
            "Train your eyes as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WDon't look aimlessly.\x01",
            "Look down upon the situation itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#30WIn addition, instantly grab the\x01",
            "elements laying in there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P#30WHuh...\x02",
    )

    CloseMessageWindow()
    OP_68(-84500, 1000, 26500, 1200)
    MoveCamera(46, 19, 0, 1200)
    OP_6E(510, 1200)
    SetCameraDistance(17330, 1200)
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetChrName("Large Redheaded Man")

    AnonymousTalk(
        0xFF,
        (
            "#3832V#40W──Those are the skills to\x01",
            "remain alive on a battlefield.\x02\x03",
            "#3833VWell, just keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xEF9)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    OP_68(-84500, 1000, 25000, 5000)

    def lambda_3737():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3737)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 15)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)
    SetChrFlags(0x8, 0x80)
    StopBGM(0x1388)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        "#00006F#5P*pwaaaah*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#5PW-Who on earth was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PHis physique and lack of openings...\x01",
            "He wasn't a common person...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x105, 0xE1, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10305F#5PWell...\x02\x03",
            "#10303F...Maybe he's even\x01",
            "more than that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    OP_68(-113400, 1000, -16000, 7500)

    def lambda_3920():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3920)
    Sleep(100)

    def lambda_3930():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3930)
    Sleep(100)

    def lambda_3940():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3940)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(750)
    Fade(1000)
    OP_68(-113400, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(23000, 4500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#6PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#6PThose are...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-109700, 1000, -12000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(19000, 3000)
    SetChrPos(0x101, -104870, 0, -2520, 225)
    SetChrPos(0x102, -102360, 0, 720, 225)
    SetChrPos(0x109, -104970, 0, 30, 225)
    SetChrPos(0x105, -102410, 0, -1580, 225)

    def lambda_3A5F():
        OP_95(0xFE, -110600, 0, -13100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A5F)

    def lambda_3A79():
        OP_95(0xFE, -108600, 0, -10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A79)

    def lambda_3A93():
        OP_95(0xFE, -110750, 0, -10950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A93)

    def lambda_3AAD():
        OP_95(0xFE, -107600, 0, -11900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3AAD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106F#5PH-How cruel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#5PCould these be...\x01",
            "The Wanted Monsters spotted this morning!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#5PN-No doubt, it's them!\x01",
            "Their features are those wanted.\x02\x03",
            "#10110FIt seems they're many more\x01",
            "than what was reported...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#10301F#5P3, 4, 5 bodies...\x01",
            "All killed with slashing attacks.\x02\x03",
            "The work of that man just now, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00013F#5PYes, I'm sure of it.\x02\x03",
            "#00008FIt seems they were cut off by\x01",
            "something like giant hatches\x01",
            "rather than a sharp blade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PY-You two...can observe\x01",
            "this quite calmly, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PI'm sorry, this is a little \x01",
            "too much for me too...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#6PUnderstood.\x01",
            "Let's get away from here for now.\x02\x03",
            "#0013F...That man...\x01",
            "It seems he's already left.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10303F#11PYeah, it seemed he was\x01",
            "walking towards Crossbell City.\x02\x03",
            "#10308F...Even if we followed after him now,\x01",
            "it seems it'd be difficult to catch up.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(19200, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [West Crossbell Highway Wanted Monsters]#0C\x01\x07\x00",
            "was abruptly terminated and expired.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -108250, 0, -10450, 225)
    SetScenarioFlags(0x126, 7)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x68, 0x3, 0x2)
    OP_29(0xA1, 0x1, 0x5)
    Sleep(500)
    OP_E2(0x2)
    PlayBGM("ed7205", 0)
    EventEnd(0x5)
    Return()

    # Function_13_2E34 end

    def Function_14_3F3D(): pass

    label("Function_14_3F3D")


    def lambda_3F42():

        label("loc_3F42")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3F42")

    QueueWorkItem2(0xFE, 2, lambda_3F42)

    def lambda_3F54():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F54)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3F3D end

    def Function_15_3F6E(): pass

    label("Function_15_3F6E")


    def lambda_3F73():

        label("loc_3F73")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3F73")

    QueueWorkItem2(0xFE, 2, lambda_3F73)

    def lambda_3F85():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F85)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3F6E end

    def Function_16_3F9F(): pass

    label("Function_16_3F9F")

    ClearChrFlags(0xC, 0xFF)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xC, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0xD, 0xFF)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x10)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xD, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0xE, 0xFF)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xE, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0xF, 0xFF)
    SetChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x10)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xF, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0x10, 0xFF)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x10, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0x11, 0xFF)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x10)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x11, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0x12, 0xFF)
    SetChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x12, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearChrFlags(0x13, 0xFF)
    SetChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x13, 0x10)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x13, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    Return()

    # Function_16_3F9F end

    def Function_17_4154(): pass

    label("Function_17_4154")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x3, 0x9)
    OP_49()
    SetChrPos(0x9, -151770, 0, -12000, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x5A, 0x78, 0x0)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    FadeToBright(1000, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 18)
    OP_68(-135050, -600, -12050, 0)
    MoveCamera(68, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(29000, 0)
    OP_68(-135050, 1800, -12050, 5000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    EndChrThread(0x9, 0x3)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 19)
    OP_68(-91300, 1800, 10000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(36500, 0)
    OP_68(-86000, 1800, 21800, 6500)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4154 end

    def Function_18_42BF(): pass

    label("Function_18_42BF")

    SetChrPos(0xFE, -151770, 0, -12000, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -136830, 0, -12000)
    OP_9F(0x1, -115160, 0, -12000)
    OP_9F(0x1, -111530, 0, -9850)
    OP_9F(0x1, -105920, 0, -3970)
    OP_9F(0x1, -95940, 0, 7180)
    OP_9F(0x1, -85300, 0, 11620)
    OP_9F(0x1, -73710, 0, 7390)
    OP_9F(0x2, 0xFE, 9500, 0x6)
    Return()

    # Function_18_42BF end

    def Function_19_4340(): pass

    label("Function_19_4340")

    SetChrPos(0xFE, -102890, 0, -70, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -94060, 0, 7900)
    OP_9F(0x1, -84410, 0, 12310)
    OP_9F(0x1, -73580, 0, 6220)
    OP_9F(0x1, -67690, 0, -9970)
    OP_9F(0x2, 0xFE, 9500, 0x6)
    Return()

    # Function_19_4340 end

    def Function_20_4397(): pass

    label("Function_20_4397")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SoundLoad(891)
    OP_68(-84000, 1000, 25700, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -84000, 0, 18900, 0)
    SetChrPos(0x102, -83150, 0, 18400, 0)
    SetChrPos(0x103, -84750, 0, 17600, 0)
    SetChrPos(0x104, -83500, 0, 16800, 0)
    SetChrPos(0x109, -84850, 0, 16350, 0)
    SetChrPos(0x105, -84400, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 5000)

    def lambda_447B():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_447B)
    Sleep(50)

    def lambda_4493():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4493)
    Sleep(50)

    def lambda_44AB():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_44AB)
    Sleep(50)

    def lambda_44C3():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_44C3)
    Sleep(50)

    def lambda_44DB():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_44DB)
    Sleep(50)

    def lambda_44F3():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_44F3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    Sound(891, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
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
    Sleep(1000)

    def lambda_45D6():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45D6)
    Sleep(50)

    def lambda_45E6():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45E6)
    Sleep(50)

    def lambda_45F6():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_45F6)
    Sleep(50)

    def lambda_4606():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4606)
    Sleep(50)

    def lambda_4616():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4616)
    Sleep(50)

    def lambda_4626():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4626)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00013F#11PNo way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PIt's from the west!\x01",
            "I can tell even if I'm not peTiote!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PIt seems we're being invited,\x01",
            "like that time with Zeit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PNo doubt.\x02\x03",
            "#00201F...Unlike with Zeit, I can sense\x01",
            "a violent will, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PA quite intelligent monster,\x01",
            "or else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PIn any case, we need\x01",
            "to be careful!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, -84500, 0, 25000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 3)
    ModifyEventFlags(0, 1, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_4397 end

    def Function_21_4802(): pass

    label("Function_21_4802")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-85000, -1000, 37000, 0)
    MoveCamera(35, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -55000, -14000, 55000, 270)
    SetChrPos(0x1, -53200, -14000, 55000, 270)
    SetChrPos(0x2, -51400, -14000, 55000, 270)
    SetChrPos(0x3, -49600, -14000, 55000, 270)
    SetCameraDistance(27000, 7000)

    def lambda_488E():
        OP_97(0x0, 0xFFFF3CB0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_488E)
    Sleep(300)

    def lambda_48AB():
        OP_97(0x1, 0xFFFF3CB0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_48AB)
    Sleep(300)

    def lambda_48C8():
        OP_97(0x2, 0xFFFF3CB0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_48C8)
    Sleep(300)

    def lambda_48E5():
        OP_97(0x3, 0xFFFF3CB0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_48E5)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_493B")
    NewScene("e4212", 100, 0, 0)
    IdleLoop()
    Jump("loc_4944")

    label("loc_493B")

    NewScene("r1070", 100, 0, 0)
    IdleLoop()

    label("loc_4944")

    Return()

    # Function_21_4802 end

    def Function_22_4945(): pass

    label("Function_22_4945")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-85000, -1000, 37000, 0)
    MoveCamera(35, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -90000, -14000, 55000, 90)
    SetChrPos(0x1, -91800, -14000, 55000, 90)
    SetChrPos(0x2, -93600, -14000, 55000, 90)
    SetChrPos(0x3, -95400, -14000, 55000, 90)
    SetCameraDistance(27000, 7000)

    def lambda_49D1():
        OP_97(0x0, 0xC350, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_49D1)
    Sleep(300)

    def lambda_49EE():
        OP_97(0x1, 0xC350, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_49EE)
    Sleep(300)

    def lambda_4A0B():
        OP_97(0x2, 0xC350, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_4A0B)
    Sleep(300)

    def lambda_4A28():
        OP_97(0x3, 0xC350, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_4A28)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    NewScene("r1060", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4945 end

    def Function_23_4A71(): pass

    label("Function_23_4A71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x3, 0x9)
    OP_49()
    SetChrPos(0x9, -155110, 0, -12520, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x2C, 0x4)
    OP_78(0x2C, 0xA)
    SetMapObjFrame(0x2C, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, -155110, 0, -12520, 0)
    OP_D5(0xA, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x2C, 0x1000)
    OP_74(0x2C, 0x1E)
    OP_71(0x2C, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-133390, 600, -12220, 0)
    MoveCamera(64, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(42200, 0)
    OP_E2(0x3)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(493, 0, 100, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 25)
    Sleep(1000)
    OP_68(-118050, -600, -8480, 2500)
    MoveCamera(19, 23, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(38860, 2500)
    BeginChrThread(0x9, 3, 0, 24)
    Sleep(500)

    NpcTalk(
        0xA,
        "Yuri",
        (
            "#6A#40WTsk, they're still after us...\x01",
            "Distance them, Reggie.\x02",
        )
    )

    Sleep(1200)
    Sound(457, 0, 100, 0)

    NpcTalk(
        0xA,
        "Reggie",
        "#6A#40WEh, easy stuff!\x02",
    )

    Sleep(1200)
    Sound(486, 0, 100, 0)
    OP_6F(0x79)
    OP_68(-88770, -600, 6650, 2000)
    MoveCamera(43, 31, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(36640, 2000)
    OP_6F(0x79)
    WaitChrThread(0xA, 3)
    OP_71(0x3, 0xB5, 0xB5, 0x1, 0x20)
    FadeToDark(300, 0, 100)

    NpcTalk(
        0x9,
        "Lloyd",
        "#00001F(At this rate, they'll pull away...!!)\x02",
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
            "Drop the Speed and Pursue\x01",         # 0
            "Leave It to Noｱl's Judgment\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE9")
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)

    NpcTalk(
        0x9,
        "Lloyd",
        "#00007FNoｱl, drop the speed for a moment and pursue them!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Noｱl",
        "#10105FY-Yes!!\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    Sound(457, 0, 100, 0)
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-83200, -600, 9180, 3000)
    BeginChrThread(0x9, 3, 0, 26)
    WaitChrThread(0x9, 3)
    OP_29(0x8B, 0x1, 0x4)
    Jump("loc_4EAB")

    label("loc_4DE9")

    OP_2C(0x8B, 0x1)
    SetScenarioFlags(0x178, 5)
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)

    NpcTalk(
        0x9,
        "Lloyd",
        "#00007FNoｱl, I leave it to you!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Noｱl",
        "#10101FYessir!!\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    OP_71(0x3, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-86520, -600, 9130, 1500)
    MoveCamera(66, 31, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(33070, 1500)
    BeginChrThread(0x9, 3, 0, 27)
    Sleep(1500)
    Sound(487, 0, 100, 0)
    WaitChrThread(0x9, 3)
    OP_29(0x8B, 0x1, 0x5)

    label("loc_4EAB")

    SetScenarioFlags(0x23, 3)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4A71 end

    def Function_24_4EB8(): pass

    label("Function_24_4EB8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -155110, 0, -12520)
    OP_9F(0x1, -113060, 0, -12300)
    OP_9F(0x1, -108940, 0, -10960)
    OP_9F(0x1, -106180, 0, -4950)
    OP_9F(0x1, -102870, 0, 580)
    OP_9F(0x2, 0xFE, 11000, 0x6)
    Return()

    # Function_24_4EB8 end

    def Function_25_4F0C(): pass

    label("Function_25_4F0C")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -155110, 0, -12520)
    OP_9F(0x1, -113060, 0, -12300)
    OP_9F(0x1, -108940, 0, -10960)
    OP_9F(0x1, -106180, 0, -4950)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -94060, 0, 7900)
    OP_9F(0x1, -84410, 0, 12310)
    OP_9F(0x1, -73580, 0, 6220)
    OP_9F(0x1, -67690, 0, -9970)
    OP_9F(0x2, 0xFE, 20000, 0x6)
    Return()

    # Function_25_4F0C end

    def Function_26_4F97(): pass

    label("Function_26_4F97")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -94060, 0, 7900)
    OP_9F(0x1, -84410, 0, 12310)
    OP_9F(0x1, -73580, 0, 6220)
    OP_9F(0x1, -67690, 0, -9970)
    OP_9F(0x2, 0xFE, 9500, 0x6)
    Return()

    # Function_26_4F97 end

    def Function_27_4FDD(): pass

    label("Function_27_4FDD")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -94060, 0, 7900)
    OP_9F(0x1, -84410, 0, 12310)
    OP_9F(0x1, -73580, 0, 6220)
    OP_9F(0x1, -67690, 0, -9970)
    OP_9F(0x2, 0xFE, 20000, 0x6)
    Return()

    # Function_27_4FDD end

    def Function_28_5023(): pass

    label("Function_28_5023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 6)), scpexpr(EXPR_END)), "loc_502D")
    Return()

    label("loc_502D")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Quit]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5109"),
        (SWITCH_DEFAULT, "loc_5122"),
    )


    label("loc_5109")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -34080, 0, -7710, 180)
    EventEnd(0x5)
    Return()

    label("loc_5122")

    Battle("BattleInfo_D64", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-34080, 1000, -7710, 0)
    OP_90(0x0, -34080, 0, -7710, 180)
    OP_90(0x1, -34080, 0, -7710, 180)
    OP_90(0x2, -34080, 0, -7710, 180)
    OP_90(0x3, -34080, 0, -7710, 180)
    OP_90(0x4, -34080, 0, -7710, 180)
    OP_90(0x5, -34080, 0, -7710, 180)
    OP_90(0x6, -34080, 0, -7710, 180)
    OP_90(0x7, -34080, 0, -7710, 180)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_51E4"),
        (1, "loc_51E9"),
        (SWITCH_DEFAULT, "loc_51EC"),
    )


    label("loc_51E4")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_51E9")

    OP_B9(0x0)
    Return()

    label("loc_51EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-32159, 600, -4140, 0)
    MoveCamera(44, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)
    SetChrFlags(0x26, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted Monster exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x10),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x10, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -32070, 0, -2640, 180)
    SetChrPos(0x102, -33150, 0, -8210, 357)
    SetChrPos(0x103, -34950, 0, -3720, 87)
    SetChrPos(0x104, -35600, 0, -6540, 87)
    SetChrPos(0x109, -30590, 0, -4710, 312)
    SetChrPos(0x105, -30830, 0, -6670, 267)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x109,
        (
            "#10105FA Craft Book...\x02\x03",
            "#10102FThis seems to be suited for\x01",
            "senior Randy and Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOk, Wazy.\x01",
            "Let's try it at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x3, 0x193)
    AddCraft(0x4, 0x193)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy and Wazy have learned the\x01\x07\x02",
            ""Last Rebellion"\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 6)
    OP_29(0x88, 0x4, 0x10)
    OP_29(0x88, 0x4, 0x2)
    OP_29(0x88, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_28_5023 end

    SaveToFile()

Try(main)
