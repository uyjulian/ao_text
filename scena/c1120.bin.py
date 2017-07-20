from ScenarioHelper import *

def main():
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
        "Grace",               # 1
        "Raines",               # 2
        "Fen",                 # 3
        "Oscar",               # 4
        "Receptionist Cynthia",         # 5
        "Iris",               # 6
        "Kate policing",             # 7
        "Piano player",             # 8
        "Guide",                 # 9
        "A maid",                 # 10
        "Citizen",                   # 11
        "Citizen",                   # 12
        "Citizen",                   # 13
        "boy",                 # 14
        "Citizen",                   # 15
        "Sister · Lease",       # 16
        "Sunsan",               # 17
        "Joanna",             # 18
        "Mols old man",             # 19
        "Roy",                   # 20
        "Wendy",             # 21
        "Citizen",                   # 22
        "Citizen",                   # 23
        "Citizen",                   # 24
        "Citizen",                   # 25
        "Citizen",                   # 26
        "Citizen",                   # 27
        "Citizen",                   # 28
        "Representative Campbell",         # 29
        "Imperialist",             # 30
        "Independence faction",             # 31
        "Independence faction",             # 32
        "Moderator",                   # 33
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
        "Function_6_B78",          # 06, 6
        "Function_7_F53",          # 07, 7
        "Function_8_1034",         # 08, 8
        "Function_9_12B5",         # 09, 9
        "Function_10_141D",        # 0A, 10
        "Function_11_1527",        # 0B, 11
        "Function_12_18B0",        # 0C, 12
        "Function_13_1B27",        # 0D, 13
        "Function_14_1D74",        # 0E, 14
        "Function_15_1E59",        # 0F, 15
        "Function_16_1F8C",        # 10, 16
        "Function_17_20DF",        # 11, 17
        "Function_18_2183",        # 12, 18
        "Function_19_22A9",        # 13, 19
        "Function_20_2379",        # 14, 20
        "Function_21_2438",        # 15, 21
        "Function_22_24C0",        # 16, 22
        "Function_23_25A9",        # 17, 23
        "Function_24_2969",        # 18, 24
        "Function_25_4C2E",        # 19, 25
        "Function_26_4C98",        # 1A, 26
        "Function_27_4CD9",        # 1B, 27
        "Function_28_4DD8",        # 1C, 28
        "Function_29_7C19",        # 1D, 29
        "Function_30_7C57",        # 1E, 30
        "Function_31_7C76",        # 1F, 31
        "Function_32_7CA7",        # 20, 32
        "Function_33_7CDB",        # 21, 33
        "Function_34_7D0F",        # 22, 34
        "Function_35_7D2B",        # 23, 35
        "Function_36_7D5C",        # 24, 36
        "Function_37_7D78",        # 25, 37
        "Function_38_7D94",        # 26, 38
        "Function_39_7DDF",        # 27, 39
        "Function_40_7E19",        # 28, 40
        "Function_41_7E7B",        # 29, 41
        "Function_42_7FB0",        # 2A, 42
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
            "★ How to make special sweets chocolat ★\x01",
            "~ Everyone at home\x01",
            "   How is it? ~\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A sweet chocolate recipe is written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B74")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Suite Chocolat\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B74")

    TalkEnd(0xFF)
    Return()

    # Function_5_A5A end

    def Function_6_B78(): pass

    label("Function_6_B78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC3")
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "#02102FOh, good deal of you too!\x02\x03",
            "Now, to the participants of MISCON\x01",
            "I am interviewing.\x02\x03",
            "#02109FHuh, you also later\x01",
            "You are going out with me properly ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, not bad,\x01",
            "I guess I'm getting time … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Huh, who escaped secretly\x01",
            "Looks good. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    SetScenarioFlags(0x0, 4)
    Jump("loc_D41")

    label("loc_CC3")


    ChrTalk(
        0x8,
        (
            "#02105FAh, is that so?\x02\x03",
            "#02100FIt is after certain such incident,\x01",
            "Those who show their faces to their families\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D41")

    Jump("loc_F4F")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")

    ChrTalk(
        0x8,
        "#02109FYahoo, Lloyd guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Grace ……\x01",
            "Do you interview for charity events?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02100FHehe, that kind of thing ☆\x02\x03",
            "It seems quite lively,\x01",
            "Crossbell citizens also\x01",
            "I can write articles that can make you feel good.\x02\x03",
            "#02103FThe scar of that raid incident\x01",
            "It has not disappeared yet ……\x02\x03",
            "#02102FAs for the mass communication,\x01",
            "I have to stop doing what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHang in there, please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 6)
    Jump("loc_F4F")

    label("loc_EC5")


    ChrTalk(
        0x8,
        (
            "#02102FAnything, for a charity event\x01",
            "It seemed like an interesting program\x01",
            "It's become a rumor … ….\x02\x03",
            "#02109FHuhu, I'll scrape thoroughly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4F")

    TalkEnd(0xFE)
    Return()

    # Function_6_B78 end

    def Function_7_F53(): pass

    label("Function_7_F53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FD3")

    ChrTalk(
        0xFE,
        (
            "Miscon, pretty\x01",
            "There was an impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got a lot of good photos,\x01",
            "I have to go home early and put it together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_FD3")


    ChrTalk(
        0xFE,
        (
            "Called for a charity event\x01",
            "Beautiful piano player ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It looks like you can take a nice photo.\x02",
    )

    CloseMessageWindow()

    label("loc_1030")

    TalkEnd(0xFE)
    Return()

    # Function_7_F53 end

    def Function_8_1034(): pass

    label("Function_8_1034")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F5")

    ChrTalk(
        0xFE,
        (
            "Well, I guess Sunosan\x01",
            "What does it mean to participate in MISCON?\x01",
            "I did not expect that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, thanks to the usual tone\x01",
            "It seems I got a little back,\x01",
            "I feel like I'm doing it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1154")

    label("loc_10F5")


    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "When it comes to participating in MISCON … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Master, I should not be mad.\x02",
    )

    CloseMessageWindow()

    label("loc_1154")

    Jump("loc_12B1")

    label("loc_1159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122C")

    ChrTalk(
        0xFE,
        (
            "From the \"Ryuushu Hotel\"\x01",
            "For a charity event\x01",
            "I'm cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the shop I have a hole that I do not have\x01",
            "I leave it to pack and loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little worried,\x01",
            "He has become a useless man\x01",
            "Perhaps it will be okay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_12B1")

    label("loc_122C")


    ChrTalk(
        0xFE,
        (
            "But … san san's guy is\x01",
            "I do not feel well at all these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Contest participation is also\x01",
            "It seems I cried out … …\x01",
            "You ought to be fine soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B1")

    TalkEnd(0xFE)
    Return()

    # Function_8_1034 end

    def Function_9_12B5(): pass

    label("Function_9_12B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")

    ChrTalk(
        0xFE,
        (
            "Uhufu, in this\x01",
            "When the number of customers in the store increases\x01",
            "Daddy is delighted too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I am worried about Lisha,\x01",
            "You surely will be back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be greeted with a smile at that time,\x01",
            "I am doing well and I have to wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1414")

    label("loc_1396")


    ChrTalk(
        0xFE,
        (
            "I am worried about Lisha,\x01",
            "You surely will be back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be greeted with a smile at that time,\x01",
            "I am doing well and I have to wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    Jump("loc_1419")

    label("loc_1419")

    TalkEnd(0xFE)
    Return()

    # Function_9_12B5 end

    def Function_10_141D(): pass

    label("Function_10_141D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DD")

    ChrTalk(
        0xFE,
        (
            "Haa … … Someone like me,\x01",
            "I got up to such a stage … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHehe … …. Joanna,\x01",
            "It was pretty cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh, it's embarrassing ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_151E")

    label("loc_14DD")


    ChrTalk(
        0xFE,
        (
            "A person like me, on such a stage … …\x01",
            "Uh, it's embarrassing ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151E")

    Jump("loc_1523")

    label("loc_1523")

    TalkEnd(0xFE)
    Return()

    # Function_10_141D end

    def Function_11_1527(): pass

    label("Function_11_1527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1671")

    ChrTalk(
        0xFE,
        (
            "Yo, Lloyd and the Support Division!\x01",
            "It was pretty cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha, when it came out\x01",
            "I was truly astonished,\x01",
            "Personally you are the winner.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_15FE")

    ChrTalk(
        0x102,
        "#00109FHehe, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_1637")

    ChrTalk(
        0x103,
        "#00202FHuh, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_1637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_1669")

    ChrTalk(
        0x109,
        "#10109FHehe, thank you!\x02",
    )

    CloseMessageWindow()

    label("loc_1669")

    SetScenarioFlags(0x0, 6)
    Jump("loc_16CB")

    label("loc_1671")


    ChrTalk(
        0xFE,
        (
            "Well, you also continue\x01",
            "Please enjoy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The food is still too much\x01",
            "Because there are plenty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_18AC")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1825")

    ChrTalk(
        0xFE,
        "Oh, is not Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOscar … …?\x01",
            "Did you come to help the event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, leave the store to Bennett\x01",
            "I came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The baguette of our place also on the table\x01",
            "They are lined up and the food that fits the bread is also\x01",
            "I can make some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FWell, it is fluffy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you also firmly\x01",
            "Please enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 7)
    Jump("loc_18AC")

    label("loc_1825")


    ChrTalk(
        0xFE,
        (
            "The baguette of our place also on the table\x01",
            "They are lined up and the food that fits the bread is also\x01",
            "I'm making some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You also firmly\x01",
            "Please enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    TalkEnd(0xFE)
    Return()

    # Function_11_1527 end

    def Function_12_18B0(): pass

    label("Function_12_18B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18C4")
    Jump("loc_1B23")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(
        0xFE,
        (
            "Lloyd guys and MissCon participants\x01",
            "They seem to be gathering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, please do your best.\x01",
            "I will be cheering here as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B23")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA8")

    ChrTalk(
        0xFE,
        "Oh, it is not Lloyd guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, Kate-senpai?\x01",
            "What in a place like this …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, for the time being of the event\x01",
            "I'm helping out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until my turn comes\x01",
            "I still have a little time,\x01",
            "I'm upset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FYour turn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oops this is\x01",
            "It was still a secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, well looking forward to it.\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 0)
    Jump("loc_1B23")

    label("loc_1AA8")


    ChrTalk(
        0xFE,
        (
            "Until my turn comes\x01",
            "I still have a little time,\x01",
            "I'm upset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, well looking forward to it.\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B23")

    TalkEnd(0xFE)
    Return()

    # Function_12_18B0 end

    def Function_13_1B27(): pass

    label("Function_13_1B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C55")

    ChrTalk(
        0x8,
        (
            "#02100FHmm, well then\x01",
            "Have you been recommended by a colleague at work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, the mistcon stand\x01",
            "I was really nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But what gave us applause\x01",
            "It was frankly delightful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhuu, it was nice to go out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02104FHmmmm … … (smooth)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1C55")


    ChrTalk(
        0xFE,
        (
            "Actually, I, in the immediate neighborhood\x01",
            "I plan to return to my home Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am planning to come back soon ……\x01",
            "I could tell you a nice souvenir to my parents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDB")

    Jump("loc_1D70")

    label("loc_1CE0")


    ChrTalk(
        0xFE,
        (
            "In the program after this,\x01",
            "I have to go up to the stage\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People stand in front\x01",
            "I am accustomed to occupation patterns,\x01",
            "After all I am nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D70")

    TalkEnd(0xFE)
    Return()

    # Function_13_1B27 end

    def Function_14_1D74(): pass

    label("Function_14_1D74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DFE")

    ChrTalk(
        0xFE,
        (
            "Ahh, after all to others\x01",
            "It's great to be foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a lot of fun,\x01",
            "I want to do it again if I have the opportunity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E55")

    label("loc_1DFE")


    ChrTalk(
        0xFE,
        (
            "Puff puff …\x01",
            "Yeah, makeup of makeup is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will aim for the top because I do it.\x02",
    )

    CloseMessageWindow()

    label("loc_1E55")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D74 end

    def Function_15_1E59(): pass

    label("Function_15_1E59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F01")

    ChrTalk(
        0xFE,
        (
            "Thanks to Miscon,\x01",
            "Crossbell City reconstruction donation money also\x01",
            "We gathered together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the citizens, and\x01",
            "To the Special Affairs Support Division\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F88")

    label("loc_1F01")


    ChrTalk(
        0xFE,
        (
            "The food and drink fee of today's party party,\x01",
            "All in Crossbell City\x01",
            "It will be donated as a reconstruction donation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to your heart\x01",
            "Please enjoy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F88")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E59 end

    def Function_16_1F8C(): pass

    label("Function_16_1F8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(
        0xFE,
        (
            "Participants,\x01",
            "It was very nice ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all I also made a maid frame\x01",
            "I wish I ran for candidacy ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_2094")

    ChrTalk(
        0xFE,
        (
            "I have a care of the standing party\x01",
            "I can not go out to Miscon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "excuse me,\x01",
            "Please come looking for other people ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_2094")


    ChrTalk(
        0xFE,
        (
            "If you need food and drink\x01",
            "Please feel free to tell us ~ ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1F8C end

    def Function_17_20DF(): pass

    label("Function_17_20DF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_215D")

    ChrTalk(
        0xF,
        (
            "Miscon is too vulgar\x01",
            "I was afraid … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hehe, I was pretty fun.\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_215D")


    ChrTalk(
        0xF,
        "I wonder what kind of song I will play next … …\x02",
    )

    CloseMessageWindow()

    label("loc_217F")

    TalkEnd(0xF)
    Return()

    # Function_17_20DF end

    def Function_18_2183(): pass

    label("Function_18_2183")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2207")

    ChrTalk(
        0xFE,
        (
            "…… Mum, Togugu ……\x01",
            "You seem to have eaten too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But for Crosver City … …\x01",
            "I am going to eat it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A5")

    label("loc_2207")


    ChrTalk(
        0xFE,
        (
            "Munching …\x01",
            "Delicious things in the crossbell\x01",
            "You seem to be in this venue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The more you eat, the more you eat it\x01",
            "To say that it will be for the city,\x01",
            "I'm going to have some fun to eat here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A5")

    TalkEnd(0xFE)
    Return()

    # Function_18_2183 end

    def Function_19_22A9(): pass

    label("Function_19_22A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        "It was a good eye candy ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all sake 's salad is limited to beauty.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2375")

    label("loc_2303")


    ChrTalk(
        0xFE,
        (
            "Well, somehow inside the venue\x01",
            "There are plenty of beautiful places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will do it later,\x01",
            "Is it related to the eyeball program?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2375")

    TalkEnd(0xFE)
    Return()

    # Function_19_22A9 end

    def Function_20_2379(): pass

    label("Function_20_2379")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23FB")

    ChrTalk(
        0xFE,
        (
            "Huhu, even if you look at me from a woman\x01",
            "It was just beautiful people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To this older sister who also works\x01",
            "It seems that I adore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2434")

    label("loc_23FB")


    ChrTalk(
        0xFE,
        (
            "Hey Hey, around your mouth\x01",
            "Ketchup is not sticky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2434")

    TalkEnd(0xFE)
    Return()

    # Function_20_2379 end

    def Function_21_2438(): pass

    label("Function_21_2438")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2493")

    ChrTalk(
        0xFE,
        "Bokune, warm weather ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People with hurt\x01",
            "I think that it was cool!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BC")

    label("loc_2493")


    ChrTalk(
        0xFE,
        (
            "Mushuu …\x01",
            "Hey, it's delicious ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BC")

    TalkEnd(0xFE)
    Return()

    # Function_21_2438 end

    def Function_22_24C0(): pass

    label("Function_22_24C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_252F")

    ChrTalk(
        0xFE,
        "I enjoyed Miscon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if I were 30 years younger too\x01",
            "I ran for candidacy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A5")

    label("loc_252F")


    ChrTalk(
        0xFE,
        (
            "It was played earlier\x01",
            "The piano music was a good sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The feeling sunk by the raid incident,\x01",
            "I feel like I will be peaceful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A5")

    TalkEnd(0xFE)
    Return()

    # Function_22_24C0 end

    def Function_23_25A9(): pass

    label("Function_23_25A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AF")

    ChrTalk(
        0x17,
        (
            "#04402FEveryone, I invite you\x01",
            "Thank you very much.\x02\x03",
            "I can hardly experience in the church\x01",
            "I think that it was an interesting attempt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHello, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FBecause it's no problem\x01",
            "Also for Ries\x01",
            "I wanted to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#04406FIndeed I am not a citizen\x01",
            "To compete with others,\x01",
            "I felt different … ….\x02\x03",
            "#04409FBut, thank you.\x01",
            "I am also happy to compliment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Well, if I could vote\x01",
            "I feel I got quite a few votes. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FShe is unaware of it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 1)
    Jump("loc_2965")

    label("loc_27AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CE")

    ChrTalk(
        0x17,
        (
            "#04402FLet me decline voting\x01",
            "Whats like that?\x01",
            "I think that it was an interesting attempt.\x02\x03",
            "#04404FMunching …\x01",
            "In this way, the standing party\x01",
            "You can enjoy it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F(Like a mountain on a dish you have\x01",
            "Cooking is served … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F(Hehe, it is truly a lease.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2965")

    label("loc_28CE")


    ChrTalk(
        0x17,
        (
            "#04404FMunching …\x01",
            "I will do it a little more\x01",
            "I am going back to the cathedral.\x02\x03",
            "#04402F…… For a while, I decided to have this party\x01",
            "I am planning to enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    TalkEnd(0xFE)
    Return()

    # Function_23_25A9 end

    def Function_24_2969(): pass

    label("Function_24_2969")

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

    def lambda_2EBD():
        OP_95(0xFE, -8350, 0, 6120, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2EBD)
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
            "#00003FWell … Mr. Lease,\x01",
            "I've been eating all the time.\x02\x03",
            "#00012FBecause it's a sister clothing\x01",
            "Is not it conspicuous more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FYes, right\x02\x03",
            "#00102FBut, really this dish\x01",
            "It is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FEach restaurant in the city cooks\x01",
            "It seems to be offering.\x02\x03",
            "#00309FFor those of you who are \"Ryuushi\"\x01",
            "There was also a spicy hemp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHuh, that is\x01",
            "I have to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Whatching\x01",
            "You are really true, you know.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30A2():

        label("loc_30A2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30A2")

    QueueWorkItem2(0x109, 0, lambda_30A2)

    def lambda_30B4():

        label("loc_30B4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30B4")

    QueueWorkItem2(0x102, 0, lambda_30B4)

    def lambda_30C6():

        label("loc_30C6")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30C6")

    QueueWorkItem2(0x104, 0, lambda_30C6)

    def lambda_30D8():

        label("loc_30D8")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30D8")

    QueueWorkItem2(0x101, 0, lambda_30D8)

    def lambda_30EA():

        label("loc_30EA")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30EA")

    QueueWorkItem2(0x105, 0, lambda_30EA)

    def lambda_30FC():

        label("loc_30FC")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30FC")

    QueueWorkItem2(0x103, 0, lambda_30FC)

    ChrTalk(
        0xE,
        (
            "The meal is really delicious,\x01",
            "Event is also a huge success?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FGiggle\x01",
            "I hope I can do so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey Hey……\x01",
            "Even though it's a big charity,\x01",
            "Do not say sinister things.\x02\x03",
            "#00000FAnyway, Senpai,\x01",
            "Frequently MISCON\x01",
            "You became interested in joining?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FPolice also, the headquarters was attacked\x01",
            "I think that I am pretty busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, well ….\x01",
            "When I was invited\x01",
            "I have hesitated too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "From Jorridge manager\x01",
            "In order to participate by all means\x01",
            "I have been told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FOh wow is that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because we are at such times\x01",
            "In a form closer to citizens\x01",
            "I wanted to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hehe, in a sense you\x01",
            "It may be that he wanted to manage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, we are\x01",
            "Such a big monster ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(803, 2, 100, 0)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Ah … it's me.\x01",
            "Sorry for a moment.\x02",
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
            "Yes, here Kate patrol ……\x01",
            "Is cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Yes, yes ……\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Is that right? I understand.\x01",
            "I will head right away.\x02",
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
        "#00005FSenpai, that was\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Well …\x01",
            "I am bad, but I can not remove it\x01",
            "A sudden job entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I am sorry,\x01",
            "For a moment to miscon\x01",
            "I can not go out …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh seriously!\x02\x03",
            "#00301FWell there's no helping it I guess\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 500)

    ChrTalk(
        0xE,
        (
            "sorry,\x01",
            "I have to go soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Apologize to Mr. Roy\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I understand.\x01",
            "Good day, seniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Bye for now\x02",
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
            "#00106FWell, a bit more\x01",
            "I wanted to talk\x01",
            "I regret to say …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah.\x02",
    )

    CloseMessageWindow()
    OP_68(1040, 1700, -1990, 2000)
    MoveCamera(38, 23, 0, 2000)
    WaitChrThread(0x1B, 3)
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        (
            "Hey, everyone.\x01",
            "Are you enjoying it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3799():

        label("loc_3799")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3799")

    QueueWorkItem2(0x109, 0, lambda_3799)

    def lambda_37AB():

        label("loc_37AB")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37AB")

    QueueWorkItem2(0x102, 0, lambda_37AB)

    def lambda_37BD():

        label("loc_37BD")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37BD")

    QueueWorkItem2(0x104, 0, lambda_37BD)

    def lambda_37CF():

        label("loc_37CF")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37CF")

    QueueWorkItem2(0x101, 0, lambda_37CF)

    def lambda_37E1():

        label("loc_37E1")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37E1")

    QueueWorkItem2(0x105, 0, lambda_37E1)

    def lambda_37F3():

        label("loc_37F3")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37F3")

    QueueWorkItem2(0x103, 0, lambda_37F3)

    ChrTalk(
        0x1B,
        (
            "Miscon is about to begin\x01",
            "Calling out to the participants\x01",
            "Can you help me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "……, that?\x01",
            "What is the police officer here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUh well that is\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sudden work in Kate\x01",
            "I explained what was in.\x07\x00\x02",
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
        "What is it ~! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, you are in trouble.\x01",
            "What are you doing ……\x02",
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
        "Oh right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Someone of you, instead\x01",
            "Will you appear in the \"women's police\" frame?\x02",
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
        "#00011FHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FUs!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha that sounds interesting\x02\x03",
            "It's no problem\x01",
            "You can try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FS-senpai what are you saying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "P-Please~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "For this charity event,\x01",
            "Apart from reconstruction assistance, we also purely people\x01",
            "There is meaning to be lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Even for Cross Bell citizens ……\x01",
            "Please do my best!\x02",
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
            "#00106FWell I guess…\x02\x03",
            "#00100FHow about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FNo helping it I guess \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMy main job is a guard,\x01",
            "If that's alright then …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "T-thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well then……\x01",
            "Who will go out to Miscon?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00309FThen, Lloyd.\x01",
            "Pick me and please.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D3E)

    def lambda_3D4B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D4B)

    def lambda_3D58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D58)

    def lambda_3D65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D65)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00011FMe!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FAs a leader of Huff, support department\x01",
            "I think it is a natural obligation.\x02\x03",
            "#10302FWait a minute, do not decay.\x01",
            "There seems to be no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FO-ok fine then\x02\x03",
            "#00003FWell then, then,\x01",
            "Why do you ask Miscon to appear …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4833")
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
            "Who to pick?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Lloyd")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3ED1")
    MenuCmd(3, 0, 0x0)

    label("loc_3ED1")

    MenuCmd(1, 0, "Erie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EFE")
    MenuCmd(3, 0, 0x3)

    label("loc_3EFE")

    MenuCmd(1, 0, "Noel")
    MenuCmd(1, 0, "Waji")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F1D")
    MenuCmd(3, 0, 0x5)

    label("loc_3F1D")

    MenuCmd(2, 0, -1, 80, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F66"),
        (3, "loc_40E8"),
        (5, "loc_42A2"),
        (1, "loc_44FB"),
        (2, "loc_4601"),
        (4, "loc_4709"),
        (SWITCH_DEFAULT, "loc_482E"),
    )


    label("loc_3F66")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001F……I understood.\x01",
            "I will get out if that is the case.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3FAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FAA)

    def lambda_3FB7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FB7)

    def lambda_3FC4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FC4)

    def lambda_3FD1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FD1)

    def lambda_3FDE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FDE)

    ChrTalk(
        0x102,
        "#00105FEr … … Lloyd! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F… … Are you going to be a woman?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FNo wonder, it might suit you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it's a delicate sen.\x02\x03",
            "#10300FBecause you have a shoulder width\x01",
            "I heard that there might be some ingenuity … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10114F(Throb……)\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 0)
    Jump("loc_482E")

    label("loc_40E8")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001F…… Randy.\x01",
            "Will you leave it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4120():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4120)

    def lambda_412D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_412D)

    def lambda_413A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_413A)

    def lambda_4147():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4147)

    def lambda_4154():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4154)

    ChrTalk(
        0x104,
        "#00305F…… Ma, you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FLa, is that Randy …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F…… imagining imagination\x01",
            "I have done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, depending on makeup and costume\x01",
            "Invisible like a man of beauty\x01",
            "It may not exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FIt is unbelievable to flowing … ….\x01",
            "Seniors are big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTohoho …\x01",
            "What is it, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 1)
    Jump("loc_482E")

    label("loc_42A2")

    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F…… Wadi.\x01",
            "Will you leave it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D6():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42D6)

    def lambda_42E3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_42E3)

    def lambda_42F0():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_42F0)

    def lambda_42FD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42FD)

    def lambda_430A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_430A)

    ChrTalk(
        0x105,
        (
            "#10302FGiggle\x01",
            "I do not care but I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWait a minute, huh?\x01",
            "Why do not you refute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FWell, something\x01",
            "It looks interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FLloyd is also Mr. Lloyd!\x02\x03",
            "Well, surely from us\x01",
            "Waji is more cheerful\x01",
            "What are you going to say ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FNo, no, I do not think so ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, in a sense\x01",
            "Maybe I can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… Randy,\x01",
            "Being silent and silent,\x01",
            "Which do you prefer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F…… It was Sumer Sen.\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 2)
    Jump("loc_482E")

    label("loc_44FB")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00000F…… Eli.\x01",
            "Will you leave it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4531():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4531)

    def lambda_453E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_453E)

    def lambda_454B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_454B)

    def lambda_4558():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4558)

    def lambda_4565():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4565)

    ChrTalk(
        0x102,
        (
            "#00112FWow, I! Is it?\x02\x03",
            "#00113FWell …\x01",
            "Well, well, I understand.\x02\x03",
            "#00100FIt's a bit embarrassing though ….\x01",
            "I will try as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x6)
    SetScenarioFlags(0x19A, 1)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_4601")

    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#00000F…… Tio.\x01",
            "Will you leave it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4637():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4637)

    def lambda_4644():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4644)

    def lambda_4651():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4651)

    def lambda_465E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_465E)

    def lambda_466B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_466B)

    ChrTalk(
        0x103,
        (
            "#00205FWow, are you me?\x02\x03",
            "#00204F………………\x01",
            "However, it is good.\x02\x03",
            "#00201FIt is a bit embarrassing\x01",
            "I will try as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x7)
    SetScenarioFlags(0x19A, 2)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_4709")

    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000F… … Noel.\x01",
            "Will you leave it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_473F():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_473F)

    def lambda_474C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_474C)

    def lambda_4759():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4759)

    def lambda_4766():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4766)

    def lambda_4773():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4773)

    ChrTalk(
        0x109,
        (
            "#10114FOh, are you me! Is it?\x01",
            "Well …\x02\x03",
            "#10103F…… Ryo, OK.\x02\x03",
            "#10102FToo much like this\x01",
            "I am not used to it … ….\x01",
            "I will try my best!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x8)
    SetScenarioFlags(0x19A, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_482E")

    Jump("loc_3E6E")

    label("loc_4833")


    ChrTalk(
        0x104,
        (
            "#00302FHahaha, if you stand on the unexpected stage\x01",
            "Does it manage somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, what is the tension of battle and investigation\x01",
            "I think that quality is different.\x02\x03",
            "#10302FBesides, it is not a uniform appearance\x01",
            "It seems unfavorable to aim for the victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, as a \"plain clothes cop\"\x01",
            "The appearance for the moment is in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "A real policewoman would have been nice though\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(This is getting weird)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4A3E")

    ChrTalk(
        0x109,
        (
            "#10102FAnyway, I have an event\x01",
            "Let's consider making it successful!\x02\x03",
            "#10109FPlease do your best, Ellie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FHehe, I support you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYeah, I'll try it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BC7")

    label("loc_4A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4B05")

    ChrTalk(
        0x102,
        (
            "#00102FAnyway, I have an event\x01",
            "Let's consider making it successful.\x02\x03",
            "#00109FGood luck, …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYeah, I'll be cheering you on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FYes, I'll do my best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BC7")

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4BC7")

    ChrTalk(
        0x103,
        (
            "#00204FAnyway, I have an event\x01",
            "Let's consider making it successful.\x02\x03",
            "#00202FGood luck, Noel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, I support you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FYeah, I will show off somehow!\x02",
    )

    CloseMessageWindow()

    label("loc_4BC7")


    ChrTalk(
        0x1B,
        (
            "── Now, I do not have much time.\x01",
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

    # Function_24_2969 end

    def Function_25_4C2E(): pass

    label("Function_25_4C2E")

    OP_95(0xFE, 3050, 0, -3910, 3000, 0x0)
    OP_95(0xFE, 1400, 0, -4710, 3000, 0x0)
    OP_95(0xFE, -1250, 0, -5460, 3000, 0x0)
    OP_95(0xFE, -940, 130, -7420, 3000, 0x0)
    OP_95(0xFE, 3690, 3560, -7710, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_4C2E end

    def Function_26_4C98(): pass

    label("Function_26_4C98")

    SetChrPos(0xFE, -3350, 0, 1340, 0)
    OP_95(0xFE, 1650, 0, 1870, 2000, 0x0)
    OP_95(0xFE, 3130, 0, 520, 2000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_4C98 end

    def Function_27_4CD9(): pass

    label("Function_27_4CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D16")

    ChrTalk(
        0x1B,
        (
            "What, seriously\x01",
            "I'm consulting!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D2A")

    label("loc_4D16")


    ChrTalk(
        0x1B,
        "Let's see!\x02",
    )

    CloseMessageWindow()

    label("loc_4D2A")


    ChrTalk(
        0x1B,
        (
            "This is Miscon!\x01",
            "A man can not participate! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Above, quickly from another person\x01",
            "Please choose! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FI understand.\x02\x03",
            "#00008FLet me see,\x01",
            "Why do you ask Miscon to appear …?\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_27_4CD9 end

    def Function_28_4DD8(): pass

    label("Function_28_4DD8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4E93")
    LoadChrToIndex("chr/ch00155.itc", 0x1E)
    SetChrPos(0x102, 1540, 750, 16000, 180)
    Jump("loc_4ED8")

    label("loc_4E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4EB8")
    LoadChrToIndex("chr/ch00255.itc", 0x1E)
    SetChrPos(0x103, 1540, 750, 16000, 180)
    Jump("loc_4ED8")

    label("loc_4EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4ED8")
    LoadChrToIndex("chr/ch02955.itc", 0x1E)
    SetChrPos(0x109, 1540, 750, 16000, 180)

    label("loc_4ED8")

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
        "Ladies and Gentlemen! <That's literally what he said in Katakana>\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Everyone, I kept you waiting for a long time.\x01",
            "Today's main program ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "\"Miss Crossbell Contest\x01",
            "~ Working woman, forever ~ \"\x01",
            "I would like to hold it! It is!\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x1B,
        (
            "So, the flow of the contest\x01",
            "I will explain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "From now on, for all the participants\x01",
            "Have them come out one by one before,\x01",
            "I will have an appeal message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The appeal message,\x01",
            "Greetings used during work and\x01",
            "I will use business complaints etc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Everyone in the audience,\x01",
            "The name of a woman who thinks to be the most attractive\x01",
            "Please fill out the ballot at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "To the women who had the most votes,\x01",
            "The title of \"Miss Cross Bell\"\x01",
            "I would like to give it to you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "─ ─ So,\x01",
            "Let's start quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Appeal time …\x01",
            "Stah ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─!\x02",
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
        "First is Entry #1\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Signboard girl of department store \"Times\"\x01",
            "A neat and pretty department store girl ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Cynthia!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 29)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xC,
        "Welcome to Department Store Times!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If there is something you do not understand\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xC, 0, 0, 31)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "Excellent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "To her neat atmosphere\x01",
            "Some people knocked out\x01",
            "You do not have much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "By the way, she seems to be free now!\x01",
            "Get Cynthia Mr.\x01",
            "Where are the happy people! Is it?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x1B,
        (
            "── Now, let's get on and on!\x01",
            "Next entry number 2!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Make the butterfly in the back street to the butterfly of the night\x01",
            "Roses of one-ring that give a fascinating charm ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Iris!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 0, 0, 29)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0xD,
        (
            "Thank you for your nomination!\x01",
            "Your iris yo ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Today as well please drink it!\x01",
            "─ ─ tattoos\x02",
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
            "Bravo!\x01",
            "No way to kiss thrown!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "The shop where you can drink with iris\x01",
            "It is said to be in the back street!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, drinking has become an adult!\x01",
            "Please be careful of the place there!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x1B,
        (
            "With this momentum,\x01",
            "Entry number 3!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A long-established store on the east street \"Ryuuji\" restaurant clerk,\x01",
            "An angel descending from the east ──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Shan Shan!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 29)
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x18,
        (
            "welcome!\x01",
            "Welcome, customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Dad's dishes are the best in the world.\x01",
            "I'm ordering a little more ~ spray\x02",
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
            "It's Kitty!\x01",
            "Behold, this committed smile!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Signboard girl, Sunsan chan\x01",
            "Famous popular people on east side!\x01",
            "That's why I am a big fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, Mr. Chan Hui of my father\x01",
            "I will not forgive insects that go to San Sang!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Only those who are ready to give up their lives\x01",
            "Please challenge!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0)

    ChrTalk(
        0x1B,
        (
            "── Come on, return\x01",
            "Entry number 4!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "From the oval store \"Genten\"\x01",
            "Beautiful female orbiting craftsman\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Wendy!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1C, 0, 0, 29)
    WaitChrThread(0x1C, 0)

    ChrTalk(
        0x1C,
        (
            "…… Well, Kohon.\x01",
            "What I feel like cheating\x01",
            "I can not tell you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "If the guide is broken,\x01",
            "Please depend on it anytime!\x02",
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
            "Please!\x01",
            "This is her taste,\x01",
            "And it can be called charm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "To meet her,\x01",
            "I intentionally destroy the guide\x01",
            "So as not to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "With her spanner\x01",
            "I will be punished with cotton!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0)

    ChrTalk(
        0x1B,
        (
            "Okay, just fine.\x01",
            "Entry number 5!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Crossbell Autonomous State Legislative Assembly,\x01",
            "To Mr. Henry MacDael\x01",
            "A serious maid serving ──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Joanna!\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x19, 0, 0, 30)
    WaitChrThread(0x19, 0)
    OP_64(0x19)

    ChrTalk(
        0x19,
        "…..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "………………AA no…………\x01",
            "…..\x02",
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
            "Welcome back, husband.\x01",
            "…..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Excuse me then!\x02",
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
            "It made me feel fresh somehow!\x01",
            "Such a maid is also nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Some of you at the venue,\x01",
            "Mr. MacDaely is hateful\x01",
            "I wonder if it has come to think!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5D22")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5D22")

    Sleep(1000)
    WaitChrThread(0x19, 0)

    ChrTalk(
        0x1B,
        (
            "Now, it's time to finish!\x01",
            "Entry number 6!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "I served the goddess of the sky\x01",
            "A clean new sister ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Reis!\x02",
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
            "The teachings of Seven Yao\x01",
            "It is in the minds of people.\x02\x03",
            "I give you all Aidos' blessing\x02",
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
            "ohhhhhhhh……!\x01",
            "What a godly appearance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Up until last time a party party\x01",
            "With the figure he was walking around\x01",
            "The gap is also good! It is!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0)

    ChrTalk(
        0x1B,
        (
            "Well then, it is the last person!\x01",
            "Entry number 7!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5F7D")

    ChrTalk(
        0x1B,
        (
            "It belongs to the police and affairs support section,\x01",
            "Venerable and beautiful lady ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Erie · Mcdael!\x02",
    )

    CloseMessageWindow()
    Jump("loc_604C")

    label("loc_5F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5FEA")

    ChrTalk(
        0x1B,
        (
            "It belongs to the police and affairs support section,\x01",
            "A girl wearing a quiet aura ──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "<Name!>\x02",
    )

    CloseMessageWindow()
    Jump("loc_604C")

    label("loc_5FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_604C")

    ChrTalk(
        0x1B,
        (
            "While on loan to the police and special affairs support section,\x01",
            "Foldable female security guard ─ ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Noel · Seeker!\x02",
    )

    CloseMessageWindow()

    label("loc_604C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6064")
    BeginChrThread(0x102, 0, 0, 30)
    WaitChrThread(0x102, 0)
    Jump("loc_608F")

    label("loc_6064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_607C")
    BeginChrThread(0x103, 0, 0, 30)
    WaitChrThread(0x103, 0)
    Jump("loc_608F")

    label("loc_607C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_608F")
    BeginChrThread(0x109, 0, 0, 30)
    WaitChrThread(0x109, 0)

    label("loc_608F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_627A")

    ChrTalk(
        0x102,
        (
            "#00105F(Uh……\x01",
            "Certainly appeal messages\x01",
            "I have to tell you. )\x02\x03",
            "#00103F(What shall I say?\x02",
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
            "Appeal in the declaration of arrest\x01",      # 0
            "Appeal with the prowess of guns\x01",        # 1
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
        (0, "loc_61C4"),
        (1, "loc_621E"),
        (SWITCH_DEFAULT, "loc_6275"),
    )


    label("loc_61C4")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x102,
        (
            "#00107F- Raise your hand!\x02\x03",
            "Based on autonomous state law,\x01",
            "We arrest you for various charges!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6275")

    label("loc_621E")


    ChrTalk(
        0x102,
        (
            "#00104F── Fuh … … hundreds of yen.\x02\x03",
            "#00101FIf you think you can escape, it is a big mistake!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6275")

    label("loc_6275")

    Jump("loc_66FD")

    label("loc_627A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_64D6")

    ChrTalk(
        0x103,
        (
            "#00200F(Now……\x01",
            "Certainly appeal messages\x01",
            "Do you need to say that? )\x02\x03",
            "#00203F(What should I say?\x02",
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
            "Appeal in the declaration of arrest\x01",            # 0
            "Appeal with Aion System\x01",      # 1
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
        (0, "loc_63C6"),
        (1, "loc_644C"),
        (SWITCH_DEFAULT, "loc_64D1"),
    )


    label("loc_63C6")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x103,
        (
            "#00203F── Data collection, complete.\x01",
            "The culprit … you are you.\x02\x03",
            "#00201FI can not escape any longer.\x01",
            "Please accompany me quietly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D1")

    label("loc_644C")


    ChrTalk(
        0x103,
        (
            "#00203F─ ─ \"Aion system\" operation ……\x01",
            "Fast deployment of power field.\x02\x03",
            "#00201FThis magical figure performance ……\x01",
            "Let's take a look at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D1")

    label("loc_64D1")

    Jump("loc_66FD")

    label("loc_64D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_66FD")

    ChrTalk(
        0x109,
        (
            "#10105FEr …\x01",
            "Certainly appeal messages\x01",
            "You ought to have to tell. )\x02\x03",
            "#10103FWhat shall I say?\x02",
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
            "Appeal in the declaration of arrest\x01",        # 0
            "Appeal with the command of the guard\x01",      # 1
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
        (0, "loc_6618"),
        (1, "loc_6685"),
        (SWITCH_DEFAULT, "loc_66FD"),
    )


    label("loc_6618")

    SetScenarioFlags(0x19A, 4)

    ChrTalk(
        0x109,
        (
            "#10101F── It completely besieged … …\x01",
            "There is no escape any longer!\x02\x03",
            "#10107FPlease exit promptly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66FD")

    label("loc_6685")


    ChrTalk(
        0x109,
        (
            "#10101F── Goal, interception of enemy armored units,\x01",
            "Rescuing an isolated refueling force!\x02\x03",
            "#10107FCombat start#7ROpen Combat#! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66FD")

    label("loc_66FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_6775")
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)

    ChrTalk(
        0x1B,
        (
            "Oh……\x01",
            "Bravo ー ー ー ー ー ー ー ー!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "This is a police officer\x01",
            "I showed you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D7")

    label("loc_6775")

    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)

    ChrTalk(
        0x1B,
        (
            "Oh……\x01",
            "Bravo ー ー ー ー ー ー ー ー!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Well, show me the good stuff\x01",
            "\"Whats going on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_683E")

    ChrTalk(
        0x102,
        (
            "#00106F(Well, hmm … ….\x01",
            "A thing that seems to be a police officer\x01",
            "I wonder if I should have said … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68EE")

    label("loc_683E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_689A")

    ChrTalk(
        0x103,
        (
            "#00206F(… … a little more like a police officer\x01",
            "I should have said that. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68EE")

    label("loc_689A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_68EE")

    ChrTalk(
        0x109,
        (
            "#10106F(Oops……\x01",
            "A thing that seems to be a police officer\x01",
            "It might have been said … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6919")
    Fade(250)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x102, 0, 0, 37)
    WaitChrThread(0x102, 0)
    Jump("loc_696A")

    label("loc_6919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6944")
    Fade(250)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    BeginChrThread(0x103, 0, 0, 37)
    WaitChrThread(0x103, 0)
    Jump("loc_696A")

    label("loc_6944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_696A")
    Fade(250)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    BeginChrThread(0x109, 0, 0, 37)
    WaitChrThread(0x109, 0)

    label("loc_696A")


    ChrTalk(
        0x1B,
        (
            "With this, all 7\x01",
            "I will end the appeal time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "To all participants\x01",
            "Once a big applause!\x02",
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
            "Then, by the audience\x01",
            "Miscon votes were held.\x07\x00\x02",
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
            "Prior to voting by Sister Lease,\x01",
            "Because of not being a crossbellian citizen\x01",
            "Because he himself declined to vote ……\x07\x00\x02",
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
            "From among the other participants\x01",
            "The winner was selected to be chosen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000F(Well, I also vote for the ballot\x01",
            "I got it ….\x01",
            "You can not put it in a group. )\x02\x03",
            "#00003F(Let's pick one now…)\x02",
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
            "Vote for Cynthia\x01",        # 0
            "Vote for Iris\x01",        # 1
            "Vote for Sunsan\x01",        # 2
            "Vote for Wendy\x01",      # 3
            "Vote for Joanna\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C1F"),
        (1, "loc_6C5D"),
        (2, "loc_6C9B"),
        (3, "loc_6CDB"),
        (4, "loc_6D17"),
        (SWITCH_DEFAULT, "loc_6D57"),
    )


    label("loc_6C1F")


    AnonymousTalk(
        0x101,
        "#00002F(Alright … let's vote for Mr. Cynthia.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x9)
    Jump("loc_6D57")

    label("loc_6C5D")


    AnonymousTalk(
        0x101,
        "#00002F(Alright … I will vote for Iris.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xA)
    Jump("loc_6D57")

    label("loc_6C9B")


    AnonymousTalk(
        0x101,
        "#00002F(Alright … let's vote for Sunsan.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xB)
    Jump("loc_6D57")

    label("loc_6CDB")


    AnonymousTalk(
        0x101,
        "#00002F(Alright … let's vote for Wendy.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xC)
    Jump("loc_6D57")

    label("loc_6D17")


    AnonymousTalk(
        0x101,
        "#00002F(Okay … I will vote for Mr. Joanna.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xD)
    Jump("loc_6D57")

    label("loc_6D57")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then…\x07\x00\x02",
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
            "Misccon's done earlier\x01",
            "Hold this place with a result announcement\x01",
            "I would like to close down.\x02",
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
        "The First Miss Crossbell Pagent winner\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "The one who shone the most is…\x02",
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

    def lambda_6F89():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F89)

    def lambda_6FA3():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FA3)

    def lambda_6FBD():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6FBD)
    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    WaitChrThread(0x101, 0)

    def lambda_6FE2():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FE2)

    def lambda_6FFC():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FFC)
    WaitChrThread(0x101, 0)

    def lambda_701A():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_701A)

    def lambda_7034():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7034)
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
        (0, "loc_70BA"),
        (1, "loc_71CF"),
        (2, "loc_72DA"),
        (3, "loc_73EB"),
        (4, "loc_7507"),
        (SWITCH_DEFAULT, "loc_7626"),
    )


    label("loc_70BA")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xC, 1, 0, 38)

    def lambda_70CE():

        label("loc_70CE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_70CE")

    QueueWorkItem2(0x1B, 1, lambda_70CE)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 1!\x01",
            "Mr. Cynthia!\x02",
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
            "The winner will be awarded a memorial shield.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hehe, thank you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xC, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_71CF")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xD, 1, 0, 38)

    def lambda_71E3():

        label("loc_71E3")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_71E3")

    QueueWorkItem2(0x1B, 1, lambda_71E3)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 2!\x01",
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
            "The winner will be awarded a memorial shield.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uhufu, thanks thanks\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xD, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_72DA")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x18, 1, 0, 38)

    def lambda_72EE():

        label("loc_72EE")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_72EE")

    QueueWorkItem2(0x1B, 1, lambda_72EE)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 3!\x01",
            "It's Sunsan!\x02",
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
            "The winner will be awarded a memorial shield.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Thank you, eh ~.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x18, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_73EB")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x1C, 1, 0, 38)

    def lambda_73FF():

        label("loc_73FF")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_73FF")

    QueueWorkItem2(0x1B, 1, lambda_73FF)

    ChrTalk(
        0x1C,
        (
            "#4S─ ─ entry number 4!\x01",
            "Mr. Wendy!\x02",
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
            "The winner will be awarded a memorial shield.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Haha, is it okay? Thank you ~.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x1C, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_7507")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x19, 1, 0, 38)

    def lambda_751B():

        label("loc_751B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_751B")

    QueueWorkItem2(0x1B, 1, lambda_751B)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 5!\x01",
            "Mr. Joanna is here!\x02",
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
            "The winner will be awarded a memorial shield.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "U-uhh, thank you… very much\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x19, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_7626")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7AA3")
    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    ChrTalk(
        0x1B,
        (
            "And this time as a special frame\x01",
            "Judge Special Award has been prepared!\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76AF"),
        (1, "loc_76CF"),
        (2, "loc_76EF"),
        (3, "loc_770F"),
        (4, "loc_772F"),
        (SWITCH_DEFAULT, "loc_774F"),
    )


    label("loc_76AF")

    OP_96(0xC, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_76CF")

    OP_96(0xD, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xD, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_76EF")

    OP_96(0x18, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x18, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_770F")

    OP_96(0x1C, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x1C, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_772F")

    OP_96(0x19, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x19, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_774F")

    OP_2C(0x8F, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_77B0")
    BeginChrThread(0x102, 1, 0, 38)

    def lambda_7768():

        label("loc_7768")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_7768")

    QueueWorkItem2(0x1B, 0, lambda_7768)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 7!\x01",
            "Erie is here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7863")

    label("loc_77B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_780C")
    BeginChrThread(0x103, 1, 0, 38)

    def lambda_77C4():

        label("loc_77C4")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_77C4")

    QueueWorkItem2(0x1B, 0, lambda_77C4)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 7!\x01",
            "This is Tio!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7863")

    label("loc_780C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7863")
    BeginChrThread(0x109, 1, 0, 38)

    def lambda_7820():

        label("loc_7820")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_7820")

    QueueWorkItem2(0x1B, 0, lambda_7820)

    ChrTalk(
        0x1B,
        (
            "#4S─ ─ entry number 7!\x01",
            "Noel is here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7863")

    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    Sound(818, 0, 80, 0)
    Sound(820, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_78A2")
    BeginChrThread(0x102, 0, 0, 40)
    WaitChrThread(0x102, 0)
    EndChrThread(0x102, 0x1)
    Jump("loc_78D5")

    label("loc_78A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_78BE")
    BeginChrThread(0x103, 0, 0, 40)
    WaitChrThread(0x103, 0)
    EndChrThread(0x103, 0x1)
    Jump("loc_78D5")

    label("loc_78BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_78D5")
    BeginChrThread(0x109, 0, 0, 40)
    WaitChrThread(0x109, 0)
    EndChrThread(0x109, 0x1)

    label("loc_78D5")

    StopEffect(0x1, 0x0)

    ChrTalk(
        0x1B,
        (
            "Even for the special prize,\x01",
            "A memorial shield will be awarded.\x01",
            "……here you go!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_799F")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '选秀活动特别奖纪念盾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('选秀活动特别奖纪念盾', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00109FHehe, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Jump("loc_7A98")

    label("loc_799F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7A1E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '选秀活动特别奖纪念盾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('选秀活动特别奖纪念盾', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00205FHow about you?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Jump("loc_7A98")

    label("loc_7A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7A98")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '选秀活动特别奖纪念盾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('选秀活动特别奖纪念盾', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        "#10109FHehe, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    label("loc_7A98")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    label("loc_7AA3")

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
            "Well then, in this\x01",
            "Miss Crossbell Contest\x01",
            "I will finish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "After this, a standing party\x01",
            "Because it will be resumed, everyone will continue\x01",
            "Enjoy the event!\x02",
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
            "Thus, for the charity event\x01",
            "Miscon was closing the curtain.\x07\x00\x02",
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

    # Function_28_4DD8 end

    def Function_29_7C19(): pass

    label("Function_29_7C19")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sleep(1000)
    Return()

    # Function_29_7C19 end

    def Function_30_7C57(): pass

    label("Function_30_7C57")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_30_7C57 end

    def Function_31_7C76(): pass

    label("Function_31_7C76")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -4460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_31_7C76 end

    def Function_32_7CA7(): pass

    label("Function_32_7CA7")

    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -3460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_7CA7 end

    def Function_33_7CDB(): pass

    label("Function_33_7CDB")

    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -2460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_7CDB end

    def Function_34_7D0F(): pass

    label("Function_34_7D0F")

    OP_95(0xFE, -1460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_34_7D0F end

    def Function_35_7D2B(): pass

    label("Function_35_7D2B")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_35_7D2B end

    def Function_36_7D5C(): pass

    label("Function_36_7D5C")

    OP_95(0xFE, 540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_36_7D5C end

    def Function_37_7D78(): pass

    label("Function_37_7D78")

    OP_95(0xFE, 1540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_37_7D78 end

    def Function_38_7D94(): pass

    label("Function_38_7D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DDE")
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_38_7D94")

    label("loc_7DDE")

    Return()

    # Function_38_7D94 end

    def Function_39_7DDF(): pass

    label("Function_39_7DDF")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -1910, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_7DDF end

    def Function_40_7E19(): pass

    label("Function_40_7E19")

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

    # Function_40_7E19 end

    def Function_41_7E7B(): pass

    label("Function_41_7E7B")

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

    # Function_41_7E7B end

    def Function_42_7FB0(): pass

    label("Function_42_7FB0")

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
            "Foreigners, especially Empire and Republicans\x01",
            "Inequitable legal system that gives preferential treatment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Even 10 of citizen's blood tax\x01",
            "Arrangement which must be paid to 2 major countries!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Whatever you think\x01",
            "Do not you think it's strange! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "If we do not stand now\x01",
            "This situation is going forward for the eternity\x01",
            "It is continuing! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Is that really OK? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "…… Hun, that is stupid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "As a matter of reality, without power\x01",
            "It is too rice cake drawn in painting such as national independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "When a major army from another country invades\x01",
            "How can you prevent it with a guard without a tank?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Whatever you think about other countries\x01",
            "It is about Eleven Empire!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "It is a \"train cannon\" to the galleria fort in the west\x01",
            "Weapons of mass destruction aiming at Crossbell City\x01",
            "It is a well-known fact that it is deployed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Whether it is a tank or a military flying boat\x01",
            "If it is rich financial affairs of Crossbell\x01",
            "It is possible to deploy it enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "What is important is our\x01",
            "Is not it a decision! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Those guys understood ……\x01",
            "It says to see the reality!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "First, prosperity of crossbell is\x01",
            "It flows from empire and republic\x01",
            "It is great to bear Mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "If you have made walls like independence\x01",
            "That wealth may also disappear! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Fairly, everyone calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "…… Anyway the problem is,\x01",
            "Such a brutal independent proposal\x01",
            "Whether or not the international community will accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Is not that argument missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "At this time, the international community has nothing to do with it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Crossbell's national independence is the only one\x01",
            "The only way to realize \"justice\"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "After all you are also Calvert\x01",
            "Is it just a convenient spokesperson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Yes, indeed I\x01",
            "Although it is called republic school etc … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "In the heart that loves crossbells\x01",
            "I am confident that I will not lose to anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Let's have that word corrected!\x02",
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
            "#00300FAlthough it was a rainy day,\x01",
            "It is quite exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, participants from citizens as well\x01",
            "It is more than I thought ….\x02\x03",
            "#00003FBut with imperialists and leading Rep. Rep.\x01",
            "Recently, it is increasing momentum\x01",
            "Is it a controversy of independent young lawmakers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, political situation of the current crossbell\x01",
            "You look like you reflected it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FSomehow, neither party\x01",
            "It sounds plausible, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F…… Actually, this problem is\x01",
            "It is not easy to conclude.\x02\x03",
            "That's over decades\x01",
            "Similar discussions have been repeated.\x02\x03",
            "#00101FBut, it surely will soon be\x01",
            "It may be time to draw a conclusion …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F………I agree.\x02\x03",
            "#10108F(Is it hard to go ahead?\x01",
            "Or subordinate without justice … …)\x02",
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

    # Function_42_7FB0 end

    SaveToFile()

Try(main)
