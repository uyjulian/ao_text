﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Guide Berkeley",         # 1
        "KeA",                    # 2
        "To Hotel Delphinia",     # 3
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

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(460, 0)                                        # 0

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_29C",          # 03, 3
        "Function_4_1186",         # 04, 4
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆Chose Tio in prologue\x01",        # 0
            "◆Chose Randy in prologue\x01",      # 1
            "◆No change\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AE"),
        (1, "loc_3BC"),
        (5, "loc_3CA"),
        (SWITCH_DEFAULT, "loc_3CA"),
    )


    label("loc_3AE")

    ClearScenarioFlags(0x121, 2)
    SetScenarioFlags(0x121, 3)
    ClearScenarioFlags(0x121, 4)
    Jump("loc_3CF")

    label("loc_3BC")

    ClearScenarioFlags(0x121, 2)
    ClearScenarioFlags(0x121, 3)
    SetScenarioFlags(0x121, 4)
    Jump("loc_3CF")

    label("loc_3CA")

    Jump("loc_3CF")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_409")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis247.itp")
    Jump("loc_46F")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_443")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis248.itp")
    Jump("loc_46F")

    label("loc_443")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis249.itp")

    label("loc_46F")

    OP_68(0, 3000, 15000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(60000, 0)

    def lambda_4A2():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A2)
    Sleep(100)

    def lambda_4BA():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4BA)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_5C5")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelam guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd and Miss Elie from the\x01",
            "Special Support Section, I presume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_645")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelam guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Lloyd and Miss Tio from the\x01",
            "Special Support Section, I presume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_6C9")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelam guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd and Mr. Randy from the\x01",
            "Special Support Section, I presume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_74D")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelam guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd and Miss Noｱl from the\x01",
            "Special Support Section, I presume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_7CB")

    ChrTalk(
        0x8,
        "#5PWelcome to Michelam guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMr. Lloyd and Mr. Wazy from the\x01",
            "Special Support Section, I presume?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CB")


    ChrTalk(
        0x101,
        "#00000F#12PYes, we are──\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12POh, you are...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_8C8")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FUhhm, if I remember correctly, you\x01",
            "are the guide who were at the auction...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_8C3")

    AnonymousTalk(
        0x103,
        "#00205FOh...indeed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8C3")

    Jump("loc_A11")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_971")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FUhhm, if I remember correctly, you\x01",
            "are the guide who were at the auction...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_96C")

    AnonymousTalk(
        0x104,
        "#00305FWhoa, really?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_96C")

    Jump("loc_A11")

    label("loc_971")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00001FUhhm, if I remember correctly, you\x01",
            "are the guide who were at the auction...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_A11")

    AnonymousTalk(
        0x102,
        "#00105FOh...that's right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A11")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PHa ha...\x01",
            "Thank you for all you have done on that occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlthough my Master \x01",
            "ended up like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStarting with me, many servants\x01",
            "were decided to have the guest\x01",
            "house management entrusted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis too is a gift by Mayor Dieter\x01",
            "out of his kind consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI see...\x01",
            "That's nice to hear.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_C18")

    ChrTalk(
        0x102,
        (
            "#00102F#12PIt seems that at the Trade\x01",
            "Conference the countries'\x01",
            "VIPs were lodged here.\x02\x03",
            "#00109FThank you very much for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E65")

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_CAB")

    ChrTalk(
        0x103,
        (
            "#00204F#12PI am sure that at the Trade Conference \x01",
            "the countriesｺ' VIPs were lodged here.\x02\x03",
            "#00202FThank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E65")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_D3F")

    ChrTalk(
        0x104,
        (
            "#00303F#12PI'm sure that at the Trade \x01",
            "Conference the countries'\x01",
            "big shots were lodged here.\x02\x03",
            "#00300FThanks a lot for your work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E65")

    label("loc_D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(
        0x109,
        (
            "#10103F#12PI'm sure that at the Trade\x01",
            "Conference the countries'\x01",
            "VIPs were lodged here...\x02\x03",
            "#10100FThank you for your hard work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E65")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(
        0x105,
        (
            "#10302F#12PI'm sure that at the Trade \x01",
            "Conference the countries'\x01",
            "big shots lodged here, eh...?\x02\x03",
            "#10304FHu hu, thank you for your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E65")


    ChrTalk(
        0x8,
        (
            "#5PI am not worthy of your words...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3665, 255, 100, 0)

    NpcTalk(
        0x9,
        "KeA's Voice",
        "#11P#12A#30W#NAh, here they are!\x02",
    )

    CloseMessageWindow()

    def lambda_EE3():

        label("loc_EE3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_EE3")

    QueueWorkItem2(0x8, 2, lambda_EE3)
    OP_68(0, 1000, 21500, 2000)
    BeginChrThread(0x9, 3, 0, 4)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x8, 0x2)

    ChrTalk(
        0x101,
        "#00002F#12PKeA, did you arrive first?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F#5PYes, I went exploring\x01",
            "around with Sully!\x02\x03",
            "#01110FThey say that the...\x01",
            "dinner party? is\x01",
            "going to start soon.\x02\x03",
            "Guys, you must take\x01",
            "your seats quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PHa ha, I understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_103B")

    ChrTalk(
        0x102,
        (
            "#00102F#12PThen, please,\x01",
            "guide us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111B")

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1071")

    ChrTalk(
        0x103,
        (
            "#00202F#12PThen, please,\x01",
            "guide us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111B")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(
        0x104,
        (
            "#00309F#12PThen, thanks\x01",
            "for guiding us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111B")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_10E2")

    ChrTalk(
        0x109,
        (
            "#10102F#12PThen, please,\x01",
            "guide us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111B")

    label("loc_10E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(
        0x105,
        (
            "#10302F#12PThen, thank you\x01",
            "for guiding us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111B")

    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5PUnderstood.\x01",
            "Then, please, come inside──\x02",
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

    def Function_4_1186(): pass

    label("Function_4_1186")


    def lambda_118B():
        OP_9B(0x1, 0xFE, 0xA, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_118B)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_1186 end

    SaveToFile()

Try(main)
