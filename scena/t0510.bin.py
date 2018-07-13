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
        "Function_6_14FE",         # 06, 6
        "Function_7_15E4",         # 07, 7
        "Function_8_18F7",         # 08, 8
        "Function_9_28B6",         # 09, 9
        "Function_10_2AB3",        # 0A, 10
        "Function_11_2BDB",        # 0B, 11
        "Function_12_2CCB",        # 0C, 12
        "Function_13_3A15",        # 0D, 13
        "Function_14_3B27",        # 0E, 14
        "Function_15_3C3C",        # 0F, 15
        "Function_16_4EEC",        # 10, 16
        "Function_17_50E8",        # 11, 17
        "Function_18_540B",        # 12, 18
        "Function_19_6590",        # 13, 19
        "Function_20_66B3",        # 14, 20
        "Function_21_692C",        # 15, 21
        "Function_22_6B10",        # 16, 22
        "Function_23_6B5B",        # 17, 23
        "Function_24_7CB4",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_81D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76F")

    ChrTalk(
        0xA,
        (
            "I feel like it's still too early\x01",
            "to reopen the mine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If everyone in town \x01",
            "wants this, I suppose\x01",
            "there's no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because things turned like this, I'd like my husband\x01",
            "and the others to work their very hardest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_818")

    label("loc_76F")


    ChrTalk(
        0xA,
        (
            "Because things turned like this, I'd like my husband\x01",
            "and the others to work their very hardest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I too have to make a delicious\x01",
            "lunchbox to support my husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_818")

    Jump("loc_14FA")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8F8")

    ChrTalk(
        0xA,
        (
            "That Alec. He approached a wolf near\x01",
            "town without hesitation and petted him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank goodness they are smart animals\x01",
            "cooperating with the Resistance, but... \x01",
            "I wished he was a little more careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(
        0xA,
        (
            "Things are dangerous as it is so, in\x01",
            "a sense, I can relax a little because\x01",
            "my husband can't enter the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But at this rate,\x01",
            "Mainz will decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President has hardly touched up\x01",
            "anywhere outside the city. I wonder\x01",
            "what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ABA")

    label("loc_A18")


    ChrTalk(
        0xA,
        (
            "With the mine closed like\x01",
            "this, Mainz will decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President has hardly touched up\x01",
            "anywhere outside the city. I wonder\x01",
            "what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")

    Jump("loc_14FA")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B79")

    ChrTalk(
        0xA,
        (
            "My husband was injured the other day\x01",
            "during the Mainz occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's all right because\x01",
            "it wasn't a big deal, but...\x01",
            "I was really worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C1D")

    label("loc_B79")


    ChrTalk(
        0xA,
        (
            "My husband has already gone back to the mine...\x01",
            "But at that time I was really scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's nice to be brave, but I wish he\x01",
            "wouldn't push himself so hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1D")

    Jump("loc_14FA")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")

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
            "Even though the miners are lightly\x01",
            "dressed, they appear to be fine.\x02",
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
    Jump("loc_D61")

    label("loc_CE5")


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

    label("loc_D61")

    Jump("loc_14FA")

    label("loc_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DB8")

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
        "How annoying!\x01\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDA")

    ChrTalk(
        0xA,
        (
            "Due to the influence of my husband, the\x01",
            "mine captain, Alec wants to be a miner too.\x02",
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
            "keep him safe until\x01",
            "he's an adult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F89")

    label("loc_EDA")


    ChrTalk(
        0xA,
        (
            "Due to the influence of my husband, the\x01",
            "mine captain, Alec wants to be a miner too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, I'm against it...\x01",
            "But if he's serious about it,\x01",
            "I must watch over him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F89")

    Jump("loc_14FA")

    label("loc_F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1033")

    ChrTalk(
        0xA,
        (
            "Every day, I worry that Alec\x01",
            "will go somewhere dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On Sunday School days,\x01",
            "the Sister watches him\x01",
            "so I can relax a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B1")

    label("loc_1033")


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

    label("loc_10B1")

    Jump("loc_14FA")

    label("loc_10B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1230")

    ChrTalk(
        0xA,
        (
            "Yesterday, I went to deliver my husband's\x01",
            "lunchbox inside the mine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There, I found Alec,\x01",
            "who had wandered in.\x01",
            "I scolded him.\x02",
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
            "I have my hands full with my husband. I wish he\x01",
            "wouldn't worry me any more than he already does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BE")

    label("loc_1230")


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
            "I wish he'd listen\x01",
            "to what I say more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BE")

    Jump("loc_14FA")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_136F")

    ChrTalk(
        0xA,
        (
            "That Hoffman. Even though he was going to\x01",
            "the mine, he forgot to bring his lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's probably hungry around now,\x01",
            "so I'll have to bring it to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_14FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147B")

    ChrTalk(
        0xA,
        (
            "My child troubles me because he\x01",
            "wants to go into dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This morning too if Mr. Gantz hadn't stopped\x01",
            "him, I don't know what would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At this rate, he'll get himself\x01",
            "seriously hurt before long. Goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14FA")

    label("loc_147B")


    ChrTalk(
        0xA,
        (
            "My child is full of curiosity.\x01",
            "He always wants to enter dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "He takes after his father. I'm sure of it.\x02",
    )

    CloseMessageWindow()

    label("loc_14FA")

    TalkEnd(0xFE)
    Return()

    # Function_5_668 end

    def Function_6_14FE(): pass

    label("Function_6_14FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_150F")
    Jump("loc_15E0")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1591")

    ChrTalk(
        0xE,
        (
            "Aww. With the rain, I can't\x01",
            "play outside. How boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wish father would get home\x01",
            "soon so we can plaaay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E0")

    label("loc_1591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_159F")
    Jump("loc_15E0")

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15AD")
    Jump("loc_15E0")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15BB")
    Jump("loc_15E0")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_15E0")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15D7")
    Jump("loc_15E0")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_15E0")

    label("loc_15E0")

    TalkEnd(0xFE)
    Return()

    # Function_6_14FE end

    def Function_7_15E4(): pass

    label("Function_7_15E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_18F3")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_170C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B5")

    ChrTalk(
        0x11,
        (
            "It looks like there's been\x01",
            "some kind of big development \x01",
            "in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Us miners can't stay\x01",
            "like this. I think I'll\x01",
            "consult with the Town Mayor...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1707")

    label("loc_16B5")


    ChrTalk(
        0x11,
        (
            "Us miners can't stay like this. \x01",
            "I think I'll consult with the Town Mayor...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1707")

    Jump("loc_18F3")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_18F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1831")

    ChrTalk(
        0x11,
        (
            "If independence goes through, there'll\x01",
            "be a steep drop in Septium trade, so\x01",
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
            "Honestly, it's frustrating, but...\x01",
            "Right now, all we can do\x01",
            "is wait and see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_18F3")

    label("loc_1831")


    ChrTalk(
        0x11,
        (
            "If independence goes through, there'll\x01",
            "be a steep drop in Septium trade, so\x01",
            "we've closed the mine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Honestly, it's frustrating, but...\x01",
            "Right now, all we can do\x01",
            "is wait and see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F3")

    TalkEnd(0xFE)
    Return()

    # Function_7_15E4 end

    def Function_8_18F7(): pass

    label("Function_8_18F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F7")

    ChrTalk(
        0xB,
        (
            "I'm so relieved Logy\x01",
            "got back from the mine.\x02",
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
            "As long as the young ones keep\x01",
            "their feet steady on the ground,\x01",
            "I'm sure a path to the future will open.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A97")

    label("loc_19F7")


    ChrTalk(
        0xB,
        (
            "I'm so relieved Logy\x01",
            "got back from the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As long as the young ones keep\x01",
            "their feet steady on the ground,\x01",
            "I'm sure a path to the future will open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A97")

    Jump("loc_28B2")

    label("loc_1A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B41")

    ChrTalk(
        0xB,
        (
            "The independence declaration\x01",
            "of invalidity crushed the\x01",
            "President's legitimacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We may be standing\x01",
            "at the crossroads\x01",
            "of history.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B77")

    label("loc_1B41")


    ChrTalk(
        0xB,
        (
            "We may be standing\x01",
            "at the crossroads\x01",
            "of history.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B77")

    Jump("loc_28B2")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C61")

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
            "With the mine sealed,\x01",
            "it seems Logy has\x01",
            "lost his will to live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh*, what should I do about this, I wonder.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CC6")

    label("loc_1C61")


    ChrTalk(
        0xB,
        (
            "And just when\x01",
            "Logy was so\x01",
            "motivated, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh*, what should I do about this, I wonder.\x02",
    )

    CloseMessageWindow()

    label("loc_1CC6")

    Jump("loc_28B2")

    label("loc_1CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D6A")

    ChrTalk(
        0xB,
        (
            "To think a Mainz occupation\x01",
            "has occurred again, just\x01",
            "like at the time of disputes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, what has happened to\x01",
            "our Crossbell, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B2")

    label("loc_1D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E72")

    ChrTalk(
        0xB,
        (
            "There's been more people leaving\x01",
            "for the city recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Logy and the others are\x01",
            "still young. They feel pride\x01",
            "toward this town of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To me, who has lived in this \x01",
            "town for a long time, there\x01",
            "could be nothing happier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F20")

    label("loc_1E72")


    ChrTalk(
        0xB,
        (
            "Logy and the others are\x01",
            "still young. They feel pride\x01",
            "toward this town of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To me, who has lived in this \x01",
            "town for a long time, there\x01",
            "could be nothing happier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F20")

    Jump("loc_28B2")

    label("loc_1F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_207C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200C")

    ChrTalk(
        0xB,
        (
            "It seems Logy is doing\x01",
            "proper working, and living\x01",
            "out his days fully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh. All that's left is\x01",
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
    Jump("loc_2077")

    label("loc_200C")


    ChrTalk(
        0xB,
        (
            "If Logy brings a\x01",
            "wife home, I'll be\x01",
            "able to rest easy.\x02",
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

    label("loc_2077")

    Jump("loc_28B2")

    label("loc_207C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(
        0xB,
        "Crossbell State independence...\x02",
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
            "It's just, the Empire and Republic won't\x01",
            "ever see this as something good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Independence would make good coals\x01",
            "for the flame of a new conflict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_227F")

    label("loc_21D7")


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
            "Independence would make good coals\x01",
            "for the flame of a new conflict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227F")

    Jump("loc_28B2")

    label("loc_2284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CE")

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
            "Technological progress is truly the savior of\x01",
            "humanity. This is a good age to be living in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2494")

    label("loc_23CE")


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
            "Technological progress is truly the savior of\x01",
            "humanity. This is a good age to be living in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    Jump("loc_28B2")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_258F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2536")

    ChrTalk(
        0xB,
        (
            "It always gets noisy\x01",
            "when Ami and Logy\x01",
            "are together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, well, I'm glad they get\x01",
            "along well as brother and sister.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_258A")

    label("loc_2536")


    ChrTalk(
        0xB,
        "Even so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wish they wouldn't\x01",
            "bicker so much, and\x01",
            "help with the chores.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258A")

    Jump("loc_28B2")

    label("loc_258F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2645")

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
            "Ah, nothing could make me happier.\x01",
            "...O Goddess of the Sky, I thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26FA")

    label("loc_2645")


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
            "...O Goddess of the Sky, I\x01",
            "thank you. Please, watch over\x01",
            "those children forevermore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FA")

    Jump("loc_28B2")

    label("loc_26FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_28B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2833")

    ChrTalk(
        0xB,
        (
            "The old mine is right outside of town. It was\x01",
            "our principal one until some ten-odd years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In it's heyday, it was\x01",
            "a mountain of treasure,\x01",
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
    Jump("loc_28B2")

    label("loc_2833")


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

    label("loc_28B2")

    TalkEnd(0xFE)
    Return()

    # Function_8_18F7 end

    def Function_9_28B6(): pass

    label("Function_9_28B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28C7")
    Jump("loc_2AAF")

    label("loc_28C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2981")

    ChrTalk(
        0xD,
        (
            "Oh, you're walking\x01",
            "in the rain without\x01",
            "an umbrella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm, I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...This must be what they\x01",
            "call a "man is handsome\x01",
            "even when drenched".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29CE")

    label("loc_2981")


    ChrTalk(
        0xD,
        (
            "You guys must be what they\x01",
            "call a "man is handsome\x01",
            "even when drenched".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CE")

    Jump("loc_2AAF")

    label("loc_29D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29E1")
    Jump("loc_2AAF")

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29EF")
    Jump("loc_2AAF")

    label("loc_29EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29FD")
    Jump("loc_2AAF")

    label("loc_29FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A18")
    Call(0, 10)
    Jump("loc_2A93")

    label("loc_2A18")


    ChrTalk(
        0xD,
        (
            "My brother's doesn't have\x01",
            "any frivolous stories to tell,\x01",
            "so I'm bored...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I guess I'm like him too, though.\x02",
    )

    CloseMessageWindow()

    label("loc_2A93")

    Jump("loc_2AAF")

    label("loc_2A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AA6")
    Jump("loc_2AAF")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2AAF")

    label("loc_2AAF")

    TalkEnd(0xFE)
    Return()

    # Function_9_28B6 end

    def Function_10_2AB3(): pass

    label("Function_10_2AB3")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xD,
        (
            "Hey, brother. Got any\x01",
            "frivolous stories to tell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't. \x01",
            "Women are annoying, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "What! You're no fun...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ah, in that case, how about Mr. Gantz? \x01",
            "There're pretty bunny girls at the\x01",
            "casino and they're all smiles and...\x02",
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

    # Function_10_2AB3 end

    def Function_11_2BDB(): pass

    label("Function_11_2BDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BEC")
    Jump("loc_2CC7")

    label("loc_2BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BFA")
    Jump("loc_2CC7")

    label("loc_2BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2C08")
    Jump("loc_2CC7")

    label("loc_2C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C16")
    Jump("loc_2CC7")

    label("loc_2C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C24")
    Jump("loc_2CC7")

    label("loc_2C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3F")
    Call(0, 10)
    Jump("loc_2CAB")

    label("loc_2C3F")


    ChrTalk(
        0x10,
        (
            "Man, talking with Ami\x01",
            "is really annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "And it's my day off too. \x01",
            "I wish she'd let me enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CAB")

    Jump("loc_2CC7")

    label("loc_2CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CBE")
    Jump("loc_2CC7")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2CC7")

    label("loc_2CC7")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BDB end

    def Function_12_2CCB(): pass

    label("Function_12_2CCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D85")

    ChrTalk(
        0xC,
        (
            "I'm relieved Max\x01",
            "is well again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The sight of the miners\x01",
            "working hard is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a woman of Mainz, I have to\x01",
            "support them as best I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E0A")

    label("loc_2D85")


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
            "As a woman of Mainz, I have to\x01",
            "support them as best I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0A")

    Jump("loc_3A11")

    label("loc_2E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFC")

    ChrTalk(
        0xC,
        (
            "It looks like the Resistance\x01",
            "is preparing for something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...If the CGF got injured like\x01",
            "in that occupation incident, \x01",
            "I don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I really hope they don't get themselves hurt.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F90")

    label("loc_2EFC")


    ChrTalk(
        0xC,
        (
            "...If the CGF got injured like\x01",
            "in that occupation incident, \x01",
            "I don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I really hope they don't get themselves hurt.\x02",
    )

    CloseMessageWindow()

    label("loc_2F90")

    Jump("loc_3A11")

    label("loc_2F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB0")
    Call(0, 13)
    Jump("loc_304C")

    label("loc_2FB0")


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
            "I've got to do everything \x01",
            "I can to cheer him up. \x01",
            "He'll get sick at this rate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304C")

    Jump("loc_3A11")

    label("loc_3051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_315E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F6")

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
            "They too probably had someone waiting\x01",
            "for them... I have no words.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3159")

    label("loc_30F6")


    ChrTalk(
        0xC,
        (
            "Those people from the CGF probably\x01",
            "had someone waiting for them too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...I have no words.\x02",
    )

    CloseMessageWindow()

    label("loc_3159")

    Jump("loc_3A11")

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3265")

    ChrTalk(
        0xC,
        (
            "Everyone, you have to be\x01",
            "careful in Mainz on rainy days.\x02",
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
            "Both Max and I have watched out for\x01",
            "that ever since we were little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32EC")

    label("loc_3265")


    ChrTalk(
        0xC,
        (
            "Everyone, you have to be\x01",
            "careful in Mainz on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Both Max and I have watched out for\x01",
            "that ever since we were little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EC")

    Jump("loc_3A11")

    label("loc_32F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FB")

    ChrTalk(
        0xC,
        (
            "Strangely, my husband has been\x01",
            "enjoying his work lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because Mr. Gantz and Mr. Logy\x01",
            "are so motivated, I think it's\x01",
            "rubbed off on him.\x02",
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
    Jump("loc_34AC")

    label("loc_33FB")


    ChrTalk(
        0xC,
        (
            "Because Mr. Gantz and Mr.\x01",
            "Logy are so motivated, I think\x01",
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

    label("loc_34AC")

    Jump("loc_3A11")

    label("loc_34B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_363B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359B")

    ChrTalk(
        0xC,
        (
            "I'm told a large monster has appeared\x01",
            "in the north mountain region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's not that far from town. \x01",
            "I worry one might appear in the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The miners aren't equipped\x01",
            "to deal with large monsters.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3636")

    label("loc_359B")


    ChrTalk(
        0xC,
        (
            "A large monster appeared in\x01",
            "the north mountain region.\x02",
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

    label("loc_3636")

    Jump("loc_3A11")

    label("loc_363B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36C9")

    ChrTalk(
        0xC,
        (
            "It seems the Trade\x01",
            "Conference has opened\x01",
            "in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Will discussions at\x01",
            "the conference affect\x01",
            "Mainz's future?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A11")

    label("loc_36C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3761")

    ChrTalk(
        0xC,
        (
            "Max went to drink with\x01",
            "the mine captain today.\x02",
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
    Jump("loc_3A11")

    label("loc_3761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385A")

    ChrTalk(
        0xC,
        (
            "Monsters appears in the mine\x01",
            "attracted to the buried Septium.\x02",
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
            "If it's just simple monsters, they\x01",
            "can deal with them on their own.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38D2")

    label("loc_385A")


    ChrTalk(
        0xC,
        (
            "The miners of Mainz\x01",
            "are all strong men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If monsters appear in the mine,\x01",
            "they can deal with them on their own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D2")

    Jump("loc_3A11")

    label("loc_38D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398E")

    ChrTalk(
        0xC,
        (
            "My husband works\x01",
            "as a miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Among the young men,\x01",
            "he's the biggest earner.\x02",
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
    Jump("loc_3A11")

    label("loc_398E")


    ChrTalk(
        0xC,
        (
            "Today too, my husband will\x01",
            "probably be hungry when\x01",
            "he gets home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to get a lot of\x01",
            "dinner ready and wait for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A11")

    TalkEnd(0xFE)
    Return()

    # Function_12_2CCB end

    def Function_13_3A15(): pass

    label("Function_13_3A15")

    OP_4B(0xC, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "*sigh*... Digging holes is\x01",
            "the only thing I'm good for. \x01",
            "To think I can't work as a miner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Max, quit feeling\x01",
            "sorry for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You'll be able to\x01",
            "enter the mine soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I hope you're right...\x01",
            "...*sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Goodness.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_3A15 end

    def Function_14_3B27(): pass

    label("Function_14_3B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B38")
    Jump("loc_3C38")

    label("loc_3B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3BDE")

    ChrTalk(
        0x12,
        (
            "I can't work in the mine, \x01",
            "so I'm helping out in town\x01",
            "with physical works.\x02",
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
    Jump("loc_3C38")

    label("loc_3BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF9")
    Call(0, 13)
    Jump("loc_3C38")

    label("loc_3BF9")


    ChrTalk(
        0x12,
        (
            "*sigh*... Digging holes is the\x01",
            "only thing I'm good for...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C38")

    TalkEnd(0xFE)
    Return()

    # Function_14_3B27 end

    def Function_15_3C3C(): pass

    label("Function_15_3C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C53")
    Call(0, 24)
    Return()

    label("loc_3C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C72")
    Call(0, 16)
    Return()

    label("loc_3C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9B")

    ChrTalk(
        0x8,
        (
            "It seems that the CGF turned\x01",
            "Resistance were able to safely\x01",
            "join with the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that the President has been\x01",
            "arrested, they no longer have a\x01",
            "reason to continue hostilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So Mireille and the\x01",
            "others' Resistance was a\x01",
            "success. ...What a relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E04")

    label("loc_3D9B")


    ChrTalk(
        0x8,
        (
            "The mine has reopened, and\x01",
            "we're getting our energy back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the real\x01",
            "battle begins now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E04")

    Jump("loc_4EE8")

    label("loc_3E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2E")

    ChrTalk(
        0x8,
        (
            "With the President's legitimacy shaken, the\x01",
            "State Guard have adopted a wait-and-see stance.\x02",
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
            "that the Resistance's\x01",
            "mission will be a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FD7")

    label("loc_3F2E")


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
            "that the Resistance's\x01",
            "mission will be a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD7")

    Jump("loc_4EE8")

    label("loc_3FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_40C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF7")
    Call(0, 17)
    Jump("loc_40BD")

    label("loc_3FF7")


    ChrTalk(
        0x8,
        (
            "To begin with, in Mainz, we can\x01",
            "only distrust the President for\x01",
            "freely making use of jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Resistance are struggling to do\x01",
            "something about the current order.\x01",
            "They're our only hope.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40BD")

    Jump("loc_4EE8")

    label("loc_40C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4345")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D3")

    ChrTalk(
        0x8,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMayor Bickson... Things have\x01",
            "been tough in Mainz, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah... \x01",
            "We hardly had any severe damage,\x01",
            "but as expected, everyone's in shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been coping up with\x01",
            "that for awhile also using\x01",
            "the Bracers' cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe shock of this incident\x01",
            "must have been considerable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah... It seems things have\x01",
            "calmed down a bit, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as the Town Mayor,\x01",
            "I plan to do all I can.\x01\x02",
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
    Jump("loc_4340")

    label("loc_42D3")


    ChrTalk(
        0x8,
        (
            "Anyway, as the Town Mayor,\x01",
            "I plan to do all I can.\x01\x02",
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

    label("loc_4340")

    Jump("loc_4EE8")

    label("loc_4345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_453B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A3")

    ChrTalk(
        0x8,
        (
            "Recently, I've been hearing reports\x01",
            "of large, unknown monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A large monster was sighted in\x01",
            "yesterday's train accident as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could these have something to\x01",
            "do with the large monster that\x01",
            "appeared in the old mine before...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Anyhow, it seems it's better to be\x01",
            "careful for everyone's safety too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4536")

    label("loc_44A3")


    ChrTalk(
        0x8,
        (
            "I've been hearing reports of large, \x01",
            "unknown monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Anyhow, it seems it's better to be\x01",
            "careful for everyone's safety too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4536")

    Jump("loc_4EE8")

    label("loc_453B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468A")

    ChrTalk(
        0x8,
        (
            "Recently, it seems the Bracers\x01",
            "are busier than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's gotten much harder to submit\x01",
            "requests that aren't urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems they're investigating\x01",
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
    Jump("loc_471D")

    label("loc_468A")


    ChrTalk(
        0x8,
        (
            "It seems the Bracers here\x01",
            "are busier than usual.\x02",
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

    label("loc_471D")

    Jump("loc_4EE8")

    label("loc_4722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4868")

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
            "The Empire and Republic have a history\x01",
            "of fighting over our mined resources. \x01",
            "We'll have to consider the question seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Each of the people of\x01",
            "Mainz must consider the\x01",
            "question individually.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48FB")

    label("loc_4868")


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
            "As one of them, I'll consider\x01",
            "it myself until election day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FB")

    Jump("loc_4EE8")

    label("loc_4900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A02")

    ChrTalk(
        0x8,
        "Gantz is rather generous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if he rarely wins at the casino,\x01",
            "he immediately use everything for\x01",
            "giving us gifts and treating us to drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rather, I feel he's throwing away more\x01",
            "mira than when he comes back broke.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AAA")

    label("loc_4A02")


    ChrTalk(
        0x8,
        (
            "I feel like Gantz is throwing away more mira\x01",
            "when he comes back after winning than\x01",
            "when he comes back broke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, I'm not strongly against this side of him.\x02",
    )

    CloseMessageWindow()

    label("loc_4AAA")

    Jump("loc_4EE8")

    label("loc_4AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BEE")

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
            "technological advances greatly,\x01",
            "but somehow I have mixed feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It feels like the town of Mainz\x01",
            "has been left another step behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Ha ha, please don't worry about it.\x01",
            "I'm just an old man talking to himself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CA2")

    label("loc_4BEE")


    ChrTalk(
        0x8,
        (
            "Anyhow, I think the Trade\x01",
            "Conference will have great meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the future of our autonomous state,\x01",
            "I wish Mayor Dieter and Chairman\x01",
            "MacDowell to do their best for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA2")

    Jump("loc_4EE8")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBF")
    Jump("loc_4D5B")

    label("loc_4CBF")


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
            "It would be helpful if you could look\x01",
            "in there every now and then for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D5B")

    Jump("loc_4EE8")

    label("loc_4D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4C")

    ChrTalk(
        0x8,
        (
            "To get to the old mine, leave\x01",
            "town, go down the mountain a\x01",
            "bit, then climb northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't know why the gate was\x01",
            "destroyed, or if anything's\x01",
            "happening in the tunnels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, do\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EE8")

    label("loc_4E4C")


    ChrTalk(
        0x8,
        (
            "To get to the old mine, leave\x01",
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

    label("loc_4EE8")

    TalkEnd(0xFE)
    Return()

    # Function_15_3C3C end

    def Function_16_4EEC(): pass

    label("Function_16_4EEC")


    ChrTalk(
        0x8,
        (
            "We replaced the broken old mine gate\x01",
            "with a sturdy new one the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right. Just in\x01",
            "case, will you take this?\x02",
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
            "#00105FUmm, are you sure? \x01",
            "We're outsiders, after all...\x02",
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
            "If there's anything you need to\x01",
            "investigate, please feel free to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just in case, we rebuilt the ladder\x01",
            "so it'll be easier to come and go.\x02",
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

    # Function_16_4EEC end

    def Function_17_50E8(): pass

    label("Function_17_50E8")

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
            "And you need oil for equipment\x01",
            "maintenance, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Backerei's store should have\x01",
            "some of that. I'll check there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07902FSure. And thank you very much.\x02\x03",
            "#07908F...We're really grateful\x01",
            "to the people of Mainz.\x02\x03",
            "#07903FIf you exposed us to\x01",
            "the State Guard, we'd\x01",
            "be in dire straits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, what are you saying?\x01",
            "...Please don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To begin with, in Mainz, we can\x01",
            "only distrust the President for\x01",
            "freely making use of jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this situation...the appearance of a\x01",
            "a Resistance force that protests the\x01",
            "status quo, is none other than our hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, I'll do everything I\x01",
            "can to support your operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07904F...Thank you very much. I will\x01",
            "never forget your kindness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_17_50E8 end

    def Function_18_540B(): pass

    label("Function_18_540B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552C")

    ChrTalk(
        0x9,
        (
            "Miss Mireille and the others CGF\x01",
            "did their best for us with their\x01",
            "long Resistance activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They thanked us many times\x01",
            "when leaving town, but...\x01",
            "We want to thank them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once everything is settled,\x01",
            "I want to invite them\x01",
            "all back to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55D9")

    label("loc_552C")


    ChrTalk(
        0x9,
        (
            "Miss Mireille and the others CGF\x01",
            "did their best for us with their\x01",
            "long Resistance activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once everything is settled,\x01",
            "I want to invite them\x01",
            "all back to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D9")

    Jump("loc_658C")

    label("loc_55DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_572A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A9")

    ChrTalk(
        0x9,
        (
            "It seems Miss Mireille and the\x01",
            "others are resting at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They said they'd be even\x01",
            "busier before long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're taking this opportunity\x01",
            "to get proper rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5725")

    label("loc_56A9")


    ChrTalk(
        0x9,
        (
            "It seems Miss Mireille and the\x01",
            "others are resting at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're taking this opportunity\x01",
            "to get proper rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5725")

    Jump("loc_658C")

    label("loc_572A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_58A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584C")

    ChrTalk(
        0x9,
        (
            "It seems Miss Mireille and the\x01",
            "others set up camp within\x01",
            "the mountain region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter how used to being outdoors you are,\x01",
            "it must be hard to keep it up for this long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It would be nice if the\x01",
            "State Guard and jaegers'\x01",
            "searches ceased a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_589E")

    label("loc_584C")


    ChrTalk(
        0x9,
        (
            "It would be nice if the\x01",
            "State Guard and jaegers'\x01",
            "searches ceased a little...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_589E")

    Jump("loc_658C")

    label("loc_58A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5974")

    ChrTalk(
        0x9,
        (
            "Miss Eolia gave me some\x01",
            "of her calming herb\x01",
            "tea the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thanks to that, I've felt\x01",
            "relaxed for the past week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to thank Miss Eolia\x01",
            "and Miss Ling for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A0A")

    label("loc_5974")


    ChrTalk(
        0x9,
        (
            "Miss Eolia and Miss Ling left for \x01",
            "the old mine today to exterminate\x01",
            "some monsters for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to thank\x01",
            "those ladies for\x01",
            "all their help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0A")

    Jump("loc_658C")

    label("loc_5A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD8")

    ChrTalk(
        0x9,
        "The mountain weather changes easily.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This rain is so bad, they even\x01",
            "had to discontinue bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should take care coming\x01",
            "and going in today's downpour.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B5C")

    label("loc_5AD8")


    ChrTalk(
        0x9,
        (
            "This rain is so bad, they even\x01",
            "had to discontinue bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should take care coming\x01",
            "and going in today's downpour.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B5C")

    Jump("loc_658C")

    label("loc_5B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4D")

    ChrTalk(
        0x9,
        (
            "It's really hard to find a marriage\x01",
            "partner for the miners, hm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "None of those misters,\x01",
            "Gantz, Marlow and Logy,\x01",
            "seem eager to find someone too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess young ones don't\x01",
            "long to get married...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5CD7")

    label("loc_5C4D")


    ChrTalk(
        0x9,
        (
            "None of those misters,\x01",
            "Gantz, Marlow and Logy,\x01",
            "seem eager to find someone too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess young ones don't\x01",
            "long to get married...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CD7")

    Jump("loc_658C")

    label("loc_5CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DFB")

    ChrTalk(
        0x9,
        (
            "Crossbell has to pay a 10%\x01",
            "of combined taxes to the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For a growing economy like Crossbell,\x01",
            "10% is a staggering amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can be seen as a decision symbolic\x01",
            "of Crossbell's subordinate relationship \x01",
            "with the two major powers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5EB8")

    label("loc_5DFB")


    ChrTalk(
        0x9,
        (
            "Crossbell has to pay a 10%\x01",
            "of combined taxes to the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It can be seen as a decision symbolic\x01",
            "of Crossbell's subordinate relationship \x01",
            "with the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB8")

    Jump("loc_658C")

    label("loc_5EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_60EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6056")

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
            "#00205F...You're talking\x01",
            "about me, aren't you.\x02\x03",
            "I'm not at the right age\x01",
            "to be married yet, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, still, you're\x01",
            "very beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In case you won't find anyone when \x01",
            "you're older, please consider it.\x02",
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
        "#00012F(H-Ha ha...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60E7")

    label("loc_6056")


    ChrTalk(
        0x9,
        (
            "Uh uh, when you're older, \x01",
            "if you find yourself without\x01",
            "a partner, please consider it.\x02",
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

    label("loc_60E7")

    Jump("loc_658C")

    label("loc_60EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6187")

    ChrTalk(
        0x9,
        "The miners are taking the day off.\x02",
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
    Jump("loc_658C")

    label("loc_6187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6407")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638B")

    ChrTalk(
        0x9,
        "That's right, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps you'd like a marriage interview\x01",
            "with one of our village's miners?\x02",
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
            "Yes. If Mr. Gantz and the others\x01",
            "had someone to come home to,\x01",
            "I think they'd work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What do you say, young ladies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FU-Umm... I'm sorry. I'm not\x01",
            "thinking of marrying yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FM-Me as well. Right now,\x01",
            "work takes priority...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I see... That's too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, if you change your\x01",
            "mind, please consider it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6402")

    label("loc_638B")


    ChrTalk(
        0x9,
        (
            "If you change your opinion on the\x01",
            "marriage interview, please consider it.\x02",
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

    label("loc_6402")

    Jump("loc_658C")

    label("loc_6407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_658C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FD")

    ChrTalk(
        0x9,
        (
            "That old mine was\x01",
            "still in use a\x01",
            "few decades ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I heard that our predecessors\x01",
            "closed it firmly because it had\x01",
            "become dangerous to go inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who would break the\x01",
            "lock. It's somehow strange...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_658C")

    label("loc_64FD")


    ChrTalk(
        0x9,
        (
            "It's dangerous to go\x01",
            "inside the old mine, so\x01",
            "it was firmly sealed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder who would break the\x01",
            "lock. It's somehow strange...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_658C")

    TalkEnd(0xFE)
    Return()

    # Function_18_540B end

    def Function_19_6590(): pass

    label("Function_19_6590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A7")
    Call(0, 24)
    Return()

    label("loc_65A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65B8")
    Jump("loc_66AF")

    label("loc_65B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65C6")
    Jump("loc_66AF")

    label("loc_65C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65D4")
    Jump("loc_66AF")

    label("loc_65D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_65E2")
    Jump("loc_66AF")

    label("loc_65E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_65F0")
    Jump("loc_66AF")

    label("loc_65F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_65FE")
    Jump("loc_66AF")

    label("loc_65FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_66A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6616")
    Jump("loc_66A1")

    label("loc_6616")


    ChrTalk(
        0xF,
        (
            "Buying up such a large quantity\x01",
            "of Septium... There aren't even\x01",
            "many traders that can do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "...I really wonder who thet were.\x02",
    )

    CloseMessageWindow()

    label("loc_66A1")

    Jump("loc_66AF")

    label("loc_66A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_66AF")

    label("loc_66AF")

    TalkEnd(0xFE)
    Return()

    # Function_19_6590 end

    def Function_20_66B3(): pass

    label("Function_20_66B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_66C4")
    Jump("loc_6928")

    label("loc_66C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_66D2")
    Jump("loc_6928")

    label("loc_66D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66ED")
    Call(0, 17)
    Jump("loc_6928")

    label("loc_66ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_688C")

    ChrTalk(
        0x13,
        (
            "#07903FThe tough situation hasn't changed.\x01",
            "We plan to do our best for awhile\x01",
            "in the mountain region.\x02\x03",
            "#07901FRandy, and the Support Section...\x01",
            "Please leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FSure, understood.\x02\x03",
            "#00301F...Don't lose to the jaegers \x01",
            "and State Guard, got it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        (
            "#07902FUh uh, look who's talking.\x02\x03",
            "#07904FThe people of Mainz are\x01",
            "cooperating with us, so I'm\x01",
            "sure we'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6928")

    label("loc_688C")


    ChrTalk(
        0x13,
        (
            "#07900FRandy, and the Support Section...\x01",
            "Please leave this to us.\x02\x03",
            "#07904FThe people of Mainz are\x01",
            "cooperating with us, so I'm\x01",
            "sure we'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6928")

    TalkEnd(0xFE)
    Return()

    # Function_20_66B3 end

    def Function_21_692C(): pass

    label("Function_21_692C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5B")

    ChrTalk(
        0x14,
        (
            "Because we've gained the help of the divine\x01",
            "wolves, it'll be easier for us to act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "They're keeping watch over the\x01",
            "mountain path and region... Just\x01",
            "that lightens our burden considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "2nd Lt. Mireille wants to take this\x01",
            "chance to rest as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6B0C")

    label("loc_6A5B")


    ChrTalk(
        0x14,
        (
            "Keeping watch over the mountain\x01",
            "path and region... Just that\x01",
            "lightens our burden considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "2nd Lt. Mireille wants to take this\x01",
            "chance to rest as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B0C")

    TalkEnd(0xFE)
    Return()

    # Function_21_692C end

    def Function_22_6B10(): pass

    label("Function_22_6B10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B5A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1555), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B30")
    Sleep(1500)
    Jump("loc_6B45")

    label("loc_6B30")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)

    label("loc_6B45")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B55")
    Sleep(333)

    label("loc_6B55")

    Jump("Function_22_6B10")

    label("loc_6B5A")

    Return()

    # Function_22_6B10 end

    def Function_23_6B5B(): pass

    label("Function_23_6B5B")

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
            "#2P──Excuse us. We're the Crossbell\x01",
            "Police, Special Support Section.\x02",
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

    def lambda_6D83():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6D83)
    Sleep(50)

    def lambda_6D93():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6D93)
    Sleep(50)

    def lambda_6DA3():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6DA3)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xF, 0)
    Sleep(500)

    def lambda_6DC2():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DC2)

    def lambda_6DDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DDC)
    Sleep(100)

    def lambda_6DF0():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DF0)

    def lambda_6E0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E0A)
    Sleep(50)

    def lambda_6E1E():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E1E)

    def lambda_6E38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6E38)
    Sleep(80)

    def lambda_6E4C():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E4C)

    def lambda_6E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6E66)
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
            "#11POh, it's you guys. Sorry to\x01",
            "make you come all this way.\x02",
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
        "#00002F#6PHello everyone, it's nice to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PMr. Gantz, how are\x01",
            "you feeling now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2PYeah, no bad effects\x01",
            "at all. I'm doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2PThanks again for\x01",
            "all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#6P*giggle*, we're happy you're doing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PSo then, monsters\x01",
            "showed up in an\x01",
            ""old mine"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes. There is a mine\x01",
            "near town that has been\x01",
            "abandoned for decades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMy, it's not good talking while standing...\x01",
            "Please, have a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'll get you all some tea now.\x02",
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
            "#00005F──The sealed entrance\x01",
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
            "#5PYes. Even though it's many years\x01",
            "old, it was a very sturdy one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POne of our citizens found\x01",
            "it destroyed, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWe just saw it intact two days ago, so\x01",
            "it must've been destroyed yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PSeriously, it must've been something\x01",
            "really strong to be able to do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P...That worries me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PSo then, once you checked inside\x01",
            "you saw monsters roaming around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PBut it's an old abandoned mine, so it's not\x01",
            "that strange for monsters to appear, is it?\x02",
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
            "#5PWhat was strange is\x01",
            "the tunnel itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PThe tunnel itself...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PHow could I put it...\x01",
            "It was faintly glowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PIt was like the walls themselves were\x01",
            "glowing with a purple-red light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PW-Well...that's\x01",
            "strange indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12PSeeing as how the mine is many years old,\x01",
            "there shouldn't be any orbal lamps.\x02\x03",
            "#00001FI wonder what the cause\x01",
            "of the glow might be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, there's no real harm done.\x01",
            "We're just worried about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWe know how busy you're, but we decided\x01",
            "to ask you to help us deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12PWe understand the situation.\x02",
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
            "#00001F#12PSeeing as the gate was destroyed,\x01",
            "I'd say we have a case.\x02\x03",
            "How about we head there right away?\x02",
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
        "#10101F#6PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHu hu... Sounds like a\x01",
            "very interesting case.\x02",
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
            "#5PGantz, please show\x01",
            "them inside for me.\x02",
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
            "#5PSo then, I'll go on ahead. \x01",
            "Once you're ready, please find me there.\x02",
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

    def lambda_7922():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7922)
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
            "#00002F#12P...Thank goodness.\x01",
            "He really looks to be doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYeah, and it's all thanks to you guys.\x02",
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
            "#5PHe still throws his mira away\x01",
            "at the casino on his days off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12P*giggle*, is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, as long as he doesn't\x01",
            "overdo it, he should be fine...\x02\x03",
            "#00005FOh right. The old mine is\x01",
            "just outside the town right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYeah. Head down the mountain\x01",
            "a bit, then head northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe don't know what caused the\x01",
            "incident. Please be very careful.\x02",
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

    # Function_23_6B5B end

    def Function_24_7CB4(): pass

    label("Function_24_7CB4")

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
            "Well, maybe we\x01",
            "shouldn't overthink it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "We made a very good profit.\x02",
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
            "#6P#00000FUmm...\x01",
            "Town Mayor,\x01",
            "Mr. Gantz, good day.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7E9E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7E9E)
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
            "Sorry, we were\x01",
            "just talking.\x02",
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
            "#11PAh, well, several CGF patrols\x01",
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
            "#11P...It's just, there's something\x01",
            "else that has me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou see, a strange group\x01",
            "appeared in Mainz the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThey bought some big chunks of \x01",
            "Septium crystals for a huge sum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FA strange group...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHow should I put it... Well, anyway,\x01",
            "they had a unique air about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt seemed like a well-built redheaded\x01",
            "middle-aged man was their leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PActually, it was exactly\x01",
            "like the hair of Randy\x01",
            "there, come to think of it.\x02",
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
        "#00005F#6P(The "Red Constellation"...!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F...Did they do\x01",
            "anything besides that\x01",
            "Septium purchase?\x02",
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
            "had me worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F(Based on what senior Randy said\x01",
            "earlier, it seems like they were\x01",
            "the ones who set the explosives...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F(Well, we have no definitive proof,\x01",
            "so we shouldn't say anything.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(But, I wonder what that jaeger\x01",
            "corps is planning on doing with\x01",
            "those Septium crystals.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301F(...The "Crimson & Co." that\x01",
            "they run has connections to a lot\x01",
            "of good-for-nothing traders.)\x02\x03",
            "#00303F(As for those large chunks of Septium, they're\x01",
            "probably earnin' some side money from sellin'\x01",
            "them on the black market.)\x02",
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
        "#11P...Hmm, that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PMaybe I should give\x01",
            "that to you guys.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)

    ChrTalk(
        0x8,
        "#5PHand that over, Gantz.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "Yeah, got it.\x02",
    )

    CloseMessageWindow()

    def lambda_8724():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_8724)
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
        "#00005F#6PThis is for the old mine...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yeah. A spare key, so to speak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm, are you sure? \x01",
            "We're outsiders, after all...\x02",
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
            "If there's ever anything you need to\x01",
            "investigate, please be our guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just in case, we rebuilt the ladder\x01",
            "so it'll be easier to come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you very much.\x01",
            "We'll use it with care.\x02",
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

    # Function_24_7CB4 end

    SaveToFile()

Try(main)
