from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t100b.bin",                # FileName
        "t100b",                    # MapName
        "t100b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t100b",                  # 0
        "Crew salsa",           # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "girl",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Water-bus",               # 7
        "SE control",                 # 8
        "Direction to the theme park",       # 9
        "Destination towards a mansion",               # 10
        "To the lake bath area",           # 11
    ))

    AddCharChip((
        "chr/ch28400.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "chr/ch20300.itc",                   # 02
        "chr/ch22300.itc",                   # 03
        "chr/ch21300.itc",                   # 04
        "chr/ch24400.itc",                   # 05
    ))

    DeclNpc(4294963556, 4294963296, 4294920116, 180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(9600,    4294963296, 4294919366, 268,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294960956, 4294963296, 4294919966, 225,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294960427, 4294963296, 4294919017, 45,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(8069,    4294963296, 4294919166, 86,   389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(8699,    4294963296, 4294917866, 45,   389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(23450,   4294962296, 4294912366, 1200,    29380,   4294961296, 4294911866, 0x007C, 0,  9,  0x0000)
    DeclActor(10350,   4294963306, 4294920886, 1200,    10350,   4294964796, 4294920886, 0x007C, 0,  12, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "Direction to the theme park")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "Destination towards a mansion")
    PlaceName(75.0, 0.0, 15.0, 0x0000, 0x0000, "To the lake bath area")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ChipFrameInfo(600, 0)                                        # 0

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_3B9",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_5D4",          # 05, 5
        "Function_6_64C",          # 06, 6
        "Function_7_6A3",          # 07, 7
        "Function_8_734",          # 08, 8
        "Function_9_7D8",          # 09, 9
        "Function_10_8AC",         # 0A, 10
        "Function_11_9A4",         # 0B, 11
        "Function_12_9C0",         # 0C, 12
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_258 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_3A9")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_3A9")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_35A")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_3A9")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_368")
    Jump("loc_3A9")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_376")
    Jump("loc_3A9")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_384")
    Jump("loc_3A9")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_392")
    Jump("loc_3A9")

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3A0")
    Jump("loc_3A9")

    label("loc_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_3A9")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3B8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 10)

    label("loc_3B8")

    Return()

    # Function_1_308 end

    def Function_2_3B9(): pass

    label("Function_2_3B9")

    SetMapObjFlags(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DC")
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0x1E)
    Jump("loc_3E2")

    label("loc_3DC")

    SetMapObjFlags(0x0, 0x4)

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407")
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    Jump("loc_419")

    label("loc_407")

    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)

    label("loc_419")

    Sound(126, 1, 80, 0)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 29380, -6000, -55430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_3B9 end

    def Function_3_46A(): pass

    label("Function_3_46A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4DA")

    ChrTalk(
        0x8,
        "Our staff will depart in due course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are returning to Cros Bell City\x01",
            "Please hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4E8")
    Jump("loc_4FF")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F6")
    Jump("loc_4FF")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4FF")

    label("loc_4FF")

    TalkEnd(0xFE)
    Return()

    # Function_3_46A end

    def Function_4_503(): pass

    label("Function_4_503")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5B9")

    ChrTalk(
        0x9,
        (
            "Since we created a theme park\x01",
            "I came to Mishram for the first time … …\x01",
            "No, I really enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Especially that \"Hoorie Kotaeta\"\x01",
            "It was a real crimele.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C7")
    Jump("loc_5D0")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5D0")

    label("loc_5D0")

    TalkEnd(0xFE)
    Return()

    # Function_4_503 end

    def Function_5_5D4(): pass

    label("Function_5_5D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_631")

    ChrTalk(
        0xA,
        "I will not say selfishly anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I will bring you again, is not it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_648")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_63F")
    Jump("loc_648")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_648")

    label("loc_648")

    TalkEnd(0xFE)
    Return()

    # Function_5_5D4 end

    def Function_6_64C(): pass

    label("Function_6_64C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_688")

    ChrTalk(
        0xB,
        (
            "Hey!\x01",
            "I'm still playing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69F")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_696")
    Jump("loc_69F")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_69F")

    label("loc_69F")

    TalkEnd(0xFE)
    Return()

    # Function_6_64C end

    def Function_7_6A3(): pass

    label("Function_7_6A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_719")

    ChrTalk(
        0xC,
        (
            "Hehe, grandpa\x01",
            "It seems that they liked the theme park quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You should come back again this time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_730")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_727")
    Jump("loc_730")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_730")

    label("loc_730")

    TalkEnd(0xFE)
    Return()

    # Function_7_6A3 end

    def Function_8_734(): pass

    label("Function_8_734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7BD")

    ChrTalk(
        0xD,
        (
            "To celebrate the birth of Grandpa\x01",
            "I got a trip with my brother and sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you are pleased with this\x01",
            "It was worth giving gifts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D4")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_7D4")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7D4")

    label("loc_7D4")

    TalkEnd(0xFE)
    Return()

    # Function_8_734 end

    def Function_9_7D8(): pass

    label("Function_9_7D8")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
    )

    CloseMessageWindow()
    OP_68(27760, -3400, -57630, 1500)
    MoveCamera(315, 28, 0, 1500)
    OP_6E(300, 1500)
    SetCameraDistance(35500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A7")
    OP_E2(0x2)
    MiniGame(0x6, 0x5, 0x5B9A, 0xFFFFEC78, 0xFFFF296E, 0x5A, 0x72C4, 0xFFFFE890, 0xFFFF277A)

    label("loc_8A7")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_9_7D8 end

    def Function_10_8AC(): pass

    label("Function_10_8AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5070, -5500, -38200, 270)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(0, 5000, -38000, 0)
    MoveCamera(325, 12, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(115000, 0)

    def lambda_952():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_952)
    BeginChrThread(0xF, 1, 0, 11)
    FadeToBright(1000, 0)
    OP_68(0, 5000, 10000, 13000)
    Sleep(9000)
    OP_0D()
    StopSound(126, 2000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t108B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_8AC end

    def Function_11_9A4(): pass

    label("Function_11_9A4")

    Sound(475, 0, 60, 0)
    Sound(476, 0, 60, 0)
    Sound(477, 0, 60, 0)
    Sleep(3000)
    Sound(477, 0, 50, 0)
    Return()

    # Function_11_9A4 end

    def Function_12_9C0(): pass

    label("Function_12_9C0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル市》行きWater-bus・時刻表\x01\x01",
            "※ For further visit\x01",
            "We are waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_12_9C0 end

    SaveToFile()

Try(main)
