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
        "Function_4_5CB",          # 04, 4
        "Function_5_FB6",          # 05, 5
        "Function_6_1CD5",         # 06, 6
        "Function_7_1D36",         # 07, 7
        "Function_8_2107",         # 08, 8
        "Function_9_2117",         # 09, 9
        "Function_10_2127",        # 0A, 10
        "Function_11_2144",        # 0B, 11
        "Function_12_2164",        # 0C, 12
        "Function_13_2184",        # 0D, 13
        "Function_14_21A4",        # 0E, 14
        "Function_15_21C4",        # 0F, 15
        "Function_16_220F",        # 10, 16
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_571")

    Jump("loc_5BF")

    label("loc_576")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_5BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47A end

    def Function_4_5CB(): pass

    label("Function_4_5CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")

    ChrTalk(
        0xFE,
        (
            "The Empire employed the jaeger corps\x01",
            "that attacked Crossbell City... There's\x01",
            "a rumor like that going around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter the circumstances,\x01",
            "I won't forgive those who\x01",
            "killed my CGF comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that's how the Empire wants\x01",
            "to play it, I will strengthen\x01",
            "my resolve as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7B0")

    label("loc_705")


    ChrTalk(
        0xFE,
        (
            "Rumor goes that large-\x01",
            "scale exercises are being\x01",
            "held in the Empire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Good then. If that's what\x01",
            "the Empire wants, I will\x01",
            "strengthen my resolve as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B0")

    Jump("loc_FB2")

    label("loc_7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_86F")

    ChrTalk(
        0xFE,
        (
            "Even if it's just drizzling,\x01",
            "as expected, your field of\x01",
            "vision worsens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that there's still\x01",
            "sightings of Cryptid appearances\x01",
            "too... I have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(
        0xFE,
        (
            "Man, I've been so busy\x01",
            "lately that I don't even\x01",
            "have time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But the Commander, 2nd Lt. and the\x01",
            "others probably have it even harder than\x01",
            "we do. I greatly admire their toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to do better too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9F9")

    label("loc_96D")


    ChrTalk(
        0xFE,
        (
            "The Commander, 2nd Lt. and the others\x01",
            "probably have it harder than us. I\x01",
            "greatly admire their toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to do better too.\x02",
    )

    CloseMessageWindow()

    label("loc_9F9")

    Jump("loc_FB2")

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF9")

    ChrTalk(
        0xFE,
        (
            "After the mayor's independence proposal,\x01",
            "the Empire and Republic reached the\x01",
            "point of openly applying pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly, this state of\x01",
            "tension makes me sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope to see some kind\x01",
            "of settlement before\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B64")

    label("loc_AF9")


    ChrTalk(
        0xFE,
        (
            "Frankly, this state of\x01",
            "tension makes me sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope to see some kind\x01",
            "of settlement before\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B64")

    Jump("loc_FB2")

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C21")

    ChrTalk(
        0xFE,
        (
            "According to intel, it's\x01",
            "likely terrorists will\x01",
            "infiltrate from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might expect, I'm\x01",
            "nervous. I hope the day will\x01",
            "end with nothing happening...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(
        0xFE,
        (
            "Burrell at Tangram Gate\x01",
            "is my best friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's worked hard every\x01",
            "day by the vice commander who\x01",
            "is extremely strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, compared to an\x01",
            "incompetent superior officer, it's\x01",
            "something most people would love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya is pretty strict too,\x01",
            "but I never thought for a second that\x01",
            "she's worse than the former commander.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E71")

    label("loc_DA0")


    ChrTalk(
        0xFE,
        (
            "Compared to an incompetent\x01",
            "superior officer, it's something\x01",
            "most people would love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya is pretty strict too,\x01",
            "but I never thought for a second that\x01",
            "she's worse than the former commander.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E71")

    Jump("loc_FB2")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F23")

    ChrTalk(
        0xFE,
        (
            "When Commander Sonya arrived,\x01",
            "security at Bellguard Gate\x01",
            "got inspired all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A capable superior\x01",
            "officer is really a\x01",
            "blessing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FB2")

    label("loc_F23")


    ChrTalk(
        0xFE,
        (
            "During the former commander's\x01",
            "tenure, work was never been\x01",
            "done in such a good mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A capable superior\x01",
            "officer is really a\x01",
            "blessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB2")

    TalkEnd(0xFE)
    Return()

    # Function_4_5CB end

    def Function_5_FB6(): pass

    label("Function_5_FB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_120C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(
        0xFE,
        (
            "With tensions over state independence rising,\x01",
            "the current situation could be said to be\x01",
            "equal to that before non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If tensions with the Empire reached\x01",
            "their limit, it's possible those\x01",
            ""Railway Cannons" could appear again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it... Can't\x01",
            "conflicts with the Empire\x01",
            "and Republic be avoided?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1207")

    label("loc_1116")


    ChrTalk(
        0xFE,
        (
            "...Even Commander Sonya\x01",
            "seems lost in thought\x01",
            "often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Mayor Dieter and\x01",
            "Chairman MacDowell are talking\x01",
            "about reorganizing the CGF...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you include opposing the\x01",
            "major powers, we've got a\x01",
            "huge heap of problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1207")

    Jump("loc_1CD1")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1302")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment\x01",
            "accident... It was\x01",
            "really awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that giant monster was\x01",
            "really the culprit... I'm\x01",
            "worried it might happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like\x01",
            "that monster to be found\x01",
            "and exterminated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13BF")

    label("loc_1302")


    ChrTalk(
        0xFE,
        (
            "Thinking about the transcontinental\x01",
            "railway's position, preventing recurrence\x01",
            "needs to be given maximum priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like\x01",
            "that monster to be found\x01",
            "and exterminated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BF")

    Jump("loc_1CD1")

    label("loc_13C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149B")

    ChrTalk(
        0xFE,
        (
            "I got this book from\x01",
            "Broude to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was really interesting.\x01",
            "Please read it yourselves,\x01",
            "if you like.\x02",
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
    Jump("loc_16A5")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D9")

    ChrTalk(
        0xFE,
        (
            "Many kinds of weapons are\x01",
            "deployed at Garrelia Fortress,\x01",
            "located inside that bedrock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the past, when the state of tension were\x01",
            "at their limit, even the "Railway Cannons"\x01",
            "were mobilized during large-scale exercises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this state\x01",
            "of tension doesn't\x01",
            "invite such a situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_16A5")

    label("loc_15D9")


    ChrTalk(
        0xFE,
        (
            "In the past, when tensions were at their\x01",
            "limit, even the "Railway Cannons" were\x01",
            "mobilized during exercises held in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this state\x01",
            "of tension doesn't\x01",
            "invite such a situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    Jump("loc_1CD1")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1771")

    ChrTalk(
        0xFE,
        (
            "I was shocked at that\x01",
            "independence proposal\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However... It might be\x01",
            "necessary to protect\x01",
            "Crossbell going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it's realized\x01",
            "somehow or other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17EF")

    label("loc_1771")


    ChrTalk(
        0xFE,
        (
            "I was shocked at the\x01",
            "independence proposal to,\x01",
            "but... It might be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it's realized\x01",
            "somehow or other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EF")

    Jump("loc_1CD1")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(
        0xFE,
        (
            "We received terrorist intel\x01",
            "and we're doing our best to\x01",
            "secure the nearby border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To defend against invasions from the\x01",
            "air, we're using a special facility\x01",
            "that was constructed nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition, if we had anti-aircraft\x01",
            "cannons like those of the army,\x01",
            "things would be perfect, but...\x02",
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
    Jump("loc_1A2B")

    label("loc_196B")


    ChrTalk(
        0xFE,
        (
            "If we had anti-aircraft cannons like those of\x01",
            "the army we could deal with an invasion from\x01",
            "the air and things would be perfect, however...\x02",
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

    label("loc_1A2B")

    Jump("loc_1CD1")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xFE,
        (
            "This morning I happened to\x01",
            "see a crimson orbal train\x01",
            "passing under the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was the Imperial government's private\x01",
            "train... The Blood and Iron Chancellor and Crown\x01",
            "Prince Olivert were probably riding in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trade conference has\x01",
            "finally started... I\x01",
            "have to stay sharp.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C09")

    label("loc_1B70")


    ChrTalk(
        0xFE,
        (
            "This morning I happened to\x01",
            "see a crimson orbal train\x01",
            "passing under the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trade conference has\x01",
            "finally started... I\x01",
            "have to stay sharp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C09")

    Jump("loc_1CD1")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1CD1")

    ChrTalk(
        0xFE,
        (
            "With the approaching trade\x01",
            "conference, our responsibilities\x01",
            "as CGF have become even larger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must ensure a secure border\x01",
            "for the sake of the visiting\x01",
            "heads of state as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD1")

    TalkEnd(0xFE)
    Return()

    # Function_5_FB6 end

    def Function_6_1CD5(): pass

    label("Function_6_1CD5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This valley is really\x01",
            "great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you fall, you won't\x01",
            "survive. How\x01",
            "thrilling...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1CD5 end

    def Function_7_1D36(): pass

    label("Function_7_1D36")

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

    # Function_7_1D36 end

    def Function_8_2107(): pass

    label("Function_8_2107")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0xBB8, 0x0)
    Return()

    # Function_8_2107 end

    def Function_9_2117(): pass

    label("Function_9_2117")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x7D0, 0x0)
    Return()

    # Function_9_2117 end

    def Function_10_2127(): pass

    label("Function_10_2127")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)

    label("loc_2130")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2143")
    Sleep(5000)
    Jump("loc_2130")

    label("loc_2143")

    Return()

    # Function_10_2127 end

    def Function_11_2144(): pass

    label("Function_11_2144")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(1200)

    label("loc_2150")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2163")
    Sleep(5000)
    Jump("loc_2150")

    label("loc_2163")

    Return()

    # Function_11_2144 end

    def Function_12_2164(): pass

    label("Function_12_2164")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(2400)

    label("loc_2170")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2183")
    Sleep(5000)
    Jump("loc_2170")

    label("loc_2183")

    Return()

    # Function_12_2164 end

    def Function_13_2184(): pass

    label("Function_13_2184")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(3600)

    label("loc_2190")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21A3")
    Sleep(5000)
    Jump("loc_2190")

    label("loc_21A3")

    Return()

    # Function_13_2184 end

    def Function_14_21A4(): pass

    label("Function_14_21A4")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(4800)

    label("loc_21B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21C3")
    Sleep(5000)
    Jump("loc_21B0")

    label("loc_21C3")

    Return()

    # Function_14_21A4 end

    def Function_15_21C4(): pass

    label("Function_15_21C4")

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

    # Function_15_21C4 end

    def Function_16_220F(): pass

    label("Function_16_220F")

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

    # Function_16_220F end

    SaveToFile()

Try(main)
