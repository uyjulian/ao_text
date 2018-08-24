from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1500.bin",                # FileName
        "r1500",                    # MapName
        "r1500",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x09,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1500",                  # 0
        "Billy",                  # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Young Man",              # 8
        "Policeman",              # 9
        "Policeman",              # 10
        "ビリーのバン",           # 11
        "Fisher",                 # 12
        "バス",                   # 13
        "State Guard Soldier",    # 14
        "State Guard Soldier",    # 15
        "State Guard Soldier",    # 16
        "State Guard Soldier",    # 17
        "State Guard Soldier",    # 18
        "State Guard Soldier",    # 19
        "グマーライ",             # 20
        "グマーライ",             # 21
        "ゴーディ・オッサー",     # 22
        "ゴーディ・オッサー",     # 23
        "Policeman",              # 24
        "Policeman",              # 25
        "Policeman",              # 26
        "Policeman",              # 27
        "Policeman",              # 28
        "Patrol Car",             # 29
        "Patrol Car",             # 30
        "車",                     # 31
        "メルカバ",               # 32
        "メルカバ",               # 33
        "メルカバ",               # 34
        "SE制御",                 # 35
        "br1500",                 # 36
        "br1500",                 # 37
        "br1500",                 # 38
        "br1500",                 # 39
        "br1500",                 # 40
        "br1500",                 # 41
        "br1500",                 # 42
        "To Crossbell City",      # 43
        "To St. Ursula Medical College",# 44
        "To Crossbell Airport",   # 45
    ))

    ATBonus("ATBonus_770", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_6273", 5,   3,   0,   8,   0,   4,   3)
    Sepith("Sepith_628B", 10,  6,   0,   0,   3,   0,   5)
    Sepith("Sepith_6283", 0,   10,  0,   7,   4,   3,   0)
    Sepith("Sepith_627B", 9,   0,   6,   3,   0,   0,   5)
    Sepith("Sepith_62AB", 3,   10,  0,   8,   3,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_7D0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_834", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_83C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_840", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_844", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_848", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_850", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_6273", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_AA8", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_628B", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_9E0", 0x0010, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_6283", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_918", 0x0000, 58, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_627B", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_7B0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    BattleInfo(
        "BattleInfo_B70", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_62AB", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7450", "ed7453", "ATBonus_770"),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_C38", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "ms62100.dat", "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7453", "ed7453", "ATBonus_770"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C7C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_7D0", "MonsterBattlePostion_830", "ed7453", "ed7453", "ATBonus_770"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch24000.itc",                   # 01
        "chr/ch22300.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch27900.itc",                   # 04
        "chr/ch22800.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch30000.itc",                   # 07
        "chr/ch46100.itc",                   # 08
        "chr/ch20400.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch66650.itc",               # 12
        "monster/ch66651.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch65850.itc",               # 16
        "monster/ch65851.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch70250.itc",               # 1A
        "monster/ch70251.itc",               # 1B
    ))

    DeclNpc(14810,   0,       4294946407, 315,  389,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(5809,    0,       4294958296, 135,  389,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6719,    0,       4294957376, 315,  389,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(13380,   0,       4294950657, 270,  389,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(5809,    0,       4294958296, 135,  389,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5809,    0,       4294958296, 135,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6719,    0,       4294957376, 315,  389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(6320,    0,       4294945467, 270,  389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(12579,   0,       4294952607, 270,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(13380,   0,       4294947657, 270,  389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10000,   0,       4294957296, 0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3490,    0,       4294958456, 0,    389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294953437, 0,       4294872127, 270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(38020,   0,       4294851207, 270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294953437, 0,       4294872127, 270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(38020,   0,       4294851207, 270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294948556, 4294896306, 0,       0x1010000,    "BattleInfo_850", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294947976, 4294893836, 10,      0x1010000,    "BattleInfo_850", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294957386, 4294870676, 10,      0x1010000,    "BattleInfo_AA8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294947036, 4294869316, 0,       0x1010000,    "BattleInfo_9E0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16920,   4294883296, 10,      0x1010000,    "BattleInfo_AA8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(22580,   4294901556, 10,      0x1010000,    "BattleInfo_918", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(32310,   4294856016, 0,       0x1010000,    "BattleInfo_B70", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(46440,   4294858766, 900,     0x1010000,    "BattleInfo_918", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 26,  0.0,                   -67.0,                 0.0,                   8100.0,                [0.01666666567325592,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    0.0,                   -0.0,                  22.333332061767578,    -0.0,                  1.0])

    DeclActor(4294956996, 180,     4294954296, 1500,    4294956996, 1680,    4294954296, 0x007C, 0,  28, 0x0000)
    DeclActor(4294953436, 0,       4294872126, 1200,    4294953436, 0,       4294872126, 0x007C, 0,  6,  0x0000)
    DeclActor(38020,   0,       4294851206, 1200,    38020,   0,       4294851206, 0x007C, 0,  7,  0x0000)
    DeclActor(4180,    0,       4294941576, 1200,    4180,    2000,    4294941576, 0x007C, 0,  27, 0x0000)
    DeclActor(5120,    0,       4294940976, 1200,    8000,    2000,    4294957296, 0x007C, 0,  27, 0x0000)
    DeclActor(9210,    0,       4294943086, 1500,    9210,    1700,    4294943086, 0x007C, 0,  47, 0x0000)

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "To St. Ursula Medical College")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "To Crossbell Airport")
    PlaceName(-10.649999618530273, 0.0, -11.800000190734863, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_DF8",          # 00, 0
        "Function_1_EA8",          # 01, 1
        "Function_2_EC7",          # 02, 2
        "Function_3_EE6",          # 03, 3
        "Function_4_FF4",          # 04, 4
        "Function_5_1BB6",         # 05, 5
        "Function_6_2291",         # 06, 6
        "Function_7_25ED",         # 07, 7
        "Function_8_2949",         # 08, 8
        "Function_9_2995",         # 09, 9
        "Function_10_29BD",        # 0A, 10
        "Function_11_2A84",        # 0B, 11
        "Function_12_2BB6",        # 0C, 12
        "Function_13_2BDD",        # 0D, 13
        "Function_14_2C71",        # 0E, 14
        "Function_15_348D",        # 0F, 15
        "Function_16_3536",        # 10, 16
        "Function_17_368D",        # 11, 17
        "Function_18_3707",        # 12, 18
        "Function_19_37BF",        # 13, 19
        "Function_20_393B",        # 14, 20
        "Function_21_39B4",        # 15, 21
        "Function_22_3A45",        # 16, 22
        "Function_23_3ACD",        # 17, 23
        "Function_24_3B4F",        # 18, 24
        "Function_25_3DCC",        # 19, 25
        "Function_26_3E40",        # 1A, 26
        "Function_27_41FA",        # 1B, 27
        "Function_28_4537",        # 1C, 28
        "Function_29_458B",        # 1D, 29
        "Function_30_47DF",        # 1E, 30
        "Function_31_4AFD",        # 1F, 31
        "Function_32_4BFD",        # 20, 32
        "Function_33_564A",        # 21, 33
        "Function_34_56BC",        # 22, 34
        "Function_35_5979",        # 23, 35
        "Function_36_599E",        # 24, 36
        "Function_37_59CC",        # 25, 37
        "Function_38_5A04",        # 26, 38
        "Function_39_5A29",        # 27, 39
        "Function_40_5ACD",        # 28, 40
        "Function_41_5B47",        # 29, 41
        "Function_42_5D21",        # 2A, 42
        "Function_43_5EFB",        # 2B, 43
        "Function_44_60D5",        # 2C, 44
        "Function_45_614F",        # 2D, 45
        "Function_46_6170",        # 2E, 46
        "Function_47_61B9",        # 2F, 47
    ))


    def Function_0_DF8(): pass

    label("Function_0_DF8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E30"),
        (1, "loc_E3C"),
        (2, "loc_E48"),
        (3, "loc_E54"),
        (4, "loc_E60"),
        (5, "loc_E6C"),
        (6, "loc_E78"),
        (SWITCH_DEFAULT, "loc_E84"),
    )


    label("loc_E30")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E3C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E48")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E54")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E60")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E6C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E78")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E84")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EA7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E90")

    label("loc_EA7")

    Return()

    # Function_0_DF8 end

    def Function_1_EA8(): pass

    label("Function_1_EA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_EA8")

    label("loc_EC6")

    Return()

    # Function_1_EA8 end

    def Function_2_EC7(): pass

    label("Function_2_EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_EC7")

    label("loc_EE5")

    Return()

    # Function_2_EC7 end

    def Function_3_EE6(): pass

    label("Function_3_EE6")

    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x1E, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    SetMapObjFlags(0x1D, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F96")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)
    ClearMapObjFlags(0x1D, 0x2000000)
    Jump("loc_FF3")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_FF3")
    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x1E, 0x2000000)

    label("loc_FF3")

    Return()

    # Function_3_EE6 end

    def Function_4_FF4(): pass

    label("Function_4_FF4")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1026")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 13380, 0, -16640, 270)
    Jump("loc_116F")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1034")
    Jump("loc_116F")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1042")
    Jump("loc_116F")

    label("loc_1042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1064")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105F")
    ClearChrFlags(0x13, 0x80)

    label("loc_105F")

    Jump("loc_116F")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1072")
    Jump("loc_116F")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1080")
    Jump("loc_116F")

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108E")
    Jump("loc_116F")

    label("loc_108E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9610, 0, -14320, 225)

    label("loc_10BA")

    Jump("loc_116F")

    label("loc_10BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10D2")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_116F")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10F9")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_116F")

    label("loc_10F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_112A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1125")
    ClearChrFlags(0xF, 0x80)

    label("loc_1125")

    Jump("loc_116F")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1158")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9610, 0, -14320, 225)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_116F")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1166")
    Jump("loc_116F")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_116F")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1183")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)
    Jump("loc_11C8")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1197")
    ClearScenarioFlags(0x22, 1)
    Event(0, 31)
    Jump("loc_11C8")

    label("loc_1197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 32)
    Jump("loc_11C8")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_11C8")
    ClearScenarioFlags(0x22, 3)
    SetChrPos(0x0, 12640, 0, -17790, 270)

    label("loc_11C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166C")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetScenarioFlags(0x38, 0)

    label("loc_1255")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    SetScenarioFlags(0x38, 1)

    label("loc_126B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    SetScenarioFlags(0x38, 2)

    label("loc_1281")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    SetScenarioFlags(0x38, 3)

    label("loc_1297")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")
    SetScenarioFlags(0x38, 4)

    label("loc_12AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    SetScenarioFlags(0x38, 5)

    label("loc_12C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D9")
    SetScenarioFlags(0x38, 6)

    label("loc_12D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    SetScenarioFlags(0x38, 7)

    label("loc_12EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1305")
    SetScenarioFlags(0x39, 0)

    label("loc_1305")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x39, 1)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x39, 2)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x39, 3)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x39, 4)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x39, 5)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x39, 6)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x39, 7)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x3A, 0)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x3A, 1)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x3A, 2)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x3A, 3)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x3A, 4)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x3A, 5)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x3A, 6)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x3A, 7)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x3B, 0)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3B, 1)

    label("loc_147B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1491")
    SetScenarioFlags(0x3B, 2)

    label("loc_1491")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A7")
    SetScenarioFlags(0x3B, 3)

    label("loc_14A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")
    SetScenarioFlags(0x3B, 4)

    label("loc_14BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    SetScenarioFlags(0x3B, 5)

    label("loc_14D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    SetScenarioFlags(0x3B, 6)

    label("loc_14E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    SetScenarioFlags(0x3B, 7)

    label("loc_14FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")
    SetScenarioFlags(0x3D, 5)

    label("loc_1515")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    SetScenarioFlags(0x3D, 6)

    label("loc_152B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    SetScenarioFlags(0x3D, 7)

    label("loc_1541")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157C")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_166C")

    label("loc_157C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159F")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_166C")

    label("loc_159F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_166C")

    label("loc_15C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E5")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_166C")

    label("loc_15E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1608")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_166C")

    label("loc_1608")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162B")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_166C")

    label("loc_162B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164E")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_166C")

    label("loc_164E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166C")
    SetScenarioFlags(0x3C, 7)

    label("loc_166C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1682")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B4")
    SetChrPos(0x0, 2680, 0, -25440, 267)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 13)

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    SetChrPos(0x0, 5120, 0, -26320, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_16E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_16F6")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 12)

    label("loc_16F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BB5")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179E")
    SetScenarioFlags(0x38, 0)

    label("loc_179E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B4")
    SetScenarioFlags(0x38, 1)

    label("loc_17B4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CA")
    SetScenarioFlags(0x38, 2)

    label("loc_17CA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E0")
    SetScenarioFlags(0x38, 3)

    label("loc_17E0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F6")
    SetScenarioFlags(0x38, 4)

    label("loc_17F6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180C")
    SetScenarioFlags(0x38, 5)

    label("loc_180C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1822")
    SetScenarioFlags(0x38, 6)

    label("loc_1822")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
    SetScenarioFlags(0x38, 7)

    label("loc_1838")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184E")
    SetScenarioFlags(0x39, 0)

    label("loc_184E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1864")
    SetScenarioFlags(0x39, 1)

    label("loc_1864")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187A")
    SetScenarioFlags(0x39, 2)

    label("loc_187A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1890")
    SetScenarioFlags(0x39, 3)

    label("loc_1890")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A6")
    SetScenarioFlags(0x39, 4)

    label("loc_18A6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BC")
    SetScenarioFlags(0x39, 5)

    label("loc_18BC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D2")
    SetScenarioFlags(0x39, 6)

    label("loc_18D2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E8")
    SetScenarioFlags(0x39, 7)

    label("loc_18E8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FE")
    SetScenarioFlags(0x3A, 0)

    label("loc_18FE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1914")
    SetScenarioFlags(0x3A, 1)

    label("loc_1914")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")
    SetScenarioFlags(0x3A, 2)

    label("loc_192A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    SetScenarioFlags(0x3A, 3)

    label("loc_1940")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1956")
    SetScenarioFlags(0x3A, 4)

    label("loc_1956")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196C")
    SetScenarioFlags(0x3A, 5)

    label("loc_196C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1982")
    SetScenarioFlags(0x3A, 6)

    label("loc_1982")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1998")
    SetScenarioFlags(0x3A, 7)

    label("loc_1998")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AE")
    SetScenarioFlags(0x3B, 0)

    label("loc_19AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C4")
    SetScenarioFlags(0x3B, 1)

    label("loc_19C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DA")
    SetScenarioFlags(0x3B, 2)

    label("loc_19DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F0")
    SetScenarioFlags(0x3B, 3)

    label("loc_19F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A06")
    SetScenarioFlags(0x3B, 4)

    label("loc_1A06")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1C")
    SetScenarioFlags(0x3B, 5)

    label("loc_1A1C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A32")
    SetScenarioFlags(0x3B, 6)

    label("loc_1A32")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A48")
    SetScenarioFlags(0x3B, 7)

    label("loc_1A48")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5E")
    SetScenarioFlags(0x3D, 5)

    label("loc_1A5E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A74")
    SetScenarioFlags(0x3D, 6)

    label("loc_1A74")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8A")
    SetScenarioFlags(0x3D, 7)

    label("loc_1A8A")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1BB5")

    label("loc_1AC5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE8")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1BB5")

    label("loc_1AE8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1BB5")

    label("loc_1B0B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1BB5")

    label("loc_1B2E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B51")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1BB5")

    label("loc_1B51")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B74")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1BB5")

    label("loc_1B74")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B97")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1BB5")

    label("loc_1B97")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB5")
    SetScenarioFlags(0x3C, 7)

    label("loc_1BB5")

    Return()

    # Function_4_FF4 end

    def Function_5_1BB6(): pass

    label("Function_5_1BB6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BFF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C1F")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1C16")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C1F")

    label("loc_1C16")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C62")
    OP_24(0x7D)
    Jump("loc_1CA5")

    label("loc_1C62")

    SoundDistance(0x7D, 0x34C6, 0x0, 0xFFFD8D16, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E3(0x9D4E, 0x118, 0xFFFE0909)
    OP_E3(0xE06A, 0x384, 0xFFFE9238)
    OP_E3(0xFCDA, 0x5A, 0xFFFF282E)

    label("loc_1CA5")

    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E58")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x35), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000)
    OP_E2(0x1)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_1E75")

    label("loc_1E58")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E75")
    OP_E2(0x0)
    SetScenarioFlags(0x0, 2)

    label("loc_1E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EF9")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x5, 0x12C, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1F50")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x5, 0x12C, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_1F80")

    label("loc_1F50")

    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)

    label("loc_1F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FEF")
    OP_11(0xA0, 0xC8, 0xFF, 0x0, 0x140, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x2, -18000, -1000, -64500, 29000, 1000, -66500)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1FF5")

    label("loc_1FEF")

    SetMapObjFlags(0xB, 0x4)

    label("loc_1FF5")

    MiniGame(0x2F, 0x3, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x14, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2048")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2048")
    Call(0, 9)

    label("loc_2048")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A9")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -13860, 0, -95170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x1, 0x1)

    label("loc_20A9")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20F5")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 38020, 0, -116090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_20F5")

    OP_1B(0x4, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2108")
    Jump("loc_21A0")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_211B")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_212E")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_212E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_214B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")
    OP_1B(0x4, 0x0, 0x19)

    label("loc_2146")

    Jump("loc_21A0")

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2159")
    Jump("loc_21A0")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_216C")
    OP_1B(0x4, 0x0, 0x19)
    Jump("loc_21A0")

    label("loc_216C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_217A")
    Jump("loc_21A0")

    label("loc_217A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2192")
    OP_1B(0x4, 0x0, 0x1E)
    Jump("loc_21A0")

    label("loc_2192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21A0")
    OP_1B(0x4, 0x0, 0x19)

    label("loc_21A0")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21BD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21CE")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21DC")
    Jump("loc_2290")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21ED")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21FB")
    Jump("loc_2290")

    label("loc_21FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_220C")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_220C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2232")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222A")
    Call(0, 9)
    Jump("loc_222D")

    label("loc_222A")

    Call(0, 8)

    label("loc_222D")

    Jump("loc_2290")

    label("loc_2232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2243")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2254")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2265")
    Call(0, 8)
    Jump("loc_2290")

    label("loc_2265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2276")
    Call(0, 9)
    Jump("loc_2290")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2284")
    Jump("loc_2290")

    label("loc_2284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2290")
    Call(0, 8)

    label("loc_2290")

    Return()

    # Function_5_1BB6 end

    def Function_6_2291(): pass

    label("Function_6_2291")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2448")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_2429")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2424")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2421")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2346():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_2346)
    TurnDirection(0x1B, 0x0, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    PlayEffect(0x7, 0x1, 0x1B, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C38", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_241C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2403")
    Call(1, 5)
    Jump("loc_241C")

    label("loc_2403")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2419")
    Call(1, 4)
    Jump("loc_241C")

    label("loc_2419")

    Call(1, 3)

    label("loc_241C")

    Jump("loc_2424")

    label("loc_2421")

    Call(1, 1)

    label("loc_2424")

    Jump("loc_243F")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_243F")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_243F")

    TalkEnd(0xFF)
    Return()

    label("loc_2448")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_25D2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CD")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_25CA")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_24EF)
    TurnDirection(0x1D, 0x0, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    PlayEffect(0x7, 0x1, 0x1D, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C7C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C5")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25AC")
    Call(1, 5)
    Jump("loc_25C5")

    label("loc_25AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25C2")
    Call(1, 4)
    Jump("loc_25C5")

    label("loc_25C2")

    Call(1, 3)

    label("loc_25C5")

    Jump("loc_25CD")

    label("loc_25CA")

    Call(1, 1)

    label("loc_25CD")

    Jump("loc_25E8")

    label("loc_25D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_25E8")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x1, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_25E8")

    TalkEnd(0xFF)
    Return()

    # Function_6_2291 end

    def Function_7_25ED(): pass

    label("Function_7_25ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27A4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_2785")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2780")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_277D")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_26A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_26A2)
    TurnDirection(0x1C, 0x0, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    PlayEffect(0x7, 0x1, 0x1C, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C38", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2778")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_275F")
    Call(1, 5)
    Jump("loc_2778")

    label("loc_275F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2775")
    Call(1, 4)
    Jump("loc_2778")

    label("loc_2775")

    Call(1, 3)

    label("loc_2778")

    Jump("loc_2780")

    label("loc_277D")

    Call(1, 1)

    label("loc_2780")

    Jump("loc_279B")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_279B")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_279B")

    TalkEnd(0xFF)
    Return()

    label("loc_27A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_292E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2929")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_2926")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_284B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_284B)
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
    Battle("BattleInfo_C7C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2921")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2908")
    Call(1, 5)
    Jump("loc_2921")

    label("loc_2908")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_291E")
    Call(1, 4)
    Jump("loc_2921")

    label("loc_291E")

    Call(1, 3)

    label("loc_2921")

    Jump("loc_2929")

    label("loc_2926")

    Call(1, 1)

    label("loc_2929")

    Jump("loc_2944")

    label("loc_292E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_2944")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2944")

    TalkEnd(0xFF)
    Return()

    # Function_7_25ED end

    def Function_8_2949(): pass

    label("Function_8_2949")

    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x1000)
    OP_78(0xC, 0x12)
    SetChrPos(0x12, 2000, 1000, 14000, 0)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    Return()

    # Function_8_2949 end

    def Function_9_2995(): pass

    label("Function_9_2995")

    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x1000)
    OP_78(0xC, 0x12)
    Return()

    # Function_9_2995 end

    def Function_10_29BD(): pass

    label("Function_10_29BD")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

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
            "St. Ursula Medical College\x01",      # 0
            "Fork (Near Sandbank)\x01",            # 1
            "Cancel\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5C")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2A7C")

    label("loc_2A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7C")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_2A7C")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_10_29BD end

    def Function_11_2A84(): pass

    label("Function_11_2A84")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2BB2")
    Fade(500)
    OP_68(-10500, 780, -11600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -9800, 180, -11100, 89)
    SetChrPos(0x1, -9800, 180, -10100, 89)
    SetChrPos(0x2, -9800, 180, -9100, 89)
    SetChrPos(0x3, -9800, 180, -8100, 89)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x14)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x14, -6300, 0, -21000, 0)
    OP_D5(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2B69():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFD314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B69)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x14, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2BB2")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_11_2A84 end

    def Function_12_2BB6(): pass

    label("Function_12_2BB6")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -9830, 180, -11430, 90)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2BB6 end

    def Function_13_2BDD(): pass

    label("Function_13_2BDD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2C38")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C2D")
    Sound(2502, 255, 100, 0)
    Jump("loc_2C33")

    label("loc_2C2D")

    Sound(2503, 255, 100, 0)

    label("loc_2C33")

    Jump("loc_2C5C")

    label("loc_2C38")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C56")
    Sound(3347, 255, 100, 0)
    Jump("loc_2C5C")

    label("loc_2C56")

    Sound(3348, 255, 100, 0)

    label("loc_2C5C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2BDD end

    def Function_14_2C71(): pass

    label("Function_14_2C71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C82")
    Jump("loc_3489")

    label("loc_2C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D82")

    ChrTalk(
        0xFE,
        (
            "Thank goodness the\x01",
            "medical goods got here\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, a swindler...? To think\x01",
            "there was that horrible a guy in\x01",
            "this time of crisis for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Though I'm relieved\x01",
            "now that he's been\x01",
            "caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DF9")

    label("loc_2D82")


    ChrTalk(
        0xFE,
        (
            "A swindler, huh...? To\x01",
            "think there was such a\x01",
            "horrible guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Though I'm relieved\x01",
            "now that he's been\x01",
            "caught.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF9")

    Jump("loc_2FD3")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE3")

    ChrTalk(
        0xFE,
        (
            "Crap, I couldn't deliver\x01",
            "the medical supplies in\x01",
            "this time of crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, what's done is\x01",
            "done, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't worry about it,\x01",
            "guys. Change your way of\x01",
            "thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F54")

    label("loc_2EE3")


    ChrTalk(
        0xFE,
        (
            "What's done is done, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't worry about it,\x01",
            "guys. Change your way of\x01",
            "thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F54")

    Jump("loc_2FD3")

    label("loc_2F59")


    ChrTalk(
        0xFE,
        (
            "Stealing medical goods in\x01",
            "Crossbell at a time like\x01",
            "this... Totally unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guys, catch that thief\x01",
            "for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD3")

    Jump("loc_3489")

    label("loc_2FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FE6")
    Jump("loc_3489")

    label("loc_2FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FF4")
    Jump("loc_3489")

    label("loc_2FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3002")
    Jump("loc_3489")

    label("loc_3002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3120")

    ChrTalk(
        0xFE,
        (
            "Hmm. I can't believe\x01",
            "there was an error in\x01",
            "the delivery address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's the sender's\x01",
            "fault, I'm partly responsible\x01",
            "for not noticing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And because I have other deliveries\x01",
            "as well, I can't even help out...\x01",
            "Hmm, I did something bad to them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31A7")

    label("loc_3120")


    ChrTalk(
        0xFE,
        (
            "Hmm. I can't believe\x01",
            "there was an error in\x01",
            "the delivery address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I've done a\x01",
            "disservice to those\x01",
            "Capua Express guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A7")

    Jump("loc_3489")

    label("loc_31AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31BA")
    Jump("loc_3489")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31C8")
    Jump("loc_3489")

    label("loc_31C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31D6")
    Jump("loc_3489")

    label("loc_31D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3359")

    ChrTalk(
        0xFE,
        (
            "Our shipping company\x01",
            "mainly handles packages\x01",
            "from out of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In particular, we've forwarded medical supplies and\x01",
            "tools from the Principality of Remiferia in the\x01",
            "north to St. Ursula Hospital many times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By transporting them, it's like I'm indirectly\x01",
            "involved in their cutting edge medical\x01",
            "treatments. I must responsibly transport them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_346D")

    label("loc_3359")


    ChrTalk(
        0xFE,
        (
            "We've forwarded medical supplies and tools from\x01",
            "the Principality of Remiferia in the north to\x01",
            "St. Ursula Hospital many times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By transporting them, it's like I'm indirectly\x01",
            "involved in their cutting edge medical\x01",
            "treatments. I must responsibly transport them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346D")

    Jump("loc_3489")

    label("loc_3472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3480")
    Jump("loc_3489")

    label("loc_3480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3489")

    label("loc_3489")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C71 end

    def Function_15_348D(): pass

    label("Function_15_348D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_349E")
    Jump("loc_3532")

    label("loc_349E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3532")

    ChrTalk(
        0xFE,
        (
            "Hmm. Actually, it's been\x01",
            "a long time since I've\x01",
            "been to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, it's a nice\x01",
            "place that's evenly\x01",
            "matched with Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3532")

    TalkEnd(0xFE)
    Return()

    # Function_15_348D end

    def Function_16_3536(): pass

    label("Function_16_3536")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35D6")

    ChrTalk(
        0xFE,
        (
            "The recent attack the\x01",
            "other day was\x01",
            "terrifying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seemed like I was having\x01",
            "a nightmare. I hope nothing\x01",
            "like that happens again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3689")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3689")

    ChrTalk(
        0xFE,
        (
            "The scene of the elegant Arseille when it\x01",
            "magnificently landed at the airport... It\x01",
            "was a sight to see, I tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. It'll make a nice\x01",
            "tale of my travels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3689")

    TalkEnd(0xFE)
    Return()

    # Function_16_3536 end

    def Function_17_368D(): pass

    label("Function_17_368D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "They say there's going to\x01",
            "be a Mishy event at the\x01",
            "Waterfront Area today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grampa, quick, let's go\x01",
            "see it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_368D end

    def Function_18_3707(): pass

    label("Function_18_3707")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "By proposing independence,\x01",
            "it appears Crossbell is\x01",
            "pressuring the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was shocked that Dieter proposed\x01",
            "it at the trade conference. Isn't\x01",
            "that a bit hasty?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3707 end

    def Function_19_37BF(): pass

    label("Function_19_37BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3898")

    ChrTalk(
        0xFE,
        (
            "Tomorrow's trade conference\x01",
            "is being held in Crossbell,\x01",
            "the crossroads of finance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will greatly influence\x01",
            "economy of neighboring\x01",
            "countries as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's worth checking\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3937")

    label("loc_3898")


    ChrTalk(
        0xFE,
        (
            "Tomorrow's trade conference will greatly\x01",
            "influence greatly influence the economies\x01",
            "of the neighboring countries as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's worth checking\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3937")

    TalkEnd(0xFE)
    Return()

    # Function_19_37BF end

    def Function_20_393B(): pass

    label("Function_20_393B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I-I told you I'm really\x01",
            "sorry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll buy you whatever you\x01",
            "want at the department\x01",
            "store, so forgive meee!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_393B end

    def Function_21_39B4(): pass

    label("Function_21_39B4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey, is it true that\x01",
            "Michelam is closed like that\x01",
            "staff member just said!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Check these things out\x01",
            "beforehand, you damn\x01",
            "idiooot!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_39B4 end

    def Function_22_3A45(): pass

    label("Function_22_3A45")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "H-Hmm... I've just\x01",
            "gotten back from a trip,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My belly hurts for some\x01",
            "reason. Should I go to\x01",
            "the hospital...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3A45 end

    def Function_23_3ACD(): pass

    label("Function_23_3ACD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "At present, police are\x01",
            "searching the airport\x01",
            "landing field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We ask you to refrain\x01",
            "from entering the search\x01",
            "zone.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3ACD end

    def Function_24_3B4F(): pass

    label("Function_24_3B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BC0")

    ChrTalk(
        0xFE,
        (
            "You're the SSS, huh?\x01",
            "Thank you for your hard\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to\x01",
            "pass through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC8")

    label("loc_3BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C39")

    ChrTalk(
        0xFE,
        (
            "Signs of terrorists\x01",
            "aiming at Orchis Tower,\x01",
            "they say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the feeling\x01",
            "this'll be one long day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC8")

    label("loc_3C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CFE")

    ChrTalk(
        0xFE,
        (
            "I'm really relieved that\x01",
            "the unveiling ceremony\x01",
            "ended without trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still the first day of the\x01",
            "trade conference, but now we have\x01",
            "crossed an important turning point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC8")

    label("loc_3CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DC8")

    ChrTalk(
        0xFE,
        (
            "During the trade conference, those\x01",
            "entering and leaving airport will be\x01",
            "subject to especially strict checks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's all do our best until\x01",
            "the final day without\x01",
            "letting our guard down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC8")

    TalkEnd(0xFE)
    Return()

    # Function_24_3B4F end

    def Function_25_3DCC(): pass

    label("Function_25_3DCC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Airport is this\x01",
            "way. ...We don't have any\x01",
            "particular business there.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    EventEnd(0x4)
    Return()

    # Function_25_3DCC end

    def Function_26_3E40(): pass

    label("Function_26_3E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F9")
    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(14210, 2050, -69500, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(38330, 0)
    SetChrPos(0x101, 1500, 0, -73720, 0)
    SetChrPos(0x107, 2470, 0, -74900, 0)
    SetChrPos(0x105, 870, 0, -75890, 0)
    SetChrSubChip(0x107, 0x5)
    FadeToBright(1000, 0)
    OP_68(-6520, 2050, -69500, 6000)
    OP_6F(0x79)
    Fade(500)
    OP_68(60, 5950, -75080, 0)
    OP_68(60, 2050, -75080, 4000)
    MoveCamera(29, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19360, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00010F#12PThis is the Crossbell City\x01",
            "Barrier... Looking at it from up\x01",
            "close like this, it's incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PFrom the Merkabah, it looks like\x01",
            "it envelops the whole of Crossbell\x01",
            "City like a dome.\x02\x03",
            "#10408FRations trucks, emergency\x01",
            "vehicles, the State Guard and Red\x01",
            "Constellation...\x02\x03",
            "#10401FIt appears the President has given\x01",
            "only those groups permission to\x01",
            "come and go as they please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#3C#12PFor those without permission,\x01",
            "it's impossible to pass\x01",
            "through by any means.\x02\x03",
            "#01201FDon't even think about trying\x01",
            "to get inside until we find a\x01",
            "way to remove the barrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PUnderstood.\x02\x03",
            "#00013F(KeA, wait for me. I'll\x01",
            "come get you... For\x01",
            "sure!)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19610, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1AE, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    SetChrPos(0x0, 990, 0, -74180, 180)
    Sleep(500)
    EventEnd(0x5)

    label("loc_41F9")

    Return()

    # Function_26_3E40 end

    def Function_27_41FA(): pass

    label("Function_27_41FA")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422C")
    SetScenarioFlags(0x31, 2)

    label("loc_422C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_426C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4261")
    Sound(2499, 255, 100, 0)
    Jump("loc_4267")

    label("loc_4261")

    Sound(3537, 255, 100, 0)

    label("loc_4267")

    Jump("loc_4272")

    label("loc_426C")

    Sound(3344, 255, 100, 0)

    label("loc_4272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_42E7")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42C7"),
        (SWITCH_DEFAULT, "loc_42D8"),
    )


    label("loc_42C7")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E2")

    label("loc_42D8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42E2")

    Jump("loc_4524")

    label("loc_42E7")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4319")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4319")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_434D"),
        (1, "loc_4451"),
        (2, "loc_44E2"),
        (SWITCH_DEFAULT, "loc_451A"),
    )


    label("loc_434D")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_437E")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_438E")

    label("loc_437E")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_438E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43E4")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4407")
    Sound(461, 0, 100, 0)

    label("loc_4407")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4427")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4437")

    label("loc_4427")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4437")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_4272")

    label("loc_4451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_44C3")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4486")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_449E")

    label("loc_4486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4499")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_449E")

    label("loc_4499")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_449E")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44DD")

    label("loc_44C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_44D3")
    OP_AF(0xFB)
    Jump("loc_44DD")

    label("loc_44D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44DD")

    Jump("loc_4524")

    label("loc_44E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4515")

    label("loc_44FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_450B")
    OP_AF(0xFB)
    Jump("loc_4515")

    label("loc_450B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4515")

    Jump("loc_4524")

    label("loc_451A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4524")

    Jump("loc_4272")

    label("loc_4529")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_41FA end

    def Function_28_4537(): pass

    label("Function_28_4537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4587")
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

    label("loc_4587")

    Call(0, 10)
    Return()

    # Function_28_4537 end

    def Function_29_458B(): pass

    label("Function_29_458B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x1F, 0x7)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    BeginChrThread(0x1F, 0, 0, 0)
    SetChrChipByIndex(0x20, 0x7)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    BeginChrThread(0x20, 0, 0, 0)
    SetChrChipByIndex(0x21, 0x7)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    BeginChrThread(0x21, 0, 0, 0)
    SetChrChipByIndex(0x22, 0x7)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrChipByIndex(0x23, 0x7)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    BeginChrThread(0x23, 0, 0, 0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1D, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1F, -1400, 0, -13600, 90)
    SetChrPos(0x20, 250, 0, -17400, 45)
    SetChrPos(0x21, 3750, 0, -20300, 45)
    SetChrPos(0x22, 5600, 0, -9350, 225)
    SetChrPos(0x23, 9550, 0, -12400, 180)
    SetChrPos(0x24, -5650, 0, -11000, 0)
    SetChrPos(0x25, 3750, 0, -24250, 270)
    OP_68(2500, 600, -9450, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25500, 0)
    OP_68(17000, 1600, -17500, 10000)
    MoveCamera(45, 20, 0, 10000)
    SetCameraDistance(23500, 10000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_458B end

    def Function_30_47DF(): pass

    label("Function_30_47DF")

    EventBegin(0x0)
    Fade(500)
    OP_68(15700, 1000, -17600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 15700, 0, -17600, 90)
    SetChrPos(0x102, 14300, 0, -18200, 90)
    SetChrPos(0x104, 14300, 0, -17000, 90)
    SetChrPos(0x109, 13200, 0, -17000, 90)
    SetChrPos(0x105, 13200, 0, -18200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F(There's still time\x01",
            "until evening...)\x02\x03",
            "#00001F(It's a little early,\x01",
            "but should we enter and\x01",
            "wait on the terrace?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Have Other Things to Do]\x01",         # 0
            "[Enter and Wait on the Terrace]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_496F"),
        (1, "loc_4991"),
        (SWITCH_DEFAULT, "loc_4AFC"),
    )


    label("loc_496F")

    SetChrPos(0x0, 11250, 0, -17610, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Jump("loc_4AFC")

    label("loc_4991")

    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAll right... It's a\x01",
            "little early, but shall\x01",
            "we wait on the terrace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FLet's prepare for the\x01",
            "worst...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_4A40():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A40)
    Sleep(50)

    def lambda_4A5D():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4A5D)
    Sleep(50)

    def lambda_4A7A():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4A7A)
    Sleep(50)

    def lambda_4A97():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4A97)
    Sleep(50)

    def lambda_4AB4():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4AB4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3510", 0, 0, 0)
    IdleLoop()
    Jump("loc_4AFC")

    label("loc_4AFC")

    Return()

    # Function_30_47DF end

    def Function_31_4AFD(): pass

    label("Function_31_4AFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 3000, -64500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    OP_68(0, 4000, -64500, 8000)
    MoveCamera(40, 27, 0, 8000)
    SetCameraDistance(30500, 8000)
    OP_71(0xB, 0x208, 0x2BC, 0x0, 0x0)
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
    SetScenarioFlags(0x23, 2)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4AFD end

    def Function_32_4BFD(): pass

    label("Function_32_4BFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C49")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_4C49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5D")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_4C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C71")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_4C71")

    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("chr/ch41450.itc", 0x1F)
    LoadChrToIndex("chr/ch41451.itc", 0x20)
    LoadChrToIndex("chr/ch41452.itc", 0x21)
    LoadChrToIndex("apl/ch51617.itc", 0x22)
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev17057.eff")
    LoadEffect(0x5, "battle/sc008100.eff")
    LoadEffect(0x6, "event/ev17059.eff")
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(497)
    SoundLoad(825)
    SoundLoad(943)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(577)
    SetChrPos(0x0, 8000, 0, 17000, 0)
    SetChrPos(0x1, 8000, 0, 17000, 0)
    SetChrPos(0x2, 8000, 0, 17000, 0)
    SetChrPos(0x3, 8000, 0, 17000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 300, 0, -76000, 180)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 2900, 0, -76000, 180)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 3100, 0, -72400, 90)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 0, -67000, 0)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2600, 0, -65400, 180)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 5300, 0, -65400, 0)
    ClearChrFlags(0x27, 0x80)
    OP_78(0xF, 0x27)
    OP_49()
    SetChrPos(0x27, 0, 19500, -19000, 90)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x16, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 20000, -19000, 90)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x65, 0xA0, 0x0, 0x20)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x10, 0x29)
    OP_49()
    SetChrPos(0x29, 0, 0, -130000, 0)
    OP_D5(0x29, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x14, 0x24)
    OP_49()
    SetChrPos(0x24, -3700, 0, -71500, 180)
    OP_D5(0x24, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x0)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    SetMapObjFrame(0x14, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x14, "mark01", 0x1, 0x1)
    ClearChrFlags(0x25, 0x80)
    OP_78(0x15, 0x25)
    OP_49()
    SetChrPos(0x25, 5300, 0, -71500, 180)
    OP_D5(0x25, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_70(0x15, 0x0)
    SetMapObjFrame(0x15, "light", 0x0, 0x1)
    SetMapObjFrame(0x15, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x15, "mark01", 0x1, 0x1)
    ClearChrFlags(0x26, 0x80)
    OP_78(0x1E, 0x26)
    OP_49()
    SetChrPos(0x26, 5300, 0, -62500, 270)
    OP_D5(0x26, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x1000)
    OP_74(0x1E, 0x1E)
    OP_70(0x1E, 0x0)
    SetMapObjFrame(0x1E, "light", 0x0, 0x1)
    SetMapObjFrame(0x1E, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x1E, "mark01", 0x1, 0x1)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0xC, 0x4)
    OP_68(0, 3000, -25000, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    OP_68(0, 3000, -78000, 10000)
    SetCameraDistance(23000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0x2A, 1, 0, 44)
    Fade(500)
    OP_68(2000, 1000, -76000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    Sleep(1000)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_51D5():

        label("loc_51D5")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_51D5")

    QueueWorkItem2(0x15, 2, lambda_51D5)

    def lambda_51E7():

        label("loc_51E7")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_51E7")

    QueueWorkItem2(0x16, 2, lambda_51E7)

    def lambda_51F9():

        label("loc_51F9")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_51F9")

    QueueWorkItem2(0x17, 2, lambda_51F9)

    def lambda_520B():

        label("loc_520B")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_520B")

    QueueWorkItem2(0x18, 2, lambda_520B)

    def lambda_521D():

        label("loc_521D")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_521D")

    QueueWorkItem2(0x19, 2, lambda_521D)

    def lambda_522F():

        label("loc_522F")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_522F")

    QueueWorkItem2(0x1A, 2, lambda_522F)
    MoveCamera(33, 27, 0, 5000)
    SetCameraDistance(30500, 5000)
    BlurSwitch(0x1388, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_5261():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5261)
    Sleep(1500)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x29, 1)
    Fade(500)
    OP_68(0, 6000, -20000, 0)
    MoveCamera(57, 47, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    CancelBlur(0)
    SetMapObjFlags(0x1, 0x1000)
    BeginChrThread(0x27, 0, 0, 38)
    BeginChrThread(0x27, 3, 0, 36)
    BeginChrThread(0x29, 3, 0, 37)
    OP_68(0, 4000, -20000, 4000)
    MoveCamera(67, 47, 0, 4000)
    SetCameraDistance(50000, 4000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    OP_6F(0x79)
    WaitChrThread(0x27, 3)
    EndChrThread(0x27, 0x0)
    SetMapObjFlags(0x1E, 0x4)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    StopSound(825, 2000, 50)
    Fade(500)
    OP_68(0, 2000, -61000, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 2000, -56000, 3000)
    MoveCamera(33, 23, 0, 3000)
    SetCameraDistance(20000, 3000)
    SetChrPos(0x24, -4200, 0, -71500, 0)
    OP_D5(0x24, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x25, 4600, 0, -74500, 0)
    OP_D5(0x25, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0x24, 3, 0, 39)
    BeginChrThread(0x25, 3, 0, 40)
    BeginChrThread(0x15, 3, 0, 41)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 42)
    Sleep(300)
    BeginChrThread(0x17, 3, 0, 43)
    StopSound(497, 2000, 70)
    OP_6F(0x79)
    Sleep(2000)
    OP_68(0, 4200, -35000, 1500)
    MoveCamera(27, 21, 0, 1500)
    SetCameraDistance(25000, 1500)
    OP_6F(0x79)
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 0, 4500, -35500, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x27, 0, 0, 34)
    Sleep(3000)
    BeginChrThread(0x2A, 1, 0, 46)
    Fade(500)
    OP_68(0, 1100, -14000, 0)
    MoveCamera(43, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(23500, 2500)
    EndChrThread(0x27, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    OP_0D()
    Sound(943, 2, 100, 0)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x137, 0x154, 0x0, 0x0)
    OP_79(0xF)
    OP_24(0x3AF)
    Sound(143, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 1100, -7500, 3000)
    MoveCamera(56, 13, 0, 3000)
    SetCameraDistance(21500, 3000)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x106, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x2A, 1, 0, 45)
    StopSound(865, 1900, 25)
    StopSound(577, 1900, 20)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x1F1)
    OP_24(0x339)
    OP_24(0x3AF)
    OP_24(0x35D)
    OP_24(0x361)
    OP_24(0x241)
    SetScenarioFlags(0x22, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4BFD end

    def Function_33_564A(): pass

    label("Function_33_564A")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    Sleep(1)
    SetChrPos(0xFE, 0, 1300, -15500, 0)

    def lambda_5677():
        OP_95(0xFE, 0, 0, -8800, 4000, 0x2)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5677)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Sleep(1)

    def lambda_56A2():
        OP_97(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56A2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_564A end

    def Function_34_56BC(): pass

    label("Function_34_56BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5978")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3000, 3500, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2000, 4200, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1100, 4800, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1500, 5100, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2700, 3700, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -900, 5000, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2800, 2900, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -1400, 4500, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 300, 4400, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2000, 4900, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3900, 3300, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -500, 3000, -35800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_34_56BC")

    label("loc_5978")

    Return()

    # Function_34_56BC end

    def Function_35_5979(): pass

    label("Function_35_5979")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_599D")
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_35_5979")

    label("loc_599D")

    Return()

    # Function_35_5979 end

    def Function_36_599E(): pass

    label("Function_36_599E")


    def lambda_59A3():
        OP_96(0xFE, 0x0, 0x14B4, 0xFFFFB5C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59A3)
    OP_D5(0xFE, 0x0, 0x2BF20, 0x0, 0x12C0)
    Return()

    # Function_36_599E end

    def Function_37_59CC(): pass

    label("Function_37_59CC")

    SetChrPos(0x29, 0, 0, -19000, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x12C0)
    Return()

    # Function_37_59CC end

    def Function_38_5A04(): pass

    label("Function_38_5A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A28")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_38_5A04")

    label("loc_5A28")

    Return()

    # Function_38_5A04 end

    def Function_39_5A29(): pass

    label("Function_39_5A29")

    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    OP_71(0x14, 0xB5, 0xF0, 0x0, 0x20)

    def lambda_5A46():
        OP_96(0xFE, 0xFFFFEF98, 0x0, 0xFFFF2540, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A46)
    WaitChrThread(0xFE, 1)
    Sound(487, 0, 100, 0)
    OP_71(0x14, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x14)
    OP_71(0x14, 0xF1, 0xF3, 0x0, 0x0)
    OP_79(0x14)
    Sound(865, 2, 80, 0)
    Sound(577, 2, 60, 0)
    Sound(861, 2, 60, 0)
    BeginChrThread(0xFE, 0, 0, 35)
    OP_87(0x5, 0x0, 0x14, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_39_5A29 end

    def Function_40_5ACD(): pass

    label("Function_40_5ACD")

    OP_71(0x15, 0xB5, 0xF0, 0x0, 0x20)

    def lambda_5ADE():
        OP_96(0xFE, 0x11F8, 0x0, 0xFFFF2158, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5ADE)
    WaitChrThread(0xFE, 1)
    OP_71(0x15, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x15)
    OP_71(0x15, 0x12C, 0x12A, 0x0, 0x0)
    OP_79(0x15)
    OP_87(0x5, 0x1, 0x15, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_40_5ACD end

    def Function_41_5B47(): pass

    label("Function_41_5B47")

    SetChrPos(0xFE, -800, 0, -70600, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5B65():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFF26D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B65)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_5B90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D20")
    SetChrSubChip(0xFE, 0x2)

    def lambda_5BA4():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BA4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_5B90")

    label("loc_5D20")

    Return()

    # Function_41_5B47 end

    def Function_42_5D21(): pass

    label("Function_42_5D21")

    SetChrPos(0xFE, 1700, 0, -69800, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5D3F():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFF29F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D3F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_5D6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EFA")
    SetChrSubChip(0xFE, 0x2)

    def lambda_5D7E():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D7E)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_5D6A")

    label("loc_5EFA")

    Return()

    # Function_42_5D21 end

    def Function_43_5EFB(): pass

    label("Function_43_5EFB")

    SetChrPos(0xFE, 200, 0, -71300, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5F19():
        OP_96(0xFE, 0xC8, 0x0, 0xFFFF2414, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F19)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)

    label("loc_5F44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60D4")
    SetChrSubChip(0xFE, 0x2)

    def lambda_5F58():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F58)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("loc_5F44")

    label("loc_60D4")

    Return()

    # Function_43_5EFB end

    def Function_44_60D5(): pass

    label("Function_44_60D5")

    Sound(497, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x339, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x339, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x339, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    OP_25(0x339, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    Sleep(200)
    OP_25(0x1F1, 0x4B)
    Return()

    # Function_44_60D5 end

    def Function_45_614F(): pass

    label("Function_45_614F")

    OP_25(0x35D, 0x14)
    Sleep(300)
    OP_25(0x35D, 0xF)
    Sleep(300)
    OP_25(0x35D, 0xA)
    Sleep(300)
    OP_25(0x35D, 0x5)
    Sleep(300)
    OP_25(0x35D, 0x0)
    Return()

    # Function_45_614F end

    def Function_46_6170(): pass

    label("Function_46_6170")

    OP_25(0x361, 0x46)
    OP_25(0x241, 0x2D)
    OP_25(0x35D, 0x2D)
    Sleep(250)
    OP_25(0x361, 0x3C)
    OP_25(0x241, 0x28)
    OP_25(0x35D, 0x28)
    Sleep(250)
    OP_25(0x361, 0x32)
    OP_25(0x241, 0x23)
    OP_25(0x35D, 0x23)
    Sleep(250)
    OP_25(0x361, 0x28)
    OP_25(0x241, 0x1E)
    OP_25(0x35D, 0x1E)
    Sleep(250)
    OP_25(0x361, 0x1E)
    OP_25(0x241, 0x19)
    OP_25(0x35D, 0x19)
    Return()

    # Function_46_6170 end

    def Function_47_61B9(): pass

    label("Function_47_61B9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North - Crossbell City\x01",
            "East - Crossbell Airport\x01",
            "South - St. Ursula Medical College  153 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_61B9 end

    SaveToFile()

Try(main)
