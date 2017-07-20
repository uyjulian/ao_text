from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0302.bin",                # FileName
        "m0302",                    # MapName
        "m0302",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0302",                  # 0
        "Insertion",           # 1
        "儕乕 儕乕 嵏 姱 姱",         # 2
        "儌儞 僪 僪 嵏姱 嵏姱 嵏姱",       # 3
        "僄儅 嵏 姱 姱",             # 4
        "儘僶 乕僣 庡擟",           # 5
        "Ceremonial ceremony",         # 6
        "I and I",       # 7
        "Working",           # 8
        "Interrogation",           # 9
        "寈姱",                   # 10
        "寈姱",                   # 11
        "Possession",                 # 12
        "Possession",                 # 13
        "僲僄 儖",                 # 14
        "Episode I",                   # 15
        "儕乕 僔儍",               # 16
        "False falsehood",   # 17
        "bm0300",                 # 18
        "bm0300",                 # 19
        "bm0300",                 # 20
        "bm0300",                 # 21
        "bm0300",                 # 22
    ))

    ATBonus("ATBonus_604", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_624", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6CCE", 5,   5,   5,   5,   10,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_664", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_66C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_644", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_704", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7A0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
        (
            ("ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84300.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84300.dat", "ms84200.dat", "ms84100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_91C", 0x0C40, 255, 6, 0, 0, 3, 0, 0, "bm0300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", 0, 0, "MonsterBattlePostion_6E4", "MonsterBattlePostion_6C4", "ed7454", "ed7453", "ATBonus_624"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_8D8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm0300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7451", "ed7453", "ATBonus_604"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch00900.itc",                   # 01
        "chr/ch30200.itc",                   # 02
        "chr/ch30500.itc",                   # 03
        "chr/ch29300.itc",                   # 04
        "chr/ch30400.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch30600.itc",                   # 07
        "chr/ch32800.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch27600.itc",                   # 0A
        "chr/ch27800.itc",                   # 0B
        "chr/ch02900.itc",                   # 0C
        "chr/ch03100.itc",                   # 0D
        "chr/ch03200.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch84150.itc",               # 10
        "monster/ch84150.itc",               # 11
        "monster/ch84250.itc",               # 12
        "monster/ch84250.itc",               # 13
        "monster/ch84350.itc",               # 14
        "monster/ch84350.itc",               # 15
        "monster/ch80150.itc",               # 16
        "monster/ch80151.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(16000,   4294961796, 338000,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294961076, 183090,  4294951296, 0x10100E1,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6460,    179480,  4294951296, 0x101010E,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294946046, 174340,  4294951296, 0x101002D,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294789376, 195000,  4000,    0x101010E,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294770116, 201540,  6000,    0x1010059,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6220,    342630,  2000,    0x101013B,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(26750,   342940,  2000,    0x10100E1,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(22170,   199660,  4294965296, 0x101002D,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(341820,  99110,   6000,    0x10100E1,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(327420,  77460,   0,       0x101010E,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(349980,  198200,  0,       0x101010E,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294467296, 500000,  0,       0x18500B4,    "BattleInfo_91C", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0040, 0, 26,  -500.0,                500.0,                 -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   62.5,                  -62.5,                 0.25,                  1.0])

    DeclActor(34000,   4294965296, 190000,  1200,    34000,   4294966296, 190000,  0x007C, 0,  4,  0x0000)
    DeclActor(16000,   4294961296, 338000,  1200,    16000,   4294962296, 338000,  0x007C, 0,  5,  0x0000)
    DeclActor(4294965296, 4294959296, 610000,  1200,    4294965296, 4294960296, 610000,  0x007C, 0,  6,  0x0000)
    DeclActor(350000,  0,       200000,  1200,    350000,  1000,    200000,  0x007C, 0,  7,  0x0000)
    DeclActor(4294956696, 4294951296, 193500,  1200,    4294956696, 4294952296, 193500,  0x007C, 0,  29, 0x0000)
    DeclActor(10000,   4294959296, 193500,  1200,    10000,   4294960296, 193500,  0x007C, 0,  30, 0x0000)
    DeclActor(4294953296, 4294959296, 192500,  1200,    4294953296, 4294960296, 192500,  0x007C, 0,  31, 0x0000)
    DeclActor(5500,    0,       748500,  1200,    5500,    1000,    748500,  0x007C, 0,  27, 0x0000)
    DeclActor(4294961296, 4294951296, 21660,   1200,    4294961296, 4294952296, 21660,   0x007C, 0,  25, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 7

    ScpFunction((
        "Function_0_A54",          # 00, 0
        "Function_1_B04",          # 01, 1
        "Function_2_B20",          # 02, 2
        "Function_3_BBD",          # 03, 3
        "Function_4_11AB",         # 04, 4
        "Function_5_12FC",         # 05, 5
        "Function_6_1513",         # 06, 6
        "Function_7_1664",         # 07, 7
        "Function_8_17CB",         # 08, 8
        "Function_9_1A77",         # 09, 9
        "Function_10_1C79",        # 0A, 10
        "Function_11_1EE1",        # 0B, 11
        "Function_12_21B7",        # 0C, 12
        "Function_13_2527",        # 0D, 13
        "Function_14_26F7",        # 0E, 14
        "Function_15_28EB",        # 0F, 15
        "Function_16_2B79",        # 10, 16
        "Function_17_2D10",        # 11, 17
        "Function_18_2EA8",        # 12, 18
        "Function_19_30CA",        # 13, 19
        "Function_20_323B",        # 14, 20
        "Function_21_3377",        # 15, 21
        "Function_22_33C9",        # 16, 22
        "Function_23_343B",        # 17, 23
        "Function_24_358E",        # 18, 24
        "Function_25_3774",        # 19, 25
        "Function_26_3870",        # 1A, 26
        "Function_27_3B2F",        # 1B, 27
        "Function_28_3CA1",        # 1C, 28
        "Function_29_3DB0",        # 1D, 29
        "Function_30_3F33",        # 1E, 30
        "Function_31_40B5",        # 1F, 31
        "Function_32_4237",        # 20, 32
        "Function_33_42C3",        # 21, 33
        "Function_34_481F",        # 22, 34
        "Function_35_4D62",        # 23, 35
        "Function_36_6B56",        # 24, 36
    ))


    def Function_0_A54(): pass

    label("Function_0_A54")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_A8C"),
        (1, "loc_A98"),
        (2, "loc_AA4"),
        (3, "loc_AB0"),
        (4, "loc_ABC"),
        (5, "loc_AC8"),
        (6, "loc_AD4"),
        (SWITCH_DEFAULT, "loc_AE0"),
    )


    label("loc_A8C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_A98")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AA4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AB0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_ABC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AC8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AD4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AE0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B03")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_B03")

    Return()

    # Function_0_A54 end

    def Function_1_B04(): pass

    label("Function_1_B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_B04")

    label("loc_B1F")

    Return()

    # Function_1_B04 end

    def Function_2_B20(): pass

    label("Function_2_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B31")
    Call(0, 24)

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B45")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)
    Jump("loc_B57")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B57")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 35)

    label("loc_B57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6E")
    Event(0, 28)

    label("loc_B6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBC")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetScenarioFlags(0x151, 1)
    SetScenarioFlags(0x151, 2)
    SetScenarioFlags(0x151, 3)

    label("loc_BBC")

    Return()

    # Function_2_B20 end

    def Function_3_BBD(): pass

    label("Function_3_BBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE3")
    ClearMapFlags(0x2000)
    Jump("loc_BE8")

    label("loc_BE3")

    SetMapFlags(0x2000)

    label("loc_BE8")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C32")
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_C32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA6")

    label("loc_C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C68")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_CA6")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C81")
    OP_C9(0x0, 0x8)
    Jump("loc_CA6")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA6")

    label("loc_C9D")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBF")
    OP_10(0x0, 0x0)
    OP_10(0x1A, 0x1)
    Jump("loc_CC5")

    label("loc_CBF")

    OP_10(0x0, 0x1)
    OP_10(0x1A, 0x0)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD9")
    OP_1B(0x1, 0x0, 0x21)

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_D3D")
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)
    Jump("loc_D93")

    label("loc_D3D")

    SetMapObjFrame(0x7, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_DF7")
    SetMapObjFrame(0x8, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_2", 0x0, 0x1)
    Jump("loc_E4D")

    label("loc_DF7")

    SetMapObjFrame(0x8, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_2", 0x0, 0x1)

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_EB1")
    SetMapObjFrame(0x9, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_2", 0x0, 0x1)
    Jump("loc_F07")

    label("loc_EB1")

    SetMapObjFrame(0x9, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_2", 0x0, 0x1)

    label("loc_F07")

    ClearMapObjFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F43")
    SetMapObjFrame(0x11, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x1, 0x1)
    OP_70(0x11, 0x28)
    Jump("loc_F63")

    label("loc_F43")

    SetMapObjFrame(0x11, "lock_r", 0x1, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x0, 0x1)
    OP_70(0x11, 0x0)

    label("loc_F63")

    OP_10(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9E")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    Jump("loc_1001")

    label("loc_F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDC")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x1, 0x1)
    Jump("loc_1001")

    label("loc_FDC")

    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)

    label("loc_1001")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 16000, -6000, 343500, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104A")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "close")
    SetMapObjFlags(0x14, 0x4)
    SetBarrier(0x3, 0x0, 0x1)
    Jump("loc_106F")

    label("loc_104A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_106F")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetMapObjFlags(0x14, 0x4)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088")
    ClearChrFlags(0x24, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x24, 0x8000)

    label("loc_1088")

    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1161")
    OP_70(0x3, 0x0)
    Jump("loc_1165")

    label("loc_1161")

    OP_70(0x3, 0x1E)

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")
    OP_70(0x4, 0x0)
    Jump("loc_117C")

    label("loc_1178")

    OP_70(0x4, 0x1E)

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118F")
    OP_70(0x5, 0x0)
    Jump("loc_1193")

    label("loc_118F")

    OP_70(0x5, 0x1E)

    label("loc_1193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A6")
    OP_70(0x6, 0x0)
    Jump("loc_11AA")

    label("loc_11A6")

    OP_70(0x6, 0x1E)

    label("loc_11AA")

    Return()

    # Function_3_BBD end

    def Function_4_11AB(): pass

    label("Function_4_11AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AB")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_1234")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_12A6")

    label("loc_1234")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A6")

    Jump("loc_12F0")

    label("loc_12AB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_12F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_11AB end

    def Function_5_12FC(): pass

    label("Function_5_12FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CD")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FB")
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x18, 0x0, 0)
    OP_98(0x18, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1359():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1359)

    def lambda_1373():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1373)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x18, 1)
    Battle("BattleInfo_8D8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13DC"),
        (2, "loc_13EB"),
        (1, "loc_13F8"),
        (SWITCH_DEFAULT, "loc_13FB"),
    )


    label("loc_13DC")

    SetScenarioFlags(0x217, 1)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_13FB")

    label("loc_13EB")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13F8")

    OP_B9(0x0)
    Return()

    label("loc_13FB")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('命中３', 1)"), scpexpr(EXPR_END)), "loc_1458")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_14C8")

    label("loc_1458")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14C8")

    Jump("loc_1507")

    label("loc_14CD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1507")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12FC end

    def Function_6_1513(): pass

    label("Function_6_1513")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1613")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_159C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_160E")

    label("loc_159C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_160E")

    Jump("loc_1658")

    label("loc_1613")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1658")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1513 end

    def Function_7_1664(): pass

    label("Function_7_1664")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1794")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x6, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the Earth × 80\x01\x07\x02",
            "#57IWater sepis × 80\x01\x07\x02",
            "#58IFire sepis × 80\x01\x07\x02",
            "#59IWind sepice × 80\x01\x07\x02",
            "#60ITime sepis × 80\x01\x07\x02",
            "#61IEmpty Sepis × 80\x01\x07\x02",
            "#62IThe phantom sepis × 80\x01\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_17B9")

    label("loc_1794")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_17B9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1664 end

    def Function_8_17CB(): pass

    label("Function_8_17CB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A73")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",              # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A14")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1972")

    ChrTalk(
        0x15,
        (
            "#10103FRush into the Orchis Tower ……\x01",
            "A fierce battle is expected.\x02\x03",
            "#10101FOnce you start a strategy,\x01",
            "It will be difficult to come back … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI see …\x01",
            "I do not know what will happen\x01",
            "You have to be thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#10100FIn the meantime, even in the city's facilities\x01",
            "Who stopped by?\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A0F")

    label("loc_1972")


    ChrTalk(
        0x15,
        (
            "#10103FRush into the Orchis Tower ……\x01",
            "A fierce battle is expected.\x02\x03",
            "#10100FIn the meantime, weapons shops in the city and\x01",
            "Also in the oval store\x01",
            "It seems better to stop by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")

    Jump("loc_1A6E")

    label("loc_1A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6E")

    ChrTalk(
        0x15,
        (
            "#10100FIt is a member organization, is not it?\x01",
            "OK!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1A6E")

    label("loc_1A6E")

    Jump("loc_17D8")

    label("loc_1A73")

    TalkEnd(0xFE)
    Return()

    # Function_8_17CB end

    def Function_9_1A77(): pass

    label("Function_9_1A77")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C75")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",              # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    ChrTalk(
        0x16,
        (
            "#10403FBy the way, when you leave here\x01",
            "It was the old city soon.\x02\x03",
            "#10402FBecause it's cheap\x01",
            "\"Trinity\"\x01",
            "Let's face it out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C16")

    label("loc_1B7C")


    ChrTalk(
        0x16,
        (
            "#10404FThe people in the old town are in Testersants\x01",
            "I will leave it to you.\x02\x03",
            "#10400FWe are in a strategy\x01",
            "Let's concentrate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C16")

    ChrTalk(
        0x101,
        "#00000FOh … That's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C16")

    Jump("loc_1C70")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C70")

    ChrTalk(
        0x16,
        "#10400FHuh, you change your members?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1C70")

    label("loc_1C70")

    Jump("loc_1A84")

    label("loc_1C75")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A77 end

    def Function_10_1C79(): pass

    label("Function_10_1C79")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",              # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E32")

    ChrTalk(
        0x101,
        "#00005FLisha, you were in such a place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#10702FYeah ….\x01",
            "Until the strategy starts, in a quiet place\x01",
            "I thought about raising my mind.\x02\x03",
            "#10703FAt that Orkis Tower,\x01",
            "\"Bloodstained Shirley\"\x01",
            "You should have it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FOh …… Like my uncle, you,\x01",
            "I guess it will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#10701F…… I will not lose, absolutely.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E7A")

    label("loc_1E32")


    ChrTalk(
        0x17,
        (
            "#10703F\"Charlie of blood dyeing\" … ….\x02\x03",
            "#10701F…… I will not lose, absolutely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7A")

    Jump("loc_1ED8")

    label("loc_1E7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(
        0x17,
        "#10700FYes, you change members.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1ED8")

    label("loc_1ED8")

    Jump("loc_1C86")

    label("loc_1EDD")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C79 end

    def Function_11_1EE1(): pass

    label("Function_11_1EE1")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",              # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2144")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B6")

    ChrTalk(
        0x9,
        (
            "#00603FFor operations into the tower\x01",
            "I will accompany you as well.\x02\x03",
            "#00600FYou too\x01",
            "Keep it ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, Mr. Dudley\x01",
            "It is encouraging if you stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00603FArrest the President\x01",
            "Okay, leaving it to the support section … …\x01",
            "It's just that.\x02\x03",
            "#00600FAs soon as I can,\x01",
            "You should go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_213F")

    label("loc_20B6")


    ChrTalk(
        0x9,
        (
            "#00603FPresident's arrest …\x01",
            "It is not as simple as it sounds like\x01",
            "You ought to know.\x02\x03",
            "#00600FFirmly now\x01",
            "Get ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213F")

    Jump("loc_21AE")

    label("loc_2144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AE")

    ChrTalk(
        0x9,
        (
            "#00600FDo you change members?\x01",
            "… … Choose quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_21AE")

    label("loc_21AE")

    Jump("loc_1EEE")

    label("loc_21B3")

    TalkEnd(0xFE)
    Return()

    # Function_11_1EE1 end

    def Function_12_21B7(): pass

    label("Function_12_21B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A9")

    ChrTalk(
        0x8,
        (
            "#01002FWell, even so … …\x01",
            "Either way this also\x01",
            "It seems to be healthy and anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FOnly the section chief ……\x01",
            "I am glad that it was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe section chiefs have been staying in the city\x01",
            "You were doing underground activities, were not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FOh, for a while, based here,\x01",
            "I was talking about a breakthrough … …\x02\x03",
            "#01001FAs it is this way,\x01",
            "I am imitating such a long way\x01",
            "I do not have time to spare.\x02\x03",
            "Whatever you do to you,\x01",
            "You will be successful in this strategy.\x01",
            "…… It is also to get back Ka'aa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … … Please leave it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 4)
    Jump("loc_2523")

    label("loc_23A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A9")

    ChrTalk(
        0x8,
        (
            "#01003FAs it is this way,\x01",
            "I do not have time to imitate a long time.\x02\x03",
            "#01001FWhatever you do to you,\x01",
            "Strategy of entering the Orkis Tower\x01",
            "I will have you succeed.\x02\x03",
            "#01002FFor citizens …… More than anything,\x01",
            "It is also for you and Kia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2523")

    label("loc_24A9")


    ChrTalk(
        0x8,
        (
            "#01004FI also shot guns\x01",
            "Let's keep maintenance.\x02\x03",
            "#01001FOperation of the Orchis Tower's inrush …\x01",
            "You make it successful anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2523")

    TalkEnd(0xFE)
    Return()

    # Function_12_21B7 end

    def Function_13_2527(): pass

    label("Function_13_2527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")

    ChrTalk(
        0xA,
        (
            "Well, before the start of the strategy\x01",
            "I have to check the armed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… That reminds you guys,\x01",
            "To the Donovan police in the hospital\x01",
            "You seem to have met him ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How\x01",
            "You looked fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, with my wife's nursing\x01",
            "It seems to be nearly complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, that was nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "While we did not have a policeman, we\x01",
            "I have to do it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_26F3")

    label("loc_267B")


    ChrTalk(
        0xA,
        (
            "Well, before the start of the strategy\x01",
            "I have to check the armed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "While we did not have a policeman, we\x01",
            "I have to do it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    TalkEnd(0xFE)
    Return()

    # Function_13_2527 end

    def Function_14_26F7(): pass

    label("Function_14_26F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2835")

    ChrTalk(
        0xD,
        (
            "Even if you start an inrush strategy,\x01",
            "Citizen's safety is given top priority\x01",
            "It is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I am not suitable for battle,\x01",
            "To prevent damage within the scope of the operation\x01",
            "I would like to take evacuation guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FSuch a role seems important, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe will be careful with our … …\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_28E7")

    label("loc_2835")


    ChrTalk(
        0xD,
        (
            "I am not suitable for battle,\x01",
            "To prevent damage within the scope of the operation\x01",
            "I would like to take evacuation guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even with such a situation,\x01",
            "Citizen's safety is given top priority\x01",
            "Because it is necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E7")

    TalkEnd(0xFE)
    Return()

    # Function_14_26F7 end

    def Function_15_28EB(): pass

    label("Function_15_28EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")
    TurnDirection(0xB, 0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#00603FEmma, I will leave this place to you.\x02\x03",
            "#00600FIn order not to hinder troubleshooting behavior,\x01",
            "Also to be alarmed around the base\x01",
            "Take care enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, sorry.\x01",
            "… … please take care of Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2A17")

    label("loc_29D0")


    ChrTalk(
        0xB,
        (
            "Please leave this place to us.\x01",
            "… … please take care of Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A17")

    Jump("loc_2B75")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B20")

    ChrTalk(
        0xB,
        (
            "Again, the strategy setup\x01",
            "I am checking it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You too, flow properly\x01",
            "It is in your head, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "… It is OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The success of the strategy\x01",
            "It depends on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please do not forget to prepare.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2B75")

    label("loc_2B20")


    ChrTalk(
        0xB,
        (
            "The success of the strategy\x01",
            "It depends on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please do not forget to prepare.\x02",
    )

    CloseMessageWindow()

    label("loc_2B75")

    TalkEnd(0xFE)
    Return()

    # Function_15_28EB end

    def Function_16_2B79(): pass

    label("Function_16_2B79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA7")

    ChrTalk(
        0xE,
        (
            "From the invalid declaration, also to the headquarters\x01",
            "A policeman who cooperates with us\x01",
            "I'm gathering little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Franz you as a liaison with them\x01",
            "I bought it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FFranz … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, everyone's pride as a police officer\x01",
            "I am doing my best to protect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I also asked for your best regards.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2D0C")

    label("loc_2CA7")


    ChrTalk(
        0xE,
        (
            "Everyone takes pride as a police\x01",
            "I am doing my best to protect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I also asked for your best regards.\x02",
    )

    CloseMessageWindow()

    label("loc_2D0C")

    TalkEnd(0xFE)
    Return()

    # Function_16_2B79 end

    def Function_17_2D10(): pass

    label("Function_17_2D10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E51")

    ChrTalk(
        0xF,
        (
            "Protect the \"Magic Guards\"\x01",
            "To break through, the police patrol car\x01",
            "It is not very powerful, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Thinking of horsepower and speed,\x01",
            "Lloyd's your car is\x01",
            "I think it will be absolutely necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, I will collect it at any rate.\x02\x03",
            "#00000FTake care of your senior Kate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yeah, Lloyd and you guys as well!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_2EA4")

    label("loc_2E51")


    ChrTalk(
        0xF,
        (
            "We till the strategy\x01",
            "I will prepare for the rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Good luck with Lloyd's guys!\x02",
    )

    CloseMessageWindow()

    label("loc_2EA4")

    TalkEnd(0xFE)
    Return()

    # Function_17_2D10 end

    def Function_18_2EA8(): pass

    label("Function_18_2EA8")

    TalkBegin(0xFE)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-12940, -13300, 188130, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(
        0xC,
        (
            "If hacking to the tower succeeds\x01",
            "Communication interruption can also be canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You say you came in\x01",
            "Mercapa, was it?\x01",
            "Communication should be possible there too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm, when that happens\x01",
            "Also backing up Jonah\x01",
            "It looks like you can accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, with Jonah's cooperation\x01",
            "I bet it is hundred people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For that,\x01",
            "Anyway hacking\x01",
            "I have to make it successful! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_30B9")

    label("loc_3049")


    ChrTalk(
        0xC,
        (
            "Until hacking succeeds,\x01",
            "It will take a little more time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tio's guys also\x01",
            "Be careful ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Fade(500)
    OP_6B(0x0)
    OP_69(0xFF, 0x0)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_18_2EA8 end

    def Function_19_30CA(): pass

    label("Function_19_30CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BA")

    ChrTalk(
        0x10,
        (
            "I was in the technical department of IBC,\x01",
            "Looking at the invalid declaration during this time,\x01",
            "I ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "David's guy\x01",
            "I want to believe in Mary Bell\x01",
            "I stayed in the tower, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It has become such a thing,\x01",
            "Is it alright……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_3237")

    label("loc_31BA")


    ChrTalk(
        0x10,
        (
            "It remained in the tower\x01",
            "I wonder if David is okay ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I also fought a fight again\x01",
            "I am worried, but … Anyway,\x01",
            "I'm helping the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3237")

    TalkEnd(0xFE)
    Return()

    # Function_19_30CA end

    def Function_20_323B(): pass

    label("Function_20_323B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F1")

    ChrTalk(
        0x11,
        (
            "For now, mage guards too\x01",
            "Come in till indoors\x01",
            "It does not seem to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If this condition persists,\x01",
            "I do not know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I hope I can break through the situation soon …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_3373")

    label("loc_32F1")


    ChrTalk(
        0x11,
        (
            "By caution to go out, citizens rarely\x01",
            "Although it is indoors,\x01",
            "Although it is dangerous, there is no difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I hope I can break through the situation soon …\x02",
    )

    CloseMessageWindow()

    label("loc_3373")

    TalkEnd(0xFE)
    Return()

    # Function_20_323B end

    def Function_21_3377(): pass

    label("Function_21_3377")

    TalkBegin(0xFE)

    ChrTalk(
        0x12,
        (
            "Ha\x01",
            "I was getting nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I hope the operation will be successful, …\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3377 end

    def Function_22_33C9(): pass

    label("Function_22_33C9")

    TalkBegin(0xFE)

    ChrTalk(
        0x13,
        (
            "Magical soldier ……\x01",
            "The president wants this card\x01",
            "I have prepared it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It's awkward but …\x01",
            "There must be somehow to do it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_33C9 end

    def Function_23_343B(): pass

    label("Function_23_343B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3518")

    ChrTalk(
        0x14,
        (
            "Weapons stored in this area,\x01",
            "It is one you purchased from a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Originally it is an illegal weapon,\x01",
            "In the situation of lack of supplies\x01",
            "I can not change my belly on my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "More than anything, to that magician\x01",
            "I hope I can pass it ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_358A")

    label("loc_3518")


    ChrTalk(
        0x14,
        (
            "Weapons stored in this area,\x01",
            "It is one you purchased from a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "To that magician\x01",
            "I hope I can pass it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358A")

    TalkEnd(0xFE)
    Return()

    # Function_23_343B end

    def Function_24_358E(): pass

    label("Function_24_358E")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -8400, -8000, 606060, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2170, -8000, 595370, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 7340, -16000, 184650, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 7390, -16000, 191840, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6000, -16000, 191840, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -9560, -16000, 190630, 17)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -8410, -16000, 188790, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7350, -16000, 183270, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -6040, -16000, 175740, 135)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -520, -8000, 606410, 90)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36A4")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -6000, -8000, 595580, 0)

    label("loc_36A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36CA")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -9520, -16000, 188860, 0)

    label("loc_36CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36F0")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -5840, 0, 608620, 225)

    label("loc_36F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3747")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17080, -16000, 178000, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 45)
    Jump("loc_3773")

    label("loc_3747")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 0)

    label("loc_3773")

    Return()

    # Function_24_358E end

    def Function_25_3774(): pass

    label("Function_25_3774")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are devices that can recover the orbment.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3861")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x13, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x13, 0x0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x13)
    OP_71(0x13, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x13, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3861")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_25_3774 end

    def Function_26_3870(): pass

    label("Function_26_3870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_387A")
    Return()

    label("loc_387A")

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
            "There are monsters with a mighty power.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Exterminate】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3952"),
        (SWITCH_DEFAULT, "loc_396B"),
    )


    label("loc_3952")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -499760, 0, 494390, 0)
    EventEnd(0x5)
    Return()

    label("loc_396B")

    Battle("BattleInfo_91C", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-499760, 1000, 494390, 0)
    OP_90(0x0, -499760, 0, 494390, 0)
    OP_90(0x1, -499760, 0, 494390, 0)
    OP_90(0x2, -499760, 0, 494390, 0)
    OP_90(0x3, -499760, 0, 494390, 0)
    OP_90(0x4, -499760, 0, 494390, 0)
    OP_90(0x5, -499760, 0, 494390, 0)
    OP_90(0x6, -499760, 0, 494390, 0)
    OP_90(0x7, -499760, 0, 494390, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3A2D"),
        (1, "loc_3A32"),
        (SWITCH_DEFAULT, "loc_3A35"),
    )


    label("loc_3A2D")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3A32")

    OP_B9(0x0)
    Return()

    label("loc_3A35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x24, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exterminated monsters!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B25")
    Sound(629, 0, 100, 0)
    Sound(842, 0, 100, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I felt that tremendous power wakes up somewhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x21F, 0)

    label("loc_3B25")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_26_3870 end

    def Function_27_3B2F(): pass

    label("Function_27_3B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B41")
    Call(0, 36)
    Return()

    label("loc_3B41")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C99")
    Fade(500)
    SetChrPos(0x0, 5000, 0, 747500, 0)
    SetChrPos(0x1, 6000, 0, 747500, 0)
    SetChrPos(0x2, 5000, 0, 746500, 0)
    SetChrPos(0x3, 6000, 0, 746500, 0)
    OP_68(5230, 0, 745110, 0)
    MoveCamera(25, 57, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x12, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 762000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0309", 108, 0, 0)
    IdleLoop()

    label("loc_3C99")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_27_3B2F end

    def Function_28_3CA1(): pass

    label("Function_28_3CA1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x12, 0x64)
    Sleep(1)
    OP_68(4580, 2750, 757170, 0)
    MoveCamera(19, 37, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2750, 759000, 270)
    OP_90(0x1, 3500, 2750, 758000, 270)
    OP_90(0x2, 4500, 2750, 759000, 270)
    OP_90(0x3, 4500, 2750, 758000, 270)
    Sound(145, 0, 100, 0)
    OP_68(4030, 0, 745730, 3200)
    MoveCamera(53, 41, 0, 3200)
    OP_71(0x12, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x12)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_3CA1 end

    def Function_29_3DB0(): pass

    label("Function_29_3DB0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_3DF9")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already been switched off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3F32")

    label("loc_3DF9")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2B")
    Fade(500)
    SetChrPos(0x0, -10890, -16000, 191940, 0)
    SetChrPos(0x1, -9900, -16000, 191760, 0)
    SetChrPos(0x2, -11180, -16000, 190380, 0)
    SetChrPos(0x3, -10290, -16000, 190460, 0)
    OP_68(-12300, -13300, 188960, 0)
    MoveCamera(34, 25, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12500, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2B")
    Call(0, 32)

    label("loc_3F2B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3F32")

    Return()

    # Function_29_3DB0 end

    def Function_30_3F33(): pass

    label("Function_30_3F33")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_3F7C")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already been switched off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_40B4")

    label("loc_3F7C")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AD")
    Fade(500)
    SetChrPos(0x0, 9590, -8000, 192060, 0)
    SetChrPos(0x1, 10650, -8000, 191930, 0)
    SetChrPos(0x2, 9680, -8000, 190620, 0)
    SetChrPos(0x3, 10730, -8000, 190350, 0)
    OP_68(8740, -5300, 191340, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x8, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40AD")
    Call(0, 32)

    label("loc_40AD")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_40B4")

    Return()

    # Function_30_3F33 end

    def Function_31_40B5(): pass

    label("Function_31_40B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_40FE")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already been switched off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4236")

    label("loc_40FE")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_422F")
    Fade(500)
    SetChrPos(0x0, -15480, -8000, 191340, 45)
    SetChrPos(0x1, -16480, -8000, 191930, 45)
    SetChrPos(0x2, -16830, -8000, 190290, 45)
    SetChrPos(0x3, -17830, -8000, 190910, 45)
    OP_68(-16450, -5300, 190460, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x9, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422F")
    Call(0, 32)

    label("loc_422F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4236")

    Return()

    # Function_31_40B5 end

    def Function_32_4237(): pass

    label("Function_32_4237")

    Fade(500)
    OP_68(-3140, -13300, 193070, 0)
    MoveCamera(41, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x11, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x1, 0x1)
    OP_0D()
    Sleep(500)
    Sound(147, 0, 100, 0)
    OP_71(0x11, 0x0, 0x28, 0x0, 0x0)
    Sleep(1300)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    Return()

    # Function_32_4237 end

    def Function_33_42C3(): pass

    label("Function_33_42C3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-19510, -11300, 175870, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, -2029, -14000, 165880, 0)
    SetChrPos(0x102, -3420, -14000, 165480, 0)
    SetChrPos(0x103, -650, -14000, 165410, 0)
    SetChrPos(0x104, -2060, -14000, 164380, 0)
    SetChrPos(0x109, -3340, -14000, 164200, 0)
    SetChrPos(0x105, -820, -14000, 164140, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-1020, -11300, 176610, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_439B():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_439B)
    Sleep(50)

    def lambda_43B8():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43B8)
    Sleep(50)

    def lambda_43D5():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43D5)
    Sleep(50)

    def lambda_43F2():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43F2)
    Sleep(50)

    def lambda_440F():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_440F)
    Sleep(50)

    def lambda_442C():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_442C)
    OP_6F(0x1)
    OP_68(-4630, -11300, 167910, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(14590, 5000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#12P#00305FHmm, I went out into a very wide place.\x02\x03",
            "#00303FIn a case of a trade meeting\x01",
            "Even when I get off the Orkis Tower\x01",
            "I was surprised … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, there are places like that\x01",
            "It seems quite far apart ….\x02\x03",
            "#00006FTo the underground of the Old Town,\x01",
            "Such a vast space\x01",
            "I thought that it was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FFrom the basement of Huff and Orkis Tower\x01",
            "Before reaching the Old Town,\x01",
            "How much Mira it took.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAlso, in the story I heard before,\x01",
            "D section as a parking lot for a driven car\x01",
            "It is said that it was built … …\x02\x03",
            "#00206FAfter all, like a car\x01",
            "It is not stopped at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI see …\x02\x03",
            "#00101FEven the popular Republic of power vehicles,\x01",
            "You should not need anything so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FIn the first place, parking lots\x01",
            "Even though it is prepared in the basement of the old city,\x01",
            "It is doubtful how many people use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI have plenty of thoughts though ….\x02\x03",
            "#00000F…… Anyway arrange devils\x01",
            "I have to go get rid of it.\x02\x03",
            "Let's go to the far side.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16B, 3)
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2029, -14000, 168880, 0)
    EventEnd(0x5)
    Return()

    # Function_33_42C3 end

    def Function_34_481F(): pass

    label("Function_34_481F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9600, -16000, 190500, 0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -10400, -16000, 188100, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -11300, -16000, 189000, 0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -12500, -16000, 188600, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -10800, -16000, 190900, 0)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -12000, -16000, 190500, 0)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -13800, -16000, 189400, 45)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -13000, -16000, 190900, 45)
    OP_4B(0xE, 0xFF)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x11, 0x28)
    OP_68(12000, -14000, 182000, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-8000, -14000, 187000, 7000)
    SetCameraDistance(23000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-10900, -14500, 193200, 0)
    MoveCamera(31, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 1500)
    OP_6F(0x79)
    Sleep(500)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WI would like you to think about it together\x01",
            "To make it a chance … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S── As one of the autonomous state representatives\x01",
            "I am here \"Cross Bell Independent Country\"\x01",
            "I declare that it is invalid!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-10900, -14900, 190900, 1000)
    MoveCamera(39, 21, 0, 1000)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#11POhh! He said it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PBut, with this a little\x01",
            "It becomes easy to move …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#00604FYeah…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        (
            "#5P#00602F── Sergei.\x01",
            "The people#4RThey are#Is it cooperation?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P#01004FPowered by Translate\x01",
            "Besides that there is not it.\x02\x03",
            "#01002FWell I think we're gonna get busy now\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 6)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_481F end

    def Function_35_4D62(): pass

    label("Function_35_4D62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x101, -9300, -16000, 188800, 0)
    SetChrPos(0x102, -9600, -16000, 187300, 0)
    SetChrPos(0x103, -10400, -16000, 189000, 0)
    SetChrPos(0x104, -10700, -16000, 187500, 0)
    SetChrPos(0x109, -11900, -16000, 188000, 45)
    SetChrPos(0x105, -11600, -16000, 186800, 0)
    SetChrPos(0x106, -10000, -16000, 186000, 0)
    SetChrPos(0x10A, -6900, -16000, 189300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -7400, -16000, 188000, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6600, -16000, 190700, 225)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -7700, -16000, 190900, 225)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9600, -16000, 190500, 180)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -7100, -16000, 186600, 270)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -5800, -16000, 188300, 270)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -5800, -16000, 187200, 270)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -5250, -16000, 186150, 270)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -4460, -16000, 188480, 270)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4570, -16000, 191320, 225)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5780, -16000, 192400, 225)
    OP_4B(0x14, 0xFF)
    SetMapObjFrame(0x7, "moni_1", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x11, 0x28)
    OP_68(-10000, -14900, 189500, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day, 9: 30 -\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7566", 0)
    OP_68(-9000, -7000, 188000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-9000, -14500, 188000, 8000)
    PlaceName2(340, 40, "c_plac53", 0x0, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-10000, -14900, 189500, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(16000, 1000)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#5POh …… Tio\x01",
            "It was safe for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PBesides, Jonah is safe,\x01",
            "They were released! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PEven with this already\x01",
            "There is no reminder!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FChief, you're too emotional\x02\x03",
            "#00202FBut I'm so glad you're ok as well\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5PAhh!\x01",
            "Tio makes me safe\x01",
            "To be pleased … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMore than 100 times a day,\x01",
            "goddess#4REidos#It is worthwhile to pray to\x01",
            "It was!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FOk now you're being annoying\x02",
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
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00012FThat's right.\x01",
            "I got together so often.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8300, -15000, 188100, 1000)
    MoveCamera(39, 22, 0, 1000)
    SetCameraDistance(15600, 1000)

    def lambda_53E8():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_53E8)
    Sleep(50)

    def lambda_53F8():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53F8)
    Sleep(50)

    def lambda_5408():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5408)
    Sleep(50)

    def lambda_5418():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5418)
    Sleep(50)

    def lambda_5428():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5428)
    Sleep(50)

    def lambda_5438():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5438)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#6P#00305FAfter all, the antipathy to the president\x01",
            "Is it increasing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FOf course\x02\x03",
            "#01001FYesterday, suddenly in the whole city\x01",
            "Martial law and exclusion orders have been issued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FThen, when pale moya got on\x01",
            "If I think about that, that's it.\x02\x03",
            "#00610F… … no longer\x01",
            "It is not a situation that you can overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We don't have an arrest warrant but\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Presidential faction in the form of current criminal arrest\x01",
            "There is no choice but to press it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI agree……\x01",
            "There seems to be no way for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10113Fthat……\x01",
            "How is the safety of citizens?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFor now, for martial law and curfews\x01",
            "It seems that he is obediently obeying.\x02\x03",
            "#11PBattle is occurring outside the town\x01",
            "I wonder if it is affecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PBut, because it was sudden\x01",
            "There seems to be many citizens who are not equipped.\x02\x03",
            "#11PTo the city hall and hotel\x01",
            "Some people are evacuating\x01",
            "I guess it's pretty troubling ~ ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FWe don't have a moment to lose\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FBut the Presidential faction\x01",
            "When it stops … …\x02\x03",
            "#10401FIt is necessary to capture the Orkis Tower\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FOh, already rough arrangements\x01",
            "It is done.\x02\x03",
            "With the destroyers remaining in the city\x01",
            "It seems that we can also collaborate.\x02\x03",
            "#01002FAnd the rest of you will come\x01",
            "I was waiting for it now or now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FDirector…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FWait for me\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10701FSo, the concrete setup\x01",
            "like what……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FCurrently in front of the tower\x01",
            "A huge group of \"Magic Guards\"\x01",
            "It seems to be defending the defense.\x02\x03",
            "#00601FWith it, with all the people here\x01",
            "Strike with hawkers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In that gap, the rushing team\x01",
            "Rush into the Orkis Tower with a car ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Continue to control the tower as it is\x01",
            "It is an arrangement to start.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10112FUh… how to put it…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt is a pretty aggressive setup\x01",
            "Do you have a winning number?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FApparently most of the defense forces are\x01",
            "It seems that it has been turned outside the city.\x02\x03",
            "#01000FProbably inside the tower\x01",
            "It should be a few, including Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PRoute from the Geo Front\x01",
            "I will be blocked as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThis area can be taken at present\x01",
            "It is probably the best policy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FIn that case…\x02",
    )

    CloseMessageWindow()

    def lambda_5CB8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5CB8)

    def lambda_5CC5():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CC5)
    Sleep(30)

    def lambda_5CD5():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5CD5)
    Sleep(30)

    def lambda_5CE5():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5CE5)
    Sleep(30)

    def lambda_5CF5():
        TurnDirection(0x106, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5CF5)
    Sleep(30)

    def lambda_5D05():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D05)
    Sleep(30)

    def lambda_5D15():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5D15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1100)

    def lambda_5D3D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D3D)

    def lambda_5D4A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5D4A)
    Sleep(30)

    def lambda_5D5A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5D5A)
    Sleep(30)

    def lambda_5D6A():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5D6A)
    Sleep(30)

    def lambda_5D7A():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5D7A)
    Sleep(30)

    def lambda_5D8A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D8A)
    Sleep(30)

    def lambda_5D9A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5D9A)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00001FThat rushing team is\x01",
            "Is it already decided?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00605FNo, that's what we're doing now\x02\x03",
            "#00601FYou guys… no way\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, if possible, the rushing team\x01",
            "Please leave it to us.\x02\x03",
            "#00013FKea at the tower\x01",
            "To get back with this hand as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FOh, that's all\x01",
            "I can not yield it to other people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FIf security inside the tower\x01",
            "It will be useful if I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FMe too …… Belle and Uncle-sama\x01",
            "I would like to ask directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FOnce as a defense army to them\x01",
            "I was a compliment, but ……\x02\x03",
            "#10101FBut that's exactly why I can't hold back\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, if it were this one\x01",
            "The scene is also falling through.\x02\x03",
            "#10402FThinking about teamwork\x01",
            "I wonder if you can hit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10704FI will definitely be useful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00600FYou guys….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01004FHehe, well then\x02\x03",
            "#01002FThat hiyoko is totally\x01",
            "I got a face in front of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FDirector…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FWell, that's good.\x01",
            "Leave the in-go team to you.\x02\x03",
            "#01001FBut all the arrangements\x01",
            "It is not that it is in order.\x02\x03",
            "So we will wait a bit more\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHacking to the Orchis Tower\x01",
            "I am on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAbout an hour more\x01",
            "Access should be possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_624F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_624F)

    def lambda_625C():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_625C)
    Sleep(50)

    def lambda_626C():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_626C)
    Sleep(50)

    def lambda_627C():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_627C)
    Sleep(50)

    def lambda_628C():
        TurnDirection(0x106, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_628C)
    Sleep(50)

    def lambda_629C():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_629C)
    Sleep(50)

    def lambda_62AC():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_62AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#6P#00205FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01004FOh, that's when I get into the team\x01",
            "It will make backup easier,\x01",
            "You can also cancel communication interference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAnd also to the guilds and various directions\x01",
            "It is necessary to contact again.\x02\x03",
            "#00600FAnyway, you\x01",
            "On the premise of going to the inrush team\x01",
            "I will set the final set-up.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15850, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "The final set-up of the inrush strategy\x01",
            "After talking with Sergei … …\x02\x03",
            "To secure a guided vehicle to use for rushing\x01",
            "I decided to return to the support department building once.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -2600, -16000, 176600, 0)
    SetChrPos(0x102, -1400, -16000, 176600, 0)
    SetChrPos(0x103, -3400, -16000, 175500, 0)
    SetChrPos(0x104, -600, -16000, 175500, 0)
    SetChrPos(0x109, -2000, -16000, 175500, 0)
    SetChrPos(0x105, -2900, -16000, 174500, 0)
    SetChrPos(0x106, -1100, -16000, 174500, 0)
    SetChrPos(0x10A, -2000, -16000, 179000, 180)
    SetChrPos(0x8, -2900, -16000, 179800, 180)
    PlayBGM("ed7566", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2000, -15000, 177700, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(15000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00005F── Well then,\x01",
            "Mr. Dudley also entered the team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FOh, at the security of the trade council\x01",
            "Also in the structure of Orkis Tower\x01",
            "You know, I know.\x02\x03",
            "#00600FIf you go down the urban area\x01",
            "I will be able to guide you to a certain extent.\x02\x03",
            "#00607FMoreover, if it becomes arrest of the president\x01",
            "Please leave it to the support section only!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FOh this again\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00204FWe already promised\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FEheh, but it saves us\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FWell, to use for inrush\x01",
            "Although it is a driving car … ….\x02\x03",
            "#10100FWe really are gonna use the SSS car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5POh, the best at the moment,\x01",
            "Both horsepower and speed\x01",
            "It's a car type that has both sides.\x02\x03",
            "#01002FTo break through the city area\x01",
            "Just hit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FThat's true…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FWell if you remain in the support section\x01",
            "There is no hand to not use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708Fbut……\x01",
            "As you move through the city area with this number\x01",
            "It looks prominent as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FThen join the accompanying members\x01",
            "Please narrow down.\x02\x03",
            "#00600FOther people are here\x01",
            "It would be good if you wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FUnderstood\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dudley joined the party\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69B9")
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)
    Jump("loc_69C1")

    label("loc_69B9")

    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x196)

    label("loc_69C1")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Dudley Combi Craft\x01\x07\x02",
            "\"Hearts of Iron\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By consuming CP by 100\x01",
            "A powerful combination attack can be launched.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    SetScenarioFlags(0x27, 1)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    SetChrPos(0x0, -1020, -16000, 175200, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    Call(0, 24)
    SetScenarioFlags(0x1A5, 3)
    OP_29(0xB1, 0x1, 0x7)
    ClearScenarioFlags(0x20, 5)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7573")
    ReplaceBGM("ed7101", "ed7573")
    ReplaceBGM("ed7116", "ed7573")
    ReplaceBGM("ed7117", "ed7573")
    ReplaceBGM("ed7111", "ed7573")
    ReplaceBGM("ed7113", "ed7573")
    EventEnd(0x5)
    Return()

    # Function_35_4D62 end

    def Function_36_6B56(): pass

    label("Function_36_6B56")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The power seems to be falling.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA2")

    ChrTalk(
        0x101,
        "#00003F…… It seems not to move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThe future is at the base of the Orkis Tower\x01",
            "It should be connected … …\x02\x03",
            "#00103FPerhaps the presidents\x01",
            "I wonder if it is stopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FIndeed, it seems possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FFrom the Geo Front\x01",
            "What breaks into the tower\x01",
            "You seemed better to give up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_6CA2")

    TalkEnd(0xFF)
    Return()

    # Function_36_6B56 end

    SaveToFile()

Try(main)
