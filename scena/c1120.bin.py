from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1120.bin",                # FileName
        "c1120",                    # MapName
        "c1120",                    # Location
        0x0017,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1120",                  # 0
        "Grace",                  # 1
        "Reins",                  # 2
        "Feng",                   # 3
        "Oscar",                  # 4
        "Receptionist Cynthia",   # 5
        "Iris",                   # 6
        "Patrol Officer Kate",    # 7
        "Piano Player",           # 8
        "Guide",                  # 9
        "Maid",                   # 10
        "Citizen",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Boy",                    # 14
        "Citizen",                # 15
        "Sister Ries",            # 16
        "Shanshan",               # 17
        "Joanna",                 # 18
        "Old Man Mors",           # 19
        "Roy",                    # 20
        "Wendy",                  # 21
        "Citizen",                # 22
        "Citizen",                # 23
        "Citizen",                # 24
        "Citizen",                # 25
        "Citizen",                # 26
        "Citizen",                # 27
        "Citizen",                # 28
        "Congressman Campbell",   # 29
        "Imperial Faction Congressman",# 30
        "Pro-Independence Congressman",# 31
        "Pro-Independence Congressman",# 32
        "Moderator",              # 33
    ))

    AddCharChip((
        "chr/ch06000.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch07000.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch26900.itc",                   # 05
        "chr/ch30600.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch25900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21000.itc",                   # 0B
        "chr/ch20300.itc",                   # 0C
        "chr/ch23000.itc",                   # 0D
        "chr/ch21702.itc",                   # 0E
        "chr/ch14000.itc",                   # 0F
        "chr/ch26902.itc",                   # 10
        "chr/ch32500.itc",                   # 11
        "chr/ch25700.itc",                   # 12
    ))

    DeclNpc(4294962637, 0,       9239,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294961347, 0,       9800,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294956767, 0,       1179,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294957107, 0,       7269,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294960717, 0,       4294965227, 109,  261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5000,    0,       2289,    270,  261,  0x0, 0,   16,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(4294963226, 0,       6420,    135,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294963987, 1049,    13500,   135,  261,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4294966277, 0,       4294957996, 270,  261,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294966506, 0,       7590,    348,  261,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(4294965116, 0,       3890,    315,  261,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294967206, 0,       4420,    45,   261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294966566, 0,       4294964527, 135,  261,  0x0, 0,   12,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294967267, 0,       4294963967, 315,  261,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5000,    0,       4294964527, 270,  261,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   10,  255,  0)
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

    DeclActor(7750,    4000,    12300,   1200,    7750,    5450,    12300,   0x007C, 0,  5,  0x0000)
    DeclActor(4294965126, 880,     11540,   1000,    4294963986, 2550,    13500,   0x007E, 0,  17, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_76E",          # 02, 2
        "Function_3_85B",          # 03, 3
        "Function_4_990",          # 04, 4
        "Function_5_A5A",          # 05, 5
        "Function_6_B73",          # 06, 6
        "Function_7_F29",          # 07, 7
        "Function_8_1030",         # 08, 8
        "Function_9_12C9",         # 09, 9
        "Function_10_1482",        # 0A, 10
        "Function_11_1588",        # 0B, 11
        "Function_12_1926",        # 0C, 12
        "Function_13_1B5B",        # 0D, 13
        "Function_14_1DDA",        # 0E, 14
        "Function_15_1EDE",        # 0F, 15
        "Function_16_203F",        # 10, 16
        "Function_17_2197",        # 11, 17
        "Function_18_2247",        # 12, 18
        "Function_19_2388",        # 13, 19
        "Function_20_249C",        # 14, 20
        "Function_21_258D",        # 15, 21
        "Function_22_25FE",        # 16, 22
        "Function_23_2702",        # 17, 23
        "Function_24_2AE8",        # 18, 24
        "Function_25_4DCA",        # 19, 25
        "Function_26_4E34",        # 1A, 26
        "Function_27_4E75",        # 1B, 27
        "Function_28_4F5F",        # 1C, 28
        "Function_29_7BDB",        # 1D, 29
        "Function_30_7C19",        # 1E, 30
        "Function_31_7C38",        # 1F, 31
        "Function_32_7C69",        # 20, 32
        "Function_33_7C9D",        # 21, 33
        "Function_34_7CD1",        # 22, 34
        "Function_35_7CED",        # 23, 35
        "Function_36_7D1E",        # 24, 36
        "Function_37_7D3A",        # 25, 37
        "Function_38_7D56",        # 26, 38
        "Function_39_7DA1",        # 27, 39
        "Function_40_7DDB",        # 28, 40
        "Function_41_7E3D",        # 29, 41
        "Function_42_7F72",        # 2A, 42
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76D")
    SetChrPos(0xFE, 3130, 0, 9060, 270)
    OP_95(0xFE, -160, 0, 7500, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -1340, 0, 3750, 1000, 0x0)
    OP_95(0xFE, -80, 0, -190, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -1120, 0, 1760, 1000, 0x0)
    OP_95(0xFE, -3830, 0, 1460, 1000, 0x0)
    OP_95(0xFE, -4390, 0, 2430, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -4330, 0, -270, 1000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2360, 0, 1350, 1000, 0x0)
    OP_95(0xFE, 1010, 0, 2510, 1000, 0x0)
    OP_95(0xFE, 1630, 0, 3540, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, 3710, 0, 4130, 1000, 0x0)
    OP_95(0xFE, 4290, 0, 7130, 1000, 0x0)
    OP_95(0xFE, 3130, 0, 9060, 1000, 0x0)
    Jump("Function_1_620")

    label("loc_76D")

    Return()

    # Function_1_620 end

    def Function_2_76E(): pass

    label("Function_2_76E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85A")
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -6960, 0, 7410, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -5820, 0, -3790, 2000, 0x0)
    OP_93(0x17, 0x2D, 0x1F4)
    Sleep(2000)
    Jump("Function_2_76E")

    label("loc_85A")

    Return()

    # Function_2_76E end

    def Function_3_85B(): pass

    label("Function_3_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_872")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    Event(0, 24)
    Jump("loc_881")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_881")
    ClearScenarioFlags(0x22, 2)
    Event(0, 41)

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")
    Event(0, 42)

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F")
    SetScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96A")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -4500, 0, -7300, 270)
    SetChrPos(0x8, -5560, 0, -7300, 90)
    SetChrPos(0x9, -5160, 0, -6000, 135)
    SetChrPos(0x18, -8590, 0, 2730, 225)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x19, 3340, 0, 10090, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x17, -5820, 0, -3790, 45)
    BeginChrThread(0x17, 0, 0, 2)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_97E")

    label("loc_96A")

    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)

    label("loc_97E")

    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_98F")

    Return()

    # Function_3_85B end

    def Function_4_990(): pass

    label("Function_4_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B3")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetScenarioFlags(0x1, 3)

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F2")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A27")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)

    label("loc_A27")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A44")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A59")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_A59")

    Return()

    # Function_4_990 end

    def Function_5_A5A(): pass

    label("Function_5_A5A")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★How To Make A Deluxe Sweet Chocolate★\x01",
            "～Why not try making it at home?～\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Sweet Chocolate\x01",
            "recipe is written down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Sweet\x01",
            "Chocolate"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B6F")

    TalkEnd(0xFF)
    Return()

    # Function_5_A5A end

    def Function_6_B73(): pass

    label("Function_6_B73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC3")
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "#02102FAh, good work you guys!\x02\x03",
            "I'm interviewing the\x01",
            "pageant participants.\x02\x03",
            "#02109FHaha, you'll go along\x01",
            "with it properly later,\x01",
            "right~♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(H-Hmm. Sorry, but it\x01",
            "looks like this is going\x01",
            "to take some time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Haha. I think it's best\x01",
            "if we secretly sneak\x01",
            "away.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    SetScenarioFlags(0x0, 4)
    Jump("loc_D37")

    label("loc_CC3")


    ChrTalk(
        0x8,
        (
            "#02105FOh, is that how it's\x01",
            "going to be?\x02\x03",
            "#02100FI suppose I really\x01",
            "should visit my family\x01",
            "after the incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    Jump("loc_F25")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB7")

    ChrTalk(
        0x8,
        "#02109FHey guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGrace... Are you\x01",
            "covering the charity\x01",
            "event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02100FHaha, you got it☆\x02\x03",
            "It looks pretty lively. I think\x01",
            "I'll be able to write an article to\x01",
            "encourage the Crossbell citizens.\x02\x03",
            "#02103FThe scars from that attack are\x01",
            "already gone...\x02\x03",
            "#02102FI've got to do what I can at the\x01",
            "pageant too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, please do your\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 6)
    Jump("loc_F25")

    label("loc_EB7")


    ChrTalk(
        0x8,
        (
            "#02102FI heard the charity\x01",
            "event has an interesting\x01",
            "program...\x02\x03",
            "#02109FHaha, it'll be the\x01",
            "perfect scoop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F25")

    TalkEnd(0xFE)
    Return()

    # Function_6_B73 end

    def Function_7_F29(): pass

    label("Function_7_F29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0xFE,
        (
            "The pageant was\x01",
            "definitely worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got a lot of great\x01",
            "photos. I've got to head\x01",
            "back and sort them out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C")

    label("loc_FB6")


    ChrTalk(
        0xFE,
        (
            "The beautiful piano\x01",
            "player who was called to\x01",
            "the charity event...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think this'll make a\x01",
            "pretty good photo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")

    TalkEnd(0xFE)
    Return()

    # Function_7_F29 end

    def Function_8_1030(): pass

    label("Function_8_1030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_114F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E7")

    ChrTalk(
        0xFE,
        (
            "Ah~, I can't believe\x01",
            "Shanshan participated in\x01",
            "the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, thankfully she's back\x01",
            "to her normal self. I think\x01",
            "it turned out all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_114A")

    label("loc_10E7")


    ChrTalk(
        0xFE,
        (
            "But, for Shanshan to\x01",
            "participate in a\x01",
            "pageant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I hope the master\x01",
            "doesn't get angry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114A")

    Jump("loc_12C5")

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(
        0xFE,
        (
            "I'm providing food from\x01",
            "The Old Dragon for the\x01",
            "charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Puck and Ruth are\x01",
            "filling the hole I left\x01",
            "by not being there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little worried, but\x01",
            "those two are serious, so\x01",
            "it'll probably be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_12C5")

    label("loc_123D")


    ChrTalk(
        0xFE,
        (
            "But... Shanshan has been\x01",
            "depressed lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like she decided to\x01",
            "participate in the contest...\x01",
            "I hope she cheers up soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C5")

    TalkEnd(0xFE)
    Return()

    # Function_8_1030 end

    def Function_9_12C9(): pass

    label("Function_9_12C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_147E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DC")

    ChrTalk(
        0xFE,
        (
            "Uhuhu. If we get more\x01",
            "customers because of this,\x01",
            "papa will be overjoyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm worried about\x01",
            "Rixia though. I'm sure\x01",
            "she'll come back for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To welcome her with a smile\x01",
            "when she returns, I've got to\x01",
            "cheer up and wait for her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1479")

    label("loc_13DC")


    ChrTalk(
        0xFE,
        (
            "I'm worried about Rixia,\x01",
            "but I'm sure she'll come\x01",
            "back to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To welcome her with a smile\x01",
            "when she returns, I've got to\x01",
            "cheer up and wait for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1479")

    Jump("loc_147E")

    label("loc_147E")

    TalkEnd(0xFE)
    Return()

    # Function_9_12C9 end

    def Function_10_1482(): pass

    label("Function_10_1482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152D")

    ChrTalk(
        0xFE,
        (
            "*sigh*... Someone like\x01",
            "me got up on stage like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha... You were very\x01",
            "cute, Joanna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, how embarrassing...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_157F")

    label("loc_152D")


    ChrTalk(
        0xFE,
        (
            "For someone like me to get\x01",
            "up on stage like that...\x01",
            "Ooh, how embarrassing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F")

    Jump("loc_1584")

    label("loc_1584")

    TalkEnd(0xFE)
    Return()

    # Function_10_1482 end

    def Function_11_1588(): pass

    label("Function_11_1588")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(
        0xFE,
        (
            "Hey, it's Lloyd and the\x01",
            "Support Section! You guys\x01",
            "were pretty cool back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I was scared when\x01",
            "you guys came out, but one\x01",
            "of you ended up winning.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_1675")

    ChrTalk(
        0x102,
        "#00109FThank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16DA")

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_16AA")

    ChrTalk(
        0x103,
        (
            "#00202FHaha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DA")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_16DA")

    ChrTalk(
        0x109,
        (
            "#10109FHaha, thank you very\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DA")

    SetScenarioFlags(0x0, 6)
    Jump("loc_172B")

    label("loc_16E2")


    ChrTalk(
        0xFE,
        (
            "Well, keep enjoying\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got plenty of food\x01",
            "left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172B")

    Jump("loc_1922")

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(
        0xFE,
        "Oh, if it isn't Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOscar? Oh, so you're\x01",
            "helping with the event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I left the store\x01",
            "to Bennett and came\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My baguettes are lined up on the\x01",
            "table there. If you like bread,\x01",
            "I've got several kinds made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, that's why you're\x01",
            "the best baker around,\x01",
            "Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. You guys enjoy\x01",
            "yourselves, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 7)
    Jump("loc_1922")

    label("loc_189B")


    ChrTalk(
        0xFE,
        (
            "My baguettes are lined up on the\x01",
            "table there. If you like bread,\x01",
            "I've got several kinds made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys enjoy\x01",
            "yourselves, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1922")

    TalkEnd(0xFE)
    Return()

    # Function_11_1588 end

    def Function_12_1926(): pass

    label("Function_12_1926")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_193A")
    Jump("loc_1B57")

    label("loc_193A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_19D4")

    ChrTalk(
        0xFE,
        (
            "Lloyd and friend. It looks\x01",
            "like you've assembled the\x01",
            "pageant participants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, do your best out\x01",
            "there. I'll be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B57")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFE")

    ChrTalk(
        0xFE,
        (
            "My, if it isn't Lloyd\x01",
            "and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHuh, Officer Kate? What\x01",
            "are you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, I'm helping out\x01",
            "with this event for a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be up in a bit, so\x01",
            "I'm having something to\x01",
            "eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FUp...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that's still a\x01",
            "secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, look forward to\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 0)
    Jump("loc_1B57")

    label("loc_1AFE")


    ChrTalk(
        0xFE,
        (
            "I'll be up in a bit, so\x01",
            "I'm having something to\x01",
            "eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, look forward to\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B57")

    TalkEnd(0xFE)
    Return()

    # Function_12_1926 end

    def Function_13_1B5B(): pass

    label("Function_13_1B5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C7F")

    ChrTalk(
        0x8,
        (
            "#02100FHmm, did your co-workers\x01",
            "suggest this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, a pageant stage is\x01",
            "really nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I was happy to\x01",
            "receive everyone's\x01",
            "applause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm glad I\x01",
            "participated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02104FHmm, hmm... (*scritch,\x01",
            "scratch*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1C7F")


    ChrTalk(
        0xFE,
        (
            "Actually, I'm planning\x01",
            "on returning home to\x01",
            "Remiferia before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I planned to head back immediately,\x01",
            "but... I thought this would make a\x01",
            "great souvenir for my parents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D32")

    Jump("loc_1DD6")

    label("loc_1D37")


    ChrTalk(
        0xFE,
        (
            "In the rest of the\x01",
            "program, I'll have to\x01",
            "appear on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I am used to standing\x01",
            "in front of people because of\x01",
            "work, I am really nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD6")

    TalkEnd(0xFE)
    Return()

    # Function_13_1B5B end

    def Function_14_1DDA(): pass

    label("Function_14_1DDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(
        0xFE,
        (
            "Aww, being adored by\x01",
            "other people is the\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was really fun. I'd\x01",
            "like to do it again if I\x01",
            "get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDA")

    label("loc_1E69")


    ChrTalk(
        0xFE,
        (
            "*puff, puff*... Alright,\x01",
            "now my makeup's perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm doing this,\x01",
            "might as well aim for\x01",
            "the top.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDA")

    TalkEnd(0xFE)
    Return()

    # Function_14_1DDA end

    def Function_15_1EDE(): pass

    label("Function_15_1EDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FA5")

    ChrTalk(
        0xFE,
        (
            "Thanks to the pageant, we've\x01",
            "raised plenty of funds for the\x01",
            "restoration of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have all of the citizens\x01",
            "and the Special Support\x01",
            "Section to thank for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_1FA5")


    ChrTalk(
        0xFE,
        (
            "The purpose of today's buffet party\x01",
            "is to solicit funds for restoration\x01",
            "across the whole of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please enjoy it to the\x01",
            "fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203B")

    TalkEnd(0xFE)
    Return()

    # Function_15_1EDE end

    def Function_16_203F(): pass

    label("Function_16_203F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(
        0xFE,
        (
            "All of the participants\x01",
            "were just so lovely~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew I should have put\x01",
            "myself out there for the\x01",
            "maid role.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2193")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_2156")

    ChrTalk(
        0xFE,
        (
            "I am helping with the\x01",
            "buffet party, so I can't\x01",
            "appear in the pageant~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sorry, but please\x01",
            "look for someone else~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2193")

    label("loc_2156")


    ChrTalk(
        0xFE,
        (
            "If you would like food\x01",
            "or drink then please,\x01",
            "have some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2193")

    TalkEnd(0xFE)
    Return()

    # Function_16_203F end

    def Function_17_2197(): pass

    label("Function_17_2197")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2229")

    ChrTalk(
        0xF,
        (
            "I felt a pageant was too\x01",
            "vulgar, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha, it actually turned\x01",
            "out to be quite fun. Good\x01",
            "work out there you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2243")

    label("loc_2229")


    ChrTalk(
        0xF,
        "What to play next...\x02",
    )

    CloseMessageWindow()

    label("loc_2243")

    TalkEnd(0xF)
    Return()

    # Function_17_2197 end

    def Function_18_2247(): pass

    label("Function_18_2247")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22CC")

    ChrTalk(
        0xFE,
        (
            "...Mmm, mmmm... I guess\x01",
            "that's what I get for\x01",
            "overeating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But for Crossbell\x01",
            "City... I'll eat\x01",
            "anything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2384")

    label("loc_22CC")


    ChrTalk(
        0xFE,
        (
            "*chew, chew*... It seems they have\x01",
            "delicious things from throughout\x01",
            "Crossbell all here in one place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it's better for\x01",
            "the city the more I eat,\x01",
            "so I'll eat all I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2384")

    TalkEnd(0xFE)
    Return()

    # Function_18_2247 end

    def Function_19_2388(): pass

    label("Function_19_2388")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_240B")

    ChrTalk(
        0xFE,
        (
            "Ah, that was a sight for\x01",
            "sore eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always knew the best\x01",
            "appetizer for drinks was\x01",
            "beautiful women.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2498")

    label("loc_240B")


    ChrTalk(
        0xFE,
        (
            "Mmm, the hall is full of\x01",
            "beautiful women for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this related to the\x01",
            "centerpiece of their program\x01",
            "they're doing later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2498")

    TalkEnd(0xFE)
    Return()

    # Function_19_2388 end

    def Function_20_249C(): pass

    label("Function_20_249C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2554")

    ChrTalk(
        0xFE,
        (
            "Haha, even though I'm a woman, I\x01",
            "have to say this place is full of\x01",
            "nothing but attractive people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems this little one\x01",
            "looks up to working\x01",
            "girls too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_2554")


    ChrTalk(
        0xFE,
        (
            "Now look here, you've\x01",
            "got ketchup on your\x01",
            "lips.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2589")

    TalkEnd(0xFE)
    Return()

    # Function_20_249C end

    def Function_21_258D(): pass

    label("Function_21_258D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25CE")

    ChrTalk(
        0xFE,
        "I... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think police are cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_25FA")

    label("loc_25CE")


    ChrTalk(
        0xFE,
        (
            "*chew, chew*... Ehehe,\x01",
            "this is good!♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FA")

    TalkEnd(0xFE)
    Return()

    # Function_21_258D end

    def Function_22_25FE(): pass

    label("Function_22_25FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2679")

    ChrTalk(
        0xFE,
        (
            "The pageant was a lot of\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. If I were 30 years\x01",
            "younger, I could\x01",
            "participate as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FE")

    label("loc_2679")


    ChrTalk(
        0xFE,
        (
            "That piano song played\x01",
            "earlier had a nice sound\x01",
            "to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like my feelings\x01",
            "regarding the attack\x01",
            "have been put to rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FE")

    TalkEnd(0xFE)
    Return()

    # Function_22_25FE end

    def Function_23_2702(): pass

    label("Function_23_2702")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293B")

    ChrTalk(
        0x17,
        (
            "#04402FThank you for inviting me,\x01",
            "everyone.\x02\x03",
            "I don't think I could have\x01",
            "an interesting experience\x01",
            "like this at the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, good work out\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI did want to vote for\x01",
            "you though, Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#04406FAs someone who's not from Crossbell,\x01",
            "I just thought it would be wrong for\x01",
            "me to compete with the other girls.\x02\x03",
            "#04409FBut, thank you very much. I'll take\x01",
            "that as a compliment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Hmm. If you could vote\x01",
            "for her, I bet she'd\x01",
            "have done pretty well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F(She's not aware of\x01",
            "that, is she.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 1)
    Jump("loc_2AE4")

    label("loc_293B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5B")

    ChrTalk(
        0x17,
        (
            "#04402FAlthough I declined to take part\x01",
            "in the voting, I thought it was\x01",
            "an interesting experience.\x02\x03",
            "#04404F*chew, chew*... Now this is how\x01",
            "you enjoy a buffet party...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F(There's a mountain of\x01",
            "food on her plate...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F(Haha. That's Ries for\x01",
            "you.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2AE4")

    label("loc_2A5B")


    ChrTalk(
        0x17,
        (
            "#04404F*chew, chew*... I'll head\x01",
            "back to the cathedral in\x01",
            "a little bit.\x02\x03",
            "#04402F...I'll enjoy this buffet\x01",
            "party for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE4")

    TalkEnd(0xFE)
    Return()

    # Function_23_2702 end

    def Function_24_2AE8(): pass

    label("Function_24_2AE8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadChrToIndex("chr/ch20800.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("apl/ch51257.itc", 0x21)
    LoadChrToIndex("chr/ch26100.itc", 0x22)
    LoadChrToIndex("apl/ch51547.itc", 0x24)
    LoadChrToIndex("chr/ch20200.itc", 0x25)
    LoadChrToIndex("chr/ch20700.itc", 0x26)
    LoadChrToIndex("chr/ch21100.itc", 0x27)
    LoadChrToIndex("chr/ch28000.itc", 0x28)
    LoadChrToIndex("chr/ch20000.itc", 0x29)
    LoadChrToIndex("chr/ch20100.itc", 0x2A)
    LoadChrToIndex("chr/ch20400.itc", 0x2B)
    SoundLoad(803)
    SoundLoad(821)
    SoundLoad(877)
    SoundLoad(818)
    SoundLoad(819)
    SoundLoad(820)
    SoundLoad(420)
    SoundLoad(421)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    OP_68(-5060, 1500, 1290, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(28100, 0)
    SetChrPos(0x10, -10190, 0, 7270, 90)
    SetChrPos(0x11, -10530, 0, 1180, 90)
    SetChrPos(0x12, -3480, 0, 2530, 340)
    SetChrPos(0x13, -2870, 0, -3210, 290)
    SetChrPos(0x14, -5740, 0, 3660, 70)
    SetChrPos(0x15, -4630, 0, 2520, 25)
    SetChrPos(0x16, 5000, 0, 2290, 270)
    SetChrPos(0x8, 3180, 0, 9920, 308)
    SetChrPos(0x9, 1230, 0, 9680, 0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 680, 0, 3780, 25)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 820, 0, 7140, 160)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -200, 0, 4660, 70)
    SetChrChipByIndex(0x20, 0x28)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -6170, 0, -3230, 70)
    SetChrChipByIndex(0x21, 0x29)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -3630, 0, -4340, 335)
    SetChrChipByIndex(0x22, 0x2A)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -5180, 0, -4080, 25)
    SetChrChipByIndex(0x23, 0x2B)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -6160, 0, -1580, 115)
    BeginChrThread(0x1D, 0, 0, 0)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    BeginChrThread(0x20, 0, 0, 0)
    BeginChrThread(0x21, 0, 0, 0)
    BeginChrThread(0x22, 0, 0, 0)
    BeginChrThread(0x23, 0, 0, 0)
    BeginChrThread(0x1A, 0, 0, 0)
    BeginChrThread(0x1B, 0, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1460, 880, 10670, 180)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -3880, 0, 8840, 180)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -4600, 0, -520, 180)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3140, 0, 6130, 245)
    SetChrChipByIndex(0xD, 0x5)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2290, 0, 4950, 245)
    BeginChrThread(0x18, 0, 0, 0)
    BeginChrThread(0x1C, 0, 0, 0)
    BeginChrThread(0x19, 0, 0, 0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -4880, 0, 5930, 155)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -230, 0, 6070, 110)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -2790, 0, -1720, 245)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2900, 0, -2250, 290)
    SetChrPos(0x101, 3000, 0, -1000, 245)
    SetChrPos(0x102, 2000, 0, -3250, 335)
    SetChrPos(0x103, 550, 0, -3270, 20)
    SetChrPos(0x104, -400, 0, -2400, 65)
    SetChrPos(0x109, -550, 0, -970, 110)
    SetChrPos(0x105, 600, 0, 100, 155)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x1A, -5310, 0, 8840, 180)
    PlayBGM("ed7162", 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToBright(2000, 0)
    OP_68(-1240, 2250, 12460, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(29120, 0)
    Sleep(2000)
    OP_68(-1980, 1500, 6460, 10000)
    MoveCamera(62, 23, 0, 10000)
    OP_6E(380, 10000)
    Sleep(10000)
    Fade(500)
    OP_68(-5990, 1500, 630, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29120, 0)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)
    OP_95(0x17, -6030, 0, 980, 3000, 0x0)
    OP_95(0x17, -7300, 0, 1270, 3000, 0x0)
    Sleep(1000)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)

    def lambda_303C():
        OP_95(0xFE, -8350, 0, 6120, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_303C)
    Sleep(1000)
    Fade(500)
    OP_68(1040, 1700, -1990, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21120, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FHmm... Ries has been\x01",
            "sampling the food this\x01",
            "whole time.\x02\x03",
            "#00012FShe stands out quite a\x01",
            "bit in her sister\x01",
            "outfit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*... You're\x01",
            "right.\x02\x03",
            "#00102FBut the food really is\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FIt seems like every restaurant\x01",
            "in the city provided food for\x01",
            "this buffet.\x02\x03",
            "#00309FOver there is some spicy mapo\x01",
            "from The Old Dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FOh, I've got to get some\x01",
            "of that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha... You guys are\x01",
            "really close, aren't\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_324D():

        label("loc_324D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_324D")

    QueueWorkItem2(0x109, 0, lambda_324D)

    def lambda_325F():

        label("loc_325F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_325F")

    QueueWorkItem2(0x102, 0, lambda_325F)

    def lambda_3271():

        label("loc_3271")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3271")

    QueueWorkItem2(0x104, 0, lambda_3271)

    def lambda_3283():

        label("loc_3283")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3283")

    QueueWorkItem2(0x101, 0, lambda_3283)

    def lambda_3295():

        label("loc_3295")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3295")

    QueueWorkItem2(0x105, 0, lambda_3295)

    def lambda_32A7():

        label("loc_32A7")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_32A7")

    QueueWorkItem2(0x103, 0, lambda_32A7)

    ChrTalk(
        0xE,
        (
            "With food this good, the\x01",
            "event has to be a\x01",
            "success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHaha... I hope it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey... This event is for\x01",
            "charity. Don't be such a\x01",
            "downer.\x02\x03",
            "#00000FBut even so, aren't you\x01",
            "worried about participating\x01",
            "in the pageant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI think HQ is plenty\x01",
            "busy dealing with the\x01",
            "attack, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, well... I was\x01",
            "unsure too when I was\x01",
            "first invited, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Chief Joe Ridge, my\x01",
            "boss, said I should\x01",
            "participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha, is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In times like these, we\x01",
            "want to grow closer to\x01",
            "the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, I guess we're\x01",
            "copying all of you, in a\x01",
            "sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, we're not all\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(803, 2, 100, 0)
    Sleep(500)

    ChrTalk(
        0xE,
        "Ah... It's me. Sorry.\x02",
    )

    CloseMessageWindow()
    OP_95(0xE, 4600, 0, -1680, 2000, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)
    OP_0D()
    Fade(250)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0xE, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Yes, this is Officer\x01",
            "Kate... Good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...Yes, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I see. Understood.\x01",
            "I'll be right there.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)
    OP_95(0xE, 2900, 0, -2250, 2000, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005FOfficer Kate, was\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Hmm... Sorry, but it's\x01",
            "urgent. I've got to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm really sorry, but I\x01",
            "won't be able to appear\x01",
            "in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAww, seriously!?\x02\x03",
            "#00301FWell if it's for work, I\x01",
            "guess it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 500)

    ChrTalk(
        0xE,
        (
            "Sorry, I've got to go\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Can you apologize for\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, got it. Thanks,\x01",
            "Officer Kate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Thanks.\x02",
    )

    CloseMessageWindow()
    OP_68(760, 1700, -3000, 3000)
    BeginChrThread(0xE, 3, 0, 25)
    Sleep(4000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)
    OP_4B(0x1B, 0xFF)
    BeginChrThread(0x1B, 3, 0, 26)

    ChrTalk(
        0x102,
        (
            "#00106FHmm. I wanted to talk\x01",
            "with her a little more.\x01",
            "Too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah...\x02",
    )

    CloseMessageWindow()
    OP_68(1040, 1700, -1990, 2000)
    MoveCamera(38, 23, 0, 2000)
    WaitChrThread(0x1B, 3)
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        (
            "Hey everyone. Enjoying\x01",
            "yourselves?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38B8():

        label("loc_38B8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_38B8")

    QueueWorkItem2(0x109, 0, lambda_38B8)

    def lambda_38CA():

        label("loc_38CA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_38CA")

    QueueWorkItem2(0x102, 0, lambda_38CA)

    def lambda_38DC():

        label("loc_38DC")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_38DC")

    QueueWorkItem2(0x104, 0, lambda_38DC)

    def lambda_38EE():

        label("loc_38EE")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_38EE")

    QueueWorkItem2(0x101, 0, lambda_38EE)

    def lambda_3900():

        label("loc_3900")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3900")

    QueueWorkItem2(0x105, 0, lambda_3900)

    def lambda_3912():

        label("loc_3912")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3912")

    QueueWorkItem2(0x103, 0, lambda_3912)

    ChrTalk(
        0x1B,
        (
            "The pagent is about to\x01",
            "start. Can you guys help me\x01",
            "gather the participants?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "...Wait, what? What\x01",
            "about the policewoman\x01",
            "who was here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F...Huh? Where's the\x01",
            "policewoman?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that Kate was\x01",
            "called away due to an\x01",
            "emergency.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)

    ChrTalk(
        0x1B,
        "W-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Hmm, that's a problem.\x01",
            "What should I do about\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "...Oh, that's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Can one of you fill the\x01",
            "policewoman role?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FWhaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FYou mean us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, now this is\x01",
            "getting interesting.\x02\x03",
            "You won't get many\x01",
            "chances like this. Why\x01",
            "not try it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FT-This isn't your\x01",
            "problem, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "P-Please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "In addition to fundraising for\x01",
            "reconstruction, this event is\x01",
            "to cheer up the citizens, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Please! For the people\x01",
            "of Crossbell!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x109)

    ChrTalk(
        0x102,
        (
            "#00106F...*sigh*, I suppose.\x02\x03",
            "#00100FWhat do you think,\x01",
            "everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...No objections.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FI'm really a guardsman.\x01",
            "If that's all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "T-Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Alright then... Who's\x01",
            "going to appear in the\x01",
            "pageant?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00309FHow 'bout you pick,\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E77)

    def lambda_3E84():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E84)

    def lambda_3E91():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E91)

    def lambda_3E9E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E9E)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00011FM-Me!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, I think it's only\x01",
            "natural that you do your duty\x01",
            "as Support Section leader.\x02\x03",
            "#10302FThat'll avoid animosity in\x01",
            "the future. Looks like time\x01",
            "is short too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FO-Ok, fine then...\x02\x03",
            "#00003FHmm. Then, the one\x01",
            "who'll appear in the\x01",
            "pageant is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4953")
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
            "Who will appear in the pageant?\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Lloyd")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4032")
    MenuCmd(3, 0, 0x0)

    label("loc_4032")

    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4057")
    MenuCmd(3, 0, 0x3)

    label("loc_4057")

    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4074")
    MenuCmd(3, 0, 0x5)

    label("loc_4074")

    MenuCmd(2, 0, -1, 80, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40BD"),
        (3, "loc_427D"),
        (5, "loc_4413"),
        (1, "loc_4661"),
        (2, "loc_4760"),
        (4, "loc_4851"),
        (SWITCH_DEFAULT, "loc_494E"),
    )


    label("loc_40BD")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001F...I understand. If\x01",
            "that's how it's going to\x01",
            "be, then I'll go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4114():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4114)

    def lambda_4121():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4121)

    def lambda_412E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_412E)

    def lambda_413B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_413B)

    def lambda_4148():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4148)

    ChrTalk(
        0x102,
        "#00105FHuh... Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F...So you plan to don\x01",
            "female clothing, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FNo, no. I mean, maybe\x01",
            "he'll look good in them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FHmm. That's a strange\x01",
            "fashion sense.\x02\x03",
            "#10300FYou have broad shoulders\x01",
            "so you should be able to\x01",
            "manage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10114F(So excited...)\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 0)
    Jump("loc_494E")

    label("loc_427D")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00001F...Randy, can you go?\x02",
    )

    CloseMessageWindow()

    def lambda_42AB():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42AB)

    def lambda_42B8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_42B8)

    def lambda_42C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_42C5)

    def lambda_42D2():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42D2)

    def lambda_42DF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_42DF)

    ChrTalk(
        0x104,
        "#00305F...S-Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FR-Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...I just imagined\x01",
            "something terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FHmm, with the right\x01",
            "makeup and clothing,\x01",
            "he'd look pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FThis won't work...\x01",
            "You're too big, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, boo-hoo... Come on,\x01",
            "you're all against it?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 1)
    Jump("loc_494E")

    label("loc_4413")

    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00001F...Wazy. Will you go?\x02",
    )

    CloseMessageWindow()

    def lambda_4441():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4441)

    def lambda_444E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_444E)

    def lambda_445B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_445B)

    def lambda_4468():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4468)

    def lambda_4475():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4475)

    ChrTalk(
        0x105,
        (
            "#10302FHaha... I don't\x01",
            "particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FH-Hey, Wazy? Why aren't\x01",
            "you against this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FWell, because it looks\x01",
            "kind of interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWhy are you being like\x01",
            "this, Lloyd!?\x02\x03",
            "I-It's like you're saying\x01",
            "Wazy has more sex appeal\x01",
            "than any of us do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FN-No, I'm not saying\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha. You kind of are,\x01",
            "in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Randy. Are you going\x01",
            "to talk or are you going\x01",
            "to shut up. Which is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F...Sorry.\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 2)
    Jump("loc_494E")

    label("loc_4661")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00000F...Elie. Can you go?\x02",
    )

    CloseMessageWindow()

    def lambda_468E():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_468E)

    def lambda_469B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_469B)

    def lambda_46A8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46A8)

    def lambda_46B5():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46B5)

    def lambda_46C2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_46C2)

    ChrTalk(
        0x102,
        (
            "#00112FM-Me!?\x02\x03",
            "#00113FHmm... T-That's right, I\x01",
            "understand.\x02\x03",
            "#00100FIt's a little\x01",
            "embarrassing, but...\x01",
            "I'll do what I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x6)
    SetScenarioFlags(0x19A, 1)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_494E")

    label("loc_4760")

    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000F...Tio. Can you go?\x02",
    )

    CloseMessageWindow()

    def lambda_478C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_478C)

    def lambda_4799():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4799)

    def lambda_47A6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_47A6)

    def lambda_47B3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_47B3)

    def lambda_47C0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_47C0)

    ChrTalk(
        0x103,
        (
            "#00205FM-Me, you say?\x02\x03",
            "#00204F...I-I understand.\x02\x03",
            "#00201FIt's a little\x01",
            "embarrassing, but I'll\x01",
            "do what I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x7)
    SetScenarioFlags(0x19A, 2)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_494E")

    label("loc_4851")

    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000F...Noｱl. Can you go?\x02",
    )

    CloseMessageWindow()

    def lambda_487E():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_487E)

    def lambda_488B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_488B)

    def lambda_4898():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4898)

    def lambda_48A5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_48A5)

    def lambda_48B2():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_48B2)

    ChrTalk(
        0x109,
        (
            "#10114FM-Me!? Hmm...\x02\x03",
            "#10103F...R-Roger that!\x02\x03",
            "#10102FI'm not very used to\x01",
            "things like this, but...\x01",
            "I'll do what I can!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x8)
    SetScenarioFlags(0x19A, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_494E")

    label("loc_494E")

    Jump("loc_3FC7")

    label("loc_4953")


    ChrTalk(
        0x104,
        (
            "#00302FHaha, you'll get the\x01",
            "hang of it once you're\x01",
            "on stage, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FTo be honest, I think there's a\x01",
            "different level of tension between\x01",
            "this and combat or investigations.\x02\x03",
            "#10302FAnd we don't have uniforms which\x01",
            "puts us at a disadvantage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, how about we pitch\x01",
            "you guys as "plainclothes\x01",
            "officers" then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "...If only we had a real\x01",
            "policewoman... What a\x01",
            "shame...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(This is getting\x01",
            "weird...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4BC8")

    ChrTalk(
        0x109,
        (
            "#10102FFor now anyway, let's\x01",
            "focus on making this\x01",
            "event a success!\x02\x03",
            "#10109FGo for it, Elie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHaha, I'll be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, I'll get through\x01",
            "this somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D57")

    label("loc_4BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4C8C")

    ChrTalk(
        0x102,
        (
            "#00102FAnyway, let's think of\x01",
            "how to make the event a\x01",
            "success!\x02\x03",
            "#00109FGo for it, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYeah, I've got your back\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FYes, I'll get through\x01",
            "this somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D57")

    label("loc_4C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4D57")

    ChrTalk(
        0x103,
        (
            "#00204FAnyway, let's think of\x01",
            "how to make the event a\x01",
            "success!\x02\x03",
            "#00202FPlease do your best,\x01",
            "Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I'll be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, I'll get through\x01",
            "this somehow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D57")


    ChrTalk(
        0x1B,
        (
            "─Come, we don't have\x01",
            "much time. Let's make\x01",
            "arrangements backstage!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x335)
    OP_24(0x36D)
    Call(0, 28)
    Return()

    # Function_24_2AE8 end

    def Function_25_4DCA(): pass

    label("Function_25_4DCA")

    OP_95(0xFE, 3050, 0, -3910, 3000, 0x0)
    OP_95(0xFE, 1400, 0, -4710, 3000, 0x0)
    OP_95(0xFE, -1250, 0, -5460, 3000, 0x0)
    OP_95(0xFE, -940, 130, -7420, 3000, 0x0)
    OP_95(0xFE, 3690, 3560, -7710, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_4DCA end

    def Function_26_4E34(): pass

    label("Function_26_4E34")

    SetChrPos(0xFE, -3350, 0, 1340, 0)
    OP_95(0xFE, 1650, 0, 1870, 2000, 0x0)
    OP_95(0xFE, 3130, 0, 520, 2000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_4E34 end

    def Function_27_4E75(): pass

    label("Function_27_4E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAF")

    ChrTalk(
        0x1B,
        (
            "Ahh, you're not serious,\x01",
            "are you!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EC5")

    label("loc_4EAF")


    ChrTalk(
        0x1B,
        "I'm telling you!\x02",
    )

    CloseMessageWindow()

    label("loc_4EC5")


    ChrTalk(
        0x1B,
        (
            "It's a pageant! Men\x01",
            "can't appear!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Pick someone else!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FU-Understood.\x02\x03",
            "#00008FUmm, then the one who\x01",
            "will appear in the\x01",
            "pagent is...\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_27_4E75 end

    def Function_28_4F5F(): pass

    label("Function_28_4F5F")

    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x18, 0xFF)
    EndChrThread(0x1C, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x1A, 0xFF)
    SetChrPos(0xC, -4460, 750, 16000, 180)
    SetChrPos(0xD, -3460, 750, 16000, 180)
    SetChrPos(0x18, -2460, 750, 16000, 180)
    SetChrPos(0x1C, -1460, 750, 16000, 180)
    SetChrPos(0x19, -460, 750, 16000, 180)
    SetChrPos(0x17, 540, 750, 16000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_501A")
    LoadChrToIndex("chr/ch00155.itc", 0x1E)
    SetChrPos(0x102, 1540, 750, 16000, 180)
    Jump("loc_505F")

    label("loc_501A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_503F")
    LoadChrToIndex("chr/ch00255.itc", 0x1E)
    SetChrPos(0x103, 1540, 750, 16000, 180)
    Jump("loc_505F")

    label("loc_503F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_505F")
    LoadChrToIndex("chr/ch02955.itc", 0x1E)
    SetChrPos(0x109, 1540, 750, 16000, 180)

    label("loc_505F")

    SetChrFlags(0xF, 0x80)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1310, 7400, 11320, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19820, 0)
    OP_68(-1310, 2500, 11320, 5000)
    MoveCamera(0, 11, 0, 5000)
    SetCameraDistance(20760, 5000)
    FadeToBright(2000, 0)
    SetChrPos(0x1B, -5720, 750, 13840, 180)
    OP_95(0x1B, -1530, 750, 12520, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1520, 880, 10600, 1000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        "Ladies and gentlemen!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "You've waited forever\x01",
            "for this! It's today's\x01",
            "main event!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "I would like to open the\x01",
            ""Miss Crossbell Contest\x01",
            "～Working Women Forever～"!!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x1B,
        (
            "Let me explain how the\x01",
            "contest is going to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Starting now, each of the\x01",
            "participants is going to appear\x01",
            "and deliver their appeal message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The appeal messages will\x01",
            "be a greeting used at work\x01",
            "or a trade expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Please write the name of\x01",
            "the most charming girl\x01",
            "on your ballot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "And the girl with the most\x01",
            "votes will be awarded the\x01",
            "title of "Miss Crossbell"!!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "─Well then, let's get\x01",
            "started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Appeal time... start!!!\x02",
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    Fade(500)
    OP_68(-1450, 2250, 14880, 0)
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    OP_95(0x1B, -2180, 750, 13210, 3000, 0x0)
    OP_95(0x1B, -5730, 750, 13620, 3000, 0x0)
    OP_93(0x1B, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x1B,
        (
            "First up is entry number\x01",
            "1!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The trim and sweet Times\x01",
            "Department Store clerk─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Cynthia!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 29)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xC,
        (
            "Welcome to Times\x01",
            "Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If there's anything you're\x01",
            "not sure about, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xC, 0, 0, 31)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "Amaaazing!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "How many people has she\x01",
            "knocked out with that\x01",
            "professional attitude!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "By the way, she's single! Who\x01",
            "out there is going to make\x01",
            "this lovely lady happy!?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x1B,
        (
            "─On to the next one!\x01",
            "Entry number 2!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A lone rose with charm\x01",
            "like a butterfly dancing\x01",
            "the Back Street night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Iris!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 0, 0, 29)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0xD,
        "Thank you! I'm Iris!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Have a lot to drink\x01",
            "today, okay? ─*kiss*㈱\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xD, 0, 0, 32)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "Bravo!! To think she'd\x01",
            "blow us a kiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The store where you can\x01",
            "drink with Iris is on\x01",
            "Back Street!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "However, alcohol is for\x01",
            "adults only! Keep that\x01",
            "in mind, folks!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x1B,
        (
            "─Let's keep up the\x01",
            "energy! It's entry\x01",
            "number 3!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The longtime waitress at The\x01",
            "Old Dragon, and angel who\x01",
            "flew down from the East─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Shanshan!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 29)
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x18,
        (
            "Hello! Welcome to our\x01",
            "store, ladies and\x01",
            "gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Papa's cooking is the\x01",
            "best around. Order a\x01",
            "lot, ok?㈱\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x18, 0, 0, 33)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "Oh my Goddess, did you\x01",
            "see that carefree\x01",
            "smile!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Poster girl Shanshan here is\x01",
            "very popular on East Street.\x01",
            "I am personally a huge fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "However, her dad\x01",
            "Zhanghui won't forgive\x01",
            "you if you try anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Please, those prepared\x01",
            "to throw away their very\x01",
            "lives only!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x1B,
        (
            "─Then on to entry number\x01",
            "4!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The lovely orbal\x01",
            "mechanic of Orbal Store\x01",
            "Genten─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Wendy!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1C, 0, 0, 29)
    WaitChrThread(0x1C, 0)

    ChrTalk(
        0x1C,
        (
            "...Ahem. I can't say I'm\x01",
            "all that clever, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "If your orbments are\x01",
            "broken or whatever, I'm\x01",
            "your girl!\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x1C, 0, 0, 34)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "How reliable! That gives\x01",
            "this girl a certain\x01",
            "charm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Careful not to break\x01",
            "your orbments just so\x01",
            "you can see her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "If you do, she'll punish\x01",
            "you with her spanner!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0)

    ChrTalk(
        0x1B,
        (
            "Wouldn't you know it?\x01",
            "We're already at entry\x01",
            "number 5!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The industrious maid who\x01",
            "serves Crossbell Chairman\x01",
            "Henry MacDowell─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Joanna!\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x19, 0, 0, 30)
    WaitChrThread(0x19, 0)
    OP_64(0x19)

    ChrTalk(
        0x19,
        "...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "...U-Um...\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x19)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x19,
        "W-Welcome home, master.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "...E-Excuse me, then.\x02",
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "Ohhhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "What a fresh feeling! I\x01",
            "like this kind of maid,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "I bet some of our audience\x01",
            "are even starting to hate\x01",
            "Mr. MacDowell!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5D75")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5D75")

    Sleep(1000)
    WaitChrThread(0x19, 0)

    ChrTalk(
        0x1B,
        (
            "We're almost there! It's\x01",
            "entry number 6!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A pure-hearted initiate\x01",
            "and servant of the Sky\x01",
            "Goddess─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Ries!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x17, 0, 0, 30)
    WaitChrThread(0x17, 0)
    Fade(250)
    Sound(802, 0, 90, 0)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    OP_A1(0x17, 0x5DC, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x17,
        (
            "The Septian Teachings\x01",
            "lie within the hearts of\x01",
            "mankind.\x02\x03",
            "May the Goddess guide\x01",
            "you all...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(500)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x17, 0, 0, 36)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "O-Ohhh! What a divine\x01",
            "presence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "It's totally different\x01",
            "from the girl sampling\x01",
            "the buffet food earlier!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0)

    ChrTalk(
        0x1B,
        (
            "Last but not least, it's\x01",
            "entry number 7!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5FD6")

    ChrTalk(
        0x1B,
        (
            "A member of the police's Special\x01",
            "Support Section, a young lady\x01",
            "with an honorable lineage─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Elie MacDowell!\x02",
    )

    CloseMessageWindow()
    Jump("loc_60D0")

    label("loc_5FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_604C")

    ChrTalk(
        0x1B,
        (
            "The girl with a quiet aura\x01",
            "assigned to the police's\x01",
            "Special Support Section─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Tio Plato!\x02",
    )

    CloseMessageWindow()
    Jump("loc_60D0")

    label("loc_604C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_60D0")

    ChrTalk(
        0x1B,
        (
            "Transferee to the police's Special\x01",
            "Support Section and CGF guardsman\x01",
            "with a sense of justice─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Noｱl Seeker!\x02",
    )

    CloseMessageWindow()

    label("loc_60D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_60E8")
    BeginChrThread(0x102, 0, 0, 30)
    WaitChrThread(0x102, 0)
    Jump("loc_6113")

    label("loc_60E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6100")
    BeginChrThread(0x103, 0, 0, 30)
    WaitChrThread(0x103, 0)
    Jump("loc_6113")

    label("loc_6100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6113")
    BeginChrThread(0x109, 0, 0, 30)
    WaitChrThread(0x109, 0)

    label("loc_6113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_62FE")

    ChrTalk(
        0x102,
        (
            "#00105F(Umm... I think I have\x01",
            "to give an appeal\x01",
            "message.)\x02\x03",
            "#00103F(What I should say?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Declaration of arrest\x01",       # 0
            "Appeal with gun skills\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x102, 0x2)
    OP_A1(0x102, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x102, 0x640, 0x6, 0x0, 0x0, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x102, 0x640, 0x8, 0x7, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6237"),
        (1, "loc_6297"),
        (SWITCH_DEFAULT, "loc_62F9"),
    )


    label("loc_6237")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x102,
        (
            "#00107F─Hands up!\x02\x03",
            "On all manner of charges\x01",
            "under state law, you're\x01",
            "under arrest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F9")

    label("loc_6297")


    ChrTalk(
        0x102,
        (
            "#00104F─*sigh*... Bullseye.\x02\x03",
            "#00101FIf you're thinking of\x01",
            "escaping, you're dead\x01",
            "wrong!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F9")

    label("loc_62F9")

    Jump("loc_6744")

    label("loc_62FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_653F")

    ChrTalk(
        0x103,
        (
            "#00200F(Now then... I have to\x01",
            "give an appeal message\x01",
            "or something.)\x02\x03",
            "#00203F(What should I say?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Declaration of arrest\x01",        # 0
            "Appeal with Aeon System\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x103, 0x2)
    OP_A1(0x103, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(533, 0, 80, 0)
    OP_A1(0x103, 0x640, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_A1(0x103, 0x640, 0x3, 0x8, 0x9, 0xA)
    Sound(337, 0, 70, 0)
    OP_A1(0x103, 0x640, 0x5, 0xB, 0xC, 0xD, 0xE, 0xF)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_643E"),
        (1, "loc_64BA"),
        (SWITCH_DEFAULT, "loc_653A"),
    )


    label("loc_643E")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x103,
        (
            "#00203F─Data collection\x01",
            "complete. The criminal\x01",
            "is... you.\x02\x03",
            "#00201FIt's too late to run.\x01",
            "Surrender peacefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653A")

    label("loc_64BA")


    ChrTalk(
        0x103,
        (
            "#00203F─Aeon System,\x01",
            "activate... Orbal field,\x01",
            "rapid deployment.\x02\x03",
            "#00201FI'll show you the power\x01",
            "of this orbal staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653A")

    label("loc_653A")

    Jump("loc_6744")

    label("loc_653F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6744")

    ChrTalk(
        0x109,
        (
            "#10105F(Umm... I think I have\x01",
            "to give an appeal\x01",
            "message.)\x02\x03",
            "#10103F(What should I say?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Declaration of arrest\x01",      # 0
            "Appeal with CGF order\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x109, 0x2)
    OP_A1(0x109, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0x3, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x109, 0x640, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA)
    Sound(590, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0xB, 0xC, 0xD, 0xC, 0xB)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_666F"),
        (1, "loc_66DF"),
        (SWITCH_DEFAULT, "loc_6744"),
    )


    label("loc_666F")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x109,
        (
            "#10101F─You're completely\x01",
            "surrounded... There's no\x01",
            "escape!\x02\x03",
            "#10107FPlease, surrender\x01",
            "immediately!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6744")

    label("loc_66DF")


    ChrTalk(
        0x109,
        (
            "#10101F─Intercept the enemy\x01",
            "armor unit and rescue\x01",
            "the supply unit!\x02\x03",
            "#10107FBegin combat!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6744")

    label("loc_6744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_67A2")
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)

    ChrTalk(
        0x1B,
        "Oh... Bravo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "You all got to see a\x01",
            "police woman in action!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67E8")

    label("loc_67A2")

    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)

    ChrTalk(
        0x1B,
        "Oh... Bravo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Hmm, she showed us\x01",
            "something good!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6860")

    ChrTalk(
        0x102,
        (
            "#00106F(H-Hmm... Maybe I should have\x01",
            "said something like what a\x01",
            "policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6938")

    label("loc_6860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_68CD")

    ChrTalk(
        0x103,
        (
            "#00206F(...Maybe I should have said\x01",
            "something more like what a\x01",
            "policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6938")

    label("loc_68CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6938")

    ChrTalk(
        0x109,
        (
            "#10106F(I messed up... Maybe if I\x01",
            "said something more like what\x01",
            "a policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6963")
    Fade(250)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x102, 0, 0, 37)
    WaitChrThread(0x102, 0)
    Jump("loc_69B4")

    label("loc_6963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_698E")
    Fade(250)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    BeginChrThread(0x103, 0, 0, 37)
    WaitChrThread(0x103, 0)
    Jump("loc_69B4")

    label("loc_698E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_69B4")
    Fade(250)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    BeginChrThread(0x109, 0, 0, 37)
    WaitChrThread(0x109, 0)

    label("loc_69B4")


    ChrTalk(
        0x1B,
        (
            "With this, all seven\x01",
            "appeals are finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Let's have a big round\x01",
            "of applause for all our\x01",
            "participants!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, the audience\x01",
            "voted to determine the\x01",
            "winner.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Before the voting, Sister\x01",
            "Ries withdrew, saying she\x01",
            "is not a Crossbell citizen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The audience proceeded\x01",
            "to select a winner from\x01",
            "the other participants.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000F(I received a ballot, but\x01",
            "putting down the name of my\x01",
            "colleague would be... you know.)\x02\x03",
            "#00003F(Alright... Who should I put\x01",
            "down?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Vote for Cynthia\x01",       # 0
            "Vote for Iris\x01",          # 1
            "Vote for Shanshan\x01",      # 2
            "Vote for Wendy\x01",         # 3
            "Vote for Joanna\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C7B"),
        (1, "loc_6CB6"),
        (2, "loc_6CEE"),
        (3, "loc_6D2A"),
        (4, "loc_6D63"),
        (SWITCH_DEFAULT, "loc_6D9D"),
    )


    label("loc_6C7B")


    AnonymousTalk(
        0x101,
        (
            "#00002F(Alright... I'll vote\x01",
            "for Cynthia.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x9)
    Jump("loc_6D9D")

    label("loc_6CB6")


    AnonymousTalk(
        0x101,
        (
            "#00002F(Alright... I'll vote\x01",
            "for Iris.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xA)
    Jump("loc_6D9D")

    label("loc_6CEE")


    AnonymousTalk(
        0x101,
        (
            "#00002F(Alright... I'll vote\x01",
            "for Shanshan.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xB)
    Jump("loc_6D9D")

    label("loc_6D2A")


    AnonymousTalk(
        0x101,
        (
            "#00002F(Alright... I'll vote\x01",
            "for Wendy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xC)
    Jump("loc_6D9D")

    label("loc_6D63")


    AnonymousTalk(
        0x101,
        (
            "#00002F(Alright... I'll vote\x01",
            "for Joanna.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xD)
    Jump("loc_6D9D")

    label("loc_6D9D")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-1450, 2250, 14880, 0)
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    StopBGM(0x7D0)
    WaitBGM()
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x17, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1450, 880, 10860, 180)
    SetChrPos(0x1B, -190, 750, 13500, 180)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "We've tallied the\x01",
            "results.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)
    OP_95(0x1A, -1450, 750, 12450, 2000, 0x0)
    OP_95(0x1A, 1620, 750, 12450, 2000, 0x0)
    OP_93(0x1A, 0xE0, 0x1F4)
    OP_95(0x1B, -1450, 750, 13500, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1450, 880, 11370, 2000, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "In the very first Miss\x01",
            "Crossbell contest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The one who will bask in\x01",
            "the light of glorious\x01",
            "victory iiis...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(420, 1, 80, 0)
    SetChrFlags(0x101, 0x48)
    SetChrFlags(0x105, 0x48)
    BeginChrThread(0x101, 1, 0, 38)
    BeginChrThread(0x105, 1, 0, 38)
    SetChrPos(0x101, 1540, 750, 16000, 180)
    SetChrPos(0x105, -4460, 750, 16000, 180)

    def lambda_6FBB():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FBB)

    def lambda_6FD5():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FD5)

    def lambda_6FEF():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6FEF)
    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    WaitChrThread(0x101, 0)

    def lambda_7014():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7014)

    def lambda_702E():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_702E)
    WaitChrThread(0x101, 0)

    def lambda_704C():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_704C)

    def lambda_7066():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7066)
    WaitChrThread(0x101, 0)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    StopEffect(0x1, 0x0)
    Sleep(1000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_70EC"),
        (1, "loc_7202"),
        (2, "loc_730C"),
        (3, "loc_7417"),
        (4, "loc_752F"),
        (SWITCH_DEFAULT, "loc_7647"),
    )


    label("loc_70EC")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xC, 1, 0, 38)

    def lambda_7100():

        label("loc_7100")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_7100")

    QueueWorkItem2(0x1B, 1, lambda_7100)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 1! It's\x01",
            "Cynthia!!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xC, 0, 0, 39)
    WaitChrThread(0xC, 0)
    EndChrThread(0xC, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    ChrTalk(
        0x1B,
        (
            "I award you this shield\x01",
            "to commemorate your\x01",
            "victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xC, 0xB4, 0x1F4)
    Jump("loc_7647")

    label("loc_7202")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xD, 1, 0, 38)

    def lambda_7216():

        label("loc_7216")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_7216")

    QueueWorkItem2(0x1B, 1, lambda_7216)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 2! It's\x01",
            "Iris!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xD, 0, 0, 39)
    WaitChrThread(0xD, 0)
    EndChrThread(0xD, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    ChrTalk(
        0x1B,
        (
            "I award you this shield\x01",
            "to commemorate your\x01",
            "victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uhuhu, thank you㈱\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xD, 0xB4, 0x1F4)
    Jump("loc_7647")

    label("loc_730C")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x18, 1, 0, 38)

    def lambda_7320():

        label("loc_7320")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_7320")

    QueueWorkItem2(0x1B, 1, lambda_7320)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 3! It's\x01",
            "Shanshan!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x18, 0, 0, 39)
    WaitChrThread(0x18, 0)
    EndChrThread(0x18, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    ChrTalk(
        0x1B,
        (
            "I award you this shield\x01",
            "to commemorate your\x01",
            "victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Ehehe, thanks~.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x18, 0xB4, 0x1F4)
    Jump("loc_7647")

    label("loc_7417")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x1C, 1, 0, 38)

    def lambda_742B():

        label("loc_742B")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_742B")

    QueueWorkItem2(0x1B, 1, lambda_742B)

    ChrTalk(
        0x1C,
        (
            "#4S─Entry number 4! It's\x01",
            "Wendy!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    OP_24(0x1A4)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x1C, 0, 0, 39)
    WaitChrThread(0x1C, 0)
    EndChrThread(0x1C, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    ChrTalk(
        0x1B,
        (
            "I award you this shield\x01",
            "to commemorate your\x01",
            "victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Ahaha, are you sure?\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x1C, 0xB4, 0x1F4)
    Jump("loc_7647")

    label("loc_752F")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x19, 1, 0, 38)

    def lambda_7543():

        label("loc_7543")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_7543")

    QueueWorkItem2(0x1B, 1, lambda_7543)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 5! It's\x01",
            "Joanna!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 0, 0, 39)
    WaitChrThread(0x19, 0)
    EndChrThread(0x19, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    ChrTalk(
        0x1B,
        (
            "I award you this shield\x01",
            "to commemorate your\x01",
            "victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "U-Umm, thank you... very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x19, 0xB4, 0x1F4)
    Jump("loc_7647")

    label("loc_7647")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7A89")
    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    ChrTalk(
        0x1B,
        (
            "Also, we have a judges'\x01",
            "special award for a\x01",
            "special entry!\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76D1"),
        (1, "loc_76F1"),
        (2, "loc_7711"),
        (3, "loc_7731"),
        (4, "loc_7751"),
        (SWITCH_DEFAULT, "loc_7771"),
    )


    label("loc_76D1")

    OP_96(0xC, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Jump("loc_7771")

    label("loc_76F1")

    OP_96(0xD, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xD, 0x87, 0x1F4)
    Jump("loc_7771")

    label("loc_7711")

    OP_96(0x18, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x18, 0x87, 0x1F4)
    Jump("loc_7771")

    label("loc_7731")

    OP_96(0x1C, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x1C, 0x87, 0x1F4)
    Jump("loc_7771")

    label("loc_7751")

    OP_96(0x19, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x19, 0x87, 0x1F4)
    Jump("loc_7771")

    label("loc_7771")

    OP_2C(0x8F, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_77C1")
    BeginChrThread(0x102, 1, 0, 38)

    def lambda_778A():

        label("loc_778A")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_778A")

    QueueWorkItem2(0x1B, 0, lambda_778A)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 7! It's\x01",
            "Elie!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7851")

    label("loc_77C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_780B")
    BeginChrThread(0x103, 1, 0, 38)

    def lambda_77D5():

        label("loc_77D5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_77D5")

    QueueWorkItem2(0x1B, 0, lambda_77D5)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 7! It's\x01",
            "Tio!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7851")

    label("loc_780B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7851")
    BeginChrThread(0x109, 1, 0, 38)

    def lambda_781F():

        label("loc_781F")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_781F")

    QueueWorkItem2(0x1B, 0, lambda_781F)

    ChrTalk(
        0x1B,
        (
            "#4S─Entry number 7! It's\x01",
            "Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7851")

    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    Sound(818, 0, 80, 0)
    Sound(820, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7890")
    BeginChrThread(0x102, 0, 0, 40)
    WaitChrThread(0x102, 0)
    EndChrThread(0x102, 0x1)
    Jump("loc_78C3")

    label("loc_7890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_78AC")
    BeginChrThread(0x103, 0, 0, 40)
    WaitChrThread(0x103, 0)
    EndChrThread(0x103, 0x1)
    Jump("loc_78C3")

    label("loc_78AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_78C3")
    BeginChrThread(0x109, 0, 0, 40)
    WaitChrThread(0x109, 0)
    EndChrThread(0x109, 0x1)

    label("loc_78C3")

    StopEffect(0x1, 0x0)

    ChrTalk(
        0x1B,
        (
            "The special award is\x01",
            "also a commemorative\x01",
            "plaque. ...Here you go!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7992")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x341, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00109FHaha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Jump("loc_7A7E")

    label("loc_7992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7A06")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x342, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00205FT-Thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Jump("loc_7A7E")

    label("loc_7A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7A7E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x343, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        "#10109FHaha, I'm honored.\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    label("loc_7A7E")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    label("loc_7A89")

    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0x18, 0xB4, 0x0)
    OP_93(0x1C, 0xB4, 0x0)
    OP_93(0x19, 0xB4, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    Fade(500)
    Fade(500)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    StopEffect(0x0, 0x0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x1B,
        (
            "That's all for the Miss\x01",
            "Crossbell pageant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The buffet will be reopening\x01",
            "afterward. Please enjoy\x01",
            "today's event, everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_6E(580, 3000)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And thusly, the charity\x01",
            "event pageant came to a\x01",
            "close.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    WaitBGM()
    OP_0D()
    OP_24(0x335)
    OP_24(0x36D)
    SetScenarioFlags(0x22, 1)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4F5F end

    def Function_29_7BDB(): pass

    label("Function_29_7BDB")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sleep(1000)
    Return()

    # Function_29_7BDB end

    def Function_30_7C19(): pass

    label("Function_30_7C19")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_30_7C19 end

    def Function_31_7C38(): pass

    label("Function_31_7C38")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -4460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_31_7C38 end

    def Function_32_7C69(): pass

    label("Function_32_7C69")

    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -3460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_7C69 end

    def Function_33_7C9D(): pass

    label("Function_33_7C9D")

    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -2460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_7C9D end

    def Function_34_7CD1(): pass

    label("Function_34_7CD1")

    OP_95(0xFE, -1460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_34_7CD1 end

    def Function_35_7CED(): pass

    label("Function_35_7CED")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_35_7CED end

    def Function_36_7D1E(): pass

    label("Function_36_7D1E")

    OP_95(0xFE, 540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_36_7D1E end

    def Function_37_7D3A(): pass

    label("Function_37_7D3A")

    OP_95(0xFE, 1540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_37_7D3A end

    def Function_38_7D56(): pass

    label("Function_38_7D56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA0")
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_38_7D56")

    label("loc_7DA0")

    Return()

    # Function_38_7D56 end

    def Function_39_7DA1(): pass

    label("Function_39_7DA1")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -1910, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_7DA1 end

    def Function_40_7DDB(): pass

    label("Function_40_7DDB")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 800, 750, 14930, 3000, 0x0)
    OP_95(0xFE, -1500, 750, 13910, 2000, 0x0)
    OP_95(0xFE, -1500, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_40_7DDB end

    def Function_41_7E3D(): pass

    label("Function_41_7E3D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1500, 900, 14300, 180)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(-1500, 2500, 14000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_41_7E3D end

    def Function_42_7F72(): pass

    label("Function_42_7F72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    LoadChrToIndex("chr/ch27702.itc", 0x1E)
    LoadChrToIndex("chr/ch27500.itc", 0x1F)
    LoadChrToIndex("chr/ch27802.itc", 0x20)
    LoadChrToIndex("chr/ch27600.itc", 0x21)
    LoadChrToIndex("chr/ch25900.itc", 0x22)
    LoadChrToIndex("chr/ch27502.itc", 0x23)
    LoadChrToIndex("chr/ch27602.itc", 0x24)
    LoadChrToIndex("chr/ch44202.itc", 0x25)
    LoadChrToIndex("chr/ch21002.itc", 0x26)
    LoadChrToIndex("chr/ch20302.itc", 0x27)
    SoundLoad(851)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x24, 2230, 900, 12630, 252)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x25, 2280, 750, 14110, 252)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x26, -5210, 900, 12820, 107)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x27, -3140, 750, 13930, 110)
    SetChrChipByIndex(0x27, 0x21)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x28, -340, 750, 14570, 180)
    SetChrChipByIndex(0x28, 0x22)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x1E, -5800, 150, 7350, 0)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1F, -4000, 150, 7350, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x20, -2250, 150, 7350, 0)
    SetChrChipByIndex(0x20, 0x23)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x21, -450, 150, 7350, 0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x22, 1250, 150, 7350, 0)
    SetChrChipByIndex(0x22, 0xE)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x23, 2930, 150, 7350, 0)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    EndChrThread(0x23, 0x0)
    SetChrBattleFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x15, 6880, 4000, 7260, 315)
    SetChrChipByIndex(0x15, 0xA)
    SetChrFlags(0x15, 0x8000)
    EndChrThread(0x15, 0x0)
    SetChrPos(0x16, 6880, 4000, -610, 315)
    SetChrChipByIndex(0x16, 0xC)
    SetChrFlags(0x16, 0x8000)
    OP_68(2390, 1500, -520, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(32530, 0)
    Sound(851, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1450, 2250, 12090, 5000)
    MoveCamera(40, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(30820, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1450, 2250, 12090, 0)
    MoveCamera(28, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22540, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x26,
        (
            "Foreigners, especially imperials and\x01",
            "republicans, are given preferential\x01",
            "treatment under the law!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "And we have to pay each\x01",
            "of the major powers 10%\x01",
            "of our hard-earned money!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "No matter how you think\x01",
            "about it, isn't that\x01",
            "just so strange!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "If we don't oppose them now, this\x01",
            "situation will go on forever! Why\x01",
            "can't you understand that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Are you really okay with\x01",
            "that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "...Hmph, what nonsense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Our real problem is that state\x01",
            "independence is too far out of reach\x01",
            "for the amount of power we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Suppose for example we're invaded\x01",
            "by a large country. How will the\x01",
            "CGF oppose them without tanks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "That large country\x01",
            "you're talking about is\x01",
            "the Empire, isn't it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "That the WMDs known as the Railway Cannons\x01",
            "have been deployed at Garrelia Fortress to\x01",
            "the west is a well-known fact!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "With Crossbell's wealth, we\x01",
            "could deploy plenty of military\x01",
            "airships, in addition to tanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Is not determination the\x01",
            "thing that's needed\x01",
            "here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "They're an unknown\x01",
            "quantity... I'm telling you\x01",
            "to look at reality here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "First and foremost, Crossbell's prosperity\x01",
            "is due in large part to the mira that\x01",
            "flows in from the Empire and Republic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "If walls are erected due to\x01",
            "independence, that wealth\x01",
            "will disappear, won't it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Now, now. Calm down,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "...Anyway, the problem is whether a high-\x01",
            "handed independence proposal like this will\x01",
            "be recognized by the international community.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Aren't we missing that\x01",
            "piece?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "This has nothing to do\x01",
            "with the international\x01",
            "community!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Crossbell State independence\x01",
            "is the only path whereby we\x01",
            "can have "justice"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "In the end, you're nothing\x01",
            "more than a convenient\x01",
            "shill for Calvard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I-It's true that I've been\x01",
            "called a member of the\x01",
            "Republican faction, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I'm confident my love of\x01",
            "Crossbell won't lose to\x01",
            "anyone's!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I'll have you take back\x01",
            "those words!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(6040, 5500, -5410, 0)
    MoveCamera(29, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21420, 0)
    SetChrPos(0x101, 6940, 4000, -3750, 315)
    SetChrPos(0x103, 6910, 4000, -4960, 315)
    SetChrPos(0x102, 8010, 4000, -4600, 315)
    SetChrPos(0x109, 7960, 4000, -5740, 315)
    SetChrPos(0x104, 4750, 4120, -6880, 0)
    SetChrPos(0x105, 5580, 4120, -8020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00300FEven on a rainy day like\x01",
            "today, it sure is lively\x01",
            "in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. More citizens than I thought are\x01",
            "participating too...\x02\x03",
            "#00003FBut influential Republican and Imperial faction\x01",
            "congressmen have been arguing more heatedly\x01",
            "lately with the new independence faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. I bet it reflects those\x01",
            "involved in Crossbell's\x01",
            "current political climate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FEach of their views\x01",
            "seems believable, at\x01",
            "least...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThis isn't a problem\x01",
            "that will be resolved so\x01",
            "easily.\x02\x03",
            "Also, these same\x01",
            "arguments are repeated\x01",
            "every decade or so.\x02\x03",
            "#00101FBut, a serious\x01",
            "conclusion might be\x01",
            "coming soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F...I agree.\x02\x03",
            "#10108F(Either a difficult\x01",
            "independence or a subordination\x01",
            "without justice, huh...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(821, 500, 90)
    SetScenarioFlags(0x17B, 6)
    SetScenarioFlags(0x22, 2)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_7F72 end

    SaveToFile()

Try(main)
