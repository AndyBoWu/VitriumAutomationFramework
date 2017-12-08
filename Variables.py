class VariableClass:

    stagingUrl = r"http://auth-staging.vitrium.com/"
    policyUrl = r"http://auth-staging.vitrium.com/secure/sharesettings"
    dashboardUrl = r"http://auth-staging.vitrium.com/secure/dashboard"
    watermarkUrl = r"http://auth-staging.vitrium.com/secure/watermarks"
    drmPolicyUrl = r"http://auth-staging.vitrium.com/secure/sharesettings"


    # DRM Policy
    addDRMBtn    = r"//button[@data-bound-action='add-sharesettings']"
    policyNameField   = r"//*[contains(@id, 'Name')]"

    # Watermark
    addWmBtn      = r"button[data-bound-action='add-watermark']"
    saveBtn       = r"//button[@data-action='save']"
    watermarkText = r"//input[@placeholder='e.g. Unlocked by John Smith']"
    watermarkName = r"input[id$='Name']"





