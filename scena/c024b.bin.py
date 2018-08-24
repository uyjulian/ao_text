﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c024b.bin",                # FileName
        "c024b",                    # MapName
        "c024b",                    # Location
        0x000F,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c024b",                  # 0
        "Sammy",                  # 1
        "Kindoll",                # 2
        "Brigitta",               # 3
        "Old Man Ryｹvic",        # 4
        "Mrs. Origa",             # 5
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21602.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20102.itc",                   # 07
        "chr/ch05102.itc",                   # 08
        "chr/ch10000.itc",                   # 09
    ))

    DeclNpc(9060,    10000,   18000,   45,   261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294965287, 1149,    60479,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(8470,    1019,    62380,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294921646, 1019,    60169,   180,  261,  0x0, 0,   4,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(7030,    150,     6969,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(4294966956, 10000,   20320,   1200,    4294966956, 11500,   20320,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(412, 0)                                        # 0

    ScpFunction((
        "Function_0_19C",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_2A2",          # 03, 3
        "Function_4_302",          # 04, 4
        "Function_5_309",          # 05, 5
        "Function_6_43A",          # 06, 6
        "Function_7_5D5",          # 07, 7
        "Function_8_68D",          # 08, 8
        "Function_9_72C",          # 09, 9
        "Function_10_842",         # 0A, 10
        "Function_11_885",         # 0B, 11
    ))


    def Function_0_19C(): pass

    label("Function_0_19C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1D4"),
        (1, "loc_1E0"),
        (2, "loc_1EC"),
        (3, "loc_1F8"),
        (4, "loc_204"),
        (5, "loc_210"),
        (6, "loc_21C"),
        (SWITCH_DEFAULT, "loc_228"),
    )


    label("loc_1D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_204")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_210")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_24B")

    Return()

    # Function_0_19C end

    def Function_1_24C(): pass

    label("Function_1_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_24C")

    label("loc_276")

    Return()

    # Function_1_24C end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A1")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_2_277")

    label("loc_2A1")

    Return()

    # Function_2_277 end

    def Function_3_2A2(): pass

    label("Function_3_2A2")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, -48700, 1200, 60400, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    Return()

    # Function_3_2A2 end

    def Function_4_302(): pass

    label("Function_4_302")

    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_302 end

    def Function_5_309(): pass

    label("Function_5_309")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")

    ChrTalk(
        0xFE,
        (
            "I heard each nation's VIPs\x01",
            "are going to the theatre to\x01",
            "see Arc-en-Ciel tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, they're going to\x01",
            "enjoy it from some nice\x01",
            "seats for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grrr, I'm so envious!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_436")

    label("loc_3D1")


    ChrTalk(
        0xFE,
        (
            "In the end, I failed to buy\x01",
            "the tickets for the next\x01",
            "renewal public performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*...\x02",
    )

    CloseMessageWindow()

    label("loc_436")

    TalkEnd(0xFE)
    Return()

    # Function_5_309 end

    def Function_6_43A(): pass

    label("Function_6_43A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557")

    ChrTalk(
        0xFE,
        (
            "When night falls, Orchis\x01",
            "Tower is lit up\x01",
            "beautifully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With its blue-and-white theme, the tower will\x01",
            "surely take your breath away with its brilliant,\x01",
            "shining beauty against the dark of night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. If you have the\x01",
            "chance, you absolutely\x01",
            "must see it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5D1")

    label("loc_557")


    ChrTalk(
        0xFE,
        (
            "When night falls, Orchis\x01",
            "Tower is lit up\x01",
            "beautifully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. If you have the\x01",
            "chance, you absolutely\x01",
            "must see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1")

    TalkEnd(0xFE)
    Return()

    # Function_6_43A end

    def Function_7_5D5(): pass

    label("Function_7_5D5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That husband of mine, I didn't\x01",
            "even ask and he's teaching me\x01",
            "many things about Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems his excitement\x01",
            "from the unveiling at noon\x01",
            "hasn't worn off.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5D5 end

    def Function_8_68D(): pass

    label("Function_8_68D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A2")
    Call(0, 9)
    Jump("loc_728")

    label("loc_6A2")


    ChrTalk(
        0xFE,
        (
            "I thought we would've drunk\x01",
            "it together and so I went\x01",
            "to buy a good wine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, enough already.\x01",
            "I'll drink it alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_728")

    TalkEnd(0xFE)
    Return()

    # Function_8_68D end

    def Function_9_72C(): pass

    label("Function_9_72C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "Aah, as I thought, this\x01",
            "wine is delicious. I'm\x01",
            "glad I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems you don't want\x01",
            "any, old lady, so I'll\x01",
            "drink it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Fine, do as you like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You paid a lot of mira\x01",
            "for it, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmph! *gluglugluglug*\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_9_72C end

    def Function_10_842(): pass

    label("Function_10_842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857")
    Call(0, 9)
    Jump("loc_881")

    label("loc_857")


    ChrTalk(
        0xFE,
        (
            "...Hmph, who cares about\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_881")

    TalkEnd(0xFE)
    Return()

    # Function_10_842 end

    def Function_11_885(): pass

    label("Function_11_885")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_885 end

    SaveToFile()

Try(main)
