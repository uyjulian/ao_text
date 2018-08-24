from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Town Mayor Bickson",     # 1
        "Mrs. Anna",              # 2
        "Miranda",                # 3
        "Grandma Burma",          # 4
        "Lurieda",                # 5
        "Ami",                    # 6
        "Alec",                   # 7
        "Miner Gantz",            # 8
        "Miner Logy",             # 9
        "Mine Captain Hoffman",   # 10
        "Miner Max",              # 11
        "2nd Lt. Mireille",       # 12
        "CGF Member",             # 13
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
        "Function_6_14D1",         # 06, 6
        "Function_7_15B3",         # 07, 7
        "Function_8_18E1",         # 08, 8
        "Function_9_282A",         # 09, 9
        "Function_10_2A0B",        # 0A, 10
        "Function_11_2B0B",        # 0B, 11
        "Function_12_2BFA",        # 0C, 12
        "Function_13_390E",        # 0D, 13
        "Function_14_3A1F",        # 0E, 14
        "Function_15_3B31",        # 0F, 15
        "Function_16_4D09",        # 10, 16
        "Function_17_4F04",        # 11, 17
        "Function_18_51F9",        # 12, 18
        "Function_19_6304",        # 13, 19
        "Function_20_6421",        # 14, 20
        "Function_21_6696",        # 15, 21
        "Function_22_6876",        # 16, 22
        "Function_23_68C1",        # 17, 23
        "Function_24_79DF",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_82E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C")

    ChrTalk(
        0xA,
        (
            "I feel like it's still\x01",
            "too early to reopen the\x01",
            "mine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If everyone in town wants\x01",
            "it, I suppose there's\x01",
            "nothing I can do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because things turned like this,\x01",
            "I'd like my husband and the others\x01",
            "to work their very hardest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_829")

    label("loc_77C")


    ChrTalk(
        0xA,
        (
            "Because things turned like this,\x01",
            "I'd like my husband and the others\x01",
            "to work their very hardest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to make a delicious\x01",
            "lunchbox to support my\x01",
            "husband as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_829")

    Jump("loc_14CD")

    label("loc_82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8FF")

    ChrTalk(
        0xA,
        (
            "That Alec. He approached a\x01",
            "wolf near town without\x01",
            "hesitation and petted him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank goodness they are smart animals\x01",
            "cooperating with the resistance... I\x01",
            "think we can relax a little now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CD")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(
        0xA,
        (
            "Things are dangerous as it is. I\x01",
            "can relax a little because my\x01",
            "husband is finished in the mines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But at this rate, Mainz\x01",
            "will decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President has hardly touched\x01",
            "anywhere outside the city. I\x01",
            "wonder what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB0")

    label("loc_A11")


    ChrTalk(
        0xA,
        (
            "With the mine closed\x01",
            "like this, Mainz will\x01",
            "decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President has hardly touched\x01",
            "anywhere outside the city. I\x01",
            "wonder what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB0")

    Jump("loc_14CD")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B63")

    ChrTalk(
        0xA,
        (
            "My husband was injured\x01",
            "the other day during the\x01",
            "Mainz occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's all right because\x01",
            "it wasn't a big deal...\x01",
            "but I'm really worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BFF")

    label("loc_B63")


    ChrTalk(
        0xA,
        (
            "My husband still hasn't reopened\x01",
            "the mine. We still don't know\x01",
            "what happened back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He is brave, but I wish\x01",
            "he wouldn't push himself\x01",
            "so hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFF")

    Jump("loc_14CD")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBD")

    ChrTalk(
        0xA,
        (
            "It's rather cold in the\x01",
            "mine on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But the miners are\x01",
            "lightly dressed and\x01",
            "appear to be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Goodness. I hope they\x01",
            "don't catch colds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D39")

    label("loc_CBD")


    ChrTalk(
        0xA,
        (
            "It's cold in the mine on\x01",
            "rainy days, but the miners\x01",
            "are lightly dressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Goodness. I hope they\x01",
            "don't catch colds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D39")

    Jump("loc_14CD")

    label("loc_D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA7")

    ChrTalk(
        0xA,
        (
            "That Alec. What is he\x01",
            "screaming this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's annoying. I wish\x01",
            "he'd stop that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CD")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC9")

    ChrTalk(
        0xA,
        (
            "Due to the influence of my\x01",
            "husband, the mine captain,\x01",
            "Alec wants to be a miner too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, I'm against it... But it's\x01",
            "not good for parents to interfere\x01",
            "with that their children want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've at least got to\x01",
            "keep him safe until he's\x01",
            "an adult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F78")

    label("loc_EC9")


    ChrTalk(
        0xA,
        (
            "Due to the influence of my\x01",
            "husband, the mine captain,\x01",
            "Alec wants to be a miner too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, I'm against it...\x01",
            "But if he's serious about\x01",
            "it, I must watch over him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F78")

    Jump("loc_14CD")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1022")

    ChrTalk(
        0xA,
        (
            "Every day, I worry that\x01",
            "Alec will go somewhere\x01",
            "dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On Sunday School days,\x01",
            "the sister watches him\x01",
            "so I can relax a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A0")

    label("loc_1022")


    ChrTalk(
        0xA,
        (
            "It seems there's no need\x01",
            "to worry when the kids\x01",
            "are at Sunday School...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since you're here, make\x01",
            "yourselves at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A0")

    Jump("loc_14CD")

    label("loc_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122C")

    ChrTalk(
        0xA,
        (
            "Yesterday, I went to deliver\x01",
            "my husband's lunchbox inside\x01",
            "the mine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There, I found Alec, who\x01",
            "had wandered inside. And\x01",
            "I scolded him, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've told him many times that it's\x01",
            "dangerous and not to go in there,\x01",
            "but when it comes to that kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have my hands full with my\x01",
            "husband. I wish he wouldn't worry\x01",
            "me any more than he already does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BA")

    label("loc_122C")


    ChrTalk(
        0xA,
        (
            "I always tell him it's dangerous\x01",
            "and not to go in the mine, but\x01",
            "when it comes to that kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wish he'd listen to\x01",
            "what I say more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BA")

    Jump("loc_14CD")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_136B")

    ChrTalk(
        0xA,
        (
            "That Hoffman. Even though he\x01",
            "was going to the mine, he\x01",
            "forgot to bring his lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's probably hungry\x01",
            "around now, so I'll have\x01",
            "to bring it to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CD")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144E")

    ChrTalk(
        0xA,
        (
            "My child troubles me\x01",
            "because he wants to go\x01",
            "into dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For example, this\x01",
            "morning, Gantz stopped\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At this rate, he'll get\x01",
            "himself seriously hurt\x01",
            "before long. Goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14CD")

    label("loc_144E")


    ChrTalk(
        0xA,
        (
            "My child is full of\x01",
            "curiosity. He always wants\x01",
            "to enter dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He takes after his\x01",
            "father. I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CD")

    TalkEnd(0xFE)
    Return()

    # Function_5_668 end

    def Function_6_14D1(): pass

    label("Function_6_14D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14E2")
    Jump("loc_15AF")

    label("loc_14E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(
        0xE,
        (
            "Aww. With the rain, I\x01",
            "can't play outside. How\x01",
            "boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wish dad would get\x01",
            "home soon so we can\x01",
            "play~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AF")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_156E")
    Jump("loc_15AF")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_157C")
    Jump("loc_15AF")

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_158A")
    Jump("loc_15AF")

    label("loc_158A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1598")
    Jump("loc_15AF")

    label("loc_1598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15A6")
    Jump("loc_15AF")

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_15AF")

    label("loc_15AF")

    TalkEnd(0xFE)
    Return()

    # Function_6_14D1 end

    def Function_7_15B3(): pass

    label("Function_7_15B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15C4")
    Jump("loc_18DD")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_16D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1683")

    ChrTalk(
        0x11,
        (
            "It looks like there's been a\x01",
            "big development in Crossbell\x01",
            "City for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...We miners can't stay\x01",
            "like this. I think I'll\x01",
            "consult with the mayor...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_16CF")

    label("loc_1683")


    ChrTalk(
        0x11,
        (
            "We miners can't stay like\x01",
            "this. I think I'll\x01",
            "consult with the mayor...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CF")

    Jump("loc_18DD")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_18DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")

    ChrTalk(
        0x11,
        (
            "If independence goes through, they'll\x01",
            "be a steep drop in septium trade, so\x01",
            "we've closed the mine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If trade with other\x01",
            "countries stops, we'll\x01",
            "just have to accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Honestly, I wish they wouldn't\x01",
            "close it down, but... Right now,\x01",
            "all we can do it wait and see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_18DD")

    label("loc_180A")


    ChrTalk(
        0x11,
        (
            "If independence goes through, they'll\x01",
            "be a steep drop in septium trade, so\x01",
            "we've closed the mine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Honestly, I wish they wouldn't\x01",
            "close it down, but... Right now,\x01",
            "all we can do it wait and see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DD")

    TalkEnd(0xFE)
    Return()

    # Function_7_15B3 end

    def Function_8_18E1(): pass

    label("Function_8_18E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(
        0xB,
        (
            "I'm so relieved Logy\x01",
            "returned to the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know what's\x01",
            "going to happen to\x01",
            "Crossbell now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As long as our young ones keep their\x01",
            "feet on steady ground, I'm sure a\x01",
            "path to the future will open.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A75")

    label("loc_19DB")


    ChrTalk(
        0xB,
        (
            "I'm so relieved Logy\x01",
            "returned to the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As long as our young ones keep their\x01",
            "feet on steady ground, I'm sure a\x01",
            "path to the future will open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A75")

    Jump("loc_2826")

    label("loc_1A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B16")

    ChrTalk(
        0xB,
        (
            "The independence invalidity\x01",
            "declaration crushed the\x01",
            "President's legitimacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We may stand at the\x01",
            "crossroads of history.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B46")

    label("loc_1B16")


    ChrTalk(
        0xB,
        (
            "We may stand at the\x01",
            "crossroads of history.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B46")

    Jump("loc_2826")

    label("loc_1B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C36")

    ChrTalk(
        0xB,
        (
            "I didn't expect Crossbell's\x01",
            "independence to lead to a\x01",
            "situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With the mine funds\x01",
            "frozen, it seems Logy has\x01",
            "lost his will to live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, what should I do\x01",
            "about this, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C9B")

    label("loc_1C36")


    ChrTalk(
        0xB,
        (
            "And just when Logy was\x01",
            "so motivated, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, what should I do\x01",
            "about this, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9B")

    Jump("loc_2826")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D32")

    ChrTalk(
        0xB,
        (
            "To think a Mainz\x01",
            "occupation occurred again,\x01",
            "just like with the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, what has happened to\x01",
            "our Crossbell, I\x01",
            "wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2826")

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2B")

    ChrTalk(
        0xB,
        (
            "There's been more people\x01",
            "leaving for the city\x01",
            "recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, Logy and the other\x01",
            "young ones feel pride\x01",
            "toward this town of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've lived in this town\x01",
            "for a long time. Nothing\x01",
            "could make me happier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ECA")

    label("loc_1E2B")


    ChrTalk(
        0xB,
        (
            "However, Logy and the other\x01",
            "young ones feel pride\x01",
            "toward this town of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've lived in this town\x01",
            "for a long time. Nothing\x01",
            "could make me happier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECA")

    Jump("loc_2826")

    label("loc_1ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB2")

    ChrTalk(
        0xB,
        (
            "It seems Logy is doing\x01",
            "proper work, and living\x01",
            "out his days fully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. All that's left is\x01",
            "for him to bring a wife\x01",
            "home, and I can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I suppose that's\x01",
            "far in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_201D")

    label("loc_1FB2")


    ChrTalk(
        0xB,
        (
            "If Logy brings a wife\x01",
            "home, I'll be able to\x01",
            "rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I suppose that's\x01",
            "far in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201D")

    Jump("loc_2826")

    label("loc_2022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_222A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217D")

    ChrTalk(
        0xB,
        (
            "Crossbell State\x01",
            "independence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As long as I've lived here, it's always\x01",
            "had no sense of reality to it. If it were\x01",
            "to actually happen, that would be lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's just, the Empire and\x01",
            "Republic won't ever see\x01",
            "this as something good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Independence would make\x01",
            "good coals for the flame\x01",
            "of a new conflict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2225")

    label("loc_217D")


    ChrTalk(
        0xB,
        (
            "I can't think the Empire and\x01",
            "Republic will remain silent over\x01",
            "this independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Independence would make\x01",
            "good coals for the flame\x01",
            "of a new conflict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2225")

    Jump("loc_2826")

    label("loc_222A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_243F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2374")

    ChrTalk(
        0xB,
        (
            "A long time ago, cave-in\x01",
            "accidents and landslides occurred\x01",
            "often in these high mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But ever since the orbal revolution\x01",
            "and the creation of excavation\x01",
            "technology, they rarely occur anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Technological progress is truly\x01",
            "the savior of humanity. This is\x01",
            "a good age to be living in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_243A")

    label("loc_2374")


    ChrTalk(
        0xB,
        (
            "A long time ago, cave-in accidents\x01",
            "and landslides occurred often...\x01",
            "But they hardly do anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Technological progress is truly\x01",
            "the savior of humanity. This is\x01",
            "a good age to be living in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243A")

    Jump("loc_2826")

    label("loc_243F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_250B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AF")

    ChrTalk(
        0xB,
        (
            "Ami and Logy must be\x01",
            "very worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. Most importantly,\x01",
            "they get along.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2506")

    label("loc_24AF")


    ChrTalk(
        0xB,
        "Nevertheless...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wish they wouldn't\x01",
            "play so much, and help\x01",
            "with the chores.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2506")

    Jump("loc_2826")

    label("loc_250B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BF")

    ChrTalk(
        0xB,
        (
            "Lately, my grandson Logy\x01",
            "has started working hard\x01",
            "without skipping out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, nothing could make\x01",
            "me happier. ...Goddess\x01",
            "of the Sky, I thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_266F")

    label("loc_25BF")


    ChrTalk(
        0xB,
        (
            "Nothing could make me happier\x01",
            "than seeing my grandson become\x01",
            "a responsible young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Goddess of the Sky, I\x01",
            "thank you. Please, watch over\x01",
            "my children forevermore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266F")

    Jump("loc_2826")

    label("loc_2674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A7")

    ChrTalk(
        0xB,
        (
            "The old mine is right outside of\x01",
            "town. It was our principal one\x01",
            "until some ten-odd years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In its heyday, it was a\x01",
            "mountain of treasure,\x01",
            "full of large crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's actually one of the reasons\x01",
            "the Empire and Republic have been\x01",
            "fighting so long over this place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2826")

    label("loc_27A7")


    ChrTalk(
        0xB,
        (
            "The old mine was mined\x01",
            "out and abandoned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But long ago, it's certain\x01",
            "to have been an important\x01",
            "place in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2826")

    TalkEnd(0xFE)
    Return()

    # Function_8_18E1 end

    def Function_9_282A(): pass

    label("Function_9_282A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_283B")
    Jump("loc_2A07")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_294B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290A")

    ChrTalk(
        0xD,
        (
            "Huh, you're walking in\x01",
            "the rain without an\x01",
            "umbrella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm~, I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...So this is what they mean\x01",
            "when they say "a man is handsome\x01",
            "even when drenched", right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2946")

    label("loc_290A")


    ChrTalk(
        0xD,
        (
            "You guys must be what\x01",
            "they call "handsome\x01",
            "men", right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2946")

    Jump("loc_2A07")

    label("loc_294B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2959")
    Jump("loc_2A07")

    label("loc_2959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2967")
    Jump("loc_2A07")

    label("loc_2967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2975")
    Jump("loc_2A07")

    label("loc_2975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_29F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2990")
    Call(0, 10)
    Jump("loc_29EB")

    label("loc_2990")


    ChrTalk(
        0xD,
        (
            "My brother's not a\x01",
            "romantic. How boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I guess I'm like\x01",
            "him too, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EB")

    Jump("loc_2A07")

    label("loc_29F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29FE")
    Jump("loc_2A07")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2A07")

    label("loc_2A07")

    TalkEnd(0xFE)
    Return()

    # Function_9_282A end

    def Function_10_2A0B(): pass

    label("Function_10_2A0B")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xD,
        (
            "Hey Logy. Got any pick-\x01",
            "up lines?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't. Women are\x01",
            "annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Aww, how boring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ah, in that case, how about Gantz? I\x01",
            "hear there are lots of pretty,\x01",
            "smiling bunny girls at the casino...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Heck if I know!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_10_2A0B end

    def Function_11_2B0B(): pass

    label("Function_11_2B0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B1C")
    Jump("loc_2BF6")

    label("loc_2B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B2A")
    Jump("loc_2BF6")

    label("loc_2B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B38")
    Jump("loc_2BF6")

    label("loc_2B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B46")
    Jump("loc_2BF6")

    label("loc_2B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B54")
    Jump("loc_2BF6")

    label("loc_2B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6F")
    Call(0, 10)
    Jump("loc_2BDA")

    label("loc_2B6F")


    ChrTalk(
        0x10,
        (
            "Man, talking with Ami is\x01",
            "really annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "And it's my day off too.\x01",
            "I wish she'd let me\x01",
            "enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDA")

    Jump("loc_2BF6")

    label("loc_2BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BED")
    Jump("loc_2BF6")

    label("loc_2BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2BF6")

    label("loc_2BF6")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B0B end

    def Function_12_2BFA(): pass

    label("Function_12_2BFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB4")

    ChrTalk(
        0xC,
        (
            "I'm relieved Max is well\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The sight of the miners\x01",
            "working hard is the\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a woman of Mainz, I\x01",
            "have to support them as\x01",
            "best I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D39")

    label("loc_2CB4")


    ChrTalk(
        0xC,
        (
            "The sight of Max and the\x01",
            "other miners working\x01",
            "hard is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a woman of Mainz, I\x01",
            "have to support them as\x01",
            "best I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D39")

    Jump("loc_390A")

    label("loc_2D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")

    ChrTalk(
        0xC,
        (
            "It looks like the\x01",
            "resistance is preparing\x01",
            "for something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...If the CGF get injured like\x01",
            "in that occupation incident, I\x01",
            "don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I really hope they don't\x01",
            "get themselves hurt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBD")

    label("loc_2E2A")


    ChrTalk(
        0xC,
        (
            "...If the CGF get injured like\x01",
            "in that occupation incident, I\x01",
            "don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I really hope they don't\x01",
            "get themselves hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBD")

    Jump("loc_390A")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2F7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDD")
    Call(0, 13)
    Jump("loc_2F77")

    label("loc_2EDD")


    ChrTalk(
        0xC,
        (
            "The fact that Max can't\x01",
            "do the work that he\x01",
            "loves hurts me too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to do everything I\x01",
            "can to cheer him up. He'll\x01",
            "get sick at this rate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F77")

    Jump("loc_390A")

    label("loc_2F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3012")

    ChrTalk(
        0xC,
        (
            "A number of CGF soldiers\x01",
            "sacrificed themselves\x01",
            "for our sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For the people waiting\x01",
            "for them... I have no\x01",
            "words.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_306C")

    label("loc_3012")


    ChrTalk(
        0xC,
        (
            "The CGF must have people\x01",
            "waiting for them as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...I have no words for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    Jump("loc_390A")

    label("loc_3071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3178")

    ChrTalk(
        0xC,
        (
            "Everyone, you have to be\x01",
            "careful in Mainz on\x01",
            "rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you lose your footing, you'll\x01",
            "tumble down the cliff... It's\x01",
            "not all that unlikely, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Both Max and I have\x01",
            "watched out for that ever\x01",
            "since we were little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31FF")

    label("loc_3178")


    ChrTalk(
        0xC,
        (
            "Everyone, you have to be\x01",
            "careful in Mainz on\x01",
            "rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Both Max and I have\x01",
            "watched out for that ever\x01",
            "since we were little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FF")

    Jump("loc_390A")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3306")

    ChrTalk(
        0xC,
        (
            "Strangely, my husband\x01",
            "has been enjoying his\x01",
            "work lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because Gantz and Logy\x01",
            "are so motivated, I think\x01",
            "it's rubbed off on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He leaves early every morning,\x01",
            "and it's pretty difficult\x01",
            "getting lunch ready for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33AF")

    label("loc_3306")


    ChrTalk(
        0xC,
        (
            "Because Gantz and Logy\x01",
            "are so motivated, I think\x01",
            "it's rubbed off on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He leaves early every morning,\x01",
            "and it's pretty difficult\x01",
            "getting lunch ready for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AF")

    Jump("loc_390A")

    label("loc_33B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349E")

    ChrTalk(
        0xC,
        (
            "I'm told a large monster\x01",
            "has appeared in the\x01",
            "north mountain district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's not that far from\x01",
            "town. I worry one will\x01",
            "appear in the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The miners aren't\x01",
            "equipped to deal with\x01",
            "large monsters.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_353B")

    label("loc_349E")


    ChrTalk(
        0xC,
        (
            "A large monster appeared\x01",
            "in the north mountain\x01",
            "district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I worry one might appear in the\x01",
            "mine. Miners aren't equipped to\x01",
            "deal with large monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353B")

    Jump("loc_390A")

    label("loc_3540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35CE")

    ChrTalk(
        0xC,
        (
            "It seems the trade\x01",
            "conference has opened in\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Will discussions at the\x01",
            "conference affect\x01",
            "Mainz's future?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_390A")

    label("loc_35CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3664")

    ChrTalk(
        0xC,
        (
            "Max went to drink with\x01",
            "the mine chief today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He works twice as hard as the\x01",
            "others. He needs a change of\x01",
            "pace on his days off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_390A")

    label("loc_3664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3760")

    ChrTalk(
        0xC,
        (
            "Monsters have appeared\x01",
            "in the mine, attracted\x01",
            "to the buried septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Normally, it would be\x01",
            "dangerous, but the miners of\x01",
            "Mainz are all strong men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it's just simple\x01",
            "monsters, we can deal\x01",
            "with them on our own.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D4")

    label("loc_3760")


    ChrTalk(
        0xC,
        (
            "The miners of Mainz are\x01",
            "all strong men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If monsters appear in\x01",
            "the mine, we can deal\x01",
            "with them on our own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D4")

    Jump("loc_390A")

    label("loc_37D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_390A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3892")

    ChrTalk(
        0xC,
        (
            "My husband works as a\x01",
            "miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He's the breadwinner\x01",
            "even though he's so\x01",
            "young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now then, I've got to\x01",
            "get a lot of dinner\x01",
            "ready and wait for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_390A")

    label("loc_3892")


    ChrTalk(
        0xC,
        (
            "My husband will probably\x01",
            "be hungry when he gets\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to get a lot of\x01",
            "dinner ready and wait\x01",
            "for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390A")

    TalkEnd(0xFE)
    Return()

    # Function_12_2BFA end

    def Function_13_390E(): pass

    label("Function_13_390E")

    OP_4B(0xC, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "*sigh*... Digging holes is the\x01",
            "only thing I'm good for. To\x01",
            "think I can't work as a miner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Max, quit feeling sorry\x01",
            "for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You'll be able to enter\x01",
            "the mine soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I hope you're\x01",
            "right...... *sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Honestly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_390E end

    def Function_14_3A1F(): pass

    label("Function_14_3A1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_3B2D")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(
        0x12,
        (
            "I can't work in the mine,\x01",
            "so I'm helping out with\x01",
            "manual labor in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But, really, not being\x01",
            "able to enter the mine...\x01",
            "I feel kinda bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_3AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEE")
    Call(0, 13)
    Jump("loc_3B2D")

    label("loc_3AEE")


    ChrTalk(
        0x12,
        (
            "*sigh*... Digging holes\x01",
            "is the only thing I'm\x01",
            "good for...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2D")

    TalkEnd(0xFE)
    Return()

    # Function_14_3A1F end

    def Function_15_3B31(): pass

    label("Function_15_3B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B48")
    Call(0, 24)
    Return()

    label("loc_3B48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B67")
    Call(0, 16)
    Return()

    label("loc_3B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C80")

    ChrTalk(
        0x8,
        (
            "It seems the resistance\x01",
            "were able to safely join\x01",
            "with the state guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that the president has been\x01",
            "arrested, they no longer have a\x01",
            "reason to continue hostilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So Mireille and the\x01",
            "others' resistance was a\x01",
            "success. ...What a relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CE9")

    label("loc_3C80")


    ChrTalk(
        0x8,
        (
            "The mine has reopened,\x01",
            "and we're getting our\x01",
            "energy back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the real battle\x01",
            "begins now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE9")

    Jump("loc_4D05")

    label("loc_3CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E13")

    ChrTalk(
        0x8,
        (
            "With the President's legitimacy\x01",
            "shaken, the State Guard have\x01",
            "adopted a wait-and-see stance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems Mireille and the\x01",
            "others are preparing for the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I pray to the Goddess\x01",
            "that the resistance's\x01",
            "mission will be a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EBC")

    label("loc_3E13")


    ChrTalk(
        0x8,
        (
            "It seems Mireille and the\x01",
            "others are preparing for the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I pray to the Goddess\x01",
            "that the resistance's\x01",
            "mission will be a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBC")

    Jump("loc_4D05")

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3F93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDC")
    Call(0, 17)
    Jump("loc_3F8E")

    label("loc_3EDC")


    ChrTalk(
        0x8,
        (
            "Originally, I didn't suspect\x01",
            "the President of quietly\x01",
            "using jaegers at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The resistance are trying to\x01",
            "do something about the current\x01",
            "order. They're our only hope.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8E")

    Jump("loc_4D05")

    label("loc_3F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4158")

    ChrTalk(
        0x8,
        "It's all of you, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMayor Bickson... Things\x01",
            "must be tough in Mainz,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah... Severe injuries\x01",
            "are few, but everyone's\x01",
            "in shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The bracers are working\x01",
            "to heal them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe shock of this\x01",
            "incident must be\x01",
            "considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah... It seems things\x01",
            "have calmed down a bit,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as mayor, I plan\x01",
            "to do all that I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys must have it\x01",
            "tough too. Do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 2)
    Jump("loc_41C0")

    label("loc_4158")


    ChrTalk(
        0x8,
        (
            "Anyway, as mayor, I plan\x01",
            "to do all that I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys must have it\x01",
            "tough too. Do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41C0")

    Jump("loc_4D05")

    label("loc_41C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_439D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4313")

    ChrTalk(
        0x8,
        (
            "Recently, I've been\x01",
            "hearing reports of\x01",
            "large, unknown monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A large monster was\x01",
            "sighted in yesterday's\x01",
            "train accident as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could these have something to do\x01",
            "with the large monster that\x01",
            "appeared in the old mine before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Anyhow, it seems best\x01",
            "to look out for\x01",
            "everyone's safety.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4398")

    label("loc_4313")


    ChrTalk(
        0x8,
        (
            "I've been hearing reports\x01",
            "of large, unknown\x01",
            "monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Anyhow, it seems best\x01",
            "to look out for\x01",
            "everyone's safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4398")

    Jump("loc_4D05")

    label("loc_439D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44EB")

    ChrTalk(
        0x8,
        (
            "Recently, it seems the\x01",
            "bracers are busier than\x01",
            "usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's gotten much harder\x01",
            "to submit requests that\x01",
            "aren't urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems you're investigating\x01",
            "the large, unknown monsters\x01",
            "that appeared recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. I have a bad feeling about\x01",
            "this. I wonder if something's\x01",
            "happening in Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_457E")

    label("loc_44EB")


    ChrTalk(
        0x8,
        (
            "It seems the bracers\x01",
            "here are busier than\x01",
            "usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. I have a bad feeling about\x01",
            "this. I wonder if something's\x01",
            "happening in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_457E")

    Jump("loc_4D05")

    label("loc_4583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_475E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C6")

    ChrTalk(
        0x8,
        (
            "Crossbell state independence...\x01",
            "I can't believe the day has\x01",
            "come to propose such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Empire and Republic have a history of\x01",
            "fighting over our mined resources. We'll\x01",
            "have to consider the question seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Each of the people of\x01",
            "Mainz must consider the\x01",
            "question separately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4759")

    label("loc_46C6")


    ChrTalk(
        0x8,
        (
            "The people of Mainz must\x01",
            "consider the question of\x01",
            "independence individually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As one of them, I'll\x01",
            "consider it myself until\x01",
            "election day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4759")

    Jump("loc_4D05")

    label("loc_475E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483A")

    ChrTalk(
        0x8,
        (
            "Gantz is rather\x01",
            "generous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After a rare win at the\x01",
            "casino, he used it immediately\x01",
            "to buy us all drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rather, I feel he's throwing\x01",
            "away more mira than when he\x01",
            "comes back broke.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48EB")

    label("loc_483A")


    ChrTalk(
        0x8,
        (
            "I feel like Gantz is throwing away\x01",
            "more mira when he comes back after\x01",
            "winning than when he comes back broke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you could say\x01",
            "that's the sort of thing\x01",
            "he would do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48EB")

    Jump("loc_4D05")

    label("loc_48F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1B")

    ChrTalk(
        0x8,
        (
            "Orchis Tower, a\x01",
            "skyscraper, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would like to welcome\x01",
            "technological advances,\x01",
            "but I have mixed feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder when I'll feel\x01",
            "like leaving this town\x01",
            "of Mainz behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Haha, please don't worry\x01",
            "about it. I'm just an old\x01",
            "man talking to himself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AC4")

    label("loc_4A1B")


    ChrTalk(
        0x8,
        (
            "Anyhow, I think the\x01",
            "trade conference will\x01",
            "have great meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the future of our state, I\x01",
            "want Mayor Dieter and Chairman\x01",
            "MacDowell to do their best for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC4")

    Jump("loc_4D05")

    label("loc_4AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE1")
    Jump("loc_4B79")

    label("loc_4AE1")


    ChrTalk(
        0x8,
        (
            "I'll let you guys keep\x01",
            "the duplicate key to the\x01",
            "old mine, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'd be helpful if you\x01",
            "could look in there every\x01",
            "now and then for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B79")

    Jump("loc_4D05")

    label("loc_4B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C69")

    ChrTalk(
        0x8,
        (
            "To get to the Old Mine, leave\x01",
            "town, go down the mountain a\x01",
            "bit, then climb northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't know why the gate was\x01",
            "destroyed or if anything's\x01",
            "happening in the tunnels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please, do be careful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D05")

    label("loc_4C69")


    ChrTalk(
        0x8,
        (
            "To get to the Old Mine, leave\x01",
            "town, go down the mountain a\x01",
            "bit, then climb northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Gantz will open the\x01",
            "entrance for you, so\x01",
            "please head there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D05")

    TalkEnd(0xFE)
    Return()

    # Function_15_3B31 end

    def Function_16_4D09(): pass

    label("Function_16_4D09")


    ChrTalk(
        0x8,
        (
            "We replaced the broken old\x01",
            "mine gate with a sturdy\x01",
            "new one the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right. Just in\x01",
            "case, will you take\x01",
            "this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00105FUmm, are you sure? We're\x01",
            "outsiders, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I can trust you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's anything you\x01",
            "need to investigate,\x01",
            "please feel free to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just in case, we rebuilt\x01",
            "the ladder so it'll be\x01",
            "easier to come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you very much.\x01",
            "We'll hang on to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 3)
    TalkEnd(0x8)
    Return()

    # Function_16_4D09 end

    def Function_17_4F04(): pass

    label("Function_17_4F04")

    OP_4B(0x8, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hmm. Then leave your\x01",
            "food supply to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And you need oil for\x01",
            "equipment maintenance,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Backerei's store should\x01",
            "have some of that. I'll\x01",
            "check there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07902FThanks. We're counting\x01",
            "on you.\x02\x03",
            "#07908F...We're really grateful\x01",
            "to the people of Mainz.\x02\x03",
            "#07903FIf you exposed us to the\x01",
            "State Guard, we'd be in\x01",
            "dire straits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, what are you\x01",
            "saying? ...Please don't\x01",
            "worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Originally, I didn't suspect\x01",
            "the President of quietly\x01",
            "using jaegers at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the middle of that... The\x01",
            "appearance of a resistance force\x01",
            "is nothing other than hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, I'll do\x01",
            "everything I can to\x01",
            "support your operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07904F...Thank you very much.\x01",
            "We'll never forget your\x01",
            "kindness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_17_4F04 end

    def Function_18_51F9(): pass

    label("Function_18_51F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5316")

    ChrTalk(
        0x9,
        (
            "Mireille and the other CGF did\x01",
            "their best for us with their\x01",
            "extended resistance activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They thanked us many times\x01",
            "when leaving town... But I\x01",
            "want to thank them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once everything is\x01",
            "settled, I want to invite\x01",
            "them all back to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53C1")

    label("loc_5316")


    ChrTalk(
        0x9,
        (
            "Mireille and the other CGF did\x01",
            "their best for us with their\x01",
            "extended resistance activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once everything is\x01",
            "settled, I want to invite\x01",
            "them all back to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C1")

    Jump("loc_6300")

    label("loc_53C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548B")

    ChrTalk(
        0x9,
        (
            "It seems Mireille and\x01",
            "the others are resting\x01",
            "at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They said they'd be busy\x01",
            "again before long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're taking this\x01",
            "opportunity to get\x01",
            "proper rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5502")

    label("loc_548B")


    ChrTalk(
        0x9,
        (
            "It seems Mireille and\x01",
            "the others are resting\x01",
            "at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're taking this\x01",
            "opportunity to get\x01",
            "proper rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5502")

    Jump("loc_6300")

    label("loc_5507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_567D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5626")

    ChrTalk(
        0x9,
        (
            "It seems Mireille and the\x01",
            "others set up camp within\x01",
            "the mountain district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter how used to being\x01",
            "outdoors you are, it must be hard\x01",
            "to keep it up for this long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It would be nice if the\x01",
            "State Guard and jaegers'\x01",
            "searches let up a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5678")

    label("loc_5626")


    ChrTalk(
        0x9,
        (
            "It would be nice if the\x01",
            "State Guard and jaegers'\x01",
            "searches let up a little...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5678")

    Jump("loc_6300")

    label("loc_567D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_57BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5736")

    ChrTalk(
        0x9,
        (
            "Eolia gave me some of\x01",
            "her calming herb tea the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thanks to that, I've\x01",
            "felt settled for the\x01",
            "past week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to thank Eolia\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_57B8")

    label("loc_5736")


    ChrTalk(
        0x9,
        (
            "Eolia left for the old\x01",
            "mine today to exterminate\x01",
            "some monsters for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to thank those\x01",
            "ladies for all their\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B8")

    Jump("loc_6300")

    label("loc_57BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5888")

    ChrTalk(
        0x9,
        (
            "The mountain weather\x01",
            "collapses easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This rain is so bad,\x01",
            "they even had to\x01",
            "discontinue bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should take care\x01",
            "coming and going in\x01",
            "today's downpour.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_590C")

    label("loc_5888")


    ChrTalk(
        0x9,
        (
            "This rain is so bad,\x01",
            "they even had to\x01",
            "discontinue bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should take care\x01",
            "coming and going in\x01",
            "today's downpour.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590C")

    Jump("loc_6300")

    label("loc_5911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59ED")

    ChrTalk(
        0x9,
        (
            "I've got to find some\x01",
            "good partners for the\x01",
            "miners...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "None of them, neither\x01",
            "Gantz, Marlowe nor Logy,\x01",
            "seem eager to find someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess young kids don't\x01",
            "long to get married...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A73")

    label("loc_59ED")


    ChrTalk(
        0x9,
        (
            "None of them, neither\x01",
            "Gantz, Marlowe nor Logy,\x01",
            "seem eager to find someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess young kids don't\x01",
            "long to get married...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A73")

    Jump("loc_6300")

    label("loc_5A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9A")

    ChrTalk(
        0x9,
        (
            "Both the Empire and Republic\x01",
            "have decided to each assess\x01",
            "a 10% tax on Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For a developing economy\x01",
            "like Crossbell, 10% is a\x01",
            "staggering amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can be seen a decision symbolic\x01",
            "of Crossbell's subordinate\x01",
            "relationship with the major powers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5C57")

    label("loc_5B9A")


    ChrTalk(
        0x9,
        (
            "Both the Empire and Republic\x01",
            "have decided to each assess\x01",
            "a 10% tax on Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can be seen a decision symbolic\x01",
            "of Crossbell's subordinate\x01",
            "relationship with the major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C57")

    Jump("loc_6300")

    label("loc_5C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DEC")

    ChrTalk(
        0x9,
        "My, you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps you'd like a\x01",
            "marriage interview with one\x01",
            "of our village's miners?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F...You're talking about\x01",
            "me, aren't you.\x02\x03",
            "I'm not at the right age\x01",
            "to be married yet,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, you're very\x01",
            "beautiful, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When you're older,\x01",
            "please return if you\x01",
            "can't find anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F(...That's a bit rude.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Y-Yeah...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E70")

    label("loc_5DEC")


    ChrTalk(
        0x9,
        (
            "When you're older, if you\x01",
            "find yourself without a\x01",
            "partner, please return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll give a cute girl\x01",
            "like you a warm welcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E70")

    Jump("loc_6300")

    label("loc_5E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F10")

    ChrTalk(
        0x9,
        (
            "The miners are taking\x01",
            "the day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think you'll be all right, but\x01",
            "if you're planning on entering,\x01",
            "please watch out for monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6300")

    label("loc_5F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6105")

    ChrTalk(
        0x9,
        "That's right, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps you'd like a\x01",
            "marriage interview with one\x01",
            "of our village's miners?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FA-A marriage interview?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. If Gantz and the others\x01",
            "had someone to come home to,\x01",
            "I think they'd work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What do you say, young\x01",
            "lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FU-Umm... I'm sorry. I'm\x01",
            "not thinking of marrying\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FMe as well. Right now,\x01",
            "work takes priority...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I see... Too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, if you change your\x01",
            "mind, please consider\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_617C")

    label("loc_6105")


    ChrTalk(
        0x9,
        (
            "If you change your opinion\x01",
            "on the marriage interview,\x01",
            "please consider it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll get everything\x01",
            "ready for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617C")

    Jump("loc_6300")

    label("loc_6181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_6300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6271")

    ChrTalk(
        0x9,
        (
            "That Old Mine was still\x01",
            "in use a few decades\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It became dangerous to go inside,\x01",
            "so I heard our predecessor\x01",
            "secured the entrance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who would break\x01",
            "the lock. It's rather\x01",
            "strange...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6300")

    label("loc_6271")


    ChrTalk(
        0x9,
        (
            "It's dangerous to go\x01",
            "inside the old mine, so we\x01",
            "sealed it securely, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who would break\x01",
            "the lock. It's rather\x01",
            "strange...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6300")

    TalkEnd(0xFE)
    Return()

    # Function_18_51F9 end

    def Function_19_6304(): pass

    label("Function_19_6304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_631B")
    Call(0, 24)
    Return()

    label("loc_631B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_632C")
    Jump("loc_641D")

    label("loc_632C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_633A")
    Jump("loc_641D")

    label("loc_633A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6348")
    Jump("loc_641D")

    label("loc_6348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6356")
    Jump("loc_641D")

    label("loc_6356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6364")
    Jump("loc_641D")

    label("loc_6364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6372")
    Jump("loc_641D")

    label("loc_6372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638A")
    Jump("loc_640F")

    label("loc_638A")


    ChrTalk(
        0xF,
        (
            "Buying up such a large quantity\x01",
            "of septium... There aren't many\x01",
            "traders who can do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...I really wonder who\x01",
            "they were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640F")

    Jump("loc_641D")

    label("loc_6414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_641D")

    label("loc_641D")

    TalkEnd(0xFE)
    Return()

    # Function_19_6304 end

    def Function_20_6421(): pass

    label("Function_20_6421")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6432")
    Jump("loc_6692")

    label("loc_6432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6440")
    Jump("loc_6692")

    label("loc_6440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_645B")
    Call(0, 17)
    Jump("loc_6692")

    label("loc_645B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F6")

    ChrTalk(
        0x13,
        (
            "#07903FThe tough situation hasn't changed.\x01",
            "We plan to do our best for a while\x01",
            "in the mountain district.\x02\x03",
            "#07901FRandy, and the support section...\x01",
            "Please leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FSure, understood.\x02\x03",
            "#00301F...Don't lose to the\x01",
            "jaegers or State Guard,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        (
            "#07902FHaha, look who's talking.\x02\x03",
            "#07904FThe people of Mainz are\x01",
            "cooperating with us, so I'm\x01",
            "sure we'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6692")

    label("loc_65F6")


    ChrTalk(
        0x13,
        (
            "#07900FRandy, and the support\x01",
            "section... Please leave\x01",
            "this to us.\x02\x03",
            "#07904FThe people of Mainz are\x01",
            "cooperating with us, so I'm\x01",
            "sure we'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6692")

    TalkEnd(0xFE)
    Return()

    # Function_20_6421 end

    def Function_21_6696(): pass

    label("Function_21_6696")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C3")

    ChrTalk(
        0x14,
        (
            "Because we've gained the help\x01",
            "of the divine wolves, it'll\x01",
            "be easier for us to act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "They're keeping watch over the\x01",
            "mountain path and district... Just\x01",
            "that lightens our burden considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Lt. Mireille wants to\x01",
            "take this chance to rest\x01",
            "as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6872")

    label("loc_67C3")


    ChrTalk(
        0x14,
        (
            "Keeping watch over the mountain\x01",
            "path and district... Just that\x01",
            "lightens our burden considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Lt. Mireille wants to\x01",
            "take this chance to rest\x01",
            "as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6872")

    TalkEnd(0xFE)
    Return()

    # Function_21_6696 end

    def Function_22_6876(): pass

    label("Function_22_6876")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68C0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1555), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6896")
    Sleep(1500)
    Jump("loc_68AB")

    label("loc_6896")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)

    label("loc_68AB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68BB")
    Sleep(333)

    label("loc_68BB")

    Jump("Function_22_6876")

    label("loc_68C0")

    Return()

    # Function_22_6876 end

    def Function_23_68C1(): pass

    label("Function_23_68C1")

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
            "#2PExcuse us. We're the\x01",
            "Crossbell Police,\x01",
            "Special Support Section.\x02",
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

    def lambda_6AE5():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6AE5)
    Sleep(50)

    def lambda_6AF5():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6AF5)
    Sleep(50)

    def lambda_6B05():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6B05)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xF, 0)
    Sleep(500)

    def lambda_6B24():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B24)

    def lambda_6B3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B3E)
    Sleep(100)

    def lambda_6B52():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B52)

    def lambda_6B6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B6C)
    Sleep(50)

    def lambda_6B80():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B80)

    def lambda_6B9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B9A)
    Sleep(80)

    def lambda_6BAE():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6BAE)

    def lambda_6BC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BC8)
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
            "#11POh, it's you guys. Sorry\x01",
            "to make you come all\x01",
            "this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#2PYo, long time no see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PHello everyone, it's\x01",
            "nice to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PGantz, how are you\x01",
            "feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2PYeah, there aren't any\x01",
            "aftereffects in particular.\x01",
            "I'm doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2PThanks again for all\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PEhe, we're just happy\x01",
            "you're doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PSo then, monsters showed\x01",
            "up at the Old Mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes. There's a mine near\x01",
            "town that's been\x01",
            "abandoned for decades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PPlease, make yourselves\x01",
            "at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'll get you all some\x01",
            "tea.\x02",
        )
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
            "#00005F─The sealed entrance\x01",
            "gate was destroyed?\x02",
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
            "#5PYes. Even though it's\x01",
            "many years old, it was a\x01",
            "very sturdy one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSome of our citizens\x01",
            "found it destroyed, you\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWe saw it intact just two\x01",
            "days ago, so it must have\x01",
            "been destroyed yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PSeriously, it must have been\x01",
            "something really strong to\x01",
            "be able to do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P...Interesting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PSo then, once you\x01",
            "checked inside you saw\x01",
            "monsters roaming around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PBut it's an old abandoned\x01",
            "mine, so it's not that strange\x01",
            "for monsters to appear, is it?\x02",
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
            "#5PWhat was strange was the\x01",
            "tunnel itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PThe tunnel itself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PHow to put it... It was\x01",
            "faintly glowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PIt was like the walls\x01",
            "themselves were glowing\x01",
            "with a purple-red light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12PThat is indeed strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12PSeeing as how the mine is\x01",
            "many years old, there\x01",
            "shouldn't be any orbal lamps.\x02\x03",
            "#00001FI wonder what the cause of\x01",
            "the glow might be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, there's no real\x01",
            "harm done. We're just\x01",
            "worried about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWe know how busy you are\x01",
            "but we decided to ask you\x01",
            "to help us deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PWe understand the\x01",
            "situation.\x02",
        )
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
            "#00001F#12PSeeing as the gate was\x01",
            "destroyed, I'd say we\x01",
            "have a case.\x02\x03",
            "How about we head there\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHehe... Sounds like an\x01",
            "interesting case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you. We'll leave\x01",
            "it in your hands.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(250)

    ChrTalk(
        0x8,
        (
            "#5PGantz, please show them\x01",
            "inside for me.\x02",
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
        "#5PYeah, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PSo then, I'll head over\x01",
            "there now. Once you're\x01",
            "ready, please find me there.\x02",
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

    def lambda_765F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_765F)
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
            "#00002F#12P...Thank goodness. He\x01",
            "really is doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, and it's all\x01",
            "thanks to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHis gambling habit's the\x01",
            "same as ever, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe still throws his mira\x01",
            "away at the casino on\x01",
            "his days off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PEhe. Is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, as long as he\x01",
            "doesn't overdo it, he\x01",
            "should be fine.\x02\x03",
            "#00005FOh right. The old mine\x01",
            "is just outside of town\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYes. Head down the\x01",
            "mountain a bit, then\x01",
            "head northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe don't know what\x01",
            "caused the incident.\x01",
            "Please be very careful.\x02",
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

    # Function_23_68C1 end

    def Function_24_79DF(): pass

    label("Function_24_79DF")

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
            "#5PHmm... Just what were\x01",
            "those guys up to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, maybe we shouldn't\x01",
            "overthink it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "They did help us out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, but we still don't know who\x01",
            "the criminal was. An abundance\x01",
            "of caution is necessary here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FUmm... Mr. Bickson,\x01",
            "Gantz. Hello.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7BBD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7BBD)
    Sleep(50)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        "#11POh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Sorry, we were just\x01",
            "talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAbout the old mine\x01",
            "incident, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh well, several CGF patrols\x01",
            "came through in relation to the\x01",
            "incident the other day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWe still have no idea. Regarding both\x01",
            "the criminal who set the explosives\x01",
            "and the phenomenon inside the tunnels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PFor now, we installed a new gate\x01",
            "to replace the broken one, and\x01",
            "sealed it right good and proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FThen I guess we won't have to\x01",
            "worry about people wandering\x01",
            "inside for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...It's just, there's\x01",
            "something else that has\x01",
            "me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou see, a strange group\x01",
            "appeared in Mainz the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThey bought some huge\x01",
            "septium crystals for a\x01",
            "huge sum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FA strange group?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHow should I put it...\x01",
            "Well anyway, they had a\x01",
            "unique air about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt seemed like a well-\x01",
            "built redheaded middle-\x01",
            "aged man was their leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PActually, it was exactly\x01",
            "like the hair of Randy\x01",
            "here, come to think of it.\x02",
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
        "#00105F(T-That's...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P(Red Constellation!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F...Did they do anything\x01",
            "besides that septium\x01",
            "purchase?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo, nothing suspicious.\x01",
            "But they didn't look\x01",
            "like traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWe don't know who destroyed\x01",
            "the old mine gate, so they\x01",
            "had me worried is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F(Based on what Randy said\x01",
            "earlier, it seems like they were\x01",
            "the ones who set the explosives.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F(Well, we have no\x01",
            "definitive proof, so we\x01",
            "shouldn't say anything.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(But, I wonder what that jaeger\x01",
            "corps is planning on doing with\x01",
            "those septium crystals.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301F(...Crimson & Co. that they run has\x01",
            "connections to a lot of good-for-\x01",
            "nothing traders.)\x02\x03",
            "#00303F(Those were large crystals. They're\x01",
            "probably earning some side money from\x01",
            "selling them on the black market.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F(I-I see...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#11PHmm, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PMaybe I should give it\x01",
            "to you guys.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)

    ChrTalk(
        0x8,
        "#5PHand it over, Gantz.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "Yeah, got it.\x02",
    )

    CloseMessageWindow()

    def lambda_8412():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_8412)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "Here, take it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#6PThis is for the old\x01",
            "mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah. A spare key, so to\x01",
            "speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm, are you sure? We're\x01",
            "outsiders, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I can trust you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's ever anything\x01",
            "you need to investigate,\x01",
            "please be our guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just in case, we rebuilt\x01",
            "the ladder so it'll be\x01",
            "easier to come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThanks. We'll use it\x01",
            "carefully.\x02",
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

    # Function_24_79DF end

    SaveToFile()

Try(main)
