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
        "Function_6_B8F",          # 06, 6
        "Function_7_F61",          # 07, 7
        "Function_8_106B",         # 08, 8
        "Function_9_1314",         # 09, 9
        "Function_10_14C5",        # 0A, 10
        "Function_11_15CF",        # 0B, 11
        "Function_12_199B",        # 0C, 12
        "Function_13_1BD3",        # 0D, 13
        "Function_14_1E51",        # 0E, 14
        "Function_15_1F55",        # 0F, 15
        "Function_16_20B4",        # 10, 16
        "Function_17_220B",        # 11, 17
        "Function_18_22C0",        # 12, 18
        "Function_19_2406",        # 13, 19
        "Function_20_2511",        # 14, 20
        "Function_21_2603",        # 15, 21
        "Function_22_2674",        # 16, 22
        "Function_23_2779",        # 17, 23
        "Function_24_2B75",        # 18, 24
        "Function_25_4F23",        # 19, 25
        "Function_26_4F8D",        # 1A, 26
        "Function_27_4FCE",        # 1B, 27
        "Function_28_50B4",        # 1C, 28
        "Function_29_7EA2",        # 1D, 29
        "Function_30_7EE0",        # 1E, 30
        "Function_31_7EFF",        # 1F, 31
        "Function_32_7F30",        # 20, 32
        "Function_33_7F64",        # 21, 33
        "Function_34_7F98",        # 22, 34
        "Function_35_7FB4",        # 23, 35
        "Function_36_7FE5",        # 24, 36
        "Function_37_8001",        # 25, 37
        "Function_38_801D",        # 26, 38
        "Function_39_8068",        # 27, 39
        "Function_40_80A2",        # 28, 40
        "Function_41_8104",        # 29, 41
        "Function_42_8239",        # 2A, 42
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
            "  ～Why don't you try making it at home?～\x01",
            "　　　           \x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Sweet Chocolate recipe is written down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_B8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Sweet Chocolate"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B8B")

    TalkEnd(0xFF)
    Return()

    # Function_5_A5A end

    def Function_6_B8F(): pass

    label("Function_6_B8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF2")
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "#02102FAh, good work you guys!\x02\x03",
            "I'm interviewing the\x01",
            "pageant participants.\x02\x03",
            "#02109FUh uh, you'll go along with\x01",
            "it properly later too, riiight♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(H-Hmm. I'm sorry for her, but it looks\x01",
            "like this is going to take some time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. I think it's best if\x01",
            "we secretly sneak away.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    SetScenarioFlags(0x0, 4)
    Jump("loc_D68")

    label("loc_CF2")


    ChrTalk(
        0x8,
        (
            "#02105FOh, is that how it's going to be?\x02\x03",
            "#02100FI suppose I really\x01",
            "should visit your family\x01",
            "after the incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D68")

    Jump("loc_F5D")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEE")

    ChrTalk(
        0x8,
        "#02109FYahhoo, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMiss Grace... Are you covering\x01",
            "the charity event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02100FUh uh, you got it☆\x02\x03",
            "It looks pretty lively. I think\x01",
            "I'll be able to write an article to\x01",
            "encourage Crossbell citizens.\x02\x03",
            "#02103FThe scars from that attack\x01",
            "aren't gone yet...\x02\x03",
            "#02102FI've got to do what I\x01",
            "can at the pageant too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHa ha, please do your best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 6)
    Jump("loc_F5D")

    label("loc_EEE")


    ChrTalk(
        0x8,
        (
            "#02102FI heard the charity\x01",
            "event has an\x01",
            "interesting program...\x02\x03",
            "#02109FUh uh, it'll be the perfect scoop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5D")

    TalkEnd(0xFE)
    Return()

    # Function_6_B8F end

    def Function_7_F61(): pass

    label("Function_7_F61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FF1")

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
            "I've got a lot of great photos. I've\x01",
            "got to head back and sort them out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_FF1")


    ChrTalk(
        0xFE,
        (
            "The beautiful piano player who was\x01",
            "called to the charity event...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think this'll make a pretty good photo.\x02",
    )

    CloseMessageWindow()

    label("loc_1067")

    TalkEnd(0xFE)
    Return()

    # Function_7_F61 end

    def Function_8_106B(): pass

    label("Function_8_106B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(
        0xFE,
        (
            "Aah, I can't believe\x01",
            "Shanshan participated\x01",
            "in the pageant.\x02",
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
    Jump("loc_1181")

    label("loc_1122")


    ChrTalk(
        0xFE,
        (
            "But, for Shanshan to\x01",
            "participate in a pageant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I hope Master doesn't get angry.\x02",
    )

    CloseMessageWindow()

    label("loc_1181")

    Jump("loc_1310")

    label("loc_1186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(
        0xFE,
        (
            "I'm providing food from\x01",
            ""The Old Dragon"\x01",
            "for the charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Puck and Ruth are filling those\x01",
            "holes caused by my not being there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little worried, but\x01",
            "those two have become serious too,\x01",
            "so it'll probably be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1310")

    label("loc_1288")


    ChrTalk(
        0xFE,
        (
            "But... Shanshan has\x01",
            "been depressed lately.\x02",
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

    label("loc_1310")

    TalkEnd(0xFE)
    Return()

    # Function_8_106B end

    def Function_9_1314(): pass

    label("Function_9_1314")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1424")

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
            "...I'm worried about Rixia though,\x01",
            "but I'm sure she'll come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To welcome her with a smile when she returns,\x01",
            "I've got to cheer up and wait for her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_14BC")

    label("loc_1424")


    ChrTalk(
        0xFE,
        (
            "I'm worried about Rixia, but \x01",
            "I'm sure she'll come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To welcome her with a smile when she returns,\x01",
            "I've got to cheer up and wait for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BC")

    Jump("loc_14C1")

    label("loc_14C1")

    TalkEnd(0xFE)
    Return()

    # Function_9_1314 end

    def Function_10_14C5(): pass

    label("Function_10_14C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1574")

    ChrTalk(
        0xFE,
        (
            "*sigh*... Someone like me\x01",
            "got up on stage like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*... You were\x01",
            "very cute, Joanna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, how embarrassing...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_15C6")

    label("loc_1574")


    ChrTalk(
        0xFE,
        (
            "For someone like me to get up on stage\x01",
            "like that... Ooh, how embarrassing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")

    Jump("loc_15CB")

    label("loc_15CB")

    TalkEnd(0xFE)
    Return()

    # Function_10_14C5 end

    def Function_11_15CF(): pass

    label("Function_11_15CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_178B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173D")

    ChrTalk(
        0xFE,
        (
            "Hey, it's Lloyd and the Support Section!\x01",
            "You were pretty cool back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, I was very surprised when\x01",
            "you came out, but personally,\x01",
            "you're the winner for me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_16CE")

    ChrTalk(
        0x102,
        "#00109F*giggle*, thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1735")

    label("loc_16CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(
        0x103,
        "#00202FUh uh, thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1735")

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_1735")

    ChrTalk(
        0x109,
        "#10109FUh uh, thank you very much!\x02",
    )

    CloseMessageWindow()

    label("loc_1735")

    SetScenarioFlags(0x0, 6)
    Jump("loc_1786")

    label("loc_173D")


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
            "We've got plenty\x01",
            "of food left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1786")

    Jump("loc_1997")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FC")

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
            "Yeah, I left the store to Bennett\x01",
            "and her father and came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My baguettes are lined up on\x01",
            "the table there since there're also\x01",
            "many dishes that can go well with bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHmm, as expected from you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. You guys enjoy\x01",
            "yourselves too, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 7)
    Jump("loc_1997")

    label("loc_18FC")


    ChrTalk(
        0xFE,
        (
            "My baguettes are lined up on the\x01",
            "the table there since there're also\x01",
            "many dishes that can go well with bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys enjoy\x01",
            "yourselves too, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1997")

    TalkEnd(0xFE)
    Return()

    # Function_11_15CF end

    def Function_12_199B(): pass

    label("Function_12_199B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19AF")
    Jump("loc_1BCF")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_1A4B")

    ChrTalk(
        0xFE,
        (
            "Lloyd and friends. It looks like you've\x01",
            "assembled the pageant participants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, do your best out there.\x01",
            "I'll be rooting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCF")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B75")

    ChrTalk(
        0xFE,
        "My, if it isn't Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHuh, senior Kate?\x01",
            "What are you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, I'm helping out with\x01",
            "this event for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be up in a bit,\x01",
            "so I'm having\x01",
            "something to eat.\x02",
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
            "Oh, that's\x01",
            "still a secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, look\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 0)
    Jump("loc_1BCF")

    label("loc_1B75")


    ChrTalk(
        0xFE,
        (
            "I'll be up in a bit,\x01",
            "so I'm having\x01",
            "something to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, look\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCF")

    TalkEnd(0xFE)
    Return()

    # Function_12_199B end

    def Function_13_1BD3(): pass

    label("Function_13_1BD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(
        0x8,
        (
            "#02100FHmm, did your co-\x01",
            "workers suggest this?\x02",
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
            "Uh uh, a pageant stage is\x01",
            "really nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I was happy to receive\x01",
            "everyone's applause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I'm glad I participated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02104FHmm, hmm... (*scritch, scratch*)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DAF")

    label("loc_1CFA")


    ChrTalk(
        0xFE,
        (
            "Actually, I'm planning on returning\x01",
            "home to Remiferia before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I planned to head back immediately, but... I thought\x01",
            "this would have made a great story for my parents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAF")

    Jump("loc_1E4D")

    label("loc_1DB4")


    ChrTalk(
        0xFE,
        (
            "In the rest of the\x01",
            "program, I will have\x01",
            "to appear on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I am used to stand\x01",
            "before people because of work,\x01",
            "I am really nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4D")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BD3 end

    def Function_14_1E51(): pass

    label("Function_14_1E51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EE0")

    ChrTalk(
        0xFE,
        (
            "Aww, being adored by\x01",
            "other people is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was really fun. I'd like to\x01",
            "do it again if I get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F51")

    label("loc_1EE0")


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
        "Since I'm doing this, might as well aim for the top.\x02",
    )

    CloseMessageWindow()

    label("loc_1F51")

    TalkEnd(0xFE)
    Return()

    # Function_14_1E51 end

    def Function_15_1F55(): pass

    label("Function_15_1F55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_201A")

    ChrTalk(
        0xFE,
        (
            "Because of the pageant, we\x01",
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
    Jump("loc_20B0")

    label("loc_201A")


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
            "Please enjoy it\x01",
            "to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B0")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F55 end

    def Function_16_20B4(): pass

    label("Function_16_20B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_213E")

    ChrTalk(
        0xFE,
        (
            "All of the participants\x01",
            "were just so lovelyyy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew I should have put myself\x01",
            "out there for the maid role.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2207")

    label("loc_213E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_21CA")

    ChrTalk(
        0xFE,
        (
            "I am helping with the buffet party,\x01",
            "so I can't appear in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sorry, but please\x01",
            "look for someone else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2207")

    label("loc_21CA")


    ChrTalk(
        0xFE,
        (
            "If you would like food or\x01",
            "drink then please, have some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2207")

    TalkEnd(0xFE)
    Return()

    # Function_16_20B4 end

    def Function_17_220B(): pass

    label("Function_17_220B")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22A2")

    ChrTalk(
        0xF,
        (
            "I felt a pageant was\x01",
            "too vulgar, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Uh uh, it actually turned out to be quite fun.\x01",
            "Good work out there you guys too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BC")

    label("loc_22A2")


    ChrTalk(
        0xF,
        "What to play next...\x02",
    )

    CloseMessageWindow()

    label("loc_22BC")

    TalkEnd(0xF)
    Return()

    # Function_17_220B end

    def Function_18_22C0(): pass

    label("Function_18_22C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_234A")

    ChrTalk(
        0xFE,
        (
            "...Mmm, mmgh mgh... I guess\x01",
            "this is what I get for overeating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But for Crossbell City...\x01",
            "I'll eat anything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2402")

    label("loc_234A")


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

    label("loc_2402")

    TalkEnd(0xFE)
    Return()

    # Function_18_22C0 end

    def Function_19_2406(): pass

    label("Function_19_2406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_248A")

    ChrTalk(
        0xFE,
        "Ah, that was a sight for sore eyes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always knew the best appetizer \x01",
            "for drinks was beautiful women.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_248A")


    ChrTalk(
        0xFE,
        (
            "Mmm, the hall is full of\x01",
            "beautiful women somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this related to the centerpiece of\x01",
            "the program they're doing later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250D")

    TalkEnd(0xFE)
    Return()

    # Function_19_2406 end

    def Function_20_2511(): pass

    label("Function_20_2511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25CA")

    ChrTalk(
        0xFE,
        (
            "Uh uh, even though I'm a woman, I have to say\x01",
            "this place is full of nothing but attractive people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems this little one looks\x01",
            "up to working girls too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FF")

    label("loc_25CA")


    ChrTalk(
        0xFE,
        (
            "Now look here, you've got\x01",
            "ketchup on your lips.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FF")

    TalkEnd(0xFE)
    Return()

    # Function_20_2511 end

    def Function_21_2603(): pass

    label("Function_21_2603")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2644")

    ChrTalk(
        0xFE,
        "I... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think police\x01",
            "are cool!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2670")

    label("loc_2644")


    ChrTalk(
        0xFE,
        (
            "*chew, chew*...\x01",
            "Ehehe, this is good!♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2670")

    TalkEnd(0xFE)
    Return()

    # Function_21_2603 end

    def Function_22_2674(): pass

    label("Function_22_2674")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26F0")

    ChrTalk(
        0xFE,
        "The pageant was a lot of fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. If I were 30 years younger,\x01",
            "I could participate as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2775")

    label("loc_26F0")


    ChrTalk(
        0xFE,
        (
            "That piano song played earlier\x01",
            "had a nice sound to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like my feelings regarding\x01",
            "the attack have been put to rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2775")

    TalkEnd(0xFE)
    Return()

    # Function_22_2674 end

    def Function_23_2779(): pass

    label("Function_23_2779")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C0")

    ChrTalk(
        0x17,
        (
            "#04402FThank you for inviting\x01",
            "me, everyone.\x02\x03",
            "I don't think I could have had an interesting\x01",
            "experience like this at the Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, good work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI did want to\x01",
            "vote for you\x01",
            "though, dear Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#04406FAs someone who's not from Crossbell,\x01",
            "I just thought it would be wrong for\x01",
            "me to compete with the other girls.\x02\x03",
            "#04409FBut, thank you very much. \x01",
            "I'll take that as a compliment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Hmm. If you could vote for her,\x01",
            "I bet she'd have done pretty well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F(She's not aware of that, is she.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 1)
    Jump("loc_2B71")

    label("loc_29C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE9")

    ChrTalk(
        0x17,
        (
            "#04402FAlthough I declined to take part\x01",
            "in the voting, I thought it was\x01",
            "an interesting experience.\x02\x03",
            "#04404F*chew, chew*... Now\x01",
            "this is how you enjoy\x01",
            "a buffet party...\x02",
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
        "#00109F(*giggle*. That's Miss Ries for you.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2B71")

    label("loc_2AE9")


    ChrTalk(
        0x17,
        (
            "#04404F*chew, chew*... I'll head\x01",
            "back to the cathedral in\x01",
            "a little bit.\x02\x03",
            "#04402F...But for now, I want to\x01",
            "enjoy this buffet party.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B71")

    TalkEnd(0xFE)
    Return()

    # Function_23_2779 end

    def Function_24_2B75(): pass

    label("Function_24_2B75")

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

    def lambda_30C9():
        OP_95(0xFE, -8350, 0, 6120, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_30C9)
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
            "#00003FHmm... Miss Ries has been sampling\x01",
            "the food this whole time.\x02\x03",
            "#00012FShe stands out quite a\x01",
            "bit in her Sister outfit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*... You're right.\x02\x03",
            "#00102FBut the food really\x01",
            "is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FIt seems like every restaurant in the\x01",
            "city provided food for this buffet.\x02\x03",
            "#00309FOver there is some spicy\x01",
            "mapo from "The Old Dragon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FOh, I've got to\x01",
            "get some of that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh... You guys are\x01",
            "really close, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_32E2():

        label("loc_32E2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_32E2")

    QueueWorkItem2(0x109, 0, lambda_32E2)

    def lambda_32F4():

        label("loc_32F4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_32F4")

    QueueWorkItem2(0x102, 0, lambda_32F4)

    def lambda_3306():

        label("loc_3306")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3306")

    QueueWorkItem2(0x104, 0, lambda_3306)

    def lambda_3318():

        label("loc_3318")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_3318")

    QueueWorkItem2(0x101, 0, lambda_3318)

    def lambda_332A():

        label("loc_332A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_332A")

    QueueWorkItem2(0x105, 0, lambda_332A)

    def lambda_333C():

        label("loc_333C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_333C")

    QueueWorkItem2(0x103, 0, lambda_333C)

    ChrTalk(
        0xE,
        (
            "The food is this good too, the event\x01",
            "has to be a success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu... \x01",
            "I hope it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now... This event\x01",
            "is for charity. Don't\x01",
            "be such a downer.\x02\x03",
            "#00000FBut even so, aren't you\x01",
            "worried about participating\x01",
            "in the pageant, senior?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI think HQ is plenty busy\x01",
            "dealing with the attack...\x02",
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
            "Section Chief Joe Ridge,\x01",
            "my boss, said I should\x01",
            "absolutely participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In times like these,\x01",
            "we want to grow closer\x01",
            "to the citizens too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh, I guess we're copying\x01",
            "all of you, in a sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, we're\x01",
            "not all that great.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(803, 2, 100, 0)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Ah... It's mine.\x01",
            "Excuse me a moment.\x02",
        )
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
            "Yes, this is officer\x01",
            "Kate... Good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Yes, yes...\x01",
            "............\x02",
        )
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
        "#00005FSenior Kate, was that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Hmm... It's a pity,\x01",
            "but it's an urgent job.\x01",
            "I've got to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm really sorry, but\x01",
            "I won't be able to\x01",
            "appear in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAww, seriously!?\x02\x03",
            "#00301FWell if it's for work, I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 500)

    ChrTalk(
        0xE,
        (
            "Sorry, I've got to\x01",
            "go immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Can you apologize\x01",
            "for me to Mr. Roy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, got it. \x01",
            "Good work, senior Kate.\x02",
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
            "with her a little\x01",
            "more. Too bad.\x02",
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
            "Hey everyone.\x01",
            "Enjoying yourselves?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39B5():

        label("loc_39B5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_39B5")

    QueueWorkItem2(0x109, 0, lambda_39B5)

    def lambda_39C7():

        label("loc_39C7")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_39C7")

    QueueWorkItem2(0x102, 0, lambda_39C7)

    def lambda_39D9():

        label("loc_39D9")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_39D9")

    QueueWorkItem2(0x104, 0, lambda_39D9)

    def lambda_39EB():

        label("loc_39EB")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_39EB")

    QueueWorkItem2(0x101, 0, lambda_39EB)

    def lambda_39FD():

        label("loc_39FD")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_39FD")

    QueueWorkItem2(0x105, 0, lambda_39FD)

    def lambda_3A0F():

        label("loc_3A0F")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3A0F")

    QueueWorkItem2(0x103, 0, lambda_3A0F)

    ChrTalk(
        0x1B,
        (
            "The pageant is about to start.\x01",
            "Can you guys help me\x01",
            "gather the participants?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "...Wait, what?\x01",
            "What about the policewoman who was here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...Uhhm, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that Kate was called\x01",
            "away due to an emergency.\x07\x00\x02",
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
        "W-Whaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Hmm, that's a problem. \x01",
            "What should I do about this...\x02",
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
            "Can one of you fill\x01",
            "the policewoman role?\x02",
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
        "#00205FYou mean us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, now this is gettin' interesting.\x02\x03",
            "You won't get many chances\x01",
            "like this. Why not try it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FT-This isn't your problem, senior...\x02",
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
            "Please! For the\x01",
            "people of Crossbell!\x02",
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
            "#00100FWhat do you think, girls?\x02",
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
            "#10100FMy occupation is that of a CGF member,\x01",
            "but if you're fine with that, then...\x02",
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
            "Alright then... Who's going\x01",
            "to appear in the pageant?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00309FHow 'bout you\x01",
            "pick, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F8E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F8E)

    def lambda_3F9B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F9B)

    def lambda_3FA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FA8)

    def lambda_3FB5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FB5)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00011FM-Me!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, I think it's only natural that you do\x01",
            "your duty as the Support Section leader.\x02\x03",
            "#10302FThat'll avoid animosity in the future.\x01",
            "Looks like time is short too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FO-Ok, fine then...\x02\x03",
            "#00003FHmm. Then, the one who'll\x01",
            "appear in the pageant is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A59")
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
            "Who will appear in the pageant?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Lloyd")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4150")
    MenuCmd(3, 0, 0x0)

    label("loc_4150")

    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4175")
    MenuCmd(3, 0, 0x3)

    label("loc_4175")

    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4192")
    MenuCmd(3, 0, 0x5)

    label("loc_4192")

    MenuCmd(2, 0, -1, 80, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41DB"),
        (3, "loc_4381"),
        (5, "loc_451E"),
        (1, "loc_4750"),
        (2, "loc_4856"),
        (4, "loc_4957"),
        (SWITCH_DEFAULT, "loc_4A54"),
    )


    label("loc_41DB")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001F...I understand. If that's how\x01",
            "it's going to be, I'll go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_422D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_422D)

    def lambda_423A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_423A)

    def lambda_4247():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4247)

    def lambda_4254():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4254)

    def lambda_4261():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4261)

    ChrTalk(
        0x102,
        "#00105FEh... Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F...So you plan to don female clothing, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWell well, maybe he'll look good in 'em?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FHmm. This is delicate.\x02\x03",
            "#10300FYou have broad shoulders so you\x01",
            "should be able to manage...\x02",
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
    Jump("loc_4A54")

    label("loc_4381")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001F...Randy,\x01",
            "can you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43AF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_43AF)

    def lambda_43BC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_43BC)

    def lambda_43C9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_43C9)

    def lambda_43D6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43D6)

    def lambda_43E3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_43E3)

    ChrTalk(
        0x104,
        "#00305F...S-Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FR-Randy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...I just imagined\x01",
            "something horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FHmm, with the right\x01",
            "makeup and clothing,\x01",
            "he could be decent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FThat wouldn't really work...\x01",
            "You're too big, senior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTohoho... \x01",
            "Come on, you're all against it?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A54")

    label("loc_451E")

    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F...Wazy.\x01",
            "Will you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_454C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_454C)

    def lambda_4559():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4559)

    def lambda_4566():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4566)

    def lambda_4573():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4573)

    def lambda_4580():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4580)

    ChrTalk(
        0x105,
        (
            "#10302FHu hu... I don't\x01",
            "particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FH-Hey, Wazy? Why aren't\x01",
            "you opposing this?\x02",
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
            "#10101FMr. Lloyd too!\x02\x03",
            "I-It's like you're saying\x01",
            "Wazy has more sex appeal\x01",
            "than any of us do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FN-No, I'm not saying that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha. You kind of\x01",
            "are, in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Mr. Randy. \x01",
            "Will you shut up or made\x01",
            "to shut up? Which is it?\x02",
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
    Jump("loc_4A54")

    label("loc_4750")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00000F...Elie.\x01",
            "Can you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_477D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_477D)

    def lambda_478A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_478A)

    def lambda_4797():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4797)

    def lambda_47A4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_47A4)

    def lambda_47B1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_47B1)

    ChrTalk(
        0x102,
        (
            "#00112FM-Me!?\x02\x03",
            "#00113FHmm... T-That's\x01",
            "right, I understand.\x02\x03",
            "#00100FIt's a little embarrassing, but...\x01",
            "I'll try to do what I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x6)
    SetScenarioFlags(0x19A, 1)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4A54")

    label("loc_4856")

    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00000F...Tio. \x01",
            "Can you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4883():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4883)

    def lambda_4890():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4890)

    def lambda_489D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_489D)

    def lambda_48AA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_48AA)

    def lambda_48B7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_48B7)

    ChrTalk(
        0x103,
        (
            "#00205FM-Me, you say?\x02\x03",
            "#00204F............\x01",
            "A-Alright.\x02\x03",
            "#00201FIt is a little embarrassing, but\x01",
            "I will try to do what I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x7)
    SetScenarioFlags(0x19A, 2)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4A54")

    label("loc_4957")

    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000F...Noｱl.\x01",
            "Can you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4984():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4984)

    def lambda_4991():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4991)

    def lambda_499E():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_499E)

    def lambda_49AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_49AB)

    def lambda_49B8():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_49B8)

    ChrTalk(
        0x109,
        (
            "#10114FM-Me!?\x01",
            "Hmm...\x02\x03",
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
    Jump("loc_4A54")

    label("loc_4A54")

    Jump("loc_40E3")

    label("loc_4A59")


    ChrTalk(
        0x104,
        (
            "#00302FHa ha, you'll get the hang\x01",
            "of it once you're on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FTo be honest, I think the tension is different from\x01",
            "when we're in an actual combat or an investigation.\x02\x03",
            "#10302FAnd in addition to that, we don't\x01",
            "have the right outfits which'll make\x01",
            "it difficult to actually score a win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, how about we pitch you guys\x01",
            "as "Private Detectives" then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...If only we had a real policewoman... What a shame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Looks like we found ourselves\x01",
            "in a strange spot, huh...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4D19")

    ChrTalk(
        0x109,
        (
            "#10102FFor now anyway, let's focus on\x01",
            "making this event a success!\x02\x03",
            "#10109FDo your best, Miss Elie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FUh uh, I will be rooting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYes, I'll do this somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA6")

    label("loc_4D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4DDB")

    ChrTalk(
        0x102,
        (
            "#00102FAnyway, let's think of how\x01",
            "to make the event a success!\x02\x03",
            "#00109FYou can do it, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FUh uh, I'll cheer for you too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FYes, I will do this somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA6")

    label("loc_4DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4EA6")

    ChrTalk(
        0x103,
        (
            "#00204FAnyway, let's think of how\x01",
            "to make the event a success!\x02\x03",
            "#00202FPlease do your best, Miss Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, I'll be rooting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FYes, I'll do this somehow!\x02",
    )

    CloseMessageWindow()

    label("loc_4EA6")


    ChrTalk(
        0x1B,
        (
            "──Come, we don't have much time. \x01",
            "Let's make arrangements at the backstage!\x02",
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

    # Function_24_2B75 end

    def Function_25_4F23(): pass

    label("Function_25_4F23")

    OP_95(0xFE, 3050, 0, -3910, 3000, 0x0)
    OP_95(0xFE, 1400, 0, -4710, 3000, 0x0)
    OP_95(0xFE, -1250, 0, -5460, 3000, 0x0)
    OP_95(0xFE, -940, 130, -7420, 3000, 0x0)
    OP_95(0xFE, 3690, 3560, -7710, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_4F23 end

    def Function_26_4F8D(): pass

    label("Function_26_4F8D")

    SetChrPos(0xFE, -3350, 0, 1340, 0)
    OP_95(0xFE, 1650, 0, 1870, 2000, 0x0)
    OP_95(0xFE, 3130, 0, 520, 2000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_4F8D end

    def Function_27_4FCE(): pass

    label("Function_27_4FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5008")

    ChrTalk(
        0x1B,
        (
            "Ahh, you're not\x01",
            "serious, are you!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_501E")

    label("loc_5008")


    ChrTalk(
        0x1B,
        "I'm telling you!\x02",
    )

    CloseMessageWindow()

    label("loc_501E")


    ChrTalk(
        0x1B,
        (
            "It's a pageant!\x01",
            "Men can't appear!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Pick someone\x01",
            "else!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FU-Understood.\x02\x03",
            "#00008FUmm, the one who will\x01",
            "appear in the pageant is...\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_27_4FCE end

    def Function_28_50B4(): pass

    label("Function_28_50B4")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_516F")
    LoadChrToIndex("chr/ch00155.itc", 0x1E)
    SetChrPos(0x102, 1540, 750, 16000, 180)
    Jump("loc_51B4")

    label("loc_516F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5194")
    LoadChrToIndex("chr/ch00255.itc", 0x1E)
    SetChrPos(0x103, 1540, 750, 16000, 180)
    Jump("loc_51B4")

    label("loc_5194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_51B4")
    LoadChrToIndex("chr/ch02955.itc", 0x1E)
    SetChrPos(0x109, 1540, 750, 16000, 180)

    label("loc_51B4")

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
        "Ladies and Gentlemen!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "You've waited forever for this!\x01",
            "It's today's main event──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "I would like to open the\x01",
            ""Miss Crossbell Contest\x01",
            "-Working Women Forever-"!!\x02",
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
            "Each of the participants is\x01",
            "going to appear and deliver\x01",
            "their appeal message.\x02",
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
            "Please write the name\x01",
            "of the most charming\x01",
            "girl on your ballot.\x02",
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
            "──Well then, \x01",
            "let's get started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Appeal time...\x01",
            "Staaaaaart!!!\x02",
        )
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
        "First up is entry number 1!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The trim and sweet "Times"\x01",
            "department store receptionist──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Cynthia!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 29)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xC,
        "Welcome to department store "Times".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If there is anything you are not sure\x01",
            "about, don't hesitate to ask.\x02",
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
            "By the way, she's single!\x01",
            "Who out there is going to make\x01",
            "this lovely lady happy!?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x1B,
        (
            "──On to the next one!\x01",
            "Entry number 2!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A lone rose with charm like a butterfly\x01",
            "dancing the Back Street night──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Iris!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 0, 0, 29)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0xD,
        (
            "Thank you for choosing me!\x01",
            "I'm your Iris☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Have a lot to drink today too, ok?\x01",
            "*──kiss*㈱\x02",
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
            "Bravoooooo!! To think\x01",
            "she'd blow us a kiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The store where you can drink\x01",
            "with Miss Iris is on Back Street!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "However, alcohol is for adults\x01",
            "only! Keep that in mind, folks!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x1B,
        (
            "──Let's keep up the energy!\x01",
            "It's entry number 3!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The longtime waitress at "The Old Dragon",\x01",
            "and angel who flew down from the East──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's lovely Shanshan!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 29)
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x18,
        (
            "Hello! Welcome to our\x01",
            "store, customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Papa's cooking is the best\x01",
            "around. Order a lot, ok?㈱\x02",
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
            "Heeere iiit iiiiiis!\x01",
            "Look at that carefree smile!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Poster girl Shanshan here is\x01",
            "very popular on East Street!\x01",
            "I'm personally a huge fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "However, her father, Zhanghui, \x01",
            "won't forgive you if you try anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Please, do it only if you're prepared \x01",
            "to throw away your very life!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x1B,
        (
            "──Then on to\x01",
            "entry number 4!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The beautiful orbments mechanic\x01",
            "of Orbal Store "Genten"──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Wendy!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1C, 0, 0, 29)
    WaitChrThread(0x1C, 0)

    ChrTalk(
        0x1C,
        (
            "...*ahem*. I can't\x01",
            "say I'm all that\x01",
            "clever, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "If your orbments are broken\x01",
            "or whatever, I'm your girl!\x02",
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
            "How reliable! \x01",
            "That gives this girl\x01",
            "a certain charm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Careful not to break\x01",
            "your orbments just\x01",
            "so you can see her!\x02",
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
            "Wouldn't you know it? We're\x01",
            "already at entry number 5!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The industrious maid who\x01",
            "serves Crossbell Chairman\x01",
            "Henry MacDowell──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Joanna!\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x19, 0, 0, 30)
    WaitChrThread(0x19, 0)
    OP_64(0x19)

    ChrTalk(
        0x19,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...U-Um...\x01",
            "............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x19)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "W-Welcome home, Master.\x01",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "............E-Excuse me, then.\x02",
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "O-Ooohhhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "What a fresh feeling! \x01",
            "This kind of maids are nice too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "I bet some of our audience\x01",
            "are even starting to hate\x01",
            "Chairman MacDowell!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5F58")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5F58")

    Sleep(1000)
    WaitChrThread(0x19, 0)

    ChrTalk(
        0x1B,
        (
            "We're almost there!\x01",
            "It's entry number 6!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A pure-hearted initiate and servant\x01",
            "of the Goddess of the Sky──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Ries!\x02",
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
            "The Septian Teachings lie\x01",
            "within the hearts of mankind.\x02\x03",
            "May the Goddess guide you all...\x02",
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
            "O-Ohhh! What a\x01",
            "divine presence!\x02",
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
            "Last but not least,\x01",
            "it's entry number 7!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_61CE")

    ChrTalk(
        0x1B,
        (
            "A member of the police's Special Support\x01",
            "Section, a young lady with an honorable lineage──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Elie MacDowell!\x02",
    )

    CloseMessageWindow()
    Jump("loc_62D5")

    label("loc_61CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_624D")

    ChrTalk(
        0x1B,
        (
            "The girl with a quiet aura assigned to\x01",
            "the police's Special Support Section──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's little Tio Plato!\x02",
    )

    CloseMessageWindow()
    Jump("loc_62D5")

    label("loc_624D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_62D5")

    ChrTalk(
        0x1B,
        (
            "Transferee to the police's Special Support Section\x01",
            "and CGF member with a sense of justice──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "It's Miss Noｱl Seeker!\x02",
    )

    CloseMessageWindow()

    label("loc_62D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_62ED")
    BeginChrThread(0x102, 0, 0, 30)
    WaitChrThread(0x102, 0)
    Jump("loc_6318")

    label("loc_62ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6305")
    BeginChrThread(0x103, 0, 0, 30)
    WaitChrThread(0x103, 0)
    Jump("loc_6318")

    label("loc_6305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6318")
    BeginChrThread(0x109, 0, 0, 30)
    WaitChrThread(0x109, 0)

    label("loc_6318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_64FF")

    ChrTalk(
        0x102,
        (
            "#00105F(Umm... I think I\x01",
            "have to give an\x01",
            "appeal message.)\x02\x03",
            "#00103F(What should I say?)\x02",
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
            "Declaration of Arrest\x01",       # 0
            "Appeal With Gun Skills\x01",      # 1
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
        (0, "loc_643C"),
        (1, "loc_6496"),
        (SWITCH_DEFAULT, "loc_64FA"),
    )


    label("loc_643C")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x102,
        (
            "#00107F──Hands up!\x02\x03",
            "Grounded on autonomous state law,\x01",
            "you're under arrest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FA")

    label("loc_6496")


    ChrTalk(
        0x102,
        (
            "#00104F──*phew*... Bullseye.\x02\x03",
            "#00101FIf you're thinking of escaping, you're dead wrong!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FA")

    label("loc_64FA")

    Jump("loc_6954")

    label("loc_64FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6748")

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
            "Declaration of Arrest\x01",        # 0
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
        (0, "loc_663F"),
        (1, "loc_66BD"),
        (SWITCH_DEFAULT, "loc_6743"),
    )


    label("loc_663F")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x103,
        (
            "#00203F──Data collection, complete.\x01",
            "The criminal is...you.\x02\x03",
            "#00201FIt's too late to run.\x01",
            "Surrender peacefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6743")

    label("loc_66BD")


    ChrTalk(
        0x103,
        (
            "#00203F──"Aeon System", activate...\x01",
            "Orbal field, rapid deployment.\x02\x03",
            "#00201FI will show you the power\x01",
            "of this orbal staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6743")

    label("loc_6743")

    Jump("loc_6954")

    label("loc_6748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6954")

    ChrTalk(
        0x109,
        (
            "#10105F(Umm... I think I\x01",
            "have to give an\x01",
            "appeal message.)\x02\x03",
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
            "Declaration of Arrest\x01",        # 0
            "Appeal with CGF Command\x01",      # 1
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
        (0, "loc_687A"),
        (1, "loc_68EC"),
        (SWITCH_DEFAULT, "loc_6954"),
    )


    label("loc_687A")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x109,
        (
            "#10101F──You're completely surrounded...\x01",
            "There's no escape!\x02\x03",
            "#10107FPlease, surrender immediately!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6954")

    label("loc_68EC")


    ChrTalk(
        0x109,
        (
            "#10101F──Intercept the enemy armored unit\x01",
            "and rescue the supply unit!\x02\x03",
            "#10107FOpen combat!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6954")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_69BC")
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)

    ChrTalk(
        0x1B,
        (
            "Oooh...\x01",
            "Bravoooooooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "You all got to see a\x01",
            "policewoman in action!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A0D")

    label("loc_69BC")

    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)

    ChrTalk(
        0x1B,
        (
            "Oooh...\x01",
            "Bravoooooooooo!\x02",
        )
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

    label("loc_6A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6A83")

    ChrTalk(
        0x102,
        (
            "#00106F(H-Hmm... Maybe I should've\x01",
            "said something like what a\x01",
            "policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5B")

    label("loc_6A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6AF0")

    ChrTalk(
        0x103,
        (
            "#00206F(...Maybe I should have said something more\x01",
            "like what a policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5B")

    label("loc_6AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6B5B")

    ChrTalk(
        0x109,
        (
            "#10106F(I messed up... Maybe if I\x01",
            "said something more like what\x01",
            "a policewoman would have...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6B86")
    Fade(250)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x102, 0, 0, 37)
    WaitChrThread(0x102, 0)
    Jump("loc_6BD7")

    label("loc_6B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6BB1")
    Fade(250)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    BeginChrThread(0x103, 0, 0, 37)
    WaitChrThread(0x103, 0)
    Jump("loc_6BD7")

    label("loc_6BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6BD7")
    Fade(250)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    BeginChrThread(0x109, 0, 0, 37)
    WaitChrThread(0x109, 0)

    label("loc_6BD7")


    ChrTalk(
        0x1B,
        (
            "With this, all their\x01",
            "appeal times are finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Let's have a big round of applause\x01",
            "for all our participants!\x02",
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
            "After that, the audience voted\x01",
            "to determine the winner.\x07\x00\x02",
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
            "Before the voting, sister Ries\x01",
            "withdrew, saying she is not a\x01",
            "Crossbell citizen.\x07\x00\x02",
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
            "The audience proceeded to select a \x01",
            "winner from the other participants.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000F(I received a ballot too..\x01",
            "Putting down the name of my\x01",
            "colleague would be...you know.)\x02\x03",
            "#00003F(....Then, who should I put down?)\x02",
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
        (0, "loc_6EA3"),
        (1, "loc_6EE3"),
        (2, "loc_6F20"),
        (3, "loc_6F5C"),
        (4, "loc_6F95"),
        (SWITCH_DEFAULT, "loc_6FD4"),
    )


    label("loc_6EA3")


    AnonymousTalk(
        0x101,
        "#00002F(Alright... I'll vote for Miss Cynthia.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x9)
    Jump("loc_6FD4")

    label("loc_6EE3")


    AnonymousTalk(
        0x101,
        "#00002F(Alright... I'll vote for Miss Iris.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xA)
    Jump("loc_6FD4")

    label("loc_6F20")


    AnonymousTalk(
        0x101,
        "#00002F(Alright... I'll vote for Shanshan.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xB)
    Jump("loc_6FD4")

    label("loc_6F5C")


    AnonymousTalk(
        0x101,
        "#00002F(Alright... I'll vote for Wendy.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xC)
    Jump("loc_6FD4")

    label("loc_6F95")


    AnonymousTalk(
        0x101,
        "#00002F(Alright... I'll vote for Miss Joanna.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xD)
    Jump("loc_6FD4")

    label("loc_6FD4")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──And then...\x07\x00\x02",
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
            "With the announcement of the results\x01",
            "of the pageant we just held,\x01",
            "the program will come to a close.\x02",
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
        "In the very first Miss Crossbell Contest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The one who will bask in the\x01",
            "light of glorious victory iiis...\x02",
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

    def lambda_723F():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_723F)

    def lambda_7259():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7259)

    def lambda_7273():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7273)
    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    WaitChrThread(0x101, 0)

    def lambda_7298():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7298)

    def lambda_72B2():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_72B2)
    WaitChrThread(0x101, 0)

    def lambda_72D0():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72D0)

    def lambda_72EA():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_72EA)
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
        (0, "loc_7370"),
        (1, "loc_748E"),
        (2, "loc_759D"),
        (3, "loc_76B2"),
        (4, "loc_77D1"),
        (SWITCH_DEFAULT, "loc_78EF"),
    )


    label("loc_7370")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xC, 1, 0, 38)

    def lambda_7384():

        label("loc_7384")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_7384")

    QueueWorkItem2(0x1B, 1, lambda_7384)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 1!\x01",
            "It's Miss Cynthia!!\x02",
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
            "I award you this plaque to commemorate\x01",
            "your victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uh uh, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xC, 0xB4, 0x1F4)
    Jump("loc_78EF")

    label("loc_748E")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xD, 1, 0, 38)

    def lambda_74A2():

        label("loc_74A2")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_74A2")

    QueueWorkItem2(0x1B, 1, lambda_74A2)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 2! \x01",
            "It's Miss Iris!\x02",
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
            "I award you this plaque to commemorate\x01",
            "your victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uhuhu, thanks㈱\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xD, 0xB4, 0x1F4)
    Jump("loc_78EF")

    label("loc_759D")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x18, 1, 0, 38)

    def lambda_75B1():

        label("loc_75B1")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_75B1")

    QueueWorkItem2(0x1B, 1, lambda_75B1)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 3!\x01",
            "It's lovely Shanshan!\x02",
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
            "I award you this plaque to commemorate\x01",
            "your victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Ehehe, thaaanks.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x18, 0xB4, 0x1F4)
    Jump("loc_78EF")

    label("loc_76B2")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x1C, 1, 0, 38)

    def lambda_76C6():

        label("loc_76C6")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_76C6")

    QueueWorkItem2(0x1B, 1, lambda_76C6)

    ChrTalk(
        0x1C,
        (
            "#4S──Entry number 4!\x01",
            "It's Miss Wendy!\x02",
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
            "I award you this plaque to commemorate\x01",
            "your victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Ahaha, are you sure? Thanks.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x1C, 0xB4, 0x1F4)
    Jump("loc_78EF")

    label("loc_77D1")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x19, 1, 0, 38)

    def lambda_77E5():

        label("loc_77E5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_77E5")

    QueueWorkItem2(0x1B, 1, lambda_77E5)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 5!\x01",
            "It's Miss Joanna!\x02",
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
            "I award you this plaque to commemorate\x01",
            "your victory. Here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "U-Umm, thank you...very much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x19, 0xB4, 0x1F4)
    Jump("loc_78EF")

    label("loc_78EF")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7D50")
    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    ChrTalk(
        0x1B,
        (
            "Also, we have a judges special\x01",
            "award for a special entry!\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7978"),
        (1, "loc_7998"),
        (2, "loc_79B8"),
        (3, "loc_79D8"),
        (4, "loc_79F8"),
        (SWITCH_DEFAULT, "loc_7A18"),
    )


    label("loc_7978")

    OP_96(0xC, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Jump("loc_7A18")

    label("loc_7998")

    OP_96(0xD, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xD, 0x87, 0x1F4)
    Jump("loc_7A18")

    label("loc_79B8")

    OP_96(0x18, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x18, 0x87, 0x1F4)
    Jump("loc_7A18")

    label("loc_79D8")

    OP_96(0x1C, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x1C, 0x87, 0x1F4)
    Jump("loc_7A18")

    label("loc_79F8")

    OP_96(0x19, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x19, 0x87, 0x1F4)
    Jump("loc_7A18")

    label("loc_7A18")

    OP_2C(0x8F, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7A6F")
    BeginChrThread(0x102, 1, 0, 38)

    def lambda_7A31():

        label("loc_7A31")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_7A31")

    QueueWorkItem2(0x1B, 0, lambda_7A31)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 7!\x01",
            "It's Miss Elie!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B0D")

    label("loc_7A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7AC0")
    BeginChrThread(0x103, 1, 0, 38)

    def lambda_7A83():

        label("loc_7A83")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_7A83")

    QueueWorkItem2(0x1B, 0, lambda_7A83)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 7!\x01",
            "It's Miss Tio!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B0D")

    label("loc_7AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7B0D")
    BeginChrThread(0x109, 1, 0, 38)

    def lambda_7AD4():

        label("loc_7AD4")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_7AD4")

    QueueWorkItem2(0x1B, 0, lambda_7AD4)

    ChrTalk(
        0x1B,
        (
            "#4S──Entry number 7!\x01",
            "It's Miss Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B0D")

    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    Sound(818, 0, 80, 0)
    Sound(820, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7B4C")
    BeginChrThread(0x102, 0, 0, 40)
    WaitChrThread(0x102, 0)
    EndChrThread(0x102, 0x1)
    Jump("loc_7B7F")

    label("loc_7B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7B68")
    BeginChrThread(0x103, 0, 0, 40)
    WaitChrThread(0x103, 0)
    EndChrThread(0x103, 0x1)
    Jump("loc_7B7F")

    label("loc_7B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7B7F")
    BeginChrThread(0x109, 0, 0, 40)
    WaitChrThread(0x109, 0)
    EndChrThread(0x109, 0x1)

    label("loc_7B7F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7C52")
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
        "#00109F*giggle*, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Jump("loc_7D45")

    label("loc_7C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7CCC")
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
        "#00205F...T-Thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Jump("loc_7D45")

    label("loc_7CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7D45")
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
        "#10109FHa ha, I'm honored.\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    label("loc_7D45")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    label("loc_7D50")

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
            "That's all for the\x01",
            "Miss Crossbell\x01",
            "pageant!\x02",
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
            "And thusly, the charity event\x01",
            "pageant came to a close.\x07\x00\x02",
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

    # Function_28_50B4 end

    def Function_29_7EA2(): pass

    label("Function_29_7EA2")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sleep(1000)
    Return()

    # Function_29_7EA2 end

    def Function_30_7EE0(): pass

    label("Function_30_7EE0")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_30_7EE0 end

    def Function_31_7EFF(): pass

    label("Function_31_7EFF")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -4460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_31_7EFF end

    def Function_32_7F30(): pass

    label("Function_32_7F30")

    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -3460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_7F30 end

    def Function_33_7F64(): pass

    label("Function_33_7F64")

    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -2460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_7F64 end

    def Function_34_7F98(): pass

    label("Function_34_7F98")

    OP_95(0xFE, -1460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_34_7F98 end

    def Function_35_7FB4(): pass

    label("Function_35_7FB4")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_35_7FB4 end

    def Function_36_7FE5(): pass

    label("Function_36_7FE5")

    OP_95(0xFE, 540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_36_7FE5 end

    def Function_37_8001(): pass

    label("Function_37_8001")

    OP_95(0xFE, 1540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_37_8001 end

    def Function_38_801D(): pass

    label("Function_38_801D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8067")
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_38_801D")

    label("loc_8067")

    Return()

    # Function_38_801D end

    def Function_39_8068(): pass

    label("Function_39_8068")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -1910, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_8068 end

    def Function_40_80A2(): pass

    label("Function_40_80A2")

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

    # Function_40_80A2 end

    def Function_41_8104(): pass

    label("Function_41_8104")

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

    # Function_41_8104 end

    def Function_42_8239(): pass

    label("Function_42_8239")

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
            "Foreigners, especially those from the Empire and\x01",
            "Republic, are treated unequally under the law!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "If we pay them 10 percent of our tax\x01",
            "revenue, I'm sure they'll agree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "No matter how you think about it,\x01",
            "isn't that just so strange!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "If we don't oppose them now, \x01",
            "this situation will go on forever!\x01",
            "Why can't you understand that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Are you really okay with that!?\x02",
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
            "Our real problem is that state independence is too\x01",
            "far out of reach for the amount of power we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Suppose for example we're invaded by a large\x01",
            "country. How will the CGF oppose them without tanks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "That large country you're talking\x01",
            "about is the Empire, isn't it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "That a WMD known as the "Railway Cannons"\x01",
            "has been deployed at Garrelia Fortress in\x01",
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
            "thing that's needed here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "What an unreasonable lot...\x01",
            "I'm telling you to look at reality!\x02",
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
            "If walls are erected due to independence,\x01",
            "that wealth will disappear, won't it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Now, now. Calm down, everyone.\x02",
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
        "Aren't we missing that piece?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "This has nothing to do with the international community!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Crossbell state independence is the only\x01",
            "path whereby we can have "justice"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "In the end, you're nothing more than\x01",
            "a convenient shill for Calvard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I-It's true that I've been called a\x01",
            "member of the Republican Faction, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "I'm confident my love of\x01",
            "Crossbell won't lose to anyone's!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "I'll have you take back those words!\x02",
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
            "#00300FEven on a rainy day like today,\x01",
            "it sure is heated in here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. More citizens than I\x01",
            "thought are participating too...\x02\x03",
            "#00003FBut influential Republic and Imperial faction\x01",
            "congressmen have been arguing more heatedly\x01",
            "lately with the new independence faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. I bet it reflects those involved in\x01",
            "Crossbell's current political climate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FEach of their views seem\x01",
            "believable, at least...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...This isn't a problem that\x01",
            "will be resolved so easily.\x02\x03",
            "Also, these same arguments are\x01",
            "repeated every decade or so.\x02\x03",
            "#00101FBut, a serious conclusion\x01",
            "might be coming soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F...I agree.\x02\x03",
            "#10108F(Either an independence with grim prospects\x01",
            "or a subordination without justice...)\x02",
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

    # Function_42_8239 end

    SaveToFile()

Try(main)
