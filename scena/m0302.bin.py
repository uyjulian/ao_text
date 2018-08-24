from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Chief Sergei",           # 1
        "Detective Dudley",       # 2
        "Detective Raymond",      # 3
        "Detective Emma",         # 4
        "Chief Roberts",          # 5
        "Receptionist Rebecca",   # 6
        "Section Chief Joe Ridge",# 7
        "Head Patrol Officer Kate",# 8
        "Researcher Clay",        # 9
        "Policeman",              # 10
        "Policeman",              # 11
        "Detective",              # 12
        "Detective",              # 13
        "Noｱl",                  # 14
        "Wazy",                   # 15
        "Rixia",                  # 16
        "トライアタッカーＲⅡ",   # 17
        "bm0300",                 # 18
        "bm0300",                 # 19
        "bm0300",                 # 20
        "bm0300",                 # 21
        "bm0300",                 # 22
    ))

    ATBonus("ATBonus_604", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_624", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_74AF", 5,   5,   5,   5,   10,  0,   0)

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
        "BattleInfo_704", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_74AF", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7A0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_74AF", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_74AF", 35, 35, 30, 0,
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
        "Function_6_1517",         # 06, 6
        "Function_7_1668",         # 07, 7
        "Function_8_17D1",         # 08, 8
        "Function_9_1A92",         # 09, 9
        "Function_10_1CAA",        # 0A, 10
        "Function_11_1F13",        # 0B, 11
        "Function_12_2257",        # 0C, 12
        "Function_13_262F",        # 0D, 13
        "Function_14_2851",        # 0E, 14
        "Function_15_2A65",        # 0F, 15
        "Function_16_2D28",        # 10, 16
        "Function_17_2ED0",        # 11, 17
        "Function_18_3097",        # 12, 18
        "Function_19_3315",        # 13, 19
        "Function_20_34E0",        # 14, 20
        "Function_21_3648",        # 15, 21
        "Function_22_36A6",        # 16, 22
        "Function_23_373C",        # 17, 23
        "Function_24_38E7",        # 18, 24
        "Function_25_3ACD",        # 19, 25
        "Function_26_3BC1",        # 1A, 26
        "Function_27_3E94",        # 1B, 27
        "Function_28_3FF9",        # 1C, 28
        "Function_29_4108",        # 1D, 29
        "Function_30_4278",        # 1E, 30
        "Function_31_43E7",        # 1F, 31
        "Function_32_4556",        # 20, 32
        "Function_33_45E2",        # 21, 33
        "Function_34_4BCC",        # 22, 34
        "Function_35_5190",        # 23, 35
        "Function_36_730A",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A7")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1230")
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
    SetScenarioFlags(0x1F0, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_12A2")

    label("loc_1230")

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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A2")

    Jump("loc_12F0")

    label("loc_12A7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FF")
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
            "Monsters appeared!\x07\x00\x02",
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
        (0, "loc_13E0"),
        (2, "loc_13EF"),
        (1, "loc_13FC"),
        (SWITCH_DEFAULT, "loc_13FF"),
    )


    label("loc_13E0")

    SetScenarioFlags(0x217, 1)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_13FF")

    label("loc_13EF")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13FC")

    OP_B9(0x0)
    Return()

    label("loc_13FF")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7E, 1)"), scpexpr(EXPR_END)), "loc_1458")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14C8")

    Jump("loc_150B")

    label("loc_14CD")

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

    label("loc_150B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12FC end

    def Function_6_1517(): pass

    label("Function_6_1517")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1613")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_159C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_160E")

    Jump("loc_165C")

    label("loc_1613")

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

    label("loc_165C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1517 end

    def Function_7_1668(): pass

    label("Function_7_1668")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A1")
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
            "#56I Earth Sepith  x80\x01\x07\x02",
            "#57I Water Sepith  x80\x01\x07\x02",
            "#58I Fire Sepith   x80\x01\x07\x02",
            "#59I Wind Sepith   x80\x01\x07\x02",
            "#60I Time Sepith   x80\x01\x07\x02",
            "#61I Space Sepith  x80\x01\x07\x02",
            "#62I Mirage Sepith x80\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_17BF")

    label("loc_17A1")


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

    label("loc_17BF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1668 end

    def Function_8_17D1(): pass

    label("Function_8_17D1")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1994")

    ChrTalk(
        0x15,
        (
            "#10103FInfiltrating Orchis\x01",
            "Tower... I expect quite\x01",
            "the tough fight.\x02\x03",
            "#10101FOnce the operation starts,\x01",
            "I it'll be probably\x01",
            "difficult to return...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're right... We don't\x01",
            "know what will happen. We\x01",
            "have to be fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#10100FSince we have time now,\x01",
            "maybe we should visit\x01",
            "the city facilities.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A28")

    label("loc_1994")


    ChrTalk(
        0x15,
        (
            "#10103FInfiltrating Orchis\x01",
            "Tower... I expect quite\x01",
            "the tough fight.\x02\x03",
            "#10100FSince we have time now,\x01",
            "maybe we should visit\x01",
            "the city facilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A28")

    Jump("loc_1A89")

    label("loc_1A2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A89")

    ChrTalk(
        0x15,
        (
            "#10100FForming the party,\x01",
            "right? Roger that!\x02",
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
    Jump("loc_1A89")

    label("loc_1A89")

    Jump("loc_17DE")

    label("loc_1A8E")

    TalkEnd(0xFE)
    Return()

    # Function_8_17D1 end

    def Function_9_1A92(): pass

    label("Function_9_1A92")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9F")

    ChrTalk(
        0x16,
        (
            "#10403F...Come to think of it,\x01",
            "the exit of this place\x01",
            "is right in Downtown.\x02\x03",
            "#10402FHehe. Since we're here,\x01",
            "why don't we visit\x01",
            "Trinity?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C45")

    label("loc_1B9F")


    ChrTalk(
        0x16,
        (
            "#10404FLeaving Downtown to the\x01",
            "Testaments will probably\x01",
            "be fine.\x02\x03",
            "#10400FWe should focus on the\x01",
            "operation, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C45")

    ChrTalk(
        0x101,
        "#00000FYeah... You're right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C45")

    Jump("loc_1CA1")

    label("loc_1C4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA1")

    ChrTalk(
        0x16,
        (
            "#10400FHehe. Are you switching\x01",
            "members?\x02",
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
    Jump("loc_1CA1")

    label("loc_1CA1")

    Jump("loc_1A9F")

    label("loc_1CA6")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A92 end

    def Function_10_1CAA(): pass

    label("Function_10_1CAA")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E76")

    ChrTalk(
        0x101,
        (
            "#00005FSo that's where you\x01",
            "were, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#10702FYes... I was thinking of\x01",
            "raising my qi in a quiet place\x01",
            "until the operation begins.\x02\x03",
            "#10703FBloody Shirley is probably\x01",
            "there, at Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FYeah... The same as uncle and\x01",
            "the others, she'll likely\x01",
            "come to block our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#10701FI won't lose, not ever.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EB4")

    label("loc_1E76")


    ChrTalk(
        0x17,
        (
            "#10703FBloody Shirley...\x02\x03",
            "#10701FI won't lose, not ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB4")

    Jump("loc_1F0A")

    label("loc_1EB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0A")

    ChrTalk(
        0x17,
        (
            "#10700FYes, let's change\x01",
            "members.\x02",
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
    Jump("loc_1F0A")

    label("loc_1F0A")

    Jump("loc_1CB7")

    label("loc_1F0F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CAA end

    def Function_11_1F13(): pass

    label("Function_11_1F13")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2253")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(
        0x9,
        (
            "#00603FI'll accompany you\x01",
            "during the infiltration\x01",
            "operation as well.\x02\x03",
            "#00600FPrepare yourselves\x01",
            "thoroughly now, while\x01",
            "you have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it will be\x01",
            "reassuring having you with\x01",
            "us, Detective Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00603FI can't leave the President's\x01",
            "arrest to the Support Section\x01",
            "alone... That's all it is.\x02\x03",
            "#00600FIf you understand, then let's\x01",
            "go at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21D8")

    label("loc_212A")


    ChrTalk(
        0x9,
        (
            "#00603FThe arrest of the President...\x01",
            "You should understand as well\x01",
            "that it's harder done than said.\x02\x03",
            "#00600FPrepare yourselves thoroughly\x01",
            "now, while you have the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D8")

    Jump("loc_224E")

    label("loc_21DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224E")

    ChrTalk(
        0x9,
        (
            "#00600FYou're changing the\x01",
            "party? ...Hurry up and\x01",
            "choose already.\x02",
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
    Jump("loc_224E")

    label("loc_224E")

    Jump("loc_1F20")

    label("loc_2253")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F13 end

    def Function_12_2257(): pass

    label("Function_12_2257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2471")

    ChrTalk(
        0x8,
        (
            "#01002FHehe. Nevertheless...\x01",
            "I'm glad you're all\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYou too Chief... Thank\x01",
            "goodness you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou've been in the city\x01",
            "acting in secret this\x01",
            "whole time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FYeah, we've been based here for a\x01",
            "while, trying to find a way out\x01",
            "of this mess, but...\x02\x03",
            "#01001FAfter the situation became like\x01",
            "this, we don't even have the time\x01",
            "to do that at leisure anymore.\x02\x03",
            "You have to make this operation\x01",
            "succeed at all costs. ...To take\x01",
            "back KeA as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes... Please leave it\x01",
            "to us!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 4)
    Jump("loc_262B")

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259D")

    ChrTalk(
        0x8,
        (
            "#01003FAfter the situation became\x01",
            "like this, we don't have time\x01",
            "to act at leisure anymore.\x02\x03",
            "#01001FYou'll have to make the Orchis\x01",
            "Tower infiltration operation\x01",
            "succeed at all costs.\x02\x03",
            "#01002FFor the citizens... But most\x01",
            "of all, for yourselves and KeA\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_262B")

    label("loc_259D")


    ChrTalk(
        0x8,
        (
            "#01004FI'll do maintenance on the\x01",
            "shotguns too.\x02\x03",
            "#01001FThe Orchis Tower infiltration\x01",
            "operation... We'll make it\x01",
            "succeed no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262B")

    TalkEnd(0xFE)
    Return()

    # Function_12_2257 end

    def Function_13_262F(): pass

    label("Function_13_262F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B7")

    ChrTalk(
        0xA,
        (
            "Well then, until the\x01",
            "operation begins, I'll\x01",
            "have to check our weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...By the way, it seems\x01",
            "you met Inspector Donovan\x01",
            "at the hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "How was he doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHis wife was nursing him and\x01",
            "it looked like he had almost\x01",
            "made a full recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, that's good to\x01",
            "hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With the inspector away,\x01",
            "we've each got to do\x01",
            "what we can, don't we.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_284D")

    label("loc_27B7")


    ChrTalk(
        0xA,
        (
            "Well then, until the\x01",
            "operation begins, I'll\x01",
            "have to check our weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With the inspector away,\x01",
            "we've each got to do\x01",
            "what we can, don't we.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284D")

    TalkEnd(0xFE)
    Return()

    # Function_13_262F end

    def Function_14_2851(): pass

    label("Function_14_2851")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A1")

    ChrTalk(
        0xD,
        (
            "When the infiltration operation\x01",
            "begins, we need to make citizen\x01",
            "safety our top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm not cut out for combat, so I\x01",
            "want to act as an evacuation guide\x01",
            "to keep damage to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEven that role is\x01",
            "important...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe'll be careful, but...\x01",
            "Please, take care of\x01",
            "yourself as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A61")

    label("loc_29A1")


    ChrTalk(
        0xD,
        (
            "I'm not cut out for combat, so I\x01",
            "want to act as an evacuation guide\x01",
            "to keep damage to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if the situation is like\x01",
            "this, we need to make citizen\x01",
            "safety our top priority.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    TalkEnd(0xFE)
    Return()

    # Function_14_2851 end

    def Function_15_2A65(): pass

    label("Function_15_2A65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B51")
    TurnDirection(0xB, 0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#00603FEmma, I leave this place to\x01",
            "you.\x02\x03",
            "#00600FSo as not to hinder the\x01",
            "operation, keep a close eye\x01",
            "on our base for me, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, understood. ...Mr.\x01",
            "Dudley, be careful as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2B98")

    label("loc_2B51")


    ChrTalk(
        0xB,
        (
            "Please leave this place\x01",
            "to us. ...Mr. Dudley, be\x01",
            "careful as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B98")

    Jump("loc_2D24")

    label("loc_2B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CBF")

    ChrTalk(
        0xB,
        (
            "I was just reviewing the\x01",
            "plans for the operation\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You all have memorized\x01",
            "how it's going to go,\x01",
            "haven't you?\x02",
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
        "...Good then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The success of the\x01",
            "operation rests on your\x01",
            "shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do not neglect careful\x01",
            "preparations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2D24")

    label("loc_2CBF")


    ChrTalk(
        0xB,
        (
            "The success of the\x01",
            "operation rests on your\x01",
            "shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do not neglect careful\x01",
            "preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D24")

    TalkEnd(0xFE)
    Return()

    # Function_15_2A65 end

    def Function_16_2D28(): pass

    label("Function_16_2D28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E66")

    ChrTalk(
        0xE,
        (
            "After the declaration of invalidity,\x01",
            "officers collaborating with us at HQ\x01",
            "have gathered little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Frantz volunteered to be\x01",
            "the liaison with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FFrantz did...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, everyone's doing\x01",
            "their best to protect\x01",
            "their pride as policemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You all do your best\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2ECC")

    label("loc_2E66")


    ChrTalk(
        0xE,
        (
            "Everyone is doing their\x01",
            "best to protect their\x01",
            "pride as policemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You all do your best\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ECC")

    TalkEnd(0xFE)
    Return()

    # Function_16_2D28 end

    def Function_17_2ED0(): pass

    label("Function_17_2ED0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302C")

    ChrTalk(
        0xF,
        (
            "Our patrol cars totally lack the\x01",
            "necessary power to break through\x01",
            "their "magic soldier" defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Taking into consideration\x01",
            "horsepower and speed, your car\x01",
            "will absolutely be needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FRight. We'll recover it\x01",
            "no matter what.\x02\x03",
            "#00000FOfficer Kate, you be\x01",
            "careful as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Right. Do your best too,\x01",
            "Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_3093")

    label("loc_302C")


    ChrTalk(
        0xF,
        (
            "We'll be preparing for\x01",
            "the infiltration until\x01",
            "the operation starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Do your best too, Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_3093")

    TalkEnd(0xFE)
    Return()

    # Function_17_2ED0 end

    def Function_18_3097(): pass

    label("Function_18_3097")

    TalkBegin(0xFE)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-12940, -13300, 188130, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3285")

    ChrTalk(
        0xC,
        (
            "If the tower hacking\x01",
            "succeeds, we can release\x01",
            "the communications jamming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That thing you were riding... The\x01",
            "Merkabah, was it called? It might be\x01",
            "possible to communicate with that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes. In that case, Jona\x01",
            "will be able to back us\x01",
            "up as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, having Jona's\x01",
            "cooperation would be a\x01",
            "tremendous help for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For that reason too, I\x01",
            "have to make the hacking\x01",
            "succeed no matter what!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3304")

    label("loc_3285")


    ChrTalk(
        0xC,
        (
            "It seems that it's going to\x01",
            "take a little more time\x01",
            "until the hacking succeeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tio and everyone, please\x01",
            "be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3304")

    Fade(500)
    OP_6B(0x0)
    OP_69(0xFF, 0x0)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_18_3097 end

    def Function_19_3315(): pass

    label("Function_19_3315")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3428")

    ChrTalk(
        0x10,
        (
            "I was at the IBC Technology\x01",
            "Department, but considering the recent\x01",
            "declaration of invalidity, I fled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "David said he wanted to\x01",
            "trust in Lady Mariabell and\x01",
            "remained in the tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "With the situation like\x01",
            "this, I wonder if he's\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_34DC")

    label("loc_3428")


    ChrTalk(
        0x10,
        (
            "David stayed in the\x01",
            "tower. I wonder if he's\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm worried about him. We quarreled\x01",
            "right before we split up... At any rate,\x01",
            "now I've got to help Chief Roberts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DC")

    TalkEnd(0xFE)
    Return()

    # Function_19_3315 end

    def Function_20_34E0(): pass

    label("Function_20_34E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AD")

    ChrTalk(
        0x11,
        (
            "At present, it appears\x01",
            "the magic soldiers aren't\x01",
            "entering buildings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "But I don't know what\x01",
            "will happen if this\x01",
            "situation drags on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I hope this deadlock\x01",
            "breaks soon...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_3644")

    label("loc_35AD")


    ChrTalk(
        0x11,
        (
            "Although most citizens are indoors\x01",
            "due to the curfew order, there's no\x01",
            "doubt the situation is dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I hope this deadlock\x01",
            "breaks soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3644")

    TalkEnd(0xFE)
    Return()

    # Function_20_34E0 end

    def Function_21_3648(): pass

    label("Function_21_3648")

    TalkBegin(0xFE)

    ChrTalk(
        0x12,
        (
            "*sigh*... I'm totally\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I hope the infiltration\x01",
            "operation succeeds...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3648 end

    def Function_22_36A6(): pass

    label("Function_22_36A6")

    TalkBegin(0xFE)

    ChrTalk(
        0x13,
        (
            "Magic soldiers, huh? To\x01",
            "think the President had\x01",
            "this card up his sleeve...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "They're troublesome,\x01",
            "but... We'll have to\x01",
            "manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_36A6 end

    def Function_23_373C(): pass

    label("Function_23_373C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3859")

    ChrTalk(
        0x14,
        (
            "The weapons stored in\x01",
            "this area were obtained\x01",
            "through a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "They'd normally be illegal weapons,\x01",
            "but in a situation where supplies\x01",
            "are lacking, we do what we must.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Most importantly, I hope\x01",
            "they're effective against\x01",
            "those magic soldiers...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_38E3")

    label("loc_3859")


    ChrTalk(
        0x14,
        (
            "The weapons stored in\x01",
            "this area were obtained\x01",
            "through a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I hope they're effective\x01",
            "against those magic\x01",
            "soldiers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E3")

    TalkEnd(0xFE)
    Return()

    # Function_23_373C end

    def Function_24_38E7(): pass

    label("Function_24_38E7")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_39FD")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -6000, -8000, 595580, 0)

    label("loc_39FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3A23")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -9520, -16000, 188860, 0)

    label("loc_3A23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3A49")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -5840, 0, 608620, 225)

    label("loc_3A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3AA0")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17080, -16000, 178000, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 45)
    Jump("loc_3ACC")

    label("loc_3AA0")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 0)

    label("loc_3ACC")

    Return()

    # Function_24_38E7 end

    def Function_25_3ACD(): pass

    label("Function_25_3ACD")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB2")
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

    label("loc_3BB2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_25_3ACD end

    def Function_26_3BC1(): pass

    label("Function_26_3BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_3BCB")
    Return()

    label("loc_3BCB")

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
            "There is a monster\x01",
            "harboring an enormous\x01",
            "power.\x02",
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
        (1, "loc_3CB5"),
        (SWITCH_DEFAULT, "loc_3CCE"),
    )


    label("loc_3CB5")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -499760, 0, 494390, 0)
    EventEnd(0x5)
    Return()

    label("loc_3CCE")

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
        (2, "loc_3D90"),
        (1, "loc_3D95"),
        (SWITCH_DEFAULT, "loc_3D98"),
    )


    label("loc_3D90")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3D95")

    OP_B9(0x0)
    Return()

    label("loc_3D98")

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
            "Monster defeated!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8A")
    Sound(629, 0, 100, 0)
    Sound(842, 0, 100, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You felt an\x01",
            "extraordinary power\x01",
            "awaken somewhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x21F, 0)

    label("loc_3E8A")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_26_3BC1 end

    def Function_27_3E94(): pass

    label("Function_27_3E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA6")
    Call(0, 36)
    Return()

    label("loc_3EA6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF1")
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

    label("loc_3FF1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_27_3E94 end

    def Function_28_3FF9(): pass

    label("Function_28_3FF9")

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

    # Function_28_3FF9 end

    def Function_29_4108(): pass

    label("Function_29_4108")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_414D")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4277")

    label("loc_414D")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a switch. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4270")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4270")
    Call(0, 32)

    label("loc_4270")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4277")

    Return()

    # Function_29_4108 end

    def Function_30_4278(): pass

    label("Function_30_4278")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_42BD")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_43E6")

    label("loc_42BD")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a switch. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DF")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43DF")
    Call(0, 32)

    label("loc_43DF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_43E6")

    Return()

    # Function_30_4278 end

    def Function_31_43E7(): pass

    label("Function_31_43E7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_442C")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4555")

    label("loc_442C")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a switch. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454E")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454E")
    Call(0, 32)

    label("loc_454E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4555")

    Return()

    # Function_31_43E7 end

    def Function_32_4556(): pass

    label("Function_32_4556")

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

    # Function_32_4556 end

    def Function_33_45E2(): pass

    label("Function_33_45E2")

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

    def lambda_46BA():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46BA)
    Sleep(50)

    def lambda_46D7():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46D7)
    Sleep(50)

    def lambda_46F4():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_46F4)
    Sleep(50)

    def lambda_4711():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4711)
    Sleep(50)

    def lambda_472E():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_472E)
    Sleep(50)

    def lambda_474B():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_474B)
    OP_6F(0x1)
    OP_68(-4630, -11300, 167910, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(14590, 5000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#12P#00305FHmm, we came out into a friggin'\x01",
            "big place, huh?\x02\x03",
            "#00303FI was shocked too when we\x01",
            "descended Orchis Tower during the\x01",
            "trade conference incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. Looks like we're\x01",
            "pretty far away from there,\x01",
            "though...\x02\x03",
            "#00006FIt's hard to believe such a\x01",
            "large area was constructed\x01",
            "even under Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Who knows how much mira\x01",
            "it took to get all the way here\x01",
            "from Orchis Tower's basement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnd according to what I've heard,\x01",
            "D-Division was constructed as an\x01",
            "underground parking lot...\x02\x03",
            "#00206FBut as you can see, there's not a\x01",
            "single car to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FRight...\x02\x03",
            "#00101FEven in the Republic, where orbal\x01",
            "cars are popular, there would be\x01",
            "no need for a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FEven if there was a parking lot\x01",
            "beneath Downtown, I question how\x01",
            "many people would actually use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWe could think any\x01",
            "number of things about\x01",
            "it, but...\x02\x03",
            "#00000FIn any case, we have to\x01",
            "go exterminate that\x01",
            "wanted monster.\x02\x03",
            "Let's try proceeding\x01",
            "further inside.\x02",
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

    # Function_33_45E2 end

    def Function_34_4BCC(): pass

    label("Function_34_4BCC")

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
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WAfter having had an\x01",
            "opportunity to think about\x01",
            "it together with everyone...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S─As a representative of the autonomous\x01",
            "state, I hereby declare the invalidity\x01",
            "of the "Independent State of Crossbell"!\x07\x00\x02",
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
        (
            "#11POhh, he actually said\x01",
            "that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PB-But now it'll become a\x01",
            "little easier for us to\x01",
            "move forward...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#00604FYeah...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        (
            "#5P#00602F─Sergei. I guess those\x01",
            "kids of yours have\x01",
            "something to do with this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P#01004FHehe... There's no one\x01",
            "else it could be.\x02\x03",
            "#01002FWell then─ It looks like\x01",
            "we've got our work cut\x01",
            "out for us.\x02",
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

    # Function_34_4BCC end

    def Function_35_5190(): pass

    label("Function_35_5190")

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
            "#1KSame day, 9:30─\x02",
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
            "#5PAah... Tio, you're\x01",
            "okay!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PJona has been freed too,\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PN-Now I have no more\x01",
            "regrets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FChief... You're way too\x01",
            "emotional.\x02\x03",
            "#00202FBut I'm glad you're\x01",
            "doing well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5PAah! To think that even\x01",
            "Tio appreciates my well-\x01",
            "being!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt was worth offering\x01",
            "over a hundred prayers\x01",
            "each day to the Goddess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FOkay, now you're just\x01",
            "being annoying.\x02",
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
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00012FI-in any case, it's\x01",
            "great you were able to\x01",
            "gather this many people.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8300, -15000, 188100, 1000)
    MoveCamera(39, 22, 0, 1000)
    SetCameraDistance(15600, 1000)

    def lambda_581B():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_581B)
    Sleep(50)

    def lambda_582B():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_582B)
    Sleep(50)

    def lambda_583B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_583B)
    Sleep(50)

    def lambda_584B():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_584B)
    Sleep(50)

    def lambda_585B():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_585B)
    Sleep(50)

    def lambda_586B():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_586B)
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
            "#6P#00305FSo the animosity towards\x01",
            "the President is as high\x01",
            "as we thought?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FWell, that much goes\x01",
            "without saying.\x02\x03",
            "#01001FHe suddenly issued martial\x01",
            "law and a curfew orders for\x01",
            "the entire city yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAfter that, a bluish\x01",
            "mist enshrouded\x01",
            "everything.\x02\x03",
            "#00610F...It's a situation we\x01",
            "absolutely can't\x01",
            "overlook any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We can't issue an arrest\x01",
            "warrant, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We'll have to attempt to\x01",
            "catch him red handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThat's true... There\x01",
            "really doesn't seem to\x01",
            "be any other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10113FUhmm... What about the\x01",
            "safety of the civilians?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFor now, it seems they are all\x01",
            "obediently following the martial\x01",
            "law.\x02\x03",
            "#11PI think that the battles outside\x01",
            "the city have had an influence\x01",
            "on their actions as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PBut because it was so sudden,\x01",
            "many are not prepared.\x02\x03",
            "#11PThere are many staying in hotels\x01",
            "or the meeting hall. They seem\x01",
            "quite troubled by this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FWe have no time to\x01",
            "waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FBut if we want to pin\x01",
            "down the President's\x01",
            "faction...\x02\x03",
            "#10401FWe'll have to capture\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FYeah. We already have a\x01",
            "rough plan worked out.\x02\x03",
            "The bracers remaining in\x01",
            "the city will lend their\x01",
            "support as well.\x02\x03",
            "#01002FWe were all eagerly\x01",
            "waiting for you guys to\x01",
            "somehow show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FThank you for waiting\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10701FSo, what kind of plan is\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FRight now, it appears that a large pack\x01",
            "of those "magic soldiers" are fortifying\x01",
            "the defenses in front of the tower.\x02\x03",
            "#00601FWe'll assault them with all the\x01",
            "personnel here and the bracers as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Through the gap that creates, the\x01",
            "infiltration team will charge\x01",
            "into the tower with a vehicle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "From there, we'll gain\x01",
            "control of the tower.\x01",
            "That's the plan.\x02",
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
        (
            "#6P#10112FUmm... I don't know what\x01",
            "to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt's quite the forceful\x01",
            "plan, but can we really\x01",
            "pull it off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FIt seems that hardly any\x01",
            "State Guard are\x01",
            "patrolling the city.\x02\x03",
            "#01000FThere should be only a\x01",
            "few members inside the\x01",
            "tower besides Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAs always, the route to\x01",
            "the tower through the\x01",
            "Geofront is sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThis is most likely the\x01",
            "best plan for the\x01",
            "current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FIn that case...\x02",
    )

    CloseMessageWindow()

    def lambda_6227():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6227)

    def lambda_6234():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6234)
    Sleep(30)

    def lambda_6244():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6244)
    Sleep(30)

    def lambda_6254():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6254)
    Sleep(30)

    def lambda_6264():
        TurnDirection(0x106, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6264)
    Sleep(30)

    def lambda_6274():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6274)
    Sleep(30)

    def lambda_6284():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6284)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1100)

    def lambda_62AC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62AC)

    def lambda_62B9():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_62B9)
    Sleep(30)

    def lambda_62C9():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_62C9)
    Sleep(30)

    def lambda_62D9():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_62D9)
    Sleep(30)

    def lambda_62E9():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_62E9)
    Sleep(30)

    def lambda_62F9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_62F9)
    Sleep(30)

    def lambda_6309():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6309)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00001FHave the members of the\x01",
            "infiltration team been\x01",
            "decided yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00605FNo, we were just...\x02\x03",
            "#00601F─Wait, don't tell me\x01",
            "that you guys plan to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, please leave the\x01",
            "infiltration to us, if\x01",
            "possible.\x02\x03",
            "#00013FIt's also to take KeA\x01",
            "back from the tower with\x01",
            "our own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, I won't hand that\x01",
            "privilege to anyone\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FIf I'm there, security\x01",
            "inside the tower\x01",
            "shouldn't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI want to go too. I have\x01",
            "things I need to ask to\x01",
            "Bell and "uncle".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI was once on their side\x01",
            "as a State Guardsman,\x01",
            "so...\x02\x03",
            "#10101FThat's why I can't let\x01",
            "them get away with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10404FWith members like these,\x01",
            "we could take on the\x01",
            "world.\x02\x03",
            "#10402FI guess we're the most\x01",
            "suitable when it comes to\x01",
            "teamwork, dontcha think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10704FI'll be sure to make\x01",
            "myself useful as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00600FYou guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01004FHaha, there they go.\x02\x03",
            "#01002FMy little rookies are\x01",
            "all grown up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FWell, all right. I'll\x01",
            "let you guys act as the\x01",
            "infiltration team.\x02\x03",
            "#01001FStill, it doesn't mean\x01",
            "that the entire plan is\x01",
            "ready yet.\x02\x03",
            "I'll need you to wait a\x01",
            "little bit longer.\x02",
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
            "#5PWe're currently\x01",
            "proceeding with the\x01",
            "Orchis Tower hacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIn about another hour,\x01",
            "access should be\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6864():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6864)

    def lambda_6871():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6871)
    Sleep(50)

    def lambda_6881():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6881)
    Sleep(50)

    def lambda_6891():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6891)
    Sleep(50)

    def lambda_68A1():
        TurnDirection(0x106, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_68A1)
    Sleep(50)

    def lambda_68B1():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_68B1)
    Sleep(50)

    def lambda_68C1():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_68C1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#6P#00205FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FSeriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01004FYeah. Providing backup for the infiltration\x01",
            "team will be easier, since getting rid of\x01",
            "the interference that prevents\x01",
            "transmissions will be possible as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAlso, we need to contact the guild and\x01",
            "all other groups once again.\x02\x03",
            "#00600FAt any rate, we'll work out the\x01",
            "definitive plan considering that the job\x01",
            "of infiltration is up to all of you.\x02",
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
            "Then, after Lloyd and co. talked with\x01",
            "Sergei and the others and worked out the\x01",
            "details of the infiltration operation...\x02\x03",
            "They decided to go back to the Support\x01",
            "Section building to retrieve their orbal\x01",
            "car for use in the plan.\x07\x00\x02",
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
            "#12P#00005F─So, Mr. Dudley, you'll\x01",
            "be on the infiltration\x01",
            "team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FYeah. Due to my participation in trade\x01",
            "conference security, I know the Orchis\x01",
            "Tower blueprints inside and out as well.\x02\x03",
            "#00600FI can even guide you to a certain\x01",
            "degree, since we're going through city\x01",
            "areas.\x02\x03",
            "#00607FAlso, when the President's arrest\x01",
            "happens, I can't entrust that to the\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FBoy oh boy. That again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00204FWe promised already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, but you'll be\x01",
            "a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FUhmm, about the orbal\x01",
            "car we'll use for the\x01",
            "infiltration...\x02\x03",
            "#10100FAre we really using the\x01",
            "Support Section's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PYeah. Right now, it's\x01",
            "the model with the best\x01",
            "speed and horsepower.\x02\x03",
            "#01002FIt's the ideal way to\x01",
            "force our way through\x01",
            "the city areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FWell, it won't be of any\x01",
            "use if we just leave it\x01",
            "at the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FHowever... Moving with these\x01",
            "numbers throughout the city is\x01",
            "going to make us stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FThen, let's take only\x01",
            "the members who we've\x01",
            "decided to go with.\x02\x03",
            "#00600FThe others will stay\x01",
            "here on standby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FUnderstood.\x02",
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
            "Dudley has joined the\x01",
            "party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7174")
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)
    Jump("loc_717C")

    label("loc_7174")

    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x196)

    label("loc_717C")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Dudley have learned the \x01\x07\x02",
            ""Hearts of Iron"\x07\x05",
            " Combi Craft.\x02",
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

    # Function_35_5190 end

    def Function_36_730A(): pass

    label("Function_36_730A")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears that the\x01",
            "orbal energy is down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7483")

    ChrTalk(
        0x101,
        (
            "#00003F...Looks like it won't\x01",
            "move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThis path should\x01",
            "connected to the base of\x01",
            "Orchis Tower...\x02\x03",
            "#00103FMaybe the President and\x01",
            "the others shut it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI see, that's a\x01",
            "possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt seems we should give up\x01",
            "on the idea of infiltrating\x01",
            "the tower from the Geofront.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_7483")

    TalkEnd(0xFF)
    Return()

    # Function_36_730A end

    SaveToFile()

Try(main)
