from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1050",                  # 0
        "Manager Haggar",         # 1
        "Lotti",                  # 2
        "Citrus",                 # 3
        "Engineer",               # 4
        "Fortune Teller",         # 5
        "KeA",                    # 6
        "Fran",                   # 7
        "Cecil",                  # 8
        "Ilya",                   # 9
        "Rixia",                  # 10
        "Sully",                  # 11
        "Mariabell",              # 12
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25600.itc",                   # 02
        "chr/ch26000.itc",                   # 03
        "chr/ch14202.itc",                   # 04
    ))

    DeclNpc(4294966817, 0,       10050,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294873337, 0,       8260,    0,    385,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294865477, 0,       8859,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1059,    0,       10489,   177,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294953937, 150,     15430,   90,   453,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  30, 0x0000)
    DeclActor(4294967276, 0,       8270,    1500,    4294966816, 1500,    10050,   0x007E, 0,  6,  0x0000)
    DeclActor(12010,   0,       15830,   1200,    12010,   450,     15830,   0x007C, 0,  5,  0x0000)
    DeclActor(1260,    0,       9210,    1500,    1060,    1500,    10490,   0x007E, 0,  11, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_586",          # 04, 4
        "Function_5_5D3",          # 05, 5
        "Function_6_6A7",          # 06, 6
        "Function_7_6AB",          # 07, 7
        "Function_8_107D",         # 08, 8
        "Function_9_1698",         # 09, 9
        "Function_10_183A",        # 0A, 10
        "Function_11_1BAB",        # 0B, 11
        "Function_12_1BAF",        # 0C, 12
        "Function_13_1DE3",        # 0D, 13
        "Function_14_2C92",        # 0E, 14
        "Function_15_2CF2",        # 0F, 15
        "Function_16_32EC",        # 10, 16
        "Function_17_35A9",        # 11, 17
        "Function_18_3625",        # 12, 18
        "Function_19_36A6",        # 13, 19
        "Function_20_3727",        # 14, 20
        "Function_21_37A8",        # 15, 21
        "Function_22_3829",        # 16, 22
        "Function_23_38AA",        # 17, 23
        "Function_24_392B",        # 18, 24
        "Function_25_39AC",        # 19, 25
        "Function_26_3A2D",        # 1A, 26
        "Function_27_3AAE",        # 1B, 27
        "Function_28_3B2F",        # 1C, 28
        "Function_29_3BB0",        # 1D, 29
        "Function_30_3C31",        # 1E, 30
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41C")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_3BC")

    label("loc_41C")

    Return()

    # Function_1_3BC end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_41D")

    label("loc_47D")

    Return()

    # Function_2_41D end

    def Function_3_47E(): pass

    label("Function_3_47E")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 106130, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_576")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4270, 0, 7670, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5450, 0, 7670, 270)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C")
    SetChrFlags(0xC, 0x10)

    label("loc_51C")

    Jump("loc_576")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_52F")
    Jump("loc_576")

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_568")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x9, -100710, 0, 8860, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_576")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_576")
    ClearChrFlags(0x9, 0x80)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_585")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_585")

    Return()

    # Function_3_47E end

    def Function_4_586(): pass

    label("Function_4_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_598")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_5AF")
    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x0, 0x1)

    label("loc_5AF")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    OP_66(0x3, 0x1)
    Jump("loc_5D2")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D2")
    OP_66(0x3, 0x1)

    label("loc_5D2")

    Return()

    # Function_4_586 end

    def Function_5_5D3(): pass

    label("Function_5_5D3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""The Holidays We Love - A Careful\x01",
            "Recipes Selection" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Picky Matcha Latte"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6A3")

    TalkEnd(0xFF)
    Return()

    # Function_5_5D3 end

    def Function_6_6A7(): pass

    label("Function_6_6A7")

    Call(0, 7)
    Return()

    # Function_6_6A7 end

    def Function_7_6AB(): pass

    label("Function_7_6AB")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1079")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_708")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728")
    OP_AF(0x64)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1074")

    label("loc_728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1074")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_873")

    ChrTalk(
        0x8,
        (
            "Since the clamor in the city quieten down, I've just\x01",
            "come with everyone to look at the hotel's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, that inexplicable azure pale tree...\x01",
            "It's even eerier seen from close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I already knew it, but reopening Michelam\x01",
            "will be difficult for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8FF")

    label("loc_873")


    ChrTalk(
        0x8,
        (
            "Michelam's reopening is still far in the future, but...\x01",
            "I just wanted to came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, feel free to ask\x01",
            "if you want to rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FF")

    Jump("loc_1074")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D7")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Mr. Lloyd...\x01",
            "Thank you for your visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The hotel is closed, but we\x01",
            "are always prepared to\x01",
            "accept customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please tell me if you want to rest.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A41")

    label("loc_9D7")


    ChrTalk(
        0x8,
        (
            "Hm, even so, why \x01",
            "those bell sounds are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "M. W. L. should be closed too...\x01",
            "It's very strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A41")

    Jump("loc_1074")

    label("loc_A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A54")
    Jump("loc_1074")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5D")

    ChrTalk(
        0x8,
        (
            "Ooh, Mr. Lloyd and Miss KeA.\x01",
            "Welcome back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am glad you could meet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FEheheh, I'm back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, I'm sorry to have made you worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, no, don't mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, your friends have\x01",
            "just gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After they all have finished their business,\x01",
            "they will go to the meeting place...\x01",
            "Should you hurry, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYou're right,\x01",
            "thank you very much.\x02\x03",
            "#00000FThen, let's go to the\x01",
            "theme park when we\x01",
            "have finished too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, let's go!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 7)
    Jump("loc_D74")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1C")

    ChrTalk(
        0x8,
        (
            "Your friends have\x01",
            "just gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After they all have finished their business,\x01",
            "they will go to the meeting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Should it be time for\x01",
            "you to head there too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D74")

    label("loc_D1C")


    ChrTalk(
        0x8,
        (
            "Your friends have\x01",
            "just gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Should it be time for\x01",
            "you to head there too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D74")

    Jump("loc_1074")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E67")

    ChrTalk(
        0x8,
        (
            "It appears that Miss KeA\x01",
            "has gone out alone just before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I spoke to her just in case,\x01",
            "but I was told to not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(KeA...\x01",
            "As I feared, maybe I should've\x01",
            "looked for her outside the hotel.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ED2")

    label("loc_E67")


    ChrTalk(
        0x8,
        (
            "It appears that Miss KeA\x01",
            "has gone out alone just before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, I wonder where\x01",
            "could she have gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED2")

    Jump("loc_1074")

    label("loc_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDE")

    ChrTalk(
        0x8,
        (
            "My my, everyone...\x01",
            "How do you feel using\x01",
            "the VIP floor at 3F?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, it's very pleasant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please inform me immediately\x01",
            "if there were to be imperfections.\x01",
            "We will deal with those at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1074")

    label("loc_FDE")


    ChrTalk(
        0x8,
        (
            "How do you feel using\x01",
            "the VIP floor at 3F?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please inform me immediately\x01",
            "if there were to be imperfections.\x01",
            "We will deal with those at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1074")

    Jump("loc_6B8")

    label("loc_1079")

    TalkEnd(0x8)
    Return()

    # Function_7_6AB end

    def Function_8_107D(): pass

    label("Function_8_107D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1146")

    ChrTalk(
        0x9,
        (
            "It seems that because it was neglected for\x01",
            "a while, quite some dust has gathered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*haah*...that azure pale tree makes me\x01",
            "feel uneasy, but I must clean properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11DD")

    label("loc_1146")


    ChrTalk(
        0x9,
        (
            "We come periodically to clean so\x01",
            "that we can reopen at any time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being that azure pale tree\x01",
            "so close to here, really\x01",
            "makes me uneasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DD")

    Jump("loc_1694")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(
        0x9,
        (
            "That Mr. Arios who became the State\x01",
            "Guard Commander in Chief passed\x01",
            "through the arcade just before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He seemed to have a cute\x01",
            "little girl with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Mr. Arios and KeA...\x01",
            "It seems they came for real.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F(Quick, let's chase after them.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13CC")

    label("loc_1309")


    ChrTalk(
        0x9,
        (
            "State Guard Commander in Chief Arios \x01",
            "passed through the arcade just before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He had a little girl with him and it seems\x01",
            "they were heading to the theme park...\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CC")

    Jump("loc_1694")

    label("loc_13D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13DF")
    Jump("loc_1694")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_146B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FA")
    Call(0, 9)
    Jump("loc_1466")

    label("loc_13FA")


    ChrTalk(
        0xFE,
        (
            "Pleeease, let me be in charge\x01",
            "to take care of Mr. Wazyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll treat you to a gelato next tiiime!\x02",
    )

    CloseMessageWindow()

    label("loc_1466")

    Jump("loc_1694")

    label("loc_146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1605")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Oh, the customer is...Mr. Wazy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C-Could it be that the\x01",
            "customers staying at\x01",
            "the VIP floor today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, in that case I think\x01",
            "those would be us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "!!!!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(D-Dear me...\x01",
            "Why today, of all days, do I have to\x01",
            "be in charge of the commoners' floor!!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I don't really get why,\x01",
            "but she looks shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, what a funny girl.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1694")

    label("loc_1605")


    ChrTalk(
        0xFE,
        (
            "D-Dear me...\x01",
            "To be in charge of the commoners'\x01",
            "floor today, of all days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a chance to be taking\x01",
            "care of Mr. Wazy, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1694")

    TalkEnd(0xFE)
    Return()

    # Function_8_107D end

    def Function_9_1698(): pass

    label("Function_9_1698")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "Come on, Citrus, I beg you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Allow me to be on duty at the VIP\x01",
            "floor where Mr. Wazy is today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And I was thinking what it was that you wanted\x01",
            "by calling me out on purpose when I'm working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, what started it all wasn't\x01",
            "you pushing it to me saying that\x01",
            ""it's a bother to take care of the VIP floor"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C-Can't you help me out there?\x01",
            "I'll treat you to a gelato next tiiime!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_1698 end

    def Function_10_183A(): pass

    label("Function_10_183A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195B")

    ChrTalk(
        0xA,
        (
            "It seems that Chairman\x01",
            "MacDowell and others were\x01",
            "confined at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Moreover, it seems that they were watched\x01",
            "by the jaegers who attacked the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may have been for the independence, but\x01",
            "the President too did some cruel things...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19FE")

    label("loc_195B")


    ChrTalk(
        0xA,
        (
            "It seems that Chairman\x01",
            "MacDowell and others were\x01",
            "confined at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President too did some cruel things...\x01",
            "I'm glad he was caught, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FE")

    Jump("loc_1BA7")

    label("loc_1A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABA")

    ChrTalk(
        0xA,
        (
            "The person sat over there is the \x01",
            "fortune teller who works at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems she showed up one day...\x01",
            "I wonder where she usually lives.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AFC")

    label("loc_1ABA")


    ChrTalk(
        0xA,
        (
            "...Whoops, I must finish the\x01",
            "cleanings quickly, not talking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFC")

    Jump("loc_1BA7")

    label("loc_1B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1B0F")
    Jump("loc_1BA7")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2A")
    Call(0, 9)
    Jump("loc_1B99")

    label("loc_1B2A")


    ChrTalk(
        0xFE,
        (
            "Geez, if you insist that much I\x01",
            "suppose I could switch with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, how self-willed you're.\x02",
    )

    CloseMessageWindow()

    label("loc_1B99")

    Jump("loc_1BA7")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1BA7")

    label("loc_1BA7")

    TalkEnd(0xFE)
    Return()

    # Function_10_183A end

    def Function_11_1BAB(): pass

    label("Function_11_1BAB")

    Call(0, 12)
    Return()

    # Function_11_1BAB end

    def Function_12_1BAF(): pass

    label("Function_12_1BAF")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DDF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Remodel - Synthesize\x01",      # 1
            "Quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C1C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3C")
    OP_AF(0x65)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DDA")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DDA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D15")

    ChrTalk(
        0xB,
        (
            "Though such a mysterious\x01",
            "thing has appeared, this place's\x01",
            "personnel has got quite the guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I want to finish the maintenance quickly\x01",
            "and get away from here at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDA")

    label("loc_1D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1DDA")

    ChrTalk(
        0xB,
        (
            "I just came with the hotel\x01",
            "people to do maintenance on\x01",
            "the facilities while they're closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you too need something,\x01",
            "don't hesitate to tell me.\x01",
            "I'll help you in my spare time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDA")

    Jump("loc_1BBC")

    label("loc_1DDF")

    TalkEnd(0xB)
    Return()

    # Function_12_1BAF end

    def Function_13_1DE3(): pass

    label("Function_13_1DE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2568")
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_217F")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -14760, 0, 12870, 50)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        "#11POh, those books...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCould they be "Agnes in the Sunny Place" that\x01",
            "you can see in Crossbell City from time to time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FUhhm, are you talking about this novel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FWell, we have gathered all the volumes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHu hu, that is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI too had the chance to obtain\x01",
            "that novel before.\x01",
            "I really enjoyed reading it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt seems it is a made-up story, but...\x01",
            "Maybe the female protagonist\x01",
            "was based on someone somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI intended to remain here\x01",
            "as a spectator until the end\x01",
            "of the Crossbell incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt could be nice doing that\x01",
            "while reading such books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F(Since we have them, should\x01",
            "we give them to this person...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18A, 5)
    Call(0, 15)
    Jump("loc_2563")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234D")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -11330, 0, 11290, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#11PThose are "Agnes in the Sunny Place" that you\x01",
            "can see in Crossbell City from time to time, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI intended to remain here\x01",
            "as a spectator until the end\x01",
            "of the Crossbell incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt could be nice doing that\x01",
            "while reading such books.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_2563")

    label("loc_234D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AD")

    ChrTalk(
        0xC,
        (
            "That azure tree...\x01",
            "To think such a thing appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tarots, crystal-gazing, star-gazing...\x01",
            "Even using all the methods I am capable of,\x01",
            "I can not read the future events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hu hu, interesting...\x01",
            "It is the first time such a thing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What will the future\x01",
            "of Crossbell be...?\x01",
            "I shall see it with my own eyes here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2563")

    label("loc_24AD")


    ChrTalk(
        0xC,
        (
            "Hu hu...probably even "they"\x01",
            "did not foresee that the situation\x01",
            "would have become like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What will the future\x01",
            "of Crossbell be...?\x01",
            "I shall see it with my own eyes here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2563")

    Jump("loc_2C8E")

    label("loc_2568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")

    ChrTalk(
        0xC,
        "Hm............\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2639")

    ChrTalk(
        0x101,
        (
            "#00005F(This person...\x01",
            "Is she the theme park fortune teller?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265E")

    label("loc_2639")


    ChrTalk(
        0x101,
        "#00005F(Who is this person...?)\x02",
    )

    CloseMessageWindow()

    label("loc_265E")


    ChrTalk(
        0x102,
        (
            "#00105F(It looks like she has tarot cards\x01",
            "spread in front of her...)\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2739")
    Jump("loc_2783")

    label("loc_2739")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2759")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2783")

    label("loc_2759")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2779")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2783")

    label("loc_2779")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2783")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "...Be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you intend to advance further...\x01",
            "You all will probably walk\x01",
            "a grand difficult path.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00201F............!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FW-What do you mean!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well then, how should I read this\x01",
            "difficult cards arrangement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is just that if you want to advance further,\x01",
            "you should be prepared to face the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you will face all the difficulties, will you be able \x01",
            "to protect what is important to you until the end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "That is what will depend on you.\x01\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x101,
        (
            "#00003F...I don't get it well, but...\x01",
            "I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hu hu, I wish you good luck.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 7)
    SetChrSubChip(0xC, 0x0)
    Jump("loc_2C8E")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF3")

    ChrTalk(
        0xC,
        (
            "If you want to advance further,\x01",
            "you should be prepared to face the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you will face all the difficulties, will you be able \x01",
            "to protect what is important to you until the end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "That is what will depend on you.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hu hu, I wish you good luck.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_2C8E")

    label("loc_2BF3")


    ChrTalk(
        0xC,
        (
            "Even if you will face all the difficulties, will you be able \x01",
            "to protect what is important to you until the end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hu hu, I wish you good luck.\x02",
    )

    CloseMessageWindow()

    label("loc_2C8E")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DE3 end

    def Function_14_2C92(): pass

    label("Function_14_2C92")

    ClearScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EE, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F4, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CF1")
    SetScenarioFlags(0x0, 5)

    label("loc_2CF1")

    Return()

    # Function_14_2C92 end

    def Function_15_2CF2(): pass

    label("Function_15_2CF2")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Hand Over the Novel\x01",      # 0
            "Do Not\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328D")

    ChrTalk(
        0x101,
        (
            "#6P#00000FIf you want...\x01",
            "Would you like to have these books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PMy...is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIf Mr. Lloyd says so...\x01",
            "For starters, they are mostly gifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FPlease feel free to accept 'em.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHu hu, in that case, I will\x01",
            "accept them with gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the entire Agnes in the Sunny Place set.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x2EE, 1)
    SubItemNumber(0x2EF, 1)
    SubItemNumber(0x2F0, 1)
    SubItemNumber(0x2F1, 1)
    SubItemNumber(0x2F2, 1)
    SubItemNumber(0x2F3, 1)
    SubItemNumber(0x2F4, 1)
    SubItemNumber(0x2F5, 1)
    SubItemNumber(0x2F6, 1)
    SubItemNumber(0x2F7, 1)
    SubItemNumber(0x2F8, 1)
    SubItemNumber(0x2F9, 1)
    SubItemNumber(0x2FA, 1)
    SubItemNumber(0x2FB, 1)

    ChrTalk(
        0xC,
        "#11P...Oh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMaybe it is presumptuous of me, but...\x01",
            "I will give this to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x396, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt is something I obtained from one\x01",
            "of my connections some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI do not know if it will serve\x01",
            "you some purpose, but...\x01",
            "Take it with you, if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FEehm, is it alright?\x01",
            "It's such a valuable-looking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHu hu, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIn the whirl of the Crossbell incident\x01",
            "I am just a bystander, this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf it is just for this level of involvement,\x01",
            "probably no one will have anything to complain.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#11PHu hu... I am just talking to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PTake good care of it, if you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FUhhm, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18A, 6)
    Jump("loc_32BC")

    label("loc_328D")


    ChrTalk(
        0x101,
        "#6P#00000F(Uhhm, maybe I should refuse.)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_32BC")

    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -12560, 0, 13000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2CF2 end

    def Function_16_32EC(): pass

    label("Function_16_32EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrPos(0x13, 0, 0, 0, 0)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(4140, 1000, 8840, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_68(5450, 1000, 10150, 6000)
    BeginChrThread(0x13, 3, 0, 17)
    BeginChrThread(0x10, 3, 0, 18)
    BeginChrThread(0xF, 3, 0, 19)
    BeginChrThread(0xE, 3, 0, 20)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x109, 3, 0, 21)
    BeginChrThread(0x105, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_32EC end

    def Function_17_35A9(): pass

    label("Function_17_35A9")

    SetChrPos(0xFE, 3500, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0xFFD3, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x10CC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x3E8, 0x7D0, 0x1)
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_3605():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3605)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_35A9 end

    def Function_18_3625(): pass

    label("Function_18_3625")

    SetChrPos(0xFE, 1300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3686():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3686)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_3625 end

    def Function_19_36A6(): pass

    label("Function_19_36A6")

    SetChrPos(0xFE, 1300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3707():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3707)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_36A6 end

    def Function_20_3727(): pass

    label("Function_20_3727")

    SetChrPos(0xFE, -600, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3788)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_3727 end

    def Function_21_37A8(): pass

    label("Function_21_37A8")

    SetChrPos(0xFE, -600, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3809():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3809)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_37A8 end

    def Function_22_3829(): pass

    label("Function_22_3829")

    SetChrPos(0xFE, -2500, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_388A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_388A)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_3829 end

    def Function_23_38AA(): pass

    label("Function_23_38AA")

    SetChrPos(0xFE, -2500, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_390B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_390B)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_38AA end

    def Function_24_392B(): pass

    label("Function_24_392B")

    SetChrPos(0xFE, -4400, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_398C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_398C)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_392B end

    def Function_25_39AC(): pass

    label("Function_25_39AC")

    SetChrPos(0xFE, -6300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3A0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A0D)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_39AC end

    def Function_26_3A2D(): pass

    label("Function_26_3A2D")

    SetChrPos(0xFE, -6300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3A8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A8E)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3A2D end

    def Function_27_3AAE(): pass

    label("Function_27_3AAE")

    SetChrPos(0xFE, -8200, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x33F4, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3B0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B0F)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_3AAE end

    def Function_28_3B2F(): pass

    label("Function_28_3B2F")

    SetChrPos(0xFE, -10100, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3B90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B90)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_3B2F end

    def Function_29_3BB0(): pass

    label("Function_29_3BB0")

    SetChrPos(0xFE, -10100, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3C11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_3BB0 end

    def Function_30_3C31(): pass

    label("Function_30_3C31")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 ～Staircase～\x01",
            "The 3F VIP floor is reserved.\x01",
            "Please refrain from entering.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_3C31 end

    SaveToFile()

Try(main)
