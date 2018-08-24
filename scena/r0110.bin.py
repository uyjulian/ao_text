from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0110.bin",                # FileName
        "r0110",                    # MapName
        "r0110",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0110", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x0F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 3, 0, 4],
    )

    BuildStringList((
        "r0110",                  # 0
        "Kaguya, the Dragon Queen",# 1
        "Chiruru",                # 2
        "マグマドローメ",         # 3
        "マグマドローメ",         # 4
        "ブレードファング",       # 5
        "ブレードファング",       # 6
        "Cryptid",                # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "br0100",                 # 12
        "br0100",                 # 13
        "br0100",                 # 14
        "br0100",                 # 15
        "br0100",                 # 16
        "br0100",                 # 17
        "To Crossbell City/Tangram Gate",# 18
        "To Armorica Village",    # 19
    ))

    ATBonus("ATBonus_588", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_5A8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4740", 2,   11,  0,   4,   0,   2,   7)
    Sepith("Sepith_4748", 3,   0,   10,  2,   4,   3,   2)
    Sepith("Sepith_4728", 7,   5,   0,   0,   4,   5,   4)
    Sepith("Sepith_4730", 5,   0,   9,   0,   3,   2,   5)
    Sepith("Sepith_4738", 0,   6,   0,   9,   4,   6,   0)
    Sepith("Sepith_4758", 21,  8,   16,  3,   0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_5E8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_64C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_650", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_654", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_65C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_660", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_664", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_66C", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_678", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_67C", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_680", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_684", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_924", 0x0000, 60, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_4740", 30, 30, 20, 20,
        (
            ("ms64500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms64500.dat", "ms64500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
        )
    )

    BattleInfo(
        "BattleInfo_888", 0x0000, 60, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_4748", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7C0", 0x0000, 60, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_4728", 30, 30, 20, 20,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms62200.dat", "ms61800.dat", "ms62200.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
        )
    )

    BattleInfo(
        "BattleInfo_724", 0x0000, 60, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_4730", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms62600.dat", "ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_688", 0x0000, 60, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_4738", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9EC", 0x0000, 82, 6, 60, 8, 1, 40, 0, "br0100", "Sepith_4758", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7450", "ed7453", "ATBonus_588"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B10", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66801.dat", "ms66801.dat", "ms66801.dat", "ms66801.dat", "ms66801.dat", "ms66801.dat", 0, 0, "MonsterBattlePostion_5C8", "MonsterBattlePostion_648", "ed7451", "ed7453", "ATBonus_5A8"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_A88", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69800.dat", "ms69800.dat", "ms69800.dat", "ms69800.dat", "ms69800.dat", "ms69800.dat", "ms69800.dat", "ms69800.dat", "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7453", "ed7453", "ATBonus_588"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_ACC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", "MonsterBattlePostion_5E8", "MonsterBattlePostion_648", "ed7453", "ed7453", "ATBonus_588"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B54", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_668", "MonsterBattlePostion_668", "ed7454", "ed7453", "ATBonus_5A8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45800.itc",                   # 00
        "chr/ch20500.itc",                   # 01
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
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch64550.itc",               # 18
        "monster/ch64551.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
        "monster/ch66850.itc",               # 1C
        "monster/ch66851.itc",               # 1D
    ))

    DeclNpc(4294953366, 5000,    86989,   80,   261,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294938946, 5199,    70849,   45,   389,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294926936, 3019,    57180,   270,  484,  0x0, 0,   22,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294877606, 4294966296, 140800,  270,  484,  0x0, 0,   22,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294926936, 3019,    57180,   270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294877606, 4294966296, 140800,  270,  484,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294951266, 21390,   1050,    0x1010000,    "BattleInfo_924", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294966646, 34640,   2009,    0x1010000,    "BattleInfo_888", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294923906, 58440,   3000,    0x1010000,    "BattleInfo_7C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294934196, 91170,   3000,    0x1010000,    "BattleInfo_724", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294916346, 128690,  1800,    0x1010000,    "BattleInfo_688", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294904556, 137000,  4294966886, 0x1010000,    "BattleInfo_924", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294899866, 109860,  40,      0x1010000,    "BattleInfo_888", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294876316, 120410,  4294966296, 0x1010000,    "BattleInfo_7C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294870066, 131570,  4294966296, 0x1010000,    "BattleInfo_724", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294954206, 34470,   2009,    0x1010000,    "BattleInfo_9EC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294909606, 66190,   3000,    0x1010000,    "BattleInfo_9EC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294909076, 121570,  860,     0x1010000,    "BattleInfo_9EC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294926776, 57430,   3020,    0x18500E1,    "BattleInfo_B10", 0,   28,  0xFFFF, 12, 13)

    DeclEvent(0x0040, 0, 16,  -40.52000045776367,    57.43000030517578,     2.0199999809265137,    16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   5.065000057220459,     -7.178750038146973,    -0.5049999952316284,   1.0])
    DeclEvent(0x0040, 0, 17,  -86.58999633789062,    135.14999389648438,    -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   10.823749542236328,    -16.893749237060547,   0.5,                   1.0])

    DeclActor(4294870496, 4294966296, 121110,  1200,    4294870496, 0,       121110,  0x007C, 0,  5,  0x0000)
    DeclActor(4294897726, 0,       107270,  1200,    4294897726, 1000,    107270,  0x007C, 0,  6,  0x0000)
    DeclActor(4294926936, 3020,    57180,   1200,    4294926936, 3020,    57180,   0x007C, 0,  7,  0x0000)
    DeclActor(4294877606, 4294966296, 140800,  1200,    4294877606, 4294966296, 140800,  0x007C, 0,  8,  0x0000)
    DeclActor(4294953366, 5000,    87310,   1200,    4294962116, 1000,    91160,   0x007C, 0,  15, 0x0000)
    DeclActor(4294950446, 5000,    89750,   1000,    4294950446, 6500,    89750,   0x007C, 0,  14, 0x0000)
    DeclActor(4294951446, 5000,    88750,   1000,    4294951446, 6500,    88750,   0x007C, 0,  14, 0x0000)
    DeclActor(4294936856, 5000,    73410,   1200,    4294936856, 6500,    73410,   0x007C, 0,  21, 0x0000)

    PlaceName(-1.3899999856948853, 0.0, -33.0, 0x0000, 0x0000, "To Crossbell City/Tangram Gate")
    PlaceName(-88.0, 0.0, 178.0, 0x0000, 0x0000, "To Armorica Village")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 12
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 13

    ScpFunction((
        "Function_0_C98",          # 00, 0
        "Function_1_D50",          # 01, 1
        "Function_2_D6D",          # 02, 2
        "Function_3_D8A",          # 03, 3
        "Function_4_E6D",          # 04, 4
        "Function_5_1ACB",         # 05, 5
        "Function_6_1C1C",         # 06, 6
        "Function_7_1D6D",         # 07, 7
        "Function_8_20C9",         # 08, 8
        "Function_9_2425",         # 09, 9
        "Function_10_2443",        # 0A, 10
        "Function_11_2447",        # 0B, 11
        "Function_12_35EB",        # 0C, 12
        "Function_13_39C1",        # 0D, 13
        "Function_14_3ABB",        # 0E, 14
        "Function_15_3AD9",        # 0F, 15
        "Function_16_3D86",        # 10, 16
        "Function_17_41E0",        # 11, 17
        "Function_18_425C",        # 12, 18
        "Function_19_459D",        # 13, 19
        "Function_20_462B",        # 14, 20
        "Function_21_466C",        # 15, 21
    ))


    def Function_0_C98(): pass

    label("Function_0_C98")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_CD8"),
        (1, "loc_CE4"),
        (2, "loc_CF0"),
        (3, "loc_CFC"),
        (4, "loc_D08"),
        (5, "loc_D14"),
        (6, "loc_D20"),
        (SWITCH_DEFAULT, "loc_D2C"),
    )


    label("loc_CD8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_CE4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_CF0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_CFC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D08")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D14")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D2C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D38")

    label("loc_D4F")

    Return()

    # Function_0_C98 end

    def Function_1_D50(): pass

    label("Function_1_D50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D6C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_D50")

    label("loc_D6C")

    Return()

    # Function_1_D50 end

    def Function_2_D6D(): pass

    label("Function_2_D6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D89")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_D6D")

    label("loc_D89")

    Return()

    # Function_2_D6D end

    def Function_3_D8A(): pass

    label("Function_3_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_DA4")
    SetChrPos(0x8, -13710, 5000, 85050, 80)

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DB7")
    SetChrFlags(0x8, 0x80)
    Jump("loc_E69")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_DCE")
    SetChrFlags(0x8, 0x80)

    label("loc_DCE")

    Jump("loc_E69")

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DE1")
    Jump("loc_E69")

    label("loc_DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E02")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DFD")
    SetChrFlags(0xFE, 0x10)

    label("loc_DFD")

    Jump("loc_E69")

    label("loc_E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E10")
    Jump("loc_E69")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E1E")
    Jump("loc_E69")

    label("loc_E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E2C")
    Jump("loc_E69")

    label("loc_E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E3F")
    SetChrFlags(0x8, 0x10)
    Jump("loc_E69")

    label("loc_E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E4D")
    Jump("loc_E69")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E5B")
    Jump("loc_E69")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E69")
    SetChrFlags(0x8, 0x80)

    label("loc_E69")

    Call(0, 9)
    Return()

    # Function_3_D8A end

    def Function_4_E6D(): pass

    label("Function_4_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E7F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E7F")

    SoundDistance(0x7B, 0xFFFFCD1A, 0x1388, 0x10946, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E3(0xFFFFDE0E, 0x1388, 0x14712)
    OP_E3(0xFFFFEBBA, 0x1388, 0x25B48)
    OP_E3(0xFFFE3EDC, 0x1388, 0x28EC4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE9")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_F52")

    label("loc_EE9")

    OP_78(0x2, 0xE)
    ClearMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x1)
    SetChrPos(0xE, -86590, -1000, 135150, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -86590, -2000, 135150, 3000, 3000, 90000)

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F79")
    ClearChrFlags(0x1B, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x1B, 0x8000)

    label("loc_F79")

    Jump("loc_F88")

    label("loc_F7E")

    SetChrFlags(0x1B, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_F88")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A4")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_17A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18A4")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
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
    Jump("loc_196A")

    label("loc_18A4")

    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
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
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    SetMapObjFlags(0x26, 0x4)

    label("loc_196A")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -5180, 1000, 91160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19CE")
    OP_66(0x4, 0x1)

    label("loc_19CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E1")
    OP_70(0x0, 0x0)
    Jump("loc_19E5")

    label("loc_19E1")

    OP_70(0x0, 0x1E)

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")
    OP_70(0x1, 0x0)
    Jump("loc_19FC")

    label("loc_19F8")

    OP_70(0x1, 0x1E)

    label("loc_19FC")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A5D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -40360, 3020, 57180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1A5D")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AA9")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -89690, -1000, 140800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1AA9")

    OP_1C(0x0, 0x3, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x4, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_4_E6D end

    def Function_5_1ACB(): pass

    label("Function_5_1ACB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC7")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1B50")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EA, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1BC2")

    label("loc_1B50")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
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

    label("loc_1BC2")

    Jump("loc_1C10")

    label("loc_1BC7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_1C10")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1ACB end

    def Function_6_1C1C(): pass

    label("Function_6_1C1C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D18")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x99, 1)"), scpexpr(EXPR_END)), "loc_1CA1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x99),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EA, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1D13")

    label("loc_1CA1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x99),
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D13")

    Jump("loc_1D61")

    label("loc_1D18")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_1D61")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C1C end

    def Function_7_1D6D(): pass

    label("Function_7_1D6D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F24")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1F05")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F00")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1EFD")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E22)
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
    Battle("BattleInfo_A88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EDF")
    Call(1, 5)
    Jump("loc_1EF8")

    label("loc_1EDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EF5")
    Call(1, 4)
    Jump("loc_1EF8")

    label("loc_1EF5")

    Call(1, 3)

    label("loc_1EF8")

    Jump("loc_1F00")

    label("loc_1EFD")

    Call(1, 1)

    label("loc_1F00")

    Jump("loc_1F1B")

    label("loc_1F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1F1B")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1F1B")

    TalkEnd(0xFF)
    Return()

    label("loc_1F24")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_20AE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A9")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_20A6")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1FCB)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_ACC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A1")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2088")
    Call(1, 5)
    Jump("loc_20A1")

    label("loc_2088")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_209E")
    Call(1, 4)
    Jump("loc_20A1")

    label("loc_209E")

    Call(1, 3)

    label("loc_20A1")

    Jump("loc_20A9")

    label("loc_20A6")

    Call(1, 1)

    label("loc_20A9")

    Jump("loc_20C4")

    label("loc_20AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_20C4")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_20C4")

    TalkEnd(0xFF)
    Return()

    # Function_7_1D6D end

    def Function_8_20C9(): pass

    label("Function_8_20C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2280")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2261")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225C")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2259")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_217E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_217E)
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
    Battle("BattleInfo_A88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2254")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_223B")
    Call(1, 5)
    Jump("loc_2254")

    label("loc_223B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2251")
    Call(1, 4)
    Jump("loc_2254")

    label("loc_2251")

    Call(1, 3)

    label("loc_2254")

    Jump("loc_225C")

    label("loc_2259")

    Call(1, 1)

    label("loc_225C")

    Jump("loc_2277")

    label("loc_2261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2277")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2277")

    TalkEnd(0xFF)
    Return()

    label("loc_2280")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_240A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2405")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2402")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2327():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2327)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_ACC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23FD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23E4")
    Call(1, 5)
    Jump("loc_23FD")

    label("loc_23E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23FA")
    Call(1, 4)
    Jump("loc_23FD")

    label("loc_23FA")

    Call(1, 3)

    label("loc_23FD")

    Jump("loc_2405")

    label("loc_2402")

    Call(1, 1)

    label("loc_2405")

    Jump("loc_2420")

    label("loc_240A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2420")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2420")

    TalkEnd(0xFF)
    Return()

    # Function_8_20C9 end

    def Function_9_2425(): pass

    label("Function_9_2425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2442")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_2442")

    Return()

    # Function_9_2425 end

    def Function_10_2443(): pass

    label("Function_10_2443")

    Call(1, 6)
    Return()

    # Function_10_2443 end

    def Function_11_2447(): pass

    label("Function_11_2447")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_245F")
    SetScenarioFlags(0x0, 2)

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_246B")
    SetScenarioFlags(0x0, 2)

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_283B")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh? And who might you\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, I'm Lloyd, from\x01",
            "the Fisherman's Guild.\x02\x03",
            "You're from the Imperial\x01",
            "Fishing Club, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, you've finally\x01",
            "come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, I am the only woman\x01",
            "of the Elite Four... My name\x01",
            "is Kaguya, the Dragon Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By my hand, the Fisherman's Guild shall be beaten\x01",
            "to within an inch of its life... It will be as\x01",
            "decisive a win as possible, an instant kill...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh ho ho, oh ho ho ho,\x01",
            "ooohhohoo―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...*cough, cough*.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "...I-In any case! It is in your best\x01",
            "interest not to harbor any fantasies\x01",
            "of winning against someone like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, before that, I\x01",
            "must ascertain if you're\x01",
            "qualified, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to challenge me,\x01",
            "show me that you've caught a\x01",
            "big one of 130 rege or more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "After that, we'll talk.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_283B")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_283B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2845")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                                 # 0
            "Challenge Her to an Angler Duel\x01",      # 1
            "Cancel\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_28A8")

    label("loc_289E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28D1")
    TurnDirection(0x8, 0x0, 0)

    label("loc_28D1")

    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A71")

    ChrTalk(
        0x8,
        (
            "Haha, then I'll check\x01",
            "your fishing notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Indeed, it seems you've\x01",
            "really caught a big one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, about the Angler\x01",
            "Duel against me that\x01",
            "you've longed for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is simple yet\x01",
            "profound. We will do a\x01",
            ""3-Round Angler Duel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have 3 chances...\x01\x07\x02",
            "Whoever's fish have the\x01",
            "highest total length, wins.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 2)
    Jump("loc_2AFA")

    label("loc_2A71")


    ChrTalk(
        0x8,
        (
            "You are challenging me\x01",
            "to a duel, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a "3-Round Angler Duel".\x01",
            "Whoever's fish have the\x01",
            "highest total length, wins\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Kaguya, the\x01",
            "Dragon Queen, to a\x01",
            ""3-Round Angler Duel"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Challenge Her\x01",      # 0
            "Refuse\x01",             # 1
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
        (0, "loc_2B9E"),
        (1, "loc_2E05"),
        (SWITCH_DEFAULT, "loc_2E69"),
    )


    label("loc_2B9E")


    ChrTalk(
        0x8,
        "Uhuhu, very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I shall teach you just\x01",
            "how little you know of\x01",
            "your place!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(-14150, 5600, 86170, 0)
    MoveCamera(55, 37, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x0, -43010, 3000, 96810, 329)
    OP_31(0x1)
    SetChrPos(0x101, -13710, 5000, 85050, 80)
    OP_93(0x8, 0x50, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51009.itc")
    MiniGame(0x7, 0x4, 0x8, 0xFFFFE7DC, 0x3E8, 0x15478, 0xFFFFEBC4, 0x3E8, 0x16418)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    SetChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1D")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-13930, 5000, 87460, 0)
    MoveCamera(55, 37, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -15660, 5000, 87000, 90)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(500)
    Call(0, 18)
    Return()

    label("loc_2D1D")

    OP_68(-14150, 5600, 86170, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -13710, 5000, 85050, 353)
    OP_93(0xFE, 0xAD, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7C")
    Call(0, 19)
    Jump("loc_2DA0")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8F")
    Jump("loc_2DA0")

    label("loc_2D8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA0")
    Call(0, 20)

    label("loc_2DA0")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x50, 0x0)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x0, -13710, 5000, 85050, 353)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E00")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2E00")

    Jump("loc_2E69")

    label("loc_2E05")


    ChrTalk(
        0x8,
        (
            "Uhuhu, you seem to be\x01",
            "seized with fear. ...You\x01",
            "boring man.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E64")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2E64")

    Jump("loc_2E69")

    label("loc_2E69")

    Jump("loc_2F65")

    label("loc_2E6E")


    ChrTalk(
        0x8,
        (
            "Haha, then I'll check\x01",
            "your fishing notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "*sigh*, how\x01",
            "disappointing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm looking for proof you've caugh a\x01",
            "big one of 130 rege or more... This\x01",
            "level of catch doesn't suffice.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F65")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2F65")

    Jump("loc_35E2")

    label("loc_2F6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F9B")
    Jump("loc_35E2")

    label("loc_2F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3066")

    ChrTalk(
        0x8,
        (
            "*sigh*, I have come to yearn\x01",
            "for the languid atmosphere\x01",
            "of the Imperial capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although I'm doing this for Sir\x01",
            "Lakelord... I wonder how long I\x01",
            "should fish in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E2")

    label("loc_3066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315F")

    ChrTalk(
        0x8,
        (
            "The Arc-en-Ciel renewal\x01",
            "performance will be held\x01",
            "tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, I'm not even\x01",
            "remotely interested in\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "More importantly,\x01",
            "there's fishing. Fishing\x01",
            "is the best of all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31B5")

    label("loc_315F")


    ChrTalk(
        0x8,
        "...Achoo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*shiver shiver*... Even\x01",
            "so, can nothing be done\x01",
            "about this rain!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B5")

    Jump("loc_35E2")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3269")

    ChrTalk(
        0x8,
        (
            "This place being a rest\x01",
            "area, sometimes people\x01",
            "come and talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, those common people!\x01",
            "Don't speak with me, a noble,\x01",
            "in such a familiar tone!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E2")

    label("loc_3269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_336B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FE")

    ChrTalk(
        0x8,
        (
            "Ooh ho ho ho. They're\x01",
            "biting at every cast\x01",
            "today, just like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, I've had\x01",
            "enough of being alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3366")

    label("loc_32FE")


    ChrTalk(
        0x8,
        (
            "Although it is for work,\x01",
            "Sylum is with Sir\x01",
            "Lakelord today as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*mgrr*, unforgivable...!\x02",
    )

    CloseMessageWindow()

    label("loc_3366")

    Jump("loc_35E2")

    label("loc_336B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_346C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341E")

    ChrTalk(
        0x8,
        (
            "Aah, Sir Lakelord... I\x01",
            "adore you㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "Oh, no... Did you hear\x01",
            "what I just said!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "T-Tell no one of this!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_3467")

    label("loc_341E")


    ChrTalk(
        0x8,
        (
            "Listen... Not a single\x01",
            "word to anyone of what\x01",
            "you heard, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3467")

    Jump("loc_35E2")

    label("loc_346C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34D6")

    ChrTalk(
        0x8,
        (
            "Anyway... This area\x01",
            "is... countryside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How I miss the offshore\x01",
            "fishing in Kreuze.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E2")

    label("loc_34D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(
        0x8,
        (
            "Ooh ho ho ho, today too\x01",
            "I fished too much and\x01",
            "now it's a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Aah, Sir Lakelord... I\x01",
            "am afraid of my own\x01",
            "talent.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C6")

    ChrTalk(
        0x101,
        (
            "#00003F(It seems I could fish\x01",
            "here, but... Since there's\x01",
            "already someone, I won't.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C6")

    Jump("loc_35E2")

    label("loc_35CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_35D9")
    Jump("loc_35E2")

    label("loc_35D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_35E2")

    label("loc_35E2")

    Jump("loc_2845")

    label("loc_35E7")

    TalkEnd(0xFE)
    Return()

    # Function_11_2447 end

    def Function_12_35EB(): pass

    label("Function_12_35EB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_361E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_361E")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_363D")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_363D")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_365C")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_365C")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_367B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_367B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_369A")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_369A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36B9")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36B9")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36D8")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36D8")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36F7")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36F7")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3716")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3716")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3735")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3735")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3754")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3754")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3773")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3773")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3792")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3792")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37B1")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37B1")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37D0")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37D0")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37EF")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37EF")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_380E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_380E")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_382D")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_382D")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_384C")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_384C")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_386B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_386B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_388A")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_388A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38A9")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38A9")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38C8")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38C8")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38E7")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E7")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3906")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3906")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3925")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3925")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3944")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3944")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3963")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3963")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3982")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3982")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39A1")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39A1")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39C0")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39C0")

    Return()

    # Function_12_35EB end

    def Function_13_39C1(): pass

    label("Function_13_39C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A70")

    ChrTalk(
        0xFE,
        (
            "I didn't expect it to\x01",
            "rain. ...I must take\x01",
            "shelter here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to eat a warm\x01",
            "Armorica Village omelet\x01",
            "rice quickly...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AB7")

    label("loc_3A70")


    ChrTalk(
        0xFE,
        (
            "...That woman, fishing\x01",
            "in this rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...She's quite brave.\x02",
    )

    CloseMessageWindow()

    label("loc_3AB7")

    TalkEnd(0xFE)
    Return()

    # Function_13_39C1 end

    def Function_14_3ABB(): pass

    label("Function_14_3ABB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_14_3ABB end

    def Function_15_3AD9(): pass

    label("Function_15_3AD9")

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
    OP_68(-11080, 5600, 87130, 1500)
    MoveCamera(45, 39, 0, 1500)
    OP_6E(560, 1500)
    SetCameraDistance(20000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D81")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BB2")
    MiniGame(0x6, 0x19, 0xFFFFC996, 0x1388, 0x1550E, 0x5A, 0xFFFFEBC4, 0x3E8, 0x16418)
    Jump("loc_3D81")

    label("loc_3BB2")

    MiniGame(0x6, 0x1A, 0xFFFFC996, 0x1388, 0x1550E, 0x5A, 0xFFFFEBC4, 0x3E8, 0x16418)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D81")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D81")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-12420, 5600, 87570, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16090, 0)
    LoadChrToIndex("apl/ch50161.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -13930, 5000, 87310, 90)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x0,
        "Lloyd",
        (
            "#00011FT-This is... I've fished\x01",
            "up another amazing big\x01",
            "one.\x02\x03",
            "#00003FIt looks just like a\x01",
            "tiger... I wonder if\x01",
            "it's a special fish?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -13930, 5000, 87310, 90)
    SetChrPos(0x2, -13930, 5000, 87310, 90)
    SetChrPos(0x3, -13930, 5000, 87310, 90)
    SetChrPos(0x4, -13930, 5000, 87310, 90)
    SetChrPos(0x5, -13930, 5000, 87310, 90)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 4)

    label("loc_3D81")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_3AD9 end

    def Function_16_3D86(): pass

    label("Function_16_3D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 2)), scpexpr(EXPR_END)), "loc_3D90")
    Return()

    label("loc_3D90")

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
            "A large monster is\x01",
            "wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3E6E"),
        (SWITCH_DEFAULT, "loc_3E87"),
    )


    label("loc_3E6E")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -45080, 3000, 53100, 225)
    EventEnd(0x5)
    Return()

    label("loc_3E87")

    Battle("BattleInfo_B10", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-45080, 4000, 53100, 0)
    OP_90(0x0, -45080, 3000, 53100, 225)
    OP_90(0x1, -45080, 3000, 53100, 225)
    OP_90(0x2, -45080, 3000, 53100, 225)
    OP_90(0x3, -45080, 3000, 53100, 225)
    OP_90(0x4, -45080, 3000, 53100, 225)
    OP_90(0x5, -45080, 3000, 53100, 225)
    OP_90(0x6, -45080, 3000, 53100, 225)
    OP_90(0x7, -45080, 3000, 53100, 225)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3F49"),
        (1, "loc_3F4E"),
        (SWITCH_DEFAULT, "loc_3F51"),
    )


    label("loc_3F49")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3F4E")

    OP_B9(0x0)
    Return()

    label("loc_3F51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-39730, 3600, 57510, 0)
    MoveCamera(58, 27, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19000, 0)
    SetChrFlags(0x1B, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted monster\x01",
            "exterminated!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xC, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -38500, 3030, 57500, 270)
    SetChrPos(0x102, -42500, 3010, 57500, 87)
    SetChrPos(0x105, -40500, 3010, 59500, 177)
    SetChrPos(0x109, -40500, 3010, 55500, 357)
    SetChrPos(0x104, -39000, 3030, 59000, 222)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x104,
        (
            "#00305FHmm. A Craft Book, huh?\x02\x03",
            "#00300FI guess this one's for\x01",
            "Wazy and Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FNoｱl, want to try it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FYes, of course!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x8, 0x194)
    AddCraft(0x4, 0x194)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl and Wazy learned\x01",
            "the "Blue Breaker"\x07\x05",
            " Combi\x01",
            "Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP,\x01",
            "a powerful combination\x01",
            "attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 2)
    OP_29(0x72, 0x4, 0x10)
    OP_29(0x72, 0x4, 0x2)
    OP_29(0x72, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_3D86 end

    def Function_17_41E0(): pass

    label("Function_17_41E0")

    Battle("BattleInfo_B54", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4227")
    OP_90(0x0, -89760, -1000, 128090, 180)
    EventEnd(0x5)
    SetChrFlags(0xE, 0x8000)
    Jump("loc_425B")

    label("loc_4227")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_423A")
    Jump("loc_425B")

    label("loc_423A")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x2, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 4)
    EventEnd(0x5)

    label("loc_425B")

    Return()

    # Function_17_41E0 end

    def Function_18_425C(): pass

    label("Function_18_425C")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Unbelievable... To think\x01",
            "you did so well against\x01",
            "I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, I am an\x01",
            "angler as well. I\x01",
            "honorably admit defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That being the case,\x01",
            "please take this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2A, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I recognize you as the\x01",
            ""Dragon Queen Killer" as per\x01",
            "Imperial Fishing Club rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, it would be a\x01",
            "problem if you got carried\x01",
            "away just for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter how much you\x01",
            "struggle, you will be no\x01",
            "match for Sir Lakelord...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to him, people\x01",
            "like you are nothing more\x01",
            "than a frog in a well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rather, a tadpole... No,\x01",
            "a mosquito larva...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...No, a water flea!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C0, 4)
    SetChrPos(0x8, -13710, 5000, 85050, 80)
    OP_66(0x4, 0x1)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4585")
    SetChrFlags(0x8, 0x10)

    label("loc_4585")

    SetChrPos(0x0, -15660, 5000, 87000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_425C end

    def Function_19_459D(): pass

    label("Function_19_459D")


    ChrTalk(
        0x8,
        (
            "Uhuhu... You are too\x01",
            "weak, too weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if there is a next time,\x01",
            "please at least show me some fun\x01",
            "then. OOH HO HO HO HO HO HO!!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_19_459D end

    def Function_20_462B(): pass

    label("Function_20_462B")


    ChrTalk(
        0x8,
        (
            "Stopping midway\x01",
            "through... Hehe, you are\x01",
            "quite the coward.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_20_462B end

    def Function_21_466C(): pass

    label("Function_21_466C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Armorica Old Road - Rest Area\x01",
            "  ※This being a public place,\x01",
            "    let's mind our manners.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_21_466C end

    SaveToFile()

Try(main)
