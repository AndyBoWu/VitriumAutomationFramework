class VariableClass:

    # Login Credential: make sure

    AndyEmail           = "andyw@vitrium.com"
    AndyPassword        = "admin"

    # SUPER ADMIN
    addAccountBtn = r"button[data-bound-action='add-account']"
    accountName = r"input[id$='Name']"
    CustomEipUrl = r"http://auth-staging.vitrium.com/api/2.0"



    userName            = "andyent"
    passWord            = "test123"

    forgotPwd           = "Forgot Your Password?"
    requestBtn          = r"//button[@data-action='request']"
    learnMoreBtn        = r"Learn More"

    # Shared Web Elements
    saveBtn             = r"//button[@data-action='save']"


    # Jump to different places
    contentUrl          = r"http://auth-staging.vitrium.com/secure/documents"
    stagingUrl          = r"http://auth-staging.vitrium.com/"
    policyUrl           = r"http://auth-staging.vitrium.com/secure/sharesettings"
    dashboardUrl        = r"http://auth-staging.vitrium.com/secure/dashboard"
    watermarkUrl        = r"http://auth-staging.vitrium.com/secure/watermarks"
    drmPolicyUrl        = r"http://auth-staging.vitrium.com/secure/sharesettings"
    contentSettingsUrl  = r"http://auth-staging.vitrium.com/secure/documentsettings"
    usersUrl            = r"http://auth-staging.vitrium.com/secure/readers"
    loginFormUrl        = r"http://auth-staging.vitrium.com/secure/forms"


    # Content Tab
    addContentBtn       = r"button[data-bound-action='add-document']"
    uploadContentBtn     = r"//*[@title='Browse local file system ...']"


    # DRM Policy
    addDRMBtn           = r"//button[@data-bound-action='add-sharesettings']"
    policyNameField     = r"//*[contains(@id, 'Name')]"

    # Watermark
    addCSBtn            = r"button[data-bound-action='add-documentsettings']"
    addWmBtn            = r"button[data-bound-action='add-watermark']"
    watermarkText       = r"//input[@placeholder='e.g. Unlocked by John Smith']"
    watermarkName       = r"input[id$='Name']"


    # USERS Tab
    addSingleUserBtn    = r"button[data-bound-action='add-reader']"
    addMultipleUserBtn  = r"button[data-bound-action='import-readers']"
    exportUsers         = r"button[data-bound-action='export-readers']"
    uName               = r"input[id$='Username']"
    uPassword           = r"input[id$='Password']"
    uNotes              = r"textarea[id$='Notes']"
    uKey                = r"input[id$='ExternalKey']"
    uField              = r"input[id$='CustomField']"
    addOneMoreUserBtn   = r"button[data-bound-action='add-user-form']"
    mPassword           = r"input[id$='Password']"

    # Login Forms
    addLoginFormBtn     = r"button[data-bound-action='add-form']"
    uploadLoginForm     = r"//*[@title='Browse local file system ...']"
