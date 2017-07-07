from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0510.bin",                # FileName
        "t0510",                    # MapName
        "t0510",                    # Location
        0x003D,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0510",                  # 0
        "Mayor of Vixen",           # 1
        "Mrs. Anna",             # 2
        "Miranda",               # 3
        "Burma Lady",           # 4
        "Lulieda",               # 5
        "Ami",                 # 6
        "Alec",                 # 7
        "Miner Gantz",             # 8
        "Miner rosie",           # 9
        "Mining head Hoffman",         # 10
        "Miner Max",           # 11
        "Lieutenant Mireille",           # 12
        "A security guard",               # 13
    ))

    AddCharChip((
        "chr/ch23200.itc",                   # 00
        "chr/ch23202.itc",                   # 01
        "chr/ch20100.itc",                   # 02
        "chr/ch20102.itc",                   # 03
        "chr/ch22700.itc",                   # 04
        "chr/ch23300.itc",                   # 05
        "chr/ch24300.itc",                   # 06
        "chr/ch23700.itc",                   # 07
        "chr/ch23000.itc",                   # 08
        "chr/ch30700.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch26302.itc",                   # 0B
        "chr/ch26202.itc",                   # 0C
        "chr/ch32600.itc",                   # 0D
        "chr/ch31200.itc",                   # 0E
        "chr/ch24302.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(4294966407, 949,     3319,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294960766, 750,     59,      270,  261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(96099,   0,       4219,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(47450,   0,       4294965796, 0,    389,  0x0, 0,   7,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(101800,  0,       500,     225,  389,  0x0, 0,   8,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(47450,   300,     0,       180,  389,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(97459,   150,     4294966127, 0,    453,  0x0, 0,   11,  0,   255, 255, 0,   7,   255,  0)
    DeclNpc(150729,  250,     100,     270,  453,  0x0, 0,   12,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(1200,    750,     4294966296, 270,  389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2200,    750,     4294967026, 270,  389,  0x0, 0,   14,  0,   0,   0,   0,   21,  255,  0)

    ChipFrameInfo(732, 0)                                        # 0

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_3B7",          # 02, 2
        "Function_3_3E2",          # 03, 3
        "Function_4_62F",          # 04, 4
        "Function_5_668",          # 05, 5
        "Function_6_131F",         # 06, 6
        "Function_7_13F9",         # 07, 7
        "Function_8_166C",         # 08, 8
        "Function_9_2409",         # 09, 9
        "Function_10_25E3",        # 0A, 10
        "Function_11_26F1",        # 0B, 11
        "Function_12_27E1",        # 0C, 12
        "Function_13_3469",        # 0D, 13
        "Function_14_3586",        # 0E, 14
        "Function_15_3689",        # 0F, 15
        "Function_16_4767",        # 10, 16
        "Function_17_496B",        # 11, 17
        "Function_18_4C76",        # 12, 18
        "Function_19_5D33",        # 13, 19
        "Function_20_5E49",        # 14, 20
        "Function_21_608B",        # 15, 21
        "Function_22_622A",        # 16, 22
        "Function_23_6275",        # 17, 23
        "Function_24_72C4",        # 18, 24
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_320"),
        (2, "loc_32C"),
        (3, "loc_338"),
        (4, "loc_344"),
        (5, "loc_350"),
        (6, "loc_35C"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_314")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_320")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_32C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_338")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_344")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_350")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_38B")

    Return()

    # Function_0_2DC end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6")
    OP_94(0xFE, 0xBD74, 0xA8C, 0xC92C, 0xFFFFFD44, 0x3E8)
    Sleep(250)
    Jump("Function_1_38C")

    label("loc_3B6")

    Return()

    # Function_1_38C end

    def Function_2_3B7(): pass

    label("Function_2_3B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E1")
    OP_94(0xFE, 0x192EE, 0x7F8, 0x1863C, 0xFFFFFB82, 0x3E8)
    Sleep(250)
    Jump("Function_2_3B7")

    label("loc_3E1")

    Return()

    # Function_2_3B7 end

    def Function_3_3E2(): pass

    label("Function_3_3E2")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xC)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_423")
    Jump("loc_60F")

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_60F")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0xC, 147900, 250, 100, 90)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x40)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 0, 750, -1000, 90)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x13, 0x10)

    label("loc_4A9")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_60F")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D0")
    Jump("loc_60F")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4DE")
    Jump("loc_60F")

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_518")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 101600, 0, 500, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 50000, 0, 1000, 315)
    Jump("loc_60F")

    label("loc_518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_526")
    Jump("loc_60F")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_534")
    Jump("loc_60F")

    label("loc_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_542")
    Jump("loc_60F")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_550")
    Jump("loc_60F")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_60F")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_592")
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_60F")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5EA")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 1200, 750, -1000, 270)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 650, -1000, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E5")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_5E5")

    Jump("loc_60F")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_60F")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_60F")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60F")

    label("loc_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_62E")

    Return()

    # Function_3_3E2 end

    def Function_4_62F(): pass

    label("Function_4_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_641")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_667")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_667")

    Return()

    # Function_4_62F end

    def Function_5_668(): pass

    label("Function_5_668")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_740")

    ChrTalk(
        0xA,
        (
            "The resumption of the mine seems to be still early\x01",
            "I am afraid … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone's feelings in the town\x01",
            "To be one,\x01",
            "After all it is only this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this way my husbands\x01",
            "I want you to work as hard as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7BC")

    label("loc_740")


    ChrTalk(
        0xA,
        (
            "In this way my husbands\x01",
            "I want you to work as hard as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I also made delicious lunch,\x01",
            "I have to support my husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BC")

    Jump("loc_131B")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_86C")

    ChrTalk(
        0xA,
        (
            "Alecったら、町の近くにいた狼に\x01",
            "I was approaching and stroking you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Cooperating with resistance\x01",
            "I am glad because it's a clever animal … …\x01",
            "I want you to be a little more careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_968")

    ChrTalk(
        0xA,
        (
            "Even just it is a noisy situation,\x01",
            "My husband does not have to enter the mine\x01",
            "In a sense I'm relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, as it is\x01",
            "Mainz is on the verge of being lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The president is also outside the city\x01",
            "I almost never put in my hands,\x01",
            "I wonder what will happen in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9FB")

    label("loc_968")


    ChrTalk(
        0xA,
        (
            "While closing the mine,\x01",
            "Mainz is on the verge of being lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The president is also outside the city\x01",
            "I almost never put in my hands,\x01",
            "I wonder what will happen in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FB")

    Jump("loc_131B")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA6")

    ChrTalk(
        0xA,
        (
            "My husband, in the occupation case during this time\x01",
            "I was slightly injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it was not a big deal\x01",
            "Although it was good, …\x01",
            "I was really worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2A")

    label("loc_AA6")


    ChrTalk(
        0xA,
        (
            "My husband has already returned to mine, but ….\x01",
            "I thought what happened at that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is nice to be brave,\x01",
            "You do not want to be too crowded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2A")

    Jump("loc_131B")

    label("loc_B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")

    ChrTalk(
        0xA,
        (
            "On the rainy day inside the mine\x01",
            "It's quite cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But all the miners\x01",
            "Even light clothing seems like normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whew, kaze something\x01",
            "I do not have to draw.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C54")

    label("loc_BD9")


    ChrTalk(
        0xA,
        (
            "On the rainy day inside the mine\x01",
            "It's pretty cool,\x01",
            "All the miners are light clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whew, kaze something\x01",
            "I do not have to draw.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C54")

    Jump("loc_131B")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CC9")

    ChrTalk(
        0xA,
        (
            "Alecったら何をあんな\x01",
            "I wonder if he is screaming loud ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If it is annoying\x01",
            "Because it is not done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD5")

    ChrTalk(
        0xA,
        (
            "With the influence of the husband who is the mining chief,\x01",
            "Alecは鉱員を目指してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually I would like to disagree … ….\x01",
            "The parents want to do what the child wants\x01",
            "It is not good to give out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To prevent at least a major injury,\x01",
            "Until you become an adult\x01",
            "I have to watch them properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6E")

    label("loc_DD5")


    ChrTalk(
        0xA,
        (
            "With the influence of the husband who is the mining chief,\x01",
            "Alecは鉱員を目指してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually I would like to disagree … ….\x01",
            "I think that girl seriously,\x01",
            "You should watch over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6E")

    Jump("loc_131B")

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")

    ChrTalk(
        0xA,
        (
            "毎日、Alecが危険な場所に\x01",
            "I'm worried if I step in on foot … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On Sunday School Day,\x01",
            "Because the sister will see\x01",
            "You can be relieved a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F88")

    label("loc_F19")


    ChrTalk(
        0xA,
        (
            "While I go to Sunday school\x01",
            "Do not worry about children\x01",
            "Looks nice … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it's no problem\x01",
            "Shall we relax?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F88")

    Jump("loc_131B")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E2")

    ChrTalk(
        0xA,
        (
            "Yesterday, to a husband working at a mine\x01",
            "I went to deliver your lunch ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "そこで、Alecが勝手に\x01",
            "Please find out that you were in the mine.\x01",
            "I scolded it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because I'm dangerous, I do not want to go in.\x01",
            "Even though I always tell you,\x01",
            "I wish that girl ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even my husband is too big,\x01",
            "I do not want you to worry too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_115B")

    label("loc_10E2")


    ChrTalk(
        0xA,
        (
            "Because the mine is dangerous\x01",
            "Even though I always tell you,\x01",
            "I wish that girl ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "More about me\x01",
            "I want you to listen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115B")

    Jump("loc_131B")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11EE")

    ChrTalk(
        0xA,
        (
            "Hoffman, if you go to the mine\x01",
            "Please forget your lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am hungry,\x01",
            "I have to go to the delivery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_131B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(
        0xA,
        (
            "My child, in danger\x01",
            "I am in trouble because I want to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mr. Ganz must stop this morning\x01",
            "What happened ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It will be a serious injury in the meantime\x01",
            "Not at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_131B")

    label("loc_12B4")


    ChrTalk(
        0xA,
        (
            "My child, I am curious as he is curious.\x01",
            "I want to enter a dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You sure looked like my husband, surely.\x02",
    )

    CloseMessageWindow()

    label("loc_131B")

    TalkEnd(0xFE)
    Return()

    # Function_5_668 end

    def Function_6_131F(): pass

    label("Function_6_131F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1330")
    Jump("loc_13F5")

    label("loc_1330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13A6")

    ChrTalk(
        0xE,
        (
            "Oh, if it's raining\x01",
            "Because I can not play outside, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Dad, come home early\x01",
            "I wonder if you can play with me ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_13A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13B4")
    Jump("loc_13F5")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13C2")
    Jump("loc_13F5")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13D0")
    Jump("loc_13F5")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_13DE")
    Jump("loc_13F5")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13EC")
    Jump("loc_13F5")

    label("loc_13EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_13F5")

    label("loc_13F5")

    TalkEnd(0xFE)
    Return()

    # Function_6_131F end

    def Function_7_13F9(): pass

    label("Function_7_13F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_140A")
    Jump("loc_1668")

    label("loc_140A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AF")

    ChrTalk(
        0x11,
        (
            "In Crossbell City\x01",
            "A lot of big movements\x01",
            "It seems there was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "…. Again, we and our miners also\x01",
            "Do not leave it like this.\x01",
            "Why do not you talk to the mayor …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_14EE")

    label("loc_14AF")


    ChrTalk(
        0x11,
        (
            "俺達鉱員もDo not leave it like this.\x01",
            "Why do not you talk to the mayor …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EE")

    Jump("loc_1668")

    label("loc_14F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DA")

    ChrTalk(
        0x11,
        (
            "Become an independent country,\x01",
            "Because the transactions of Seven Yaishi have drastically decreased\x01",
            "Once the mine was closed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Trade with other countries is completely\x01",
            "I just stopped.\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Honestly I do not stop … …\x01",
            "For now I only have to see the situation\x01",
            "Hey, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1668")

    label("loc_15DA")


    ChrTalk(
        0x11,
        (
            "Become an independent country,\x01",
            "Because the transactions of Seven Yaishi have drastically decreased\x01",
            "Once the mine was closed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Honestly I do not stop … …\x01",
            "For now I only have to see the situation\x01",
            "Hey, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    TalkEnd(0xFE)
    Return()

    # Function_7_13F9 end

    def Function_8_166C(): pass

    label("Function_8_166C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1745")

    ChrTalk(
        0xB,
        (
            "Rosie returned to the mine,\x01",
            "I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Crossbell\x01",
            "What will happen in the future\x01",
            "I do not know yet ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Young people steadily\x01",
            "As long as you put your feet on the ground,\x01",
            "Surely the future will be opened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17C4")

    label("loc_1745")


    ChrTalk(
        0xB,
        (
            "Rosie returned to the mine,\x01",
            "I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Young people steadily\x01",
            "As long as you put your feet on the ground,\x01",
            "Surely the future will be opened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_2405")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_18BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186E")

    ChrTalk(
        0xB,
        (
            "In an invalid declaration of an independent country,\x01",
            "Presence as President\x01",
            "The legitimacy was also frustrated …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We are now in history\x01",
            "I am at a big crossroads\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18B6")

    label("loc_186E")


    ChrTalk(
        0xB,
        (
            "We are now in history\x01",
            "I am at a big crossroads\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    Jump("loc_2405")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198E")

    ChrTalk(
        0xB,
        (
            "Crossbell independence\x01",
            "To develop into the situation so far\x01",
            "I did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As the mine was blocked\x01",
            "Rosie lost her energy\x01",
            "It seems I got it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ha, what should I do?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19F8")

    label("loc_198E")


    ChrTalk(
        0xB,
        (
            "Rosie is getting big\x01",
            "Finding a motivation for the work of the mine\x01",
            "Even though I was …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ha, what should I do?\x02",
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_2405")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A96")

    ChrTalk(
        0xB,
        (
            "Like the era of conflict,\x01",
            "Occupation of Mainz\x01",
            "It will not happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, the crossbells are united\x01",
            "I wonder what happened … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_1A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6C")

    ChrTalk(
        0xB,
        (
            "People who go out into town recently\x01",
            "Although it is increasing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Rosie and young people,\x01",
            "Pride the city of Mainz\x01",
            "I am thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have lived in this town for a long time\x01",
            "To me, no more\x01",
            "I do not feel happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BF8")

    label("loc_1B6C")


    ChrTalk(
        0xB,
        (
            "Rosie and young people,\x01",
            "Pride the city of Mainz\x01",
            "I am thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have lived in this town for a long time\x01",
            "To me, no more\x01",
            "I do not feel happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF8")

    Jump("loc_2405")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(
        0xB,
        (
            "Rosie is properly\x01",
            "Being to work,\x01",
            "Every day seems to be fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehuu, even my daughter-in-law\x01",
            "If you bring me\x01",
            "I can relieve too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, not much.\x01",
            "I wonder if it is ahead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D3C")

    label("loc_1CCD")


    ChrTalk(
        0xB,
        (
            "Rosie is also a wife\x01",
            "If you bring me\x01",
            "I can relieve too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, not much.\x01",
            "I wonder if it is ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3C")

    Jump("loc_2405")

    label("loc_1D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3C")

    ChrTalk(
        0xB,
        "Crossbell's national independence ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have lived in this place until now\x01",
            "I have no real talk but,\x01",
            "It will be very nice if you realize it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Both the Empire and the Republic\x01",
            "You should never do well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To a new battle of battle\x01",
            "I wish I had not done it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EB7")

    label("loc_1E3C")


    ChrTalk(
        0xB,
        (
            "Proposed independence,\x01",
            "The fact that the Empire and the Republic are silent\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To a new battle of battle\x01",
            "I wish I had not done it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB7")

    Jump("loc_2405")

    label("loc_1EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB8")

    ChrTalk(
        0xB,
        (
            "In the past, there was a fall accident at Takayama\x01",
            "Mudslide something\x01",
            "It was something that happened often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But after the revolutionary guidance\x01",
            "Drilling technology has also been established,\x01",
            "Accidents rarely occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Technological progress definitely saves people.\x01",
            "It was a very good age.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_204D")

    label("loc_1FB8")


    ChrTalk(
        0xB,
        (
            "In the past there were falling accidents and landslides\x01",
            "It happened frequently … ….\x01",
            "There are hardly any recent days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Technological progress definitely saves people.\x01",
            "It was a very good age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204D")

    Jump("loc_2405")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_213D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DE")

    ChrTalk(
        0xB,
        (
            "Amiとロージーは、\x01",
            "It is noisy when two people are ready\x01",
            "nothing I can do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, well brothers and sisters\x01",
            "It's good and good-bye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2138")

    label("loc_20DE")


    ChrTalk(
        0xB,
        "Even so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do not play with two people,\x01",
            "Even with housekeeping help\x01",
            "I wish I could do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2138")

    Jump("loc_2405")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(
        0xB,
        (
            "Recently, my grandchild Rosie\x01",
            "Without skipping work properly\x01",
            "It came to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, there is nothing so pleasant.\x01",
            "…… Thank you, the sky goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_228D")

    label("loc_21EB")


    ChrTalk(
        0xB,
        (
            "My grandchildren to a human servant\x01",
            "What will become it is,\x01",
            "What's more than anything for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Thank you, the sky goddess.\x01",
            "We will continue to hold the children\x01",
            "Please be watchful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228D")

    Jump("loc_2405")

    label("loc_2292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2380")

    ChrTalk(
        0xB,
        (
            "The former mine just out of town,\x01",
            "It's a major tunnel a few decades ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "During the heyday, large crystals\x01",
            "It was excavated with cracks\x01",
            "It was a mountain of treasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Long ago, the Empire and the Republic\x01",
            "I fought repeatedly through conflict\x01",
            "It is a place to say it is one reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2405")

    label("loc_2380")


    ChrTalk(
        0xB,
        (
            "The former mine has been mined out\x01",
            "I have become an abandoned mine … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In ancient crossbells,\x01",
            "Undoubtedly important\x01",
            "It certainly was a place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2405")

    TalkEnd(0xFE)
    Return()

    # Function_8_166C end

    def Function_9_2409(): pass

    label("Function_9_2409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_241A")
    Jump("loc_25DF")

    label("loc_241A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_251E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D9")

    ChrTalk(
        0xD,
        (
            "Oh, you guys\x01",
            "Without rasping in the rain\x01",
            "Were you walking around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I see ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Indeed,\x01",
            "\"Water too dripping good man\"\x01",
            "I guess it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2519")

    label("loc_24D9")


    ChrTalk(
        0xD,
        (
            "You guys, exactly\x01",
            "\"Water too dripping good man\"\x01",
            "That's right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    Jump("loc_25DF")

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_252C")
    Jump("loc_25DF")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_253A")
    Jump("loc_25DF")

    label("loc_253A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2548")
    Jump("loc_25DF")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2563")
    Call(0, 10)
    Jump("loc_25C3")

    label("loc_2563")


    ChrTalk(
        0xD,
        (
            "brother,\x01",
            "Because it does not have a floating story\x01",
            "It's boring, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I am similar, though.\x02",
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_25DF")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25D6")
    Jump("loc_25DF")

    label("loc_25D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_25DF")

    label("loc_25DF")

    TalkEnd(0xFE)
    Return()

    # Function_9_2409 end

    def Function_10_25E3(): pass

    label("Function_10_25E3")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xD,
        (
            "Hey Hey, Onii-chan.\x01",
            "Does not it have anything that has floated up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That's not it.\x01",
            "I only have a woman or a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "What, it is boring ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, if it is Mr. Gantz?\x01",
            "With a casino and a beautiful bunny girl\x01",
            "Doing ha ha ha … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "You know!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_10_25E3 end

    def Function_11_26F1(): pass

    label("Function_11_26F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2702")
    Jump("loc_27DD")

    label("loc_2702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2710")
    Jump("loc_27DD")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_271E")
    Jump("loc_27DD")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_272C")
    Jump("loc_27DD")

    label("loc_272C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_273A")
    Jump("loc_27DD")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")
    Call(0, 10)
    Jump("loc_27C1")

    label("loc_2755")


    ChrTalk(
        0x10,
        (
            "ったく、Amiと話すのは\x01",
            "It is very painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because it is a pity holiday\x01",
            "Please let me fall in love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C1")

    Jump("loc_27DD")

    label("loc_27C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27D4")
    Jump("loc_27DD")

    label("loc_27D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_27DD")

    label("loc_27DD")

    TalkEnd(0xFE)
    Return()

    # Function_11_26F1 end

    def Function_12_27E1(): pass

    label("Function_12_27E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AC")

    ChrTalk(
        0xC,
        (
            "Max regained her energy\x01",
            "I am relieved too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The figures that miners are devoted to their work\x01",
            "As expected after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I am a Mainz woman,\x01",
            "I have to support them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_292B")

    label("loc_28AC")


    ChrTalk(
        0xC,
        (
            "Max and miners\x01",
            "A figure to drive into work\x01",
            "As expected after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I am a Mainz woman,\x01",
            "I have to support them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292B")

    Jump("loc_3465")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")

    ChrTalk(
        0xC,
        (
            "Resistance people\x01",
            "You seem to be preparing something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Like in the occupation case,\x01",
            "If the people of the guard hurt\x01",
            "We can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I really want you to be careful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A92")

    label("loc_2A0C")


    ChrTalk(
        0xC,
        (
            "…… Like in the occupation case,\x01",
            "If the people of the guard hurt\x01",
            "We can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I really want you to be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_2A92")

    Jump("loc_3465")

    label("loc_2A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB2")
    Call(0, 13)
    Jump("loc_2B4A")

    label("loc_2AB2")


    ChrTalk(
        0xC,
        (
            "Max is\x01",
            "What I can not do my favorite work\x01",
            "I feel sick, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if I managed to forcibly\x01",
            "I have to get it done.\x01",
            "This situation will get sick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4A")

    Jump("loc_3465")

    label("loc_2B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF7")

    ChrTalk(
        0xC,
        (
            "To help us,\x01",
            "Everyone of the guards\x01",
            "It was a victim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The people waiting for them also\x01",
            "Let's have it … no words.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C48")

    label("loc_2BF7")


    ChrTalk(
        0xC,
        (
            "To the guards as well,\x01",
            "Let's be waiting people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "… … There is no word.\x02",
    )

    CloseMessageWindow()

    label("loc_2C48")

    Jump("loc_3465")

    label("loc_2C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D34")

    ChrTalk(
        0xC,
        (
            "You are Mainz on a rainy day\x01",
            "You must be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you slip your feet,\x01",
            "Hold on to the bottom of a cliff … …\x01",
            "Because it can be such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I and Max, too,\x01",
            "I was careful when I was little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DAE")

    label("loc_2D34")


    ChrTalk(
        0xC,
        (
            "You are Mainz on a rainy day\x01",
            "You must be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I and Max, too,\x01",
            "I was careful when I was little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DAE")

    Jump("loc_3465")

    label("loc_2DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAD")

    ChrTalk(
        0xC,
        (
            "Recently, my husband got strange\x01",
            "Just tighten your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mr. Ganz and Rosie\x01",
            "Because I was motivated,\x01",
            "It seems that my husband also got a light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Every morning I got to go early,\x01",
            "I also prepare lunch boxes\x01",
            "It was quite easy to become a Taehen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F5B")

    label("loc_2EAD")


    ChrTalk(
        0xC,
        (
            "Mr. Ganz and Rosie\x01",
            "Because I was motivated,\x01",
            "It seems that my husband also got a fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Every morning I got to go early,\x01",
            "I also prepare lunch boxes\x01",
            "It was quite easy to become a Taehen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5B")

    Jump("loc_3465")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3036")

    ChrTalk(
        0xC,
        (
            "Anything, in the mountains in the north\x01",
            "A big demon has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is a place not far from the town,\x01",
            "I am worried whether it will come out also in the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you become a large devil, you are the only miner\x01",
            "I can not deal with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30C3")

    label("loc_3036")


    ChrTalk(
        0xC,
        (
            "In the mountains in the north\x01",
            "A big demon has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I am worried whether it will come out also in the mine.\x01",
            "If you become a large devil, you are the only miner\x01",
            "I can not deal with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C3")

    Jump("loc_3465")

    label("loc_30C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_315E")

    ChrTalk(
        0xC,
        (
            "In Crossbell City\x01",
            "There is something trade meeting\x01",
            "It seems that it is open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Depending on the content of the meeting,\x01",
            "In the future of Mainz\x01",
            "Is there an influence?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31F9")

    ChrTalk(
        0xC,
        (
            "Max, today\x01",
            "I entered the drink with the mining chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I usually work as much as I do,\x01",
            "On a day off, I firmly\x01",
            "You must change your mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_31F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E0")

    ChrTalk(
        0xC,
        (
            "Attracted by the buried seven ice stone,\x01",
            "Demons come to mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is dangerous if it is normal,\x01",
            "Mainz's miners\x01",
            "Oh yeah, with a strong male guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it is a little or softly demon\x01",
            "I manage to manage myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3350")

    label("loc_32E0")


    ChrTalk(
        0xC,
        (
            "Mainz's miners\x01",
            "Oh yeah, with a strong male guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it is a demon beast that got into a mine\x01",
            "I manage to manage myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3350")

    Jump("loc_3465")

    label("loc_3355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3402")

    ChrTalk(
        0xC,
        (
            "My husband,\x01",
            "Do the miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Within the current youngsters\x01",
            "It is the biggest bread maker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, today as well\x01",
            "Prepare plenty of dinner\x01",
            "I have to wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3465")

    label("loc_3402")


    ChrTalk(
        0xC,
        (
            "Well, today, my husband\x01",
            "Hungry\x01",
            "I will come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Prepare plenty of dinner\x01",
            "I have to wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3465")

    TalkEnd(0xFE)
    Return()

    # Function_12_27E1 end

    def Function_13_3469(): pass

    label("Function_13_3469")

    OP_4B(0xC, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "Ha ha … … I only dig holes\x01",
            "Even though I do not care,\x01",
            "It is impossible for mine to work …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Max, even getting down\x01",
            "Let's do it badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After a while I will also go to the mine\x01",
            "I will get in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I hope so ….\x01",
            "…………… Ha ~ ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… Completely.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_3469 end

    def Function_14_3586(): pass

    label("Function_14_3586")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3597")
    Jump("loc_3685")

    label("loc_3597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3633")

    ChrTalk(
        0x12,
        (
            "Because I can not do mine work,\x01",
            "Do you know the town's heavy lifting\x01",
            "I do a lot of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However,\x01",
            "I wish I had not entered the mine …\x01",
            "I do not feel good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3685")

    label("loc_3633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364E")
    Call(0, 13)
    Jump("loc_3685")

    label("loc_364E")


    ChrTalk(
        0x12,
        (
            "Ha ha … … I only dig holes\x01",
            "Even though I do not have a job … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3685")

    TalkEnd(0xFE)
    Return()

    # Function_14_3586 end

    def Function_15_3689(): pass

    label("Function_15_3689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A0")
    Call(0, 24)
    Return()

    label("loc_36A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36BF")
    Call(0, 16)
    Return()

    label("loc_36BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_383B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C6")

    ChrTalk(
        0x8,
        (
            "It was a resistance\x01",
            "Guards, safely\x01",
            "It seems that we could join the Defense Forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that the president was detained … …\x01",
            "There is no reason to oppose them anymore\x01",
            "It's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mireille's resistance activities, too,\x01",
            "That is why he finally succeeded.\x01",
            "…… I was relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3836")

    label("loc_37C6")


    ChrTalk(
        0x8,
        (
            "Mainz also resumed the mine,\x01",
            "I began to regain liveliness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However,\x01",
            "It's about a real fight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3836")

    Jump("loc_4763")

    label("loc_383B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3947")

    ChrTalk(
        0x8,
        (
            "The president's legitimacy is shaken,\x01",
            "I hear that Defense Forces have also come to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mireilleu guys,\x01",
            "Looking at the release of Crossbell City\x01",
            "It seems that he is getting ready steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Resistance people\x01",
            "To accomplish the mission safely,\x01",
            "Let's say the goddess pray.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39FB")

    label("loc_3947")


    ChrTalk(
        0x8,
        (
            "Mireilleu guys,\x01",
            "Looking at the release of Crossbell City\x01",
            "It seems that he is getting ready steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Resistance people\x01",
            "To accomplish the mission safely,\x01",
            "Let's say the goddess pray.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FB")

    Jump("loc_4763")

    label("loc_3A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1B")
    Call(0, 17)
    Jump("loc_3ACD")

    label("loc_3A1B")


    ChrTalk(
        0x8,
        (
            "Originally in Mainz,\x01",
            "Operate that soldiers calmly\x01",
            "The president had only distrust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I scratch trying to manage my current system\x01",
            "Resistance people,\x01",
            "It is hope for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ACD")

    Jump("loc_4763")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB9")

    ChrTalk(
        0x8,
        "Are you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMayor of Vixen……\x01",
            "Mainz was also serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah……\x01",
            "There was hardly any serious damage\x01",
            "As expected, everyone is shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have the cooperation of the Zoukokushin also,\x01",
            "For a while to heal it\x01",
            "I was concentrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe impact of the incident was substantial\x01",
            "I guess it was ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh … now it is Oita,\x01",
            "It seems to have calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as I am the mayor\x01",
            "As much as possible\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys are going to have difficulties\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 2)
    Jump("loc_3D34")

    label("loc_3CB9")


    ChrTalk(
        0x8,
        (
            "Anyway, as I am the mayor\x01",
            "As much as possible\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys are going to have difficulties\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D34")

    Jump("loc_4763")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")

    ChrTalk(
        0x8,
        (
            "Recently, large monsters that may be subjects\x01",
            "Do not listen to the story that you saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in a derailment accident that happened yesterday,\x01",
            "It is said that a huge monster was witnessed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These were formerly mine\x01",
            "With large monsters that appeared\x01",
            "Is there anything to do with it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, for the safety of everyone\x01",
            "It seems better to keep in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F0B")

    label("loc_3E7D")


    ChrTalk(
        0x8,
        (
            "Recently, large monsters that may be subjects\x01",
            "I often listen to talk that you have seen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, for the safety of everyone\x01",
            "It seems better to keep in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0B")

    Jump("loc_4763")

    label("loc_3F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4047")

    ChrTalk(
        0x8,
        (
            "Recently, hawkers\x01",
            "You seem to be busier than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is not so urgent request\x01",
            "It became less reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Apparently saying recently\x01",
            "Large and unnoticeable demons\x01",
            "It seems to be investigating … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I have a bad feeling.\x01",
            "Something on the crossbell\x01",
            "Is it going to happen …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40CA")

    label("loc_4047")


    ChrTalk(
        0x8,
        (
            "The busyness of the hushman,\x01",
            "It seems that it has increased recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I have a bad feeling.\x01",
            "Something on the crossbell\x01",
            "Is it going to happen …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CA")

    Jump("loc_4763")

    label("loc_40CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E0")

    ChrTalk(
        0x8,
        (
            "Crossbell's national independence ……\x01",
            "No way it is\x01",
            "It is said that the proposed date will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For mine resources Empire and Republic\x01",
            "Even in this town with a contested history,\x01",
            "It is a question to be seriously discussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For that matter,\x01",
            "To each residents of Mainz\x01",
            "I have to think about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426B")

    label("loc_41E0")


    ChrTalk(
        0x8,
        (
            "Whether national independence is\x01",
            "Every person in Mainz residents\x01",
            "I have to think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until the voting day I will also be a resident,\x01",
            "Let's say you are thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426B")

    Jump("loc_4763")

    label("loc_4270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4352")

    ChrTalk(
        0x8,
        "Gantz is a generous man with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if you rarely win at the casino,\x01",
            "Delivering prizes and buying alcohol\x01",
            "It will be used immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rather, after returning home\x01",
            "Do not let the Mira fly away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D2")

    label("loc_4352")


    ChrTalk(
        0x8,
        (
            "Gantz is better than go home\x01",
            "The one who wins and returns\x01",
            "I feel Mira is flying away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, it seems that he seems to be like him.\x02",
    )

    CloseMessageWindow()

    label("loc_43D2")

    Jump("loc_4763")

    label("loc_43D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F1")

    ChrTalk(
        0x8,
        (
            "Skyscraper Building,\x01",
            "Orkis Tower ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The progress of technology is great\x01",
            "I would like to welcome you,\x01",
            "I feel somewhat complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The town called Mainz is one step further\x01",
            "I feel I was left behind in the era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Ha ha, do not mind it.\x01",
            "It's just a senior idiot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_457C")

    label("loc_44F1")


    ChrTalk(
        0x8,
        (
            "Anyway, to hold a trade meeting\x01",
            "I think there is great significance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of the future of autonomous province,\x01",
            "To the mayor of Dieter\x01",
            "I hope you do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_457C")

    Jump("loc_4763")

    label("loc_4581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_460F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4599")
    Jump("loc_460A")

    label("loc_4599")


    ChrTalk(
        0x8,
        (
            "The key of the old mine,\x01",
            "Just to be sure for you\x01",
            "Let's pass it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so sometimes\x01",
            "You will be saved if you look at the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460A")

    Jump("loc_4763")

    label("loc_460F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E3")

    ChrTalk(
        0x8,
        (
            "The former mine left the town,\x01",
            "After a little down\x01",
            "It is located ahead of climbing the northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why the door was broken,\x01",
            "What is happening in the galleries,\x01",
            "We do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "please,\x01",
            "Be careful again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4763")

    label("loc_46E3")


    ChrTalk(
        0x8,
        (
            "The former mine left the town,\x01",
            "After a little down\x01",
            "It is located ahead of climbing the northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Gant's entrance\x01",
            "Because it is open,\x01",
            "Toward me there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4763")

    TalkEnd(0xFE)
    Return()

    # Function_15_3689 end

    def Function_16_4767(): pass

    label("Function_16_4767")


    ChrTalk(
        0x8,
        (
            "Just the other day, I opened the door of a broken old mine\x01",
            "Change to a new sturdy one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, just in case\x01",
            "Will you keep this in my possession?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '旧矿山的钥匙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('旧矿山的钥匙', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00105FWell, is that okay?\x01",
            "Once we are outsiders … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, you guys can trust.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something I want to investigate\x01",
            "Come in freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just to be sure, it will be easier for you to move back and forth\x01",
            "I also dialed the ladder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you very much.\x01",
            "I will keep it carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 3)
    TalkEnd(0x8)
    Return()

    # Function_16_4767 end

    def Function_17_496B(): pass

    label("Function_17_496B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hmm, how about food?\x01",
            "Leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, for maintenance of equipment\x01",
            "Is not oil necessary, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That place is at Bekkarai's shop\x01",
            "Let's check because there will be stockpiles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07902FWell, thank you.\x02\x03",
            "#07908F…… To everyone in Mainz\x01",
            "I can not thank you enough.\x02\x03",
            "#07903FIf you cooperate with us\x01",
            "If you are a defense army,\x01",
            "Given that danger … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha, what kind of …\x01",
            "Please do not mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Originally in Mainz,\x01",
            "Operate that soldiers calmly\x01",
            "The president had only distrust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Meanwhile … … to contradict the present situation\x01",
            "What you showed in Resistance,\x01",
            "It is nothing but hope for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, as much as possible,\x01",
            "I will cooperate with your activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07904F……Thank you.\x01",
            "I will never forget this kindness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_17_496B end

    def Function_18_4C76(): pass

    label("Function_18_4C76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D90")

    ChrTalk(
        0x9,
        (
            "Long resistance activities,\x01",
            "Mireille's guards\x01",
            "It worked really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When leaving the town, again and again\x01",
            "He told me a thank you ….\x01",
            "We would like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When everything is done and it calms down,\x01",
            "I'm sure they will\x01",
            "I want to invite him to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E32")

    label("loc_4D90")


    ChrTalk(
        0x9,
        (
            "Long resistance activities,\x01",
            "Mireille's guards\x01",
            "It worked really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When everything is done and it calms down,\x01",
            "I'm sure they will\x01",
            "I want to invite him to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E32")

    Jump("loc_5D2F")

    label("loc_4E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F03")

    ChrTalk(
        0x9,
        (
            "Mireille now,\x01",
            "It seems like you are taking a rest at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm getting more busy soon\x01",
            "That's what I was talking about ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On this occasion, a proper holiday\x01",
            "I would like you to take it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F7D")

    label("loc_4F03")


    ChrTalk(
        0x9,
        (
            "Mireille now,\x01",
            "It seems like you are taking a rest at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On this occasion, a proper holiday\x01",
            "I would like you to take it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7D")

    Jump("loc_5D2F")

    label("loc_4F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_50CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5082")

    ChrTalk(
        0x9,
        (
            "Resistance folks\x01",
            "To the point where the mountainous area is complicated\x01",
            "I heard that they are camping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even though I'm accustomed to outdoor activities,\x01",
            "It should be painful that this state will prolong ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Searching for defense forces and hunters,\x01",
            "If you calm down for a while\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50C8")

    label("loc_5082")


    ChrTalk(
        0x9,
        (
            "Searching for defense forces and hunters,\x01",
            "If you calm down for a while\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C8")

    Jump("loc_5D2F")

    label("loc_50CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_523D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A6")

    ChrTalk(
        0x9,
        (
            "During this time Mr. Eoria,\x01",
            "Herbal tea calming down your heart\x01",
            "Please have them divide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thanks to me in this week,\x01",
            "It got organized quite nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To Eoria\x01",
            "You must thank him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5238")

    label("loc_51A6")


    ChrTalk(
        0x9,
        (
            "Mr. Eoria,\x01",
            "Today the devil from the abandoned mine\x01",
            "You came to get rid of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Have someone help me,\x01",
            "They really\x01",
            "You must thank him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5238")

    Jump("loc_5D2F")

    label("loc_523D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5312")

    ChrTalk(
        0x9,
        "The weather in the mountain is easy to collapse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Too busy, even bus operations\x01",
            "There are things that will stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today it is not pouring down there,\x01",
            "You should take care when you come and go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53A8")

    label("loc_5312")


    ChrTalk(
        0x9,
        (
            "If it rains heavily, even bus operations\x01",
            "There are things that will stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today it is not pouring down there,\x01",
            "You should take care when you come and go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A8")

    Jump("loc_5D2F")

    label("loc_53AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5496")

    ChrTalk(
        0x9,
        (
            "The partner of the miners,\x01",
            "I can not find it easily …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Gantz and Mr. Maruro\x01",
            "Rosie also said that,\x01",
            "It seems that it is not interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Young children are less likely to get married\x01",
            "I wonder if I do not long for … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5521")

    label("loc_5496")


    ChrTalk(
        0x9,
        (
            "Mr. Gantz and Mr. Maruro\x01",
            "Rosie also said that,\x01",
            "You do not feel upset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Young children are less likely to get married\x01",
            "I wonder if I do not long for … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5521")

    Jump("loc_5D2F")

    label("loc_5526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_56DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5630")

    ChrTalk(
        0x9,
        (
            "Crossbell in the Empire and the Republic\x01",
            "Together with tax revenues of 10\x01",
            "It is a fixed rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the evolving crossbell of economy\x01",
            "Speaking of 10 of tax revenue is an amazing amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This autonomous state is the second largest country\x01",
            "It is subordinated,\x01",
            "It is an arrangement that can be called a symbol.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56DA")

    label("loc_5630")


    ChrTalk(
        0x9,
        (
            "Crossbell in the Empire and the Republic\x01",
            "Together with tax revenues of 10\x01",
            "It is a fixed rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This autonomous state is the second largest country\x01",
            "It is subordinated,\x01",
            "It is an arrangement that can be called a symbol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56DA")

    Jump("loc_5D2F")

    label("loc_56DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586F")

    ChrTalk(
        0x9,
        "Oh, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's fine\x01",
            "With miners in Mainz\x01",
            "Why do not you try making a match?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F… … Maybe, to me\x01",
            "Are you listening?\x02\x03",
            "I am still at the age we can marry\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, too\x01",
            "It is a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it became bigger and there was no opponent,\x01",
            "Please come and talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F(… … It is slightly rude.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Hahaha ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_58E8")

    label("loc_586F")


    ChrTalk(
        0x9,
        (
            "Huhu, getting bigger\x01",
            "Without partner,\x01",
            "Please come and talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you are a cute girl you want to see\x01",
            "It's a big welcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E8")

    Jump("loc_5D2F")

    label("loc_58ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_597D")

    ChrTalk(
        0x9,
        "I am off the mine today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think that you guys are fine,\x01",
            "If you're planning on entering\x01",
            "Please be careful with demons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2F")

    label("loc_597D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B47")

    ChrTalk(
        0x9,
        "That's right … you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the miners in Mainz\x01",
            "Why do not you try making a match?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FAre you in good condition?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, Mr. Gans\x01",
            "If there is a person waiting for return\x01",
            "I think I can work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What about you, ladies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FEr, um … … I'm sorry.\x01",
            "I have not thought about marriage yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106Fじ, I am also now\x01",
            "Because work is important ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, if you feel like it\x01",
            "Please think about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BB9")

    label("loc_5B47")


    ChrTalk(
        0x9,
        (
            "If you feel like having a marriage,\x01",
            "Please think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am caught\x01",
            "Because I will set it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB9")

    Jump("loc_5D2F")

    label("loc_5BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAE")

    ChrTalk(
        0x9,
        (
            "That former mine, several decades ago\x01",
            "In times when conflict was still happening\x01",
            "It is a used tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because it is complicated and dangerous,\x01",
            "If the predecessor was closed severely\x01",
            "I'm listening ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who broke the key.\x01",
            "It is kind of creepy …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D2F")

    label("loc_5CAE")


    ChrTalk(
        0x9,
        (
            "That old mine,\x01",
            "Because it is complicated and dangerous\x01",
            "I was severely closed ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who broke the key.\x01",
            "It is kind of creepy …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2F")

    TalkEnd(0xFE)
    Return()

    # Function_18_4C76 end

    def Function_19_5D33(): pass

    label("Function_19_5D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4A")
    Call(0, 24)
    Return()

    label("loc_5D4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D5B")
    Jump("loc_5E45")

    label("loc_5D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D69")
    Jump("loc_5E45")

    label("loc_5D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D77")
    Jump("loc_5E45")

    label("loc_5D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D85")
    Jump("loc_5E45")

    label("loc_5D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D93")
    Jump("loc_5E45")

    label("loc_5D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DA1")
    Jump("loc_5E45")

    label("loc_5DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB9")
    Jump("loc_5E37")

    label("loc_5DB9")


    ChrTalk(
        0xF,
        (
            "Such a large grain of seven giant stone\x01",
            "To purchase in large quantities,\x01",
            "I can not manage it because there are merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "…… I was wondering what it was.\x02",
    )

    CloseMessageWindow()

    label("loc_5E37")

    Jump("loc_5E45")

    label("loc_5E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5E45")

    label("loc_5E45")

    TalkEnd(0xFE)
    Return()

    # Function_19_5D33 end

    def Function_20_5E49(): pass

    label("Function_20_5E49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E5A")
    Jump("loc_6087")

    label("loc_5E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5E68")
    Jump("loc_6087")

    label("loc_5E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E83")
    Call(0, 17)
    Jump("loc_6087")

    label("loc_5E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF6")

    ChrTalk(
        0x13,
        (
            "#07903FThe painful situation will not change,\x01",
            "For a while in mountainous areas\x01",
            "I will try hard.\x02\x03",
            "#07901FRandy, everyone at the support department ……\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FOh, I understand.\x02\x03",
            "#00301F… … to hunters and defense forces\x01",
            "You will not lose?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        (
            "#07902FHehuu, who are you talking about?\x02\x03",
            "#07904FAnd everyone in Mainz\x01",
            "I'm cooperating with you,\x01",
            "Surely we are OK.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6087")

    label("loc_5FF6")


    ChrTalk(
        0x13,
        (
            "#07900FRandy, everyone at the support department ……\x01",
            "Please leave it to me.\x02\x03",
            "#07904FEveryone in Mainz\x01",
            "They are cooperating,\x01",
            "Surely we are all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6087")

    TalkEnd(0xFE)
    Return()

    # Function_20_5E49 end

    def Function_21_608B(): pass

    label("Function_21_608B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6185")

    ChrTalk(
        0x14,
        (
            "With the help of the god wolf,\x01",
            "We also became easier to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Watch over the mountain roads and alert for mountainous areas ……\x01",
            "Even just letting them\x01",
            "Because it can considerably reduce the burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Lieutenant Mireilleには、この機に\x01",
            "I want you to take time off as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6226")

    label("loc_6185")


    ChrTalk(
        0x14,
        (
            "Watch over the mountain roads and alert for mountainous areas ……\x01",
            "Even if you just leave them to the gods\x01",
            "You can considerably reduce the burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Lieutenant Mireilleには、この機に\x01",
            "I want you to take time off as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6226")

    TalkEnd(0xFE)
    Return()

    # Function_21_608B end

    def Function_22_622A(): pass

    label("Function_22_622A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6274")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1555), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_624A")
    Sleep(1500)
    Jump("loc_625F")

    label("loc_624A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)

    label("loc_625F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_626F")
    Sleep(333)

    label("loc_626F")

    Jump("Function_22_622A")

    label("loc_6274")

    Return()

    # Function_22_622A end

    def Function_23_6275(): pass

    label("Function_23_6275")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30700.itc", 0x1E)
    LoadChrToIndex("chr/ch30702.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(560, 2250, -1210, 0)
    MoveCamera(312, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 700, 750, -8600, 0)
    SetChrPos(0x102, -500, 750, -8600, 0)
    SetChrPos(0x109, 700, 750, -10000, 0)
    SetChrPos(0x105, -500, 750, -10000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -250, 650, -1000, 90)
    SetChrChipByIndex(0x8, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 600, 750, -500, 135)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2000, 750, -1000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(34000, 1500)
    BeginChrThread(0x9, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0x8, 1, 0, 22)
    OP_0D()
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    Sound(103, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2PExcuse me.\x01",
            "Crossbell Police, Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(34000, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_68(-1500, 250, 0, 4000)

    def lambda_648B():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_648B)
    Sleep(50)

    def lambda_649B():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_649B)
    Sleep(50)

    def lambda_64AB():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_64AB)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xF, 0)
    Sleep(500)

    def lambda_64CA():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64CA)

    def lambda_64E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64E4)
    Sleep(100)

    def lambda_64F8():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64F8)

    def lambda_6512():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6512)
    Sleep(50)

    def lambda_6526():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6526)

    def lambda_6540():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6540)
    Sleep(80)

    def lambda_6554():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6554)

    def lambda_656E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_656E)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#11PHello, you guys.\x01",
            "You bother me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#2PWait a while, for the time being!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PEveryone, I have not been to a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PThose who are Gantz … …\x01",
            "How is your physical condition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2POh, especially without sequelae\x01",
            "I am doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2PThank you very much.\x01",
            "Please let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#6PHehe, it seems to be healthy and more than anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PSo …\x01",
            "In the place called \"former mine\"\x01",
            "Demons have occurred?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, near the town\x01",
            "It became an abandonment several decades ago\x01",
            "It's an old tunnel ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, there are also story talks,\x01",
            "Please sit there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PNow I will make tea.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(1260, 2200, 3060, 0)
    MoveCamera(322, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33750, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3780, 270)
    SetChrPos(0x109, 1250, 950, 1500, 0)
    SetChrPos(0x105, 250, 950, 1500, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, 800, 950, 5100, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -800, 950, 3780, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00005F─ ─ It was blocked\x01",
            "Were the entrance doors destroyed?\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(1260, 1950, 3070, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5POh, though it was decades ago\x01",
            "It was a very solid door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is broken by someone\x01",
            "Humans in the town have discovered … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PBecause there was no abnormality 2 days ago\x01",
            "Perhaps, I think it was yesterday that I was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAbsolutely, doing something joked\x01",
            "There is a fellow bastard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P… … I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PSo, when I looked inside\x01",
            "The monster was wandering around … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PBut well, if it is an old gallery trail or something\x01",
            "Even if there are demons, are not they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNo, that's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhat I thought was strange\x01",
            "Gallery itself#12R噵 噵 噵 噵 噵 噵#That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PGallery itself … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWhat is it?\x01",
            "It's blinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PThe wall itself is a reddish purple light\x01",
            "Is it stained? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PWell, that is ……\x01",
            "It certainly is creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12PWhen it comes to a tunnel a few decades ago\x01",
            "There should have been no lighting lights either.\x02\x03",
            "#00001FWhy is it shining due to its cause?\x01",
            "Surely you are interested …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, there is no harm in the town\x01",
            "As a matter of fact a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI thought you were busy, but\x01",
            "I contacted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PI understood the circumstances.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00001F#12PThe thing that the door was destroyed\x01",
            "It can be seen that there is incidences.\x02\x03",
            "Let's look at the state immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6POK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PGiggle\x01",
            "It sounds like an interesting incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(250)

    ChrTalk(
        0x8,
        (
            "#5PGanz, for you guys\x01",
            "Leave the road open.\x02",
        )
    )

    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5POh, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PThen, I'm going ahead.\x01",
            "Come when you're ready!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -630, 750, 5180, 270)
    Sleep(500)
    OP_95(0xF, -2150, 750, 4460, 2500, 0x0)

    def lambda_6F73():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6F73)
    OP_68(80, 1950, 2060, 3000)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    Sleep(100)
    SetChrSubChip(0x9, 0x2)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(600)
    Sound(104, 0, 100, 0)
    OP_68(1080, 1950, 3060, 1200)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(150)
    OP_6F(0x1)
    WaitChrThread(0xF, 1)
    SetChrFlags(0xF, 0x80)

    ChrTalk(
        0x101,
        (
            "#00002F#12P……Was good.\x01",
            "You look really well, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, thanks to you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PJust Well, Gamble Favorite\x01",
            "You have not changed at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs usual I am on holiday\x01",
            "I will come home at the casino and come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PHehe, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, if you do not bring down yourself\x01",
            "I do not think there is any problem … …\x02\x03",
            "#00005FYes, old mine is\x01",
            "It is a place just out of town, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5Pええ、After a little down\x01",
            "It 's on the tip that climbed the northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI do not know what is the cause.\x01",
            "Be careful again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x8, -890, 950, 3320, 90)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -6530, 750, 60, 270)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -250, 750, -750, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x12A, 0)
    OP_29(0xA2, 0x4, 0x2)
    OP_29(0xA2, 0x1, 0x0)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_23_6275 end

    def Function_24_72C4(): pass

    label("Function_24_72C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1850, 750, -1060, 0)
    MoveCamera(316, 22, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(37200, 0)
    SetChrPos(0x101, 700, 750, -3300, 0)
    SetChrPos(0x102, -500, 750, -3300, 0)
    SetChrPos(0x104, 700, 750, -4500, 0)
    SetChrPos(0x109, -500, 750, -4500, 0)
    SetChrPos(0x105, 100, 750, -5700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PHM……\x01",
            "They are one … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, even if you do not think deeply\x01",
            "Is not it something you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Thanks to you I made a profit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, the culprits during this time\x01",
            "I do not know.\x01",
            "What has come to mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FEr …\x01",
            "Mayor of the mayor, Mr. Ganz,\x01",
            "Hello.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7488():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7488)
    Sleep(50)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        "#11POh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Bad bad, now a bit\x01",
            "I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FDid you mean ……\x01",
            "On the matter of the former mine during this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh no, as to the matter during this time\x01",
            "From that time on, the guard is also several times\x01",
            "It came to a patrol … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe culprit who laid the explosive\x01",
            "The mystery of the abnormality of the tunnel also\x01",
            "Still not understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PFor once, instead of a broken door\x01",
            "Attach a new and sturdy door,\x01",
            "I kept it tightly sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FIn the meantime,\x01",
            "Also worrying about people getting in the wrong place\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… However, apart from that\x01",
            "There is something to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PActually, in the meantime, to Mainz\x01",
            "An eccentric group appeared … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTheir crystals of large seven giant stones\x01",
            "I bought it at a high price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FWhimsical group …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSomehow, anyway\x01",
            "There is a unique atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PA large redheaded middle-aged man\x01",
            "It seems he was led … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, by the way, that redhead,\x01",
            "To Randy's hair color\x01",
            "Just like I was surprised.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F(Sure, that … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P(\"Red constellation\" …… !?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F…… They are\x01",
            "Apart from bought Seven Yarrow\x01",
            "Are you doing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo, do you have a special suspicious behavior\x01",
            "I did not mean it … …\x01",
            "I can not see it like a trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSome who have destroyed the door of the old mine\x01",
            "As it is not clear,\x01",
            "I was concerned … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F(Randy's seniors' story,\x01",
            "The culprit who laid the explosive is exactly\x01",
            "It seems they were … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F(Well, there is no clear evidence\x01",
            "You'd better face down. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(But the hunting soldiers are\x01",
            "Purchasing Seven Yarrow Stone Crystals\x01",
            "I wonder what he is going to do … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301F(… … The \"Crimson Shokai\"\x01",
            "It leads to merchants who are not even\x01",
            "I have a lot of connections. )\x02\x03",
            "#00303F(If it is a large grain of seven oysters,\x01",
            "If they let them handle it on the dark route\x01",
            "I am going to make a good pocket money. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F(I see. ….)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#11P…… Hmm, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAgain, you guys\x01",
            "It seems better to keep it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)

    ChrTalk(
        0x8,
        "#5PGantt, give it to me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "Oh, I understand.\x02",
    )

    CloseMessageWindow()

    def lambda_7C91():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7C91)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "Here, do not accept it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '旧矿山的钥匙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('旧矿山的钥匙', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#6PIs this the old mine …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh, it's a so-called spare key.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWell, is that okay?\x01",
            "Once we are outsiders … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, you guys can trust.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今後、If there is something I want to investigate\x01",
            "Come in freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just to be sure, it will be easier for you to move back and forth\x01",
            "I also dialed the ladder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you very much.\x01",
            "I will cherish it carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0x8, 0xF, 0)
    TurnDirection(0xF, 0x8, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14F, 2)
    OP_29(0xA3, 0x1, 0x3)
    SetChrPos(0x0, 0, 750, -3500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_72C4 end

    SaveToFile()

Try(main)
