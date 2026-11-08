from findmy import AppleAccount, LocalAnisetteProvider, LoginState, TrustedDeviceSecondFactorMethod, SmsSecondFactorMethod

ani = LocalAnisetteProvider(libs_path="ani_libs.bin")
account = AppleAccount(ani)

state = account.login(username="your_apple_id", password="your_password")

if state == LoginState.LOGGED_IN:
    print("Logged in successfully!")
if state == LoginState.REQUIRE_2FA:  # Account requires 2FA
    methods = account.get_2fa_methods()

    for i, method in enumerate(methods):
        if isinstance(method, TrustedDeviceSecondFactorMethod):
            print(f"{i} - Trusted Device")
        elif isinstance(method, SmsSecondFactorMethod):
            print(f"{i} - SMS ({method.phone_number})")

    # example output:
    # 0 - Trusted Device
    # 1 - SMS (+31 •• ••••••55)
    # 2 - SMS (+31 •• ••••••32)