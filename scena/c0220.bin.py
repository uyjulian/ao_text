from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0220",                  # 0
        "Ian lawyer",           # 1
        "Pete",                 # 2
        "Office worker",           # 3
        "Emma investigator",             # 4
        "Policeman",                   # 5
        "Investigator",                 # 6
        "Investigator",                 # 7
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
        "chr/ch27802.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch27600.itc",                   # 06
        "chr/ch27800.itc",                   # 07
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2259,    140,     5500,    90,   453,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5289,    1019,    16959,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1370,    29,      1990,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294958786, 0,       45979,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294966727, 29,      39380,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14350,   1000,    4294967226, 2000,    14350,   2500,    4294967226, 0x007C, 0,  20, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_4F7",          # 02, 2
        "Function_3_599",          # 03, 3
        "Function_4_20D3",         # 04, 4
        "Function_5_359D",         # 05, 5
        "Function_6_36D9",         # 06, 6
        "Function_7_387E",         # 07, 7
        "Function_8_392C",         # 08, 8
        "Function_9_3AB7",         # 09, 9
        "Function_10_3C09",        # 0A, 10
        "Function_11_49CD",        # 0B, 11
        "Function_12_4C92",        # 0C, 12
        "Function_13_5315",        # 0D, 13
        "Function_14_7186",        # 0E, 14
        "Function_15_71D1",        # 0F, 15
        "Function_16_721C",        # 10, 16
        "Function_17_7267",        # 11, 17
        "Function_18_72B2",        # 12, 18
        "Function_19_72FD",        # 13, 19
        "Function_20_7348",        # 14, 20
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5510, 1020, 16030, 225)
    Jump("loc_4C9")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, 3150, 1020, 12920, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4C9")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_368")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_387")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DA")
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_3FE")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3FE")

    SetChrFlags(0x8, 0x80)

    label("loc_403")

    Jump("loc_4C9")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_452")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x10)
    Jump("loc_4C9")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_471")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_490")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C9")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_4F6")

    Return()

    # Function_1_2A0 end

    def Function_2_4F7(): pass

    label("Function_2_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_57F")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)

    label("loc_598")

    Return()

    # Function_2_4F7 end

    def Function_3_599(): pass

    label("Function_3_599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 12)
    Jump("loc_20CF")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(
        0xFE,
        (
            "#02200FAre you guys ……\x01",
            "Did you see Mr. Dieter's speech?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FTo the sudden change of the situation\x01",
            "I feel confused …\x01",
            "Did you say that?\x02\x03",
            "#02203FMost of the citizens feel that way\x01",
            "It will be holding it.\x02\x03",
            "#02201FHowever, the \"dark fight\" of the two major powers\x01",
            "It is also the fact that actually happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F…… My uncle had said,\x01",
            "It's about an inexplicable \"accident\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FWell …\x02\x03",
            "#02201FBut, to such facts\x01",
            "While pretending not to notice,\x01",
            "I have enjoyed the happiness in front of me ……\x02\x03",
            "This is because as Dieter said\x01",
            "All of us living in the crossbell\x01",
            "I guess it is a sin.\x02\x03",
            "#02203FIndependence as a state,\x01",
            "To face them\x01",
            "I think that it is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMr. Ian … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FSorry\x01",
            "Having been addressed to that speech,\x01",
            "It seems that the fever has entered.\x02\x03",
            "#02200Fanyway……\x01",
            "Already a die#2RTo#He was thrown.\x02\x03",
            "#02203FWhat to do now … ….\x01",
            "That is because each residents\x01",
            "It must be a matter to think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 1)
    Jump("loc_9CA")

    label("loc_944")


    ChrTalk(
        0xFE,
        (
            "#02203FAlready a die#2RTo#He was thrown.\x02\x03",
            "#02200FWhat to do now … ….\x01",
            "That is because each residents\x01",
            "It must be a matter to think about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA")

    Jump("loc_20CF")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E98")

    ChrTalk(
        0xFE,
        (
            "#02203FFuu …\x01",
            "That company's company\x01",
            "The material … and …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Ian … …\x01",
            "You look busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "#02205FOh, you guys ……\x02\x03",
            "#02203FIn the case of an example attack many companies\x01",
            "You seem to have suffered damage.\x02\x03",
            "#02200FAbout a week ago,\x01",
            "I was consulted by them\x01",
            "I did not have a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F… It will be a hard time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FWell …\x01",
            "But it can not be helped.\x02\x03",
            "#02200FBecause IBC was destroyed,\x01",
            "Transaction destination and workplace itself\x01",
            "Many have lost.\x02\x03",
            "I am also a lawyer,\x01",
            "As much as we can\x01",
            "I have to do it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHugh, as expected\x01",
            "It is like Mr. Beak Bee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut,\x01",
            "Also draft a constitutional draft\x01",
            "You held them, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FOh, about that\x01",
            "I managed to finish it,\x01",
            "I just submitted it to the autonomous state government.\x02\x03",
            "#02202FNo, you can do it if you do it.\x01",
            "Thanks to recently I did not sleep until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIs it sleep insomnia … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FEr, impossible impossible\x01",
            "Please do not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FHehe, I am sorry for your thoughtfulness.\x02\x03",
            "#02203FToday's minutes' consultation\x01",
            "Because it will break up to a certain extent,\x01",
            "I am going to take a good rest tonight.\x02\x03",
            "#02200F…… Well then, you\x01",
            "I am sorry to have kept you waiting.\x02\x03",
            "You guys also have lots of requests\x01",
            "Whether it is coming,\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we'll do that\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_F1B")

    label("loc_E98")


    ChrTalk(
        0xFE,
        (
            "#02200FI am for the citizen\x01",
            "In the position of a lawyer\x01",
            "I will do my best.\x02\x03",
            "You guys also have lots of requests\x01",
            "Whether it is coming,\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1B")

    Jump("loc_20CF")

    label("loc_F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1035")

    ChrTalk(
        0xFE,
        (
            "#02200FRefrain from referendum\x01",
            "I got up at this timing\x01",
            "Occupation of Mainz …\x02\x03",
            "To withdraw independence advocacy\x01",
            "Empire, or republic organized,\x01",
            "There seems to be some citizens thinking that.\x02\x03",
            "#02203F…… No way,\x01",
            "To cause the situation so far,\x01",
            "I did not expect it either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10EF")

    label("loc_1035")


    ChrTalk(
        0xFE,
        (
            "#02200FThe case in this case, the empire and the republic\x01",
            "To withdraw independence advocacy\x01",
            "It is thought that it was structured.\x02\x03",
            "#02203F…… No way,\x01",
            "To cause the situation so far,\x01",
            "I did not expect it either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EF")

    Jump("loc_20CF")

    label("loc_10F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(
        0xFE,
        "#02200FOh, you guys ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(
        0x101,
        (
            "#00004FMr. Ian … …\x01",
            "Thanks for yesterday\x01",
            "It was.\x02\x03",
            "#00000FEvidence that the teacher found,\x01",
            "It was useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FOh, I heard the story from Pete.\x01",
            "A man named Minneshi, somehow\x01",
            "I heard that he did it for wanted arrangements.\x02\x03",
            "#02202FAlthough, although I say, I am only to the last\x01",
            "I just helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, I was really saved.\x02\x03",
            "#00000FAs for the draft constitution\x01",
            "I have been busy … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1307")

    label("loc_12B4")


    ChrTalk(
        0x101,
        (
            "#00000FMr. Ian … …\x01",
            "Long time no see.\x02\x03",
            "Preparation of a draft constitution,\x01",
            "It sounds like you are busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1307")


    ChrTalk(
        0xFE,
        (
            "#02200FOh, but a little\x01",
            "In the place where I got it together.\x02\x03",
            "Even cup of coffee to make a break\x01",
            "I was just thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh……\x01",
            "Interfere with the break time\x01",
            "Did it happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FNo, that's not it.\x01",
            "I also talk with you guys\x01",
            "It will be a good change.\x02\x03",
            "#02205F… By the way, you guys.\x01",
            "To investigate yesterday's derailment accident\x01",
            "It seems to have been ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, for the time being\x01",
            "I understood it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI omit a detailed explanation, but …\x01",
            "Artificially induced\x01",
            "There is no mistake when looking at as an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02205FHmm, was that so …?\x02\x03",
            "#02203F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FMr. Ian … …\x01",
            "What's the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F…, no, no dead people came out\x01",
            "Please think that it was really good.\x02\x03",
            "#02200FAnyway, recently it is something noisy.\x01",
            "You must be careful enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 0)
    Jump("loc_16E3")

    label("loc_15F6")


    ChrTalk(
        0xFE,
        (
            "#02200FA draft constitution has also been gathered up a bit … …\x01",
            "It seems that there is still room for improvement.\x02\x03",
            "#02203FAlthough there are some physical demands,\x01",
            "For the future of Crossbell\x01",
            "It can not cause a weak tone to vomit.\x02\x03",
            "#02200FAlways, the draft Constitution\x01",
            "I'll make it up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_20CF")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1784")

    ChrTalk(
        0x8,
        (
            "#02200FThis incident ……\x01",
            "As far as time permits\x01",
            "I will help you.\x02\x03",
            "#02202FHuhu, I will face it later\x01",
            "You guys also investigate\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CF")

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1820")

    ChrTalk(
        0x8,
        (
            "#02200FThis incident ……\x01",
            "As far as time permits\x01",
            "I will help you.\x02\x03",
            "#02202FHuhu, I will face it later\x01",
            "You guys also investigate\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CF")

    label("loc_1820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_182E")
    Jump("loc_20CF")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_183C")
    Jump("loc_20CF")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")

    ChrTalk(
        0xFE,
        (
            "#02205FOh, you guys.\x01",
            "It is rare to come this kind of night.\x02\x03",
            "#02200FDaddy is with you … …\x01",
            "It seems to be related to tomorrow's meeting\x01",
            "Have you had problems as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FFrom now on, make sure of it\x01",
            "I'm going.\x02\x03",
            "#00600FFor the sake of completeness,\x01",
            "To keep uncertain elements crushed\x01",
            "I have never done it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FWell, it's too cautious.\x01",
            "It will not be.\x02\x03",
            "#02200FI do not know detailed circumstances … …\x01",
            "Please do it by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A57")

    label("loc_19E9")


    ChrTalk(
        0xFE,
        (
            "#02200FNow……\x01",
            "Preparation is enough around here.\x02\x03",
            "#02203FIn preparation for tomorrow for the time being,\x01",
            "Shall I take a day off earlier today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A57")

    Jump("loc_20CF")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")

    ChrTalk(
        0xFE,
        (
            "#02200FThe leaders will crossbell\x01",
            "You seem to have visited.\x02\x03",
            "#02203FOn the first day of the trade meeting\x01",
            "The city's vigilance has further increased\x01",
            "I feel it.\x02\x03",
            "#02200FTrouble is called\x01",
            "What happens at such times ……\x01",
            "You guys are also careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BEF")

    label("loc_1B47")


    ChrTalk(
        0xFE,
        (
            "#02203FNow that the leaders have visited,\x01",
            "Crossbell city alert\x01",
            "It would have been further increased.\x02\x03",
            "#02200FTrouble is called\x01",
            "What happens at such times ……\x01",
            "You guys are also careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jump("loc_20CF")

    label("loc_1BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEE")

    ChrTalk(
        0xFE,
        (
            "#02200FThe commerce meeting is finally tomorrow,\x01",
            "It will be held.\x02\x03",
            "In the unveiling ceremony, the leaders of the countries\x01",
            "I plan to come … …\x02\x03",
            "In case you have something in their hands\x01",
            "It will develop into an international problem.\x02\x03",
            "To you guys, even more\x01",
            "I have to do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D60")

    label("loc_1CEE")


    ChrTalk(
        0xFE,
        (
            "#02200FIf you have something to worry about\x01",
            "Please contact us anytime.\x02\x03",
            "If you like me\x01",
            "Let everything be powerful\x01",
            "I will get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D60")

    Jump("loc_20CF")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(
        0xFE,
        (
            "#02203F\"Black Moon\" took over the acquisition of Rubathe's trace\x01",
            "You seem to be progressing steadily.\x02\x03",
            "#02201FThat place will be the one of the black moon,\x01",
            "I do not want to think much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI agree……\x01",
            "It is going to be troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F…… However, there is no way.\x01",
            "Probably to the story of reality\x01",
            "I guess it will be … …\x02\x03",
            "#02200FWhew ……\x01",
            "The problem that Crossbell has is\x01",
            "We still have many piles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F5D")

    label("loc_1ED8")


    ChrTalk(
        0xFE,
        (
            "#02200FRubache's trace is black moon\x01",
            "What got it\x01",
            "It will be a matter of time.\x02\x03",
            "Whew ……\x01",
            "The problem that Crossbell has is\x01",
            "We still have many piles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5D")

    Jump("loc_20CF")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(
        0xFE,
        (
            "#02203FThe Special Affairs Support Division\x01",
            "Great expectation from citizens\x01",
            "You should have it.\x02\x03",
            "#02202FBeing dependent on more than before\x01",
            "It will increase, but by all means\x01",
            "Do your best.\x02\x03",
            "The accumulation of each one,\x01",
            "Surely Crossbell's hope\x01",
            "I guess it will be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20CF")

    label("loc_205F")


    ChrTalk(
        0xFE,
        (
            "#02200FTo the work of the mission support department,\x01",
            "I also expect it.\x02\x03",
            "#02202FBy all means, to the expectations of citizens\x01",
            "Please answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CF")

    TalkEnd(0xFE)
    Return()

    # Function_3_599 end

    def Function_4_20D3(): pass

    label("Function_4_20D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F5")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_20F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",                      # 0
            "Read Ian's writing\x01",      # 1
            "quit\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2173")
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21F9")

    label("loc_2173")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2187")
    Jump("loc_21F9")

    label("loc_2187")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        "Thank you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "please……\x01",
            "I would like to ask Professor Ian.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F9")

    Jump("loc_20FF")

    label("loc_21FE")

    Jump("loc_3599")

    label("loc_2203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2211")
    Jump("loc_3599")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_22A9")

    ChrTalk(
        0xFE,
        (
            "Because of the independence of crossbell,\x01",
            "I drew up a draft constitution\x01",
            "I am Mr. Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As one of independent leaders,\x01",
            "There are places I think\x01",
            "I guess there are ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_22A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233F")

    ChrTalk(
        0xFE,
        (
            "Mr. Ian, very\x01",
            "I'm busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were one,\x01",
            "Instead of Mr. Ian\x01",
            "I was consulted … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23B9")

    label("loc_233F")


    ChrTalk(
        0xFE,
        (
            "…… Anyway now,\x01",
            "I will do my best with Mr. Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to have you take a rest,\x01",
            "I have to finish my work as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_3599")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_24F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    ChrTalk(
        0xFE,
        (
            "Mainz into an armed group\x01",
            "To be occupied ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the inhabitants have no sin,\x01",
            "It is a terrible story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What we do to our citizens\x01",
            "Is not it possible to do …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F2")

    label("loc_247A")


    ChrTalk(
        0xFE,
        (
            "Professor Ian also said that\x01",
            "It seems to be damaging my chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What we do to our citizens\x01",
            "Is not it possible to do …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F2")

    Jump("loc_3599")

    label("loc_24F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(
        0xFE,
        (
            "Yesterday's incident in Armoria\x01",
            "I have to put together … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I left it to the teacher,\x01",
            "Also, important documents are at the back of the mountain of documents\x01",
            "It will be buried.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2656")

    ChrTalk(
        0x101,
        (
            "#00000FHaha … but,\x01",
            "I am glad that I could really solve it.\x02\x03",
            "He helped me a lot\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, it is unexpected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone in the support department,\x01",
            "I really appreciate your work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CF")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_26F4")

    ChrTalk(
        0x101,
        (
            "#00003F(Case of Armorica ……\x01",
            "An example of minnes is a man\x01",
            "Is that about the matter involved? )\x02\x03",
            "(… after all, properly\x01",
            "I should have done it to the end … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CF")

    label("loc_26F4")


    ChrTalk(
        0x101,
        (
            "#00005FAlmorica's incident ……\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, actually an evil dealer ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, sorry.\x01",
            "What I did and …\x01",
            "It was confidentiality obligation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right.\x01",
            "Well, if you solve it\x01",
            "It was very nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CF")

    SetScenarioFlags(0x16C, 2)
    Jump("loc_281B")

    label("loc_27D7")


    ChrTalk(
        0xFE,
        (
            "Anyway……\x01",
            "The village of Almorika is saved\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_3599")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283B")
    SetScenarioFlags(0x0, 1)
    Jump("loc_283B")

    label("loc_283B")

    Jump("loc_3599")

    label("loc_2840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2929")

    ChrTalk(
        0xFE,
        (
            "Regarding the case of Almorika village,\x01",
            "I have identified similar cases in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clues to the solution from unexpected places\x01",
            "Because I will find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Professor Ian, Mr. Harold's\x01",
            "I am going to your house.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AD")

    label("loc_2929")


    ChrTalk(
        0xFE,
        (
            "Regarding the case of Almorika village,\x01",
            "I have identified similar cases in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Professor Ian, Mr. Harold's\x01",
            "I am going to your house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AD")

    Jump("loc_2B9D")

    label("loc_29B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_END)), "loc_2B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A88")

    ChrTalk(
        0xFE,
        (
            "Mr. Ian also created a draft constitution\x01",
            "I am on a very busy scene … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "You can not overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, as much as I can\x01",
            "I will be happy to help you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B06")

    label("loc_2A88")


    ChrTalk(
        0xFE,
        (
            "Just because you are busy,\x01",
            "You can not overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, as much as I can\x01",
            "I will be happy to help you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B06")

    Jump("loc_2B9D")

    label("loc_2B0B")


    ChrTalk(
        0xFE,
        (
            "If Professor Ian, stay on the second floor\x01",
            "I am working on the drafting of a constitutional draft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am busy quite busy today,\x01",
            "I also have to support it firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9D")

    Jump("loc_3599")

    label("loc_2BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3023")

    ChrTalk(
        0xFE,
        "Oh, you guys at the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Professor Ian,\x01",
            "Now I am at work on the second floor\x01",
            "I'm muffled up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FSomehow, I'm pretty busy recently\x01",
            "You seem to be playing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs it so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, actually …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regarding the example national independence\x01",
            "To the mayor to draft a constitutional draft\x01",
            "I heard that you were asked.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF2")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2CF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D18")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3E")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D64")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D64")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007FWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F\"Constitution\" … ….\x01",
            "Is not autonomous state law?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F\"Constitution\" means\x01",
            "Established basic conditions for the existence of the state\x01",
            "It becomes a fundamental law.\x02\x03",
            "#00100FGovernance rights and mechanisms of the country,\x01",
            "With the highest regulations that set out the principle\x01",
            "It will not allow interference from other countries.\x02\x03",
            "In order to have a state as a state\x01",
            "It will be absolutely indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FThe\x01",
            "It is also a difficult shimmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FBut if Professor Ian\x01",
            "I wonder if it is just right for you …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHe works in neighboring countries as well\x01",
            "If Mr. Bear beard,\x01",
            "You will do it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, surely a wonderful draft constitution\x01",
            "It should be made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then,\x01",
            "Say hello to Ian\x01",
            "Can you say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, we'll do that\x01",
            "I think that the teacher will encourage me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 1)
    Jump("loc_30A9")

    label("loc_3023")


    ChrTalk(
        0xFE,
        (
            "Mr. Ian said,\x01",
            "Draft a constitutional draft\x01",
            "It is said that the mayor asked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I surely Mr. Ian\x01",
            "A wonderful draft constitution\x01",
            "It should be made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A9")

    Jump("loc_3599")

    label("loc_30AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3128")

    ChrTalk(
        0xFE,
        (
            "If Professor Ian,\x01",
            "Today I got to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is any message,\x01",
            "I'll tell you later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_3128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_31B2")

    ChrTalk(
        0xFE,
        (
            "That, this file …\x01",
            "The place to store is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ian Professor at all,\x01",
            "Because it is Zubora like this … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3296")

    ChrTalk(
        0xFE,
        (
            "That, consultation fee for the customer earlier … …\x01",
            "It seems to be much less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Ian is a teacher,\x01",
            "You also charge fees without permission\x01",
            "Was it lost?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he is a lawyer,\x01",
            "Firmly like this\x01",
            "I have to get it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32FE")

    label("loc_3296")


    ChrTalk(
        0xFE,
        (
            "…… Ian is a teacher,\x01",
            "You also charge fees without permission\x01",
            "Was it lost?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Absolutely already, a muscle ……\x02",
    )

    CloseMessageWindow()

    label("loc_32FE")

    Jump("loc_3599")

    label("loc_3303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C3")

    ChrTalk(
        0xFE,
        (
            "Recently, Professor Ian also\x01",
            "Especially, please be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the relationship that the trade council approached\x01",
            "Further consultation is increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As much as I can,\x01",
            "I have to support my teacher.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3431")

    label("loc_33C3")


    ChrTalk(
        0xFE,
        (
            "As the trade meeting approached,\x01",
            "Recently consultations are on the rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As much as I can,\x01",
            "I have to support my teacher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3431")

    Jump("loc_3599")

    label("loc_3436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34BD")

    ChrTalk(
        0xFE,
        (
            "Recently what\x01",
            "Customers who come to consult\x01",
            "It is increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The teacher is also working clothes,\x01",
            "I have to take a rest somewhere ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3556")

    ChrTalk(
        0xFE,
        (
            "Oh, everyone at the Special Affairs Division … …\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Ian is at the desk.\x01",
            "If you have anything, please come over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3599")

    label("loc_3556")


    ChrTalk(
        0xFE,
        (
            "Mr. Ian is a desk.\x01",
            "If you have anything, please come over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3599")

    TalkEnd(0xFE)
    Return()

    # Function_4_20D3 end

    def Function_5_359D(): pass

    label("Function_5_359D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365A")

    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "To destroyed IBC\x01",
            "I was in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My workplace is gone,\x01",
            "It's completely out of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, … from now on\x01",
            "What should I do?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36D5")

    label("loc_365A")


    ChrTalk(
        0xFE,
        (
            "I was in IBC\x01",
            "My workplace is gone,\x01",
            "It's completely out of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, … from now on\x01",
            "What should I do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D5")

    TalkEnd(0xFE)
    Return()

    # Function_5_359D end

    def Function_6_36D9(): pass

    label("Function_6_36D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F2")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3804")

    ChrTalk(
        0xFE,
        (
            "He invented \"plan\" … …\x01",
            "I saw that it had been practiced long ago\x01",
            "I do not think he is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuously, our Investigation Part I\x01",
            "Grimwood Law Firm\x01",
            "I will continue searching the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … Please take care of everyone.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37FC")

    ChrTalk(
        0x10A,
        (
            "#00600FWell …\x01",
            "I am here, Emma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FC")

    SetScenarioFlags(0x0, 3)
    Jump("loc_387A")

    label("loc_3804")


    ChrTalk(
        0xFE,
        (
            "Continuously, our Investigation Part I\x01",
            "Ian Grimwood Law Firm\x01",
            "I will continue searching the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … Please take care of everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_387A")

    TalkEnd(0xFE)
    Return()

    # Function_6_36D9 end

    def Function_7_387E(): pass

    label("Function_7_387E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Currently, by the investigation division\x01",
            "Grimwood Law Firm\x01",
            "The search for houses is proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The key of the door following the second floor was also successfully unlocked.\x01",
            "…… I hope to find something clue.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_387E end

    def Function_8_392C(): pass

    label("Function_8_392C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1E")

    ChrTalk(
        0xFE,
        (
            "None of the medieval alchemy and\x01",
            "I dealt with the Zemrian civilization\x01",
            "It seems to be a document.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is quite old document, but …\x01",
            "To collect so much\x01",
            "It will take a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together Ian's suspects\x01",
            "I was planning to do \"planning\" … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3AB3")

    label("loc_3A1E")


    ChrTalk(
        0xFE,
        (
            "It is quite old document, but …\x01",
            "To collect so much\x01",
            "It will take a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together Ian's suspects\x01",
            "I was planning to do \"planning\" … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB3")

    TalkEnd(0xFE)
    Return()

    # Function_8_392C end

    def Function_9_3AB7(): pass

    label("Function_9_3AB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B87")

    ChrTalk(
        0xFE,
        (
            "From the terminal, IBC and Orkis Tower\x01",
            "Traces of frequent communication have been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Probably as a masterpiece from this place\x01",
            "President … … No, to Croix suspects\x01",
            "I guess they had instructions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C05")

    label("loc_3B87")


    ChrTalk(
        0xFE,
        (
            "Probably as a masterpiece from this place\x01",
            "To Croix suspects\x01",
            "I guess they had instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We have to prosecute carefully … …\x02",
    )

    CloseMessageWindow()

    label("loc_3C05")

    TalkEnd(0xFE)
    Return()

    # Function_9_3AB7 end

    def Function_10_3C09(): pass

    label("Function_10_3C09")

    EventBegin(0x0)
    Fade(500)
    OP_68(6060, 2320, 15510, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 7120, 1020, 15230, 270)
    SetChrPos(0x102, 7010, 1020, 16640, 270)
    SetChrPos(0x103, 7000, 1020, 13880, 315)
    SetChrPos(0x104, 8300, 1000, 14190, 270)
    SetChrPos(0xF4, 8600, 1000, 15690, 270)
    SetChrPos(0xF5, 8400, 1000, 17000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11PHello, I …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PMr. Ian … why … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FPete … ….?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0x9,
        "#6PMi, everyone …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DCC")

    ChrTalk(
        0xB,
        (
            "#5PMr. Dudley …\x01",
            "Also,\x01",
            "Is cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00603F……Ah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF4")

    label("loc_3DCC")


    ChrTalk(
        0xB,
        (
            "#5PThe Special Affairs Support Division ……\x01",
            "Is cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF4")


    ChrTalk(
        0x101,
        (
            "#11P#00001FEmma 's investigators also appreciate your work.\x01",
            "…… Is Mr. Ian's home search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYeah …… As an important reference person,\x01",
            "It is the place where I was investigating in the investigation one section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI thought it was cruel … …\x01",
            "As an official of Mr. Grimewood\x01",
            "I have him also present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PGusu …\x01",
            "No, I asked for it from myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PMr. Ian … Before I lose it,\x01",
            "Because I was saying something to worry about\x01",
            "Encourage me to make sure.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_END)), "loc_402B")

    ChrTalk(
        0x104,
        (
            "#11P#00308FOh …… cleaning the desk\x01",
            "He asked me to be asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FCertainly, at that time\x01",
            "Why did you say such a thing suddenly?\x01",
            "I was worried … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426D")

    label("loc_402B")


    ChrTalk(
        0x102,
        "#11P#00105FAnxious … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PThat \"magician\" was hanging around\x01",
            "If the emergency situation is settled ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PGo back to the office and bring your teacher's desk\x01",
            "Please clean it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005Fclean up……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYeah, I will hurry and go out first\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PNormally, I will leave the cleaning to my teacher\x01",
            "Try not to touch the desk as much as possible\x01",
            "I usually said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PFor work, assistant's servant\x01",
            "Because many things can not be shown\x01",
            "I was leaving it as it was ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FMr. Ian is … …\x01",
            "Certainly it is interesting …\x02\x03",
            "#00106FAt such timing\x01",
            "To ask for cleaning,\x01",
            "I'm not sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426D")


    ChrTalk(
        0x9,
        (
            "#6PThe answer a while ago ……\x01",
            "I got from Professor Ian 's desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P……This.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pete gave out the opened envelope.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_42FA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42FA)
    Sleep(50)

    def lambda_430A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_430A)
    Sleep(50)

    def lambda_431A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_431A)
    Sleep(50)

    def lambda_432A():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_432A)
    Sleep(50)

    def lambda_433A():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_433A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4409")

    ChrTalk(
        0x105,
        "#11P#10401FIs this … … a letter?\x02",
    )

    CloseMessageWindow()
    Jump("loc_447E")

    label("loc_4409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4443")

    ChrTalk(
        0x109,
        "#11P#10101FIs this … … a letter?\x02",
    )

    CloseMessageWindow()
    Jump("loc_447E")

    label("loc_4443")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_447E")

    ChrTalk(
        0x106,
        "#11P#10701FIs this … … a letter?\x02",
    )

    CloseMessageWindow()

    label("loc_447E")


    ChrTalk(
        0x101,
        "#11P#00001F… Can I read it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P……………… (Kokun)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    Call(0, 11)

    ChrTalk(
        0x101,
        "#11P#00006F…… Ian sensei ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4547")

    ChrTalk(
        0x101,
        "#11P#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_45C6")

    label("loc_4547")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4589")

    ChrTalk(
        0x109,
        "#11P#10108F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_45C6")

    label("loc_4589")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45C6")

    ChrTalk(
        0x105,
        "#11P#10408F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_45C6")


    ChrTalk(
        0xB,
        (
            "#5P…… On his desk,\x01",
            "Several other documents\x01",
            "It was kept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI am currently consulting with my office\x01",
            "Future response to the client was noted\x01",
            "A huge memo ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnd Pete's boy's\x01",
            "To arrange a guardian,\x01",
            "Procedural documents such as parental authority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P…… Uoo, Professor Ian … …\x01",
            "Why is this …?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46EE():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_46EE)
    Sleep(50)

    def lambda_46FE():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46FE)
    Sleep(50)

    def lambda_470E():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_470E)
    Sleep(50)

    def lambda_471E():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_471E)
    Sleep(50)

    def lambda_472E():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_472E)
    Sleep(50)

    def lambda_473E():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_473E)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#6PForget that the teacher became indebted to,\x01",
            "Why can I be happy?\x01",
            "There is not it … ___ ___ 0\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00106FPete … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#00208F…… Ian is a big fool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00306FOh, I can not tell anything about people ….\x01",
            "The one who left it is such a letter\x01",
            "I guess I can never be convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F… That is right.\x02\x03",
            "#00008FPete, we are going now\x01",
            "I will head to Mr. Ian.\x02\x03",
            "#00001FWe must be sure to grab the truth there ……\x01",
            "I will bring back the teachers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PMi, everyone …\x01",
            "…… Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6Pplease……\x01",
            "I would like to ask Professor Ian.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    SetScenarioFlags(0x1BD, 6)
    EventEnd(0x5)
    Return()

    # Function_10_3C09 end

    def Function_11_49CD(): pass

    label("Function_11_49CD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 40, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── To Pete.\x01",
            "First of all, leave this letter and put your ex\x01",
            "I want you to apologize for sudden departure.\x02\x01",
            "Once I took you as a guardian,\x01",
            "Since I started to work in my office\x01",
            "I had my eyes shining every day.\x02\x01",
            "From that day of destiny, I was dominated by lamentation and sadness,\x01",
            "It was supposed to be only for achieving the plan\x01",
            "My life …… I really appreciate it if I am missing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 40, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because of you,\x01",
            "For a while, I was also worried … …\x02\x01",
            "Again the plan can not be stopped.\x01",
            "You can not go back to me.\x02\x01",
            "Pete, whatever ……\x01",
            "I want you to forget about me and be happy.\x02\x01",
            "Wise wishes to be a fine adult\x01",
            "I pray to the goddess from a distant place.\x02\x01",
            "── Ian Grimwood\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_49CD end

    def Function_12_4C92(): pass

    label("Function_12_4C92")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_68(4790, 1920, 14330, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 4830, 1020, 12570, 0)
    SetChrPos(0x102, 3990, 1020, 12720, 0)
    SetChrPos(0x109, 5650, 1000, 11990, 0)
    SetChrPos(0x105, 2910, 1000, 11990, 0)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5P#02205FOh, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see, Mr. Ian.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FHaha, it's been a long time.\x01",
            "Once the activity has been paused\x01",
            "I was listening … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I resumed work.\x01",
            "looking forward to contact with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FHehuu, I see.\x01",
            "A new member also entered,\x01",
            "I was told that my mind was overturned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FCertainly, famous\x01",
            "Was it \"bear beard teacher\"?\x02\x03",
            "#10304FHuh, I'm counting on you from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02205FOh, thanks for your kindness.\x02\x03",
            "#02203F……Uh,\x01",
            "Where did you do your business card ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F74")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F9A")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FC0")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4FC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FE6")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4FE6")

    Sleep(1000)
    TurnDirection(0x109, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10106FWow, Wazi ……\x01",
            "Against superiors\x01",
            "There will be courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FMr. Ian is already\x01",
            "Nori is too good.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02202FWell, no no …\x01",
            "In a relationship of people and people,\x01",
            "Self-introduction is very important.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "── Kohon, then\x01",
            "Shall I try again?\x02\x03",
            "My name is Ian Grimwood.\x01",
            "The director of this law firm\x01",
            "It is a lawyer who has been made to do.\x02\x03",
            "Managers of the Special Affairs Support Division,\x01",
            "I'm begging to ask you again.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x109,
        (
            "#10100FLikewise,\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI also have something to discuss with you variously\x01",
            "There may be.\x02\x03",
            "#00004FAt that time, please do not hesitate to us\x01",
            "Please lend me your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FOh, anytime\x01",
            "Please come.\x02\x03",
            "Anything as long as I am OK\x01",
            "I'm going to have a consultation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x12C, 4)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4C92 end

    def Function_13_5315(): pass

    label("Function_13_5315")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(-940, 1300, -180, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -2710, 0, -490, 90)
    SetChrPos(0x102, -2710, 0, -490, 90)
    SetChrPos(0x103, -2710, 0, -490, 90)
    SetChrPos(0x104, -2710, 0, -490, 90)
    SetChrPos(0x109, -2710, 0, -490, 90)
    SetChrPos(0x105, -2710, 0, -490, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    OP_68(2570, 1300, 1440, 5000)
    MoveCamera(65, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20900, 5000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    ChrTalk(
        0x8,
        "#02205FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FIan-sensei!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FWas good……\x01",
            "Did you stay in the office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FOh, now it's just\x01",
            "It's a place to take a rest … …\x02\x03",
            "#02201F…… Hmm, something to me\x01",
            "Is there also a consultation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fdo you understand……\x01",
            "As expected it is a teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FHuhu, the face of the person with the request is\x01",
            "That's hundreds and thousands\x01",
            "I am watching it.\x02\x03",
            "#02200FWhich, please sit there.\x01",
            "I am also a busy body,\x01",
            "Let's talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FExcuse us, thank you\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd investigated the day before.\x01",
            "Minnes' profile and action ……\x02\x03",
            "And it turned out today\x01",
            "The fact that he was collecting the land rights book\x01",
            "I told Ian.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_68(5320, 500, 6810, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21670, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2310, 200, 5400, 90)
    SetChrPos(0x102, 2310, 200, 4570, 90)
    SetChrPos(0x103, 2260, 200, 6070, 90)
    SetChrPos(0x104, 4530, 200, 7520, 180)
    SetChrPos(0x109, 3780, 200, 7520, 180)
    SetChrPos(0x105, 5160, 200, 7520, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#02200FHmm … I see.\x01",
            "I understood most of the circumstances.\x02\x03",
            "Originally this is my case\x01",
            "I'd like to take over … …\x02\x03",
            "#02203FAs you guys know,\x01",
            "Now I am preparing a draft constitution\x01",
            "There is an important work.\x02\x03",
            "#02203FI'm sorry, I underwrite it\x01",
            "I can hardly make time to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIt's fine, it's not a problem\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FIn this way consultation\x01",
            "Even if you just get on board\x01",
            "I am saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FI'm sorry ….\x01",
            "Instead, now, as much as possible\x01",
            "I will give you advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThat's fine, thank you\x02\x03",
            "#00001FSo what exactly do you think?\x02\x03",
            "Mr. Minnes' actions so far …\x01",
            "From there, signs of some kind of crime\x01",
            "Can you read it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#02203FI've heard about him once I think\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00309FOh seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FOh … from the acquaintance of the empire\x01",
            "In the case that I got it as reference material\x01",
            "There are something very similar.\x02\x03",
            "However, if it is a totally similar incident\x01",
            "I can not conclude, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Anyway now,\x01",
            "The beginning of the investigation\x01",
            "It is a wanted situation.\x02\x03",
            "#00003FAbout that fish,\x01",
            "Could you please tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200F… … Well, it will be nice.\x01",
            "It is a request of you who are not even others.\x02\x03",
            "#02203FSo then\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x8,
        (
            "#02203F── Several years ago …\x01",
            "To the baroner who has the Eleventh Empire,\x01",
            "A man came.\x02\x03",
            "#02201FThe man's name is \"Lidner\" …\x01",
            "I work for a famous sake brewing company\x01",
            "He is a man calling for a fantastic businessman.\x02\x03",
            "And Lidner,\x01",
            "I bought a profitable story in the baron.\x02\x03",
            "For generations, in the baron's territory\x01",
            "A vast wheat field inherited … …\x01",
            "It is the entrepreneurship of the Sake brewery company that used it.\x02\x03",
            "#02203FBuilding a beer factory in the territory,\x01",
            "Leave that management to a baron … …\x01",
            "It seems that it was almost such contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F! That sounds like\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FGiggle\x01",
            "To the story that I heard somewhere\x01",
            "It looks like a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F── The Baron accepted his profitable story,\x01",
            "Lidner brought it\x01",
            "I signed the contract.\x02\x03",
            "#02200FAnd the whole area of the wheat field was nominated for management,\x01",
            "And some of the land is nominated for factory construction\x01",
            "It was temporarily transferred to Lidner.\x02\x03",
            "In addition, as the capital of the company\x01",
            "A part of the property of the baroness was turned,\x01",
            "Preparation for entrepreneurs steadily and steadily … …\x02\x03",
            "#02203FBut … Lidner,\x01",
            "Part of the property's assets and assets,\x01",
            "I disappeared while holding them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FAh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FSuddenly lost contact with Lidner,\x01",
            "It seems that the baroners have gone impatient … …\x02\x03",
            "At that time a serious situation\x01",
            "I was not conscious of progressing.\x02\x03",
            "#02201FWell, Liverner\x01",
            "The right letter of the land which received the deposit\x01",
            "It sold it to a third party.\x02\x03",
            "It was a prime property for some nobles to build holliday homs\x02\x03",
            "#02203F─ ─ after all, to the baroness\x01",
            "Only a huge debt left … …\x01",
            "I will soon give up all the territory.\x02\x03",
            "As a result of the loss of the territory, the rank is also deprived of …\x01",
            "After that, they became irreconciled … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhat is it …?\x01",
            "It is a terrible story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FFor someone to be so selfish…\x02\x03",
            "It's so aggrivating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F── This is what I heard about you\x01",
            "It is the first incident I came up with.\x02\x03",
            "You win credit by falsifying your identity,\x01",
            "Ultimately deceive the enormous wealth … …\x02\x03",
            "#02201FThe so-called \"fraud\"\x01",
            "It can be said that it is one of the signatures.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FFraud!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIn other words, the person named Mininness\x01",
            "It is not an officer of Quincy Company … …\x02\x03",
            "#00200FAt least with high liklihood fraudlent\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FWell … I can not conclude\x01",
            "The possibility is high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIn fact, the common part is\x01",
            "I could confirm a couple of … …\x02\x03",
            "#00001FFor now this matter\x01",
            "Investigate as a fraud case\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThen …\x01",
            "Naturally, the part to be investigated\x01",
            "You see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, yes.\x01",
            "The man named Minnes is roughly divided into two,\x01",
            "There is a questionable part.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FFirst of all, that plan …\x01",
            "\"Armorica · Honey Company\"\x01",
            "Whether it really exists or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FRegarding that,\x01",
            "If you know the movement of Mira\x01",
            "You may be caught.\x02\x03",
            "#10300FBefore starting a business with Crossbell,\x01",
            "The need to receive loans with IBC\x01",
            "There should be.\x02\x03",
            "If you have a lie in your plan\x01",
            "There is evidence in IBC\x01",
            "Is not the possibility high?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnd another thing, of course, I want to check\x01",
            "Minnes really is \"Quincy Company\"\x01",
            "It is whether it is an officer or not.\x02\x03",
            "#00001F…… This is a foreign company,\x01",
            "It seems to be a pain to take the back … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FIt may not be very useful\x01",
            "I do not think so.\x02\x03",
            "#00100FIf it is to my house, perhaps\x01",
            "There may be something to be helpful.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)

    ChrTalk(
        0x103,
        "#00205FA leger??\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FActually, in my house Quincy's company\x01",
            "I have a pamphlet.\x02\x03",
            "In that case, the company's overview and so on\x01",
            "Because it was written, maybe\x01",
            "It might be helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FQuincy's brochure ……\x01",
            "Why did you have a girlfriend?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00113FEr, actually, I …\x01",
            "I like quite a lot of sweets, but ….\x02\x03",
            "#00100FAbout this time, about Quincy\x01",
            "I was very interested,\x01",
            "You got ordered the brochure.\x02\x03",
            "My room's home\x01",
            "It should be on a bookshelf, but …\x02\x03",
            "#00106F…… You can not do it.\x01",
            "I do not have such a pamphlet for drifting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FNo, actually it could mean something\x02\x03",
            "#02200FIf it becomes official document of the company,\x01",
            "Somehow, with the words of a man named Minnes\x01",
            "Contradictory content may be found.\x02\x03",
            "It might be good to check it out just in case\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FI agree……\x01",
            "I will go to Elly 's house.\x02\x03",
            "#00000F…… Ian, precious story\x01",
            "Thank you very much.\x02\x03",
            "Thanks to the investigation policy\x01",
            "It looks like it gathers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FWell, a little\x01",
            "It seems to be useful, nothing more.\x02\x03",
            "… … certainly, you guys are now\x01",
            "Based on your house in Harold\x01",
            "You were investigating, were not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FWhat, this incident ……\x01",
            "As far as time permits\x01",
            "I was thinking of having you help me.\x02\x03",
            "#02203FBecause I am a busy body,\x01",
            "Although it will not be useful to that extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FNo, hey … …\x01",
            "It is encouraging!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FIf you have a professional\x01",
            "It is hundred power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FHuhu, I will face it later\x01",
            "You guys also investigate\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we'll do that\x02\x03",
            "#00003F……Well then,\x01",
            "Let's assume that it will hit the investigation immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FInvestigate cash flow with IBC,\x01",
            "Take the plan of Minnes' plan … …\x02\x03",
            "And for reference level\x01",
            "Examining materials at McDaill's residence,\x01",
            "Look for discrepancies with his words … …\x02\x03",
            "So there are two places to check out\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FI understand.\x01",
            "Let's give you some evidence!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x1)
    SetScenarioFlags(0x177, 3)
    ClearMapFlags(0x10000000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    SetChrPos(0x0, 2400, 30, 1120, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_13_5315 end

    def Function_14_7186(): pass

    label("Function_14_7186")


    def lambda_718B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_718B)

    def lambda_719C():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_719C)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3290, 30, 900, 2000, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_14_7186 end

    def Function_15_71D1(): pass

    label("Function_15_71D1")


    def lambda_71D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_71D6)

    def lambda_71E7():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71E7)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 2330, 30, 1420, 2000, 0x0)
    TurnDirection(0x102, 0x8, 500)
    Return()

    # Function_15_71D1 end

    def Function_16_721C(): pass

    label("Function_16_721C")


    def lambda_7221():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7221)

    def lambda_7232():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7232)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 3210, 30, -360, 2000, 0x0)
    TurnDirection(0x103, 0x8, 500)
    Return()

    # Function_16_721C end

    def Function_17_7267(): pass

    label("Function_17_7267")


    def lambda_726C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_726C)

    def lambda_727D():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_727D)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2300, 30, 80, 2000, 0x0)
    TurnDirection(0x104, 0x8, 500)
    Return()

    # Function_17_7267 end

    def Function_18_72B2(): pass

    label("Function_18_72B2")


    def lambda_72B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_72B7)

    def lambda_72C8():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72C8)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 1960, 30, -1080, 2000, 0x0)
    TurnDirection(0x109, 0x8, 500)
    Return()

    # Function_18_72B2 end

    def Function_19_72FD(): pass

    label("Function_19_72FD")


    def lambda_7302():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7302)

    def lambda_7313():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7313)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1200, 0, 350, 2000, 0x0)
    TurnDirection(0x105, 0x8, 500)
    Return()

    # Function_19_72FD end

    def Function_20_7348(): pass

    label("Function_20_7348")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_20_7348 end

    SaveToFile()

Try(main)
