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
        "Function_3_3E30",         # 03, 3
        "Function_4_3E9C",         # 04, 4
        "Function_5_3F19",         # 05, 5
        "Function_6_3F3E",         # 06, 6
        "Function_7_3F63",         # 07, 7
        "Function_8_3F90",         # 08, 8
        "Function_9_3FDF",         # 09, 9
        "Function_10_4058",        # 0A, 10
        "Function_11_40D1",        # 0B, 11
        "Function_12_4105",        # 0C, 12
        "Function_13_4121",        # 0D, 13
        "Function_14_4179",        # 0E, 14
        "Function_15_41E4",        # 0F, 15
        "Function_16_4273",        # 10, 16
        "Function_17_42CB",        # 11, 17
        "Function_18_4336",        # 12, 18
        "Function_19_43C5",        # 13, 19
        "Function_20_43DD",        # 14, 20
        "Function_21_441C",        # 15, 21
        "Function_22_4467",        # 16, 22
        "Function_23_44E2",        # 17, 23
        "Function_24_450C",        # 18, 24
        "Function_25_454C",        # 19, 25
        "Function_26_4575",        # 1A, 26
        "Function_27_458D",        # 1B, 27
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
            "#00008F#5PThis place is...\x01",
            "The Republican border?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIn this place the State Guard\x01",
            "shouldn't be able to reach us.\x02",
        )
    )

    WaitChrThread(0x8, 0)
    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PFirst of all, let's take a breather.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#NThank you, Zeit.\x01",
            "...You really saved me.\x02",
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
        "#00011F#5PHuh────\x02",
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
            "#6P#NSomething like a "barrier"\x01",
            "that wraps Crossbell City.\x02\x03",
            "They say that "allowed existences" \x01",
            "can freely come and go...\x02\x03",
            "But existences that are not,\x01",
            "can't pass through at all.\x02\x03",
            "Be they people or vehicles.\x02",
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
            "#5P"Pleroma Grass" is already blooming\x01",
            "in profusion all around Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIt wouldn't be an exaggeration\x01",
            "to say that Crossbell itself has\x01",
            "become united with the "Sept-Terrion".\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        (
            "#00008F#12PIn the end, what's\x01",
            ""Pleroma Grass"?\x02\x03",
            "I heard it's connected to the Septium\x01",
            "vein running underground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PYou could say it's like an eye the old\x01",
            ""Sept-Terrion of Mirage" made bloom\x01",
            "to understand people and the surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PBy connecting spiritually with the "Sept-Terrion",\x01",
            "it can also warp the surrounding space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThat's also probably the cause of the\x01",
            "appearance of the "Cryptids". By nature, \x01",
            "they shouldn't show up in this dimension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see...\x02\x03",
            "#00008F...The many inhuman rituals the\x01",
            ""D∴G Cult" did back in the day...\x02\x03",
            "#00013FThat was also the reason why\x01",
            ""Gnosis", made with Pleroma\x01",
            "Grass, was used, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PHm, probably the knowledge and personalities\x01",
            "of the many subjects who were sacrificed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PTheir enormous quantity of information\x01",
            "was sent over to the "girl" who was\x01",
            "sleeping at the "Fort of Sun".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PTheir information was self-organised\x01",
            "and became nourishment to bring forth\x01",
            "a more eminent character...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThen, after 500 years had passed,\x01",
            "the "core" of the "Sept-Terrion" woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P#40W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──This is what\x01",
            "I can tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P"They" meticulously shaped their \x01",
            "plans and created this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIn that sense, the choices\x01",
            "you can make are very few.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat about fleeing abroad\x01",
            "until the storm blows over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PHa ha, right...\x02\x03",
            "#00008F...In Calvard there's\x01",
            "uncle's home too, so\x01",
            "it wouldn't be bad.\x02",
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
            "#00006F#6P──But, I won't do that.\x02\x03",
            "#00000FI still have to ascertain the\x01",
            "truth I want to know the most.\x02",
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
            "#00003F#6PEven in order to ascertain that...\x01",
            "I need everyone's strength.\x02\x03",
            "Elie, Tio, Randy. And also\x01",
            "the strength of many others...\x02\x03",
            "#00008FTo do that...\x01",
            "I'll return "there".\x02\x03",
            "#00000FAlthough I'm sorry for you\x01",
            "who brought me all the way here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat is the truth you want to ascertain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P──It's obvious.\x02",
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
            "#00008F#12PIt's not her power, nor her personal history...\x02\x03",
            "#00000FIt's what that kid, KeA,\x01",
            "really wants to do.\x02\x03",
            "I guess that unless I take that kid back,\x01",
            "she won't tell me her true feelings.\x02",
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
            "#00006F#12PAlso, to be exposed to such\x01",
            "pressure that the old "Sept-\x01",
            "Terrion" couldn't withstand...\x02\x03",
            "There's no way I could leave our KeA\x01",
            "in such circumstances, right?\x02",
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
            "President and Mr. Arios to do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#NHu hu...\x02",
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
        "#11P#2917V#30W#25A#NAhaha, truly a doting parent.\x02",
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
            "#00011FAnd Abbas...\x01",
            "And Miss Ries and you too!?\x02",
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
        "──Long time no see, Bannings.\x02",
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
            "Heya, it's been\x01",
            "four months for us?\x02\x03",
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
            "#00006F#6P#NI'm sure you and Miss Ries are\x01",
            ""Gralsritter" from the Church...\x02\x03",
            "#00007FWazy, don't tell me you're too──!?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)
    Sound(2430, 255, 100, 0)

    NpcTalk(
        0x9,
        "Wazy",
        "#10404F#5PHu hu...\x02",
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
            "#2919VDominion No. IX── the "Azure\x01",
            "Testament", Wazy Hemisphere.\x02\x03",
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
        "#00011F#6P............(*agape*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12102F#5P...Incidentally, I hold the\x01",
            "position of Knight among them.\x02\x03",
            "Being Wazy's aid is my main duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P...Aah, enough!\x01",
            "It's too sudden and I don't know what's what.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PT-Then...\x02\x03",
            "When we met for the first time, Miss Ries,\x01",
            "you didn't tell anything each other...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11P...I am sorry.\x01",
            "We pretended to be strangers.\x02\x03",
            "#13802FLord Hemisphere's undercover mission\x01",
            "is regarded as an absolute secrecy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PAnd so, thanks to her coming,\x01",
            "Archbishop Eralda's watchfulness\x01",
            "went completely astray, you know.\x02\x03",
            "#10402FMan, you were really of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#13804F#11PI am happy to have been of service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PWell, in case of Ries, no matter\x01",
            "what you think, she's someone\x01",
            "who doesn't look like a normal sister.\x02\x03",
            "#04302FI'm sure the Archbishop too was bewildered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11P...That's none of your business.\x02\x03",
            "#13811FAnd I think you're not someone\x01",
            "who can tell on others, Kevin.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Somehow no one would see\x01",
            "him as a normal clergyman...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5P──Well, let's leave our\x01",
            "re-introductions at this.\x02\x03",
            "#10400FWe came here because\x01",
            "we were called by him.\x02",
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
            "#11P#NHm, I did that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#NIf your resolve was firm, I thought\x01",
            "you would've needed collaborators.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    def lambda_20F1():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20F1)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#10406F#5PI think you figured it out\x01",
            "since I infiltrated, but...\x02\x03",
            "#10401FThe Knights had predicted this\x01",
            "situation to a certain degree.\x02\x03",
            "However, there were many things we\x01",
            "didn't know too, like the Crois Clan\x01",
            "conspiracy and KeA's true identity.\x02\x03",
            "We were generally informed the\x01",
            "other day, when we met with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PAt any rate, the vanishing of the "Sept-Terrion\x01",
            "of Mirage" and the creation, by human hands,\x01",
            "of a new Sept-Terrion in his stead...\x02\x03",
            "The situation is far from the Knights' \x01",
            "role of "Artifacts" recovering.\x02\x03",
            "We didn't have an excuse for\x01",
            "an intervention anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04303F#11POn the other hand, we can't\x01",
            "leave things be since the\x01",
            ""Society" is involved...\x02\x03",
            "#04300FSo, I thought to rely on "you",\x01",
            "as an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PExactly──\x02\x03",
            "#10402FI think we'll be allowed to intervene\x01",
            "in this matter under the guise of\x01",
            "collaborating with you.\x02\x03",
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
            "#00006F#6P──I want to confirm one thing.\x02\x03",
            "#00013FWhat do you plan to do...\x01",
            "To KeA?\x02",
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
        "#04306F#11P...That's a difficult question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13808F#11PBut I think that nothing\x01",
            "will come by deceiving him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PHm, we should\x01",
            "tell him frankly first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5P...Right.\x02\x03",
            "#10401FThe "Sept-Terrion of Zero" is, honestly, a far\x01",
            "more dangerous and troublesome existence than\x01",
            "the Sept-Terrion of Space, the "Aureole".\x02\x03",
            "At this point, although we\x01",
            "don't know her full powers,\x01",
            "she created such a situation.\x02\x03",
            "#10406F──Do you know what's going on now in\x01",
            "the other countries on the continent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PNo...\x02\x03",
            "#00001F...But I've heard that a civil\x01",
            "war has started in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PTo be honest, the direct cause was the\x01",
            "annihilation of the Imperial Armored Division\x01",
            "that was committed to the Crossbell region.\x02\x03",
            "#04308FBecause the Empire has got its pride too,\x01",
            "it sent in one division after the other, but...\x01",
            "They were all destroyed by those "dolls".\x02\x03",
            "#04301FSo, while the Imperial Army was in\x01",
            "confusion, the Noble Alliance troops\x01",
            "suddenly occupied the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#12100F#5PAs a result, the Blood and Iron Chancellor\x01",
            "was shot and he's nowhere to be found...\x02\x03",
            "And a long-term civil war began to\x01",
            "involve the whole Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11POn the other hand, an economic\x01",
            "panic, stemming from Crossbell,\x01",
            "broke out in the Republic...\x02\x03",
            "#13801FAnd due to the increase of terrorists activities,\x01",
            "the state of emergency has been proclaimed.\x02",
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
            "#10403F#5PNaturally, even other countries\x01",
            "aren't immune to panic and confusion.\x02\x03",
            "Especially in the regions that have been\x01",
            "oppressed until now by the Empire and Republic,\x01",
            "suspicious movements have begun to appear.\x02\x03",
            "#10408F──In this situation, it seems that President\x01",
            "Dieter has been appealing to all lands.\x02\x03",
            "#10401FTo join a new order with Crossbell\x01",
            "as leading power, that is.\x02",
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
            "#00003F...Of course, the "Sept-Terrion"\x01",
            "power is involved in that setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5POf course.\x02\x03",
            "It's the power that was able to \x01",
            "readily repel the Imperial Army, \x01",
            "said to be the strongest of Zemuria.\x02\x03",
            "#10408FFurthermore, there're only three archaisms\x01",
            "that the "Society" prepared, but...\x02\x03",
            "#10402FWon't their production be increased,\x01",
            "they will all receive the "Sept-Terrion"\x01",
            "power and sent all over Zemuria?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PKh...\x02\x03",
            "#00007F...KeA...\x01",
            "That child won't do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5P──Incidentally, it's not the case that those\x01",
            "archaisms are controlled by the Sept-Terrion.\x02\x03",
            "They're probably existences like \x01",
            ""guardians" that receive the Sept-Terrion \x01",
            "power and move autonomously.\x02\x03",
            "Like the unit called "Pater-Mater" that\x01",
            "that girl called Renne was using.\x02",
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
            "#04306F#11P...In that sense, they aren't\x01",
            "related to that kid's will,\x01",
            "but they move on their own.\x02\x03",
            "#04301FOn the contrary, it's possible\x01",
            "they can be used by people\x01",
            "unrelated to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11PDifferent from KeA's will...\x02\x03",
            "#13808FWe can't ignore the risk\x01",
            "that much "power" holds.\x02",
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
            "#00003F#11P─I understand your point of view.\x02\x03",
            "#00001FIf you don't mind it...\x01",
            "I want to ask for your help.\x02",
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
            "#10405F#6PEeh...?\x02\x03",
            "#10402FI thought you'd have refused\x01",
            "our proposal for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PIt's a situation where I, for sure,\x01",
            "can't do anything alone...\x02\x03",
            "#00008FThe more its resolution drags on,\x01",
            "the more that child could suffer too...\x02\x03",
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
            "#00007F#11PIf you will try to deal\x01",
            "with KeA as you please!\x02\x03",
            "I'll tell you here, and now, that I'll \x01",
            "hinder you with everything I've got!\x02\x03",
            "#00003FAnd it's not just me!\x01",
            "Elie, Tio, Randy...\x01",
            "I'm sure they'd say the same thing!\x02\x03",
            "#00013FNo logic nor reason involved──\x01",
            "We're just her "guardians"!\x02",
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
            "#04304F#6PHaha, you're an intelligent person,\x01",
            "and yet a really passionate man.\x02\x03",
            "#04302FWazy, I think I understand\x01",
            "why you like him too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10409F#6PHu hu, I don't exaggerate\x01",
            "when I say I love him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#11PWazy, I'm serious here──!\x02",
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
            "#10403F#5P──As a Knight of the Gral,\x01",
            "I swear upon Aidios's name.\x02\x03",
            "I promise I will absolutely\x01",
            "hear your opinion regarding\x01",
            "how to deal with that kid.\x02",
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
            "#10406F#5P...This is the maximum we can\x01",
            "do considering our position.\x02\x03",
            "#10402FWhat about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYeah...it's plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12102F#5P──Then it's settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04304F#11PAlright, let's begin\x01",
            "to move at once.\x02",
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
            "#12PHmm...\x01",
            "That's quite a nostalgic sound.\x02\x03",
            "The Church's "Heaven's Wheels", hm?\x02",
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

    def lambda_39ED():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39ED)
    Sleep(30)

    def lambda_39FD():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_39FD)
    Sleep(30)

    def lambda_3A0D():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3A0D)
    Sleep(30)

    def lambda_3A1D():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_3A1D)
    Sleep(30)

    def lambda_3A2D():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3A2D)
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
            "#13804F#5PThey're war airships called "Merkabah"\x01",
            "we Gralsritter use.\x02\x03",
            "#13802FIn addition to stealth functions, they're\x01",
            "equipped with optical camouflage too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5PUsing these, we'll intrude in absolute\x01",
            "secrecy into Crossbell's airspace...\x02\x03",
            "#10400FHave you mentally prepared, Lloyd!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4SYeah── of course!\x02",
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
            "#00003F#6P#N#30W(KeA...\x01",
            "...And everyone...)\x02\x03",
            "#00013F#30W(Please wait for me...!)\x02",
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

    def Function_3_3E30(): pass

    label("Function_3_3E30")

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

    # Function_3_3E30 end

    def Function_4_3E9C(): pass

    label("Function_4_3E9C")

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

    # Function_4_3E9C end

    def Function_5_3F19(): pass

    label("Function_5_3F19")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1A4, 0x1AE, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1AE, 0x1D6, 0x0, 0x20)
    Return()

    # Function_5_3F19 end

    def Function_6_3F3E(): pass

    label("Function_6_3F3E")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_6_3F3E end

    def Function_7_3F63(): pass

    label("Function_7_3F63")

    SetChrPos(0xFE, -137500, 4019, -45600, 30)
    OP_95(0xFE, -133390, 4000, -39760, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_7_3F63 end

    def Function_8_3F90(): pass

    label("Function_8_3F90")

    SetChrPos(0xFE, -138450, 3480, -47600, 90)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 2000, 0x2)
    OP_95(0xFE, -132640, 4000, -40680, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_8_3F90 end

    def Function_9_3FDF(): pass

    label("Function_9_3FDF")

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

    # Function_9_3FDF end

    def Function_10_4058(): pass

    label("Function_10_4058")

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

    # Function_10_4058 end

    def Function_11_40D1(): pass

    label("Function_11_40D1")

    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    SetChrPos(0x8, -131250, 4000, -31250, 215)
    OP_93(0x8, 0xD7, 0x1F4)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_11_40D1 end

    def Function_12_4105(): pass

    label("Function_12_4105")

    OP_95(0xFE, -130300, 4000, -36350, 2000, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    Return()

    # Function_12_4105 end

    def Function_13_4121(): pass

    label("Function_13_4121")

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

    # Function_13_4121 end

    def Function_14_4179(): pass

    label("Function_14_4179")

    OP_96(0xFE, 0xFFFDECB6, 0x3E8, 0xFFFEE896, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x1F4, 0xFFFEE896, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x0, 0xFFFEE896, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFE0C, 0xFFFEE896, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFC18, 0xFFFEE896, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_14_4179 end

    def Function_15_41E4(): pass

    label("Function_15_41E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4272")
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFAEC, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFD44, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0xC8, 0x1)
    Jump("Function_15_41E4")

    label("loc_4272")

    Return()

    # Function_15_41E4 end

    def Function_16_4273(): pass

    label("Function_16_4273")

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

    # Function_16_4273 end

    def Function_17_42CB(): pass

    label("Function_17_42CB")

    OP_96(0xFE, 0xFFFE1E7A, 0x3E8, 0xFFFED388, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x1F4, 0xFFFED388, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x0, 0xFFFED388, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFE0C, 0xFFFED388, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFC18, 0xFFFED388, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 18)
    Return()

    # Function_17_42CB end

    def Function_18_4336(): pass

    label("Function_18_4336")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C4")
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFAEC, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFD44, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0xC8, 0x1)
    Jump("Function_18_4336")

    label("loc_43C4")

    Return()

    # Function_18_4336 end

    def Function_19_43C5(): pass

    label("Function_19_43C5")

    Sleep(1000)
    OP_95(0xFE, -130310, 4100, -40610, 2000, 0x0)
    Return()

    # Function_19_43C5 end

    def Function_20_43DD(): pass

    label("Function_20_43DD")

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

    # Function_20_43DD end

    def Function_21_441C(): pass

    label("Function_21_441C")

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

    # Function_21_441C end

    def Function_22_4467(): pass

    label("Function_22_4467")

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

    # Function_22_4467 end

    def Function_23_44E2(): pass

    label("Function_23_44E2")

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

    # Function_23_44E2 end

    def Function_24_450C(): pass

    label("Function_24_450C")

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

    # Function_24_450C end

    def Function_25_454C(): pass

    label("Function_25_454C")

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

    # Function_25_454C end

    def Function_26_4575(): pass

    label("Function_26_4575")

    SetChrChipByIndex(0xA, 0x24)
    Fade(250)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_26_4575 end

    def Function_27_458D(): pass

    label("Function_27_458D")

    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_27_458D end

    SaveToFile()

Try(main)
