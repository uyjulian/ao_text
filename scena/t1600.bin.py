from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1600",                  # 0
        "Baggio",                 # 1
        "Shizuku",                # 2
        "Professor Seiland",      # 3
        "Janitor Dyson",          # 4
        "Nurse Xilun",            # 5
        "Nurse Meihua",           # 6
        "Arios",                  # 7
        "Sergei",                 # 8
        "St. Ursula Byroad",      # 9
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch05400.itc",                   # 01
        "chr/ch44800.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch29900.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch05300.itc",                   # 06
    ))

    DeclNpc(4294945317, 6000,    18520,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294963707, 7000,    11229,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3430,    7000,    4294958137, 180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294940737, 6000,    14199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294940737, 6000,    14199,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])

    DeclActor(17500,   7000,    4294964296, 2000,    18000,   8000,    4294964296, 0x007C, 0,  22, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_380",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_5DE",          # 03, 3
        "Function_4_6BD",          # 04, 4
        "Function_5_9D6",          # 05, 5
        "Function_6_E4A",          # 06, 6
        "Function_7_12D0",         # 07, 7
        "Function_8_19B1",         # 08, 8
        "Function_9_1BAE",         # 09, 9
        "Function_10_1CFA",        # 0A, 10
        "Function_11_2033",        # 0B, 11
        "Function_12_274A",        # 0C, 12
        "Function_13_326F",        # 0D, 13
        "Function_14_3295",        # 0E, 14
        "Function_15_32BB",        # 0F, 15
        "Function_16_32E1",        # 10, 16
        "Function_17_3307",        # 11, 17
        "Function_18_332D",        # 12, 18
        "Function_19_3353",        # 13, 19
        "Function_20_3379",        # 14, 20
        "Function_21_339F",        # 15, 21
        "Function_22_33C5",        # 16, 22
        "Function_23_354F",        # 17, 23
        "Function_24_3A0C",        # 18, 24
        "Function_25_3A57",        # 19, 25
        "Function_26_3AA2",        # 1A, 26
        "Function_27_3AED",        # 1B, 27
        "Function_28_3B38",        # 1C, 28
        "Function_29_3B83",        # 1D, 29
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_308"),
        (1, "loc_314"),
        (2, "loc_320"),
        (3, "loc_32C"),
        (4, "loc_338"),
        (5, "loc_344"),
        (6, "loc_350"),
        (SWITCH_DEFAULT, "loc_35C"),
    )


    label("loc_308")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_314")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_320")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_32C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_338")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_344")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_350")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_37F")

    Return()

    # Function_0_2C8 end

    def Function_1_380(): pass

    label("Function_1_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8450, 7000, -13870, 135)
    Jump("loc_4EE")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 13730, 7000, -3100, 90)
    Jump("loc_4EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -26060, 6000, 14200, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -27060, 6000, 14200, 0)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    SetChrFlags(0x9, 0x10)

    label("loc_441")

    Jump("loc_4EE")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4EE")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_4EE")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -22110, 6000, 16760, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20450, 6000, 17030, 315)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E0")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xB, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_502")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_511")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_511")

    Return()

    # Function_1_380 end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_524")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5BF")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_5BF")

    label("loc_5BF")

    ClearMapObjFlags(0x5, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5DD")

    Return()

    # Function_2_512 end

    def Function_3_5DE(): pass

    label("Function_3_5DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    Call(0, 8)
    Jump("loc_6B9")

    label("loc_5FC")


    ChrTalk(
        0x8,
        (
            "A nurse, it could be nice.\x01",
            "It's not that there aren't\x01",
            "any male nurses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I had nothing to lose so I tried\x01",
            "asking sis for advice, but somehow\x01",
            "I feel that a path has opened for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9")

    TalkEnd(0xFE)
    Return()

    # Function_3_5DE end

    def Function_4_6BD(): pass

    label("Function_4_6BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2")
    Call(0, 11)
    Jump("loc_9D2")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966")
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11200FBy the way, everyone.\x02\x03",
            "KeA came to the hospital\x01",
            "three days ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah...now that you\x01",
            "mention it, she did\x01",
            "come to visit you.\x02\x03",
            "#00000FUhhm, did something\x01",
            "happen with KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11208FNo... I felt like she\x01",
            "was somehow a\x01",
            "little strange.\x02\x03",
            "#11203FLike she was brooding over something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FKeA was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FShe didn't show\x01",
            "such a behaviour\x01",
            "in front of us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...Maybe KeA too\x01",
            "is uneasy about\x01",
            "Crossbell situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FRight...\x01",
            "Maybe she was hiding her feelings\x01",
            "to not make us worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, in any case it seems it would\x01",
            "be better to keep this in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 6)
    Jump("loc_9D2")

    label("loc_966")


    ChrTalk(
        0x9,
        (
            "#11200FI think things are hard for you too,\x01",
            "but please, do your best.\x02\x03",
            "I'll cheer for you from here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D2")

    TalkEnd(0xFE)
    Return()

    # Function_4_6BD end

    def Function_5_9D6(): pass

    label("Function_5_9D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E7")
    Jump("loc_E46")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B52")

    ChrTalk(
        0xA,
        (
            "Physicians and medical interns all together\x01",
            "are progressing in dealing with the variety\x01",
            "of medicines lack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They probably won't be perfect,\x01",
            "but doing one's very best at\x01",
            "every time is a doctor's duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On my pride and dignity as a pharmacology\x01",
            "and neurology professor, I swear upon the\x01",
            "Goddess that I'll absolutely make it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C41")

    label("loc_B52")


    ChrTalk(
        0xA,
        (
            "Physicians and medical interns all together\x01",
            "are progressing in dealing with the variety\x01",
            "of medicines lack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On my pride and dignity as a pharmacology\x01",
            "and neurology professor, I swear upon the\x01",
            "Goddess that I'll absolutely make it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C41")

    Jump("loc_E46")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_C54")
    Jump("loc_E46")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C62")
    Jump("loc_E46")

    label("loc_C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(
        0xA,
        (
            "Shizuku...\x01",
            "The possibilities she can recover her \x01",
            "eyesight are as low as they can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...However, as long as the patient \x01",
            "doesn't give up, I too won't give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the name of Seiland...\x01",
            "One day, for sure, I'll cure her with my own hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E46")

    label("loc_D7A")


    ChrTalk(
        0xA,
        (
            "If Shizuku's eyesight recovery surgery\x01",
            "succeeds, it'll become hope too for the\x01",
            "patients who have the same handicap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the name of Seiland...\x01",
            "One day, for sure, I'll cure her with my own hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E46")

    TalkEnd(0xFE)
    Return()

    # Function_5_9D6 end

    def Function_6_E4A(): pass

    label("Function_6_E4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ECE")

    ChrTalk(
        0xB,
        (
            "That giant tree is amazing...\x01",
            "You can see it from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I wonder what's going\x01",
            "to happen to Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CC")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_EDC")
    Jump("loc_12CC")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1030")

    ChrTalk(
        0xB,
        (
            "In nowadays lectures at the research laboratory,\x01",
            "it seems that they can't almost do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's the effect of collecting samples \x01",
            "in the highways not being able to\x01",
            "stock up from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate, it seems that the medical interns study\x01",
            "environment too will gradually end up worsening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1102")

    label("loc_1030")


    ChrTalk(
        0xB,
        (
            "In nowadays lectures at the research laboratory,\x01",
            "it seems that they can't almost do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate, it seems that the medical interns study\x01",
            "environment too will gradually end up worsening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1102")

    Jump("loc_12CC")

    label("loc_1107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1115")
    Jump("loc_12CC")

    label("loc_1115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122B")

    ChrTalk(
        0xB,
        (
            "When I work around here,\x01",
            "I can pick up gossips from the\x01",
            "medical interns on lunch break...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Lately there're many gossips\x01",
            "all regarding Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have nothing to do with her, but...\x01",
            "I actually wonder what kind of person she is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12CC")

    label("loc_122B")


    ChrTalk(
        0xB,
        (
            "Recently, Professor Seiland is\x01",
            "the talk among the medical interns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have nothing to do with her, but...\x01",
            "I actually wonder what kind of person she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CC")

    TalkEnd(0xFE)
    Return()

    # Function_6_E4A end

    def Function_7_12D0(): pass

    label("Function_7_12D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12E1")
    Jump("loc_19AD")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_12EF")
    Jump("loc_19AD")

    label("loc_12EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130A")
    Call(0, 9)
    Jump("loc_1330")

    label("loc_130A")


    ChrTalk(
        0xC,
        (
            "Ehehe, Meifa\x01",
            "is really reliable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1330")

    Jump("loc_19AD")

    label("loc_1335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1499")

    ChrTalk(
        0xC,
        (
            "About today's sheets drying method,\x01",
            "I came up with it yesterday. \x01",
            "It's the "pile-drying" killing move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Goodness, by pile-drying\x01",
            "two sheets, the number\x01",
            "you can dry doubles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this, I can perfectly\x01",
            "cover today's share for Meihua,\x01",
            "who has a day off, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...O-Oh, but...\x01",
            "What if they don't get dry at all...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_154B")

    label("loc_1499")


    ChrTalk(
        0xC,
        (
            "Uuh, I discovered that the\x01",
            ""pile-drying" killing move \x01",
            "doesn't dry the sheets at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since Meihua has a day off,\x01",
            "I was thinking to do my\x01",
            "best for two people, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154B")

    Jump("loc_19AD")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_155E")
    Jump("loc_19AD")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_156C")
    Jump("loc_19AD")

    label("loc_156C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_157A")
    Jump("loc_19AD")

    label("loc_157A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")

    ChrTalk(
        0xC,
        (
            "The other day, when Mihail was\x01",
            "discharged, I gave my handkerchief\x01",
            "to Meihua who was crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, somehow she suddenly stopped\x01",
            "crying and staaared at me with her eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uuhn, what was that for?\x01",
            "After she didn't even gave the handkerchief back...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1752")

    label("loc_1699")


    ChrTalk(
        0xC,
        (
            "Meihua, I wonder what happened\x01",
            "to my handkerchief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I found it in the dormitory room before.\x01",
            "I liked it because it was pleasant to the \x01",
            "touch and had a nice design, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1752")

    Jump("loc_19AD")

    label("loc_1757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_184E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1772")
    Call(0, 8)
    Jump("loc_1849")

    label("loc_1772")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Ah, I see!\x01",
            "Why don't you wear a nurse uniform to try?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "Come on Meihua, take off\x01",
            "those and lend them to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I-I won't!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(U-Uhhm, she's the\x01",
            "same as always...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_1849")

    Jump("loc_19AD")

    label("loc_184E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(
        0xC,
        (
            "Uh uh, what nice weather today.\x01",
            "The laundry will get dry well♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...*haah*, somehow this\x01",
            "warm weather...\x01",
            "Makes me sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe I'll get one sheet\x01",
            "and sleep in it once again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_199F")

    label("loc_1926")


    ChrTalk(
        0xC,
        (
            "Basking in the sun\x01",
            "here is pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I have the feeling that today\x01",
            "Meihua won't be coming...\x01",
            "Yes, I'll sleep☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199F")

    Jump("loc_19AD")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19AD")

    label("loc_19AD")

    TalkEnd(0xFE)
    Return()

    # Function_7_12D0 end

    def Function_8_19B1(): pass

    label("Function_8_19B1")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "I failed the medical intern examination...\x01",
            "I'm feeling more and more ashamed at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Say, sis Xilun.\x01",
            "What should I do from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(Baggio...\x01",
            "To be asking Xilun for advice, he\x01",
            "really must be at his wits end.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, why don't you try becoming\x01",
            "a nurse like your sis here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "I-Isn't that a proper opinion\x01",
            "coming from you, Xilun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see, male nurse...\x01",
            "I didn't think about that!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_8_19B1 end

    def Function_9_1BAE(): pass

    label("Function_9_1BAE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Xilun, you...\x01",
            "If you pile the sheets one\x01",
            "on the other, they won't dry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Honestly, for how\x01",
            "many years have\x01",
            "you been doing this job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Eeehm, since I joined with you, \x01",
            "Meihua, it's been one, two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Enough, you don't have to honestly\x01",
            "reply to pointless things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Her, dry these again!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_1BAE end

    def Function_10_1CFA(): pass

    label("Function_10_1CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D0B")
    Jump("loc_202F")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D19")
    Jump("loc_202F")

    label("loc_1D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D34")
    Call(0, 9)
    Jump("loc_1DB5")

    label("loc_1D34")


    ChrTalk(
        0xD,
        (
            "Honestly, that Xilun...\x01",
            "Can't she even properly\x01",
            "dry the sheets alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Really, if I don't watch\x01",
            "her she does no good...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB5")

    Jump("loc_202F")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1DC8")
    Jump("loc_202F")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DD6")
    Jump("loc_202F")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DE4")
    Jump("loc_202F")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE2")

    ChrTalk(
        0xD,
        (
            "That Xilun, it seems that she was\x01",
            "being scolded by the Head Nurse today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Usually she does nothing but mistakes,\x01",
            "so it's important that she's scolded\x01",
            "now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Well, at a proper time\x01",
            "I'll go stick for her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F70")

    label("loc_1EE2")


    ChrTalk(
        0xD,
        (
            "That Xilun, it seems that she was\x01",
            "being scolded by the Head Nurse today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I'll go stick for her later.\x01",
            "...I too am quite soft.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F70")

    Jump("loc_202F")

    label("loc_1F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F83")
    Jump("loc_202F")

    label("loc_1F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9E")
    Call(0, 8)
    Jump("loc_2013")

    label("loc_1F9E")


    ChrTalk(
        0xD,
        (
            "Xilun... Soooooometimes\x01",
            "she says something proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I guess that tomorrow\x01",
            "is going to snow or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2013")

    Jump("loc_202F")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2026")
    Jump("loc_202F")

    label("loc_2026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_202F")

    label("loc_202F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CFA end

    def Function_11_2033(): pass

    label("Function_11_2033")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3510, 8300, 11470, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x104, -1400, 7000, 11230, 270)
    SetChrPos(0x102, -1990, 7000, 12030, 225)
    SetChrPos(0x101, -2790, 7000, 12830, 225)
    SetChrPos(0x103, -3590, 7000, 13630, 180)
    SetChrPos(0x109, -2590, 7000, 14030, 180)
    SetChrPos(0x105, -3400, 7000, 14840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00000FSo you were here,\x01",
            "Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11205FAh...are you the people\x01",
            "from the Support Section?\x02\x03",
            "#11200FDid you come to visit\x01",
            "someone, today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FYes, Fran is hospitalised here.\x02\x03",
            "#10100FThen we visited a police\x01",
            "inspector and Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FI see...\x01",
            "I had heard about Miss Fran\x01",
            "from Miss Cecil and...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#12P#11203FAs I suspected, the city raid incident \x01",
            "seems to have been quite grave...\x02\x03",
            "#11208FIt seems that Miss Cecil, the others and\x01",
            "the doctors too have been so busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah...\x01",
            "It was indeed so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FBy the way, Shizuku,\x01",
            "did Mr. Arios come\x01",
            "to visit you recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FNo, not a single time after\x01",
            "the raid incident happened...\x02\x03",
            "#11200FHe called me, but it seems\x01",
            "really busy with many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00200FIs that so...?\x01",
            "How sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200F...No, I'm fine.\x02\x03",
            "#11203FA lot of people turned into victims\x01",
            "and many were injured too...\x02\x03",
            "Among them, I can't be the only\x01",
            "one who gets all the attentions.\x02\x03",
            "#11208F...I too want to do something,\x01",
            "like encouraging Miss Fran\x01",
            "and the other patients, but...\x02\x03",
            "#11203F...It's just that I, who can't see,\x01",
            "can only do that...\x01",
            "That's really mortifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00300F...No, I think it's plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI think that you, in your condition,\x01",
            "are giving courage to everyone to\x01",
            "fight in the face of adversity.\x02\x03",
            "#00004F...We must do our best too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10302FHu hu...right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200FEhm...\x01",
            "I think things are hard for you too,\x01",
            "but please, do your best.\x02\x03",
            "#11203FI'll cheer for you from here...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0x5A, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x18E, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2790, 7000, 12830, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_2033 end

    def Function_12_274A(): pass

    label("Function_12_274A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02500.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1900, 7000, 14600, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1300, 7000, 15610, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3100, 7000, 14600, 180)
    OP_68(-3510, 8400, 11470, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16160, 0)
    SetChrPos(0x104, -2100, 7000, 16800, 180)
    SetChrPos(0x102, -1900, 7000, 17810, 180)
    SetChrPos(0x101, -2310, 7000, 18610, 180)
    SetChrPos(0x103, -1700, 7000, 19600, 180)
    SetChrPos(0x109, -1910, 7000, 20600, 180)
    SetChrPos(0x105, -2120, 7000, 21590, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    BeginChrThread(0x105, 3, 0, 21)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0xE,
        "#01400FShizuku, watch your step.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FYes, thank you father.\x02\x03",
            "#11204FUh uh, what a nice breeze...\x01",
            "And the sunlight is bright,\x01",
            "warm and pleasant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, I'm glad for you.\x02\x03",
            "#00003F...By the way, just before\x01",
            "you said you became able\x01",
            "to perceive light around you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11200FYes, although I say that, I don't\x01",
            "understand it in a very detailed way.\x02\x03",
            "#11203FIt's like there's a pure\x01",
            "white haze all around and\x01",
            "I can feel the brightness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAlthough you feel the light,\x01",
            "it seems it's really not to\x01",
            "a degree that you can see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01403F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x9,
        (
            "#6P#11202F...E-Ehhm.\x01",
            "Everyone, please don't\x01",
            "feel so depressed.\x02\x03",
            "#11209FI'm very glad with the results\x01",
            "of this surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10305FEeh...is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203F...It's true that at first\x01",
            "I was feeling down since\x01",
            "it wasn't a perfect recovery.\x02\x03",
            "#11208FI thought I'll never be\x01",
            "able to recover...\x01",
            "I almost gave up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FBut thinking about it, it's the\x01",
            "first time that the "treatment\x01",
            "has progressed" this much.\x02\x03",
            "#11204FThat's why my eyes, although\x01",
            "slowly, will get better for sure...\x01",
            "I could think like that again.\x02\x03",
            "#11200FFor father who supports me\x01",
            "and everyone in the hospital\x01",
            "and KeA too, I won't...\x02\x03",
            "#11209FI won't give up from now on\x01",
            "and continue the treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10102FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F...You sure are strong.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#6P#11205FE-Ehm...I'm sorry,\x01",
            "it sounded conceited as I thought.\x02\x03",
            "#11203FI'm always causing troubles\x01",
            "for father who pays the\x01",
            "doctors' bills for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01403F...If you say you won't give up,\x01",
            "then I'll support you like I did until now.\x02\x03",
            "#01402FDon't think about unnecessary things\x01",
            "and focus on getting back your eyesight.\x02\x03",
            "#01404FSaya too would want that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203FFather...you're right.\x02\x03",
            "#11202FEven for mother who is\x01",
            "with the venerable Goddess...\x01",
            "I'll do my best from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004FEh eh, Arios.\x01",
            "She's really your kid, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, true.\x01",
            "Same backbone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01404F...I'm sure she took\x01",
            "that from her mother.\x02\x03",
            "#01400F──The leave out time is almost over.\x01",
            "Shizuku, we're going back to your room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#11205FAh...yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThen, let's go back.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others enjoyed\x01",
            "chatting for a short time in Shizuku's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("t1550", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_274A end

    def Function_13_326F(): pass

    label("Function_13_326F")


    def lambda_3274():
        OP_95(0xFE, -3590, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3274)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_13_326F end

    def Function_14_3295(): pass

    label("Function_14_3295")


    def lambda_329A():
        OP_95(0xFE, -2590, 7000, 11020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_329A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_14_3295 end

    def Function_15_32BB(): pass

    label("Function_15_32BB")


    def lambda_32C0():
        OP_95(0xFE, -1500, 7000, 10030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_32BB end

    def Function_16_32E1(): pass

    label("Function_16_32E1")


    def lambda_32E6():
        OP_95(0xFE, -1400, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32E6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_32E1 end

    def Function_17_3307(): pass

    label("Function_17_3307")


    def lambda_330C():
        OP_95(0xFE, -1990, 7000, 12030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_330C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_17_3307 end

    def Function_18_332D(): pass

    label("Function_18_332D")


    def lambda_3332():
        OP_95(0xFE, -2790, 7000, 12830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3332)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_18_332D end

    def Function_19_3353(): pass

    label("Function_19_3353")


    def lambda_3358():
        OP_95(0xFE, -3590, 7000, 13630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3358)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_3353 end

    def Function_20_3379(): pass

    label("Function_20_3379")


    def lambda_337E():
        OP_95(0xFE, -2590, 7000, 14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_337E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_3379 end

    def Function_21_339F(): pass

    label("Function_21_339F")


    def lambda_33A4():
        OP_95(0xFE, -3400, 7000, 14840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33A4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_339F end

    def Function_22_33C5(): pass

    label("Function_22_33C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D5")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[4F Pharmacology - Neurology Research Lab]\x01",      # 0
            "[Quit]\x01",                                          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3480"),
        (1, "loc_34C9"),
        (SWITCH_DEFAULT, "loc_34D0"),
    )


    label("loc_3480")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BB")
    SetScenarioFlags(0x22, 0)
    NewScene("t1650", 100, 0, 0)
    IdleLoop()
    Jump("loc_34C4")

    label("loc_34BB")

    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_34C4")

    Jump("loc_34D0")

    label("loc_34C9")

    EventEnd(0x3)
    Jump("loc_34D0")

    label("loc_34D0")

    Jump("loc_354E")

    label("loc_34D5")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FThe research laboratory is this way, eh?\x01",
            "We don't have any particular\x01",
            "business so let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)

    label("loc_354E")

    Return()

    # Function_22_33C5 end

    def Function_23_354F(): pass

    label("Function_23_354F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 9400, -3400, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 18740, 7000, -3160, 270)
    SetChrPos(0x102, 18740, 7000, -3160, 270)
    SetChrPos(0x109, 18740, 7000, -3160, 270)
    SetChrPos(0x105, 18740, 7000, -3160, 270)
    SetChrPos(0x104, 18740, 7000, -3160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14750, 8000, -3400, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x5, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x104,
        (
            "#00301F...I feel like I got many things but at the\x01",
            "same time the mysteries have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FSomehow it's irritating...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes, now that Doctor Joachim has passed away,\x01",
            "the clues have become too few...\x02\x03",
            "#00103FWe could figure out something if at least\x01",
            "the database analysis proceeded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FWell, about that, I guess it\x01",
            "could be one task for the future?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FYeah...\x01",
            "Let's keep that in mind too.\x02\x03",
            "#00003F──At any rate, this request\x01",
            "is now completed.\x02\x03",
            "#00000FIt could be good to drop by sister\x01",
            "Cecil on our way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYeah, let's do that!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [New Professor's Request]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x70, 0x1, 0x6)
    OP_29(0x70, 0x1, 0x7)
    OP_29(0x70, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15500, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_23_354F end

    def Function_24_3A0C(): pass

    label("Function_24_3A0C")


    def lambda_3A11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A11)

    def lambda_3A22():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A22)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13000, 7000, -3000, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_24_3A0C end

    def Function_25_3A57(): pass

    label("Function_25_3A57")


    def lambda_3A5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A5C)

    def lambda_3A6D():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A6D)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 14160, 7000, -2240, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_25_3A57 end

    def Function_26_3AA2(): pass

    label("Function_26_3AA2")


    def lambda_3AA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3AA7)

    def lambda_3AB8():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AB8)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 15890, 7000, -3980, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_26_3AA2 end

    def Function_27_3AED(): pass

    label("Function_27_3AED")


    def lambda_3AF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3AF2)

    def lambda_3B03():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B03)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 14180, 7000, -4310, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_27_3AED end

    def Function_28_3B38(): pass

    label("Function_28_3B38")


    def lambda_3B3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3B3D)

    def lambda_3B4E():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B4E)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 15840, 7000, -2650, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_28_3B38 end

    def Function_29_3B83(): pass

    label("Function_29_3B83")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, we can't enter the hospital\x01",
            "ward without going to the reception.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -16059, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_29_3B83 end

    SaveToFile()

Try(main)
