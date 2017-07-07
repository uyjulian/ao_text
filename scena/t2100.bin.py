from ScenarioHelper import *

def main():
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
        "Mr. Broard",           # 1
        "Member Dalia",             # 2
        "Chiluru",                 # 3
        "Imperial army tank",             # 4
        "Imperial army tank",             # 5
        "Imperial army tank",             # 6
        "Imperial army tank",             # 7
        "Imperial army tank",             # 8
        "SE control",                 # 9
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
        "Function_5_DE9",          # 05, 5
        "Function_6_191C",         # 06, 6
        "Function_7_197C",         # 07, 7
        "Function_8_1D4D",         # 08, 8
        "Function_9_1D5D",         # 09, 9
        "Function_10_1D6D",        # 0A, 10
        "Function_11_1D8A",        # 0B, 11
        "Function_12_1DAA",        # 0C, 12
        "Function_13_1DCA",        # 0D, 13
        "Function_14_1DEA",        # 0E, 14
        "Function_15_1E0A",        # 0F, 15
        "Function_16_1E55",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('狙击枪管', 1)"), scpexpr(EXPR_END)), "loc_503")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_575")

    label("loc_503")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_575")

    Jump("loc_5BF")

    label("loc_57A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB")

    ChrTalk(
        0xFE,
        (
            "I attacked Crossbell City\x01",
            "The hunting corps was hired by the empire … …\x01",
            "You seem to have such a rumor right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those who hurt the guards of the guard,\x01",
            "You can not forgive anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the empire is going to do that,\x01",
            "I also enclose my belly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_741")

    label("loc_6BB")


    ChrTalk(
        0xFE,
        (
            "Large-scale in the direction of the empire\x01",
            "I do not have exercises\x01",
            "There are rumors ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… It is excellent.\x01",
            "If the empire is going to do that,\x01",
            "I also enclose my belly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741")

    Jump("loc_DE5")

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7C1")

    ChrTalk(
        0xFE,
        (
            "Even with a light rain\x01",
            "My visibility got worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eyewitnesses still have witness information\x01",
            "It seems that it is coming out … ….\x01",
            "I have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE5")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(
        0xFE,
        (
            "Well, recently I am busy.\x01",
            "I do not have time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… But, the commander and the three captains\x01",
            "I guess it's harder than us.\x01",
            "I admire that toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I also have to work harder.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_8F1")

    label("loc_883")


    ChrTalk(
        0xFE,
        (
            "Commander and the three lords\x01",
            "I guess it's harder than us.\x01",
            "I admire that toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I also have to work harder.\x02",
    )

    CloseMessageWindow()

    label("loc_8F1")

    Jump("loc_DE5")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CC")

    ChrTalk(
        0xFE,
        (
            "Since the mayor advocated independence,\x01",
            "Empire and the republic pressured blatantly\x01",
            "It began to come over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To be honest, this tension condition hurts the stomach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the early hours some kind of settlement\x01",
            "I hope you will show me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A2F")

    label("loc_9CC")


    ChrTalk(
        0xFE,
        "To be honest, this tension condition hurts the stomach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the early hours some kind of settlement\x01",
            "I hope you will show me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    Jump("loc_DE5")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(
        0xFE,
        (
            "According to information, from the direction of the empire\x01",
            "Terrorists intrude\x01",
            "It seems that there is a high possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting nervous as expected.\x01",
            "If there is nothing and the day is over\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE5")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")

    ChrTalk(
        0xFE,
        (
            "The barrel at the tangram gate\x01",
            "I am a friend of mine … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a demanding deputy commander like a demon\x01",
            "It seems to be shaggy everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if the boss is incompetent\x01",
            "It is a luxury trouble for anything that is tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sonya command is also pretty tough,\x01",
            "I was glad that the previous commander was better\x01",
            "I do not think it is a rejuvenation either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CB5")

    label("loc_C10")


    ChrTalk(
        0xFE,
        (
            "Compared to my boss is incompetent\x01",
            "It is a luxury trouble for anything that is tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sonya command is also pretty tough,\x01",
            "I was glad that the previous commander was better\x01",
            "I do not think it is a rejuvenation either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB5")

    Jump("loc_DE5")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5C")

    ChrTalk(
        0xFE,
        (
            "Sonja command came,\x01",
            "Also to guard at the Belgard gate\x01",
            "Motivation will come out suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My superior is competent,\x01",
            "I am truly happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DE5")

    label("loc_D5C")


    ChrTalk(
        0xFE,
        (
            "When there was a previous commander,\x01",
            "In such a fulfilling mood\x01",
            "I never worked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My superior is competent,\x01",
            "I am truly happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE5")

    TalkEnd(0xFE)
    Return()

    # Function_4_5CB end

    def Function_5_DE9(): pass

    label("Function_5_DE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")

    ChrTalk(
        0xFE,
        (
            "In this situation where the mind of national independence increases,\x01",
            "The current state of tension is before the treaty\x01",
            "It can be said to be equal or higher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If conflict with the empire reaches the limit,\x01",
            "The possibility that that \"train cannon\" will appear again\x01",
            "There is enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again … … between the Empire and the Republic\x01",
            "Is it possible to avoid conflict?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FD2")

    label("loc_F02")


    ChrTalk(
        0xFE,
        (
            "…… Recently, Sonja commander also\x01",
            "He seems to be indulging in thinking well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regarding the restructuring of the guard,\x01",
            "Both Mayor Dieter and McDowell\x01",
            "I heard that they are discussing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Including confrontation with two major powers,\x01",
            "The problem is stacking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD2")

    Jump("loc_1918")

    label("loc_FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_113B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment accident ……\x01",
            "It was really terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that giant monster\x01",
            "If it is a criminal … …\x01",
            "I am worried about whether it will happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, the search and extermination of things\x01",
            "It is a place you want to manage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1136")

    label("loc_10B4")


    ChrTalk(
        0xFE,
        (
            "Given the position of the transit railway,\x01",
            "Prevention of recurrence is a top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, the search and extermination of things\x01",
            "It is a place you want to manage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    Jump("loc_1918")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1226")

    ChrTalk(
        0xFE,
        (
            "Mr. Broward says it's a distraction\x01",
            "I gave up the book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was quite interesting,\x01",
            "If you do not mind, everyone too\x01",
            "Please read it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝８卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝８卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 7)
    Jump("loc_13C6")

    label("loc_1226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1328")

    ChrTalk(
        0xFE,
        (
            "It is inside that bedrock\x01",
            "\"Galleria Fortress\"\x01",
            "Various weapons are deployed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the past, in extreme tension conditions\x01",
            "In a large-scale exercise held,\x01",
            "\"Train cannon\" was also in operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This tension is so far\x01",
            "Do not invite the situation\x01",
            "I would like to pray.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13C6")

    label("loc_1328")


    ChrTalk(
        0xFE,
        (
            "In the past, in extreme tension conditions\x01",
            "In the exercise held in the empire,\x01",
            "\"Train cannon\" was also in operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This tension is so far\x01",
            "Do not invite the situation\x01",
            "I would like to pray.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C6")

    Jump("loc_1918")

    label("loc_13CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148D")

    ChrTalk(
        0xFE,
        (
            "To that independence advocate\x01",
            "I was also surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But … … crossbell\x01",
            "In order to protect us from now on\x01",
            "It may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it will be realized somehow.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14FF")

    label("loc_148D")


    ChrTalk(
        0xFE,
        (
            "To that independence advocate\x01",
            "I was also surprised … …\x01",
            "It may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it will be realized somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_14FF")

    Jump("loc_1918")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164F")

    ChrTalk(
        0xFE,
        (
            "Terrorist information received,\x01",
            "Maximum security around the border\x01",
            "I am making efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to prevent entry from the air route,\x01",
            "Special facilities installed nearby\x01",
            "It is operated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition, if there is an anti-aircraft gun that the military has\x01",
            "I can do everything … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even if I do not have a bad day\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_16E6")

    label("loc_164F")


    ChrTalk(
        0xFE,
        (
            "If there is an anti-aircraft artillery like the army has\x01",
            "Even against entry from the air\x01",
            "I can do everything … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even if I do not have a bad day\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E6")

    Jump("loc_1918")

    label("loc_16EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(
        0xFE,
        (
            "I will go under the gate this morning\x01",
            "I saw a crimson guide train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is a train dedicated to the Imperial government ……\x01",
            "That \"Iron Blood Chancellor\" and Oliver's Prince\x01",
            "I guess it was on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trade meeting has finally begun … …\x01",
            "I feel such a sensation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1864")

    label("loc_17E4")


    ChrTalk(
        0xFE,
        (
            "I will go under the gate this morning\x01",
            "I saw a crimson guide train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trade meeting has finally begun … …\x01",
            "I feel such a sensation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1864")

    Jump("loc_1918")

    label("loc_1869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(
        0xFE,
        (
            "As the trade meeting approached,\x01",
            "We are also responsible for the guard\x01",
            "It has grown even bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To enter the crossbell\x01",
            "To protect the leaders of each country ……\x01",
            "Security of the border must be severe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1918")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE9 end

    def Function_6_191C(): pass

    label("Function_6_191C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This valley is still amazing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will be fine if I fall.\x01",
            "I'm thrashing … ….\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_191C end

    def Function_7_197C(): pass

    label("Function_7_197C")

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

    # Function_7_197C end

    def Function_8_1D4D(): pass

    label("Function_8_1D4D")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0xBB8, 0x0)
    Return()

    # Function_8_1D4D end

    def Function_9_1D5D(): pass

    label("Function_9_1D5D")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x7D0, 0x0)
    Return()

    # Function_9_1D5D end

    def Function_10_1D6D(): pass

    label("Function_10_1D6D")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)

    label("loc_1D76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D89")
    Sleep(5000)
    Jump("loc_1D76")

    label("loc_1D89")

    Return()

    # Function_10_1D6D end

    def Function_11_1D8A(): pass

    label("Function_11_1D8A")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(1200)

    label("loc_1D96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DA9")
    Sleep(5000)
    Jump("loc_1D96")

    label("loc_1DA9")

    Return()

    # Function_11_1D8A end

    def Function_12_1DAA(): pass

    label("Function_12_1DAA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(2400)

    label("loc_1DB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DC9")
    Sleep(5000)
    Jump("loc_1DB6")

    label("loc_1DC9")

    Return()

    # Function_12_1DAA end

    def Function_13_1DCA(): pass

    label("Function_13_1DCA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(3600)

    label("loc_1DD6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DE9")
    Sleep(5000)
    Jump("loc_1DD6")

    label("loc_1DE9")

    Return()

    # Function_13_1DCA end

    def Function_14_1DEA(): pass

    label("Function_14_1DEA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(4800)

    label("loc_1DF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E09")
    Sleep(5000)
    Jump("loc_1DF6")

    label("loc_1E09")

    Return()

    # Function_14_1DEA end

    def Function_15_1E0A(): pass

    label("Function_15_1E0A")

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

    # Function_15_1E0A end

    def Function_16_1E55(): pass

    label("Function_16_1E55")

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

    # Function_16_1E55 end

    SaveToFile()

Try(main)
