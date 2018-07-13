from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3020_1.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [312, 2241, 3092, 7809, 8485, 9696, 10405, 14106, 15372, 0, 15964, 0, 17001, 17807, 18678, 22114, 0, 23075, 0, 206, 92, 0, 0],
    )

    BuildStringList((
        "e3020_1",                # 0
    ))

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_8C1",          # 01, 1
        "Function_2_C14",          # 02, 2
        "Function_3_1E81",         # 03, 3
        "Function_4_2125",         # 04, 4
        "Function_5_25E0",         # 05, 5
        "Function_6_28A5",         # 06, 6
        "Function_7_371A",         # 07, 7
        "Function_8_3C0C",         # 08, 8
        "Function_9_3E5C",         # 09, 9
        "Function_10_4269",        # 0A, 10
        "Function_11_458F",        # 0B, 11
        "Function_12_48F6",        # 0C, 12
        "Function_13_5662",        # 0D, 13
        "Function_14_5A23",        # 0E, 14
        "Function_15_5CCE",        # 0F, 15
        "Function_16_7883",        # 10, 16
        "Function_17_7A7E",        # 11, 17
        "Function_18_7F50",        # 12, 18
        "Function_19_83D3",        # 13, 19
        "Function_20_92FC",        # 14, 20
        "Function_21_96F1",        # 15, 21
        "Function_22_9A60",        # 16, 22
        "Function_23_AAD3",        # 17, 23
        "Function_24_AE37",        # 18, 24
        "Function_25_B644",        # 19, 25
        "Function_26_B995",        # 1A, 26
        "Function_27_D90C",        # 1B, 27
        "Function_28_DC20",        # 1C, 28
        "Function_29_DD3B",        # 1D, 29
        "Function_30_E003",        # 1E, 30
        "Function_31_E3D0",        # 1F, 31
        "Function_32_FE77",        # 20, 32
        "Function_33_10387",       # 21, 33
        "Function_34_10667",       # 22, 34
        "Function_35_1106C",       # 23, 35
        "Function_36_112DB",       # 24, 36
        "Function_37_11505",       # 25, 37
        "Function_38_11A9C",       # 26, 38
        "Function_39_1224E",       # 27, 39
        "Function_40_12780",       # 28, 40
        "Function_41_12A49",       # 29, 41
        "Function_42_12E5B",       # 2A, 42
        "Function_43_12E5F",       # 2B, 43
        "Function_44_14269",       # 2C, 44
        "Function_45_145EC",       # 2D, 45
        "Function_46_145F0",       # 2E, 46
        "Function_47_15755",       # 2F, 47
        "Function_48_1595D",       # 30, 48
        "Function_49_15AAB",       # 31, 49
        "Function_50_160EA",       # 32, 50
        "Function_51_16225",       # 33, 51
        "Function_52_167F2",       # 34, 52
        "Function_53_17214",       # 35, 53
        "Function_54_17C5D",       # 36, 54
        "Function_55_17FAA",       # 37, 55
        "Function_56_1817E",       # 38, 56
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_38D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    Call(1, 1)
    Jump("loc_388")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8")

    ChrTalk(
        0x11,
        (
            "#00101FBell is most likely participating\x01",
            "in this plan for herself.\x02\x03",
            "#00108FA lot of things about Bell amaze me,\x01",
            "her personality included. Maybe\x01",
            "that's what fascinates me...\x02\x03",
            "#00103F...But no matter the reason,\x01",
            "a plan that sacrifices\x01",
            "someone can't be forgiven.\x02\x03",
            "#00100FI've been friends with Bell since we were little...\x01",
            "I'll definitely make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_388")

    label("loc_2D8")


    ChrTalk(
        0x11,
        (
            "#00103FNo matter the reason,\x01",
            "a plan that sacrifices\x01",
            "someone can't be forgiven.\x02\x03",
            "#00100FAs Bell's friend since we were little...\x01",
            "I'll definitely make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388")

    Jump("loc_8BD")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_4DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462")

    ChrTalk(
        0x11,
        (
            "#00103FAs a Crois, Bell is\x01",
            "likely deeply involved\x01",
            "with this plan.\x02\x03",
            "#00108FI'm sure she and Lawyer Ian\x01",
            "have the truth we are seeking...\x02\x03",
            "#00101F...Let's go, Lloyd.\x01",
            "To take back KeA!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DA")

    label("loc_462")


    ChrTalk(
        0x11,
        (
            "#00108FI'm sure Bell and Lawyer Ian\x01",
            "have the truth we are seeking...\x02\x03",
            "#00101F...Let's go, Lloyd.\x01",
            "To take back KeA!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA")

    Jump("loc_8BD")

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")

    ChrTalk(
        0x11,
        (
            "#00108FBell... I wonder if she planned\x01",
            "to discard "uncle" from the start.\x02\x03",
            "And, to think Lawyer Ian\x01",
            "was the mastermind...\x02\x03",
            "#00106F...It's no good, it seems I'm\x01",
            "confusing myself. I've got\x01",
            "to put my thoughts in order.\x02\x03",
            "#00100FAnyway, we have no choice but\x01",
            "to go. To that "Tree of Azure"...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6AD")

    label("loc_61F")


    ChrTalk(
        0x11,
        (
            "#00108F...Too much has happened and\x01",
            "I've gotten confused, but...\x02\x03",
            "#00100FAnyway, we have no choice but\x01",
            "to go. To that "Tree of Azure"...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD")

    Jump("loc_8BD")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF")

    ChrTalk(
        0x11,
        (
            "#00103FIt seems that my grandfather's independence\x01",
            "declaration of invalidity is having\x01",
            "significant effects everywhere.\x02\x03",
            "#00108FNow that the State Guard has withdrawn,\x01",
            "unrest might appear in various places...\x02\x03",
            "#00100FIt might be a good idea to\x01",
            "visit various places in between\x01",
            "stopping the "big bells".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8BD")

    label("loc_7FF")


    ChrTalk(
        0x11,
        (
            "#00103FThe independence declaration of invalidity\x01",
            "is having significant effects everywhere.\x02\x03",
            "#00100FIt might be a good idea to\x01",
            "visit various places in between\x01",
            "stopping the "big bells".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD")

    TalkEnd(0xFE)
    Return()

    # Function_0_138 end

    def Function_1_8C1(): pass

    label("Function_1_8C1")


    ChrTalk(
        0x11,
        (
            "#00100FFinally... The path to\x01",
            "the place where KeA is\x01",
            "waiting for us is open.\x02\x03",
            "#00108FAnd Lawyer Ian, the mastermind,\x01",
            "and Bell are there too...\x02\x03",
            "#00103F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FElie......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103FBell is most likely participating\x01",
            "in this plan for herself.\x02\x03",
            "#00108FA lot of things about Bell amaze me,\x01",
            "her personality included. Maybe\x01",
            "that's what fascinates me...\x02\x03",
            "#00101F...But no matter the reason,\x01",
            "a plan that sacrifices\x01",
            "someone can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah, that's right.\x02\x03",
            "#00001FThough we don't know what Miss Mariabell\x01",
            "and Lawyer Ian's plan is, we can't let them\x01",
            "use KeA any more than they already have.\x02\x03",
            "#00003FElie, it might be hard\x01",
            "fighting against her, but...\x01",
            "Please, lend me your aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103F...Yes, I'm prepared for that.\x02\x03",
            "#00101FAs Bell's friend since we were little...\x01",
            "I'll definitely make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 1)
    Return()

    # Function_1_8C1 end

    def Function_2_C14(): pass

    label("Function_2_C14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C38")
    Call(1, 56)
    Jump("loc_E17")

    label("loc_C38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C58")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    label("loc_C58")


    ChrTalk(
        0xB,
        (
            "#00200FMr. Lloyd, \x01",
            "if you like, please\x01",
            "accept this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Tio's Account"\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 1)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#00005FA "Pom!" account...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FPrecisely because of the current situation,\x01",
            "leisure is important, I think.\x02\x03",
            "#00202FI will be your opponent anytime, so\x01",
            "please feel free to challenge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, sure.\x02\x03",
            "#00004F(I think Tio is a formidable\x01",
            "rival... But I've got to\x01",
            "try my best somehow.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E17")
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E17")

    Jump("loc_1E7D")

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")
    Call(1, 5)
    Jump("loc_FBB")

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F36")

    ChrTalk(
        0xB,
        (
            "#00208FLawyer Ian is an opponent not\x01",
            "even Mr. Guy was able to reach...\x01",
            "His determination was really big.\x02\x03",
            "#00203FThen, we will need to have\x01",
            "such a great determination\x01",
            "to surpass even that...\x02\x03",
            "#00202F...Let's do our best, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_FBB")

    label("loc_F36")


    ChrTalk(
        0xB,
        (
            "#00203FWe will need to have such\x01",
            "a great determination to\x01",
            "surpass even Lawyer Ian's...\x02\x03",
            "#00202F...Let's do our best, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBB")

    Jump("loc_1E7D")

    label("loc_FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_11ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(
        0xB,
        (
            "#00200FA strange dimension has formed\x01",
            "within the "Tree of Azure".\x02\x03",
            "#00203FFar exceeding the "fields" created by the \x01",
            "resonance of the big bells in the "Temple" \x01",
            "and "Tower", a world that completely \x01",
            "disregards the laws of physics...\x02\x03",
            "#00201FOur common sense won't be\x01",
            "any good there... Let's be\x01",
            "cautious as we proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_11E8")

    label("loc_111E")


    ChrTalk(
        0xB,
        (
            "#00203FA strange dimension that completely\x01",
            "disregard the laws of physics has\x01",
            "formed within the "Tree of Azure".\x02\x03",
            "#00201FOur common sense won't be\x01",
            "any good there... Let's be\x01",
            "cautious as we proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E8")

    Jump("loc_1E7D")

    label("loc_11ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E0")

    ChrTalk(
        0xB,
        (
            "#00200FIndeed, I sense KeA-like\x01",
            "waves from that "huge tree".\x02\x03",
            "Miss Mariabell said that\x01",
            ""huge tree" is KeA\x01",
            "herself, but...\x02\x03",
            "#00206F...I don't understand. \x01",
            "What is she planning, making\x01",
            "something like that appear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1381")

    label("loc_12E0")


    ChrTalk(
        0xB,
        (
            "#00200FMiss Mariabell said that\x01",
            ""huge tree" is KeA\x01",
            "herself, but...\x02\x03",
            "#00206F...I don't understand. \x01",
            "What is she planning, making\x01",
            "something like that appear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    Jump("loc_1E7D")

    label("loc_1386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(
        0xB,
        (
            "#00200FBecause it seems we don't need a new\x01",
            ""gap" this time, I've handed all my\x01",
            "shipboard duties to Jona.\x02\x03",
            "#00203FOur opponent is that "Society"...\x01",
            "We don't know what kind of\x01",
            "methods they will employ.\x02\x03",
            "#00200FAdjustments have to be constantly\x01",
            "made, to the orbal staff too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1562")

    label("loc_14B7")


    ChrTalk(
        0xB,
        (
            "#00203FOur opponent is that "Society"...\x01",
            "We don't know what kind of\x01",
            "methods they will employ.\x02\x03",
            "#00200FAdjustments have to be constantly\x01",
            "made, to the orbal staff too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1562")

    Jump("loc_1E7D")

    label("loc_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_16EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1582")
    Call(1, 4)
    Jump("loc_16E5")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163E")

    ChrTalk(
        0xB,
        (
            "#00204FIt was only for a short time, but...\x01",
            "I am really glad I was\x01",
            "able to walk with Zeit.\x02\x03",
            "#00202FFrom now on, I have\x01",
            "to work hard to repay\x01",
            "him for his protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_16E5")

    label("loc_163E")


    ChrTalk(
        0xB,
        (
            "#00204FNow then, I have to\x01",
            "help with the hacking\x01",
            "final preparations.\x02\x03",
            "#00211FAlthough I believe in Jona's ability, I can't\x01",
            "deny that sometimes he is not through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E5")

    Jump("loc_1E7D")

    label("loc_16EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_18D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1809")

    ChrTalk(
        0xB,
        (
            "#00200FIf we get back Miss Elie,\x01",
            "the entire Support\x01",
            "Section will be reunited.\x02\x03",
            "#00203FBecause Chairman MacDowell\x01",
            "is confined, security must\x01",
            "be pretty tight too...\x02\x03",
            "#00202FZeit volunteered to take\x01",
            "on a dangerous role, so let's\x01",
            "make it an absolute success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_18CD")

    label("loc_1809")


    ChrTalk(
        0xB,
        (
            "#00203FBecause Miss Elie and Chairman\x01",
            "MacDowell are confined, security\x01",
            "must be pretty tight too...\x02\x03",
            "#00200FZeit volunteered to take\x01",
            "on a dangerous role, so let's\x01",
            "make it an absolute success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CD")

    Jump("loc_1E7D")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")

    ChrTalk(
        0xB,
        (
            "#00200FFrom West Crossbell Highway we can\x01",
            "go to Bellguard Gate, the Police Academy...\x02\x03",
            "#00206F*sigh*, we have found a "gap"\x01",
            "in a difficult location...\x02\x03",
            "#00200F...But right now, all we\x01",
            "can do is go where we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1A7C")

    label("loc_19C5")


    ChrTalk(
        0xB,
        (
            "#00206FFrom West Crossbell Highway we can\x01",
            "go to Bellguard Gate, the Police Academy...\x02\x03",
            "#00200FIt's a difficult location, but...\x01",
            "For now anyway, all we\x01",
            "can do is go where we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    Jump("loc_1E7D")

    label("loc_1A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9C")
    Call(1, 3)
    Jump("loc_1B28")

    label("loc_1A9C")


    ChrTalk(
        0xB,
        (
            "#00208FZeit's subordinate wolves... \x01",
            "I wonder what they are doing now.\x02\x03",
            "#00203FIt would be reassuring if we\x01",
            "could receive their aid...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B28")

    Jump("loc_1E7D")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B48")
    Call(1, 56)
    Jump("loc_1E7D")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEC")
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0xB,
        (
            "#00203FA cooperation between the Foundation\x01",
            "and the Church... I heard the rumors,\x01",
            "but I finally obtained proof.\x02\x03",
            "#00202FAnyway, it looks like I will be able to use this\x01",
            "terminal without feeling uncomfortable.\x02\x03",
            "I was thinking of using them with my Aeon\x01",
            "System to widen the search for "gaps".\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D0F")
    Jump("loc_1D59")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D2F")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D59")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D4F")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D59")

    label("loc_1D4F")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D59")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FMr. Abbas, please continue\x01",
            "showing me how to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100FHm, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1E7D")

    label("loc_1DEC")


    ChrTalk(
        0xB,
        (
            "#00203FUsing my Aeon System, it\x01",
            "seems like I will be able to\x01",
            "widen the search for "gaps".\x02\x03",
            "#00200FLeave this place to\x01",
            "Miss Fran and myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7D")

    TalkEnd(0xFE)
    Return()

    # Function_2_C14 end

    def Function_3_1E81(): pass

    label("Function_3_1E81")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00205FBy the way...\x01",
            "Your subordinates formed a pack\x01",
            "on the mountain path, Zeit.\x02\x03",
            "#00200FAre they "Divine Wolves"\x01",
            "like you, Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CNo, they're just normal wolves.\x02\x03",
            "#01200FHowever, they're my family.\x01",
            "They follow me since the era Ursula\x01",
            "was alive, generation after generation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00203FA Divine Wolf's family... No wonder you\x01",
            "were able to overpower the military\x01",
            "dogs so easily in the Revache incident.\x02\x03",
            "#00208FI hope they are safe too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CRegarding that, I gave them detailed\x01",
            "instructions before leaving,\x01",
            "so there's no need to worry.\x02\x03",
            "#01200FRight now, they're probably watching\x01",
            "over the situation from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_3_1E81 end

    def Function_4_2125(): pass

    label("Function_4_2125")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00203F...Alright, there we go. With\x01",
            "this your treatment is complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01200F#3CRight. I'm in your debt, Tio.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#00005FZeit... Is that a wound\x01",
            "from that battle earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CYes. With those "Red Constellation".\x02\x03",
            "#01200FThe wound itself should heal\x01",
            "quickly... But their skills can't\x01",
            "be compared to the State Guard.\x02\x03",
            "The surprise attack worked well\x01",
            "as a diversion, but the same\x01",
            "technique won't work again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00002FBut you really helped us\x01",
            "out back there. Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHu hu. Thanks are unnecessary.\x02\x03",
            "#01200F...Now then. It seems there is no longer\x01",
            "a need for me to accompany you, now that\x01",
            "you've recovered your comrades.\x02\x03",
            "I will be on reserve, the same as before. \x01",
            "You can call me in time of need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FWith orbal waves from the\x01",
            "orbal staff, the same as\x01",
            "before, right? ...Understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CAlso, from now on, I'll \x01",
            "come running to battle \x01",
            "in my original form.\x02\x03",
            "#01203FIf those are the kind of monsters roaming\x01",
            "around, it seems they'll be easy prey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha. It's reassuring\x01",
            "that you'll be coming\x01",
            "in your original form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00202FAlright then Zeit. Once again, I\x01",
            "look forward to working with you.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1D7, 0)
    Return()

    # Function_4_2125 end

    def Function_5_25E0(): pass

    label("Function_5_25E0")


    ChrTalk(
        0xB,
        (
            "#00203F...Hearing that Lawyer Ian killed Mr. Guy\x01",
            "personally, when he should have been his\x01",
            "close fried... That made me a little uneasy.\x02\x03",
            "#00208FI wonder what is the "Azure-Zero Project"\x01",
            "he went to such lengths for...\x02\x03",
            "#00206FMost of all, I wonder whether\x01",
            "we can reach this opponent\x01",
            "not even Mr. Guy could...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right. That is\x01",
            "indeed concerning.\x02\x03",
            "#00008FLawyer Ian's resolve is likely\x01",
            "even greater than Mr. Arios'.\x02\x03",
            "#00001FBut... That's exactly why\x01",
            "we need to show resolve\x01",
            "even greater than him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00208FA resolve even greater than\x01",
            "Lawyer Ian's... That's right.\x02\x03",
            "#00201FLet's do our best, Mr. Lloyd.\x01",
            "I think that right now is the\x01",
            "time to surpass Mr. Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... Of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 2)
    Return()

    # Function_5_25E0 end

    def Function_6_28A5(): pass

    label("Function_6_28A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_2AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C3")
    Call(1, 11)
    Jump("loc_2AEB")

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2F")

    ChrTalk(
        0xE,
        (
            "#00300FOur final opponents are\x01",
            "the enigmatic milady Mariabell\x01",
            "and Mr. Grimwood, the mastermind.\x02\x03",
            "#00303FBecause they're usin' Keddo,\x01",
            "the "Sept-Terrion of Zero",\x01",
            "they'll definitely be trouble.\x02\x03",
            "#00302FBut of course, we can't take\x01",
            "even one step backwards.\x02\x03",
            "#00309FOur cute and lovely daughter\x01",
            "is waitin' for her papas.\x01",
            "It's time we face them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2AEB")

    label("loc_2A2F")


    ChrTalk(
        0xE,
        (
            "#00302FWe don't know what kind of opponents they're,\x01",
            "but we can't take even one step backwards.\x02\x03",
            "#00309FOur cute and lovely daughter\x01",
            "is waitin' for her papas.\x01",
            "It's time we face them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEB")

    Jump("loc_3716")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_2BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0B")
    Call(1, 10)
    Jump("loc_2BC4")

    label("loc_2B0B")


    ChrTalk(
        0xE,
        (
            "#00303FFrom now on, I'll have to keep\x01",
            "showin' the foothold I've found...\x02\x03",
            "#00302FTo my late father, and uncle,\x01",
            "to whom I'm somehow indebted.\x01",
            "That'll be the greatest duty I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC4")

    Jump("loc_3716")

    label("loc_2BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_2C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE4")
    Call(1, 9)
    Jump("loc_2C6B")

    label("loc_2BE4")


    ChrTalk(
        0xE,
        (
            "#00303FI'll have to settle things\x01",
            "with that real monster of\x01",
            "my uncle.\x02\x03",
            "#00301FI must change my way of\x01",
            "thinkin' while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6B")

    Jump("loc_3716")

    label("loc_2C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_2E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D89")

    ChrTalk(
        0xE,
        (
            "#00301FWe drove off the "Red Constellation"'s\x01",
            "airship, but it looks like that was just \x01",
            "a preliminary test for them.\x02\x03",
            "#00303FUncle and Shirley are\x01",
            "eagerly waiting...\x02\x03",
            "#00301FWe don't know what they\x01",
            "have in store for us. We\x01",
            "can't let down our guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2E11")

    label("loc_2D89")


    ChrTalk(
        0xE,
        (
            "#00303FUncle and Shirley are\x01",
            "eagerly waiting...\x02\x03",
            "#00301FWe don't know what they\x01",
            "have in store for us. We\x01",
            "can't let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E11")

    Jump("loc_3716")

    label("loc_2E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2C")

    ChrTalk(
        0xE,
        (
            "#00300FNo matter what that\x01",
            ""huge tree" is, to us it's\x01",
            "small. ...Right, Lloyd?\x02\x03",
            "#00304FWe'll take Keddo back with us. As long as\x01",
            "we remember that, everything will be ok.\x02\x03",
            "#00300FIf we have time to think about it,\x01",
            "let's start the invasion already.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2F9B")

    label("loc_2F2C")


    ChrTalk(
        0xE,
        (
            "#00304FI've maintained my halberd\x01",
            "and "Berserker" properly.\x02\x03",
            "#00300FLet's go and take\x01",
            "back Keddo already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9B")

    Jump("loc_3716")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_31BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310D")

    ChrTalk(
        0xE,
        (
            "#00303FIn terms of combined battle power,\x01",
            "Red Constellation is likely\x01",
            "stronger than we are, but...\x02\x03",
            "#00301FThose "Society" guys have those\x01",
            "archaisms, not to mention that\x01",
            "ridiculously skilled spear expert.\x02\x03",
            "In terms of raw power, \x01",
            "this won't be an easy fight.\x02\x03",
            "#00303F...Anyway, they're not\x01",
            "to be taken lightly.\x01",
            "Remember that, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_31B5")

    label("loc_310D")


    ChrTalk(
        0xE,
        (
            "#00303FLookin' at it in terms of\x01",
            "raw power, winnin' against\x01",
            "the "Society" won't be easy.\x02\x03",
            "#00301F...Anyway, they're not\x01",
            "to be taken lightly.\x01",
            "Remember that, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B5")

    Jump("loc_3716")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3346")

    ChrTalk(
        0xE,
        (
            "#00300FIf we broadcast the declaration of\x01",
            "invalidity, the State Guard will at\x01",
            "least take a wait-and-see position...\x02\x03",
            "#00303FThe President is personally employin'\x01",
            "the "Red Constellation", so they'll\x01",
            "likely fight us, the same as always.\x02\x03",
            "#00308FNo... They might use methods\x01",
            "even bolder than what they \x01",
            "employed until now.\x02\x03",
            "#00300FAnyway, we have to be on our guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3420")

    label("loc_3346")


    ChrTalk(
        0xE,
        (
            "#00303FEven after the declaration of invalidity,\x01",
            "the "Red Constellation" will likely fight\x01",
            "us as they have until now.\x02\x03",
            "#00301FIt's possible they might use\x01",
            "bolder methods. We have to\x01",
            "be on our guard goin' forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3420")

    Jump("loc_3716")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_350C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3440")
    Call(1, 8)
    Jump("loc_3507")

    label("loc_3440")


    ChrTalk(
        0xE,
        (
            "#00300FIt's unlikely that uncle and Shirley are\x01",
            "with the Michelam security force, but...\x02\x03",
            "#00303FI'm sure there's a leader of\x01",
            "Gareth's level with them. ...We've\x01",
            "got to make sure we're prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3507")

    Jump("loc_3716")

    label("loc_350C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3527")
    Call(1, 7)
    Jump("loc_3716")

    label("loc_3527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3663")

    ChrTalk(
        0xE,
        (
            "#00304FMireille and the others are workin'\x01",
            "with the people of Mainz, so there's\x01",
            "no need to worry about 'em right now.\x02\x03",
            "#00300FWe've got other things to do, so\x01",
            "let's focus on what's in front of us.\x02\x03",
            "#00309FRely as much as you want on me from now on.\x01",
            "Big brother here will go on a nice rampage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3716")

    label("loc_3663")


    ChrTalk(
        0xE,
        (
            "#00303FWe've got other things to do, so\x01",
            "let's focus on what's in front of us.\x02\x03",
            "#00300FRely as much as you want on me from now on.\x01",
            "Big brother here will go on a nice rampage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3716")

    TalkEnd(0xFE)
    Return()

    # Function_6_28A5 end

    def Function_7_371A(): pass

    label("Function_7_371A")


    ChrTalk(
        0xE,
        (
            "#00309FI can't believe there's even a\x01",
            "workshop... Man, the Merkabah\x01",
            "leaves nothing to be desired.\x02\x03",
            "#00300FWith this, it looks like\x01",
            "I can finish my periodic\x01",
            ""Berserker" maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh yeah. Master Guillaume\x01",
            "fixed it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FYeah. But based on his advice,\x01",
            "I'm limitin' my use of it.\x02\x03",
            "#00300FAnd bro Douglas taught me\x01",
            "this halberd. I can't let my\x01",
            "skills with it get rusty, now...\x02\x03",
            "#00300FI'll be two-timin' with this guy here\x01",
            "and the halberd going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, your way of saying it...\x01",
            "That's very like you, Randy.\x02\x03",
            "#00003FBut, Vice Commander Douglas,\x01",
            "huh... I wonder how he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FI'm sure that guy is carryin' out\x01",
            "his Vice Commander duties with\x01",
            "integrity, the same as always.\x02\x03",
            "#00301FBut, includin' the Commander, I really don't\x01",
            "know if they approve of the current situation.\x02\x03",
            "#00303FIf they didn't, they would\x01",
            "have rebelled like Mireille\x01",
            "and the others, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... We need to find\x01",
            "out what the commanders\x01",
            "are thinking somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FWell, there's a lot of things we need to do.\x01",
            "Let's just focus on what's in front of us.\x02\x03",
            "#00300FRely as much as you want on me from now on.\x01",
            "Big brother here will go on a nice rampage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha... Got it. I'll be\x01",
            "counting on you, Randy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 1)
    Return()

    # Function_7_371A end

    def Function_8_3C0C(): pass

    label("Function_8_3C0C")


    ChrTalk(
        0xD,
        (
            "#10703FA "Red Constellation" force\x01",
            "is in position at Michelam.\x02\x03",
            "#10708F...I wonder if "Bloody\x01",
            "Shirley" is with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303F...No. It's not in her\x01",
            "nature to guard a place\x01",
            "where VIPs are confined.\x02\x03",
            "#00300FSomeone else is there,\x01",
            "probably another leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10703F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FDear Rixia... For now,\x01",
            "let's focus on saving'\x01",
            "Milady and the Chairman.\x02\x03",
            "#00300FAs for my uncle and Shirley,\x01",
            "we'll have to confront 'em sooner\x01",
            "or later, even if we don't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10708F...Yes, you're right. \x01",
            "Sorry, Mr. Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00309FHa ha, you don't need to apologize.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_8_3C0C end

    def Function_9_3E5C(): pass

    label("Function_9_3E5C")


    ChrTalk(
        0xE,
        (
            "#00303FFor as long as I can remember, Shirley\x01",
            "has always been a real man-eatin'\x01",
            "tiger who only finds joy in fightin'.\x02\x03",
            "The only thing that can satisfy her is the\x01",
            "battlefield, where it's kill or be killed...\x02\x03",
            "#00302FSuch a gal suffered a defeat aside the realm\x01",
            "of the "be killed" by dear Rixia's hands...\x01",
            "I'm sure she's very confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right... Before\x01",
            "losing consciousness,\x01",
            "she looked dissatisfied.\x02\x03",
            "#00002FBut Randy, it looks like\x01",
            "you're a little relieved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302F...Ha ha, I guess. Although she's like that,\x01",
            "the fact that she's my cousin doesn't change.\x02\x03",
            "#00303FHonestly, thinkin' about what she did, \x01",
            "I thought it couldn't be helped if she\x01",
            "had brought revenge upon her, but...\x02\x03",
            "#00300FI've got to thank dear Rixia again \x01",
            "for havin' not seeked revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303F...I too will very soon\x01",
            "need to settle things with\x01",
            "my uncle, a real monster.\x02\x03",
            "#00300FWhen that happens, I'll need your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, of course. \x01",
            "We'll combine everyone's strength\x01",
            "and get through this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 2)
    Return()

    # Function_9_3E5C end

    def Function_10_4269(): pass

    label("Function_10_4269")


    ChrTalk(
        0xE,
        "#00303F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYour uncle... \x01",
            "As I suspected, he\x01",
            "was crazily strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FYeah... I was able to hold\x01",
            "out against 'im because\x01",
            "of your help, though.\x02\x03",
            "#00306FHonestly, even if I were to fight 'him\x01",
            "again, I'm not sure I could win.\x02\x03",
            "#00300FAs the strongest jaeger, his name\x01",
            ""Red Ogre" isn't just for show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...If we combine our strengths, I'm\x01",
            "sure we'll overpower him any time.\x02\x03",
            "#00000FBecause you're with us, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304F...Ha ha, that's right. \x01",
            "That's the strength I've obtained.\x02\x03",
            "#00300FFrom now on, I'll have to keep\x01",
            "showin' the foothold I've found...\x02\x03",
            "#00303FTo my late ol' man, and uncle,\x01",
            "to whom I'm somehow indebted.\x01",
            "That'll be the greatest duty I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah... We too will do our\x01",
            "very best to help you with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00309FHa ha, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 3)
    Return()

    # Function_10_4269 end

    def Function_11_458F(): pass

    label("Function_11_458F")


    ChrTalk(
        0xE,
        (
            "#00301FOur final opponents are\x01",
            "the enigmatic milady Mariabell\x01",
            "and Mr. Grimwood, the mastermind.\x02\x03",
            "#00303FOn the basis of fightin' strength\x01",
            "alone, they're more dangerous\x01",
            "than uncle or ol' man Arios...\x02\x03",
            "#00301FBecause they're usin' Keddo,\x01",
            "the "Sept-Terrion of Zero",\x01",
            "they'll definitely be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FYeah... This fight might be even tougher\x01",
            "than the one against Mr. Arios was.\x02\x03",
            "#00001FBut──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FThe whole truth is waiting for us there──\x01",
            "We can't back down now, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FD-Don't finish my sentences.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FHa ha. We've hung out together\x01",
            "so long, I already knew what\x01",
            "you were goin' to say.\x02\x03",
            "#00304FOf course. I'm not plannin' on\x01",
            "takin' a single step backwards.\x02\x03",
            "#00302FI mean, our cute, beloved daughter\x01",
            "is waitin' for her papas, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... You're right.\x01",
            "Let's go to KeA with everyone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 4)
    Return()

    # Function_11_458F end

    def Function_12_48F6(): pass

    label("Function_12_48F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4914")
    Call(1, 14)
    Jump("loc_4AE9")

    label("loc_4914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3E")

    ChrTalk(
        0x10,
        (
            "#10100FNow that we've come this far, \x01",
            "I think all we have to do is\x01",
            "believe in ourselves and bust in.\x02\x03",
            "#10104FTo protect Crossbell going forward... \x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "#10102FBefore being a policemen or a CGF member,\x01",
            "as comrades who live together in this land...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4AE9")

    label("loc_4A3E")


    ChrTalk(
        0x10,
        (
            "#10100FTo protect Crossbell going forward... \x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "Before being a policemen or a CGF member,\x01",
            "as comrades who live together in this land...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE9")

    Jump("loc_565E")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_4C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFA")

    ChrTalk(
        0x10,
        (
            "#10106FI was surprised when that\x01",
            "warship appeared...\x02\x03",
            "#10100FBut I'm glad we arrived somehow\x01",
            "safely at the "huge tree".\x02\x03",
            "#10103FIt's just, it's not a given\x01",
            "that it won't appear again.\x02\x03",
            "#10101FUs standby members have\x01",
            "to be on our guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C70")

    label("loc_4BFA")


    ChrTalk(
        0x10,
        (
            "#10103FIt's not a given that the\x01",
            "warship won't appear again.\x02\x03",
            "#10101FUs standby members have\x01",
            "to be on our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C70")

    Jump("loc_565E")

    label("loc_4C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4ECD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E28")

    ChrTalk(
        0x10,
        (
            "#10103FWith Mr. Arios gone, it seems command\x01",
            "of the entire State Guard has been\x01",
            "transferred to Commander Sonya.\x02\x03",
            "#10100FFor awhile, it looks like they'll be\x01",
            "dealing with the chaos caused by\x01",
            "the appearance of that "huge tree".\x02\x03",
            "#10104FI think it'll be difficult...\x01",
            "But if we leave it to Commander\x01",
            "Sonya, I'm sure it will be fine.\x02\x03",
            "#10100FLet's push onward, to\x01",
            "the objective that is\x01",
            "right in front of us!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4EC8")

    label("loc_4E28")


    ChrTalk(
        0x10,
        (
            "#10104FIf we leave the State\x01",
            "Guard to Commander Sonya,\x01",
            "I'm sure it will be fine.\x02\x03",
            "#10100FLet's push onward, to\x01",
            "the objective that is\x01",
            "right in front of us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC8")

    Jump("loc_565E")

    label("loc_4ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_50EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_501C")

    ChrTalk(
        0x10,
        (
            "#10101FBoth the "Temple of Moon" and "Tower of Stargaze"\x01",
            "were ruins formerly under CGF supervision.\x02\x03",
            "#10106FIf we somehow had just grasped the\x01",
            "true nature of the bells, the situation\x01",
            "wouldn't have gotten this bad...\x02\x03",
            "#10103F...But nothing will come of regret.\x01",
            "Anyway, right now, I have to face forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_50E5")

    label("loc_501C")


    ChrTalk(
        0x10,
        (
            "#10108FIf we had grasped the true nature\x01",
            "of the bells before, the situation\x01",
            "wouldn't have gotten this bad...\x02\x03",
            "#10103F...But nothing will come of regret.\x01",
            "Anyway, right now, I have to face forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E5")

    Jump("loc_565E")

    label("loc_50EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_537D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5270")

    ChrTalk(
        0x10,
        (
            "#10103FShaking the legality of the state independence...\x02\x03",
            "#10101FThat's simply to shake the legality of\x01",
            "the State Guard organization itself.\x02\x03",
            "#10108FI think Commander Sonya will\x01",
            "handle it well, so considerable\x01",
            "chaos should probably be avoided.\x02\x03",
            "#10103F...In a way, it might be a relief that the two major\x01",
            "powers are unable to act due to civil war and panic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5378")

    label("loc_5270")


    ChrTalk(
        0x10,
        (
            "#10101FIf we deliver the invalidity declaration now,\x01",
            "forces at Bellguard and Tangram gates... and\x01",
            "everywhere else too will be rather confused...\x02\x03",
            "#10103F...In a way, it might be a relief that the two major\x01",
            "powers are unable to act due to civil war and panic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5378")

    Jump("loc_565E")

    label("loc_537D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_565E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5398")
    Call(1, 13)
    Jump("loc_565E")

    label("loc_5398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55BA")

    ChrTalk(
        0x10,
        (
            "#10105FAh, M-Mr. Lloyd...\x02\x03",
            "#10111FUmm, I... I was surprised\x01",
            "you could say something\x01",
            "like "You'll be mine", but...\x02\x03",
            "#10106FUm, I fully understand\x01",
            "that you didn't say it\x01",
            "with that meaning!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, "with that meaning"? \x01",
            "Even now, I'm not sure which\x01",
            "meaning you intend, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#10106F(I-I wonder if he's saying it seriously...)\x02\x03",
            "#10100F...*ahem*, anyway. Let's think\x01",
            "of the capture of Michelam\x01",
            "right now, first and foremost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, of course. I'll be\x01",
            "counting on you, Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_565E")

    label("loc_55BA")


    ChrTalk(
        0x10,
        (
            "#10100F...*ahem*, anyway. Let's think\x01",
            "of the capture of Michelam\x01",
            "right now, first and foremost!\x02\x03",
            "I will do my best,\x01",
            "for both Miss Elie and\x01",
            "Chairman MacDowell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_565E")

    TalkEnd(0xFE)
    Return()

    # Function_12_48F6 end

    def Function_13_5662(): pass

    label("Function_13_5662")

    OP_4B(0x10, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01912F*sigh*... I'm really\x01",
            "glad I got to reunite\x01",
            "with you again, big sis.\x02\x03",
            "#01911FOoh, I think I'm\x01",
            "gonna cry again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10112FC'mon. Fran...\x02\x03",
            "#10104F...But, I'm really relieved that\x01",
            "your injuries fully healed.\x01\x02\x03",
            "#10109FAnd it looks like you've been\x01",
            "working well with Mr. Lloyd\x01",
            "and Wazy. Uh uh, good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FC-Come on Noｱl. How long are you\x01",
            "gonna treat me like a kiiid...\x02\x03",
            "#01905F...Oh, right.\x01",
            "You've come to the point that Mr.\x01",
            "Lloyd said "You'll be mine" to yooou.\x02\x03",
            "#01906FWell, it can't be helped if you still  see me\x01",
            "as a kid now that you've stepped and jumped\x01",
            "straight to adulthood...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#10111FY-You dummy...! \x01",
            "What're you saying Fran!?\x02\x03",
            "#10106FMr. Lloyd didn't say it\x01",
            "meaning it in that way..!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FOh wow, you're getting all\x01",
            "embarrassed remembering it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(...I don't know what they're talking\x01",
            "about, but... It's weirdly difficult\x01",
            "to get into their conversation.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 5)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_13_5662 end

    def Function_14_5A23(): pass

    label("Function_14_5A23")


    ChrTalk(
        0x10,
        (
            "#10101FThe end is finally here...\x02\x03",
            "#10103FNow that we've come this far, \x01",
            "I think all we have to do is\x01",
            "believe in ourselves and bust in.\x02\x03",
            "#10108FEven after this incident\x01",
            "is over, many difficulties\x01",
            "lie ahead for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... But in the end, all we\x01",
            "can do is handle the things in\x01",
            "front of us, one by one.\x02\x03",
            "#00000FThe resolution of this incident\x01",
            "itself is just the first step\x01",
            "towards protecting Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10109FUh uh. If my father was alive, \x01",
            "I'm sure he'd say the same thing.\x02\x03",
            "#10103FTo protect Crossbell going forward... \x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "#10102FBefore being a policemen or a CGF member,\x01",
            "as comrades who live together in this land...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 6)
    Return()

    # Function_14_5A23 end

    def Function_15_5CCE(): pass

    label("Function_15_5CCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CEC")
    Call(1, 18)
    Jump("loc_5F12")

    label("loc_5CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3F")

    ChrTalk(
        0xA,
        (
            "#10404FI've felt this for awhile while I was with you.\x01",
            "The "bond" between you all and KeA is the real thing.\x02\x03",
            "#10402FNo matter what happens, as long as\x01",
            "you guys continue to pursue her,\x01",
            "I think there's still hope.\x02\x03",
            "#10409FWell, if this is how it's going\x01",
            "to be, I'll stick with you until\x01",
            "the end. For lovely KeA, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F12")

    label("loc_5E3F")


    ChrTalk(
        0xA,
        (
            "#10404FNo matter what happens, as long as\x01",
            "you guys continue to pursue her,\x01",
            "I think there's still hope.\x02\x03",
            "#10409FWell, if this is how it's going\x01",
            "to be, I'll stick with you until\x01",
            "the end. For lovely KeA, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F12")

    Jump("loc_787F")

    label("loc_5F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_6005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F32")
    Call(1, 17)
    Jump("loc_6000")

    label("loc_5F32")


    ChrTalk(
        0xA,
        (
            "#10404FFinally, I was able to settle\x01",
            "things with him in my own way.\x01",
            "...Allow me to thank you.\x02\x03",
            "#10402FFrom here on I will support you as\x01",
            "a Gralsritter, and as a member of \x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6000")

    Jump("loc_787F")

    label("loc_6005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_END)), "loc_613D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6025")
    Call(1, 55)
    Jump("loc_6138")

    label("loc_6025")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60AE")

    ChrTalk(
        0xA,
        (
            "#10403FIt seems like "he" wants\x01",
            "to settle things with me.\x02\x03",
            "#10400FLet's head for the\x01",
            "barrier once we're ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6138")

    label("loc_60AE")


    ChrTalk(
        0xA,
        (
            "#10403FIt seems like "he" wants\x01",
            "to settle things with me.\x02\x03",
            "#10400FPlace me in the search party.\x01",
            "Let's head for the barrier together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6138")

    Jump("loc_787F")

    label("loc_613D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_62E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_624C")

    ChrTalk(
        0xA,
        (
            "#10404FNow then, it's finally time\x01",
            "to begin our exploration.\x02\x03",
            "#10401FIt's too bad we can't proceed in the Merkabah... \x01",
            "But "he" too is waiting ahead.\x02\x03",
            "#10403FI'll have to advance steadily,\x01",
            "even to finally settle things I\x01",
            "failed to before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_62E3")

    label("loc_624C")


    ChrTalk(
        0xA,
        (
            "#10401F"He" too is waiting ahead\x01",
            "within the "huge tree".\x02\x03",
            "#10403FI'll have to advance steadily,\x01",
            "even to finally settle things I\x01",
            "failed to before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E3")

    Jump("loc_787F")

    label("loc_62E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C4")

    ChrTalk(
        0xA,
        (
            "#10403FNow that that "huge tree" appeared,\x01",
            "it looks like the Holy Nation of\x01",
            "Arteria is in an uproar too.\x02\x03",
            "#10400FAnyhow, this is an "unexpected\x01",
            "miracle" that isn't recorded in\x01",
            "any of the Church's Testaments.\x02\x03",
            "#10408FThe "Salt Pale" was one of\x01",
            "those too. The leaders can't\x01",
            "help but exercise caution...\x02\x03",
            "#10400FBut, as long as KeA is in\x01",
            "there, we can't take it easy.\x02\x03",
            "I'm taking responsibility,\x01",
            "so tell Abbas if you're going \x01",
            "to the "huge tree".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_658D")

    label("loc_64C4")


    ChrTalk(
        0xA,
        (
            "#10404FAs long as KeA's over there, we don't\x01",
            "have time to wait for direction from\x01",
            "the Holy Nation of Arteria.\x02\x03",
            "#10400FI'm taking responsibility,\x01",
            "so tell Abbas if you're going \x01",
            "to the "huge tree".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_658D")

    Jump("loc_787F")

    label("loc_6592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_685C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6764")

    ChrTalk(
        0xA,
        (
            "#10400FOur order and the "Society" have fought\x01",
            "many times, outside the gaze of history.\x01",
            "We are fated opponents, so to speak.\x02\x03",
            "#10403FOur order has looked into them, but\x01",
            "we have especially little information\x01",
            "on the "Fool" and "Steel Maiden".\x02\x03",
            "We'll end up facing them like this,\x01",
            "without effective countermeasures, but...\x02\x03",
            "#10402FNothing ventured, nothing gained,\x01",
            "they say. Anyway, let's dive in and\x01",
            "see if there's a chance at victory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6857")

    label("loc_6764")


    ChrTalk(
        0xA,
        (
            "#10403FOur order has looked into the "Society",\x01",
            "but we have especially little information\x01",
            "on the "Fool" and "Steel Maiden".\x02\x03",
            "#10402FNothing ventured, nothing gained,\x01",
            "they say. Anyway, let's dive in and\x01",
            "see if there's a chance at victory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6857")

    Jump("loc_787F")

    label("loc_685C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_6A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D8")

    ChrTalk(
        0xA,
        (
            "#10402FIt looks like there's especially little\x01",
            "security around the Booster Site.\x02\x03",
            "#10404FIt's outside the State Guard and jagers' security\x01",
            "zone, and if we head there in the Merkabah, it\x01",
            "looks like we'll finish without being interrupted.\x02\x03",
            "#10408FHow will this "declaration\x01",
            "of invalidity" change the future...?\x02\x03",
            "#10409FHu hu, only the Goddess knows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A4B")

    label("loc_69D8")


    ChrTalk(
        0xA,
        (
            "#10404FHow will this "declaration\x01",
            "of invalidity" change the future...?\x02\x03",
            "#10409FHu hu, only the Goddess knows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A4B")

    Jump("loc_787F")

    label("loc_6A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C35")

    ChrTalk(
        0xA,
        (
            "#10402FThe beach at Michelam, eh?\x01",
            "To think we'd be going there in this way...\x02\x03",
            "#10406FIf possible, I'd like to take a leisurely vacation\x01",
            "day on the beach with everyone again, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWe'll take back KeA...\x01",
            "And once everything's\x01",
            "over, I'm sure we will.\x02\x03",
            "#00000FAnd next time, let's\x01",
            "invite the Chief, Abbas and\x01",
            "Commander Sonya as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FAhaha, that would be great!\x02\x03",
            "#10400FI'll put forth every effort to\x01",
            "grab hold of that day, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6CEB")

    label("loc_6C35")


    ChrTalk(
        0xA,
        (
            "#10404FThe beach at Michelam... \x01",
            "Rather than a day off, a hard \x01",
            "fight is waiting for us this time.\x02\x03",
            "#10400FI'll put forth every effort to grab\x01",
            "hold of peaceful days once again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CEB")

    Jump("loc_787F")

    label("loc_6CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_70B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FAB")

    ChrTalk(
        0xA,
        (
            "#10404FOh boy, when it comes to you, Miss Grace,\x01",
            "you always want an interview at all costs.\x02\x03",
            "I can't tell you anything too important\x01",
            "or else Abbas will get mad at me, but...\x02\x03",
            "#10409FSince you're this enthusiastic,\x01",
            "I might tell you some half-truths.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0xA, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E92")
    Jump("loc_6EDC")

    label("loc_6E92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6EB2")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EDC")

    label("loc_6EB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6ED2")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EDC")

    label("loc_6ED2")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EDC")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#02109FAh, that's no good, Wazyyy.\x01",
            "Just limit yourself to the "truths"!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(Abbas is having a hard time too, huh...)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_70B2")

    label("loc_6FAB")


    ChrTalk(
        0xA,
        (
            "#10404FIn short, the "Testaments" group\x01",
            "was a parody name based on\x01",
            "my "Testament" nickname.\x02\x03",
            "#10409FHonestly, I had been okay with whatever name,\x01",
            "but Abbas was so annoying... He's the type\x01",
            "who starts to focus from the superficial.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_70B2")

    Jump("loc_787F")

    label("loc_70B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_7459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7236")

    ChrTalk(
        0xA,
        (
            "#10403FLooks like Rixia is on the\x01",
            "deck, lost in thought.\x02\x03",
            "Arc-en-ciel, Heiyue, and "Yin"'s duty...\x01",
            "There's probably a lot\x01",
            "she's worried about.\x02\x03",
            "#10402FHu hu. If you like, why don't\x01",
            "you give her some advice?\x02\x03",
            "#10409FIt's possible you'll trigger\x01",
            "some kind of flag, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI-I wouldn't give her advice\x01",
            "with such an ulterior motive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_736C")

    label("loc_7236")


    ChrTalk(
        0xA,
        (
            "#10403FLooks like Rixia is on the\x01",
            "deck, lost in thought.\x02\x03",
            "Arc-en-ciel, Heiyue, and "Yin"'s duty...\x01",
            "There's probably a lot\x01",
            "she's worried about.\x02\x03",
            "#10402FHu hu, then... It seems you gave\x01",
            "her some advice...maybe you\x01",
            "triggered some kind of flag?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I didn't give her advice\x01",
            "to trigger such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_736C")

    SetScenarioFlags(0x0, 7)
    Jump("loc_7454")

    label("loc_7374")


    ChrTalk(
        0xA,
        (
            "#10404FEven so, Rixia...\x01",
            "Leaving aside the clothes she's wearing now,\x01",
            "you wouldn't really tell that she's "Yin", hm?\x02\x03",
            "#10400FHu hu, right because her personality is so normal,\x01",
            "I could say it's natural to not notice it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7454")

    Jump("loc_787F")

    label("loc_7459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757C")

    ChrTalk(
        0xA,
        (
            "#10400FNow that Tio and Fran are here, we'll be\x01",
            "able to make efficient use of this ship.\x02\x03",
            "#10404FEven if we find "gaps", there's a\x01",
            "limit to what we can do on our own.\x01",
            "This is a big step forward for us.\x02\x03",
            "#10400FHu hu, this might be the\x01",
            "guidance of Aidios too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_761F")

    label("loc_757C")


    ChrTalk(
        0xA,
        (
            "#10404FWe went to St. Ursula Hospital as our first destination\x01",
            "and rendezvoused with Tio and Fran...\x02\x03",
            "#10400FHu hu, this might be the\x01",
            "guidance of Aidios too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761F")

    Jump("loc_787F")

    label("loc_7624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_787F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_763F")
    Call(1, 16)
    Jump("loc_787F")

    label("loc_763F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77DE")

    ChrTalk(
        0xA,
        (
            "#10406FThings are looking pretty grim... But for\x01",
            "right now, we've got to keep a steady pace.\x02\x03",
            "#10400F...Oh, that's right. I don't mind if\x01",
            "you use the facilities onboard freely.\x02\x03",
            "There are equipment, accessory and workshop\x01",
            "facilities── And if you go to the upper deck\x01",
            "corridor, there's a nap room you can use.\x02\x03",
            "#10409FWhy don't you go to check them out\x01",
            "while also having a look at the crew?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_787F")

    label("loc_77DE")


    ChrTalk(
        0xA,
        (
            "#10400FI don't mind if you use the facilities\x01",
            "onboard the Merkabah freely.\x02\x03",
            "#10409FWhy don't you go to check them out\x01",
            "while also having a look at the crew?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_787F")

    TalkEnd(0xFE)
    Return()

    # Function_15_5CCE end

    def Function_16_7883(): pass

    label("Function_16_7883")


    ChrTalk(
        0xA,
        (
            "#10403FFor starters, we found a "gap" at the\x01",
            "St. Ursula Byroad sandbank before\x01",
            "the accident happened, but...\x02\x03",
            "#10400FFrom now on, we'll need to detect\x01",
            ""gaps" where it looks like we can land.\x02\x03",
            "#10406FThe Merkabah is short of crew, and\x01",
            "things are looking pretty grim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Even so, we can only\x01",
            "proceed one step at a time.\x02\x03",
            "#00001FWe need to get our comrades\x01",
            "and KeA back... I know all too\x01",
            "well that it won't be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHu hu, got it. For now, we've\x01",
            "got to do things the hard way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 7)
    Return()

    # Function_16_7883 end

    def Function_17_7A7E(): pass

    label("Function_17_7A7E")


    ChrTalk(
        0xA,
        "#10402FHey, nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNice work yourself, Wazy...\x01",
            "How are you feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FEh, no need to worry. As you\x01",
            "can see, I'm taking a break.\x02\x03",
            "#10408FBecause the recoil is great,\x01",
            "normally I keep my strength\x01",
            "in check as much as possible...\x02\x03",
            "#10404FHu hu. It's been awhile\x01",
            "since I got so fired up too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou gave everything you\x01",
            "had to defeat Wald...\x02\x03",
            "I guess you needed to do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FYeah, exactly.\x02\x03",
            "#10408F...If I had used my full power since\x01",
            "the very beginning, maybe he wouldn't\x01",
            "have tormented himself so much.\x02\x03",
            "#10403FI'm probably completely\x01",
            "responsible in that respect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHu hu, it's ok.\x01",
            "I'm not regretting it, but it'll have\x01",
            "to serve me as a lesson for the future.\x02\x03",
            "#10404FIn any case...\x01",
            "Finally, I was able to settle\x01",
            "things with him in my own way.\x02\x03",
            "Now, the duty of Wazy Hemisphere, \x01",
            "the Testaments leader, is finished.\x01\x02\x03",
            "#10402FAllow me to thank all of you\x01",
            "who saw this through with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha... You're welcome.\x02\x03",
            "#00000FStrong enemies are waiting\x01",
            "for us ahead too... \x01",
            "We'll be counting on you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHu hu, roger that, leader.\x02\x03",
            "#10404FFrom here on I will support you as\x01",
            "a Gralsritter, and as a member of \x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 1)
    Return()

    # Function_17_7A7E end

    def Function_18_7F50(): pass

    label("Function_18_7F50")


    ChrTalk(
        0xA,
        (
            "#10400FWe got some information from\x01",
            "the "Divine Blade of Wind",\x01",
            "but several mysteries remain.\x02\x03",
            "#10403FThe "Azure-Zero Project"... \x01",
            "Mr. Beardy-Bear planned the whole thing.\x02\x03",
            "#10408FMiss Mariabell must have known the capabilities\x01",
            "of KeA, the "Sept-Terrion of Zero"...\x01",
            "Just how is she planning on using that?\x02\x03",
            "#10406FIt seems the only way to know that\x01",
            "is to question them directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... I'm sure we'll understand\x01",
            "if we make our way to them.\x02\x03",
            "#00008FMaybe even the reason\x01",
            "why KeA joined them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F...Well, you don't need to worry.\x02\x03",
            "#10402FI've felt this for awhile while I was with you.\x01",
            "The "bond" between you all and KeA is the real thing.\x02\x03",
            "#10409FNo matter what happens, as long as\x01",
            "you guys continue to pursue her,\x01",
            "I think there's still hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Right. I'm sure\x01",
            "everything will go well.\x02\x03",
            "#00005FBut, you talk like you're not one of us.\x01",
            "Aren't you part of that "bond", Wazy?\x02\x03",
            "#00004FI'm sure KeA would think so too...\x01",
            "Let's all make our way to her together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F...Hu hu, that's a \x01",
            "nice thing to say.\x02\x03",
            "#10402FWell, if this is how it's going\x01",
            "to be, I'll stick with you until\x01",
            "the end. For lovely KeA, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 2)
    Return()

    # Function_18_7F50 end

    def Function_19_83D3(): pass

    label("Function_19_83D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_8617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83F1")
    Call(1, 21)
    Jump("loc_8612")

    label("loc_83F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8543")

    ChrTalk(
        0xD,
        (
            "#10708F"Yin" and the path of the artist...\x01",
            "I haven't concretely decided which\x01",
            "I'll follow going forward, but...\x02\x03",
            "#10704FRight now, I feel I want to protect \x01",
            "Crossbell... The place where Miss \x01",
            "Ilya and the others live.\x02\x03",
            "#10702FTo protect "that which is\x01",
            "important"... I will do my very\x01",
            "best together with all of you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8612")

    label("loc_8543")


    ChrTalk(
        0xD,
        (
            "#10704FRight now, I feel I want to protect \x01",
            "Crossbell... The place where Miss \x01",
            "Ilya and the others live.\x02\x03",
            "#10702FTo protect "that which is\x01",
            "important"... I will do my very\x01",
            "best together with all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8612")

    Jump("loc_92F8")

    label("loc_8617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_86E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8632")
    Call(1, 20)
    Jump("loc_86DD")

    label("loc_8632")


    ChrTalk(
        0xD,
        (
            "#10703FThanks to all of you, \x01",
            "I was finally able to\x01",
            "settle things with her.\x02\x03",
            "#10702FTo repay that favor too... \x01",
            "I will stick with you until\x01",
            "the end of this incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86DD")

    Jump("loc_92F8")

    label("loc_86E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_END)), "loc_8835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8702")
    Call(1, 54)
    Jump("loc_8830")

    label("loc_8702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A4")

    ChrTalk(
        0xD,
        (
            "#10703F...I'm ready. Let's head for\x01",
            "the barrier immediately.\x02\x03",
            "#10701FTo discover my way\x01",
            "forward as well... \x01",
            "I must meet her once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8830")

    label("loc_87A4")


    ChrTalk(
        0xD,
        (
            "#10703F...I'm ready. Please include\x01",
            "me in the search party.\x02\x03",
            "#10701FTo discover my way\x01",
            "forward as well... \x01",
            "I must meet her once again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8830")

    Jump("loc_92F8")

    label("loc_8835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_89AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890D")

    ChrTalk(
        0xD,
        (
            "#10703F...We've finally come this far.\x02\x03",
            "Many tough opponents are\x01",
            "waiting for us, "her" included.\x02\x03",
            "#10701FLet us harden our resolve.\x01",
            "To grab hold of that which\x01",
            "is precious to us too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_89A9")

    label("loc_890D")


    ChrTalk(
        0xD,
        (
            "#10703FMany tough opponents are\x01",
            "waiting for us, "her" included.\x02\x03",
            "#10701FLet us harden our resolve.\x01",
            "To grab hold of that which\x01",
            "is precious to us too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A9")

    Jump("loc_92F8")

    label("loc_89AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B24")

    ChrTalk(
        0xD,
        (
            "#10703FTo settle things with myself too...\x01",
            "I must settle things with "her" who\x01",
            "is waiting in the "huge tree".\x02\x03",
            "#10701F...My mind is made up. Let us depart\x01",
            "once preparations are complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Now that Arc-en-ciel\x01",
            "is free, possibly...)\x02\x03",
            "(Before heading to the "Huge\x01",
            "Tree", maybe I should take\x01",
            "Rixia to see "that person"...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8BE4")

    label("loc_8B24")


    ChrTalk(
        0xD,
        (
            "#10703FTo settle things with myself too...\x01",
            "I must settle things with "her" who\x01",
            "is waiting in the "huge tree".\x02\x03",
            "#10701F...My mind is made up. Let us depart\x01",
            "once preparations are complete.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE4")

    Jump("loc_8D9B")

    label("loc_8BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D05")

    ChrTalk(
        0xD,
        (
            "#10704FNow that Miss Ilya has given me\x01",
            "courage, I have nothing to fear.\x02\x03",
            "#10701FWhat remains is to settle things with "her"\x01",
            "to also settle things with myself too...\x02\x03",
            "#10702F...My mind is made up. Once\x01",
            "preparations are complete, let\x01",
            "us head for the "huge tree".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8D9B")

    label("loc_8D05")


    ChrTalk(
        0xD,
        (
            "#10704FNow that Miss Ilya has given me\x01",
            "courage, I have nothing to fear.\x02\x03",
            "#10702FOnce preparations are complete,\x01",
            "let us head for the "huge tree".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D9B")

    Jump("loc_92F8")

    label("loc_8DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_8F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EAD")

    ChrTalk(
        0xD,
        (
            "#10708FTo think I, "Yin", would\x01",
            "help save Crossbell...\x02\x03",
            "#10703FIt's a bit late for this, but I feel like\x01",
            "it's a role I do not deserve.\x02\x03",
            "#10701F...However, this too is to free\x01",
            "Crossbell City and Arc-en-ciel...\x01",
            "So I shall do my very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8F75")

    label("loc_8EAD")


    ChrTalk(
        0xD,
        (
            "#10708FTo think I, "Yin", would help\x01",
            "save Crossbell... I feel like\x01",
            "it's a role I do not deserve, but...\x02\x03",
            "#10701FThis too is to free Crossbell City\x01",
            "and Arc-en-ciel... \x01",
            "So I shall do my very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F75")

    Jump("loc_92F8")

    label("loc_8F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_9022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F95")
    Call(1, 8)
    Jump("loc_901D")

    label("loc_8F95")


    ChrTalk(
        0xD,
        (
            "#10708F"Bloody Shirley"...\x01",
            "Her attitude worries me, but...\x02\x03",
            "#10703F...Right now, let's focus on\x01",
            "saving Miss Elie and the Chairman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_901D")

    Jump("loc_92F8")

    label("loc_9022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_92F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921C")

    ChrTalk(
        0xD,
        (
            "#10705FH-Honestly, I'd like you not to\x01",
            "write an article about "Yin"...?\x02\x03",
            "#10706FI'm somehow worried about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FThe real story behind everyone's favorite\x01",
            "theatrical troupe! The history and truth behind\x01",
            "the legendary "Yin"! Rixia Mao's three sizes!\x02\x03",
            "#02109FThis is a rare chance so,\x01",
            "c'mon, tell me everythiiing♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10706FUuuh, Mr. Lloooyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FS-Somehow dodge her questions\x01",
            "the best you can...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x1, 0)
    Jump("loc_92F8")

    label("loc_921C")


    ChrTalk(
        0xD,
        (
            "#10706FIt's always been the Troupe Chief who\x01",
            "cut her short at the proper time for me...\x01",
            "T-To think she was this persistent...\x02\x03",
            "#10709FReally, I'd like you not to\x01",
            "write an article...? I'm\x01",
            "somehow worried about it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92F8")

    TalkEnd(0xFE)
    Return()

    # Function_19_83D3 end

    def Function_20_92FC(): pass

    label("Function_20_92FC")


    ChrTalk(
        0xD,
        (
            "#10703F"Bloody Shirley"...\x02\x03",
            "Like her name says, her path\x01",
            "must've been dyed with blood.\x02\x03",
            "She lives for that and because\x01",
            "she finds joy in battles she's\x01",
            "the girl she's today...\x02\x03",
            "#10708FAs "Yin", I don't view that as\x01",
            "something not regarding me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10704FBut... I feel I have finally\x01",
            "changed, in a real sense.\x02\x03",
            "#10702FMiss Ilya, Mr. Lloyd and everyone \x01",
            "else, too... I feel I've changed \x01",
            "through the many people I've met.\x02\x03",
            "#10703FTo the extent that she and I, who're\x01",
            "similar people, ended up walking\x01",
            "on completely different paths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FBy meeting people...\x02\x03",
            "#00000FIf you think about it,\x01",
            "maybe all this was fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10702FYes... I really think that too.\x02\x03",
            "#10704FThanks to all of you, \x01",
            "I was finally able to\x01",
            "settle things with her.\x02\x03",
            "#10702FTo repay that favor too... \x01",
            "I will stick with you until\x01",
            "the end of this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we're counting on you, Rixia.\x02\x03",
            "We'll save KeA together and we'll return\x01",
            "smiling to Miss Ilya and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10709FUh uh, right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 5)
    Return()

    # Function_20_92FC end

    def Function_21_96F1(): pass

    label("Function_21_96F1")


    ChrTalk(
        0xD,
        (
            "#10708F...The end of this\x01",
            "journey grows close.\x02\x03",
            "#10703FI don't know how useful\x01",
            ""Yin"'s powers will be\x01",
            "against Miss Mariabell, but...\x02\x03",
            "#10701FAnyway, I will do everything I\x01",
            "can, together with all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... I'm counting on you.\x02\x03",
            "#00009FHa ha, maybe I'm late in saying this, but...\x01",
            "Fighting, cooperating with each other...\x01",
            "We did that many times too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10709FA-Ahaha...\x01",
            "Thank you for that.\x02\x03",
            "#10703F"Yin" and the path of the artist...\x01",
            "I haven't concretely decided which\x01",
            "I'll follow going forward, but...\x02\x03",
            "#10702FRight now, I feel I want to protect \x01",
            "Crossbell... The place where Miss \x01",
            "Ilya and the others live.\x02\x03",
            "#10704FIf the power I have as "Yin"\x01",
            "is of use, then... I shall\x01",
            "display it without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThanks, Rixia... \x01",
            "We'll be counting on you.\x02\x03",
            "#00000FLet's do our best together, to\x01",
            "protect what is precious to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10702FYes...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 6)
    Return()

    # Function_21_96F1 end

    def Function_22_9A60(): pass

    label("Function_22_9A60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7E")
    Call(1, 23)
    Jump("loc_9C35")

    label("loc_9A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B75")

    ChrTalk(
        0x13,
        (
            "#01203F#3COnce, "Demiourgos", the Sept-Terrion\x01",
            "of Mirage, chose to annihilate itself...\x02\x03",
            "#01200FI can't say that KeA \x01",
            "couldn't have arrived at \x01",
            "the same conclusion.\x02\x03",
            "Child of man, take KeA back\x01",
            "and stop that from happening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9C35")

    label("loc_9B75")


    ChrTalk(
        0x13,
        (
            "#01203F#3CI can't say that KeA couldn't\x01",
            "have arrived at the same conclusion of\x01",
            ""Demiourgos", the Sept-Terrion of Mirage.\x02\x03",
            "#01200FChild of man, take KeA back\x01",
            "and stop that from happening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C35")

    Jump("loc_AACF")

    label("loc_9C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_9DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2F")

    ChrTalk(
        0x13,
        (
            "#01203F#3CThere's no doubt that KeA is\x01",
            "somewhere inside the "huge tree".\x02\x03",
            "#01200FMaybe in its deepest place...\x01",
            "Together with that Crois clan woman\x01",
            "and the wirepuller lawyer.\x02\x03",
            "Call me any time if\x01",
            "you need my help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9DAB")

    label("loc_9D2F")


    ChrTalk(
        0x13,
        (
            "#01203F#3CThere's no doubt that KeA is\x01",
            "somewhere inside the "huge tree".\x02\x03",
            "#01200FCall me any time if\x01",
            "you need my help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DAB")

    Jump("loc_AACF")

    label("loc_9DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EE7")

    ChrTalk(
        0x13,
        (
            "#01200F#3CI don't have the slightest\x01",
            "idea how much you'll be\x01",
            "able to do to that "huge tree".\x02\x03",
            "It wouldn't be an exaggeration to say that...\x01",
            "It has power rivaling that of the Goddess.\x02\x03",
            "#01203FTo think that the children of man deep-rooted\x01",
            "delusions could arrive at such a point...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9FBE")

    label("loc_9EE7")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIt wouldn't be an exaggeration to say that...\x01",
            "That "huge tree", has power\x01",
            "rivaling that of the Goddess.\x02\x03",
            "#01203FTo think that the children of man deep-rooted\x01",
            "delusions could arrive at such a point...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FBE")

    Jump("loc_AACF")

    label("loc_9FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18B")

    ChrTalk(
        0x13,
        (
            "#01203F#3CThe bells located in Crossbell are\x01",
            "things for creating a "place" where \x01",
            "to amplify the "Sept-Terrion" power...\x02\x03",
            "#01200FIf we reference this to the present situation,\x01",
            "we can probably believe Jｶrg's study results.\x02\x03",
            "#01203FTo think that the children of\x01",
            "man did such a deed...\x01",
            "They even created that Cult's cradle...\x02\x03",
            "#01200FOnce again, the alchemists of the Crois clan seem\x01",
            "to have some absurd deep-rooted delusions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A25C")

    label("loc_A18B")


    ChrTalk(
        0x13,
        (
            "#01203F#3CTo think that the children of\x01",
            "man did such a deed...\x01",
            "They even created that Cult's cradle...\x02\x03",
            "#01200FOnce again, the alchemists of the Crois clan seem\x01",
            "to have some absurd deep-rooted delusions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A25C")

    Jump("loc_AACF")

    label("loc_A261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27C")
    Call(1, 4)
    Jump("loc_A485")

    label("loc_A27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3B0")

    ChrTalk(
        0x13,
        (
            "#01203F#3CAs you're now, you don't\x01",
            "need my protection.\x02\x03",
            "#01200FLike before, I'll stay behind and\x01",
            "you can call me when needed.\x02\x03",
            "From now on, I'll come running\x01",
            "to battle in my original form.\x02\x03",
            "#01203FHu hu, if those are the kind of monsters\x01",
            "roaming around, it seems they'll be easy prey.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A485")

    label("loc_A3B0")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIf you'll call me in your time of need,\x01",
            "From now on, I'll come running\x01",
            "to battle in my original form.\x02\x03",
            "#01203FHu hu, if those are the kind of monsters\x01",
            "roaming around, it seems they'll be easy prey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A485")

    Jump("loc_AACF")

    label("loc_A48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69C")

    ChrTalk(
        0x13,
        (
            "#01200F#3CLeave to me the diversions against the jaegers.\x01",
            "If I return to my original form, I should\x01",
            "be able to lure many of them.\x02\x03",
            "During that time, drive away the dispersed force\x01",
            "and head to where Elie and the Chairman are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe opponents are jaegers. I think they'll \x01",
            "be a lot dangerous for you too, Zeit...\x02\x03",
            "#00001FPlease, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHu hu, don't worry.\x01",
            "I don't plan to go down easily.\x02\x03",
            "#01200FI swear on my Divine Wolf pride that\x01",
            "I'll make sport of a lot of enemies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A745")

    label("loc_A69C")


    ChrTalk(
        0x13,
        (
            "#01203F#3CIf I return to my original form, I should\x01",
            "be able to lure many of them.\x02\x03",
            "#01200FI swear on my Divine Wolf pride that\x01",
            "I'll make sport of a lot of enemies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A745")

    Jump("loc_AACF")

    label("loc_A74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_A831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A765")
    Call(1, 3)
    Jump("loc_A82C")

    label("loc_A765")


    ChrTalk(
        0x13,
        (
            "#01200F#3CMy family has been keeping an eye on Crossbell\x01",
            "for generations, since the era Ursula lived in.\x02\x03",
            "They're probably somewhere watching\x01",
            "the situation attentively.\x01",
            "You don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A82C")

    Jump("loc_AACF")

    label("loc_A831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_AACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA1A")

    ChrTalk(
        0x13,
        "#01200F#3C...That nurse woman...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FEhhm...\x01",
            "I there something wrong with sister Cecil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3C...Hu hu, no, nothing.\x01",
            "I thought it was karma for sure.\x02\x03",
            "It's nothing important, \x01",
            "so don't mind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CIt any case, I could say\x01",
            "it was fortuitous to be\x01",
            "able to reunite with Tio.\x02\x03",
            "Now go to get back\x01",
            "your SSS comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FY-Yeah. I don't understand very well, but...\x01",
            "I'll do that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AACF")

    label("loc_AA1A")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIn any case, I could say\x01",
            "it was fortuitous to be\x01",
            "able to reunite with Tio.\x02\x03",
            "She seems kind of busy now, but...\x01",
            "Hu hu, I guess I'll go check\x01",
            "on how she's doing later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AACF")

    TalkEnd(0xFE)
    Return()

    # Function_22_9A60 end

    def Function_23_AAD3(): pass

    label("Function_23_AAD3")


    ChrTalk(
        0x13,
        (
            "#01200F#3COnce, "Demiourgos", the Sept-Terrion of\x01",
            "Mirage, chose to annihilate itself...\x02\x03",
            "Lloyd, I told you that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt went berserk, and so, to defend the\x01",
            "people he hurt who it should've protected...\x01",
            "It was like that, right?\x02\x03",
            "#00003F...Even KeA who is the "Sept-Terrion\x01",
            "of Zero", will end up doing that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3C...I don't know.\x02\x03",
            "However, becoming the "Sept-Terrion of Zero" she,\x01",
            "in the end, even  brought forth that  "huge tree"\x01",
            "that has a power rivaling that of the Goddess.\x02\x03",
            "At present, there's no guarantee that\x01",
            "she'll be able to control such immense\x01",
            "power in the future.\x02\x03",
            "#01203FI can't say that she couldn't have\x01",
            "arrived at the same conclusion of\x01",
            ""Demiourgos", the Sept-Terrion of Mirage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00001FWell, as long as we're here,\x01",
            "I won't let her do that...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01200F#3C...Hu hu, that's exactly how you're.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_23_AAD3 end

    def Function_24_AE37(): pass

    label("Function_24_AE37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7F), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE5E")
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1DE, 3)

    label("loc_AE5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6B), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE79")
    Call(1, 53)
    Jump("loc_B640")

    label("loc_AE79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AF69")

    ChrTalk(
        0x14,
        (
            "#00603FYou have your own qualities.\x01",
            "By growing those, you'll be able to\x01",
            "get close to be an excellent detective.\x02\x03",
            "#00602FIn the future too, you'll have to devote yourself\x01",
            "even more to aim to be your own kind of detective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B640")

    label("loc_AF69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_B14B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF84")
    Call(1, 25)
    Jump("loc_B146")

    label("loc_AF84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0A6")

    ChrTalk(
        0x14,
        (
            "#00603FThe death of Guy Bannings... Three\x01",
            "years have passed since then, and the\x01",
            "real truth has finally come to light.\x02\x03",
            "All that's left is to resolve\x01",
            "this situation, in a real sense.\x02\x03",
            "#00602FLet's go, Bannings. Now is the time to\x01",
            "show me you can surpass your brother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B146")

    label("loc_B0A6")


    ChrTalk(
        0x14,
        (
            "#00603FAll that's left is to resolve\x01",
            "this situation, in a real sense.\x02\x03",
            "#00602FLet's go, Bannings. Now is the time to\x01",
            "show me you can surpass your brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B146")

    Jump("loc_B640")

    label("loc_B14B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_B3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2BB")

    ChrTalk(
        0x14,
        (
            "#00600FDon't stop moving, Bannings.\x01",
            "To arrive at the truth, you can\x01",
            "only take one step at a time.\x02\x03",
            "#00603FAbove all, we need to resolve this incident\x01",
            "quickly. We don't know what impact this\x01",
            ""huge tree" will have on Crossbell.\x02\x03",
            "#00608FLawyer Ian, MacLaine... They won't be\x01",
            "easy opponents to deal with, but\x01",
            "I'm sure we can overcome them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B3A1")

    label("loc_B2BB")


    ChrTalk(
        0x14,
        (
            "#00600FWe need to resolve this incident\x01",
            "quickly. We don't know what impact this\x01",
            ""huge tree" will have on Crossbell.\x02\x03",
            "#00608FLayer Ian, MacLaine... They won't be\x01",
            "easy opponents to deal with, but\x01",
            "I'm sure we can overcome them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3A1")

    Jump("loc_B640")

    label("loc_B3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B564")

    ChrTalk(
        0x14,
        (
            "#00608FI can't believe it... To think Lawyer\x01",
            "Ian was the mastermind...\x02\x03",
            "#00610FGuh, how pitiful, considering \x01",
            "I visited his office frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F...Anyway, the only way is to meet\x01",
            "with Lawyer Ian and MacLaine directly\x01",
            "and question their motives.\x02\x03",
            "#00601FThis is no longer a problem for the\x01",
            "SSS alone. I will do whatever it\x01",
            "takes to grab hold of the truth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B640")

    label("loc_B564")


    ChrTalk(
        0x14,
        (
            "#00603FAnyway, the only way is to meet\x01",
            "with Lawyer Ian and MacLaine\x01",
            "directly and question their motives.\x02\x03",
            "#00600FThis is no longer a problem for the\x01",
            "SSS alone. I will do whatever it\x01",
            "takes to grab hold of the truth!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B640")

    TalkEnd(0xFE)
    Return()

    # Function_24_AE37 end

    def Function_25_B644(): pass

    label("Function_25_B644")


    ChrTalk(
        0x14,
        (
            "#00600FThe death of Guy Bannings... Three years\x01",
            "have passed since then, and the real\x01",
            "truth has finally come to light, huh.\x02\x03",
            "#00603FAnd MacLaine bore that\x01",
            "heavy burden to this day.\x02\x03",
            "#00608F...What an awkward guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHe bore everything himself,\x01",
            "cut a way out and\x01",
            "proceeded forward...\x02\x03",
            "#00008FThat might be why Mr.\x01",
            "Arios was so strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F...But, that was a misguided strength.\x02\x03",
            "#00608FHe should've understood that too... \x01",
            "That's why he gave way to you all.\x02\x03",
            "#00600FAnyway, Bannings. \x01",
            "With this, you're over\x01",
            "Guy's death, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Yes. I'd like to\x01",
            "sort it out once again,\x01",
            "but I'm good for now.\x02\x03",
            "#00001FNow there's the final "barrier"...\x01",
            "I've got to focus on overcoming\x01",
            "Lawyer Ian and Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00604FGood then.\x02\x03",
            "#00602FTo resolve this case\x01",
            "in a real sense...\x01",
            "You can only advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 2)
    Return()

    # Function_25_B644 end

    def Function_26_B995(): pass

    label("Function_26_B995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9A3")
    Call(0, 11)
    Return()

    label("loc_B9A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9C5")
    Call(1, 56)
    TalkEnd(0xFE)
    Return()

    label("loc_B9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB37")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F3")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x0, 0)

    label("loc_B9F3")


    ChrTalk(
        0x8,
        (
            "#12100F...That's right. Since you're\x01",
            "here, I'll give you this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Abbas' Account"\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        (
            "#00000FA "Pom!" account?\x01",
            "You play too, Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FOnly when I have free time, though.\x02\x03",
            "#12100FI'll be your opponent if you want, \x01",
            "so please challenge me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB32")
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB32")

    Jump("loc_BB74")

    label("loc_BB37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB4D")
    Call(1, 28)
    Jump("loc_BB74")

    label("loc_BB4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB63")
    Call(1, 29)
    Jump("loc_BB74")

    label("loc_BB63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB74")
    Call(1, 30)

    label("loc_BB74")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BBD8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Move with Merkabah\x01",      # 1
            "Change Party\x01",            # 2
            "Quit\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_BC1A")

    label("loc_BBD8")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Move with Merkabah\x01",      # 1
            "Quit\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC1A")

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC39"),
        (1, "loc_D596"),
        (2, "loc_D8DA"),
        (SWITCH_DEFAULT, "loc_D8F6"),
    )


    label("loc_BC39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_BDA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2F")

    ChrTalk(
        0x8,
        (
            "#12100FWe might have to get involved with\x01",
            "the "Red Constellation" from now on...\x02\x03",
            "But right now, resolving this\x01",
            "incident is more important.\x02\x03",
            "You should make sure you're prepared\x01",
            "before heading to the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BDA3")

    label("loc_BD2F")


    ChrTalk(
        0x8,
        (
            "#12100FAs knights, we too will fulfill\x01",
            "our duties to the end.\x02\x03",
            "You all should make sure\x01",
            "you're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA3")

    Jump("loc_D591")

    label("loc_BDA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_BE33")

    ChrTalk(
        0x8,
        (
            "#12100F...I'm sure those\x01",
            "Vipers are worried\x01",
            "about Wald too.\x02\x03",
            "We'll have to retrieve him when\x01",
            "danger has left Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D591")

    label("loc_BE33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_C162")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF2D")

    ChrTalk(
        0x8,
        (
            "#12100FThe airframe has sustained light\x01",
            "damage. Flight won't be a problem.\x02\x03",
            "The ship can withdraw\x01",
            "from the "huge tree"\x01",
            "at any time.\x02\x03",
            "If you would like to withdraw from\x01",
            "the "huge tree", just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BFCB")

    label("loc_BF2D")


    ChrTalk(
        0x8,
        (
            "#12100FFor the time being, it seems the\x01",
            "Merkabah has avoided significant damage.\x02\x03",
            "If you would like to withdraw from\x01",
            "the "huge tree", just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFCB")

    Jump("loc_C15D")

    label("loc_BFD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0BC")

    ChrTalk(
        0x8,
        (
            "#12100FThe airframe has sustained light\x01",
            "damage. Flight won't be a problem.\x02\x03",
            "We were able to secure a safe\x01",
            "route into the "Tree of Azure".\x02\x03",
            "If you would like to once again go to\x01",
            "the "huge tree", just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C15D")

    label("loc_C0BC")


    ChrTalk(
        0x8,
        (
            "#12100FFor the time being, it seems the\x01",
            "Merkabah has avoided significant damage.\x02\x03",
            "If you would like to once again go to\x01",
            "the "huge tree", just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C15D")

    Jump("loc_D591")

    label("loc_C162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C34A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29A")

    ChrTalk(
        0x8,
        (
            "#12100FAs for the meaning of the appearance\x01",
            "of the "Tree of Azure", even the Church\x01",
            "has no idea as of yet.\x02\x03",
            "If we enter it, we\x01",
            "have no idea what\x01",
            "could happen.\x02\x03",
            "It's possible that it could\x01",
            "fall on Crossbell, but...\x02\x03",
            "If there's something\x01",
            "you have to do, that\x01",
            "might take precedence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C345")

    label("loc_C29A")


    ChrTalk(
        0x8,
        (
            "#12100FAs for the meaning of the appearance\x01",
            "of the "Tree of Azure" even the Church\x01",
            "has no idea as of yet.\x02\x03",
            "At any rate, make sure you're\x01",
            "prepared before entering it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C345")

    Jump("loc_D591")

    label("loc_C34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C816")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_C5D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C502")

    ChrTalk(
        0x8,
        (
            "#12100FThe last of the bells we must stop is in the "Tower\x01",
            "of Stargaze" on the outskirts of St. Ursula Byroad.\x02\x03",
            "But the "Steel Maiden", one of the\x01",
            "Anguis, and her subordinates, \x01",
            "the walkｸres, lie in wait for you.\x02\x03",
            "Overcoming them will be next to impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...We have to do it. We'll find\x01",
            "out our chance at victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FHmm. Well said. If you have\x01",
            "made up your mind, then go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C5D2")

    label("loc_C502")


    ChrTalk(
        0x8,
        (
            "#12100FThe "Steel Maiden", one of the\x01",
            "Anguis, and her subordinates,\x01",
            "the walkｸres lie in wait for you.\x02\x03",
            "Overcoming them will be next to impossible...\x01",
            "But if you're determined,  then show me you'll do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5D2")

    Jump("loc_C811")

    label("loc_C5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C767")

    ChrTalk(
        0x8,
        (
            "#12100FOur first destination is the\x01",
            ""Temple of Moon"... A Middle\x01",
            "Ages ruin in the Mainz region.\x02\x03",
            "According to Meister Jｶrg, Campanella\x01",
            "the "Fool", one of the Enforcers,\x01",
            "is waiting for you there...\x02\x03",
            "He normally works behind the scenes,\x01",
            "and we have hardly any information on\x01",
            "him. ...He's a mysterious character.\x02\x03",
            "I don't know what he\x01",
            "has in store for you.\x01",
            "Be ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C811")

    label("loc_C767")


    ChrTalk(
        0x8,
        (
            "#12100FCampanella the "Fool", one of the\x01",
            "Enforcers, is waiting for you\x01",
            "at the "Temple of Moon"...\x02\x03",
            "I don't know what he\x01",
            "has in store for you.\x01",
            "Be ready for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C811")

    Jump("loc_D591")

    label("loc_C816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_CA8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9C3")

    ChrTalk(
        0x8,
        (
            "#12100FIt seems the State Guard and jaegers on the\x01",
            "ground are on high alert because Chairman\x01",
            "MacDowell has been taken from them.\x02\x03",
            "Under these conditions, I don't think\x01",
            "we can land the Merkabah anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... In that case, \x01",
            "I think we should focus on\x01",
            "the plan at the Booster Site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes. All that's left is to\x01",
            "choose the plan's start time.\x02\x03",
            "Speak to me once you're ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA87")

    label("loc_C9C3")


    ChrTalk(
        0x8,
        (
            "#12100FBecause of the high alert, we\x01",
            "can't land the Merkabah anywhere.\x02\x03",
            "You should focus on\x01",
            "making the plan at the\x01",
            "Booster Site a success.\x02\x03",
            "I'm ready on my end. \x01",
            "Speak to me once you're too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA87")

    Jump("loc_D591")

    label("loc_CA8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_CD81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC68")

    ChrTalk(
        0x8,
        (
            "#12100FOnce you arrive at Michelam,\x01",
            "interception by jaegers will\x01",
            "begin immediately.\x02\x03",
            "To avoid anti-aircraft weapons\x01",
            "fire, the Merkabah will temporarily\x01",
            "hide itself high in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOnce we land, we can't return until we\x01",
            "save Elie and Chairman MacDowell, huh.\x01",
            "This is sure to be a tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes. Most likely worse than you're imagining.\x02\x03",
            "Equipment, orbments, restoratives...\x01",
            "You should make sure they're all in order.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CD7C")

    label("loc_CC68")


    ChrTalk(
        0x8,
        (
            "#12100FOnce the fighting starts at Michelam, this\x01",
            "ship will temporarily hide itself high in\x01",
            "the sky to avoid anti-aircraft weapons fire.\x02\x03",
            "You won't be able to return to the ship during\x01",
            "this time. You should make sure your weapons,\x01",
            "orbments and restoratives are in order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD7C")

    Jump("loc_D591")

    label("loc_CD81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_CF8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEFF")

    ChrTalk(
        0x8,
        (
            "#12100FThat reporter seems to be thoroughly\x01",
            "researching this Merkabah and Wazy.\x02\x03",
            "...Man. It's unprecedented\x01",
            "to take a reporter aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well... I'm sure\x01",
            "she's just curious. \x01",
            "Isn't it fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F...Well, whatever. Wazy\x01",
            "gave permission, after all.\x02\x03",
            "If the worst happens,\x01",
            "I'll have you take\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Why me...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CF88")

    label("loc_CEFF")


    ChrTalk(
        0x8,
        (
            "#12100FMan, it's unprecedented for\x01",
            "one involved in journalism\x01",
            "to come aboard...\x02\x03",
            "Well, Wazy gave permission,\x01",
            "so it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF88")

    Jump("loc_D591")

    label("loc_CF8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_D10B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D064")

    ChrTalk(
        0x8,
        (
            "#12100FThe CGF Resistance is acting for\x01",
            "a different cause than "Heiyue"...\x02\x03",
            "Both of them have risen in revolt\x01",
            "and left the President's side.\x02\x03",
            "If you're going, maybe you should hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D106")

    label("loc_D064")


    ChrTalk(
        0x8,
        (
            "#12100FEven if they're the CGF, they won't\x01",
            "hold out against the State Guard and\x01",
            "jaegers' battle strength for long.\x02\x03",
            "If you're going, maybe you should hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D106")

    Jump("loc_D591")

    label("loc_D10B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D3B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2BC")

    ChrTalk(
        0x8,
        (
            "#12100FThe "Heaven's Wheel" the Merkabah\x01",
            "uses for its engine was originally a\x01",
            "flight-capable artifact vehicle...\x02\x03",
            "After the orbal revolution, we improved the shape\x01",
            "to its current form with the help of the Foundation.\x02\x03",
            "In addition, we have a small part in\x01",
            "development of tactical orbments.\x02\x03",
            "...But in the end, it is unofficial to\x01",
            "the common people. Careful that this\x01",
            "information does not leak outside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D3AB")

    label("loc_D2BC")


    ChrTalk(
        0x8,
        (
            "#12100FBoth this Merkabah and tactical\x01",
            "orbments were first born out of a partnership\x01",
            "between the Foundation and the Church...\x02\x03",
            "...In the end, it is unofficial to\x01",
            "the common people. Careful that this\x01",
            "information does not leak outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3AB")

    Jump("loc_D591")

    label("loc_D3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3CB")
    Call(1, 27)
    Jump("loc_D591")

    label("loc_D3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4F9")

    ChrTalk(
        0x8,
        (
            "#12100FWhen we move to somewhere new, we need to\x01",
            "be on guard against the "Aions" per Wazy's\x01",
            "orders, but the current system is sufficient.\x02\x03",
            "There's no need to worry\x01",
            "about us. You should get your\x01",
            "gear and orbments in order.\x02\x03",
            "Speak with me once you're\x01",
            "ready to head to the surface.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D591")

    label("loc_D4F9")


    ChrTalk(
        0x8,
        (
            "#12100FThere's no need to worry\x01",
            "about us. You should get your\x01",
            "gear and orbments in order.\x02\x03",
            "Speak with me once you're\x01",
            "ready to head to the surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D591")

    Jump("loc_D900")

    label("loc_D596")

    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D8CB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6B9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D5EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6B4")
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6AF")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6AF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D6A0")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D690")
    Call(0, 6)
    Jump("loc_D693")

    label("loc_D690")

    Call(0, 5)

    label("loc_D693")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D6AF")

    label("loc_D6A0")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D6AF")

    Jump("loc_D5EF")

    label("loc_D6B4")

    Jump("loc_D8C5")

    label("loc_D6B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D6D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D79B")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D796")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D796")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D787")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D777")
    Call(0, 6)
    Jump("loc_D77A")

    label("loc_D777")

    Call(0, 5)

    label("loc_D77A")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D796")

    label("loc_D787")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D796")

    Jump("loc_D6D6")

    label("loc_D79B")

    Jump("loc_D8C5")

    label("loc_D7A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D887")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D882")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D87D")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D87D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D86E")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D85E")
    Call(0, 6)
    Jump("loc_D861")

    label("loc_D85E")

    Call(0, 5)

    label("loc_D861")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D87D")

    label("loc_D86E")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D87D")

    Jump("loc_D7BD")

    label("loc_D882")

    Jump("loc_D8C5")

    label("loc_D887")

    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8A3")
    Call(0, 12)

    label("loc_D8A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8BA")
    Call(0, 6)
    Jump("loc_D8BD")

    label("loc_D8BA")

    Call(0, 5)

    label("loc_D8BD")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)

    label("loc_D8C5")

    Return()

    label("loc_D8CB")

    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_D900")

    label("loc_D8DA")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D900")

    label("loc_D8F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D900")

    Jump("loc_BB85")

    label("loc_D905")

    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_B995 end

    def Function_27_D90C(): pass

    label("Function_27_D90C")


    ChrTalk(
        0x8,
        (
            "#12100FA communication came in just now.\x01",
            "Merkabah No. 5 has successfully\x01",
            "shaken of the "Aion".\x02\x03",
            "Sir Graham and his\x01",
            "crew are uninjured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... That's a relief.\x02\x03",
            "#00005F...Come to think of it, Abbas. Is it ok\x01",
            "for you to be away from the controls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo need to worry... \x01",
            "I can control  most of the "Merkabah"'s\x01",
            "functions from this seat.\x02\x03",
            "And, because we are high in the sky\x01",
            "above a "gap" in automatic pilot mode,\x01",
            "there's no need to sit in the cockpit.\x02\x03",
            "When we move to somewhere new, we need to\x01",
            "be on guard against the "Aions" per Wazy's\x01",
            "orders, but the current system is sufficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... That's indeed\x01",
            "highly efficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FAnyway, make sure you're\x01",
            "ready while you're aboard.\x02\x03",
            "Speak with me once you're\x01",
            "ready to head to the surface.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 3)
    Return()

    # Function_27_D90C end

    def Function_28_DC20(): pass

    label("Function_28_DC20")


    ChrTalk(
        0x8,
        (
            "#12100FUsing the airframe's\x01",
            "armor and an anti-shock\x01",
            "field as a bulldozer...\x02\x03",
            "The airframe has sustained light\x01",
            "damage. Flight won't be a problem.\x02\x03",
            "The ship can withdraw\x01",
            "from the "huge tree"\x01",
            "at any time.\x02\x03",
            "If you would like to withdraw from\x01",
            "the "huge tree", just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 5)
    Return()

    # Function_28_DC20 end

    def Function_29_DD3B(): pass

    label("Function_29_DD3B")


    ChrTalk(
        0x8,
        (
            "#12100FIt seems Wald is out of the way.\x02\x03",
            "...I've known him for two years,\x01",
            "ever since I infiltrated\x01",
            "Crossbell with Wazy...\x02\x03",
            "Wazy seemed to be enjoying\x01",
            "himself ever since we formed\x01",
            "the Testaments for cover.\x02\x03",
            "Although a Revache\x01",
            "plot made it dangerous\x01",
            "for a time...\x02\x03",
            "To Wazy, Wald was a\x01",
            "good fighting partner,\x01",
            "and even a good friend.\x02\x03",
            "#12102FI'm sure Wald thinks the same of Wazy, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FT-They certainly did work well together, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FThe fact that Wazy held\x01",
            "back might have been one\x01",
            "element of the motive.\x02\x03",
            "Well, because Wazy doesn't say it,\x01",
            "I can't be really sure, so...\x02\x03",
            "...This conversation was pointless.\x01",
            "Don't say a word of it to anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FS-Sure, alright.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 6)
    Return()

    # Function_29_DD3B end

    def Function_30_E003(): pass

    label("Function_30_E003")


    ChrTalk(
        0x8,
        (
            "#12100F...Just now, when you were\x01",
            "fighting the "Divine Blade"...\x02\x03",
            "The radar detected a\x01",
            "flying object entering\x01",
            "this "Sanctuary".\x02\x03",
            "It appears to be the Red \x01",
            "Constellation's "Beowulf".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh... It was all right!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FHm, it seems they landed at a different point\x01",
            "without paying attention to us and after a\x01",
            "little while, they withdrew from the "huge tree".\x02\x03",
            "Most likely, they were\x01",
            "here to collect the "Red Ogre"\x01",
            "and "Bloody Shirley".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... \x01",
            "As an officer, I would've liked\x01",
            "to question them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, it can't be helped.\x01",
            "It would've been impossible to stop\x01",
            "them just with the standby squad.\x02\x03",
            "Also, that proficiency in retreating\x01",
            "is characteristic of jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt's possible we might meet\x01",
            "them again someday...\x02\x03",
            "#00001F...But right now, we need\x01",
            "to focus on resolving\x01",
            "this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes, exactly.\x02\x03",
            "You should make sure you're prepared\x01",
            "before heading to the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 7)
    Return()

    # Function_30_E003 end

    def Function_31_E3D0(): pass

    label("Function_31_E3D0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E48F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6E), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3FB")
    Call(1, 52)
    TalkEnd(0xC)
    Return()

    label("loc_E3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_E48F")

    ChrTalk(
        0xC,
        (
            "#01909FPlease take good care\x01",
            "of that charm, ok?\x02\x03",
            "I made it while praying for\x01",
            "everyone's safety, so I'm\x01",
            "sure it will be effective!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_E48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D2")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5AE")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E53A")
    Jump("loc_E584")

    label("loc_E53A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E55A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E584")

    label("loc_E55A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E57A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E584")

    label("loc_E57A")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E584")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_E5BE")

    label("loc_E5AE")

    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x0, 0)

    label("loc_E5BE")


    ChrTalk(
        0xC,
        (
            "#01900FEveryone, do you know of an\x01",
            "orbal game called "Pom!"?\x02\x03",
            "#01909FHu hu, actually I began playing it too.\x01",
            "If you want, let us exchange accounts.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Fran's Account" obtained.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6BB")
    ClearChrFlags(0xC, 0x10)

    label("loc_E6BB")

    SetChrSubChip(0xC, 0x0)
    Jump("loc_E6CD")

    label("loc_E6C4")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6CD")

    Jump("loc_FE73")

    label("loc_E6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_E8A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6ED")
    Call(1, 33)
    Jump("loc_E89C")

    label("loc_E6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E812")

    ChrTalk(
        0xC,
        (
            "#01904FEven enduring the anxiety\x01",
            "is akin to fighting together\x01",
            "with all of you...\x02\x03",
            "#01902FIn that case, there's\x01",
            "only one thing I can do.\x02\x03",
            "#01909FI, Fran Seeker... will\x01",
            "pray here for the safety of\x01",
            "my big sis and everyone!\x02\x03",
            "Please absolutely, absolutely\x01",
            "return safely, ok!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E89C")

    label("loc_E812")


    ChrTalk(
        0xC,
        (
            "#01909FI, Fran Seeker... Will pray\x01",
            "here for the safety of my\x01",
            "big sis and everyone!\x02\x03",
            "Please absolutely, absolutely\x01",
            "return safely, ok!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E89C")

    Jump("loc_FE73")

    label("loc_E8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_EAA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9FD")

    ChrTalk(
        0xC,
        (
            "#01900FTo think that the interior\x01",
            "of the "huge tree" is so\x01",
            "prettier than I expecteeed...\x02\x03",
            "#01904FIf it wasn't a time like\x01",
            "this, I feel like I could\x01",
            "enjoy the scenery foreveeer.\x02\x03",
            "#01905F...No, I mustn't. I mustn't\x01",
            "let down my guard, right?\x02\x03",
            "#01909FAnyway, do your best everyone! \x01",
            "I'll be rooting for you from heeere!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_EAA3")

    label("loc_E9FD")


    ChrTalk(
        0xC,
        (
            "#01906FThe interior of this "huge tree" is\x01",
            "pretty, but I mustn't let down my guard.\x02\x03",
            "#01909FAnyway, do your best everyone! \x01",
            "I'll be rooting for you from heeere!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAA3")

    Jump("loc_FE73")

    label("loc_EAA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EC1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB90")

    ChrTalk(
        0xC,
        (
            "#01905FIt was a little scary breaking\x01",
            "into that "huge tree", but...\x02\x03",
            "#01901F...I'm a police officer too.\x01",
            "It's in times like these that\x01",
            "I have to show my courage!\x02\x03",
            "#01909FMr. Lloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_EC18")

    label("loc_EB90")


    ChrTalk(
        0xC,
        (
            "#01901F...I'm a police officer too.\x01",
            "It's in times like these that\x01",
            "I have to show my courage!\x02\x03",
            "#01909FMr. Lloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC18")

    Jump("loc_FE73")

    label("loc_EC1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_EE2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED6F")

    ChrTalk(
        0xC,
        (
            "#01900FIf we do something about the barrier\x01",
            "and the white "Aion", we'll be able\x01",
            "to start invading the city, right?\x02\x03",
            "#01904FThe "declaration of invalidity" likely\x01",
            "reached Chief Sergei and the others in\x01",
            "the city, so they might be on the move.\x02\x03",
            "#01909FAnyway, this is the final push! \x01",
            "Do your best, you guys!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_EE28")

    label("loc_ED6F")


    ChrTalk(
        0xC,
        (
            "#01900FIf we do something about the barrier\x01",
            "and the white "Aion", we'll be able\x01",
            "to start invading the city, right?\x02\x03",
            "#01909FAnyway, this is the final push! \x01",
            "Do your best, you guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE28")

    Jump("loc_FE73")

    label("loc_EE2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_F211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F128")

    ChrTalk(
        0xC,
        (
            "#01904F(*klak klak klak klak*...)\x02\x03",
            "Ah, Ah... Test, test...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FFran, what are you doing?\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EF37")
    Jump("loc_EF81")

    label("loc_EF37")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EF57")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF81")

    label("loc_EF57")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF77")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF81")

    label("loc_EF77")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF81")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#01902FOh, Mr. Lloyd. I was just\x01",
            "testing the microphone\x01",
            "and camera.\x02\x03",
            "We can send images and sounds from\x01",
            "the Merkabah's monitor system, through\x01",
            "the orbal net, to screens everywhere.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "#01904F"This is Fran Seeker.\x01",
            "I love my big sis so much!"\x02\x03",
            "#01909F...Yeah, the speech recognition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Ha ha, no matter the situation,\x01",
            "Fran can calm you down...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_F20C")

    label("loc_F128")


    ChrTalk(
        0xC,
        (
            "#01902FWe can send images and sounds from\x01",
            "the Merkabah's monitor system, through\x01",
            "the orbal net, to screens everywhere.\x02\x03",
            "#01909FI have to carefully check everything\x01",
            "so that Chairman MacDowell's voice\x01",
            "can reach the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F20C")

    Jump("loc_FE73")

    label("loc_F211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_F371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F22C")
    Call(1, 13)
    Jump("loc_F36C")

    label("loc_F22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F313")

    ChrTalk(
        0xC,
        (
            "#01912FUh uh, I'm so glad\x01",
            "big sis got back.\x02\x03",
            "#01901FMr. Lloyd...\x01",
            "Please, take good\x01",
            "care of big sis!\x02\x03",
            "#01909FI'm secretly rooting\x01",
            "for you too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(H-Hmm... I feel like there's\x01",
            "some misunderstanding.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_F36C")

    label("loc_F313")


    ChrTalk(
        0xC,
        (
            "#01901FPlease, take good\x01",
            "care of big sis!\x02\x03",
            "#01909FI'm secretly rooting\x01",
            "for you too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F36C")

    Jump("loc_FE73")

    label("loc_F371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_F4FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F495")

    ChrTalk(
        0xC,
        (
            "#01908FWest Crossbell Highway...\x01",
            "Bellguard Gate is there.\x02\x03",
            "#01903FBig sis is probably there too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#01906F*sigh*, I can't be doing this.\x01",
            "I have to pull myself together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Fran. As expected, \x01",
            "she's worried about Noｱl...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_F4F6")

    label("loc_F495")


    ChrTalk(
        0xC,
        (
            "#01908FBig sis is probably at Bellguard Gate...\x02\x03",
            "#01906F...I wonder what she's doing now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4F6")

    Jump("loc_FE73")

    label("loc_F4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_FC4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA65")

    ChrTalk(
        0xC,
        (
            "#01908F...Big sis has even \x01",
            "accepted to oppose us...\x01",
            "That's the path she chose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... To be honest, I think\x01",
            "hers is not a normal resolve.\x02\x03",
            "#00003FWhat made Noｱl made up\x01",
            "her mind to such an extent...\x02\x03",
            "#00008FI feel like the cause is just not\x01",
            "the current series of incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903F...Probably...\x02\x03",
            "#01901FI think it's got roots in\x01",
            "our father's passing away\x01",
            "when we were little.\x02\x03",
            "#01908F...He was "accidently shot" by a rifle\x01",
            "during a Republic military exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWhat...!?\x02\x03",
            "Your father died about\x01",
            "ten years ago due to\x01",
            "an "accident", right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FI was still small and don't\x01",
            "remember the details, but...\x02\x03",
            "#01908FDuring a Republic military exercise, there was an\x01",
            "accidental firing, and the shot happened to hit\x01",
            "my father on guard duty.. That's what they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...So that's what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903FBut Crossbell being in the position\x01",
            "it is in, naturally couldn't regard\x01",
            "the matter as serious...\x02\x03",
            "#01908FAnd in the end, it was seen and\x01",
            "dealt with as an "accident."\x02\x03",
            "My mother was sad, but seemed\x01",
            "to accept it from the start as\x01",
            "a risk of a dangerous job...\x02\x03",
            "#01903F...But probably, my big sister hasn't accepted it.\x01",
            "Not even now, after all this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...That may very well be true.\x02\x03",
            "#00003F(The reason for Noｱl's strong\x01",
            "desire to protect Crossbell... \x01",
            "I feel like I understand it now...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 7)
    Jump("loc_FC46")

    label("loc_FA65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBC7")

    ChrTalk(
        0xC,
        (
            "#01908F...Sorry. \x01",
            "Somehow I've gotten serious and all.\x02\x03",
            "#01903FFormer CGF members who objects\x01",
            "to the current State Guard...\x02\x03",
            "#01900FRight now, we must think of meeting\x01",
            "up with them as our top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... You're right.\x02\x03",
            "#00000FFran, I leave the backing up to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909FYes, sir! I'll do everything I caaan!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_FC46")

    label("loc_FBC7")


    ChrTalk(
        0xC,
        (
            "#01903FFormer CGF members who objects\x01",
            "to the current State Guard...\x02\x03",
            "#01900FIf they're not my big sis,\x01",
            "just who are they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC46")

    Jump("loc_FE73")

    label("loc_FC4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_FE73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC66")
    Call(1, 32)
    Jump("loc_FE73")

    label("loc_FC66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDAA")

    ChrTalk(
        0xC,
        (
            "#01900FWhile searching for "gaps",\x01",
            "we incidentally found reactions\x01",
            "from dangerous monsteeers.\x02\x03",
            "From now on, I will take the responsibility\x01",
            "and send information to the terminal as\x01",
            "official support requeeests.\x02\x03",
            "#01909FIf you defeat one of them,\x01",
            "don't forget to report using\x01",
            "the terminal in the cabiiin!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_FE73")

    label("loc_FDAA")


    ChrTalk(
        0xC,
        (
            "#01900FI am still inexperienced, but I\x01",
            "will do my very best to support\x01",
            "you onboard the Merkabah!\x02\x03",
            "#01909FEveryone, if you defeat a Wanted\x01",
            "Monster, please report using the\x01",
            "terminal in the cabiiin!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE73")

    TalkEnd(0xC)
    Return()

    # Function_31_E3D0 end

    def Function_32_FE77(): pass

    label("Function_32_FE77")


    ChrTalk(
        0xC,
        (
            "#01900FThe Merkabah is equipped with an information\x01",
            "terminal like the one at the Support Section...\x02\x03",
            "#01909FFrom now on, I'll take responsibility\x01",
            "for sending support request\x01",
            "information to that terminaaal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow, is that so. Indeed\x01",
            "there was a terminal in\x01",
            "the cabin...\x02\x03",
            "#00003FCome to think of it, where is\x01",
            "that information coming from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FI was interested in it too,\x01",
            "so I asked Mr. Abbas...\x02\x03",
            "#01904FIt seems that, while searching for "gaps",\x01",
            "you can also incidentally find reactions\x01",
            "from dangerous monsteeers.\x02\x03",
            "#01902FIt seems a Merkabah's function to discover at an\x01",
            "early stage things that could be dangerous when\x01",
            "doing operations and to deal with theeem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... Indeed, they'd be dangerous\x01",
            "if left alone, so we'll take care of\x01",
            "them if there's a spare moment.\x02\x03",
            "#00009FBut, reporting to you Fran... It's been\x01",
            "awhile, and it really takes me back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FUh uh, that's riiight!\x01",
            "Somehow, I'm deeply moved too.\x02\x03",
            "#01906FIt might take a bit of time to report\x01",
            "from the cabin terminal, but...\x02\x03",
            "#01900FPlease, do the same procedure you used\x01",
            "until now even to get a proper evaluation\x01",
            "when one day we'll go back to the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Yeah, that's right.\x02\x03",
            "#00000FThen, please take care of us as\x01",
            "our operator once again, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909FRoger thaaat!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_32_FE77 end

    def Function_33_10387(): pass

    label("Function_33_10387")


    ChrTalk(
        0xC,
        (
            "#01903FThis is really, really\x01",
            "the final climax...\x02\x03",
            "#01908FIn times like these, I know it's\x01",
            "pathetic to be only able to wait\x01",
            "in this safe place...\x02\x03",
            "#01906FI've also thought many times how nice\x01",
            "would be to fight alongside you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Nonsense. Fighting against enemies\x01",
            "isn't just about "fighting".\x02\x03",
            "#00000FIt's precisely because you and\x01",
            "everyone else are waiting for us\x01",
            "that we're able to do our best.\x02\x03",
            "No matter how hard it will be,\x01",
            "we'll absolutely return to where you're...\x01",
            "I believe that from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01900FMr. Lloyd...\x01",
            "...I understand.\x02\x03",
            "#01909FI, Fran Seeker... will\x01",
            "pray here for the safety of\x01",
            "my big sister and everyone!\x02\x03",
            "Please absolutely, absolutely\x01",
            "return safely, ok!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_33_10387 end

    def Function_34_10667(): pass

    label("Function_34_10667")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107BB")

    ChrTalk(
        0x9,
        (
            "#02305FOh yeah, guys...\x01",
            "You have a "Pom!"\x01",
            "account, right?\x02\x03",
            "#02304FHehe. Since I'm here, I think I'll gift\x01",
            "you with the great Jona's account.\x02\x03",
            "#02309FIf you think you can win against me,\x01",
            "who's been involved since the development\x01",
            "stage, just go ahead and try.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Jona's Account"\x07\x00",
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_11068")

    label("loc_107BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_10903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107D6")
    Call(1, 36)
    Jump("loc_108FE")

    label("loc_107D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088F")

    ChrTalk(
        0x9,
        (
            "#02306FTch, what.\x01",
            "I'm so worried\x01",
            "and yet, you...\x02\x03",
            "#02300FHmph, well...\x01",
            "At least do your best.\x02\x03",
            "#02309FGive me back my\x01",
            "leisurely orbal net\x01",
            "life that I had before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_108FE")

    label("loc_1088F")


    ChrTalk(
        0x9,
        (
            "#02300FWell... At least do your best.\x02\x03",
            "#02309FGive me back my\x01",
            "leisurely orbal net\x01",
            "life that I had before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108FE")

    Jump("loc_11068")

    label("loc_10903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_10B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A85")

    ChrTalk(
        0x9,
        (
            "#02301FThat feeling like an infinite amount\x01",
            "of light is being sucked into the tree...\x01",
            "It reminds me of the orbal net concept...\x02\x03",
            "#02303FCome to think of it, the Crois clan used\x01",
            "the orbal net in their plot too, didn't they.\x02\x03",
            "The form of that "huge tree" itself\x01",
            "was related to their "project".\x02\x03",
            "#02302F...Well, I'll leave any\x01",
            "further analysis to you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10B18")

    label("loc_10A85")


    ChrTalk(
        0x9,
        (
            "#02303FThe form of that "huge tree" itself\x01",
            "might be related to their "project".\x02\x03",
            "#02302F...Well, I'll leave any\x01",
            "further analysis to you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B18")

    Jump("loc_11068")

    label("loc_10B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C0C")

    ChrTalk(
        0x9,
        (
            "#02303FIt would've been better if I\x01",
            "returned to my Geofront base, but...\x02\x03",
            "#02302FRight now, this place is more\x01",
            "interesting. Since I'm here, I'll\x01",
            "stick with you guys until the end.\x02\x03",
            "#02304FHehe, be grateful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10C96")

    label("loc_10C0C")


    ChrTalk(
        0x9,
        (
            "#02302FRight now, this place is more\x01",
            "interesting. Since I'm here, I'll\x01",
            "stick with you guys until the end.\x02\x03",
            "#02304FHehe, be grateful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C96")

    Jump("loc_11068")

    label("loc_10C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E0A")

    ChrTalk(
        0x9,
        (
            "#02302FThe orbal net hacking went\x01",
            "better than I expected.\x02\x03",
            "#02306FIt's just, the signal booster\x01",
            "circuit was completely cut off,\x01",
            "so we can't do it again.\x02\x03",
            "#02309F...Hehe. Well, whatever. Right now,\x01",
            "we've just gotta scare the hell out\x01",
            "of those guys at Orchis Tower.\x02\x03",
            "#02302FLater we've got to\x01",
            "liberate Crossbell City\x01",
            "and retake my base!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10EA6")

    label("loc_10E0A")


    ChrTalk(
        0x9,
        (
            "#02300FIt looks like there's a strong\x01",
            "opponent, but I'm counting on you.\x02\x03",
            "#02309FWe've got to hurry and liberate\x01",
            "Crossbell City and take back my base!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EA6")

    Jump("loc_11068")

    label("loc_10EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_11068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EC6")
    Call(1, 35)
    Jump("loc_11068")

    label("loc_10EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC6")

    ChrTalk(
        0x9,
        (
            "#02306FAnyway, I've got to get back at\x01",
            "those guys for locking me up in\x01",
            "a place where there's no terminal.\x02\x03",
            "#02310FEspecially that Mariabell woman!\x01",
            "I'll teach that witch a lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Looks like he bears quite the grudge...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_11068")

    label("loc_10FC6")


    ChrTalk(
        0x9,
        (
            "#02302FI'm ready to start the\x01",
            "hacking whenever you are!\x02\x03",
            "#02309FJust you watch! Terminals throughout Crossbell\x01",
            "will broadcast the declaration of invalidity!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11068")

    TalkEnd(0xFE)
    Return()

    # Function_34_10667 end

    def Function_35_1106C(): pass

    label("Function_35_1106C")


    ChrTalk(
        0x9,
        (
            "#02305FHey, are we starting the operation yet?\x02\x03",
            "I'm ready to start the\x01",
            "hacking whenever you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, someone's excited...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02304FHehe. It's finally time to get\x01",
            "back at those guys who locked me\x01",
            "in a place where there's no terminal.\x02\x03",
            "#02302FJust you watch! Terminals\x01",
            "throughout Crossbell will broadcast\x01",
            "that old Chairman's face and voice!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FChairman MacDowell, you mean.\x02\x03",
            "#00001FJona, even in times\x01",
            "like these, you have to\x01",
            "use proper politeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306FAh, enough already. \x01",
            "You're annoying as always.\x02\x03",
            "#02302FEnough already, just start\x01",
            "the operation now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_35_1106C end

    def Function_36_112DB(): pass

    label("Function_36_112DB")


    ChrTalk(
        0x9,
        (
            "#02300FLooks like we're getting\x01",
            "close to the end.\x02\x03",
            "#02303F...Umm, are you ok? It looks\x01",
            "like that Mariabell woman is\x01",
            "waiting for you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow, how strange... You're\x01",
            "actually worried about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305FO-Of course I am! \x01",
            "Who wouldn't worried in this\x01",
            "whacked-out situation!?\x02\x03",
            "#02306FTch, what.\x01",
            "I'm so worried and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, my bad.\x02\x03",
            "#00000F...Thanks, Jona. We'll\x01",
            "definitely return safely.\x02\x03",
            "I'm counting on you to make sure\x01",
            "we're ready to withdraw anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02303FHmph, I know that already.\x01",
            "At least do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_36_112DB end

    def Function_37_11505(): pass

    label("Function_37_11505")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_11516")
    Jump("loc_11A98")

    label("loc_11516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_11524")
    Jump("loc_11A98")

    label("loc_11524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11532")
    Jump("loc_11A98")

    label("loc_11532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_116E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1166F")

    ChrTalk(
        0xF,
        (
            "#02103FThe mysterious society of "Ouroboros"...\x01",
            "I heard they were behind the strange\x01",
            "phenomenon that occurred in Liberl.\x02\x03",
            "#02101FThough they haven't showed themselves\x01",
            "as much as last time, we've got to\x01",
            "protect the important points...\x02\x03",
            "#02106F...Just what could their goal possibly be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_116E2")

    label("loc_1166F")


    ChrTalk(
        0xF,
        (
            "#02103FThe "Ouroboros" society...\x02\x03",
            "#02101FTheir mysteries only get bigger.\x01",
            "Just what is their true objective?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116E2")

    Jump("loc_11A98")

    label("loc_116E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_118CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11804")

    ChrTalk(
        0xF,
        (
            "#02102FThe "declaration of invalidity"\x01",
            "plan is finally assembled.\x02\x03",
            "Now that Chairman MacDowell's\x01",
            "statement is ready, all that's\x01",
            "left is to put it into effect...\x02\x03",
            "#02106F...Ooh, I'm getting so excited! I wonder\x01",
            "if I should do voice training on the deck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_118CA")

    label("loc_11804")


    ChrTalk(
        0xF,
        (
            "#02102FNow that Chairman MacDowell's\x01",
            "statement is ready, all that's\x01",
            "left is to put it into effect...\x02\x03",
            "#02106F...Ooh, I'm getting so excited! I wonder\x01",
            "if I should do voice training on the deck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118CA")

    Jump("loc_11A98")

    label("loc_118CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_11A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118EA")
    Call(1, 38)
    Jump("loc_11A98")

    label("loc_118EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A39")

    ChrTalk(
        0xF,
        (
            "#02109FNow then, Wazy and Miss Rixia.\x01",
            "Let's continue our interview!\x02\x03",
            "I'm just an interested person! Of course\x01",
            "I won't write an article about this, so\x01",
            "don't hold back and tell me everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10706FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FOh boy, to think she loves\x01",
            "gossip this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Will they be all right...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_11A98")

    label("loc_11A39")


    ChrTalk(
        0xF,
        (
            "#02105F...Wow, is that so!?\x02\x03",
            "#02109FAh, I just love that kind\x01",
            "of behind-the-scenes stuff!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A98")

    TalkEnd(0xFE)
    Return()

    # Function_37_11505 end

    def Function_38_11A9C(): pass

    label("Function_38_11A9C")


    ChrTalk(
        0xF,
        (
            "#02104FTo be able to interview\x01",
            "this amazing lineup on\x01",
            "this amazing airship...\x02\x03",
            "#02109FAh, it just tickles\x01",
            "my journalist's soul!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FM-Miss Grace... You're not going to \x01",
            "write an article about all this, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02102FNot a chance! Don't worry! In the end,\x01",
            "this is just for personal interest.\x02\x03",
            "#02104FI've got to sort out the material\x01",
            "I got at the time of the Resistance too.\x01",
            "I won't write an article about it, rest assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FR-Right...\x02\x03",
            "#00005F...By the way, what details did\x01",
            "you get from the Resistance?\x02\x03",
            "#00003FI think it was something about a problem\x01",
            "that's occurring in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106FHmm. I guess. It's a bit\x01",
            "of a long story, but...\x02\x03",
            "#02101FActually, ever since the day the\x01",
            "independence was declared, our articles\x01",
            "have been subject to censorship.\x02\x03",
            "We haven't been able to publish\x01",
            "any opposition faction articles\x01",
            "critical of the President at all...\x02\x03",
            "#02106FOn top of that, our use of\x01",
            "communications equipment and coverage\x01",
            "conduct themselves are regulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FHe's nothing if not thorough...\x02\x03",
            "#00003F...Well, it's President Dieter after all.\x01",
            "He could be capable of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FWell, that kind of stuff is very\x01",
            "far from my idea of journalism,\x01",
            "so I can't go along with it.\x02\x03",
            "#02102FI ignored the notices and continued my coverage,\x01",
            "when finally the State Guard caught wind of it.\x02\x03",
            "#02104FCrossbell City was getting a tough place\x01",
            "to be, so I went over to the Resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSo that's how it went down... \x01",
            "You did well to stay safe this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109FThat's because Reins arranged an\x01",
            "escape route for me. I'm glad I\x01",
            "have such a skilled junior.\x02\x03",
            "#02100F...Anyway, because of the situation,\x01",
            "I'll cooperate with the liberation\x01",
            "of Crossbell City in my own way!\x02\x03",
            "#02109FThe say "The pen is mightier than the sword," and\x01",
            "I won't lose to the likes of the State Guard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha... Maybe there will be something\x01",
            "you can help us with. I'll be counting\x01",
            "on you when the time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 7)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_38_11A9C end

    def Function_39_1224E(): pass

    label("Function_39_1224E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_124CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1226C")
    Call(1, 41)
    Jump("loc_124C5")

    label("loc_1226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C0")

    ChrTalk(
        0x12,
        (
            "#02503FI can't do anything more\x01",
            "to be useful to you all.\x02\x03",
            "#02500FAt least, as the one who gave the declaration of\x01",
            "invalidity, I shall continue to think of how to\x01",
            "deal with its influence on Crossbell's future.\x02\x03",
            "As Chairman of the autonomous state congress...\x01",
            "And above all, as one of the\x01",
            "citizens living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_124C5")

    label("loc_123C0")


    ChrTalk(
        0x12,
        (
            "#02503FAs the one who gave the declaration of invalidity;\x01",
            "I shall continue to think of how to deal with\x01",
            "its influence on Crossbell's future.\x02\x03",
            "#02500FAs Chairman of the autonomous state congress...\x01",
            "And above all, as one of the\x01",
            "citizens living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124C5")

    Jump("loc_1277C")

    label("loc_124CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1277C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124E5")
    Call(1, 40)
    Jump("loc_1277C")

    label("loc_124E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1269D")

    ChrTalk(
        0x12,
        (
            "#02500FI am ready to give the\x01",
            ""independent state declaration\x01",
            "of invalidity" anytime.\x02\x03",
            "#02503FAll that's left is how the declaration will\x01",
            "go over with the people of Crossbell... \x01",
            "Everything depends on it.\x02\x03",
            "#02500FI cannot give a performance as great\x01",
            "as Dieter's, but I shall endeavor to\x01",
            "convey my own sincerity.\x02\x03",
            "I must do this, to get each and\x01",
            "every person living in Crossbell to\x01",
            "think about the future of this land.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_1277C")

    label("loc_1269D")


    ChrTalk(
        0x12,
        (
            "#02503FThe "independent state declaration of invalidity"...\x01",
            "I shall endeavor to convey my own sincerity.\x02\x03",
            "#02500FI must do this, to get each and\x01",
            "every person living in Crossbell to\x01",
            "think about the future of this land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1277C")

    TalkEnd(0xFE)
    Return()

    # Function_39_1224E end

    def Function_40_12780(): pass

    label("Function_40_12780")


    ChrTalk(
        0x101,
        (
            "#00000FChairman MacDowell...\x01",
            "Are you ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02500FYes. I can deliver the\x01",
            ""independent state declaration\x01",
            "of invalidity" anytime.\x02\x03",
            "The declaration itself leaves\x01",
            "nothing to be desired.\x02\x03",
            "#02503FOf course, it itself is a\x01",
            "reflection of Dieter's words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503FNo... Thanks are unnecessary.\x02\x03",
            "#02501FAll that's left is how the declaration\x01",
            "will go over with the people of Crossbell... \x01",
            "Everything depends on it.\x02\x03",
            "I cannot give a performance as great\x01",
            "as Dieter's, but I shall endeavor to\x01",
            "convey my own sincerity.\x02\x03",
            "#02503FI must do this, to get each and\x01",
            "every person living in Crossbell to\x01",
            "think about the future of this land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight... I'm counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 1)
    Return()

    # Function_40_12780 end

    def Function_41_12A49(): pass

    label("Function_41_12A49")


    ChrTalk(
        0x12,
        "#02503F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FChairman MacDowell...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x101, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12B2B")
    Jump("loc_12B75")

    label("loc_12B2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12B4B")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12B75")

    label("loc_12B4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12B6B")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12B75")

    label("loc_12B6B")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12B75")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(
        0x12,
        (
            "#02505F...Oh, sorry.\x01",
            "I was just thinking.\x02\x03",
            "#02503FThe independent state of Crossbell declaration\x01",
            "of invalidity... Although it will break the current\x01",
            "stalemate, is it really the right thing to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F...Most likely, this problem\x01",
            "does not have a "right" answer.\x02\x03",
            "#02500FBut, I feel the act of seeking the right\x01",
            "answer is important, in and of itself.\x02\x03",
            "As Chair of the autonomous state congress...\x01",
            "And above all, as one of the\x01",
            "citizens living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Thank you very much.\x02\x03",
            "#00000FWhen the incident is over,\x01",
            "we'll be helping you too,\x01",
            "Mr. Chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02509FHu hu, and I thank you for it. I'll be\x01",
            "counting on you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1DA, 2)
    Return()

    # Function_41_12A49 end

    def Function_42_12E5B(): pass

    label("Function_42_12E5B")

    Call(1, 43)
    Return()

    # Function_42_12E5B end

    def Function_43_12E5F(): pass

    label("Function_43_12E5F")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14265")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Buy Equipment\x01",      # 1
            "Buy Items\x01",          # 2
            "Quit\x01",               # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12ECF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_12ECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12EEE")
    OP_AF(0xD8)
    Jump("loc_12F40")

    label("loc_12EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_12EFE")
    OP_AF(0xD7)
    Jump("loc_12F40")

    label("loc_12EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12F0E")
    OP_AF(0xD6)
    Jump("loc_12F40")

    label("loc_12F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_12F1E")
    OP_AF(0xD5)
    Jump("loc_12F40")

    label("loc_12F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_12F2E")
    OP_AF(0xD4)
    Jump("loc_12F40")

    label("loc_12F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_12F3E")
    OP_AF(0xD3)
    Jump("loc_12F40")

    label("loc_12F3E")

    OP_AF(0xD2)

    label("loc_12F40")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14260")

    label("loc_12F4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F6F")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14260")

    label("loc_12F6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F83")
    Jump("loc_14260")

    label("loc_12F83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14260")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_131FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13142")

    ChrTalk(
        0x15,
        (
            "The time has come for the battle that will dispute\x01",
            "the fate of Crossbell to reach its conclusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what would have happened if Church\x01",
            "personnel weren't already gathered here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We've managed to reach this point somehow. \x01",
            "Since it's you all, I'm sure everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Come now. Be sure everything is in order\x01",
            "before heading for the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_131F8")

    label("loc_13142")


    ChrTalk(
        0x15,
        (
            "We've managed to reach this point. Since it's\x01",
            "you all, I'm sure everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Come now. Be sure everything is in order\x01",
            "before heading for the final battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131F8")

    Jump("loc_14260")

    label("loc_131FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_133C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1330E")

    ChrTalk(
        0x15,
        (
            "It looks like the "huge tree" path\x01",
            "continues quite deeply inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If things get dangerous, it'll be important\x01",
            "to return periodically and resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of this incident depends\x01",
            "on you. Proceed as carefully as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_133BB")

    label("loc_1330E")


    ChrTalk(
        0x15,
        (
            "If things get dangerous, it'll be important\x01",
            "to return periodically and resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of this incident depends\x01",
            "on you. Proceed as carefully as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133BB")

    Jump("loc_14260")

    label("loc_133C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_135E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13522")

    ChrTalk(
        0x15,
        (
            "Before going to the "huge tree" you'd\x01",
            "want to finish all your preparations, but\x01",
            "there's a limit to all the stuff we can have here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "For now, you'd probably want to\x01",
            "visit places, facilities and friends\x01",
            "throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what's going to happen... But\x01",
            "you've got to make sure you've got no regrets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_135E1")

    label("loc_13522")


    ChrTalk(
        0x15,
        (
            "For now, you'd probably want to\x01",
            "visit places, facilities and friends\x01",
            "throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what's going to happen... But\x01",
            "you've got to make sure you've got no regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135E1")

    Jump("loc_14260")

    label("loc_135E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_137B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13708")

    ChrTalk(
        0x15,
        (
            "Jｶrg Rosenberg... To think a\x01",
            "man of the "Society" would\x01",
            "give us valuable information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "As a Knight, it's a problem if \x01",
            "I just believe him, but the\x01",
            "information does not seem like lies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm sure there's different kinds\x01",
            "of people within the Society...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_137AE")

    label("loc_13708")


    ChrTalk(
        0x15,
        (
            "Jｶrg Rosenberg... I can't simply\x01",
            "believe him, but the information\x01",
            "does not seem like lies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm sure there's different kinds\x01",
            "of people within the Society...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137AE")

    Jump("loc_14260")

    label("loc_137B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_13996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138E0")

    ChrTalk(
        0x15,
        (
            "Once Chairman MacDowell gives the independent\x01",
            "state declaration of invalidity, its effect will\x01",
            "appear throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think it will become easier for the Resistance\x01",
            "forces hiding throughout Crossbell to act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "...I feel a turning point is drawing near.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13991")

    label("loc_138E0")


    ChrTalk(
        0x15,
        (
            "Once Chairman MacDowell gives the independent\x01",
            "state declaration of invalidity, its effect will\x01",
            "appear throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "...I feel a turning point is drawing near.\x02",
    )

    CloseMessageWindow()

    label("loc_13991")

    Jump("loc_14260")

    label("loc_13996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_13BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE2")

    ChrTalk(
        0x15,
        (
            "The mission to save Chairman\x01",
            "MacDowell... It's not like I'm on the\x01",
            "raid team, but even so, I'm nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Your opponents are a company from the "Red\x01",
            "Constellation"... A fight that can't be compared to\x01",
            "any you've faced before is waiting for you down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please everyone. \x01",
            "Come back safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13BA6")

    label("loc_13AE2")


    ChrTalk(
        0x15,
        (
            "Your opponents are a company from the "Red\x01",
            "Constellation"... A fight that can't be compared to\x01",
            "any you've faced before is waiting for you down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please everyone. \x01",
            "Come back safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BA6")

    Jump("loc_14260")

    label("loc_13BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_13D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C96")

    ChrTalk(
        0x15,
        (
            "It sure is lively\x01",
            "onboard the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Normally it's just the staff of\x01",
            "our order. Even commoners\x01",
            "coming aboard is rare...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just keep this between you and me,\x01",
            "but I don't think this is too bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13D22")

    label("loc_13C96")


    ChrTalk(
        0x15,
        (
            "Commoners hardly ever\x01",
            "even come aboard the\x01",
            "Merkabah, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just keep this between you and me,\x01",
            "but I don't think this is too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D22")

    Jump("loc_14260")

    label("loc_13D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_13EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E3A")

    ChrTalk(
        0x15,
        (
            ""Yin", the legendary assassin...\x01",
            "Even I've heard the rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But to think she's that girl...\x01",
            "The world is full of surprises, eh?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...Well, I think it must have been\x01",
            "quite a shock too when you learned\x01",
            "Lord Hemisphere was a clergyman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13EAA")

    label("loc_13E3A")


    ChrTalk(
        0x15,
        (
            ""Yin", the legendary assassin...\x01",
            "To think she's that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Ha ha, the world is full of surprises, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_13EAA")

    Jump("loc_14260")

    label("loc_13EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1407B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F78")

    ChrTalk(
        0x15,
        (
            "So you've reunited with your friends...?\x01",
            "It seems you had a great start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Still, there's nothing like getting\x01",
            "well prepared in advance.\x01",
            "Stay safe in the future too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_14076")

    label("loc_13F78")


    ChrTalk(
        0x15,
        (
            "Thanks to Lord Hemisphere's Thaumaturgy,\x01",
            "we'll be able to visit the hospital for awhile\x01",
            "without bumping into the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "However, just because the beginning was\x01",
            "good, it doesn't mean you can let down\x01",
            "your guard. Be careful as you proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14076")

    Jump("loc_14260")

    label("loc_1407B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_14260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14096")
    Call(1, 44)
    Jump("loc_14260")

    label("loc_14096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141C0")

    ChrTalk(
        0x15,
        (
            "Anyhow, we have plenty of\x01",
            "equipment and accessories, so\x01",
            "let me know in case you need them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...*sigh*, but even so, Lord Hemisphere...\x01",
            "We kept being wrapped around\x01",
            "his finger since in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away,\x01",
            "I think Mr. Abbas was\x01",
            "really good to stay with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_14260")

    label("loc_141C0")


    ChrTalk(
        0x15,
        (
            "We have kept being wrapped around\x01",
            "Lord Hemisphere's finger since in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away,\x01",
            "I think Mr. Abbas was\x01",
            "really good to stay with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14260")

    Jump("loc_12E6C")

    label("loc_14265")

    TalkEnd(0x15)
    Return()

    # Function_43_12E5F end

    def Function_44_14269(): pass

    label("Function_44_14269")


    ChrTalk(
        0x15,
        (
            "I'm Squire Ventos. \x01",
            "I handle management of\x01",
            "the shipboard facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have plenty of equipment and\x01",
            "accessories, so let me know when\x01",
            "you need them before the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FManage, you said...\x01",
            "You're short staffed,\x01",
            "so it must be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, Lord Hemisphere suddenly\x01",
            "restarted operations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We could only get a minimum\x01",
            "number of personnel onboard.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x15, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14477")
    Jump("loc_144C1")

    label("loc_14477")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14497")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_144C1")

    label("loc_14497")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_144B7")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_144C1")

    label("loc_144B7")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_144C1")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(
        0xA,
        (
            "#10404FHu hu. Anyway, it's\x01",
            "an urgent situation.\x02\x03",
            "#10409FAlthough it's been two years, I'm glad\x01",
            "to be working with you again, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "...*sigh*, anyway, I've got to do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm, looks like he's having\x01",
            "a hard time in many ways...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x1DA, 3)
    Return()

    # Function_44_14269 end

    def Function_45_145EC(): pass

    label("Function_45_145EC")

    Call(1, 46)
    Return()

    # Function_45_145EC end

    def Function_46_145F0(): pass

    label("Function_46_145F0")

    TalkBegin(0x16)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15751")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Quit\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1465A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1465A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1467A")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1574C")

    label("loc_1467A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1468E")
    Jump("loc_1574C")

    label("loc_1468E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1574C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_14843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1479E")

    ChrTalk(
        0x16,
        (
            "Now that you've come this far,\x01",
            "I can say nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The enemy standing in your way is\x01",
            "strong, but I am sure the Goddess\x01",
            "of the Sky will guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, be careful. May the\x01",
            "Goddess protect you all...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1483E")

    label("loc_1479E")


    ChrTalk(
        0x16,
        (
            "The enemy standing in your way is\x01",
            "strong, but I am sure the Goddess\x01",
            "of the Sky will guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, be careful. May the\x01",
            "Goddess protect you all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1483E")

    Jump("loc_1574C")

    label("loc_14843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_14A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14989")

    ChrTalk(
        0x16,
        (
            "The "Sept-Terrion of Zero"... \x01",
            "To think it brought forth such a dimension...\x01",
            "That's truly an act of the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...We've come together this\x01",
            "far, but the fate of this\x01",
            "ship is in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can't do much for you, but please\x01",
            "speak with me whenever you\x01",
            "need to prepare your orbments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14A3B")

    label("loc_14989")


    ChrTalk(
        0x16,
        (
            "We've come together this\x01",
            "far, but the fate of this\x01",
            "ship is in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can't do much for you, but please\x01",
            "speak with me whenever you\x01",
            "need to prepare your orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A3B")

    Jump("loc_1574C")

    label("loc_14A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B26")

    ChrTalk(
        0x16,
        (
            "...I feel the tension onboard this airship\x01",
            "is even greater than it was before the\x01",
            "Crossbell City liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We've finally reached the final stage...\x01",
            "May the Goddess protect you all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14B75")

    label("loc_14B26")


    ChrTalk(
        0x16,
        (
            "We've finally reached the final stage...\x01",
            "May the Goddess protect you all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B75")

    Jump("loc_1574C")

    label("loc_14B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE6")

    ChrTalk(
        0x16,
        (
            "At present, after the declaration of invalidity, \x01",
            "the Merkabah No. 5 staying outside of\x01",
            "Crossbell contacted us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Lord Graham and the others too are making\x01",
            "various preparations to assist us with the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To receive their assistance, we\x01",
            "need to do something about the\x01",
            "white "Aion" and the "barrier".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14DC2")

    label("loc_14CE6")


    ChrTalk(
        0x16,
        (
            "Lord Graham and the others too are making\x01",
            "various preparations to assist us with the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To receive their assistance, we\x01",
            "need to do something about the\x01",
            "white "Aion" and the "barrier".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DC2")

    Jump("loc_1574C")

    label("loc_14DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_14FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EFE")

    ChrTalk(
        0x16,
        (
            "When it's time to begin the hacking,\x01",
            "I'll be assisting as well from that \x01",
            "terminal over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The orbal net is outside my expertise,\x01",
            "but I can at least assist with the \x01",
            "Merkabah's system features...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For our order's mission as well,\x01",
            "I will give this everything I have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14FB6")

    label("loc_14EFE")


    ChrTalk(
        0x16,
        (
            "The orbal net is outside my expertise,\x01",
            "but I can at least assist with the \x01",
            "Merkabah's system features...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For our order's mission as well,\x01",
            "I will give this everything I have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FB6")

    Jump("loc_1574C")

    label("loc_14FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_15130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15085")

    ChrTalk(
        0x16,
        (
            "It looks like State Guard forces\x01",
            "aren't at Michelam, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even with just jaegers,\x01",
            "it's sure to be dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, make sure your\x01",
            "orbments are fully ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1512B")

    label("loc_15085")


    ChrTalk(
        0x16,
        (
            "It looks like State Guard forces\x01",
            "aren't at Michelam, but it's sure to\x01",
            "be dangerous even with just jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, make sure your\x01",
            "orbments are fully ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1512B")

    Jump("loc_1574C")

    label("loc_15130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_15326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1527C")

    ChrTalk(
        0x16,
        (
            "That "Berserker" rifle Mr.\x01",
            "Randy has... It seems it hides\x01",
            "considerable firepower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If the "Red Constellation", one of the strongest\x01",
            "jaeger corps on the continent, has showed up\x01",
            "as our opponents, things will be pretty difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Just one look at that weapon,\x01",
            "and I understood that somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_15321")

    label("loc_1527C")


    ChrTalk(
        0x16,
        (
            "That "Berserker" rifle Mr.\x01",
            "Randy has... It seems it hides\x01",
            "considerable firepower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I realized that the "Red Constellation"\x01",
            "has showed up as our opponents.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15321")

    Jump("loc_1574C")

    label("loc_15326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1551B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1547E")

    ChrTalk(
        0x16,
        (
            "You need a lot of faith to put up\x01",
            "resistance against a large organization\x01",
            "like the "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "They can't even resupply properly\x01",
            "and they acted like they have\x01",
            "somehow betrayed their comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I don't know who their leader is,\x01",
            "but it's certain someone with its\x01",
            "own beliefs and with a backbone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_15516")

    label("loc_1547E")


    ChrTalk(
        0x16,
        (
            "To resist them, you\x01",
            "need a lot of faith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I don't know who their leader is,\x01",
            "but it's certain someone with its\x01",
            "own beliefs and with a backbone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15516")

    Jump("loc_1574C")

    label("loc_1551B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_156B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15647")

    ChrTalk(
        0x16,
        (
            "Please don't enter\x01",
            "that engine room no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "There's an important thing that can't\x01",
            "be shown to commoners in there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_END)), "loc_1561C")

    ChrTalk(
        0x101,
        (
            "#00005F(Could it be the\x01",
            ""Heaven's Wheel" artifact\x01",
            "Abbas mentioned earlier...?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1563F")

    label("loc_1561C")


    ChrTalk(
        0x101,
        "#00005F(What could it be...?)\x02",
    )

    CloseMessageWindow()

    label("loc_1563F")

    SetScenarioFlags(0x2, 2)
    Jump("loc_156B2")

    label("loc_15647")


    ChrTalk(
        0x16,
        (
            "I've got to perform\x01",
            "maintenance in the\x01",
            "engine room pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "...Please don't peek inside, ok?\x02",
    )

    CloseMessageWindow()

    label("loc_156B2")

    Jump("loc_1574C")

    label("loc_156B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1574C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156D2")
    Call(1, 47)
    Jump("loc_1574C")

    label("loc_156D2")


    ChrTalk(
        0x16,
        (
            "...Now that the Society has\x01",
            "showed themselves, our order\x01",
            "cannot let this incident pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_1574C")

    Jump("loc_145FD")

    label("loc_15751")

    TalkEnd(0x16)
    Return()

    # Function_46_145F0 end

    def Function_47_15755(): pass

    label("Function_47_15755")


    ChrTalk(
        0x16,
        (
            "You're from the Crossbell Police's\x01",
            "Special Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I'm Juno, in\x01",
            "charge of the\x01",
            "engine room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Just leave your Quartz\x01",
            "synthesis and tactical\x01",
            "orbments modifications to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow... A squire\x01",
            "can even do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Uh uh. I have confidence in\x01",
            "myself when it comes to\x01",
            "tasks requiring dexterity.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x16,
        (
            "...Now that the Society has\x01",
            "showed themselves, our order\x01",
            "cannot let this incident pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight... I'm counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 4)
    Return()

    # Function_47_15755 end

    def Function_48_1595D(): pass

    label("Function_48_1595D")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KNap Room \x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",      # 0
            "Quit\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA7")
    EventBegin(0x2)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    OP_0D()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_15A12():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A12)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFF, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    OP_70(0x3, 0x0)
    OP_68(1300, 1000, -92030, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 270)
    SetChrSubChip(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x3)

    label("loc_15AA7")

    TalkEnd(0xFF)
    Return()

    # Function_48_1595D end

    def Function_49_15AAB(): pass

    label("Function_49_15AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AC1")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_15AC1")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15ADA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1609D")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_15B13"),
        (1, "loc_15B42"),
        (2, "loc_16081"),
        (3, "loc_16089"),
        (SWITCH_DEFAULT, "loc_16098"),
    )


    label("loc_15B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15B32")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_15B3D")

    label("loc_15B32")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_15B3D")

    Jump("loc_16098")

    label("loc_15B42")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C33")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        "This is Crossbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_15C0B")

    AnonymousTalk(
        0xFF,
        "I will receive your report.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing, complete.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C2E")

    label("loc_15C0B")


    AnonymousTalk(
        0xFF,
        "There no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_15C2E")

    Jump("loc_16073")

    label("loc_15C33")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15C8A")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, this is Crossbell Poliiice!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CBF")

    label("loc_15C8A")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you for your hard wooork.\x02",
    )

    CloseMessageWindow()

    label("loc_15CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_15F5D")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Then, I'll receive your report, okaaay?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15ED0")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_15D40"),
        (13, "loc_15D8E"),
        (12, "loc_15DD9"),
        (SWITCH_DEFAULT, "loc_15E1D"),
    )


    label("loc_15D40")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 1st...\x01",
            "That's too amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E1D")

    label("loc_15D8E")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 2nd──\x01",
            "That's amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E1D")

    label("loc_15DD9")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 3rd──\x01",
            "You did, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E1D")

    label("loc_15E1D")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send you\x01",
            "the special article you gaaained!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard wooork!\x01",
            "I hope to be working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F55")

    label("loc_15ED0")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "The report is oveeer.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me again the\x01",
            "next time you complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F55")

    SetScenarioFlags(0x2, 4)
    Jump("loc_16073")

    label("loc_15F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_15FEA")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...\x01",
            "Haven't you just made a report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please do it again when you complete a request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16073")

    label("loc_15FEA")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...it seems you don't have\x01",
            "any request you can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please, let's work together agaaain.\x02",
    )

    CloseMessageWindow()

    label("loc_16073")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_16098")

    label("loc_16081")

    Call(1, 50)
    Jump("loc_16098")

    label("loc_16089")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16098")

    label("loc_16098")

    Jump("loc_15ADA")

    label("loc_1609D")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160DA")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(1, 51)
    Return()

    label("loc_160DA")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_49_15AAB end

    def Function_50_160EA(): pass

    label("Function_50_160EA")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_1610C")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1610C")
    ClearScenarioFlags(0x2A, 0)

    label("loc_1610C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_16129")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16129")
    ClearScenarioFlags(0x2A, 1)

    label("loc_16129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_16146")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16146")
    ClearScenarioFlags(0x2A, 2)

    label("loc_16146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_16163")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16163")
    ClearScenarioFlags(0x2A, 3)

    label("loc_16163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_16180")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16180")
    ClearScenarioFlags(0x2A, 4)

    label("loc_16180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_1619D")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1619D")
    ClearScenarioFlags(0x2A, 5)

    label("loc_1619D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_161A9")
    SetScenarioFlags(0x2A, 6)

    label("loc_161A9")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161EE")
    Sound(498, 1, 50, 0)
    Jump("loc_161F4")

    label("loc_161EE")

    Sound(498, 1, 100, 0)

    label("loc_161F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16224")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16224")

    Return()

    # Function_50_160EA end

    def Function_51_16225(): pass

    label("Function_51_16225")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_1628E")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_1628E")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00205FOh...\x02\x03",
            "#00204FIt looks like you've\x01",
            "won against all "Pom!"\x01",
            "opponents, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWow, reallyyy!?\x02\x03",
            "#01909FThat's Mr. Lloyd for you...\x01",
            "He's too amaziiing!!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_163FB")

    ChrTalk(
        0x9,
        (
            "#02302FHeh, that's right.\x01",
            "You're pretty good too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163FB")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks. \x01",
            "I just got lucky, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo. In puzzle games like that, luck isn't the\x01",
            "primary factor that determines the winner.\x02\x03",
            "#12102FBannings, you are a\x01",
            "true "Pom! Master".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F...T-Thank you for that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166E6")

    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "If you like, please take this.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xF0, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100FIt's a prohibited Master Quartz, jointly\x01",
            "developed by the Church and Epstein\x01",
            "Foundation using ancient techniques.\x02\x03",
            "Being it too powerful and difficult to handle\x01",
            "it's something we hesitated to use, but...\x02\x03",
            "#12102FYou should be able to use it in the right way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, understood. \x01",
            "I'll put it to use, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167C0")

    label("loc_166E6")


    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "#12102FI'll give you this as a prize.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, thanks.\x01",
            "I'll put it to good use.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_167C0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_16225 end

    def Function_52_167F2(): pass

    label("Function_52_167F2")

    EventBegin(0x0)
    Fade(500)
    OP_68(4130, -1100, 7060, 0)
    MoveCamera(47, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14590, 0)
    SetChrPos(0x101, 4000, -1500, 5730, 315)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_168C9")
    Jump("loc_16913")

    label("loc_168C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_168E9")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16913")

    label("loc_168E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16909")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16913")

    label("loc_16909")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16913")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01905FMr. Lloyd... \x01",
            "You look tired somehow.\x02\x03",
            "Are you all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FYeah... In a manner of speaking.\x02\x03",
            "#00003FBecause many things have happened,\x01",
            "fatigue might be showing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FUmm, please don't push\x01",
            "yourself too hard, oook?\x02\x03",
            "#01908FWhen I think what would happen\x01",
            "if you or my big sis collapsed...\x01",
            "I get really scared, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, thanks.\x01",
            "I'll be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01901FJust being careful isn't enough! You've got\x01",
            "to get proper rest in times like these!\x02\x03",
            "#01902FIf you like, shall I\x01",
            "give you a massage?\x02\x03",
            "#01909FIf I violently press the pressure points affecting\x01",
            "fatigue, you'll get better in a bam, you knooow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F(T-That sounds incredibly painful, somehow...)\x02\x03",
            "#00002FU-Umm... I'm good. I\x01",
            "appreciate the thought.\x02\x03",
            "#00009FI feel refreshed just talking\x01",
            "to you somehow, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01905FHuh? ...R-Reallyyy?\x02\x03",
            "#01909FEhehe... I'm happy to\x01",
            "hear you say thaaat.\x02\x03",
            "#01904FAs an operator, it's my\x01",
            "duty to cheer up all\x01",
            "of you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FHa ha. I think this\x01",
            "might be your calling.\x02\x03",
            "#00004FAnd you don't even know how many times your smile\x01",
            "has healed us through the terminal screen...\x02\x03",
            "#00000FI think that among the people who come and go at\x01",
            "police HQ, a great many comes just to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FOoh. If you say that much,\x01",
            "I'll get all embarrassed...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#6P#01904FBut you're right. I want\x01",
            "you to do your best from\x01",
            "here on out, ok Mr. Lloyd?\x02\x03",
            "#01902FIf you like,\x01",
            "please take this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#11P#00005FYou're giving this...to me?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_17113")

    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, please\x01",
            "take it.\x02\x03",
            "#01904FI mean, you might be\x01",
            "my brother-in-law in\x01",
            "the future...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00011FWh...Whaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01909FMwhuhuhu... If you need\x01",
            "info on my big sis,\x01",
            "I know everythiiing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00012F(H-Ha ha...I give up. I'm sure\x01",
            "she saw through the whole thing...)\x02\x03",
            "#00000F...Umm, then I'll\x01",
            "put it to good use.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171BE")

    label("loc_17113")


    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, please\x01",
            "take it.\x02\x03",
            "I made it while praying for\x01",
            "everyone's safety, so I'm\x01",
            "sure it will be effective!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FHa ha, then I'll put\x01",
            "it to good use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171BE")


    ChrTalk(
        0xC,
        "#6P#01909FEhehe, please treasure iiit.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D9, 4)
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17211")
    OP_E0(0x34, 0x0)

    label("loc_17211")

    EventEnd(0x5)
    Return()

    # Function_52_167F2 end

    def Function_53_17214(): pass

    label("Function_53_17214")

    EventBegin(0x0)
    Fade(500)
    OP_68(97920, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15320, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_172EB")
    Jump("loc_17335")

    label("loc_172EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1730B")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17335")

    label("loc_1730B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1732B")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17335")

    label("loc_1732B")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17335")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#5P#00603FHmm...\x02\x03",
            "#00600F...Bannings, it seems\x01",
            "you too have grown a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603FI've accompanied\x01",
            "you all this far, but...\x02\x03",
            "Your investigation and reasoning skills\x01",
            "are sound. I can say you've completely left\x01",
            "behind the immatureness you had before.\x02\x03",
            "You still haven't reached the level of Guy and\x01",
            "MacLaine when they were on active duty, but...\x02\x03",
            "#00602FHmph. It was worth looking\x01",
            "after you at Section One.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FU-Umm... \x01",
            "What's this all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P#00603FJust shut up and listen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FY-Yes sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00600F...I just name-dropped Guy and\x01",
            "MacLaine, but I won't tell you to\x01",
            "be a detective like they were.\x02\x03",
            "You have your own qualities.\x01",
            "By growing those, you'll be able to\x01",
            "get close to be an excellent detective.\x02\x03",
            "#00604FIn the future too, you'll have to devote yourself\x01",
            "even more to aim to be your own kind of detective.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x14,
        "#5P#00605F...What, you got a problem with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FN-No... \x01",
            "I'm just surprised.\x02\x03",
            "#00006FIt's not like you to have such a high\x01",
            "opinion of me, Mr. Dudley...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603FWhat will happen to the State Guard\x01",
            "depends on how things unfold, but\x01",
            "the police will continue to exist.\x02\x03",
            "#00600FWhen this chain of events\x01",
            "concludes, I'm sure at least\x01",
            "you'll return to the police.\x02\x03",
            "To prepare you for that, I just thought\x01",
            "I'd give you some advice as the\x01",
            "senior detective of Section One.\x02\x03",
            "#00603FThat's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see...\x02\x03",
            "#00004F...Thank you very much.\x02\x03",
            "#00002FI'll work hard to live up to your\x01",
            "expectations, Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00606FHmph, don't misunderstand.\x02\x03",
            "Everything I've said is just based on analysing\x01",
            "what you did until now and on objective facts.\x02\x03",
            "#00600FBesides, unless we resolve this incident\x01",
            "and seize the entire truth of it, we won't\x01",
            "be able to proceed to what comes next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Ha ha. As always, he doesn't\x01",
            "say openly what he really feels...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        "#5P#00601F...What's that grin on your face?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00011FN-No, it's nothing!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B9B")
    Jump("loc_17C4A")

    label("loc_17B9B")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Dudley learned\x01",
            "Hearts of Iron II.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Dudley's "Hearts of Iron"\x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)

    label("loc_17C4A")

    OP_E0(0x24, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1D9, 1)
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x14, 0x0)
    EventEnd(0x5)
    Return()

    # Function_53_17214 end

    def Function_54_17C5D(): pass

    label("Function_54_17C5D")

    EventBegin(0x0)
    Fade(500)
    OP_68(96790, 1200, -101940, 0)
    MoveCamera(48, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 96960, 0, -100830, 180)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x101, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17D34")
    Jump("loc_17D7E")

    label("loc_17D34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17D54")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17D7E")

    label("loc_17D54")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17D74")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17D7E")

    label("loc_17D74")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D7E")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about the barrier to Rixia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            "#12P#10704F...It looks like\x01",
            "I need to go.\x02\x03",
            "#10701FAs someone who shares fate with "her"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Say, Rixia.\x02\x03",
            "#00001FIf possible, I'd like you\x01",
            "to leave her to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12P#10706F──No.\x02\x03",
            "#10708FIn a way, both she and myself are\x01",
            "the product of similar circumstances.\x02\x03",
            "I need to find the path I'll\x01",
            "take going forward as well...\x02\x03",
            "#10701FShe and I must\x01",
            "confront each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Understood.\x02\x03",
            "#00001FLet's go once we're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 4)
    SetChrSubChip(0xD, 0x0)
    EventEnd(0x5)
    Return()

    # Function_54_17C5D end

    def Function_55_17FAA(): pass

    label("Function_55_17FAA")

    EventBegin(0x0)
    Fade(500)
    OP_68(101090, 1000, -93870, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100220, 0, -93940, 90)
    SetChrPos(0xA, 101370, 150, -94090, 270)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about the barrier to Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10404FHmph... I see.\x02\x03",
            "#10408F...Honestly. Why does he\x01",
            "have to obsess over\x01",
            "a blockhead like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10401FIt seems like "he" wants\x01",
            "to settle things with me.\x02\x03",
            "#10403FLloyd, can I join\x01",
            "the search party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, got it.\x02\x03",
            "#00000FLet's go once we're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 0)
    SetChrPos(0xA, 101790, 150, -93960, 90)
    EventEnd(0x5)
    Return()

    # Function_55_17FAA end

    def Function_56_1817E(): pass

    label("Function_56_1817E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3010, -500, 6090, 0)
    MoveCamera(46, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -3520, -1500, 5560, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18255")
    Jump("loc_1829F")

    label("loc_18255")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18275")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1829F")

    label("loc_18275")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18295")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1829F")

    label("loc_18295")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1829F")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_93(0x8, 0x104, 0x0)
    EndChrThread(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00200FMr. Abbas just showed\x01",
            "me how to use the\x01",
            "terminal, but...\x02\x03",
            "#00203FIt seems like the Merkabah's systems\x01",
            "were made by the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh... Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FYes, there is no mistake.\x02\x03",
            "#00203FIn the past, I spotted some people of\x01",
            "the Church at the Foundation's HQ...\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1848D")
    Jump("loc_184D7")

    label("loc_1848D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_184AD")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_184D7")

    label("loc_184AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_184CD")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_184D7")

    label("loc_184CD")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_184D7")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FMost likely, the Foundation and Church\x01",
            "have been cooperating ever since...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F...Unofficially, though.\x02\x03",
            "This Merkabah was formerly the\x01",
            ""Heaven's Wheel", a flight-\x01",
            "capable artifact vehicle...\x02\x03",
            "After the orbal revolution, with the help of the\x01",
            "Foundation, we used the "Heaven's Wheel"\x01",
            "mechanism, giving it its current form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F"Heaven's Wheel"... \x01",
            "It's the name Zeit muttered when\x01",
            "he first saw the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FI'll tell you this while I'm at it.\x01",
            "The Church also participates in\x01",
            "development of tactical orbments.\x02\x03",
            "The "Orbal Magic"(Arts) you all use\x01",
            "were formerly used through a\x01",
            "skill called "Thaumaturgy".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F...I think you already know this,\x01",
            "but this is a strictly informal matter.\x01",
            "Do not leak this information outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, of course we know that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00200FI understand as well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    OP_93(0x8, 0x13B, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_56_1817E end

    SaveToFile()

Try(main)
