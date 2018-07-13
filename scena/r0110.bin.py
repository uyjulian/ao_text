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
        "Function_6_1C1D",         # 06, 6
        "Function_7_1D6F",         # 07, 7
        "Function_8_20CD",         # 08, 8
        "Function_9_242B",         # 09, 9
        "Function_10_2449",        # 0A, 10
        "Function_11_244D",        # 0B, 11
        "Function_12_35E8",        # 0C, 12
        "Function_13_39BE",        # 0D, 13
        "Function_14_3AC4",        # 0E, 14
        "Function_15_3AE2",        # 0F, 15
        "Function_16_3D8F",        # 10, 16
        "Function_17_41F7",        # 11, 17
        "Function_18_4273",        # 12, 18
        "Function_19_4595",        # 13, 19
        "Function_20_4624",        # 14, 20
        "Function_21_4666",        # 15, 21
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BC2")

    Jump("loc_1C11")

    label("loc_1BC7")

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

    label("loc_1C11")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1ACB end

    def Function_6_1C1D(): pass

    label("Function_6_1C1D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D19")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x99, 1)"), scpexpr(EXPR_END)), "loc_1CA2")
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
    Jump("loc_1D14")

    label("loc_1CA2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x99),
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

    label("loc_1D14")

    Jump("loc_1D63")

    label("loc_1D19")

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

    label("loc_1D63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C1D end

    def Function_7_1D6F(): pass

    label("Function_7_1D6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F27")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1F08")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F03")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1F00")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E25)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EE2")
    Call(1, 5)
    Jump("loc_1EFB")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EF8")
    Call(1, 4)
    Jump("loc_1EFB")

    label("loc_1EF8")

    Call(1, 3)

    label("loc_1EFB")

    Jump("loc_1F03")

    label("loc_1F00")

    Call(1, 1)

    label("loc_1F03")

    Jump("loc_1F1E")

    label("loc_1F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1F1E")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1F1E")

    TalkEnd(0xFF)
    Return()

    label("loc_1F27")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_20B2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AD")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_20AA")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1FCF)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A5")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_208C")
    Call(1, 5)
    Jump("loc_20A5")

    label("loc_208C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20A2")
    Call(1, 4)
    Jump("loc_20A5")

    label("loc_20A2")

    Call(1, 3)

    label("loc_20A5")

    Jump("loc_20AD")

    label("loc_20AA")

    Call(1, 1)

    label("loc_20AD")

    Jump("loc_20C8")

    label("loc_20B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_20C8")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_20C8")

    TalkEnd(0xFF)
    Return()

    # Function_7_1D6F end

    def Function_8_20CD(): pass

    label("Function_8_20CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2285")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2266")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2261")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_225E")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2183():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2183)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2259")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2240")
    Call(1, 5)
    Jump("loc_2259")

    label("loc_2240")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2256")
    Call(1, 4)
    Jump("loc_2259")

    label("loc_2256")

    Call(1, 3)

    label("loc_2259")

    Jump("loc_2261")

    label("loc_225E")

    Call(1, 1)

    label("loc_2261")

    Jump("loc_227C")

    label("loc_2266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_227C")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_227C")

    TalkEnd(0xFF)
    Return()

    label("loc_2285")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2410")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240B")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2408")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_232D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_232D)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2403")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23EA")
    Call(1, 5)
    Jump("loc_2403")

    label("loc_23EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2400")
    Call(1, 4)
    Jump("loc_2403")

    label("loc_2400")

    Call(1, 3)

    label("loc_2403")

    Jump("loc_240B")

    label("loc_2408")

    Call(1, 1)

    label("loc_240B")

    Jump("loc_2426")

    label("loc_2410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2426")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2426")

    TalkEnd(0xFF)
    Return()

    # Function_8_20CD end

    def Function_9_242B(): pass

    label("Function_9_242B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2448")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_2448")

    Return()

    # Function_9_242B end

    def Function_10_2449(): pass

    label("Function_10_2449")

    Call(1, 6)
    Return()

    # Function_10_2449 end

    def Function_11_244D(): pass

    label("Function_11_244D")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2465")
    SetScenarioFlags(0x0, 2)

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_2471")
    SetScenarioFlags(0x0, 2)

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2837")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, my name is Lloyd,\x01",
            "from the Fisherman's Guild.\x02\x03",
            "You're from the Fishing Emperor Club, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, you have finally come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, I am the only woman\x01",
            "of the Elite Four...\x01",
            "My name is Kaguya, the "Dragon Queen".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Being who I am, I will pulverize the\x01",
            "Fisherman's Guild and the likes...\x01",
            "A decisive win it will be, an instant killing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh ho ho, oh ho ho ho, ooohhohoo―\x02",
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
            "...I-In any case!\x01",
            "It is in your best interests to not harbor the\x01",
            "fantasy or something like winning against me.\x02",
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
            "Well, but before that, I will ascertain\x01",
            "if you are qualified, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to challenge me,\x01",
            "show me you caught a big\x01",
            "game of 130 rege or more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We will talk about it after that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2837")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2837")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2898")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                                 # 0
            "Challenge Her to an Angler Duel\x01",      # 1
            "Quit\x01",                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_28A2")

    label("loc_2898")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28CB")
    TurnDirection(0x8, 0x0, 0)

    label("loc_28CB")

    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7B")

    ChrTalk(
        0x8,
        (
            "Uh uh, then, I will check\x01",
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
            "Indeed, you really seem\x01",
            "to have caught a big \x01",
            "game of 130 rege or more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, about the "Angler Duel"\x01",
            "against me that you longed for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is simple but profound. We will\x01",
            "do a "3 Rounds Angler Duel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have 3 chances...\x01\x07\x02",
            "Who has the bigger\x01",
            "size sum total, wins\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 2)
    Jump("loc_2AFB")

    label("loc_2A7B")


    ChrTalk(
        0x8,
        "You are challenging me to a duel, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is a "3 Rounds Angler Duel".\x01\x07\x02",
            "Who has the bigger\x01",
            "size sum total, wins\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFB")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Kaguya, the "Dragon Queen",\x01",
            "to a "3 Rounds Angler Duel"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Challenge Her\x01",      # 0
            "Do Not\x01",             # 1
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
        (0, "loc_2BA2"),
        (1, "loc_2E05"),
        (SWITCH_DEFAULT, "loc_2E65"),
    )


    label("loc_2BA2")


    ChrTalk(
        0x8,
        "Uhuhu, very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will teach you how much\x01",
            "you do not know your place!\x02",
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

    Jump("loc_2E65")

    label("loc_2E05")


    ChrTalk(
        0x8,
        (
            "Uhuhu, you seem to be seized with fear.\x01",
            "...Boring man.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E60")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2E60")

    Jump("loc_2E65")

    label("loc_2E65")

    Jump("loc_2F73")

    label("loc_2E6A")


    ChrTalk(
        0x8,
        (
            "Uh uh, then, I will check\x01",
            "your fishing notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "*sigh*, disappointing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What I am looking for is the proof you\x01",
            "have caught a big game of 130 rege or more...\x01",
            "This level of catches do not suffice.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F73")
    OP_93(0x8, 0x50, 0x0)
    SetChrFlags(0x8, 0x10)

    label("loc_2F73")

    Jump("loc_35DF")

    label("loc_2F78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FA9")
    Jump("loc_35DF")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_306D")

    ChrTalk(
        0x8,
        (
            "*sigh*, I have come to yearn for the\x01",
            "languid atmosphere of the empire capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is for Sir Lakelord...\x01",
            "I wonder for how much time\x01",
            "should I fish in such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DF")

    label("loc_306D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316F")

    ChrTalk(
        0x8,
        (
            "Tomorrow, the Arc-en-ciel\x01",
            "renewal public performance\x01",
            "is going to take place...\x02",
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
            "Hmph, I am not even remotely\x01",
            "interested in something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "More than that, fishing,\x01",
            "fishing is the best of all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31CC")

    label("loc_316F")


    ChrTalk(
        0x8,
        "...*atchoo*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*shiver shiver*...even so, can not\x01",
            "anything be done about this rain!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CC")

    Jump("loc_35DF")

    label("loc_31D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3279")

    ChrTalk(
        0x8,
        (
            "Being this place a refresh area,\x01",
            "sometimes people come and\x01",
            "they talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, those common people!\x01",
            "Do not speak familiarly\x01",
            "to me, a noble!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DF")

    label("loc_3279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330A")

    ChrTalk(
        0x8,
        (
            "Ooh ho ho ho, today too they bite\x01",
            "at every cast, like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, I have had\x01",
            "enough of being alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_336E")

    label("loc_330A")


    ChrTalk(
        0x8,
        (
            "Although it is for work, today too\x01",
            "Sylum is with Sir Lakelord...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*mgrr*, unforgivable...!\x02",
    )

    CloseMessageWindow()

    label("loc_336E")

    Jump("loc_35DF")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342C")

    ChrTalk(
        0x8,
        (
            "Aah, Sir Lakelord...\x01",
            "I adore you㈱\x02",
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
            "Oh, no...\x01",
            "You have heard what I just said!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "D-Do not tell anyone else!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_3464")

    label("loc_342C")


    ChrTalk(
        0x8,
        (
            "Listen...\x01",
            "Not a word to anyone of what you heard!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3464")

    Jump("loc_35DF")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34D2")

    ChrTalk(
        0x8,
        (
            "Anyway...\x01",
            "This area is...countryside.\x02",
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
    Jump("loc_35DF")

    label("loc_34D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35C8")

    ChrTalk(
        0x8,
        (
            "Ooh ho ho ho, today too I fished too\x01",
            "much and now it is a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Aah, Sir Lakelord...\x01",
            "I am afraid of my own talent.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C3")

    ChrTalk(
        0x101,
        (
            "#00003F(It seems I could fish here, but...\x01",
            "Since there's already someone, I won't.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C3")

    Jump("loc_35DF")

    label("loc_35C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_35D6")
    Jump("loc_35DF")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_35DF")

    label("loc_35DF")

    Jump("loc_2841")

    label("loc_35E4")

    TalkEnd(0xFE)
    Return()

    # Function_11_244D end

    def Function_12_35E8(): pass

    label("Function_12_35E8")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_361B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_361B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_363A")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_363A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3659")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3659")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3678")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3678")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3697")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3697")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36B6")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36B6")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36D5")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36D5")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36F4")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36F4")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3713")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3713")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3732")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3732")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3751")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3751")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3770")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3770")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_378F")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_378F")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37AE")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37AE")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37CD")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37CD")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37EC")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37EC")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_380B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_380B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_382A")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_382A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3849")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3849")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3868")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3868")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3887")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3887")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38A6")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38A6")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38C5")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38C5")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38E4")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E4")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3903")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3903")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3922")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3922")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3941")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3941")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3960")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3960")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_397F")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_397F")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_399E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_399E")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39BD")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39BD")

    Return()

    # Function_12_35E8 end

    def Function_13_39BE(): pass

    label("Function_13_39BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A73")

    ChrTalk(
        0xFE,
        (
            "I didn't expect if was going to rain.\x01",
            "...I must take shelter here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to eat a warm Armorica\x01",
            "Village omurice quickly...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AC0")

    label("loc_3A73")


    ChrTalk(
        0xFE,
        (
            "...That woman, fishing\x01",
            "amidst such a rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...She's quite brave.\x02",
    )

    CloseMessageWindow()

    label("loc_3AC0")

    TalkEnd(0xFE)
    Return()

    # Function_13_39BE end

    def Function_14_3AC4(): pass

    label("Function_14_3AC4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_14_3AC4 end

    def Function_15_3AE2(): pass

    label("Function_15_3AE2")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
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
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8A")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BB9")
    MiniGame(0x6, 0x19, 0xFFFFC996, 0x1388, 0x1550E, 0x5A, 0xFFFFEBC4, 0x3E8, 0x16418)
    Jump("loc_3D8A")

    label("loc_3BB9")

    MiniGame(0x6, 0x1A, 0xFFFFC996, 0x1388, 0x1550E, 0x5A, 0xFFFFEBC4, 0x3E8, 0x16418)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D8A")
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
            "#00011FT-This is...\x01",
            "I've fished up another amazing big game.\x02\x03",
            "#00003FIt looks just like a tiger...\x01",
            "I wonder if it's a special fish?\x01\x02",
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

    label("loc_3D8A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_3AE2 end

    def Function_16_3D8F(): pass

    label("Function_16_3D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 2)), scpexpr(EXPR_END)), "loc_3D99")
    Return()

    label("loc_3D99")

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
        (1, "loc_3E75"),
        (SWITCH_DEFAULT, "loc_3E8E"),
    )


    label("loc_3E75")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -45080, 3000, 53100, 225)
    EventEnd(0x5)
    Return()

    label("loc_3E8E")

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
        (2, "loc_3F50"),
        (1, "loc_3F55"),
        (SWITCH_DEFAULT, "loc_3F58"),
    )


    label("loc_3F50")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3F55")

    OP_B9(0x0)
    Return()

    label("loc_3F58")

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
            "#00305FHm, a Craft Book, huh?\x02\x03",
            "#00300FThis one seems suited for Wazy and Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FNoｱl, do you want to try it?\x02",
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
            "Noｱl and Wazy have learned the\x01\x07\x02",
            ""Blue Breaker"\x07\x05",
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

    # Function_16_3D8F end

    def Function_17_41F7(): pass

    label("Function_17_41F7")

    Battle("BattleInfo_B54", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_423E")
    OP_90(0x0, -89760, -1000, 128090, 180)
    EventEnd(0x5)
    SetChrFlags(0xE, 0x8000)
    Jump("loc_4272")

    label("loc_423E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4251")
    Jump("loc_4272")

    label("loc_4251")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x2, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 4)
    EventEnd(0x5)

    label("loc_4272")

    Return()

    # Function_17_41F7 end

    def Function_18_4273(): pass

    label("Function_18_4273")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Unbelievable...\x01",
            "I, have to withdraw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, I am an angler too.\x01",
            "I properly recognise my defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, please\x01",
            "take this.\x02",
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
            "Then, I recognize you as the "Dragon Queen\x01",
            "Killer" as per Fishing Emperor Club rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...However, it would be a problem\x01",
            "if you got carried away just for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter how you struggle, you\x01",
            "will be no match for Sir Lakelord...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to that person, people like\x01",
            "you are similar to a frog in a well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rather, a tadpole...\x01",
            "No, a mosquito's larva...\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_457D")
    SetChrFlags(0x8, 0x10)

    label("loc_457D")

    SetChrPos(0x0, -15660, 5000, 87000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_4273 end

    def Function_19_4595(): pass

    label("Function_19_4595")


    ChrTalk(
        0x8,
        (
            "Uhuhu...\x01",
            "You are too weak, too weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if there will be a next time,\x01",
            "please make me have some fun then.\x01",
            "OOH OH OH OH OH OH OH!!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_19_4595 end

    def Function_20_4624(): pass

    label("Function_20_4624")


    ChrTalk(
        0x8,
        (
            "Stopping midway through...\x01",
            "Uh uh, you are quite the coward.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_20_4624 end

    def Function_21_4666(): pass

    label("Function_21_4666")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Armorica Old Road - Refresh Area"\x01",
            "  ※Being this a public place,\x01",
            "     let's mind our manners.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_21_4666 end

    SaveToFile()

Try(main)
