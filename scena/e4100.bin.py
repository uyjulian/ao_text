from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4100.bin",                # FileName
        "e4100",                    # MapName
        "e4100",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -74000, 0, -2500, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4100",                  # 0
        "Divine Wolf Zeit",       # 1
        "Dominion Wazy",          # 2
        "Dominion Kevin",         # 3
        "Squire Ries",            # 4
        "Knight Abbas",           # 5
        "Divine Wolf Zeit",       # 6
        "メルカバ",               # 7
        "メルカバ",               # 8
        "メルカバ光学迷彩",       # 9
        "メルカバ光学迷彩",       # 10
        "SE制御",                 # 11
    ))

    DeclNpc(0,       0,       0,       0,    229,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_25E",          # 02, 2
        "Function_3_3D11",         # 03, 3
        "Function_4_3D7D",         # 04, 4
        "Function_5_3DFA",         # 05, 5
        "Function_6_3E1F",         # 06, 6
        "Function_7_3E44",         # 07, 7
        "Function_8_3E71",         # 08, 8
        "Function_9_3EC0",         # 09, 9
        "Function_10_3F39",        # 0A, 10
        "Function_11_3FB2",        # 0B, 11
        "Function_12_3FE6",        # 0C, 12
        "Function_13_4002",        # 0D, 13
        "Function_14_405A",        # 0E, 14
        "Function_15_40C5",        # 0F, 15
        "Function_16_4154",        # 10, 16
        "Function_17_41AC",        # 11, 17
        "Function_18_4217",        # 12, 18
        "Function_19_42A6",        # 13, 19
        "Function_20_42BE",        # 14, 20
        "Function_21_42FD",        # 15, 21
        "Function_22_4348",        # 16, 22
        "Function_23_43C3",        # 17, 23
        "Function_24_43ED",        # 18, 24
        "Function_25_442D",        # 19, 25
        "Function_26_4456",        # 1A, 26
        "Function_27_446E",        # 1B, 27
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_247")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_247")

    Return()

    # Function_0_238 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_25D")

    Return()

    # Function_1_248 end

    def Function_2_25E(): pass

    label("Function_2_25E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("chr/ch06710.itc", 0x1F)
    LoadChrToIndex("chr/ch11400.itc", 0x20)
    LoadChrToIndex("chr/ch11500.itc", 0x21)
    LoadChrToIndex("apl/ch51620.itc", 0x22)
    LoadChrToIndex("apl/ch51614.itc", 0x23)
    LoadChrToIndex("apl/ch51615.itc", 0x24)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadChrToIndex("apl/ch51619.itc", 0x26)
    SoundLoad(2917)
    SoundLoad(2918)
    SoundLoad(2919)
    SoundLoad(2920)
    SoundLoad(962)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis413.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12100.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    SetChrPos(0x101, -129880, 4000, -26390, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2000)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x2, 0x8)
    OP_49()
    SetChrPos(0x8, -127870, 4000, -35110, 0)
    OP_93(0x8, 0x5A, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x1, 0x20)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x2, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x2, "Null_senaka(42)")
    SetMapObjFrame(0x2, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x2, "879mabuta:Layer2(44)", 0x0, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x0, 0xE)
    OP_78(0x1, 0xF)
    OP_78(0x4, 0x10)
    OP_78(0x5, 0x11)
    SetChrPos(0xE, -136010, -1150, -71530, 0)
    SetChrPos(0x10, -136010, -1150, -71530, 0)
    SetChrPos(0xF, -123270, -1350, -76920, 0)
    SetChrPos(0x11, -123270, -1350, -76920, 0)
    OP_93(0xE, 0x0, 0x15E)
    OP_93(0x10, 0x0, 0x15E)
    OP_93(0xF, 0x0, 0x15E)
    OP_93(0x11, 0x0, 0x15E)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3000, 0, 0, 0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 4000, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    OP_70(0x3, 0x0)
    Sound(132, 2, 100, 0)
    BeginChrThread(0x12, 1, 0, 20)
    Sleep(2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(-207000, 1650, -16820, 0)
    MoveCamera(333, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(74640, 0)
    SetChrPos(0x8, -225000, 0, -24000, 0)
    BeginChrThread(0x8, 0, 0, 3)
    OP_68(-165050, 1650, -5550, 6000)
    MoveCamera(312, 34, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(56890, 6000)
    PlaceName2(340, 200, "c_plac65", 0x0, 0)
    Sleep(4500)
    StopSound(962, 2000, 40)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    SetChrPos(0x8, -132000, 4000, -31000, 0)
    OP_93(0x8, 0x46, 0x0)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_93(0x101, 0x0, 0x0)
    SetChrSubChip(0x101, 0x3)
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Sleep(1000)
    BeginChrThread(0x12, 1, 0, 21)
    FadeToBright(500, 0)
    SetCameraDistance(15390, 6000)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 4)
    Sleep(1000)
    OP_68(-129750, 7300, -28810, 4500)
    MoveCamera(263, 11, 0, 4500)
    OP_6E(600, 4500)
    OP_0D()
    Sleep(1000)
    SetChrPos(0xD, -128370, 7200, -29090, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x101, 0)
    Sleep(500)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00008F#5PThis place is... the\x01",
            "Republican border?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThe State Guard should\x01",
            "not be able to reach us\x01",
            "in this place.\x02",
        )
    )

    WaitChrThread(0x8, 0)
    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PFirst, let's take a\x01",
            "breather.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#NThank you, Zeit. ...You\x01",
            "really saved me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00011F#5PHuh─\x02",
    )

    CloseMessageWindow()
    OP_68(-146110, 10500, -23540, 3000)
    MoveCamera(260, 9, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15390, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F#6P#NWhat's that...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#6P#NSomething like a Barrier\x01",
            "that wraps Crossbell\x01",
            "City.\x02\x03",
            "They say that "allowed\x01",
            "existences" can freely\x01",
            "come and go...\x02\x03",
            "But existences that are\x01",
            "not, can't pass through\x01",
            "at all.\x02\x03",
            "Be they people or\x01",
            "vehicles.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00013F#6P#N...Such a thing...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Fade(500)
    OP_0D()
    OP_68(-129830, 6900, -28710, 80000)
    MoveCamera(235, 19, 0, 80000)
    OP_6E(600, 80000)
    SetCameraDistance(20000, 80000)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PPleroma Grass is already\x01",
            "in full bloom all over\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIt wouldn't be an exaggeration to\x01",
            "say that Crossbell itself has become\x01",
            "united with the Sept-Terrion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        (
            "#00008F#12PIn the end, what is\x01",
            "Pleroma Grass?\x02\x03",
            "I heard it's connected\x01",
            "to the septium vein\x01",
            "running underground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThey are said to be eyes the old Sept-\x01",
            "Terrion of Mirage caused to bloom, to\x01",
            "know the people of the surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PBy connecting spiritually with\x01",
            "the Sept-Terrion, they can also\x01",
            "warp the surrounding space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThey are likely the reason for the\x01",
            "appearance of the Cryptids, which do\x01",
            "not normally appear in this dimension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see...\x02\x03",
            "#00008F...The various inhuman\x01",
            "rituals the D∴G Cult\x01",
            "conducted long ago...\x02\x03",
            "#00013FThat was the reason Gnosis,\x01",
            "made with Pleroma Grass,\x01",
            "was used in them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PYes. The knowledge and\x01",
            "personalities of the many\x01",
            "subjects who were sacrificed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThat enormous quantity of information was\x01",
            "most likely transferred to the "girl" who\x01",
            "was sleeping at the Fort of Sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PTheir information self-organised\x01",
            "and became nourishment to bring\x01",
            "forth a more eminent character...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThen, after 500 years had\x01",
            "passed, the "core" of the\x01",
            "Sept-Terrion woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P#40W......\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P─This is all I can tell\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P"They" meticulously\x01",
            "shaped their plans and\x01",
            "created this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIn that sense, the\x01",
            "choices you can make are\x01",
            "very few.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat about fleeing\x01",
            "abroad until the storm\x01",
            "blows over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PHaha, right...\x02\x03",
            "#00008F...Uncle's home is in\x01",
            "Calvard, so that\x01",
            "wouldn't be so bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-130699, 6500, -28440, 0)
    MoveCamera(264, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17590, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#6P─But, I won't do that.\x02\x03",
            "#00000FI still have to\x01",
            "ascertain the truth I\x01",
            "want to know the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PAnd to ascertain that...\x01",
            "I need everyone's\x01",
            "strength.\x02\x03",
            "Elie, Tio, Randy. And\x01",
            "also the strength of\x01",
            "many others...\x02\x03",
            "#00008FTo do that... I'll\x01",
            "return "there".\x02\x03",
            "#00000FAlthough I'm sorry for\x01",
            "saying so after you\x01",
            "brought me all this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat is the truth you\x01",
            "want to ascertain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P─Isn't it obvious?\x02",
    )

    CloseMessageWindow()
    OP_68(-129470, 6300, -28970, 0)
    MoveCamera(263, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12800, 0)
    Fade(500)
    OP_0D()
    TurnDirection(0x101, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#12PIt's not her power, nor\x01",
            "her personal history...\x02\x03",
            "#00000FIt's what that kid, KeA,\x01",
            "really wants to do.\x02\x03",
            "Probably, unless I take\x01",
            "her back, she won't tell\x01",
            "me her true feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#12PAlso, to think she'll be exposed to\x01",
            "pressure so great, the former Sept-\x01",
            "Terrion couldn't withstand it...\x02\x03",
            "There's no way I could leave our\x01",
            "KeA in such circumstances, right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00010F#12P#4SI swear I'll bring her back!\x01",
            "Even if I have to beat the\x01",
            "President and Arios to do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#NHehe...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    StopBGM(0xFA0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x2000)
    SetChrFlags(0xC, 0x2000)
    SetChrFlags(0xA, 0x2000)
    SetChrFlags(0xB, 0x2000)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xA, 0, 0, 9)
    BeginChrThread(0xB, 0, 0, 10)
    Sleep(100)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Young Man's Voice",
        (
            "#11P#2917V#30W#25A#NAhaha, truly a doting\x01",
            "parent.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PHuh...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)
    OP_68(-137840, 4800, -46130, 0)
    MoveCamera(235, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18330, 0)
    Fade(500)
    OP_68(-133770, 4600, -39110, 4000)
    MoveCamera(227, 20, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(19660, 4000)
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x101, 0, 0, 12)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_6F(0x79)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x101,
        (
            "#00005F#6P#NWazy, how...\x02\x03",
            "#00011FAnd Abbas... And Ries\x01",
            "and you too!?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Abbas")

    AnonymousTalk(
        0xFF,
        "─Long time no see, Bannings.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        "It has been a long time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            "Heya. I guess it's been four months\x01",
            "for us?\x02\x03",
            "I'm happy you remember me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NIf I recall, you're Ries\x01",
            "from the Church's\x01",
            ""Gralsritter"...\x02\x03",
            "#00007FWazy, don't tell me\x01",
            "you're─!?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)
    Sound(2430, 255, 100, 0)

    NpcTalk(
        0x9,
        "Wazy",
        "#10404F#5PHehe...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    OP_68(-133770, 4600, -39110, 100000)
    MoveCamera(227, 19, 0, 100000)
    OP_6E(600, 100000)
    SetCameraDistance(16860, 100000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#2918V#30WSeptian Church, Gralsritter.\x02\x03",
            "#2919VDominion No. IX─ The Azure\x01",
            "Testament, Wazy Hemisphere.\x02\x03",
            "#2920VNice to meet you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB68)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00011F#6P............ (*agape*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12102F#5P...Incidentally, I hold\x01",
            "the position of knight\x01",
            "among them.\x02\x03",
            "Aiding Wazy is my main\x01",
            "duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P...Aah, enough! It's too\x01",
            "sudden and I don't know\x01",
            "what's what.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PT-Then...\x02\x03",
            "When we met for the first\x01",
            "time, Ries, you didn't say\x01",
            "anything to each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11P...I'm sorry. We\x01",
            "pretended to be\x01",
            "strangers.\x02\x03",
            "#13802FLord Hemisphere's\x01",
            "infiltration mission is\x01",
            "of the utmost secrecy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PAnd because she came, Archbishop\x01",
            "Eralda's suspicions were\x01",
            "completely misdirected, you know.\x02\x03",
            "#10402FMan, you were really a great\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13804F#11PI'm happy to have been\x01",
            "of service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PWell in Ries' case, she's doesn't\x01",
            "look like a normal sister no\x01",
            "matter how you slice it.\x02\x03",
            "#04302FI'm certain the Archbishop was\x01",
            "confused as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11P...That's none of your\x01",
            "business.\x02\x03",
            "#13811FAnd I don't think you're\x01",
            "one to talk, Kevin.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Not a single one of\x01",
            "them looks like a normal\x01",
            "clergyman...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5P─Well, that's about it\x01",
            "for the reintroductions.\x02\x03",
            "#10400FWe came because we were\x01",
            "called by him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x104, 0x1F4)

    ChrTalk(
        0x101,
        "#00011F#6PBy Zeit?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    WaitChrThread(0x8, 0)
    SetChrPos(0xD, -132240, 7300, -35100, 0)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#NYes, I did that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#NIf your resolve was firm,\x01",
            "I thought you would have\x01",
            "needed allies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6POh...\x02",
    )

    CloseMessageWindow()

    def lambda_2070():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2070)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#10406F#5PI think you figured it out because\x01",
            "of my infiltration, but...\x02\x03",
            "#10401FWe Gralsritter had predicted this\x01",
            "situation to a certain degree.\x02\x03",
            "However, there were many things we\x01",
            "didn't know, like the Crois clan's\x01",
            "conspiracy and KeA's true identity.\x02\x03",
            "We were given an overview the other\x01",
            "day, when we met up with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PAt any rate, the vanishing of the Sept-\x01",
            "Terrion of Mirage and the creation, by human\x01",
            "hands, of a new Sept-Terrion in its stead...\x02\x03",
            "The situation is far from the Knights' role\x01",
            "of "Artifact" recovery.\x02\x03",
            "We had no excuse for an intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04303F#11POn the other hand, we can't\x01",
            "leave things be since\x01",
            "Ouroboros is involved...\x02\x03",
            "#04300FAnd so, I thought to rely\x01",
            "on "you", as an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PExactly─\x02\x03",
            "#10402FI think we'll be allowed to\x01",
            "intervene in this matter in the\x01",
            "guise of collaborating with you.\x02\x03",
            "What do you say, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P─I want to confirm one\x01",
            "thing.\x02\x03",
            "#00013FWhat do you plan to\x01",
            "do... to KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#10408F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11P...That's a difficult\x01",
            "question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13808F#11PBut I don't think\x01",
            "there's any use in\x01",
            "trying to deceive him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PYes, we should honestly\x01",
            "tell him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5P...Right.\x02\x03",
            "#10401FThe Sept-Terrion of Zero is, to be quite honest,\x01",
            "a far more dangerous and troublesome existence\x01",
            "than the Sept-Terrion of Space, the Aureole.\x02\x03",
            "At present, despite the fact that we don't know\x01",
            "her full powers, she created this situation.\x02\x03",
            "#10406F─Do you know what's going on right now in the\x01",
            "other countries on the continent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PNo...\x02\x03",
            "#00001F...But I've heard a\x01",
            "civil war has started in\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PI'll be blunt. The direct cause was the\x01",
            "annihilation of the Imperial armored\x01",
            "division that invaded Crossbell.\x02\x03",
            "#04308FBecause the Empire has its pride, it sent\x01",
            "in one division after the next, but...\x01",
            "They were all destroyed by those "dolls".\x02\x03",
            "#04301FAnd while the Imperial Army was in chaos,\x01",
            "the Noble Alliance troops suddenly\x01",
            "occupied the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#12100F#5PAs a result, the Blood and\x01",
            "Iron Chancellor was shot and\x01",
            "he's nowhere to be found...\x02\x03",
            "And a civil war involving\x01",
            "the entire Empire has\x01",
            "started to drag on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11POn the other hand, an economic\x01",
            "panic stemming from Crossbell\x01",
            "broke out in the Republic...\x02\x03",
            "#13801FAnd due to an increase in acts\x01",
            "of terror, a state of\x01",
            "emergency has been declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P...Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5PNaturally, even other countries aren't immune\x01",
            "to panic and confusion.\x02\x03",
            "Especially in the regions that have been\x01",
            "oppressed until now by the Empire and Republic,\x01",
            "suspicious movements have begun to appear.\x02\x03",
            "#10408F─In this situation, it seems that President\x01",
            "Dieter has been appealing to all lands.\x02\x03",
            "#10401FTo join a new order with Crossbell as the\x01",
            "leading power, that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00013F#6P............\x02\x03",
            "#00003F...Naturally, with the\x01",
            "power of the Sept-\x01",
            "Terrion as a backdrop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5POf course.\x02\x03",
            "Its power easily repelled the Imperial army,\x01",
            "said to be the strongest in Zemuria.\x02\x03",
            "#10408FFurthermore, Ouroboros prepared only three\x01",
            "archaisms, but...\x02\x03",
            "#10402FWhat if more were produced, they all received\x01",
            "the power of the Sept-Terrion, and they were\x01",
            "sent to the far corners of the continent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PUgh...\x02\x03",
            "#00007F...KeA... She would\x01",
            "never do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5P─Incidentally, it's not the case that\x01",
            "those archaisms are controlled by the\x01",
            "Sept-Terrion.\x02\x03",
            "They're probably existences like\x01",
            "Guardians that receive the Sept-\x01",
            "Terrion's power and move autonomously.\x02\x03",
            "Like that Pater-Mater unit Renne was\x01",
            "using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11P...In that sense, they\x01",
            "aren't bound to that kid's\x01",
            "will, but move on their own.\x02\x03",
            "#04301FOn the contrary, it's\x01",
            "possible they can be used by\x01",
            "people unrelated to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11PAgainst KeA's will...\x02\x03",
            "#13808FWe can't ignore the\x01",
            "danger her power holds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()
    OP_68(-132290, 5000, -37670, 0)
    MoveCamera(1, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11P─I understand your point\x01",
            "of view.\x02\x03",
            "#00001FThen if you don't\x01",
            "mind... I'd like to ask\x01",
            "for your help.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#10405F#6PHuh?\x02\x03",
            "#10402FI thought you'd have\x01",
            "refused our proposal for\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PIt's a situation where I,\x01",
            "for sure, can't do anything\x01",
            "alone...\x02\x03",
            "#00008FAnd the more its resolution\x01",
            "drags on, the more that\x01",
            "child could suffer too...\x02\x03",
            "#00010F─But!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetCameraDistance(14300, 500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 250)
    Sound(802, 0, 70, 0)
    SetChrSubChip(0x101, 0x7)
    OP_6F(0x79)
    CancelBlur(0)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#11PIf you decide to deal with\x01",
            "KeA as you please!\x02\x03",
            "I'll tell you here and now,\x01",
            "that I'll oppose you with\x01",
            "everything I've got!\x02\x03",
            "#00003FAnd not just me either!\x01",
            "Elie, Tio, Randy... I'm sure\x01",
            "they'd say the same thing!\x02\x03",
            "#00013FThere's no logic nor reason\x01",
            "involved─ We're just her\x01",
            ""guardians"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#13805F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12102F#6P......Hm.........\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04304F#6PHaha. You're a bright\x01",
            "kid but so passionate.\x02\x03",
            "#04302FI feel like I understand\x01",
            "why you like him, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10409F#6PHehe. It's no\x01",
            "exaggeration to say I\x01",
            "love him, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#11PWazy, I'm being serious\x01",
            "here─!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(-133770, 4600, -39110, 0)
    MoveCamera(227, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16860, 0)
    Fade(500)
    OP_68(-133450, 4400, -39970, 2000)
    MoveCamera(227, 22, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14450, 2000)
    OP_0D()
    BeginChrThread(0x9, 0, 0, 25)
    WaitChrThread(0x9, 0)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "#10403F#5P─As a Knight of the Gral, I\x01",
            "swear upon Aidios's name.\x02\x03",
            "I promise I will absolutely\x01",
            "hear your opinion regarding\x01",
            "dealing with that kid.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-133770, 4600, -39110, 1500)
    MoveCamera(227, 19, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16860, 1500)
    Sleep(500)
    SetChrSubChip(0x9, 0x0)
    Sleep(130)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#10406F#5P...Given our position,\x01",
            "that's the most we can\x01",
            "do.\x02\x03",
            "#10402FWhat do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYeah... That's plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12102F#5P─Then it's settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04304F#11PAlright, let's get\x01",
            "moving at once.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0xA, 2, 0, 26)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x12, 1, 0, 22)
    StopSound(132, 1000, 30)
    OP_68(-134270, 4400, -39100, 2500)
    MoveCamera(227, 19, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(16860, 2500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#6PW-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12PHmm... That's quite a\x01",
            "nostalgic sound.\x02\x03",
            "The Church's Heaven's\x01",
            "Wheels, huh.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    SetChrPos(0xE, -136010, 41150, -71530, 0)
    SetChrPos(0x10, -136010, 41150, -71530, 0)
    SetChrPos(0xF, -123270, 46350, -76920, 0)
    SetChrPos(0x11, -123270, 46350, -76920, 0)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 16)
    BeginChrThread(0x101, 1, 0, 19)
    BeginChrThread(0x12, 1, 0, 23)
    BeginChrThread(0xA, 2, 0, 27)
    OP_68(-126850, 7200, -36760, 3000)
    MoveCamera(185, -18, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(9560, 3000)
    Sleep(1500)
    WaitChrThread(0xA, 2)

    def lambda_38E4():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38E4)
    Sleep(30)

    def lambda_38F4():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38F4)
    Sleep(30)

    def lambda_3904():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3904)
    Sleep(30)

    def lambda_3914():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_3914)
    Sleep(30)

    def lambda_3924():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3924)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)
    OP_68(-126020, 9000, -47760, 9000)
    MoveCamera(188, 23, 0, 9000)
    OP_6E(600, 9000)
    SetCameraDistance(24000, 9000)
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(4000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011F#12P#NA-Airships...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    BeginChrThread(0x12, 1, 0, 24)
    Fade(500)
    OP_68(-132090, 5900, -41380, 0)
    MoveCamera(359, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#13804F#5PThey're war airships called\x01",
            "Merkabah we Gralsritter use.\x02\x03",
            "#13802FIn addition to stealth\x01",
            "functions, they're equipped with\x01",
            "optical camouflage as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5PUsing these, we'll invade\x01",
            "Crossbell's airspace in\x01",
            "absolute secrecy...\x02\x03",
            "#10400FAre you ready, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4SYeah─ Of course!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-167100, 6900, -14880, 0)
    MoveCamera(262, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(52800, 0)
    Fade(500)
    SetCameraDistance(48800, 20000)
    OP_0D()
    StopSound(496, 1000, 30)
    StopSound(497, 1000, 30)
    Sleep(800)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F#6P#N#30W(KeA... ...And\x01",
            "everyone...)\x02\x03",
            "#00013F#30W(Please, wait for me!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(48800, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x3C2)
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x1F0)
    OP_29(0xAE, 0x1, 0x2)
    OP_29(0xAE, 0x4, 0x10)
    SubItemNumber(0x333, 1)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x22, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_25E end

    def Function_3_3D11(): pass

    label("Function_3_3D11")

    SetChrPos(0xFE, -250000, 0, -28000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -225000, 0, -24000)
    OP_9F(0x1, -210000, 0, -20750)
    OP_9F(0x1, -193000, 0, -15500)
    OP_9F(0x1, -173000, 0, -10500)
    OP_9F(0x1, -130000, 0, -5220)
    OP_9F(0x2, 0xFE, 20000, 0x6)
    Return()

    # Function_3_3D11 end

    def Function_4_3D7D(): pass

    label("Function_4_3D7D")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    OP_D3(0x101, 0xFF, "")
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0xFFFDFF4E, 0xFA0, 0xFFFF92A0, 0xFA, 0x3E8)
    Sound(326, 0, 40, 0)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_4_3D7D end

    def Function_5_3DFA(): pass

    label("Function_5_3DFA")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1A4, 0x1AE, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1AE, 0x1D6, 0x0, 0x20)
    Return()

    # Function_5_3DFA end

    def Function_6_3E1F(): pass

    label("Function_6_3E1F")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_6_3E1F end

    def Function_7_3E44(): pass

    label("Function_7_3E44")

    SetChrPos(0xFE, -137500, 4019, -45600, 30)
    OP_95(0xFE, -133390, 4000, -39760, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_7_3E44 end

    def Function_8_3E71(): pass

    label("Function_8_3E71")

    SetChrPos(0xFE, -138450, 3480, -47600, 90)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 2000, 0x2)
    OP_95(0xFE, -132640, 4000, -40680, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_8_3E71 end

    def Function_9_3EC0(): pass

    label("Function_9_3EC0")

    SetChrPos(0xFE, -144000, -40, -56500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -134290, 4000, -38890, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_9_3EC0 end

    def Function_10_3F39(): pass

    label("Function_10_3F39")

    SetChrPos(0xFE, -144000, 600, -54730, 30)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -135320, 4000, -38530, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_10_3F39 end

    def Function_11_3FB2(): pass

    label("Function_11_3FB2")

    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    SetChrPos(0x8, -131250, 4000, -31250, 215)
    OP_93(0x8, 0xD7, 0x1F4)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_11_3FB2 end

    def Function_12_3FE6(): pass

    label("Function_12_3FE6")

    OP_95(0xFE, -130300, 4000, -36350, 2000, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    Return()

    # Function_12_3FE6 end

    def Function_13_4002(): pass

    label("Function_13_4002")

    Sleep(1000)
    OP_71(0x4, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xE, 1, 0, 14)
    BeginChrThread(0x10, 1, 0, 14)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_75(0x0, 0x1, 0x0)
    OP_75(0x0, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x4, 0x1, 0x3E8)
    OP_75(0x6, 0x2, 0x1F4)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    Return()

    # Function_13_4002 end

    def Function_14_405A(): pass

    label("Function_14_405A")

    OP_96(0xFE, 0xFFFDECB6, 0x3E8, 0xFFFEE896, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x1F4, 0xFFFEE896, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x0, 0xFFFEE896, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFE0C, 0xFFFEE896, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFC18, 0xFFFEE896, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_14_405A end

    def Function_15_40C5(): pass

    label("Function_15_40C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4153")
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFAEC, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFD44, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0xC8, 0x1)
    Jump("Function_15_40C5")

    label("loc_4153")

    Return()

    # Function_15_40C5 end

    def Function_16_4154(): pass

    label("Function_16_4154")

    Sleep(2000)
    OP_71(0x5, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xF, 1, 0, 17)
    BeginChrThread(0x11, 1, 0, 17)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x4)
    OP_75(0x1, 0x1, 0x0)
    OP_75(0x1, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x5, 0x1, 0x3E8)
    OP_75(0x7, 0x2, 0x1F4)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)
    Return()

    # Function_16_4154 end

    def Function_17_41AC(): pass

    label("Function_17_41AC")

    OP_96(0xFE, 0xFFFE1E7A, 0x3E8, 0xFFFED388, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x1F4, 0xFFFED388, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x0, 0xFFFED388, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFE0C, 0xFFFED388, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFC18, 0xFFFED388, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 18)
    Return()

    # Function_17_41AC end

    def Function_18_4217(): pass

    label("Function_18_4217")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42A5")
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFAEC, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFD44, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0xC8, 0x1)
    Jump("Function_18_4217")

    label("loc_42A5")

    Return()

    # Function_18_4217 end

    def Function_19_42A6(): pass

    label("Function_19_42A6")

    Sleep(1000)
    OP_95(0xFE, -130310, 4100, -40610, 2000, 0x0)
    Return()

    # Function_19_42A6 end

    def Function_20_42BE(): pass

    label("Function_20_42BE")

    Sound(962, 2, 10, 0)
    Sleep(400)
    OP_25(0x3C2, 0xF)
    Sleep(400)
    OP_25(0x3C2, 0x14)
    Sleep(400)
    OP_25(0x3C2, 0x19)
    Sleep(400)
    OP_25(0x3C2, 0x1E)
    Sleep(400)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Return()

    # Function_20_42BE end

    def Function_21_42FD(): pass

    label("Function_21_42FD")

    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Return()

    # Function_21_42FD end

    def Function_22_4348(): pass

    label("Function_22_4348")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(300)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(300)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(300)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(300)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(300)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(300)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(300)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(300)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_22_4348 end

    def Function_23_43C3(): pass

    label("Function_23_43C3")

    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    OP_25(0x1F0, 0x46)
    Return()

    # Function_23_43C3 end

    def Function_24_43ED(): pass

    label("Function_24_43ED")

    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Return()

    # Function_24_43ED end

    def Function_25_442D(): pass

    label("Function_25_442D")

    Sleep(500)
    SetChrChipByIndex(0x9, 0x23)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    Sleep(120)
    SetChrSubChip(0x9, 0x0)
    Sleep(120)
    SetChrSubChip(0x9, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(300)
    Return()

    # Function_25_442D end

    def Function_26_4456(): pass

    label("Function_26_4456")

    SetChrChipByIndex(0xA, 0x24)
    Fade(250)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_26_4456 end

    def Function_27_446E(): pass

    label("Function_27_446E")

    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_27_446E end

    SaveToFile()

Try(main)
