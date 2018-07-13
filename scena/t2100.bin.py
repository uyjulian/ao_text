from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 1, 0, 2],
    )

    BuildStringList((
        "t2100",                  # 0
        "Broude ",                # 1
        "Dahlia",                 # 2
        "Chiruru",                # 3
        "帝国軍戦車",             # 4
        "帝国軍戦車",             # 5
        "帝国軍戦車",             # 6
        "帝国軍戦車",             # 7
        "帝国軍戦車",             # 8
        "SE制御",                 # 9
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch20500.itc",                   # 02
    ))

    DeclNpc(4294953467, 10000,   4294964336, 270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294953236, 10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294948696, 5000,    4294949946, 270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(1500,    5050,    4294947296, 1200,    1500,    6050,    4294947296, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_33D",          # 02, 2
        "Function_3_47A",          # 03, 3
        "Function_4_5CC",          # 04, 4
        "Function_5_1012",         # 05, 5
        "Function_6_1E10",         # 06, 6
        "Function_7_1E71",         # 07, 7
        "Function_8_2242",         # 08, 8
        "Function_9_2252",         # 09, 9
        "Function_10_2262",        # 0A, 10
        "Function_11_227F",        # 0B, 11
        "Function_12_229F",        # 0C, 12
        "Function_13_22BF",        # 0D, 13
        "Function_14_22DF",        # 0E, 14
        "Function_15_22FF",        # 0F, 15
        "Function_16_234A",        # 10, 16
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_316")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D0")
    Jump("loc_316")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DE")
    Jump("loc_316")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EC")
    Jump("loc_316")

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FA")
    Jump("loc_316")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_308")
    Jump("loc_316")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_316")
    ClearChrFlags(0xA, 0x80)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_32D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_33C")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_33C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)

    label("loc_33C")

    Return()

    # Function_1_2B4 end

    def Function_2_33D(): pass

    label("Function_2_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_357")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_385")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_385")

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_385")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_409")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xE6, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_420")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_420")

    label("loc_420")

    SetMapObjFrame(0xFF, "open", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475")
    OP_70(0x2, 0x0)
    Jump("loc_479")

    label("loc_475")

    OP_70(0x2, 0x1E)

    label("loc_479")

    Return()

    # Function_2_33D end

    def Function_3_47A(): pass

    label("Function_3_47A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x2D, 1)"), scpexpr(EXPR_END)), "loc_4FF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_571")

    label("loc_4FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_571")

    Jump("loc_5C0")

    label("loc_576")

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

    label("loc_5C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47A end

    def Function_4_5CC(): pass

    label("Function_4_5CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_703")

    ChrTalk(
        0xFE,
        (
            "It was the Empire who employed the\x01",
            "jaeger corps who attacked Crossbell City...\x01",
            "There's such a rumor going around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter the circumstances, I won't\x01",
            "forgive those who killed my CGF comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the Empire wants to play like that,\x01",
            "I too will strengthen my resolve.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7B6")

    label("loc_703")


    ChrTalk(
        0xFE,
        (
            "Rumor goes that large-scale\x01",
            "practices are being performed\x01",
            "in the Empire region, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Very good. \x01",
            "If the Empire wants to do those,\x01",
            "I too will strengthen my resolve.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B6")

    Jump("loc_100E")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_889")

    ChrTalk(
        0xFE,
        (
            "Even if it's just a drizzle, as you can\x01",
            "expect, your field of vision worsens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that there's still eyewitness intel\x01",
            "about Cryptid appearances too, so...\x01",
            "I have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100E")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987")

    ChrTalk(
        0xFE,
        (
            "Man, lately I've been so busy\x01",
            "that I don't even have time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But the Commander, 2nd Lt. and the\x01",
            "others are probably having it harder than us.\x01",
            "I greatly admire that toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I too must do my best more.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A1B")

    label("loc_987")


    ChrTalk(
        0xFE,
        (
            "The Commander, 2nd Lt. and the others\x01",
            "are probably having it harder than us.\x01",
            "I greatly admire that toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I too must do my best more.\x02",
    )

    CloseMessageWindow()

    label("loc_A1B")

    Jump("loc_100E")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B15")

    ChrTalk(
        0xFE,
        (
            "After the mayor's independence proposal,\x01",
            "the Empire and Republic reached the\x01",
            "point to openly apply pressures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Frankly, this state of tension stomachaches me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope to see some kind\x01",
            "of settlement early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B7C")

    label("loc_B15")


    ChrTalk(
        0xFE,
        "Frankly, this state of tension stomachaches me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope to see some kind\x01",
            "of settlement early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7C")

    Jump("loc_100E")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C43")

    ChrTalk(
        0xFE,
        (
            "According to intel, it's likely\x01",
            "that terrorists will infiltrate\x01",
            "from the Empire region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can expect, I'm nervous.\x01",
            "I hope the day will end\x01",
            "with nothing happening...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100E")

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDB")

    ChrTalk(
        0xFE,
        (
            "Burrell who is at Tangram\x01",
            "Gate is my best friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's been worked hard every day by\x01",
            "the Vice Commander who is extremely strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, compared to an incompetent superior\x01",
            "officer, it's something most people would love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya is pretty strict too,\x01",
            "but I don't think not even in the slightest\x01",
            "that it was better with the former Commander.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EBA")

    label("loc_DDB")


    ChrTalk(
        0xFE,
        (
            "Compared to an incompetent superior officer, \x01",
            "it's something most people would love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya is pretty strict too,\x01",
            "but I don't think not even in the slightest\x01",
            "that it was better with the former Commander.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBA")

    Jump("loc_100E")

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")

    ChrTalk(
        0xFE,
        (
            "With the coming of Commander Sonya,\x01",
            "even security at Bellguard Gate\x01",
            "got motivated all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A capable superior officer\x01",
            "is really a blessing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_100E")

    label("loc_F78")


    ChrTalk(
        0xFE,
        (
            "At the time of the former Commander,\x01",
            "work had never been done with such\x01",
            "a satisfying mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A capable superior officer\x01",
            "is really a blessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100E")

    TalkEnd(0xFE)
    Return()

    # Function_4_5CC end

    def Function_5_1012(): pass

    label("Function_5_1012")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119C")

    ChrTalk(
        0xFE,
        (
            "The situation, with the state independence trend\x01",
            "rising, is a state of tension that can be said to\x01",
            "be equal to before the Non-Aggression Pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In case a confrontation with the Empire\x01",
            "reached its limit, there're enough possibilities\x01",
            "for those "Railway Cannons" to appear again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected...can't a conflict with\x01",
            "the Empire and Republic be avoided?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12A4")

    label("loc_119C")


    ChrTalk(
        0xFE,
        (
            "...Recently, even Commander Sonya\x01",
            "seems often absorbed in thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that Mayor Dieter and\x01",
            "Chairman MacDowell are talking\x01",
            "together about the CGF reorganization...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Including the two major powers opposition,\x01",
            "there're a huge heap of problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A4")

    Jump("loc_1E0C")

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_148D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B9")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment accident...\x01",
            "It was really awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that giant monster\x01",
            "was really the culprit...\x01",
            "I'm worried if it won't happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, I'd like something to be done\x01",
            "about that monster search and extermination.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1488")

    label("loc_13B9")


    ChrTalk(
        0xFE,
        (
            "Thinking about the transcontinental railway position,\x01",
            "recurrence prevention is a matter of maximum priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, I'd like something to be done\x01",
            "about that monster search and extermination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1488")

    Jump("loc_1E0C")

    label("loc_148D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1784")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(
        0xFE,
        (
            "I got this book from Mr.\x01",
            "Broude just to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it was very interesting,\x01",
            "please read it too, if you like.\x01\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 7)
    Jump("loc_177F")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A9")

    ChrTalk(
        0xFE,
        (
            "Many kinds of weapons are deployed\x01",
            "at "Garrelia Fortress", located inside\x01",
            "that bedrock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the past, when the state of tension was at\x01",
            "its limit, even the "Railway Cannons" were\x01",
            "mobilized during large-scale practices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this state of tension\x01",
            "doesn't invite such a situation.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_177F")

    label("loc_16A9")


    ChrTalk(
        0xFE,
        (
            "In the past, when the state of tension was at\x01",
            "its limit, even the "Railway Cannons" were\x01",
            "mobilized during practices held in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this state of tension\x01",
            "doesn't invite such a situation.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177F")

    Jump("loc_1E0C")

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1862")

    ChrTalk(
        0xFE,
        (
            "I too was shocked about\x01",
            "that independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However... It could be something \x01",
            "necessary in order to protect \x01",
            "Crossbell from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it realizes in a way or another.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18F0")

    label("loc_1862")


    ChrTalk(
        0xFE,
        (
            "I too was shocked about\x01",
            "that independence proposal, but...\x01",
            "It could be something necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it realizes in a way or another.\x02",
    )

    CloseMessageWindow()

    label("loc_18F0")

    Jump("loc_1E0C")

    label("loc_18F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7E")

    ChrTalk(
        0xFE,
        (
            "We received terrorists intel\x01",
            "and we're making our best effort\x01",
            "about security nearby the national border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To defend against invasions from airspace,\x01",
            "we're using a special facility that was set up\x01",
            "nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition, if we had anti-aircraft cannons like\x01",
            "those of the army things could be perfect, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's useless asking\x01",
            "for the impossible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B3E")

    label("loc_1A7E")


    ChrTalk(
        0xFE,
        (
            "If we had anti-aircraft cannons like those of the\x01",
            "army we could deal with an invasion from the air\x01",
            "and things would be perfect, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's useless asking\x01",
            "for the impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3E")

    Jump("loc_1E0C")

    label("loc_1B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C85")

    ChrTalk(
        0xFE,
        (
            "This morning I happened to see a crimson\x01",
            "orbal train passing under the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was the Imperial government private train...\x01",
            "The "Blood and Iron Chancellor" and Crown\x01",
            "Prince Olivert were probably riding in that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Trade Conference has finally started...\x01",
            "I have to stay sharp.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D1E")

    label("loc_1C85")


    ChrTalk(
        0xFE,
        (
            "This morning I happened to see a crimson\x01",
            "orbal train passing under the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Trade Conference has finally started...\x01",
            "I have to stay sharp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1E")

    Jump("loc_1E0C")

    label("loc_1D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E0C")

    ChrTalk(
        0xFE,
        (
            "With the Trade Conference getting closer,\x01",
            "even our responsibilities as CGF\x01",
            "have become furthermore bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even to protect every countries'\x01",
            "VIPs coming to Crossbell...\x01",
            "We must make national border security strict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0C")

    TalkEnd(0xFE)
    Return()

    # Function_5_1012 end

    def Function_6_1E10(): pass

    label("Function_6_1E10")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This valley is really great...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you fall, you won't survive.\x01",
            "How thrilling...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1E10 end

    def Function_7_1E71(): pass

    label("Function_7_1E71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_04a.pmf", 0x22C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_F3(200000)
    LoadEffect(0x0, "event/ev15060.eff")
    SoundLoad(825)
    SoundLoad(923)
    OP_68(-66820, 1000, -14120, 0)
    MoveCamera(307, 12, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(75270, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x22C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-69430, 11500, -13600, 0)
    MoveCamera(297, 8, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(65000, 0)
    SetCameraDistance(71000, 5500)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -122940, 200, -1170, 0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xB)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -139790, 200, -2770, 0)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0xC)
    OP_93(0xC, 0x5A, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -156790, 200, 2770, 0)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xD)
    OP_93(0xD, 0x5A, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -177000, 200, 1140, 0)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0xE)
    OP_93(0xE, 0x5A, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -198000, 200, -1150, 0)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0xF)
    OP_93(0xF, 0x5A, 0x0)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac66", 0x0, 0)
    OP_6F(0x79)
    BeginChrThread(0xB, 0, 0, 10)
    BeginChrThread(0xC, 0, 0, 11)
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 14)
    BeginChrThread(0x10, 1, 0, 15)
    OP_68(-91380, 15200, 2180, 0)
    MoveCamera(331, 11, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(83380, 0)
    Fade(500)
    OP_0D()
    OP_68(-90600, 7400, 2210, 7500)
    MoveCamera(331, 5, 0, 7500)
    OP_6E(450, 7500)
    SetCameraDistance(77550, 7200)
    OP_6F(0x79)
    SetCameraDistance(40000, 5000)
    OP_68(-85000, 4700, 1860, 8200)
    Sleep(4500)
    MoveCamera(317, -1, 0, 3500)
    OP_6F(0x79)
    OP_68(-32549, 4800, -7710, 18500)
    SetCameraDistance(42000, 4000)
    Sleep(6000)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    OP_68(-54250, 2570, -1160, 0)
    MoveCamera(270, 10, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(14060, 0)
    Fade(500)
    BeginChrThread(0xB, 1, 0, 9)
    BeginChrThread(0xC, 1, 0, 9)
    BeginChrThread(0xD, 1, 0, 9)
    BeginChrThread(0xE, 1, 0, 9)
    BeginChrThread(0xF, 1, 0, 9)
    OP_68(-43550, 2570, -690, 8000)
    MoveCamera(266, 7, 0, 8000)
    OP_6E(450, 8000)
    SetCameraDistance(17940, 8000)
    Sleep(1500)
    OP_75(0x6, 0x2, 0x2BC)
    Sleep(3500)
    OP_75(0x7, 0x2, 0x2BC)
    Sleep(2000)
    StopSound(923, 1000, 60)
    StopSound(825, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1E71 end

    def Function_8_2242(): pass

    label("Function_8_2242")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0xBB8, 0x0)
    Return()

    # Function_8_2242 end

    def Function_9_2252(): pass

    label("Function_9_2252")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x7D0, 0x0)
    Return()

    # Function_9_2252 end

    def Function_10_2262(): pass

    label("Function_10_2262")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)

    label("loc_226B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227E")
    Sleep(5000)
    Jump("loc_226B")

    label("loc_227E")

    Return()

    # Function_10_2262 end

    def Function_11_227F(): pass

    label("Function_11_227F")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(1200)

    label("loc_228B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_229E")
    Sleep(5000)
    Jump("loc_228B")

    label("loc_229E")

    Return()

    # Function_11_227F end

    def Function_12_229F(): pass

    label("Function_12_229F")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(2400)

    label("loc_22AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22BE")
    Sleep(5000)
    Jump("loc_22AB")

    label("loc_22BE")

    Return()

    # Function_12_229F end

    def Function_13_22BF(): pass

    label("Function_13_22BF")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(3600)

    label("loc_22CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22DE")
    Sleep(5000)
    Jump("loc_22CB")

    label("loc_22DE")

    Return()

    # Function_13_22BF end

    def Function_14_22DF(): pass

    label("Function_14_22DF")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(4800)

    label("loc_22EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22FE")
    Sleep(5000)
    Jump("loc_22EB")

    label("loc_22FE")

    Return()

    # Function_14_22DF end

    def Function_15_22FF(): pass

    label("Function_15_22FF")

    Sound(923, 2, 10, 0)
    Sound(825, 2, 20, 0)
    Sleep(1500)
    OP_25(0x39B, 0x14)
    OP_25(0x339, 0x1E)
    Sleep(1000)
    OP_25(0x39B, 0x1E)
    OP_25(0x339, 0x28)
    Sleep(1000)
    OP_25(0x39B, 0x28)
    OP_25(0x339, 0x32)
    Sleep(500)
    OP_25(0x39B, 0x32)
    OP_25(0x339, 0x3C)
    Sleep(500)
    OP_25(0x39B, 0x3C)
    OP_25(0x339, 0x46)
    Sleep(500)
    OP_25(0x339, 0x50)
    Return()

    # Function_15_22FF end

    def Function_16_234A(): pass

    label("Function_16_234A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-100000, 0, 0, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(80000, 0)
    FadeToBright(1000, 0)
    OP_68(-100000, 10000, 0, 7000)
    Sleep(5000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_234A end

    SaveToFile()

Try(main)
