from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1560.bin",                # FileName
        "c1560",                    # MapName
        "c1560",                    # Location
        0x00AC,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 172, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1560",                  # 0
        "President Dieter",       # 1
        "Kibun Sigmund",         # 2
        "Charlie",             # 3
        "Wald",               # 4
        "Marybele",             # 5
        "Secretary Arios",           # 6
        "Security guard",                 # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_1AC",          # 01, 1
        "Function_2_24B",          # 02, 2
        "Function_3_17C1",         # 03, 3
        "Function_4_180B",         # 04, 4
        "Function_5_1855",         # 05, 5
        "Function_6_1B09",         # 06, 6
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_1AB")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1AB")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_1AB")

    Return()

    # Function_0_174 end

    def Function_1_1AC(): pass

    label("Function_1_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_24A")

    Return()

    # Function_1_1AC end

    def Function_2_24B(): pass

    label("Function_2_24B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch03300.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch03800.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 150, 116200, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16800, 0, 111600, 90)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18000, 0, 111300, 90)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19600, 0, 111800, 90)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    VolumeBGM(0x46, 0x7D0)
    OP_68(19500, 2000, 111500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(250, 90, -1, -1)
    SetChrName("Grace")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─ ─ From here onwards\x01",
            "A scoop of many from my side\x01",
            "I will tell you.\x02\x03",
            "First of all it happened two months ago\x01",
            "Although it is the Crossbell City raid incident ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(18000, 1200, 113500, 2000)
    MoveCamera(39, 18, 0, 2000)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11301F#5P…… This unpleasant picture\x01",
            "At any moment#4RWhen#Will it continue until?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E9():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4E9)
    Sleep(100)

    def lambda_4F9():
        OP_93(0xD, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_4F9)
    Sleep(100)

    def lambda_509():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_509)
    Sleep(100)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0xC,
        (
            "#12P#02913FBecause I could grasp the intrusion route,\x01",
            "Physical blocking\x01",
            "I am in the middle of doing it.\x02\x03",
            "#02912FIt will be another two minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10503FAbout the street screens\x01",
            "We have already started withdrawal.\x02\x03",
            "#10500FThe citizen will soon leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11303FHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04500FHuh, it was a good surprise.\x02\x03",
            "#04504FBangs that interweave falsehood#4RMogyu#… ….\x01",
            "Is it the meaning of an old soldier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11306F#5PWhat is like other people's affairs ……\x02\x03",
            "#11310FBecause you guys missed the chairman\x01",
            "I wonder if it was like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04504FNo, about that\x01",
            "There is no choice but to apologize.\x02\x03",
            "#04502FHowever, as argued here,\x01",
            "All root#10R噵 噵 噵 噵 噵#If you crush\x01",
            "It should have been such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#11303FThe baby#4RMiko#There is also a mood of Den.\x02\x03",
            "#11301FTo the stakeholders of the support department\x01",
            "I can not do anything unrelenting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02913FHuff, I have a toothy crow\x01",
            "There is no choice but to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10503F…… even for the military officers outside the city\x01",
            "There should be not a little influence.\x02\x03",
            "#10500FLet's restore it somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11303FOh, I beg you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    MoveCamera(39, 18, 0, 4000)
    OP_68(18000, 1200, 108500, 4000)

    def lambda_902():
        OP_96(0xFE, 0x4650, 0x0, 0x182B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_902)
    Sleep(500)

    def lambda_91F():

        label("loc_91F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_91F")

    QueueWorkItem2(0x9, 2, lambda_91F)
    Sleep(100)

    def lambda_934():

        label("loc_934")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_934")

    QueueWorkItem2(0xC, 2, lambda_934)
    WaitChrThread(0xD, 1)
    Sound(103, 0, 100, 0)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(18000, 1200, 113500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sound(104, 0, 100, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9A7():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_9A7)
    Sleep(100)

    def lambda_9B7():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_9B7)
    Sleep(100)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x9,
        (
            "#12P#04503F─ ─ So we also\x01",
            "Let's make it into the forearm.\x02\x03",
            "#04504F\"Black moon#4RHayuue#Resistance to … ….\x02\x03",
            "#04502FEarnest#4R噵 噵#I will have you hunt it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02912FI and the people of \"association\"\x01",
            "I will keep in touch.\x02\x03",
            "#02913FChurch ship and support department ……\x01",
            "I need to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11301FOh, go ahead.\x02",
    )

    CloseMessageWindow()

    def lambda_B1D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B1D)
    WaitChrThread(0xC, 2)
    SetCameraDistance(16000, 3000)

    def lambda_B37():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B37)
    Sleep(100)

    def lambda_B54():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B54)
    WaitChrThread(0x9, 2)

    def lambda_B65():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B65)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, 13000, 0, 3000, 180)
    SetChrPos(0xC, 13000, 0, 3000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    OP_68(13000, 1300, -1100, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    MoveCamera(41, 21, 0, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_C3E():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C3E)

    def lambda_C58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C58)
    Sleep(1000)

    def lambda_C6C():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C6C)

    def lambda_C86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C86)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5P#04504FHuh, good grief.\x02\x03",
            "#04500FDear Father\x01",
            "It seems that the ending is not enough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    ChrTalk(
        0xC,
        (
            "#12P#02906FWell, even with a wishful thought\x01",
            "I want to think.\x02\x03",
            "#02913FRearrange the order across the continent\x01",
            "A grand plan … ….\x02\x03",
            "#02902FBy all means my father alone\x01",
            "There is a limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#04504FSo excellent staff\x01",
            "That's why I lend a lot of power.\x02\x03",
            "#04500FSwords and swords, that man sauce#8R噵 噵 噵 噵#like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P#02913FHuh, that is it.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27500, 0, -600, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, -1500, 270)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    NpcTalk(
        0xA,
        "Voice of a girl",
        "Dad, are you finished talking?\x02",
    )

    CloseMessageWindow()

    def lambda_ED1():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ED1)
    Sleep(50)

    def lambda_EEE():
        OP_96(0xFE, 0x4010, 0x0, 0xFFFFFA24, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EEE)

    def lambda_F08():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F08)
    Sleep(50)

    def lambda_F18():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_F18)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(24500, 1100, -1100, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_68(14500, 1100, -1100, 4500)
    SetCameraDistance(16500, 4500)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11P#04609FOh, it is Bell lady!\x01",
            "Yahoo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01608F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02909Fふふ、Charlieさんは\x01",
            "I am always fine.\x02\x03",
            "#02902FAbout the story of the example\x01",
            "Did you think about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#04605FOh, my lady's private unit\x01",
            "Was it the top?\x02\x03",
            "#04606FYeah, it sounds interesting\x01",
            "I also like the current environment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#5P#04501FWell, in front of me\x01",
            "Do not pull out dignifiedly\x01",
            "I would like to receive it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    ChrTalk(
        0xC,
        (
            "#12P#02904FOh, this is rude.\x02\x03",
            "#02912FWell then, Sigmund.\x01",
            "Regarding future arrangements\x01",
            "As I told you earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#04504FOh, I got it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#04500F#5P── Boy.\x01",
            "What about you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1209():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1209)

    ChrTalk(
        0xB,
        (
            "#01603F#11P…… I am your\x01",
            "Remember I did not become a friend.\x02\x03",
            "#01600FI will let you do it on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04504FFu … Well it will be nice.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#5P#04602FWald、その気があれば\x01",
            "Because I'll train you\x01",
            "You can come any time is not it ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01601F#11PPhew\x02",
    )

    CloseMessageWindow()
    OP_68(19500, 1200, -1100, 4000)
    MoveCamera(51, 17, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)

    def lambda_1343():

        label("loc_1343")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1343")

    QueueWorkItem2(0xB, 2, lambda_1343)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(14700, 1200, -1650, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    EndChrThread(0xB, 0x2)

    ChrTalk(
        0xC,
        (
            "#6P#02913FGiggle\x01",
            "They are reliable people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#01603F… … Father girl#4ROyako#It is a mistake.\x02\x03",
            "#01602FEven equal opportunity you are\x01",
            "I think that it is a considerable tama.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02909FUhufu …\x02\x03",
            "#02912FDo you regret it?\x01",
            "I got on my invitation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#11P#01604FHappy … is not it?\x02\x03",
            "#01603FThanks to the medicine you gave me\x01",
            "I got \"Tikara\" ……\x02\x03",
            "#01602FIt seems like everyone can not master\x01",
            "It is overwhelming \"Tikara\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02913FHuh, that's right.\x02\x03",
            "魔人化した時のWaldさんは\x01",
            "Power#4RLaw#Then the strongest person … …\x02\x03",
            "#02902FFor us as well\x01",
            "It is a unique sample.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#01604FWell, at best I'm willing\x01",
            "I am going to be a guinea pig.\x02\x03",
            "#01601FCrush that bastard … …\x01",
            "To prove who is the best.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── In this way,\x01",
            "The aftermath due to the invalid declaration being issued\x01",
            "It gradually spread to domestic and overseas.\x02\x03",
            "The movement in the city wrapped in the barrier\x01",
            "杳#2RYo#I could not have known … …\x02\x03",
            "Movement of soldiers of defense army is not small,\x01",
            "At the Belgard gate, Tangram gate and so on\x01",
            "The disturbance of the command system also began to surface.\x02\x03",
            "Something like that - ─\x01",
            "Melcova to board the Lloyd's\x01",
            "A contact from a person came in.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x23, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_24B end

    def Function_3_17C1(): pass

    label("Function_3_17C1")


    def lambda_17C6():
        OP_95(0xFE, 35000, 0, -100, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17C6)
    WaitChrThread(0x9, 1)

    def lambda_17E4():
        OP_95(0xFE, 40000, 0, -100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17E4)

    def lambda_17FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17FE)
    Return()

    # Function_3_17C1 end

    def Function_4_180B(): pass

    label("Function_4_180B")


    def lambda_1810():
        OP_95(0xFE, 35000, 0, -700, 2800, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1810)
    WaitChrThread(0xA, 1)

    def lambda_182E():
        OP_95(0xFE, 40000, 0, -700, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_182E)

    def lambda_1848():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1848)
    Return()

    # Function_4_180B end

    def Function_5_1855(): pass

    label("Function_5_1855")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    OP_68(18000, 1300, 104100, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 100, 116250, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 18000, 0, 90000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    Sound(103, 0, 100, 0)
    OP_68(18000, 1300, 114100, 7000)
    SetCameraDistance(14500, 7000)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1942():
        OP_96(0xFE, 0x4650, 0x0, 0x1B580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1942)
    WaitChrThread(0xE, 1)
    OP_64(0xE)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    def lambda_1991():
        OP_96(0xFE, 0x4650, 0x96, 0x1C520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1991)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrSubChip(0x8, 0x1)
    Sound(886, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#11307F#4S\"The barrier\" has disappeared! Is it?\x02\x03",
            "#11310FDamn\x01",
            "The members of \"Society\" are also not good.\x02\x03",
            "#11303FIn this way all \"God machine#4RIron#The\x01",
            "Should I turn to city defense ……\x02\x03",
            "#11307FPlease call Secretary of Defense!\x01",
            "Bell and Sigmunds too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PWell, I understand!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_93(0xE, 0xB4, 0x1F4)

    def lambda_1AE0():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1AE0)
    OP_0D()
    EndChrThread(0xE, 0xFF)
    OP_6F(0x79)
    SetScenarioFlags(0x23, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1855 end

    def Function_6_1B09(): pass

    label("Function_6_1B09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18000, 200, 116400, 180)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    OP_68(18000, 1200, 115600, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_6_1B09 end

    SaveToFile()

Try(main)
