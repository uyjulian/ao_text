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

    Sepith("Sepith_755F", 5,   5,   5,   5,   10,  0,   0)

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
        "BattleInfo_704", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_755F", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7A0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_755F", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_755F", 35, 35, 30, 0,
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
        "Function_5_12FD",         # 05, 5
        "Function_6_1519",         # 06, 6
        "Function_7_166B",         # 07, 7
        "Function_8_17C5",         # 08, 8
        "Function_9_1ABA",         # 09, 9
        "Function_10_1CE7",        # 0A, 10
        "Function_11_1F63",        # 0B, 11
        "Function_12_2296",        # 0C, 12
        "Function_13_2669",        # 0D, 13
        "Function_14_289A",        # 0E, 14
        "Function_15_2AFF",        # 0F, 15
        "Function_16_2DB9",        # 10, 16
        "Function_17_2F6D",        # 11, 17
        "Function_18_3130",        # 12, 18
        "Function_19_339F",        # 13, 19
        "Function_20_3577",        # 14, 20
        "Function_21_36EB",        # 15, 21
        "Function_22_374A",        # 16, 22
        "Function_23_37DE",        # 17, 23
        "Function_24_3991",        # 18, 24
        "Function_25_3B77",        # 19, 25
        "Function_26_3C6D",        # 1A, 26
        "Function_27_3F3E",        # 1B, 27
        "Function_28_40AA",        # 1C, 28
        "Function_29_41B9",        # 1D, 29
        "Function_30_4330",        # 1E, 30
        "Function_31_44A6",        # 1F, 31
        "Function_32_461C",        # 20, 32
        "Function_33_46A8",        # 21, 33
        "Function_34_4CC8",        # 22, 34
        "Function_35_5242",        # 23, 35
        "Function_36_73B3",        # 24, 36
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A2")

    Jump("loc_12F1")

    label("loc_12A7")

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

    label("loc_12F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_11AB end

    def Function_5_12FD(): pass

    label("Function_5_12FD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1400")
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x18, 0x0, 0)
    OP_98(0x18, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_135A():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_135A)

    def lambda_1374():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1374)
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
        (0, "loc_13E1"),
        (2, "loc_13F0"),
        (1, "loc_13FD"),
        (SWITCH_DEFAULT, "loc_1400"),
    )


    label("loc_13E1")

    SetScenarioFlags(0x217, 1)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_1400")

    label("loc_13F0")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13FD")

    OP_B9(0x0)
    Return()

    label("loc_1400")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7E, 1)"), scpexpr(EXPR_END)), "loc_1459")
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
    Jump("loc_14C9")

    label("loc_1459")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14C9")

    Jump("loc_150D")

    label("loc_14CE")

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

    label("loc_150D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12FD end

    def Function_6_1519(): pass

    label("Function_6_1519")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1615")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_159E")
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
    Jump("loc_1610")

    label("loc_159E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1610")

    Jump("loc_165F")

    label("loc_1615")

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

    label("loc_165F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1519 end

    def Function_7_166B(): pass

    label("Function_7_166B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1795")
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
            "#56IEarth Sepith x80\x01\x07\x02",
            "#57IWater Sepith x80\x01\x07\x02",
            "#58IFire Sepith x80\x01\x07\x02",
            "#59IWind Sepith x80\x01\x07\x02",
            "#60ITime Sepith x80\x01\x07\x02",
            "#61ISpace Sepith x80\x01\x07\x02",
            "#62IMirage Sepith x80\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_17B3")

    label("loc_1795")


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

    label("loc_17B3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_166B end

    def Function_8_17C5(): pass

    label("Function_8_17C5")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Organise Party\x01",      # 1
            "Quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A51")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(
        0x15,
        (
            "#10103FBreaking into Orchis Tower...\x01",
            "I expect quite the harsh fight.\x02\x03",
            "#10101FWhen the operation starts, I think\x01",
            "it'll be probably difficult to come back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're right...\x01",
            "We don't know what will happen.\x01",
            "We must go fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#10100FNow that we still have time,\x01",
            "it could be better to stop by\x01",
            "the facilities in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A4C")

    label("loc_19A3")


    ChrTalk(
        0x15,
        (
            "#10103FBreaking into Orchis Tower...\x01",
            "I expect quite the harsh fight.\x02\x03",
            "#10100FNow that we still have time,\x01",
            "it could be better to stop by\x01",
            "the facilities in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4C")

    Jump("loc_1AB1")

    label("loc_1A51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB1")

    ChrTalk(
        0x15,
        (
            "#10100FAre you organising the party?\x01",
            "Roger that!\x02",
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
    Jump("loc_1AB1")

    label("loc_1AB1")

    Jump("loc_17D2")

    label("loc_1AB6")

    TalkEnd(0xFE)
    Return()

    # Function_8_17C5 end

    def Function_9_1ABA(): pass

    label("Function_9_1ABA")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Organise Party\x01",      # 1
            "Quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C86")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDC")

    ChrTalk(
        0x16,
        (
            "#10403F...Now that I think about it, if we exit\x01",
            "from here Downtown is just there.\x02\x03",
            "#10402FHu hu, since we have \x01",
            "the opportunity, why\x01",
            "not visiting "Trinity"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1BDC")


    ChrTalk(
        0x16,
        (
            "#10404FLeaving Downtown to the Testaments\x01",
            "will probably be fine.\x02\x03",
            "#10400FWe should focus on\x01",
            "the operation, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C81")

    ChrTalk(
        0x101,
        "#00000FYeah...you're right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C81")

    Jump("loc_1CDE")

    label("loc_1C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDE")

    ChrTalk(
        0x16,
        "#10400FHu hu, are you switching members?\x02",
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
    Jump("loc_1CDE")

    label("loc_1CDE")

    Jump("loc_1AC7")

    label("loc_1CE3")

    TalkEnd(0xFE)
    Return()

    # Function_9_1ABA end

    def Function_10_1CE7(): pass

    label("Function_10_1CE7")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F5F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Organise Party\x01",      # 1
            "Quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB8")

    ChrTalk(
        0x101,
        "#00005FSo that's where you were, Rixia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#10702FYes...\x01",
            "I was thinking to raise my qi in a quiet\x01",
            "place until the operation begins.\x02\x03",
            "#10703F"Bloody Shirley" is\x01",
            "probably in there,\x01",
            "at Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FYeah... Same for uncle and the others,\x01",
            "she'll likely come to block our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#10701F...I won't lose, absolutely.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EFA")

    label("loc_1EB8")


    ChrTalk(
        0x17,
        (
            "#10703F"Bloody Shirley"...\x02\x03",
            "#10701FI won't lose, absolutely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_1F5A")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F5A")

    ChrTalk(
        0x17,
        "#10700FYes, you're changing members, right?\x02",
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
    Jump("loc_1F5A")

    label("loc_1F5A")

    Jump("loc_1CF4")

    label("loc_1F5F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CE7 end

    def Function_11_1F63(): pass

    label("Function_11_1F63")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2292")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Organise Party\x01",      # 1
            "Quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216B")

    ChrTalk(
        0x9,
        (
            "#00603FI'll accompany you in the tower\x01",
            "breaking into operation too.\x02\x03",
            "#00600FNow that you still have the time,\x01",
            "prepare yourselves thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it's reassuring having\x01",
            "Mr. Dudley coming with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00603FI can't leave the President's arrest\x01",
            "only to the Support Section...\x01",
            "It's only that.\x02\x03",
            "#00600FIf you got it, then\x01",
            "let's go at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_221A")

    label("loc_216B")


    ChrTalk(
        0x9,
        (
            "#00603FThe President's arrest...\x01",
            "You too should understand that\x01",
            "it's not as simple as saying it.\x02\x03",
            "#00600FNow that you still have the time,\x01",
            "prepare yourselves thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221A")

    Jump("loc_228D")

    label("loc_221F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228D")

    ChrTalk(
        0x9,
        (
            "#00600FChanging members, right?\x01",
            "...Make your decision at once.\x02",
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
    Jump("loc_228D")

    label("loc_228D")

    Jump("loc_1F70")

    label("loc_2292")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F63 end

    def Function_12_2296(): pass

    label("Function_12_2296")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B0")

    ChrTalk(
        0x8,
        (
            "#01002FEh eh, nevertheless...\x01",
            "I'm glad you're\x01",
            "all fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYou too Chief...\x01",
            "Thank goodness you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou always stayed in the city\x01",
            "doing underground activities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FYeah, we've been based here for a while,\x01",
            "discussing to find a way out, but...\x02\x03",
            "#01001FAfter the situation became like this,\x01",
            "we don't even have the time to do\x01",
            "that at leisure anymore.\x02\x03",
            "You'll have to make this operation\x01",
            "succeed at all costs.\x01",
            "...In order to get back KeA too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes...please leave it to us!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 4)
    Jump("loc_2665")

    label("loc_24B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D6")

    ChrTalk(
        0x8,
        (
            "#01003FAfter the situation became like this, we\x01",
            "don't have time to act at leisure anymore.\x02\x03",
            "#01001FYou'll have to make the breaking\x01",
            "into Orchis Tower operation\x01",
            "succeed at all costs.\x02\x03",
            "#01002FFor the citizens...but most\x01",
            "of all, for you and KeA too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes sir...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2665")

    label("loc_25D6")


    ChrTalk(
        0x8,
        (
            "#01004FI'll do maintenance\x01",
            "on the shotguns too.\x02\x03",
            "#01001FThe breaking into Orchis Tower operation...\x01",
            "We'll make it succeed no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2665")

    TalkEnd(0xFE)
    Return()

    # Function_12_2296 end

    def Function_13_2669(): pass

    label("Function_13_2669")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2801")

    ChrTalk(
        0xA,
        (
            "Well then, until the operation begins,\x01",
            "I'll have to check the armaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...By the way, you seem\x01",
            "to have met Inspector\x01",
            "Donovan at the hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How was him,\x01",
            "was he fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. There was his wife nursing him and\x01",
            "it looked like he was near a full recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ha ha, that's nice to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "While the Inspector is absent, we\x01",
            "must go on in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2896")

    label("loc_2801")


    ChrTalk(
        0xA,
        (
            "Well then, until the operation begins,\x01",
            "I'll have to check the armaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "While the Inspector is absent, we\x01",
            "must go on in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2896")

    TalkEnd(0xFE)
    Return()

    # Function_13_2669 end

    def Function_14_289A(): pass

    label("Function_14_289A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A19")

    ChrTalk(
        0xD,
        (
            "When the breaking into operation\x01",
            "begins, we need to make the\x01",
            "citizens' safety our top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm not suited for combat, so I want to act as \x01",
            "an evacuation guide to not have unnecessary \x01",
            "damages in the operation scope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FEven that kind of role is important...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe will be careful too, but...\x01",
            "Please, take care of yourselves too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2AFB")

    label("loc_2A19")


    ChrTalk(
        0xD,
        (
            "I'm not suited for combat, so I want to act as \x01",
            "an evacuation guide to not have unnecessary \x01",
            "damages in the operation scope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if the situation is like this,\x01",
            "we need to make the citizens'\x01",
            "safety our top priority.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFB")

    TalkEnd(0xFE)
    Return()

    # Function_14_289A end

    def Function_15_2AFF(): pass

    label("Function_15_2AFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C04")
    TurnDirection(0xB, 0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#00603FEmma, I'm leaving this place to you.\x02\x03",
            "#00600FTo not have hindrances to the operation\x01",
            "conduct, pay a lot of attention to the\x01",
            "base surroundings vigilance too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, roger.\x01",
            "...Mr. Dudley, be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2C47")

    label("loc_2C04")


    ChrTalk(
        0xB,
        (
            "Please leave this place to us.\x01",
            "...Mr. Dudley, be careful too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C47")

    Jump("loc_2DB5")

    label("loc_2C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D61")

    ChrTalk(
        0xB,
        (
            "I'm just checking the\x01",
            "operation plans again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're properly keeping in mind how\x01",
            "it's going to be carried out, right?\x02",
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
            "The operation's success\x01",
            "runs on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Do not neglect careful preparations.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2DB5")

    label("loc_2D61")


    ChrTalk(
        0xB,
        (
            "The operation's success\x01",
            "runs on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Do not neglect careful preparations.\x02",
    )

    CloseMessageWindow()

    label("loc_2DB5")

    TalkEnd(0xFE)
    Return()

    # Function_15_2AFF end

    def Function_16_2DB9(): pass

    label("Function_16_2DB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F03")

    ChrTalk(
        0xE,
        (
            "After the declaration of invalidity, officers\x01",
            "who collaborate with us at headquarters\x01",
            "are gathering little by little.\x02",
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
            "Hm, everyone is doing their best to\x01",
            "protect their pride as policemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You all do your best too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2F69")

    label("loc_2F03")


    ChrTalk(
        0xE,
        (
            "Everyone is doing their best to\x01",
            "protect their pride as policemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You all do your best too.\x02",
    )

    CloseMessageWindow()

    label("loc_2F69")

    TalkEnd(0xFE)
    Return()

    # Function_16_2DB9 end

    def Function_17_2F6D(): pass

    label("Function_17_2F6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C0")

    ChrTalk(
        0xF,
        (
            "To break through the "magic soldiers" defense, \x01",
            "a patrol car totally lacks the necessary power.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Taking into consideration horse\x01",
            "powers and speed, Lloyd's car\x01",
            "will be absolutely needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes. We'll recover it no matter what.\x02\x03",
            "#00000FSenior Kate, be careful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yes, do your best too, Lloyd!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_312C")

    label("loc_30C0")


    ChrTalk(
        0xF,
        (
            "We will carry out breaking into\x01",
            "preparations until the operation starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Do your best too, Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_312C")

    TalkEnd(0xFE)
    Return()

    # Function_17_2F6D end

    def Function_18_3130(): pass

    label("Function_18_3130")

    TalkBegin(0xFE)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-12940, -13300, 188130, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3317")

    ChrTalk(
        0xC,
        (
            "If the tower's hacking succeeds, we can\x01",
            "release the communications jamming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The thing you were riding...\x01",
            "The Merkabah, was it called?\x01",
            "It could be possible to communicate with that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes. In that case,\x01",
            "we could get Jona's\x01",
            "backup too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, having Jona's cooperation\x01",
            "would be a tremendous help for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For that reason too, I\x01",
            "have to make the hacking \x01",
            "succeed no matter what!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_338E")

    label("loc_3317")


    ChrTalk(
        0xC,
        (
            "It seems that it's going to take a little\x01",
            "more time until the hacking succeeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tio and you all,\x01",
            "be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338E")

    Fade(500)
    OP_6B(0x0)
    OP_69(0xFF, 0x0)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_18_3130 end

    def Function_19_339F(): pass

    label("Function_19_339F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B3")

    ChrTalk(
        0x10,
        (
            "I was at the IBC technology department,\x01",
            "but considering the recent declaration\x01",
            "of invalidity, I ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "David said he wanted to\x01",
            "trust Miss Mariabell and\x01",
            "remained in the tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "With the situation like this,\x01",
            "I wonder if he's all right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_3573")

    label("loc_34B3")


    ChrTalk(
        0x10,
        (
            "I wonder if David who stayed\x01",
            "in the tower is all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm worried about him. At the time of\x01",
            "parting we even ended up quarreling...\x01",
            "At any rate, now I have to help Chief Roberts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3573")

    TalkEnd(0xFE)
    Return()

    # Function_19_339F end

    def Function_20_3577(): pass

    label("Function_20_3577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3645")

    ChrTalk(
        0x11,
        (
            "At present, it appears that\x01",
            "the magic soldiers didn't\x01",
            "enter inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I don't know what will happen\x01",
            "if this situation drags on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I hope this deadlock state breaks fast...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_36E7")

    label("loc_3645")


    ChrTalk(
        0x11,
        (
            "Although the citizens are mostly indoor\x01",
            "due to the curfew order, there's no\x01",
            "doubt the situation is dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I hope this deadlock state breaks fast...\x02",
    )

    CloseMessageWindow()

    label("loc_36E7")

    TalkEnd(0xFE)
    Return()

    # Function_20_3577 end

    def Function_21_36EB(): pass

    label("Function_21_36EB")

    TalkBegin(0xFE)

    ChrTalk(
        0x12,
        (
            "*sigh*...\x01",
            "I'm totally nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I hope the breaking into operation succeeds...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_36EB end

    def Function_22_374A(): pass

    label("Function_22_374A")

    TalkBegin(0xFE)

    ChrTalk(
        0x13,
        (
            "Magic soldiers, eh...?\x01",
            "To think the President had\x01",
            "this card up his sleeve...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That's troublesome, but...\x01",
            "We have to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_374A end

    def Function_23_37DE(): pass

    label("Function_23_37DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3903")

    ChrTalk(
        0x14,
        (
            "The weapons stored in this area were\x01",
            "obtained through a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "By nature, they'd be illegal weapons,\x01",
            "but in a situation in which we lack goods,\x01",
            "needs must when the devil drives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Most of all, I hope they're effective \x01",
            "against those magic soldiers...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_398D")

    label("loc_3903")


    ChrTalk(
        0x14,
        (
            "The weapons stored in this area were\x01",
            "obtained through a certain route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I hope they're effective\x01",
            "against those magic soldiers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398D")

    TalkEnd(0xFE)
    Return()

    # Function_23_37DE end

    def Function_24_3991(): pass

    label("Function_24_3991")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3AA7")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -6000, -8000, 595580, 0)

    label("loc_3AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3ACD")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -9520, -16000, 188860, 0)

    label("loc_3ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3AF3")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -5840, 0, 608620, 225)

    label("loc_3AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3B4A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17080, -16000, 178000, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 45)
    Jump("loc_3B76")

    label("loc_3B4A")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 0)

    label("loc_3B76")

    Return()

    # Function_24_3991 end

    def Function_25_3B77(): pass

    label("Function_25_3B77")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5E")
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

    label("loc_3C5E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_25_3B77 end

    def Function_26_3C6D(): pass

    label("Function_26_3C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_3C77")
    Return()

    label("loc_3C77")

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
            "There is a monster harboring an enormous power.\x02",
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
        (1, "loc_3D5F"),
        (SWITCH_DEFAULT, "loc_3D78"),
    )


    label("loc_3D5F")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -499760, 0, 494390, 0)
    EventEnd(0x5)
    Return()

    label("loc_3D78")

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
        (2, "loc_3E3A"),
        (1, "loc_3E3F"),
        (SWITCH_DEFAULT, "loc_3E42"),
    )


    label("loc_3E3A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3E3F")

    OP_B9(0x0)
    Return()

    label("loc_3E42")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F34")
    Sound(629, 0, 100, 0)
    Sound(842, 0, 100, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You felt an outrageous power awakening somewhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x21F, 0)

    label("loc_3F34")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_26_3C6D end

    def Function_27_3F3E(): pass

    label("Function_27_3F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F50")
    Call(0, 36)
    Return()

    label("loc_3F50")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A2")
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

    label("loc_40A2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_27_3F3E end

    def Function_28_40AA(): pass

    label("Function_28_40AA")

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

    # Function_28_40AA end

    def Function_29_41B9(): pass

    label("Function_29_41B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_41FE")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_432F")

    label("loc_41FE")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4328")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4328")
    Call(0, 32)

    label("loc_4328")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_432F")

    Return()

    # Function_29_41B9 end

    def Function_30_4330(): pass

    label("Function_30_4330")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_4375")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_44A5")

    label("loc_4375")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449E")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_449E")
    Call(0, 32)

    label("loc_449E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_44A5")

    Return()

    # Function_30_4330 end

    def Function_31_44A6(): pass

    label("Function_31_44A6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_44EB")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch is already off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_461B")

    label("loc_44EB")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4614")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4614")
    Call(0, 32)

    label("loc_4614")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_461B")

    Return()

    # Function_31_44A6 end

    def Function_32_461C(): pass

    label("Function_32_461C")

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

    # Function_32_461C end

    def Function_33_46A8(): pass

    label("Function_33_46A8")

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

    def lambda_4780():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4780)
    Sleep(50)

    def lambda_479D():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_479D)
    Sleep(50)

    def lambda_47BA():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47BA)
    Sleep(50)

    def lambda_47D7():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47D7)
    Sleep(50)

    def lambda_47F4():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_47F4)
    Sleep(50)

    def lambda_4811():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4811)
    OP_6F(0x1)
    OP_68(-4630, -11300, 167910, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(14590, 5000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#12P#00305FHm, we came out into a friggin' big place, huh?\x02\x03",
            "#00303FEven when we got off from Orchis\x01",
            "Tower due to the Trade Conference\x01",
            "incident I was taken aback, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, location speaking, it\x01",
            "seems quite separated from there...\x02\x03",
            "#00006FHard to believe that even under\x01",
            "Downtown such a huge space\x01",
            "was constructed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, who knows how much mira\x01",
            "was used to reach Downtown\x01",
            "from underground Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAlso, according to what I have heard\x01",
            "before, it appears that D-Division was\x01",
            "built as a parking lot for orbal vehicles...\x02\x03",
            "#00206FBut as you can see, vehicles\x01",
            "aren't parked here at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FRight...\x02\x03",
            "#00101FThere would be any use for such a place even in\x01",
            "the Republic where orbal vehicles are popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FAnd first of all, even if something like a parking\x01",
            "lot was provided underground Downtown,\x01",
            "I question that many people would use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWe could think anything about it, but...\x02\x03",
            "#00000F...In any case, we have to go to\x01",
            "exterminate the Wanted Monster.\x02\x03",
            "Let's try proceeding further inside.\x02",
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

    # Function_33_46A8 end

    def Function_34_4CC8(): pass

    label("Function_34_4CC8")

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
            "#30WAfter having had an opportunity to\x01",
            "think about it together with everyone...\x07\x00\x02",
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
            "#4S──As one representative of the autonomous\x01",
            "state, I hereby declare the invalidity of the\x01",
            ""Independent State of Crossbell"!\x07\x00\x02",
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
        "#11POoh, he said that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PB-But now it'll become\x01",
            "a little easier to act...!\x02",
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
            "#5P#00602F──Mr. Sergei,\x01",
            "I guess it's their doing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P#01004FEh eh...\x01",
            "What else could it be.\x02\x03",
            "#01002FWell then── It seems we're gonna get busy.\x02",
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

    # Function_34_4CC8 end

    def Function_35_5242(): pass

    label("Function_35_5242")

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
            "#1KSame Day, 9:30──\x02",
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
        "#5PAah...Tio, you're safe!\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMoreover, Jona was released\x01",
            "safely too, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PN-Now I don't have\x01",
            "any more regrets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FChief...you are too emotional.\x02\x03",
            "#00202FBut I am glad you are well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5PAah!\x01",
            "To think that Tio is\x01",
            "glad for me being well...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt was worth it offering\x01",
            "more than a hundred prayers\x01",
            "a day to the Goddess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FThat is really too annoying.\x02",
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
            "#5P#00012FN-Nevertheless...\x01",
            "So many people have gathered up, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8300, -15000, 188100, 1000)
    MoveCamera(39, 22, 0, 1000)
    SetCameraDistance(15600, 1000)

    def lambda_58C8():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_58C8)
    Sleep(50)

    def lambda_58D8():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_58D8)
    Sleep(50)

    def lambda_58E8():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_58E8)
    Sleep(50)

    def lambda_58F8():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_58F8)
    Sleep(50)

    def lambda_5908():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5908)
    Sleep(50)

    def lambda_5918():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5918)
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
            "#6P#00305FDoes it mean the animosity against\x01",
            "the President has risen like I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FWell, that goes without saying.\x02\x03",
            "#01001FHe suddenly issued martial law and a curfew\x01",
            "order for the entire city yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAfter that, a bluish mist\x01",
            "enshrouded everything.\x02\x03",
            "#00610F...It's a situation we absolutely\x01",
            "can't overlook anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We can't issue an arrest warrant, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We can only restrain the President's\x01",
            "party in the form of flagrant offenders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106F......Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FRight...\x01",
            "It seems that's the only way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10113FUhhm...\x01",
            "How is the citizens' security?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAt present, they're quietly abiding\x01",
            "to the martial law and curfew.\x02\x03",
            "#11PI think the fact that fightings are taking place\x01",
            "outside the city is having an influence too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PBut since it was suddenly, it seems that\x01",
            "there're many citizens unprepared for it.\x02\x03",
            "#11PIt seems there're even people taking shelter at\x01",
            "the City Meeting Hall, in the hotels and so on.\x01",
            "I guess that's quite troublesome, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FNo time to waste...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10403FHowever, suppressing the\x01",
            "President's party...\x02\x03",
            "#10401FMeans that we need to\x01",
            "capture Orchis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FYeah, we've got a rough\x01",
            "plan already.\x02\x03",
            "It appears that we'll be cooperating with\x01",
            "the remaining Bracers in the city too.\x02\x03",
            "#01002FWe were just eagerly awaiting\x01",
            "for you all to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FChief... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...Thank you for\x01",
            "waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10701FSo, what kind of plan\x01",
            "is it specifically...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAt present, it appears that a large pack \x01",
            "of those "magic soldiers" are fortifying \x01",
            "the defenses in front of the tower.\x02\x03",
            "#00601FWe'll assault them with all the\x01",
            "personnel here and the Bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Taking that chance, the breaking into team\x01",
            "will charge into the tower with a vehicle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We'll gain control of the tower\x01",
            "like that. That's the plan.\x02",
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
        "#6P#10112FEhhm...I don't know what to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt's quite the forceful plan,\x01",
            "but is there a chance to win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01003FIt seems that a big part of the State\x01",
            "Guard have been sent outside the city.\x02\x03",
            "#01000FI think that there should be only a few\x01",
            "inside the tower, starting with Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThe route from the Geofront\x01",
            "has been sealed, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThis is probably the best measure to\x01",
            "take in such a current situation.\x02",
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

    def lambda_633D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_633D)

    def lambda_634A():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_634A)
    Sleep(30)

    def lambda_635A():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_635A)
    Sleep(30)

    def lambda_636A():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_636A)
    Sleep(30)

    def lambda_637A():
        TurnDirection(0x106, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_637A)
    Sleep(30)

    def lambda_638A():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_638A)
    Sleep(30)

    def lambda_639A():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_639A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1100)

    def lambda_63C2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63C2)

    def lambda_63CF():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63CF)
    Sleep(30)

    def lambda_63DF():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_63DF)
    Sleep(30)

    def lambda_63EF():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_63EF)
    Sleep(30)

    def lambda_63FF():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_63FF)
    Sleep(30)

    def lambda_640F():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_640F)
    Sleep(30)

    def lambda_641F():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_641F)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00001FHas that breaking into team\x01",
            "been decided yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00605FNo, we were just...\x02\x03",
            "#00601F──Wait, don't tell me that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, please entrust the breaking\x01",
            "into team to us, if possible.\x02\x03",
            "#00013FIt's also to get back KeA, who is\x01",
            "in the tower, with our own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, I won't hand over\x01",
            "only that to anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FI will be useful for the\x01",
            "tower inside security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI too...I want to directly ask\x01",
            "questions to Bell and "uncle".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI assisted them as a \x01",
            "State Guard once, so...\x02\x03",
            "#10101FThat's why I can't leave them alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, with members like these we\x01",
            "could go through even a bloodshed.\x02\x03",
            "#10402FThinking about teamwork, I guess\x01",
            "we're the most suitable ones?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10704FI'll be useful to you for sure.\x02",
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
            "#11P#01004F...Eh eh, oh boy.\x02\x03",
            "#01002FThose mere rookies have completely\x01",
            "become grown ups now.\x02",
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
            "#11P#01003FWell, all right.\x01",
            "I'll entrust the breaking into team to you.\x02\x03",
            "#01001FStill, it doesn't mean that the\x01",
            "entire plan is ready yet.\x02\x03",
            "I'll have you wait a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FAnd this mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe're currently proceeding with\x01",
            "the Orchis Tower hacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIn about one more hour,\x01",
            "access should be possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6942():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6942)

    def lambda_694F():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_694F)
    Sleep(50)

    def lambda_695F():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_695F)
    Sleep(50)

    def lambda_696F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_696F)
    Sleep(50)

    def lambda_697F():
        TurnDirection(0x106, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_697F)
    Sleep(50)

    def lambda_698F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_698F)
    Sleep(50)

    def lambda_699F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_699F)
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
        "#12P#00002FReally...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01004FYeah, so even back up to the breaking\x01",
            "into team would be easier and the release\x01",
            "of the communication jamming possible too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#11P#00603FAlso, we need to contact the Guild\x01",
            "and all quarters once again.\x02\x03",
            "#00600FAt any rate, we'll work out the definitive \x01",
            "plan considering that the breaking into \x01",
            "team is going to be leaved to you.\x02",
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
            "Then, after Lloyd and tem talked\x01",
            "with Sergei and the others about the\x01",
            "breaking into operation definitive plan...\x02\x03",
            "They decided to go back to the SSS building\x01",
            "to retrieve the orbal car to be used in the plan.\x07\x00\x02",
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
            "#12P#00005F──So, Mr. Dudley, you'll\x01",
            "be in the breaking into team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FYeah, due to the Trade Conference security, \x01",
            "I too know the Orchis Tower blueprints.\x01\x02\x03",
            "#00600FI can even guide you to a certain degree\x01",
            "since we're going through city areas.\x02\x03",
            "#00607FAlso, when the President's arrest will happen,\x01",
            "I can't leave that only to the Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FBoy oh boy, again with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00204FWe promised already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, but he will be a real help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FUhhm, about the orbal car we'll\x01",
            "use for the breaking into...\x02\x03",
            "#10100FAre we really using the SSS one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PYeah. At present, it's the\x01",
            "car model which unites both\x01",
            "great horsepower and speed.\x02\x03",
            "#01002FIt will be truly the ideal to force a\x01",
            "breakthrough through the city areas.\x02",
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
            "#12P#10404FWell, leaving it at the Support Section\x01",
            "would have no meaning then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FHowever...\x01",
            "Moving with these numbers throughout\x01",
            "the city is going to make us stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00603FThen, let's wring out the members\x01",
            "who are going to come.\x02\x03",
            "#00600FThe others will stay\x01",
            "here on standby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAcknowledged.\x02",
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
            "Dudley has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_721E")
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)
    Jump("loc_7226")

    label("loc_721E")

    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x196)

    label("loc_7226")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Dudley have learned the\x01\x07\x02",
            ""Hearts of Iron"\x07\x05",
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

    # Function_35_5242 end

    def Function_36_73B3(): pass

    label("Function_36_73B3")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the orbal energy is down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7533")

    ChrTalk(
        0x101,
        "#00003F...It looks like it doesn't move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThis path should be connected to\x01",
            "the Orchis Tower foundations...\x02\x03",
            "#00103FMaybe the President and\x01",
            "the others have stopped it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FI see, it could be possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSeems it's better to give up\x01",
            "the idea to infiltrate the\x01",
            "tower from the Geofront.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_7533")

    TalkEnd(0xFF)
    Return()

    # Function_36_73B3 end

    SaveToFile()

Try(main)
