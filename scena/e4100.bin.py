from ScenarioHelper import *

def main():
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
        "God wolf Zeit",           # 1
        "Guardian knight Waji",           # 2
        "Kevin Guardian",         # 3
        "Knight Lease",           # 4
        "Positive knight Abbas",         # 5
        "God wolf Zeit",           # 6
        "Mercapa",               # 7
        "Mercapa",               # 8
        "Mercapa optical camouflage",       # 9
        "Mercapa optical camouflage",       # 10
        "SE control",                 # 11
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
        "Function_3_3945",         # 03, 3
        "Function_4_39B1",         # 04, 4
        "Function_5_3A2E",         # 05, 5
        "Function_6_3A53",         # 06, 6
        "Function_7_3A78",         # 07, 7
        "Function_8_3AA5",         # 08, 8
        "Function_9_3AF4",         # 09, 9
        "Function_10_3B6D",        # 0A, 10
        "Function_11_3BE6",        # 0B, 11
        "Function_12_3C1A",        # 0C, 12
        "Function_13_3C36",        # 0D, 13
        "Function_14_3C8E",        # 0E, 14
        "Function_15_3CF9",        # 0F, 15
        "Function_16_3D88",        # 10, 16
        "Function_17_3DE0",        # 11, 17
        "Function_18_3E4B",        # 12, 18
        "Function_19_3EDA",        # 13, 19
        "Function_20_3EF2",        # 14, 20
        "Function_21_3F31",        # 15, 21
        "Function_22_3F7C",        # 16, 22
        "Function_23_3FF7",        # 17, 23
        "Function_24_4021",        # 18, 24
        "Function_25_4061",        # 19, 25
        "Function_26_408A",        # 1A, 26
        "Function_27_40A2",        # 1B, 27
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
            "#00008F#5Phere……\x01",
            "Is it the borders of the Republic?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIf it is here,\x01",
            "You will not come and extend your hand.\x02",
        )
    )

    WaitChrThread(0x8, 0)
    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PYou should take a breath\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#NThank you, Zeit.\x01",
            "…… I was really saved.\x02",
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
        "#00011F#5PHuh-\x02",
    )

    CloseMessageWindow()
    OP_68(-146110, 10500, -23540, 3000)
    MoveCamera(260, 9, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15390, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F#6P#NThat is!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#6P#NCrossbell like wrapping the city\x01",
            "It is like a \"barrier\" that appeared.\x02\x03",
            "About \"permissible existence\"\x01",
            "It seems I can freely go in and out ……\x02\x03",
            "Not being present\x01",
            "It seems that there is nothing to pass through.\x02\x03",
            "People, vehicles…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00013F#6P#NThey have that now…\x02",
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
            "#5PAlready \"Praroma Grass\" also\x01",
            "Blooming across the Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PNow the crossbell itself\x01",
            "\"It was integrated with\" treasure \"\x01",
            "It will not be an exaggeration to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        (
            "#00008F#12PWhat is \"pre-prawn grass\"\x01",
            "After all?\x02\x03",
            "In the underground streams\x01",
            "I heard that it is related ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5POnce the \"illusionary treasure\"\x01",
            "Know people and the ground#2RTo#It bloomed to bloom\x01",
            "Should I say it even as a looking eye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PBy being spiritually connected with \"treasure\"\x01",
            "It also distorts the surrounding space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5POriginally, it does not appear in this dimension\x01",
            "\"Gentile beast\" and others are also appearing\x01",
            "That may be the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see…\x02\x03",
            "#00008F…… Once the \"D∴G Church\"\x01",
            "A number of outrageous ceremonies that came … …\x02\x03",
            "#00013FIt was made from pre-prawn grass as raw material\x01",
            "Even the fact that \"Gnostic\" was used\x01",
            "There was a reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWell, probably a sacrifice\x01",
            "Many#4RSweet#The subject's knowledge and personality ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThose enormous information\x01",
            "To \"Sleep\" in \"Fort of the Sun\"\x01",
            "I guess it was being delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThe information is self-organized,\x01",
            "To create a higher personality\x01",
            "It becomes nursery bed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PAnd after 500 years,\x01",
            "I woke up \"nuclear\" of \"treasure\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P#40W…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P── I am sorry\x01",
            "This is about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P\"They\" carefully planned the plan,\x01",
            "I have created this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PIn that sense, you can get naked\x01",
            "The choices will be too few.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PUntil the blooms cool down like this\x01",
            "Why do not you escape to a foreign country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PHaha, that is true\x02\x03",
            "#00008F… … If it's a clubber\x01",
            "I have my uncle's house,\x01",
            "It may not be bad.\x02",
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
            "#00006F#6PBut no thanks\x02\x03",
            "#00000FThe truth that I want to know most\x01",
            "I have not checked it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PTo confirm that … ….\x01",
            "I need everyone's power.\x02\x03",
            "Eli, Tio, Randy.\x01",
            "Besides that, a lot of power … …\x02\x03",
            "#00008FTo that end I …\x01",
            "I will return to \"that side\".\x02\x03",
            "#00000FFar away until here\x01",
            "Though it is bad for me to send it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PWhat is the truth you want to find?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6PIt's obvious\x02",
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
            "#00008F#12PIt has nothing to do with power or growth\x02\x03",
            "#00000FThat girl is ── Ka\x01",
            "What do you really want?#20R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#That is it.\x02\x03",
            "Perhaps, unless you regain that child,\x01",
            "You will not tell me what you are supposed to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#12PPlus, once the \"treasure\"\x01",
            "Heavy pressure that was unbearable\x01",
            "It may be exposed …\x02\x03",
            "In such an environment, our keyer\x01",
            "Is there no reason to keep it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00010F#12P#4SPresident or Arios\x01",
            "Even if you strike you will never take it back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#NHah\x02",
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
        "Voice of a boy",
        "#11P#2917V#30W#25A#NAhah, you really are an overobsessed parent\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PHuh…\x02",
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
            "#00005F#6P#NWazy… why…\x02\x03",
            "#00011FAnd to Abbas …\x01",
            "To Lease, you are! Is it?\x02",
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
        "Long time no see, Bannings\x02",
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
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        "Nice to see you again\x02",
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
            "Yeah, with me\x01",
            "Is it the first time in 4 months?\x02\x03",
            "I'm happy you remember me\x02",
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
            "#00006F#6P#NCertainly you and Lease\x01",
            "Church's \"Star Cup Order\" … …\x02\x03",
            "#00007FWazy, no way, you…!?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)
    Sound(2430, 255, 100, 0)

    NpcTalk(
        0x9,
        "Waji",
        "#10404F#5PHah\x02",
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
            "#2918V#30WMember of the Septian Church Order of Chivarly\x02\x03",
            "#2919VGuardian Knight#8RDominion#No. 9 -\x01",
            "\"The Blue Book\" Wadi Hemisphere.\x02\x03",
            "#2920VNice to see you again\x02",
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
        "#00011F#6P………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12102F#5PBy the way, myself\x01",
            "It is in the position of a regular knight of the Order.\x02\x03",
            "Wazy's principal assistant\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P…… Oh no!\x01",
            "Suddenly suddenly what is what?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PSo that means…\x02\x03",
            "When I first met with Lease,\x01",
            "Why did not you say anything …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11P……Excuse me.\x01",
            "I was pretending to be unaware.\x02\x03",
            "#13802FInvestigation of Sir Hemisphere's infiltration\x01",
            "Because it was considered top secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PSo thanks to her coming\x01",
            "Eldar Archbishop's attention\x01",
            "It was not surprising that he diverted completely.\x02\x03",
            "#10402FIt was really a help\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#13804F#11PI'm honored that I could be helpful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PIn the case of leasing,\x01",
            "Whatever you think about ordinary sister\x01",
            "Let's see it.\x02\x03",
            "#04302FThe Archbishop was totally confused\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11PI was quite helpful\x02\x03",
            "#13811FI mean Kevin\x01",
            "I think that I can not say people.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Ordinary as anyone\x01",
            "I can not see it as a priest … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5P─ ─ Well, again\x01",
            "Please introduce yourself to this.\x02\x03",
            "#10400FIt was that we appeared in this place\x01",
            "Because he called to me there.\x02",
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
            "#11P#NYes, that is true\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#NIf your determination of stickiness is firm\x01",
            "I hope cooperators are necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh….\x02",
    )

    CloseMessageWindow()

    def lambda_1F41():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F41)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#10406F#5PEven as I was infiltrating\x01",
            "I think I understand ……\x02\x03",
            "#10401FTo some extent,\x01",
            "Predict this situation.\x02\x03",
            "However, Cloys' conspiracy\x01",
            "Regarding the identity of KEYA\x01",
            "There were many things I did not understand.\x02\x03",
            "As soon as I met him again,\x01",
            "I taught you all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PHowever, \"the treasure of the phantom\" has disappeared,\x01",
            "A new treasure instead of that\x01",
            "When it comes to being created with human hands ……\x02\x03",
            "The situation is \"ancient artifacts#8RArtifact#Recover\x01",
            "Get out of the role of the Order.\x02\x03",
            "In this way the excuse to intervene\x01",
            "It was a place to lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04303F#11PBut \"association\"\x01",
            "As it is involved in this situation\x01",
            "Okay, leave me alone …\x02\x03",
            "#04300FSo there is an excuse of \"you\"\x01",
            "I thought I'd rely on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5PSo that's it\x02\x03",
            "#10402FIn a way that will cooperate with you\x01",
            "For us this incident\x01",
            "I think that I will intervene.\x02\x03",
            "How about it Lloyd\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W…..\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PLet me confirm one thing\x02\x03",
            "#00013FYou guys ……\x01",
            "What are you going to do with Kaoru?\x02",
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
        "#10408F#5P…..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04306F#11PThat's a difficult question…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13808F#11PBut even if you misrepresent it\x01",
            "I think that it will not start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5PWell, to be honest\x01",
            "First of all I should tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5PRight…\x02\x03",
            "#10401F\"zero#2Rzero#The treasure of \"But, ──\x01",
            "To be honest, \"the treasure of the sky#8RAuroru#\"Than\x01",
            "It is far more dangerous and troublesome.\x02\x03",
            "At the moment, the whole picture of power\x01",
            "Despite being unseen,\x01",
            "I have made up the situation so far.\x02\x03",
            "#10406F── You are now the continental countries\x01",
            "Do you know what is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PNo…\x02\x03",
            "#00001F… … The civil war on the empire\x01",
            "I heard rumors about it that started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11PBukkake, direct opportunity\x01",
            "It was put in the direction of crossbell\x01",
            "That the Imperial Army Division was destroyed.\x02\x03",
            "#04308FThe Imperial Army also has pride\x01",
            "I sent out the division one after another\x01",
            "All the dolls have returned … …\x02\x03",
            "#04301FSo in the confusion of the Imperial Army\x01",
            "The Allied forces of aristocratic forces\x01",
            "I occupied Dengeki at Teito.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#12100F#5PAs a result, the Chancellor of Iron and Ireas collapsed,\x01",
            "I am missing … ….\x02\x03",
            "A civil war involving all the empire\x01",
            "It is a situation that has begun to be prolonged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13803F#11POn the other hand, even in the Republic\x01",
            "Start from the crossbell\x01",
            "An economic crisis has occurred ……\x02\x03",
            "#13801FBy actively activating terrorism\x01",
            "An emergency declaration has been issued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PIs that right…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5POf course, other countries\x01",
            "It is not related to depression or confusion.\x02\x03",
            "Especially in the Empire and the Republic\x01",
            "In the area that was being pressed down\x01",
            "Kina smelly movement is starting to appear.\x02\x03",
            "#10408FIn the meantime, President Dieter\x01",
            "She seems to be working on various places.\x02\x03",
            "#10401FMake Crossbell an alliance\x01",
            "Trying to participate in a new order.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00013F#6P…\x02\x03",
            "#00003F…… Of course, in the background\x01",
            "Is there the power of \"treasure\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10404F#5POf course\x02\x03",
            "The Imperial Army that is said to be the strongest continent on the continent\x01",
            "It's just enough to repel.\x02\x03",
            "#10408FMoreover, now \"association\" prepared\x01",
            "There are only three doll weapons ….\x02\x03",
            "#10402FIt is increased production,\x01",
            "Everything received the power of \"treasure\"\x01",
            "Why do not you fly across the continent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PUgh\x02\x03",
            "#00007F…… Kaoru ……\x01",
            "That child does not do such a thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12100F#5P─ ─ By the way that doll weapon\x01",
            "The treasure is not manipulating it.\x02\x03",
            "Receive the power of treasure, act autonomously\x01",
            "It may be like a \"guardian\".\x02\x03",
            "That daughter called Ren used it\x01",
            "Like the aircraft called \"Patel = Mattel\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PAh….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04306F#11P…… In that sense,\x01",
            "Regardless of that child's will\x01",
            "I mean that you move on your own.\x02\x03",
            "#04301FOn the contrary,\x01",
            "There is even the possibility of being used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#13806F#11PKeA's will aside\x02\x03",
            "#13808FThe danger that that \"power\" has is\x01",
            "It can be ignored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P…..\x02",
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
            "#00003F#11PI understand your opinion\x02\x03",
            "#00001FI do not mind that … …\x01",
            "I would like to ask for cooperation now.\x02",
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
            "#10402FMake a clear offer\x01",
            "I thought I'd be wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PIt's just a matter of myself.\x01",
            "It is certain that there is no … …\x02\x03",
            "#00008FThe longer the solution prolongs\x01",
            "That girl may also suffer … …\x02\x03",
            "#00010FBut!\x02",
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
            "#00007F#11PIf you do not do it\x01",
            "If you decide to treat Ka'aa!\x02\x03",
            "Only by stopping with full power\x01",
            "I will tell you in this place now!\x02\x03",
            "#00003FNot only me!\x01",
            "Eli, Tio, Randy\x01",
            "I bet he should say the same thing!\x02\x03",
            "#00013FRegardless of reason and reasoning ─\x01",
            "Just as the \"guardian\" of that child!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#13805F#6PAh….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12102F#6PHmm\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04304F#6PHa ha, like a brilliant person\x01",
            "Mechamacha hot brother and.\x02\x03",
            "#04302FWas this review helpful?\x01",
            "I feel like I can understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10409F#6PEven if it says that I love you\x01",
            "It is not an exaggeration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#11PWazy… I'm being serious!\x02",
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
            "#10403F#5P── As a knight of the star cup\x01",
            "goddess#4REidos#Let's swear by betting on the name of.\x02\x03",
            "Regarding treatment of that child\x01",
            "Your opinion\x01",
            "I promise to always hear it.\x02",
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
            "#10406F#5P…… as our position\x01",
            "This neighborhood is the limit though.\x02\x03",
            "#10402FHow's that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYeah, that's fine\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12102F#5PThen it's decided\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04304F#11POK, soon,\x01",
            "Let's start moving.\x02",
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
        "#00005F#6PW-what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12PHm …\x01",
            "It sounds a lot of nostalgic.\x02\x03",
            "Is that the Heavenly Ship of the church?\x02",
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

    def lambda_3530():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3530)
    Sleep(30)

    def lambda_3540():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3540)
    Sleep(30)

    def lambda_3550():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3550)
    Sleep(30)

    def lambda_3560():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_3560)
    Sleep(30)

    def lambda_3570():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3570)
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
        "#00011F#12P#NA-airships!?\x02",
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
            "#13804F#5PI use it in the Star Cup Order\x01",
            "It is a strategy boat called \"Mercapa\".\x02\x03",
            "#13802FIn addition to the stealth function,\x01",
            "It has optical camouflage function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10403F#5PUse this to keep secrets behind\x01",
            "Sneak into Cross Bell airspace … …\x02\x03",
            "#10400FAre you prepared, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#11P#4SYeah, of course!\x02",
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
            "#00003F#6P#N#30W(Keya …\x01",
            "… and everyone … …)\x02\x03",
            "#00013F#30W(Wait for me..!)\x02",
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
    SubItemNumber('蓝花', 1)
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

    def Function_3_3945(): pass

    label("Function_3_3945")

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

    # Function_3_3945 end

    def Function_4_39B1(): pass

    label("Function_4_39B1")

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

    # Function_4_39B1 end

    def Function_5_3A2E(): pass

    label("Function_5_3A2E")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1A4, 0x1AE, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1AE, 0x1D6, 0x0, 0x20)
    Return()

    # Function_5_3A2E end

    def Function_6_3A53(): pass

    label("Function_6_3A53")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_6_3A53 end

    def Function_7_3A78(): pass

    label("Function_7_3A78")

    SetChrPos(0xFE, -137500, 4019, -45600, 30)
    OP_95(0xFE, -133390, 4000, -39760, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_7_3A78 end

    def Function_8_3AA5(): pass

    label("Function_8_3AA5")

    SetChrPos(0xFE, -138450, 3480, -47600, 90)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 2000, 0x2)
    OP_95(0xFE, -132640, 4000, -40680, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_8_3AA5 end

    def Function_9_3AF4(): pass

    label("Function_9_3AF4")

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

    # Function_9_3AF4 end

    def Function_10_3B6D(): pass

    label("Function_10_3B6D")

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

    # Function_10_3B6D end

    def Function_11_3BE6(): pass

    label("Function_11_3BE6")

    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    SetChrPos(0x8, -131250, 4000, -31250, 215)
    OP_93(0x8, 0xD7, 0x1F4)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_11_3BE6 end

    def Function_12_3C1A(): pass

    label("Function_12_3C1A")

    OP_95(0xFE, -130300, 4000, -36350, 2000, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    Return()

    # Function_12_3C1A end

    def Function_13_3C36(): pass

    label("Function_13_3C36")

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

    # Function_13_3C36 end

    def Function_14_3C8E(): pass

    label("Function_14_3C8E")

    OP_96(0xFE, 0xFFFDECB6, 0x3E8, 0xFFFEE896, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x1F4, 0xFFFEE896, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x0, 0xFFFEE896, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFE0C, 0xFFFEE896, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFC18, 0xFFFEE896, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_14_3C8E end

    def Function_15_3CF9(): pass

    label("Function_15_3CF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D87")
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFAEC, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFD44, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0xC8, 0x1)
    Jump("Function_15_3CF9")

    label("loc_3D87")

    Return()

    # Function_15_3CF9 end

    def Function_16_3D88(): pass

    label("Function_16_3D88")

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

    # Function_16_3D88 end

    def Function_17_3DE0(): pass

    label("Function_17_3DE0")

    OP_96(0xFE, 0xFFFE1E7A, 0x3E8, 0xFFFED388, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x1F4, 0xFFFED388, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x0, 0xFFFED388, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFE0C, 0xFFFED388, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFC18, 0xFFFED388, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 18)
    Return()

    # Function_17_3DE0 end

    def Function_18_3E4B(): pass

    label("Function_18_3E4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ED9")
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFAEC, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFD44, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0xC8, 0x1)
    Jump("Function_18_3E4B")

    label("loc_3ED9")

    Return()

    # Function_18_3E4B end

    def Function_19_3EDA(): pass

    label("Function_19_3EDA")

    Sleep(1000)
    OP_95(0xFE, -130310, 4100, -40610, 2000, 0x0)
    Return()

    # Function_19_3EDA end

    def Function_20_3EF2(): pass

    label("Function_20_3EF2")

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

    # Function_20_3EF2 end

    def Function_21_3F31(): pass

    label("Function_21_3F31")

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

    # Function_21_3F31 end

    def Function_22_3F7C(): pass

    label("Function_22_3F7C")

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

    # Function_22_3F7C end

    def Function_23_3FF7(): pass

    label("Function_23_3FF7")

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

    # Function_23_3FF7 end

    def Function_24_4021(): pass

    label("Function_24_4021")

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

    # Function_24_4021 end

    def Function_25_4061(): pass

    label("Function_25_4061")

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

    # Function_25_4061 end

    def Function_26_408A(): pass

    label("Function_26_408A")

    SetChrChipByIndex(0xA, 0x24)
    Fade(250)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_26_408A end

    def Function_27_40A2(): pass

    label("Function_27_40A2")

    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_27_40A2 end

    SaveToFile()

Try(main)
