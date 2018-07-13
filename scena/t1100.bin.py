from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1100",                  # 0
        "Jaeger Sachs",           # 1
        "Jaeger",                 # 2
        "Jaeger",                 # 3
        "Jaeger",                 # 4
        "Jaeger",                 # 5
        "Military Dog",           # 6
        "Military Dog",           # 7
        "SE制御",                 # 8
        "bt1010",                 # 9
        "To Hotel Delphinia",     # 10
    ))

    ATBonus("ATBonus_280", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_340", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_324", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_32C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_330", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_334", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_338", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_360", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42002.dat", "ms41902.dat", "ms41902.dat", "ms86100.dat", "ms86100.dat", 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_320", "ed7540", "ed7453", "ATBonus_280"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51706.itc",                   # 00
        "chr/ch00000.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   1.5,                   -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 18,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_411",          # 01, 1
        "Function_2_4C6",          # 02, 2
        "Function_3_17A3",         # 03, 3
        "Function_4_17B6",         # 04, 4
        "Function_5_17C9",         # 05, 5
        "Function_6_17D3",         # 06, 6
        "Function_7_17EE",         # 07, 7
        "Function_8_180F",         # 08, 8
        "Function_9_1830",         # 09, 9
        "Function_10_1EE6",        # 0A, 10
        "Function_11_1F03",        # 0B, 11
        "Function_12_1F20",        # 0C, 12
        "Function_13_1F38",        # 0D, 13
        "Function_14_1F50",        # 0E, 14
        "Function_15_1F79",        # 0F, 15
        "Function_16_1F8F",        # 10, 16
        "Function_17_25AC",        # 11, 17
        "Function_18_2646",        # 12, 18
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    Event(0, 2)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_410")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_410")

    Return()

    # Function_0_3F0 end

    def Function_1_411(): pass

    label("Function_1_411")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_44D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476")
    Call(0, 17)

    label("loc_476")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_4C5")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4C5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_4C5")

    Return()

    # Function_1_411 end

    def Function_2_4C6(): pass

    label("Function_2_4C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51323.itc", 0x1E)
    SetChrPos(0x101, 0, 0, -32000, 0)
    SetChrPos(0x153, 0, 0, -17000, 0)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -21500, 6000)
    MoveCamera(0, 20, 0, 6000)
    SetCameraDistance(28000, 6000)
    Sleep(3500)

    def lambda_562():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)
    BeginChrThread(0xF, 1, 0, 7)

    ChrTalk(
        0x101,
        "#00001F#6P#N(In such a place...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -16500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x153,
        "#01108F#40W#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12P#NKeA, so you were here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0xB4, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0x153,
        "#01102F#5PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -17000, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_69E():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFBD98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69E)

    def lambda_6B8():

        label("loc_6B8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6B8")

    QueueWorkItem2(0x153, 2, lambda_6B8)
    Sleep(4000)

    def lambda_6CD():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFBD98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6CD)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x153, 0x2)
    OP_6F(0x79)
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 40, "c_plac73", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#12P#NHa ha, how nostalgic.\x02\x03",
            "#00000F...Do you remember?\x01",
            "We escaped together from here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01104F#12P#NEheheh...\x01",
            "How could I forget?\x02\x03",
            "#01121FAfter all, KeA's memories\x01",
            "began from here, no?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00002F#12P#N...I know.\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01103F#12P#NSay, Lloyd.\x02\x03",
            "#01101FKeA was here, but... The place were\x01",
            "she belonged to, is another one, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#12P#NYeah...\x02\x03",
            "#00001F...As I thought, are you concerned...\x01",
            "About your own origins?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01106F#12P#N...Yes.\x02\x03",
            "Somehow, it's been bothering me\x01",
            "little by little, as of late...\x02\x03",
            "#01108FI heard from you all that\x01",
            "I was born a ton of time before...\x02\x03",
            "#01112FRecently, I feel like I've finally\x01",
            "understood what that means...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P#NI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(42, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 50000)
    OP_0D()
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#01122F#11PEheheh....\x02\x03",
            "#01121FI have Lloyd and Elie...\x01",
            "Tio, Randy and everyone...\x02\x03",
            "Shizuku, Ryｹ, the others and teacher\x01",
            "Marble too are my friends...\x02\x03",
            "#01108FIt's true that every day is fun, but...\x02\x03",
            "#01106F#30WOccasionally, you see...only every\x01",
            "once in awhile, I feel lonely...\x02\x03",
            "#30W...As if I had been abandoned\x01",
            "in that pitch-black cavern...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00001F#6P──KeA.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(670, 1000, -16940, 1500)
    Sleep(400)

    def lambda_C0B():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0B)
    OP_93(0x153, 0x10E, 0x190)
    WaitChrThread(0x101, 1)
    Fade(250)
    Sound(898, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x153, 3, 0, 4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x153,
        (
            "#01123F#40W#11PSorry...I'm sorry.\x02\x03",
            "I didn't really\x01",
            "want to say this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PFool, don't hold back.\x02\x03",
            "#00008FAlso...you didn't want to say it, right?\x02\x03",
            "#00001FYou didn't want to cause us, who are\x01",
            "feeling down, unnecessary worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01114F#40W#11P............(*nod*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PListen...it's the opposite, KeA.\x02\x03",
            "#00004FWe can get better just because\x01",
            "you're relying on us, KeA.\x02\x03",
            "We'll never lose and \x01",
            "wholeheartedly do our best.\x02\x03",
            "#00002FAnd so, don't hold back.\x02\x03",
            "#00009FI──at least I'll always\x01",
            "be by your side, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01102F#30W#11P......Ah......\x02\x03",
            "#30W#01104F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Fade(250)
    Sound(812, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x153, 3, 0, 6)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x153,
        "#01109F#11PEheheh, thank you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x153, 0x4B0, 0x6, 0x7, 0x8, 0x7, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x153,
        (
            "#01101F#11PHowever, if you say such a thing, you'll\x01",
            "never be able to get a wife, you know?\x02\x03",
            "Having such a kid with you,\x01",
            "your chances will vanish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHey now...\x01",
            "Where did you learn that?\x02\x03",
            "#00011FWait, could it be that you\x01",
            "read about it at the library?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111F#11PHmm, that's also true, but...\x02\x03",
            "#01100FMaybe it was by talking to\x01",
            "many people in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PMaybe you're studying too much...\x02\x03",
            "#00000F──And at any rate, my wedding\x01",
            "is still far away in the future.\x02\x03",
            "Even my big brother was 25 when\x01",
            "he was trying to get married.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105F#11PLloyd's older brother?\x02\x03",
            "#01106F...I see.\x01",
            "The one who passed away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, but it's a story of the past.\x02\x03",
            "#00000FI have 7 years to go until my big brother's age...\x01",
            "I can think about something like marrying before\x01",
            "becoming a proper adult.\x02\x03",
            "#00012FAlso, to begin with, I can't\x01",
            "because I don't have someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Sleep(100)
    OP_A1(0x153, 0x5DC, 0x4, 0x7, 0x6, 0x7, 0x8)
    Sleep(200)

    ChrTalk(
        0x153,
        (
            "#01105F#11P7 years to go means...\x02\x03",
            "How old will KeA be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PWell, you should be 9 now, so...\x02\x03",
            "#00004FAbout 16──\x01",
            "Ha ha, you'll be older than how Tio is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01103F#11PHmm...\x02\x03",
            "#01101FIf KeA reaches that age,\x01",
            "can she marry too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00011F#6P#4SEEH!?\x02\x03",
            "#00006FWell, no matter what you say, but\x01",
            "isn't marrying at 16 too early!?\x02\x03",
            "#00008FWell, I'm sure that if a guardian approves\x01",
            "you should be able to marry after you're 16...\x02\x03",
            "#00007FB-But no!\x01",
            "I'll never approve, ok!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111F#11PHmm, I wasn't meaning\x01",
            "it in that way...\x02\x03",
            "#01104F...Eheheh, but I understand.\x02\x03",
            "#01121FThere's nothing I have to\x01",
            "worry about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, nothing.\x02\x03",
            "#00000F──Come on, it's time we\x01",
            "head to the theme park.\x02\x03",
            "You've been looking forward to it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#11PEheheh...\x02\x03",
            "#01110FYou know, I was asked by\x01",
            "Shizuku to tell her what kind\x01",
            "of place the theme park is.\x02\x03",
            "Also, when her eyes are healed,\x01",
            "we'll come together to play!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00002FAlright, in that case, we have to\x01",
            "have a lot of fun all the more, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x153, 0x5DC, 0x6, 0x9, 0xA, 0xB, 0xA, 0x9, 0x8)
    Sleep(100)

    ChrTalk(
        0x153,
        "#01109F#11PYes!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x2)
    OP_49()
    OP_D7(0x1E)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    BeginChrThread(0xF, 1, 0, 8)
    SetChrPos(0x0, 0, 0, -12000, 180)
    SetScenarioFlags(0x145, 2)
    OP_29(0xA5, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_2_4C6 end

    def Function_3_17A3(): pass

    label("Function_3_17A3")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x10, 0x11, 0x12)
    Return()

    # Function_3_17A3 end

    def Function_4_17B6(): pass

    label("Function_4_17B6")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_4_17B6 end

    def Function_5_17C9(): pass

    label("Function_5_17C9")

    OP_A1(0xFE, 0x3E8, 0x3, 0x13, 0x14, 0x15)
    Return()

    # Function_5_17C9 end

    def Function_6_17D3(): pass

    label("Function_6_17D3")

    SetChrPos(0xFE, 750, 0, -17000, 270)
    OP_A1(0xFE, 0x3E8, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_6_17D3 end

    def Function_7_17EE(): pass

    label("Function_7_17EE")

    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Return()

    # Function_7_17EE end

    def Function_8_180F(): pass

    label("Function_8_180F")

    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x50)
    Return()

    # Function_8_180F end

    def Function_9_1830(): pass

    label("Function_9_1830")

    EventBegin(0x0)
    FadeToDark(300, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch00351.itc", 0x23)
    LoadChrToIndex("chr/ch02950.itc", 0x24)
    LoadChrToIndex("chr/ch02951.itc", 0x25)
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)
    LoadChrToIndex("chr/ch41950.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x2B)
    LoadChrToIndex("chr/ch41952.itc", 0x2C)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("monster/ch86150.itc", 0x2F)
    LoadChrToIndex("monster/ch86151.itc", 0x30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 5100, 0)
    OP_90(0x103, 500, 0, 3300, 0)
    OP_90(0x104, -700, 0, 5200, 0)
    OP_90(0x105, -500, 0, 3500, 0)
    OP_90(0x106, 1500, 0, 4350, 0)
    OP_90(0x109, -1500, 0, 4050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x28)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 10)
    BeginChrThread(0xE, 0, 0, 10)
    SetChrPos(0x8, 0, 0, 20000, 180)
    SetChrPos(0x9, -2000, 0, 19500, 180)
    SetChrPos(0xC, 2000, 0, 19500, 180)
    SetChrPos(0xD, -1300, 0, 23000, 180)
    SetChrPos(0xE, 1300, 0, 23000, 180)
    OP_68(0, 1000, 17000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(18500, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 1, 0, 15)

    def lambda_1A86():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A86)
    Sleep(50)

    def lambda_1A9E():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A9E)
    Sleep(50)

    def lambda_1AB6():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1AB6)
    Sleep(50)

    def lambda_1ACE():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1ACE)
    Sleep(50)

    def lambda_1AE6():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1AE6)
    Sleep(50)

    def lambda_1AFE():
        OP_9B(0x0, 0x106, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1AFE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 16000, 0)
    OP_68(350, 1000, 17640, 1500)
    MoveCamera(41, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PTch, to think they assaulted\x01",
            "us by sheer strength...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00312F#12PSachs.\x01",
            "The fact that you're here seems\x01",
            "to mean you're the last ones, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...Yeah, Captain Randolph.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, we too, as members\x01",
            "of the "Red Constellation",\x01",
            "can't let you pass through here!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#5P#4SDo your utmost best, guys!\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5PIf we can't defend this place to the end,\x01",
            "the vice leader and missus will waste us!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    ChrTalk(
        0x9,
        "#5PJaー!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    ChrTalk(
        0xC,
        "#5PWe'll crush you with all our might!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PBring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#12PI will make you pay\x01",
            "for the Arc-en-ciel...!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11000, 500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 13)
    BeginChrThread(0x9, 3, 0, 12)
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0xD, 3, 0, 14)
    BeginChrThread(0xE, 3, 0, 14)

    def lambda_1E18():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E18)

    def lambda_1E2D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E2D)

    def lambda_1E42():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E42)

    def lambda_1E57():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E57)

    def lambda_1E6C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E6C)

    def lambda_1E81():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E81)
    Sleep(200)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    Battle("BattleInfo_360", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 16)
    Return()

    # Function_9_1830 end

    def Function_10_1EE6(): pass

    label("Function_10_1EE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F02")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_10_1EE6")

    label("loc_1F02")

    Return()

    # Function_10_1EE6 end

    def Function_11_1F03(): pass

    label("Function_11_1F03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F1F")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_11_1F03")

    label("loc_1F1F")

    Return()

    # Function_11_1F03 end

    def Function_12_1F20(): pass

    label("Function_12_1F20")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_12_1F20 end

    def Function_13_1F38(): pass

    label("Function_13_1F38")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_13_1F38 end

    def Function_14_1F50(): pass

    label("Function_14_1F50")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_14_1F50 end

    def Function_15_1F79(): pass

    label("Function_15_1F79")

    Sleep(2200)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 20, 0)
    Return()

    # Function_15_1F79 end

    def Function_16_1F8F(): pass

    label("Function_16_1F8F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch42053.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00356.itc", 0x26)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 16100, 0)
    OP_90(0x103, 500, 0, 14300, 0)
    OP_90(0x104, -700, 0, 16200, 0)
    OP_90(0x105, -500, 0, 14500, 0)
    OP_90(0x106, 1500, 0, 15350, 0)
    OP_90(0x109, -1500, 0, 15050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x9, -2500, 0, 21000, 0)
    SetChrPos(0xC, 2000, 0, 22500, 45)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 200, 0, 19100, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    VolumeBGM(0x32, 0x7D0)
    OP_68(-360, 1000, 18310, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14250, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_2150():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2150)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#40W...Tch...\x01",
            "Captain Randolph...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#40WYou're...far stronger than\x01",
            "when you were in the corps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, my workplace trains\x01",
            "me in many ways.\x02\x03",
            "#00300FIt's the experience that's\x01",
            "different, the experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#40WHah...\x01",
            "Greater experience than us who're\x01",
            "addicted to battlefields every day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#40WWhat kind of workplace is that...\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_22E4():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22E4)
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    OP_68(-230, 1000, 18600, 500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -500, 0, 18250, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#60W#5P#2S...Watch...out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#60W#5P#2SInside there..\x01",
            "...Those guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#60W#5P#2S............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#12P...Did he faint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PYeah...\x01",
            "He's totally out.\x02\x03",
            "#00311F"Those guys"...\x01",
            "What the heck did he mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PA trap probably.\x01",
            "A different "enemy", perhaps...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PHm, I don't know but\x01",
            "we should be on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12P...If we need treatment we\x01",
            "should have it now that we can.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x7D0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x0, 0, 0, 11900, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_1F8F end

    def Function_17_25AC(): pass

    label("Function_17_25AC")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 1100, 0, 15000, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, -2500, 0, 18000, 0)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 2000, 0, 19500, 45)
    Return()

    # Function_17_25AC end

    def Function_18_2646(): pass

    label("Function_18_2646")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe guest house is this way.\x02\x03",
            "We don't have any particular business\x01",
            "over there until tonight's dinner party.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    OP_68(0, 700, -1700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37000, 0)
    EventEnd(0x4)
    Return()

    # Function_18_2646 end

    SaveToFile()

Try(main)
