from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4200.bin",                # FileName
        "e4200",                    # MapName
        "e4200",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4200",                  # 0
        "God wolf Zeit",           # 1
        "God wolf Zeit",           # 2
        "Lloyd",                 # 3
        "Lloyd",                 # 4
        "SE control",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20500,   4500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(15500,   5500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(16000,   4949,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_158",          # 01, 1
        "Function_2_16D",          # 02, 2
        "Function_3_1FC8",         # 03, 3
        "Function_4_203F",         # 04, 4
        "Function_5_2073",         # 05, 5
        "Function_6_209B",         # 06, 6
        "Function_7_20C3",         # 07, 7
        "Function_8_20E0",         # 08, 8
        "Function_9_20F6",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_157")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_157")

    Return()

    # Function_0_148 end

    def Function_1_158(): pass

    label("Function_1_158")

    OP_F0(0x1, 0x4B0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0x190, 0x0)
    Return()

    # Function_1_158 end

    def Function_2_16D(): pass

    label("Function_2_16D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51620.itc", 0x20)
    SoundLoad(132)
    SoundLoad(962)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    SetChrPos(0x8, 16000, 0, 0, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x0, "Null_senaka(42)")
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 3)
    BeginChrThread(0xC, 2, 0, 4)
    Sleep(4000)
    PlayBGM("ed7304", 0)
    OP_68(32000, 5000, 0, 0)
    MoveCamera(330, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(69420, 0)
    FadeToBright(1000, 0)
    OP_68(17500, 5800, 0, 6000)
    MoveCamera(320, 18, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(18500, 6000)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    OP_68(17550, 6100, 0, 30000)
    MoveCamera(326, 3, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15500, 30000)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00011F#5PThe goddess sends#2RMound#My holy beast ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell, such an existence#4Rthing#When\x01",
            "It will be quick to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11POnce a gift from the goddess,\x01",
            "Great Treasures of the Seven#8RSept-Terion#\"… ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PTo watch over those goings\x01",
            "It is us that keep on staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00003F#5PWe?\x02\x03",
            "#00001FPossibly due to Libert incident\x01",
            "Also \"dragon\" that appeared … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHum, truly Satoshi#2RSato#Ina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PEven the Dragon Regnart\x01",
            "Surely my brothers#4RHiragana#It is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PTo watch \"the treasure of the sky\"\x01",
            "I remained in the land of Libert … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PNow solved from \"mission\"\x01",
            "I do not know where it disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00006F#5PThat's crazy…\x02\x03",
            "#00008FBut then also Zeit\x01",
            "From long ago to the crossbell land …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell, 1200 years ago\x01",
            "Before the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11POnce \"the treasure of the phantom\"\x01",
            "Why has it disappeared ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAfter that, to reproduce the treasure\x01",
            "What kind of things were done ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PSomewhat awareness#2RTo#ing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(17150, 6100, 0, 0)
    MoveCamera(313, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00006F#5P…… To be honest, to investigate\x01",
            "It was a part I could not find out.\x02\x03",
            "#00008FThe treasure of the goddess ……\x01",
            "Clois family who inherited it … …\x02\x03",
            "Why is the treasure lost,\x01",
            "Ka'a has such a role\x01",
            "Was it supposed to be carried on the back …?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xA,
        (
            "#00001F#5P── I beg you.\x01",
            "Please let me know.\x02\x03",
            "What happened 1200 years ago?\x02\x03",
            "And 500 years ago,\x01",
            "I wonder what happened to Ka'aa.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(18000, 5500, 0, 2500)
    MoveCamera(310, 3, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PVery well then\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell, for that I am\x01",
            "It appeared before the nakedness.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x1, 0x1)
    StopBGM(0x1770)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThe Master of Aidos who were sent to this land\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PIt governs \"vision\"\x01",
            "\"The False God#8RDemi-gols#\"It was called.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P\"Phantom\" governs perception and recognition,\x01",
            "Furthermore, it is an attribute that also controls \"causation\".\x02\x03",
            "To the treasure harboring its power,\x01",
            "He focused on the Clois family at the time\x01",
            "What the human faction wanted … …\x02\x03",
            "It is a goddess#4REidos#Instead of …\x01",
            "It was a role as a \"god\" on the earth.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis272.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PIdentifying people#2RTo#Ri地上の全てを識#2RTo#Ri\x01",
            "Leading humans by controlling causality ……\x02\x03",
            "It seemingly unlimited human desire\x01",
            "The treasure of \"Empty treasure#8RAuroru#\"Also\x01",
            "There would have been anything in common.\x02\x03",
            "However, \"the treasure of the vision#8RDemi-gols#\"…\x01",
            "By being given a high personality\x01",
            "I did not make the same mistake.\x02\x03",
            "It does not degenerate to the last,\x01",
            "Wisdom and judgment that can lead correctly …\x02\x03",
            "With that, the existence of a person\x01",
            "It was supposed to be guided correctly.\x02\x03",
            "─ ─ \"heart\" of the treasure itself\x01",
            "I have only to reach the limit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis273.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PEveryone's sex#2RSaka#With#2RLike this#,\x01",
            "Absurdity of every world -\x02\x03",
            "To understand and guide it\x01",
            "It means having the same \"emotions\" as people do.\x02\x03",
            "And \"the treasure of the vision#8RDemi-gols#\"Heart\" is\x01",
            "It gradually broke and went sick.\x02\x03",
            "If it remains as it is,\x01",
            "It hurts people to protect … …\x02\x03",
            "The treasure you realized so - ─\x01",
            "I made one decision at the end of my troubles.\x02\x03",
            "myself#4R噵 噵#Solving the causal cause of existence,\x01",
            "To extinguish from this world#20R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#The way that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16500, 5800, 0, 0)
    MoveCamera(322, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    Sound(223, 0, 60, 0)
    Sound(934, 0, 70, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    Sleep(1000)
    Sound(934, 0, 40, 0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(700)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    Sleep(300)
    FadeToBright(1500, 16777215)
    OP_0D()
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00006F#5PThat's what happened…\x02\x03",
            "#00013FBut then, then\x01",
            "People left after … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell - to the extinction of treasure\x01",
            "I was awfully awful, sorrowful, afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAnd why was it so,\x01",
            "I wonder what the treasure thought and thought\x01",
            "Without worrying ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PEquivalent to the lost treasure#4Rthing#To\x01",
            "It was possessed by creating.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1500, 100)
    StopSound(962, 1500, 60)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11POf course at first\x01",
            "It was just a fumble.\x02\x03",
            "However over 700 years,\x01",
            "While collecting various knowledge\x01",
            "I invented my own technology.\x02\x03",
            "In other words, it is said to create yes\x01",
            "Magic skill called \"alchemy\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis274.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAnd they said, in this place\x01",
            "I made a tremendous and far-reaching plan.\x02\x03",
            "We prepared a puppet called \"cult\"\x01",
            "The presence of becoming a \"nucleus\" of new treasure\x01",
            "To entrust and bring up … …\x02\x03",
            "And the concept of \"training\"\x01",
            "Huge \"formula\" applied to the limit\x01",
            "To prepare in this area …\x02\x03",
            "It was several hundred years ago ──\x01",
            "The Alchemist of the Cloyce family\x01",
            "It was a plan I started.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis275.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PTo make it possible financially,\x01",
            "They mask the mask of the table \"banker\"\x01",
            "It will start to suffer … …\x02\x03",
            "Meanwhile, if you are a \"cult\"\x01",
            "The \"nuclear\" given as a subject of faith\x01",
            "I started to wiggle to awaken.\x02\x03",
            "And the time of 500 years passed …\x01",
            "It is a translation that it reached the current situation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    SetChrSubChip(0x101, 0x2)
    FadeToBright(1500, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    ChrTalk(
        0xA,
        (
            "#00006F#5PIt's a story without reason\x02\x03",
            "#00008FBut finally … the whole picture of the incident\x01",
            "I feel like I'm starting to see it.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    OP_68(17500, 5800, 0, 2500)

    ChrTalk(
        0xA,
        (
            "#00003F#5P─ ─ Zeit.\x01",
            "Mr. Maria Bell went to Kea\x01",
            "\"zero#2Rzero#It was said that \"treasure of the.\x02\x03",
            "#00013FWhat does that mean?\x02\x03",
            "What is lost \"illusionary treasure\"\x01",
            "Is it another thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PUnfortunately……\x01",
            "I do not even know about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PPerhaps the Clois family,\x01",
            "At the end of 1200 years of imbalances\x01",
            "I guessed \"something\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThereby\x01",
            "\"The treasure of the vision#8RDemi-gols#\"And the equivalent existence\x01",
            "Not only to reproduce … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHas the power beyond that\x01",
            "It seems that he completed \"Zero's treasure\".\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis276.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThat white doll#4RHuman gutta#Power of.\x02\x03",
            "That is not the power of the doll itself,\x01",
            "It should be seen as the power of \"treasure\".\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis277.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAnd, \"The treasure of the vision\"\x01",
            "I can do that for a moment\x01",
            "I did not have the power.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis278.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThe power to eliminate space is\x01",
            "Somewhat like \"sky\" attribute\x01",
            "It is derived.\x02\x03",
            "If that is not everything ……\x01",
            "How much potential do you have?\x01",
            "I can not imagine it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 2, 0, 6)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00008F#5PI see..\x02\x03",
            "#00003F…\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00006F#5PTell me one more thing\x02\x03",
            "#00008FAs long as I heard the story so far,\x01",
            "That girl … …\x02\x03",
            "#00001F…… Kaoru ……\x01",
            "You are not a normal human being, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PSomething inanimate of the form of humanity\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PTo reproduce \"treasure\"\x01",
            "The existence created as \"nuclear\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PPerhaps with the mystery of alchemy\x01",
            "Rebuilt \"artificial life#8RHomemurkus#\"right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00008F#30W#5P….\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis279.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis280.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis281.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis282.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00006F#5P#30W(Maybe … … from a while ago\x01",
            "You knew … …)\x02\x03",
            "(Nevertheless in front of us\x01",
            "Laugh like that … …)\x02\x03",
            "#00008F(KeA….)\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 7)
    MoveCamera(30, 5, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(52000, 6000)
    Sleep(1000)
    OP_68(12000, 5000, 0, 5000)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("e4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_16D end

    def Function_3_1FC8(): pass

    label("Function_3_1FC8")

    Sound(132, 2, 20, 0)
    Sleep(200)
    OP_25(0x84, 0x19)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Sleep(200)
    OP_25(0x84, 0x23)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x2D)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x37)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(2000)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x64)
    Return()

    # Function_3_1FC8 end

    def Function_4_203F(): pass

    label("Function_4_203F")

    Sleep(200)
    Sound(962, 2, 30, 0)
    Sleep(2000)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Sleep(400)
    OP_25(0x3C2, 0x37)
    Sleep(400)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_4_203F end

    def Function_5_2073(): pass

    label("Function_5_2073")

    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x1E)
    Return()

    # Function_5_2073 end

    def Function_6_209B(): pass

    label("Function_6_209B")

    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_6_209B end

    def Function_7_20C3(): pass

    label("Function_7_20C3")

    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(850)
    SetChrSubChip(0x101, 0x4)
    Sleep(1500)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    Return()

    # Function_7_20C3 end

    def Function_8_20E0(): pass

    label("Function_8_20E0")

    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Return()

    # Function_8_20E0 end

    def Function_9_20F6(): pass

    label("Function_9_20F6")

    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    Return()

    # Function_9_20F6 end

    SaveToFile()

Try(main)
