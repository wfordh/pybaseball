from .fangraphs_stats_base import FangraphsStatsBase


class FangraphsBattingStats(FangraphsStatsBase):
    COMMON                            = 'c'
    LINE_BREAK                        = '-1'
    NAME                              = '0'
    TEAM                              = '1'
    SEASON                            = '2'
    AGE                               = '3'
    G                                 = '4'
    GAMES                             = G
    AB                                = '5'
    AT_BATS                           = AB
    PA                                = '6'
    PLATE_APPEARANCES                 = PA
    H                                 = '7'
    HITS                              = H
    SINGLES                           = '8'  # 1B
    DOUBLES                           = '9'  # 2B
    TRIPLES                           = '10' # 3B
    HR                                = '11'
    HOME_RUNS                         = HR
    R                                 = '12'
    RUNS                              = R
    RBI                               = '13'
    BB                                = '14'
    WALKS                             = BB
    IBB                               = '15'
    INTENTIONAL_WALKS                 = IBB
    SO                                = '16'
    STRIKE_OUTS                       = SO
    HBP                               = '17'
    HIT_BY_PITCH                      = HBP
    SF                                = '18'
    SACRIFICE_FLY                     = SF
    SH                                = '19'
    SACRIFICE_HIT                     = SH
    GDP                               = '20'
    GROUNDED_DOUBLE_PLAY              = GDP
    SB                                = '21'
    STOLEN_BASES                      = SB
    CS                                = '22'
    CAUGHT_STEALING                   = CS
    AVG                               = '23'
    BATTING_AVERAGE                   = AVG
    GB                                = '24'
    GROUND_BALLS                      = GB
    FB                                = '25'
    FLY_BALLS                         = FB
    LD                                = '26' # ?
    IFFB                              = '27' # ?
    PITCHES                           = '28'
    BALLS                             = '29'
    STRIKES                           = '30'
    IFH                               = '31' # ? INFIELD_HITS?
    BU                                = '32' # ?
    BUH                               = '33' # ?
    BB_PCT                            = '34' # BB%
    WALK_PERCENTAGE                   = BB_PCT
    K_PCT                             = '35' # K%
    STRIKE_PERCENTAGE                 = K_PCT
    BB_K                              = '36'
    WALKS_PER_STRIKOUT                = BB_K # BB/K
    OBP                               = '37'
    ON_BASE_PERCENTAGE                = OBP
    SLG                               = '38'
    SLUGGING                          = SLG
    OPS                               = '39'
    ON_BASE_PLUS_SLUGGING             = OPS
    ISO                               = '40'
    ISOLATED_POWER                    = ISO
    BABIP                             = '41'
    BATTING_AVERAGE_FOR_BALLS_IN_PLAY = BABIP
    GB_FB                             = '42' # GB/FB
    GROUND_BALLS_PER_FLY_BALL         = GB_FB
    LD_PCT                            = '43' # LD% ?
    GB_PCT                            = '44' # GB%
    GROUND_BALL_PERCENTAGE            = GB_PCT
    FB_PCT                            = '45'# FB%
    FLY_BALL_PERCENTAGE               = FB_PCT
    IFFB_PCT                          = '46' # IFFB% ?
    HR_FB                             = '47' # HR/FB
    HOME_RUNS_PER_FLY_BALL            = HR_FB
    IFH_PCT                           = '48' # IFH%
    INFIELD_HIT_PERCENTAGE            = IFH_PCT
    BUH_PCT                           = '49' # BUH% ?
    WOBA                              = '50'
    WEIGHTED_ON_BASE_AVERAGE          = WOBA
    WRAA                              = '51' # ?
    WRC                               = '52'
    WEIGHTED_RUNS_CREATED             = WRC
    BAT                               = '53' # ?
    FLD                               = '54' # ?
    REP                               = '55' # ?
    POS                               = '56' # ?
    RAR                               = '57'
    RUNS_ABOVE_REPLACEMENT            = RAR
    WAR                               = '58'
    WINS_ABOVE_REPLACEMENT            = WAR
    DOL                               = '59'
    DOLLARS_VALUE                     = DOL
    SPD                               = '60' # SPEED?
    WRC_PLUS                          = '61' # wRC+
    WEIGHTED_RUNS_CREATED_PLUS        = WRC_PLUS
    WPA                               = '62'
    WIN_PROBABILITY_ADDED             = WPA
    NEGATIVE_WPA                      = '63' # -WPA
    NEGATIVE_WIN_PROBABILITY_ADDED    = NEGATIVE_WPA
    POSITIVE_WPA                      = '64' # +WPA
    POSITIVE_WIN_PROBABILITY_ADDED    = POSITIVE_WPA
    RE24                              = '65' # ?
    REW                               = '66' # ?
    PLI                               = '67' # ?
    PHLI                              = '68' # ?
    PH                                = '69' # ?
    WPA_LI                            = '70' # WPA/LI ?
    CLUTCH                            = '71'
    FB_PCT_2                          = '72' # FB% ? Not sure the difference between this and the one in position 45
    FBV                               = '73' # ?
    SL_PCT                            = '74' # SL% ?
    SLV                               = '75' # ?
    CT_PCT                            = '76' # CT% ?
    CTV                               = '77'
    CB_PCT                            = '78' # CB% ?
    CBV                               = '79' # ?
    CH_PCT                            = '80' # CH% ?
    CHV                               = '81' # ?
    SF_PCT                            = '82' # SF% ?
    SFV                               = '83' # ?
    KN_PCT                            = '84' # KN% ?
    KNV                               = '85' # ?
    XX_PCT                            = '86' # XX% ?
    PO_PCT                            = '87' # PO% ?
    WFB                               = '88' # ?
    WSL                               = '89' # ?
    WCT                               = '90' # ?
    WCB                               = '91' # ?
    WCH                               = '92' # ?
    WSF                               = '93' # ?
    WKN                               = '94' # ?
    WFB_C                             = '95' # wFB/C ?
    WSL_C                             = '96' # wSL/C ?
    WCT_C                             = '97' # wCT/C ?
    WCB_C                             = '98' # wCB/C ?
    WCH_C                             = '99' # wCH/C ?
    WSF_C                             = '100' # wSF/C ?
    WKN_C                             = '101' # wKN/C ?
    OSWING_PCT                        = '102' # O-Swing% ?
    ZSWING_PCT                        = '103' # Z-Swing% ?
    SWING_PCT                         = '104' # Swing% ?
    OCONTACT_PCT                      = '105' # O-Contact% ?
    ZCONTACT_PCT                      = '106' # Z-Contact% ?
    CONTACT_PCT                       = '107' # Contact% ?
    ZONE_PCT                          = '108' # Zone% ?
    FSTRIKE_PCT                       = '109' # F-Strike% ?
    SWSTR_PCT                         = '110' # SwStr% SWINGING_STRIKE_PERCENTAGE?
    BSR                               = '111' # ?
    FA_PCT_PFX                        = '112' # 'FA% (pfx)' ?
    FT_PCT_PFX                        = '113' # 'FT% (pfx)' ?
    FC_PCT_PFX                        = '114' # 'FC% (pfx)' ?
    FS_PCT_PFX                        = '115' # 'FS% (pfx)' ?
    FO_PCT_PFX                        = '116' # 'FO% (pfx)' ?
    SI_PCT_PFX                        = '117' # 'SI% (pfx)' ?
    SL_PCT_PFX                        = '118' # 'SL% (pfx)' ?
    CU_PCT_PFX                        = '119' # 'CU% (pfx)' ?
    KC_PCT_PFX                        = '120' # 'KC% (pfx)' ?
    EP_PCT_PFX                        = '121' # 'EP% (pfx)' ?
    CH_PCT_PFX                        = '122' # 'CH% (pfx)' ?
    SC_PCT_PFX                        = '123' # 'SC% (pfx)' ?
    KN_PCT_PFX                        = '124' # 'KN% (pfx)' ?
    UN_PCT_PFX                        = '125' # 'UN% (pfx)' ?
    VFA_PFX                           = '126' # 'vFA (pfx)' ?
    VFT_PFX                           = '127' # 'vFT (pfx)' ?
    VFC_PFX                           = '128' # 'vFC (pfx)' ?
    VFS_PFX                           = '129' # 'vFS (pfx)' ?
    VFO_PFX                           = '130' # 'vFO (pfx)' ?
    VSI_PFX                           = '131' # 'vSI (pfx)' ?
    VSL_PFX                           = '132' # 'vSL (pfx)' ?
    VCU_PFX                           = '133' # 'vCU (pfx)' ?
    VKC_PFX                           = '134' # 'vKC (pfx)' ?
    VEP_PFX                           = '135' # 'vEP (pfx)' ?
    VCH_PFX                           = '136' # 'vCH (pfx)' ?
    VSC_PFX                           = '137' # 'vSC (pfx)' ?
    VKN_PFX                           = '138' # 'vKN (pfx)' ?
    FA_X_PFX                          = '139' # 'FA-X (pfx)' ?
    FT_X_PFX                          = '140' # 'FT-X (pfx)' ?
    FC_X_PFX                          = '141' # 'FC-X (pfx)' ?
    FS_X_PFX                          = '142' # 'FS-X (pfx)' ?
    FO_X_PFX                          = '143' # 'FO-X (pfx)' ?
    SI_X_PFX                          = '144' # 'SI-X (pfx)' ?
    SL_X_PFX                          = '145' # 'SL-X (pfx)' ?
    CU_X_PFX                          = '146' # 'CU-X (pfx)' ?
    KC_X_PFX                          = '147' # 'KC-X (pfx)' ?
    EP_X_PFX                          = '148' # 'EP-X (pfx)' ?
    CH_X_PFX                          = '149' # 'CG-X (pfx)' ?
    SC_X_PFX                          = '150' # 'SC-X (pfx)' ?
    KN_X_PFX                          = '151' # 'KN-X (pfx)' ?
    FA_Z_PFX                          = '152' # 'FA-Z (pfx)' ?
    FT_Z_PFX                          = '153' # 'FT-Z (pfx)' ?
    FC_Z_PFX                          = '154' # 'FC-Z (pfx)' ?
    FS_Z_PFX                          = '155' # 'FS-Z (pfx)' ?
    FO_Z_PFX                          = '156' # 'FO-Z (pfx)' ?
    SI_Z_PFX                          = '157' # 'SI-Z (pfx)' ?
    SL_Z_PFX                          = '158' # 'SL-Z (pfx)' ?
    CU_Z_PFX                          = '159' # 'CU-Z (pfx)' ?
    KC_Z_PFX                          = '160' # 'KC-Z (pfx)' ?
    EP_Z_PFX                          = '161' # 'EP-Z (pfx)' ?
    CH_Z_PFX                          = '162' # 'CH-Z (pfx)' ?
    SC_Z_PFX                          = '163' # 'SC-Z (pfx)' ?
    KN_Z_PFX                          = '164' # 'KN-Z (pfx)' ?
    WFA_PFX                           = '165' # 'wFA (pfx)' ?
    WFT_PFX                           = '166' # 'wFT (pfx)' ?
    WFC_PFX                           = '167' # 'wFC (pfx)' ?
    WFS_PFX                           = '168' # 'wFS (pfx)' ?
    WFO_PFX                           = '169' # 'wFO (pfx)' ?
    WSI_PFX                           = '170' # 'wSI (pfx)' ?
    WSL_PFX                           = '171' # 'wSL (pfx)' ?
    WCU_PFX                           = '172' # 'wCU (pfx)' ?
    WKC_PFX                           = '173' # 'wKC (pfx)' ?
    WEP_PFX                           = '174' # 'wEP (pfx)' ?
    WCH_PFX                           = '175' # 'wCH (pfx)' ?
    WSC_PFX                           = '176' # 'wSC (pfx)' ?
    WKN_PFX                           = '177' # 'wKN (pfx)' ?
    WFA_C_PFX                         = '178' # 'wFA/C (pfx)' ?
    WFT_C_PFX                         = '179' # 'wFT/C (pfx)' ?
    WFC_C_PFX                         = '180' # 'wFC/C (pfx)' ?
    WFS_C_PFX                         = '181' # 'wFS/C (pfx)' ?
    WFO_C_PFX                         = '182' # 'wFO/C (pfx)' ?
    WSI_C_PFX                         = '183' # 'wSI/C (pfx)' ?
    WSL_C_PFX                         = '184' # 'wSL/C (pfx)' ?
    WCU_C_PFX                         = '185' # 'wCU/C (pfx)' ?
    WKC_C_PFX                         = '186' # 'wKC/C (pfx)' ?
    WEP_C_PFX                         = '187' # 'wEP/C (pfx)' ?
    WCH_C_PFX                         = '188' # 'wCH/C (pfx)' ?
    WSC_C_PFX                         = '189' # 'wSC/C (pfx)' ?
    WKN_C_PFX                         = '190' # 'wKN/C (pfx)' ?
    OSWING_PCT_PFX                    = '191' # 'O-Swing% (pfx)' ?
    ZSWING_PCT_PFX                    = '192' # 'Z-Swing% (pfx)' ?
    SWING_PCT_PFX                     = '193' # 'Swing% (pfx)' ?
    OCONTACT_PCT_PFX                  = '194' # 'O-Contact% (pfx)' ?
    ZCONTACT_PCT_PFX                  = '195' # 'Z-Contact% (pfx)' ?
    CONTACT_PCT_PFX                   = '196' # 'Contact% (pfx)' ?
    ZONE_PCT_PFX                      = '197' # 'Zone% (pfx)' ?
    PACE                              = '198' # ?
    DEF                               = '199' # ?
    WSB                               = '200' # ?
    UBR                               = '201' # ?
    AGE_RNG                           = '202' # 'Age Rng' ?
    OFF                               = '203' # ?
    LG                                = '204' # Lg ?
    wGDP                              = '205'# wGDP ? WEIGHTED_GROUNDED_DOUBLE_PLAY?
    PULL_PCT                          = '206' # Pull% ?
    CENT_PCT                          = '207' # Cent% ?
    OPPO_PCT                          = '208' # Oppo% ?
    SOFT_PCT                          = '209' # Soft% ?
    MED_PCT                           = '210' # Med% ?
    HARD_PCT                          = '211' # Hard% ?
    TTO_PCT                           = '212' # TTO% ?
    CH_PCT_PI                         = '213' # 'CH% (pi)' ?
    CS_PCT_PI                         = '214' # 'CS% (pi)' ?
    CU_PCT_PI                         = '215' # 'CU% (pi)' ?
    FA_PCT_PI                         = '216' # 'FA% (pi)' ?
    FC_PCT_PI                         = '217' # 'FC% (pi)' ?
    FS_PCT_PI                         = '218' # 'FS% (pi)' ?
    KN_PCT_PI                         = '219' # 'KN% (pi)' ?
    SB_PCT_PI                         = '220' # 'SB% (pi)' ?
    SI_PCT_PI                         = '221' # 'SI% (pi)' ?
    SL_PCT_PI                         = '222' # 'SL% (pi)' ?
    XX_PCT_PI                         = '223' # 'XX% (pi)' ?
    VCH_PI                            = '224' # 'vCH (pi)' ?
    VCS_PI                            = '225' # 'vCS (pi)' ?
    VCU_PI                            = '226' # 'vCU (pi)' ?
    VFA_PI                            = '227' # 'vFA (pi)' ?
    VFC_PI                            = '228' # 'vFC (pi)' ?
    VFS_PI                            = '229' # 'vFS (pi)' ?
    VKN_PI                            = '230' # 'vKN (pi)' ?
    VSB_PI                            = '231' # 'vSB (pi)' ?
    VSI_PI                            = '232' # 'vSI (pi)' ?
    VSL_PI                            = '233' # 'vSL (pi)' ?
    VXX_PI                            = '234' # 'vXX (pi)' ?
    CH_X_PI                           = '235' # 'CH-X (pi)' ?
    CS_X_PI                           = '236' # 'CS-X (pi)' ?
    CU_X_PI                           = '237' # 'CU-X (pi)' ?
    FA_X_PI                           = '238' # 'FA-X (pi)' ?
    FC_X_PI                           = '239' # 'FC-X (pi)' ?
    FS_X_PI                           = '240' # 'FS-X (pi)' ?
    KN_X_PI                           = '241' # 'KN-X (pi)' ?
    SB_X_PI                           = '242' # 'SB-X (pi)' ?
    SI_X_PI                           = '243' # 'SI-X (pi)' ?
    SL_X_PI                           = '244' # 'SL-X (pi)' ?
    XX_X_PI                           = '245' # 'XX-X (pi)' ?
    CH_Z_PI                           = '246' # 'CH-Z (pi)' ?
    CS_Z_PI                           = '247' # 'CS-Z (pi)' ?
    CU_Z_PI                           = '248' # 'CU-Z (pi)' ?
    FA_Z_PI                           = '249' # 'FA-Z (pi)' ?
    FC_Z_PI                           = '250' # 'FC-Z (pi)' ?
    FS_Z_PI                           = '251' # 'FS-Z (pi)' ?
    KN_Z_PI                           = '252' # 'KN-Z (pi)' ?
    SB_Z_PI                           = '253' # 'SB-Z (pi)' ?
    SI_Z_PI                           = '254' # 'SI-Z (pi)' ?
    SL_Z_PI                           = '255' # 'SL-Z (pi)' ?
    XX_Z_PI                           = '256' # 'XX-Z (pi)' ?
    WCH_PI                            = '257' # 'wCH (pi)' ?
    WCS_PI                            = '258' # 'wCS (pi)' ?
    WCU_PI                            = '259' # 'wCU (pi)' ?
    WFA_PI                            = '260' # 'wFA (pi)' ?
    WFC_PI                            = '261' # 'wFC (pi)' ?
    WFS_PI                            = '262' # 'wFS (pi)' ?
    WKN_PI                            = '263' # 'wKN (pi)' ?
    WSB_PI                            = '264' # 'wSB (pi)' ?
    WSI_PI                            = '265' # 'wSI (pi)' ?
    WSL_PI                            = '266' # 'wSL (pi)' ?
    WXX_PI                            = '267' # 'wXX (pi)' ?
    WCH_C_PI                          = '268' # 'wCH/C (pi)' ?
    WCS_C_PI                          = '269' # 'wCS/C (pi)' ?
    WCU_C_PI                          = '270' # 'wCU/C (pi)' ?
    WFA_C_PI                          = '271' # 'wFA/C (pi)' ?
    WFC_C_PI                          = '272' # 'wFC/C (pi)' ?
    WFS_C_PI                          = '273' # 'wFS/C (pi)' ?
    WKN_C_PI                          = '274' # 'wKN/C (pi)' ?
    WSB_C_PI                          = '275' # 'wSB/C (pi)' ?
    WSI_C_PI                          = '276' # 'wSI/C (pi)' ?
    WSL_C_PI                          = '277' # 'wSL/C (pi)' ?
    WXX_C_PI                          = '278' # 'wXX/C (pi)' ?
    OSWING_PCT_PI                     = '279' # 'O-Swing% (pfx)' ?
    ZSWING_PCT_PI                     = '280' # 'Z-Swing% (pfx)' ?
    SWING_PCT_PI                      = '281' # 'Swing% (pfx)' ?
    OCONTACT_PCT_PI                   = '282' # 'O-Contact% (pfx)' ?
    ZCONTACT_PCT_PI                   = '283' # 'Z-Contact% (pfx)' ?
    CONTACT_PCT_PI                    = '284' # 'Contact% (pfx)' ?
    ZONE_PCT_PI                       = '285' # 'Zone% (pfx)' ?
    PACE_PI                           = '286' # 'Pace (pi)'?
    FRM                               = '287' # ?
    AVG_PLUS                          = '288' # AVG+ ?
    BB_PCT_PLUS                       = '289' # BB%+ ?
    K_PCT_PLUS                        = '290' # K%+ ?
    OBP_PLUS                          = '291' # OBP+ ?
    SLG_PLUS                          = '292' # SLG+ ?
    ISO_PLUS                          = '293' # ISO+ ?
    BABIP_PLUS                        = '294' # BABIP+ ?
    LD_PLUS_PCT                       = '295' # LD+% ?
    GB_PCT_PLUS                       = '296' # GB%+ ?
    FB_PCT_PLUS                       = '297' # FB%+ ?
    HR_FB_PCT_PLUS                    = '298' # HR/FB%+ ?
    PULL_PCT_PLUS                     = '299' # Pull%+ ?
    CENT_PCT_PLUS                     = '300' # Cent%+ ?
    OPPO_PCT_PLUS                     = '301' # Oppo%+ ?
    SOFT_PCT_PLUS                     = '302' # Soft%+ ?
    MED_PCT_PLUS                      = '303' # Med %+ ?
    HARD_PCT_PLUS                     = '304' # Hard%+ ?
    EV                                = '305' # ?
    LA                                = '306' # ?
    BARRELS                           = '307' # ?
    BARREL_PCT                        = '308' # Barrel% ?
    MAXEV                             = '309' # maxEV ?
    HARDHIT                           = '310' # ?
    HARDHIT_PCT                       = '311' # HardHit% ?
    EVENTS                            = '312' # ?
