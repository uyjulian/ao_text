from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t110b.bin",                # FileName
        "t110b",                    # MapName
        "t110b",                    # Location
        0x0046,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 1, 0, 2],
    )

    BuildStringList((
        "t110b",                  # 0
        "Guideman Barclay",       # 1
        "Keya",                 # 2
        "Destination to Hotel · Delfinia",# 3
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
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

    DeclNpc(0,       0,       23000,   180,  257,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 3,   0.0,                   2.0,                   -0.800000011920929,    400.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.5,                  0.1599999964237213,    1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "Destination to Hotel · Delfinia")

    ChipFrameInfo(460, 0)                                        # 0

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_29C",          # 03, 3
        "Function_4_104E",         # 04, 4
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1CC end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Return()

    # Function_1_27C end

    def Function_2_27D(): pass

    label("Function_2_27D")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_295")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_27D end

    def Function_3_29C(): pass

    label("Function_3_29C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    SetChrPos(0x101, 600, 200, 0, 0)
    SetChrPos(0xEF, -600, 200, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 750, 29220, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 23000, 180)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆ I chose Tio in the introduction\x01",        # 0
            "◆ I chose Randy in the introduction\x01",      # 1
            "◆ Do not change\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AD"),
        (1, "loc_3BB"),
        (5, "loc_3C9"),
        (SWITCH_DEFAULT, "loc_3C9"),
    )


    label("loc_3AD")

    ClearScenarioFlags(0x121, 2)
    SetScenarioFlags(0x121, 3)
    ClearScenarioFlags(0x121, 4)
    Jump("loc_3CE")

    label("loc_3BB")

    ClearScenarioFlags(0x121, 2)
    ClearScenarioFlags(0x121, 3)
    SetScenarioFlags(0x121, 4)
    Jump("loc_3CE")

    label("loc_3C9")

    Jump("loc_3CE")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_408")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis247.itp")
    Jump("loc_46E")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_442")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis248.itp")
    Jump("loc_46E")

    label("loc_442")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis249.itp")

    label("loc_46E")

    OP_68(0, 3000, 15000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(60000, 0)

    def lambda_4A1():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A1)
    Sleep(100)

    def lambda_4B9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4B9)
    FadeToBright(1000, 0)
    OP_68(0, 3000, 25000, 8000)
    Sleep(7000)
    OP_0D()
    Fade(1000)
    OP_68(0, 1000, 21000, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 3500)
    OP_0D()
    Sleep(500)
    OP_9B(0x0, 0x8, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_5B3")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelin Guesthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd of the Special Affairs Support Division\x01",
            "You are Ellie, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_623")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelin Guesthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Lloyd of the Special Affairs Support Division\x01",
            "You are welcome, Tio?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_698")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelin Guesthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd of the Special Affairs Support Division\x01",
            "You are Randy, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelin Guesthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd of the Special Affairs Support Division\x01",
            "Noel-sama, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelin Guesthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd of the Special Affairs Support Division\x01",
            "Welcome you, are not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_777")


    ChrTalk(
        0x101,
        "#00000F#12PYes, I see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12PWell … you …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_866")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FWell, at a certain auction meeting\x01",
            "I was doing a guide role … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_861")

    AnonymousTalk(
        0x103,
        "#00205FAh … indeed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_861")

    Jump("loc_988")

    label("loc_866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_8FE")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FWell, at a certain auction meeting\x01",
            "I was doing a guide role … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_8F9")

    AnonymousTalk(
        0x104,
        "#00305FOops, was that so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8F9")

    Jump("loc_988")

    label("loc_8FE")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FWell, at a certain auction meeting\x01",
            "I was doing a guide role … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_988")

    AnonymousTalk(
        0x102,
        "#00105FAh … That was right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_988")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5Pmy mother……\x01",
            "I am sorry for that passage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMy husband is in such a shape\x01",
            "It has become … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBeginning with myself, many servants\x01",
            "Continue to manage the guesthouse\x01",
            "I will leave it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis is also Mayor of Dieter\x01",
            "Careful gift#4RTomato#It is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI see……\x01",
            "That was more than anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_B4F")

    ChrTalk(
        0x102,
        (
            "#00102F#12PAt the trade meeting\x01",
            "The leaders of each country here\x01",
            "You heard you were able to stay.\x02\x03",
            "#00109FI really appreciate your work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_BBA")

    ChrTalk(
        0x103,
        (
            "#00204F#12PCertainly at the trade meeting\x01",
            "The heads of countries have stayed.\x02\x03",
            "#00202FThank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C32")

    ChrTalk(
        0x104,
        (
            "#00303F#12PIt is certainly a trade meeting\x01",
            "Great master of each country\x01",
            "I stayed here.\x02\x03",
            "#00300FI am very tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_CA8")

    ChrTalk(
        0x109,
        (
            "#10103F#12PCertainly at the trade meeting\x01",
            "The heads of countries are here\x01",
            "I was staying …\x02\x03",
            "#10100FCongratulations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_D1B")

    ChrTalk(
        0x105,
        (
            "#10302F#12PIt is certainly a trade meeting\x01",
            "Here is a great man\x01",
            "Did you stay?\x02\x03",
            "#10304FHuh, thanks for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1B")


    ChrTalk(
        0x8,
        (
            "#5PMerciless words …\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3665, 255, 100, 0)

    NpcTalk(
        0x9,
        "Keyaの声",
        "#11P#12A#30W#NI love you!\x02",
    )

    CloseMessageWindow()

    def lambda_D88():

        label("loc_D88")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_D88")

    QueueWorkItem2(0x8, 2, lambda_D88)
    OP_68(0, 1000, 21500, 2000)
    BeginChrThread(0x9, 3, 0, 4)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x8, 0x2)

    ChrTalk(
        0x101,
        "#00002F#12PKeya、先に来てたのか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F#5PYeah, with Shri\x01",
            "I was exploring all around.\x02\x03",
            "#01110FIs not it Bansanke soon?\x01",
            "It will start.\x02\x03",
            "Lloyd's also\x01",
            "I have to go to the table quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12POkay, I understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_EE4")

    ChrTalk(
        0x102,
        (
            "#00102F#12PWell then,\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE5")

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(
        0x103,
        (
            "#00202F#12PWell then,\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE5")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_F68")

    ChrTalk(
        0x104,
        (
            "#00309F#12PThen, guide,\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE5")

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_FAC")

    ChrTalk(
        0x109,
        (
            "#10102F#12PWell then,\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE5")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_FE5")

    ChrTalk(
        0x105,
        (
            "#10302F#12PWell then,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE5")

    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5PCertainly.\x01",
            "Then, please go inside - ─\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20250, 1000)
    OP_6F(0x79)
    OP_0D()
    StopSound(126, 1000, 80)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t113B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_29C end

    def Function_4_104E(): pass

    label("Function_4_104E")


    def lambda_1053():
        OP_9B(0x1, 0xFE, 0xA, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1053)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_104E end

    SaveToFile()

Try(main)
